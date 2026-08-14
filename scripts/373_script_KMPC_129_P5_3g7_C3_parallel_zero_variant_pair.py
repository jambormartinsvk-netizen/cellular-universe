"""CLI runner for KMPC-129 parallel C3 gamma0/af0 pair receipts.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import traceback

from baseScripts.p5_general_synchronous import c3_zero_variant_parallel as c3


RUN_ID = "KMPC-129"
EXPECTED_BASE_SHA256 = (
    "8D839A2F628A311DCC2C951D7A23974A2276FF11031ADD2984FF708854B0C2E5"
)
PARENT_WORKER_WALL_LIMIT_SECONDS = 9.0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run one C3 gamma0/af0 pair through two bounded workers."
    )
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--smoke", action="store_true")
    action.add_argument("--audit", action="store_true")
    action.add_argument(
        "--worker-variant", choices=c3.VARIANTS, help=argparse.SUPPRESS
    )
    action.add_argument(
        "--worker-smoke", choices=c3.VARIANTS, help=argparse.SUPPRESS
    )
    parser.add_argument("--mode", choices=c3.MODES, required=True)
    parser.add_argument("--k", type=float, choices=c3.K_VALUES, required=True)
    parser.add_argument("--result-dir", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--max-runtime-seconds", type=float, default=4.8)
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
            json.dump(
                _native(payload), handle, indent=2, sort_keys=True, allow_nan=False
            )
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        temporary.replace(path)
    except Exception:
        if temporary.exists():
            temporary.unlink()
        raise


def _result_dir(args: argparse.Namespace, script_path: Path) -> Path:
    return (
        args.result_dir.resolve()
        if args.result_dir is not None
        else (script_path.parent / "results" / "k_mpc_005").resolve()
    )


def _run_two_workers(
    script_path: Path,
    mode: str,
    k_mpc: float,
    result_dir: Path,
    max_runtime_seconds: float,
    smoke: bool,
) -> dict[str, dict[str, object]]:
    action = "--worker-smoke" if smoke else "--worker-variant"
    processes: dict[str, subprocess.Popen[str]] = {}
    for variant in c3.VARIANTS:
        command = [
            sys.executable,
            str(script_path),
            action,
            variant,
            "--mode",
            mode,
            "--k",
            str(k_mpc),
            "--result-dir",
            str(result_dir),
            "--max-runtime-seconds",
            str(max_runtime_seconds),
        ]
        processes[variant] = subprocess.Popen(
            command,
            cwd=str(script_path.parent.parent),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
        )
    started = time.monotonic()
    records: dict[str, dict[str, object]] = {}
    try:
        for variant, process in processes.items():
            remaining = PARENT_WORKER_WALL_LIMIT_SECONDS - (time.monotonic() - started)
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
            records[variant] = {
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
        for variant, process in processes.items():
            stdout, stderr = process.communicate()
            records.setdefault(variant, {
                "returncode": process.returncode,
                "stdout": stdout,
                "stderr": stderr,
                "payload": None,
                "parse_error": "PARENT_WORKER_WALL_TIMEOUT",
            })
    return records


def _successful_payloads(
    records: dict[str, dict[str, object]]
) -> dict[str, dict[str, object]]:
    payloads: dict[str, dict[str, object]] = {}
    for variant in c3.VARIANTS:
        record = records.get(variant)
        if not isinstance(record, dict):
            continue
        payload = record.get("payload")
        if record.get("returncode") == 0 and isinstance(payload, dict):
            payloads[variant] = payload
    return payloads


def _worker_records_pass(records: dict[str, dict[str, object]]) -> bool:
    return len(_successful_payloads(records)) == len(c3.VARIANTS)


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

    if args.worker_smoke is not None:
        payload = c3.run_worker_smoke(
            args.mode, args.k, args.worker_smoke, result_dir
        )
        payload["source_hashes"] = {
            "base": observed_base_hash,
            "runner": runner_hash,
        }
        print(json.dumps(_native(payload), sort_keys=True, allow_nan=False))
        return 0 if payload["pass"] is True else 2

    if args.worker_variant is not None:
        payload = c3.run_variant_worker(
            args.mode,
            args.k,
            args.worker_variant,
            args.max_runtime_seconds,
            result_dir,
        )
        payload["source_hashes"]["runner"] = runner_hash
        print(json.dumps(_native(payload), sort_keys=True, allow_nan=False))
        return 0

    if args.smoke:
        records = _run_two_workers(
            script_path,
            args.mode,
            args.k,
            result_dir,
            args.max_runtime_seconds,
            smoke=True,
        )
        payloads = _successful_payloads(records)
        payload = c3.aggregate_smoke_workers(args.mode, args.k, payloads)
        payload["worker_process_records"] = {
            variant: {
                "returncode": record.get("returncode"),
                "stderr": record.get("stderr"),
                "parse_error": record.get("parse_error"),
            }
            for variant, record in records.items()
        }
        payload["source_hashes"] = {
            "base": observed_base_hash,
            "runner": runner_hash,
        }
        print(json.dumps(_native(payload), indent=2, sort_keys=True, allow_nan=False))
        return 0 if payload["pass"] is True and _worker_records_pass(records) else 2

    expected_name = c3.output_name(args.mode, args.k)
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
    records: dict[str, dict[str, object]] = {}
    try:
        records = _run_two_workers(
            script_path,
            args.mode,
            args.k,
            result_dir,
            args.max_runtime_seconds,
            smoke=False,
        )
        if not _worker_records_pass(records):
            raise RuntimeError("one or more KMPC-129 workers failed")
        payloads = _successful_payloads(records)
        payload = c3.aggregate_workers(
            args.mode,
            args.k,
            payloads,
            parent_runtime_seconds=time.monotonic() - parent_started,
        )
        payload["source_hashes"]["runner"] = runner_hash
        _write_immutable_json(output, payload)
    except Exception as exc:
        failure = result_dir / c3.failure_name(args.mode, args.k)
        compact_records = {
            variant: {
                "returncode": record.get("returncode"),
                "stderr": record.get("stderr"),
                "parse_error": record.get("parse_error"),
            }
            for variant, record in records.items()
        }
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
                "physical_receipt": "parallel_gamma0_af0_pair",
            },
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            "traceback": traceback.format_exc(),
            "worker_process_records": compact_records,
            "successful_worker_payloads": _successful_payloads(records),
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
        "candidate_interpretation_not_verdict": (
            payload["candidate_interpretation_not_verdict"]
        ),
        "pair_pass": payload["pair_pass"],
        "runtime_seconds": payload["runtime_seconds"],
        "worker_runtime_seconds": payload["worker_runtime_seconds"],
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
