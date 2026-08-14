"""CLI runner for KMPC-138 BI/.15 local 45-s exact exception.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import traceback

from baseScripts.p5_general_synchronous import (
    c3_zero_variant_parallel_v9_bi_k0p15_fuel_order_roundtrip as c3,
)


RUN_ID = "KMPC-138"
EXPECTED_BASE_SHA256 = (
    "489ED57D2F874CAC60E7733050C7DB4E8D59AABAD197827965F6322B80515D0D"
)
COEFFICIENT_MAX_RUNTIME_SECONDS = 4.8
EXACT_MAX_RUNTIME_SECONDS = 45.0
PARENT_TOTAL_WALL_LIMIT_SECONDS = 49.0
STAGE_PROCESS_OVERHEAD_SECONDS = 0.75
PARENT_MERGE_RESERVE_SECONDS = 0.75
SHARD_CHOICES = tuple(c3.shard_key(*shard) for shard in c3.SHARDS)
VARIANT_CHOICES = ("gamma0", "af0")
c3.RUN_ID = RUN_ID


def output_name(mode: str, k_mpc: float) -> str:
    if (mode, k_mpc) != ("BI", 0.15):
        raise ValueError("KMPC-138 is frozen to BI/k=0.15")
    return (
        "RUN_KMPC_138_P5_3G7_C3_BI_K0p15_ZERO_VARIANT_PAIR_"
        "LOCAL_45S_HP_M1_EXACT_RESUME.json"
    )


def failure_name(mode: str, k_mpc: float) -> str:
    return output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Run BI/.15 C3 through four 4.8-s binary64 coefficient shards "
            "followed by two parallel local 45-s decimal80 exact shards."
        )
    )
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--smoke", action="store_true")
    action.add_argument("--audit", action="store_true")
    action.add_argument(
        "--worker-coefficient-shard", choices=SHARD_CHOICES, help=argparse.SUPPRESS
    )
    action.add_argument(
        "--worker-coefficient-smoke-shard",
        choices=SHARD_CHOICES,
        help=argparse.SUPPRESS,
    )
    action.add_argument(
        "--worker-exact-variant", choices=VARIANT_CHOICES, help=argparse.SUPPRESS
    )
    action.add_argument(
        "--worker-exact-smoke-variant",
        choices=VARIANT_CHOICES,
        help=argparse.SUPPRESS,
    )
    parser.add_argument("--mode", choices=("BI",), required=True)
    parser.add_argument("--k", type=float, choices=(0.15,), required=True)
    parser.add_argument("--result-dir", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--handoff-output", type=Path, help=argparse.SUPPRESS)
    parser.add_argument("--handoff-input", type=Path, help=argparse.SUPPRESS)
    parser.add_argument("--handoff-sha256", help=argparse.SUPPRESS)
    parser.add_argument("--handoff-file-sha256", help=argparse.SUPPRESS)
    parser.add_argument(
        "--max-runtime-seconds",
        type=float,
        default=COEFFICIENT_MAX_RUNTIME_SECONDS,
    )
    parser.add_argument(
        "--exact-max-runtime-seconds",
        type=float,
        default=EXACT_MAX_RUNTIME_SECONDS,
    )
    return parser


def _native(value: object) -> object:
    if isinstance(value, dict):
        return {str(key): _native(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_native(item) for item in value]
    if hasattr(value, "item") and callable(getattr(value, "item")):
        return _native(value.item())
    return value


def _write_immutable_json(path: Path, payload: dict[str, object]) -> None:
    if path.exists():
        raise FileExistsError(f"immutable output already exists: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    if temporary.exists():
        raise FileExistsError(f"stale temporary output exists: {temporary}")
    try:
        with temporary.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(_native(payload), handle, indent=2, sort_keys=True, allow_nan=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        temporary.replace(path)
    except Exception:
        if temporary.exists():
            temporary.unlink()
        raise


def _parse_shard(value: str) -> tuple[str, str]:
    parts = tuple(value.split("/"))
    if len(parts) != 2 or parts not in c3.SHARDS:
        raise ValueError(f"invalid shard {value}")
    return parts


def _result_dir(args: argparse.Namespace, script_path: Path) -> Path:
    return (
        args.result_dir.resolve()
        if args.result_dir is not None
        else (script_path.parent / "results" / "k_mpc_005").resolve()
    )


def _record(process: subprocess.Popen[str]) -> dict[str, object]:
    stdout, stderr = process.communicate()
    payload: object = None
    parse_error = ""
    if stdout.strip():
        try:
            payload = json.loads(stdout)
        except json.JSONDecodeError as exc:
            parse_error = f"{type(exc).__name__}: {exc}"
    return {
        "returncode": process.returncode,
        "stdout": stdout,
        "stderr": stderr,
        "payload": payload,
        "parse_error": parse_error,
    }


def _run_commands(
    commands: dict[str, list[str]],
    wall_limit_seconds: float,
) -> dict[str, dict[str, object]]:
    environment = dict(os.environ)
    environment.update({
        "OMP_NUM_THREADS": "1",
        "OPENBLAS_NUM_THREADS": "1",
        "MKL_NUM_THREADS": "1",
    })
    processes = {
        key: subprocess.Popen(
            command,
            cwd=str(Path(__file__).resolve().parent.parent),
            env=environment,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
        )
        for key, command in commands.items()
    }
    started = time.monotonic()
    records: dict[str, dict[str, object]] = {}
    try:
        for key, process in processes.items():
            remaining = wall_limit_seconds - (time.monotonic() - started)
            if remaining <= 0.0:
                raise subprocess.TimeoutExpired(process.args, 0.0)
            stdout, stderr = process.communicate(timeout=remaining)
            payload: object = None
            parse_error = ""
            if stdout.strip():
                try:
                    payload = json.loads(stdout)
                except json.JSONDecodeError as exc:
                    parse_error = f"{type(exc).__name__}: {exc}"
            records[key] = {
                "returncode": process.returncode,
                "stdout": stdout,
                "stderr": stderr,
                "payload": payload,
                "parse_error": parse_error,
            }
    except subprocess.TimeoutExpired:
        for process in processes.values():
            if process.poll() is None:
                process.kill()
        for key, process in processes.items():
            if key not in records:
                records[key] = _record(process)
                if records[key]["returncode"] != 0:
                    records[key]["parse_error"] = "STAGE_WALL_TIMEOUT"
    return records


def _base_command(
    script_path: Path,
    action: str,
    action_value: str,
    mode: str,
    k_mpc: float,
    result_dir: Path,
    max_runtime_seconds: float,
) -> list[str]:
    return [
        sys.executable,
        str(script_path),
        action,
        action_value,
        "--mode",
        mode,
        "--k",
        str(k_mpc),
        "--result-dir",
        str(result_dir),
        "--max-runtime-seconds",
        str(max_runtime_seconds),
    ]


def _coefficient_commands(
    script_path: Path,
    mode: str,
    k_mpc: float,
    result_dir: Path,
    max_runtime_seconds: float,
    smoke: bool,
    handoff_dir: Path | None = None,
) -> dict[str, list[str]]:
    action = (
        "--worker-coefficient-smoke-shard"
        if smoke
        else "--worker-coefficient-shard"
    )
    commands: dict[str, list[str]] = {}
    for variant, level in c3.SHARDS:
        key = c3.shard_key(variant, level)
        command = _base_command(
            script_path,
            action,
            key,
            mode,
            k_mpc,
            result_dir,
            max_runtime_seconds,
        )
        if not smoke and level == "audit":
            if handoff_dir is None:
                raise RuntimeError("KMPC-138 handoff directory missing")
            command.extend([
                "--handoff-output",
                str(handoff_dir / f"{variant}_audit.json"),
            ])
        commands[key] = command
    return commands


def _exact_commands(
    script_path: Path,
    mode: str,
    k_mpc: float,
    result_dir: Path,
    max_runtime_seconds: float,
    smoke: bool,
    coefficient_payloads: dict[str, dict[str, object]] | None = None,
    handoff_dir: Path | None = None,
) -> dict[str, list[str]]:
    action = (
        "--worker-exact-smoke-variant" if smoke else "--worker-exact-variant"
    )
    commands: dict[str, list[str]] = {}
    for variant in VARIANT_CHOICES:
        command = _base_command(
            script_path,
            action,
            variant,
            mode,
            k_mpc,
            result_dir,
            max_runtime_seconds,
        )
        if not smoke:
            if coefficient_payloads is None or handoff_dir is None:
                raise RuntimeError("KMPC-138 exact command handoff inputs missing")
            summary = coefficient_payloads[f"{variant}/audit"][
                "exact_boundary_handoff"
            ]
            command.extend([
                "--handoff-input",
                str(handoff_dir / f"{variant}_audit.json"),
                "--handoff-sha256",
                summary["handoff_sha256"],
                "--handoff-file-sha256",
                summary["handoff_file_sha256"],
            ])
        commands[variant] = command
    return commands


def _successful_payloads(
    records: dict[str, dict[str, object]],
) -> dict[str, dict[str, object]]:
    payloads: dict[str, dict[str, object]] = {}
    for key, record in records.items():
        payload = record.get("payload")
        if record.get("returncode") == 0 and isinstance(payload, dict):
            payloads[key] = payload
    return payloads


def _records_pass(records: dict[str, dict[str, object]], expected: int) -> bool:
    return len(_successful_payloads(records)) == expected


def _compact_records(records: dict[str, dict[str, object]]) -> dict[str, object]:
    return {
        key: {
            "returncode": record.get("returncode"),
            "stderr": record.get("stderr"),
            "parse_error": record.get("parse_error"),
        }
        for key, record in records.items()
    }


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    script_path = Path(__file__).resolve()
    base_path = Path(c3.__file__).resolve()
    observed_base_hash = c3.sha256_file(base_path)
    if observed_base_hash != EXPECTED_BASE_SHA256:
        raise RuntimeError(
            f"base SHA-256 mismatch: {observed_base_hash} != {EXPECTED_BASE_SHA256}"
        )
    result_dir = _result_dir(args, script_path)
    runner_hash = c3.sha256_file(script_path)

    if args.worker_coefficient_smoke_shard is not None:
        variant, level = _parse_shard(args.worker_coefficient_smoke_shard)
        payload = c3.run_worker_smoke(
            args.mode, args.k, variant, level, result_dir
        )
        print(json.dumps(_native(payload), sort_keys=True, allow_nan=False))
        return 0 if payload["pass"] is True else 2

    if args.worker_exact_smoke_variant is not None:
        payload = c3.run_exact_worker_smoke(
            args.mode, args.k, args.worker_exact_smoke_variant, result_dir
        )
        print(json.dumps(_native(payload), sort_keys=True, allow_nan=False))
        return 0 if payload["pass"] is True else 2

    if args.worker_coefficient_shard is not None:
        variant, level = _parse_shard(args.worker_coefficient_shard)
        payload = c3.run_support_worker(
            args.mode,
            args.k,
            variant,
            level,
            args.max_runtime_seconds,
            result_dir,
        )
        handoff = payload.pop("exact_boundary_handoff")
        if level == "audit":
            if args.handoff_output is None or not isinstance(handoff, dict):
                raise RuntimeError("KMPC-138 audit worker handoff output missing")
            handoff_path = args.handoff_output.resolve()
            canonical_hash = c3.handoff_hash(handoff)
            _write_immutable_json(handoff_path, handoff)
            payload["exact_boundary_handoff"] = {
                "identity": handoff["identity"],
                "variant_fuel_fingerprint": handoff[
                    "variant_fuel_fingerprint"
                ],
                "float_driver_capture": handoff["float_driver_capture"],
                "handoff_sha256": canonical_hash,
                "handoff_file_sha256": c3.sha256_file(handoff_path),
                "temporary_transport_not_published": True,
            }
        elif handoff is not None:
            raise RuntimeError("KMPC-138 accepted worker emitted audit handoff")
        else:
            payload["exact_boundary_handoff"] = None
        print(json.dumps(_native(payload), sort_keys=True, allow_nan=False))
        return 0

    if args.worker_exact_variant is not None:
        if (
            args.handoff_input is None
            or args.handoff_sha256 is None
            or args.handoff_file_sha256 is None
        ):
            raise RuntimeError("KMPC-138 exact worker handoff arguments missing")
        payload = c3.run_exact_worker(
            args.mode,
            args.k,
            args.worker_exact_variant,
            args.max_runtime_seconds,
            result_dir,
            args.handoff_input.resolve(),
            args.handoff_sha256,
            args.handoff_file_sha256,
        )
        print(json.dumps(_native(payload), sort_keys=True, allow_nan=False))
        return 0 if payload["technical_pass"] is True else 2

    if args.smoke:
        coefficient_records = _run_commands(
            _coefficient_commands(
                script_path,
                args.mode,
                args.k,
                result_dir,
                args.max_runtime_seconds,
                smoke=True,
            ),
            wall_limit_seconds=5.0,
        )
        exact_records = _run_commands(
            _exact_commands(
                script_path,
                args.mode,
                args.k,
                result_dir,
                args.max_runtime_seconds,
                smoke=True,
            ),
            wall_limit_seconds=3.0,
        )
        payload = c3.aggregate_smoke_shards(
            _successful_payloads(coefficient_records),
            _successful_payloads(exact_records),
        )
        payload["worker_process_records"] = {
            "coefficient_wave": _compact_records(coefficient_records),
            "exact_boundary_wave": _compact_records(exact_records),
        }
        payload["source_hashes"] = {
            "base": observed_base_hash,
            "runner": runner_hash,
        }
        print(json.dumps(_native(payload), indent=2, sort_keys=True, allow_nan=False))
        return 0 if (
            payload["pass"] is True
            and _records_pass(coefficient_records, 4)
            and _records_pass(exact_records, 2)
        ) else 2

    if args.max_runtime_seconds != COEFFICIENT_MAX_RUNTIME_SECONDS:
        raise ValueError("KMPC-138 coefficient limit must remain exactly 4.8 s")
    if args.exact_max_runtime_seconds != EXACT_MAX_RUNTIME_SECONDS:
        raise ValueError("KMPC-138 exact limit must remain exactly 45.0 s")
    expected_name = output_name(args.mode, args.k)
    output = (
        args.output.resolve()
        if args.output is not None
        else (result_dir / expected_name).resolve()
    )
    if output.parent != result_dir or output.name != expected_name:
        raise ValueError("official output must use the frozen name inside result-dir")
    if output.exists():
        raise FileExistsError(f"immutable output already exists: {output}")

    parent_started = time.monotonic()
    coefficient_records: dict[str, dict[str, object]] = {}
    exact_records: dict[str, dict[str, object]] = {}
    handoff_path: Path | None = None
    try:
        with tempfile.TemporaryDirectory(
            prefix="KMPC138_HANDOFF_", dir=result_dir
        ) as temporary_name:
            handoff_path = Path(temporary_name).resolve()
            coefficient_records = _run_commands(
                _coefficient_commands(
                    script_path,
                    args.mode,
                    args.k,
                    result_dir,
                    args.max_runtime_seconds,
                    smoke=False,
                    handoff_dir=handoff_path,
                ),
                wall_limit_seconds=min(
                    args.max_runtime_seconds + STAGE_PROCESS_OVERHEAD_SECONDS,
                    PARENT_TOTAL_WALL_LIMIT_SECONDS - PARENT_MERGE_RESERVE_SECONDS,
                ),
            )
            if not _records_pass(coefficient_records, 4):
                raise RuntimeError("KMPC-138 coefficient wave incomplete")
            coefficient_payloads = _successful_payloads(coefficient_records)
            remaining = (
                PARENT_TOTAL_WALL_LIMIT_SECONDS
                - PARENT_MERGE_RESERVE_SECONDS
                - (time.monotonic() - parent_started)
            )
            if remaining <= 0.0:
                raise TimeoutError("KMPC-138 no parent budget for exact wave")
            exact_records = _run_commands(
                _exact_commands(
                    script_path,
                    args.mode,
                    args.k,
                    result_dir,
                    args.exact_max_runtime_seconds,
                    smoke=False,
                    coefficient_payloads=coefficient_payloads,
                    handoff_dir=handoff_path,
                ),
                wall_limit_seconds=min(
                    args.exact_max_runtime_seconds
                    + STAGE_PROCESS_OVERHEAD_SECONDS,
                    remaining,
                ),
            )
            if not _records_pass(exact_records, 2):
                raise RuntimeError("KMPC-138 exact-boundary wave incomplete")
            exact_payloads = _successful_payloads(exact_records)
        temporary_removed = handoff_path is not None and not handoff_path.exists()
        if not temporary_removed:
            raise RuntimeError("KMPC-138 temporary handoff directory not removed")
        payload = c3.aggregate_shards(
            coefficient_payloads,
            exact_payloads,
            result_dir,
            parent_runtime_seconds=time.monotonic() - parent_started,
            temporary_handoffs_removed=temporary_removed,
        )
        payload["process_architecture"]["local_exact_runtime_exception"] = {
            "scope": "BI_K0p15_GAMMA0_AF0_EXACT_BOUNDARY_ONLY",
            "coefficient_worker_limit_seconds": COEFFICIENT_MAX_RUNTIME_SECONDS,
            "exact_worker_limit_seconds": EXACT_MAX_RUNTIME_SECONDS,
            "parent_total_wall_limit_seconds": PARENT_TOTAL_WALL_LIMIT_SECONDS,
            "historical_authority": "KMPC-112_RUNTIME_34p86_LIMIT_45",
            "equations_matrices_thresholds_changed": False,
        }
        if payload["pair_pass"]:
            payload["candidate_interpretation_not_verdict"] = (
                "PASS_C3_BI_K0P15_ZERO_PAIR_LOCAL_45S_"
                "HP_M1_EXACT_RESUME_CANDIDATE_ONLY"
            )
        if time.monotonic() - parent_started > PARENT_TOTAL_WALL_LIMIT_SECONDS:
            raise TimeoutError("KMPC-138 parent total wall limit exceeded")
        payload["source_hashes"]["runner"] = runner_hash
        _write_immutable_json(output, payload)
    except Exception as exc:
        failure = result_dir / failure_name(args.mode, args.k)
        failure_payload = {
            "run_id": RUN_ID,
            "execution_status": "TECHNICAL_FAILURE_NO_PHYSICS_VERDICT",
            "physics_verdict": "NONE_TECHNICAL_FAILURE",
            "authorship": {
                "theory_author": "Martin Jambor",
                "script_creator": "Codex (OpenAI)",
            },
            "identity": {
                "mode": args.mode,
                "k_Mpc_inverse": args.k,
                "physical_receipt": (
                    "BI_K0p15_local_45s_HP_M1_exact_resume"
                ),
            },
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            "traceback": traceback.format_exc(),
            "worker_process_records": {
                "coefficient_wave": _compact_records(coefficient_records),
                "exact_boundary_wave": _compact_records(exact_records),
            },
            "successful_worker_payloads": {
                "coefficient_wave": _successful_payloads(coefficient_records),
                "exact_boundary_wave": _successful_payloads(exact_records),
            },
            "temporary_handoff_directory_removed": bool(
                handoff_path is None or not handoff_path.exists()
            ),
            "source_hashes": {
                "base": observed_base_hash,
                "runner": runner_hash,
            },
            "score_effect": "NONE",
            "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
        }
        _write_immutable_json(failure, failure_payload)
        print(f"{RUN_ID} technical failure receipt: {failure}", file=sys.stderr)
        return 3
    print(json.dumps({
        "run_id": RUN_ID,
        "output": str(output),
        "candidate_interpretation_not_verdict": payload[
            "candidate_interpretation_not_verdict"
        ],
        "HP_M1_exact_resume_pass": payload["HP_M1_exact_resume_pass"],
        "pair_pass": payload["pair_pass"],
        "runtime_seconds": payload["runtime_seconds"],
        "coefficient_worker_runtime_seconds": {
            key: row["runtime_seconds"]
            for key, row in coefficient_payloads.items()
        },
        "exact_worker_runtime_seconds": {
            key: row["runtime_seconds"] for key, row in exact_payloads.items()
        },
    }, indent=2, sort_keys=True, allow_nan=False))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(
            f"{RUN_ID} pre-output technical failure: {type(exc).__name__}: {exc}",
            file=sys.stderr,
        )
        raise SystemExit(2)
