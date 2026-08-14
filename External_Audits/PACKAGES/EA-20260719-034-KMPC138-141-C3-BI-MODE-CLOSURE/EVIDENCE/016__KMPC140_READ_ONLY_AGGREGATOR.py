"""Read-only parent recovery for KMPC-139 BI/.15 worker evidence.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
No worker, CPQR, coefficient solve, or exact solve is called here.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys
import time
import traceback
from typing import Mapping

from baseScripts.p5_general_synchronous import (
    c3_zero_variant_parallel_v9_bi_k0p15_fuel_order_roundtrip as c3,
)


RUN_ID = "KMPC-140"
SOURCE_RUN_ID = "KMPC-139"
MODE = "BI"
K_MPC = 0.15
MAX_RUNTIME_SECONDS = 4.8
EXACT_RUNTIME_SECONDS = 45.0
EXPECTED_BASE_SHA256 = (
    "489ED57D2F874CAC60E7733050C7DB4E8D59AABAD197827965F6322B80515D0D"
)
SOURCE_RECEIPT_NAME = (
    "RUN_KMPC_139_P5_3G7_C3_BI_K0p15_ZERO_VARIANT_PAIR_"
    "LOCAL_45S_HP_M1_EXACT_RESUME_TECHNICAL_FAILURE.json"
)
EXPECTED_SOURCE_RECEIPT_SHA256 = (
    "FBACDAB50EAC1D7ADB38104560F04806252E5A2DD19E605289A33B7E35FC334B"
)
OUTPUT_NAME = (
    "RUN_KMPC_140_P5_3G7_C3_BI_K0p15_ZERO_VARIANT_PAIR_"
    "LOCAL_45S_HP_M1_EXACT_RESUME_READ_ONLY_AGGREGATE.json"
)
FAILURE_NAME = OUTPUT_NAME.replace(".json", "_TECHNICAL_FAILURE.json")
COEFFICIENT_KEYS = {
    "gamma0/accepted",
    "gamma0/audit",
    "af0/accepted",
    "af0/audit",
}
EXACT_KEYS = {"gamma0", "af0"}

# The inherited aggregate must validate the immutable child identities as
# KMPC-139. Only the newly published parent receipt is renamed KMPC-140.
c3.RUN_ID = SOURCE_RUN_ID


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest().upper()


def write_immutable_json(path: Path, payload: Mapping[str, object]) -> None:
    if path.exists():
        raise FileExistsError(f"immutable output already exists: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    if temporary.exists():
        raise FileExistsError(f"stale temporary output exists: {temporary}")
    try:
        temporary.write_text(
            json.dumps(
                payload,
                indent=2,
                sort_keys=True,
                ensure_ascii=False,
                allow_nan=False,
            )
            + "\n",
            encoding="utf-8",
        )
        temporary.replace(path)
    finally:
        if temporary.exists():
            temporary.unlink()


def require_mapping(value: object, label: str) -> Mapping[str, object]:
    if not isinstance(value, dict):
        raise RuntimeError(f"KMPC-140 expected mapping: {label}")
    return value


def load_source_receipt(result_dir: Path) -> tuple[Path, dict[str, object]]:
    path = (result_dir / SOURCE_RECEIPT_NAME).resolve()
    if not path.is_file():
        raise FileNotFoundError(f"KMPC-140 frozen source receipt missing: {path}")
    if sha256_file(path) != EXPECTED_SOURCE_RECEIPT_SHA256:
        raise RuntimeError("KMPC-140 frozen source receipt hash mismatch")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RuntimeError("KMPC-140 source receipt root must be an object")
    return path, value


def validate_process_records(receipt: Mapping[str, object]) -> dict[str, bool]:
    records = require_mapping(receipt.get("worker_process_records"), "records")
    coefficient = require_mapping(records.get("coefficient_wave"), "coefficient records")
    exact = require_mapping(records.get("exact_boundary_wave"), "exact records")
    checks = {
        "coefficient_record_set_exact": set(coefficient) == COEFFICIENT_KEYS,
        "exact_record_set_exact": set(exact) == EXACT_KEYS,
    }
    for wave_name, rows in (("coefficient", coefficient), ("exact", exact)):
        for key, raw_row in rows.items():
            row = require_mapping(raw_row, f"{wave_name} record {key}")
            checks[f"{wave_name}/{key}/returncode_zero"] = row.get("returncode") == 0
            checks[f"{wave_name}/{key}/parse_clean"] = row.get("parse_error") == ""
            checks[f"{wave_name}/{key}/stderr_clean"] = row.get("stderr") == ""
    return checks


def validate_payloads(
    receipt: Mapping[str, object],
) -> tuple[dict[str, dict[str, object]], dict[str, dict[str, object]], dict[str, bool]]:
    successful = require_mapping(
        receipt.get("successful_worker_payloads"), "successful payloads"
    )
    coefficient_raw = require_mapping(
        successful.get("coefficient_wave"), "coefficient payloads"
    )
    exact_raw = require_mapping(successful.get("exact_boundary_wave"), "exact payloads")
    checks = {
        "source_run_id": receipt.get("run_id") == SOURCE_RUN_ID,
        "source_status_technical_failure": receipt.get("execution_status")
        == "TECHNICAL_FAILURE_NO_PHYSICS_VERDICT",
        "source_error_is_contract_guard_key": receipt.get("error_type") == "KeyError"
        and "contract_guard" in str(receipt.get("error_message")),
        "temporary_handoffs_removed": receipt.get(
            "temporary_handoff_directory_removed"
        )
        is True,
        "coefficient_payload_set_exact": set(coefficient_raw) == COEFFICIENT_KEYS,
        "exact_payload_set_exact": set(exact_raw) == EXACT_KEYS,
    }
    coefficient: dict[str, dict[str, object]] = {}
    exact: dict[str, dict[str, object]] = {}
    for key in sorted(COEFFICIENT_KEYS):
        row = deepcopy(require_mapping(coefficient_raw.get(key), f"coefficient {key}"))
        if not isinstance(row, dict):
            raise AssertionError("deepcopy of dict must remain dict")
        variant, level = key.split("/", maxsplit=1)
        checks[f"{key}/run_id"] = row.get("run_id") == SOURCE_RUN_ID
        checks[f"{key}/role"] = row.get("worker_role") == (
            "C3_BI_K0P15_TWO_WAVE_COEFFICIENT_SHARD"
        )
        checks[f"{key}/identity"] = row.get("identity") == {
            "mode": MODE,
            "k_Mpc_inverse": K_MPC,
            "variant": variant,
            "support_level": level,
        }
        checks[f"{key}/runtime_limit"] = row.get("runtime_limit_seconds") == 4.8
        runtime = row.get("runtime_seconds")
        checks[f"{key}/runtime_within_limit"] = (
            isinstance(runtime, (int, float)) and 0.0 <= runtime <= 4.8
        )
        evidence = row.get("exact_resume_evidence")
        checks[f"{key}/premerge_evidence"] = (
            isinstance(evidence, dict) and evidence.get("pass") is True
        )
        checks[f"{key}/legacy_alias_absent"] = "contract_guard" not in row
        successor = row.get("successor_contract_guard")
        checks[f"{key}/successor_contract_present"] = (
            isinstance(successor, dict) and successor.get("pass") is True
        )
        coefficient[key] = row
    for variant in sorted(EXACT_KEYS):
        row = deepcopy(require_mapping(exact_raw.get(variant), f"exact {variant}"))
        if not isinstance(row, dict):
            raise AssertionError("deepcopy of dict must remain dict")
        checks[f"exact/{variant}/run_id"] = row.get("run_id") == SOURCE_RUN_ID
        checks[f"exact/{variant}/role"] = row.get("worker_role") == (
            "C3_BI_K0P15_TWO_WAVE_EXACT_BOUNDARY_SHARD"
        )
        checks[f"exact/{variant}/identity"] = row.get("identity") == {
            "mode": MODE,
            "k_Mpc_inverse": K_MPC,
            "variant": variant,
            "support_level": "audit",
        }
        checks[f"exact/{variant}/runtime_limit"] = (
            row.get("runtime_limit_seconds") == EXACT_RUNTIME_SECONDS
        )
        runtime = row.get("runtime_seconds")
        checks[f"exact/{variant}/runtime_within_limit"] = (
            isinstance(runtime, (int, float))
            and 0.0 <= runtime <= EXACT_RUNTIME_SECONDS
        )
        technical = row.get("technical_checks")
        checks[f"exact/{variant}/technical_checks_all_true"] = (
            isinstance(technical, dict)
            and bool(technical)
            and all(value is True for value in technical.values())
        )
        checks[f"exact/{variant}/local_owner_active"] = (
            isinstance(technical, dict)
            and technical.get("local_45s_deadline_owner_active") is True
        )
        checks[f"exact/{variant}/owner_restored"] = (
            isinstance(technical, dict)
            and technical.get("original_deadline_owner_restored") is True
        )
        boundary = row.get("high_precision_boundary")
        checks[f"exact/{variant}/driver_pass"] = (
            isinstance(boundary, dict)
            and isinstance(boundary.get("driver"), dict)
            and boundary["driver"].get("pass_driver") is True
        )
        checks[f"exact/{variant}/holdout_pass"] = (
            isinstance(boundary, dict)
            and isinstance(boundary.get("holdout"), dict)
            and boundary["holdout"].get("pass_holdout") is True
            and boundary["holdout"].get("rows_added_to_driver_solve") == 0
        )
        checks[f"exact/{variant}/technical_pass"] = row.get("technical_pass") is True
        checks[f"exact/{variant}/boundary_pass"] = row.get("exact_boundary_pass") is True
        exact[variant] = row
    return coefficient, exact, checks


def add_legacy_aliases(
    coefficient: Mapping[str, Mapping[str, object]],
) -> tuple[dict[str, dict[str, object]], dict[str, object]]:
    normalized: dict[str, dict[str, object]] = {}
    aliases: list[dict[str, object]] = []
    for key in sorted(COEFFICIENT_KEYS):
        original = require_mapping(coefficient.get(key), f"alias source {key}")
        if "contract_guard" in original:
            raise RuntimeError(f"KMPC-140 unexpected pre-existing alias: {key}")
        successor = original.get("successor_contract_guard")
        if not isinstance(successor, dict):
            raise RuntimeError(f"KMPC-140 successor contract missing: {key}")
        before_sha = canonical_sha256(original)
        row = deepcopy(original)
        row["contract_guard"] = deepcopy(successor)
        restored = deepcopy(row)
        del restored["contract_guard"]
        if canonical_sha256(restored) != before_sha:
            raise RuntimeError(f"KMPC-140 existing field changed: {key}")
        if row["contract_guard"] != row["successor_contract_guard"]:
            raise RuntimeError(f"KMPC-140 alias value mismatch: {key}")
        normalized[key] = row
        aliases.append({
            "payload": key,
            "source_field": "successor_contract_guard",
            "added_alias": "contract_guard",
            "source_payload_sha256": before_sha,
            "existing_fields_unchanged": True,
            "alias_exact_equal": True,
        })
    register = {
        "operation": "ADD_LEGACY_SCHEMA_ALIAS_ONLY",
        "alias_count": len(aliases),
        "existing_values_changed": 0,
        "child_run_ids_changed": 0,
        "aliases": aliases,
        "pass": len(aliases) == 4,
    }
    return normalized, register


def preflight(result_dir: Path) -> tuple[
    Path,
    dict[str, dict[str, object]],
    dict[str, dict[str, object]],
    dict[str, object],
    dict[str, bool],
]:
    wrapper_path = Path(c3.__file__).resolve()
    receipt_path, receipt = load_source_receipt(result_dir)
    coefficient, exact, payload_checks = validate_payloads(receipt)
    normalized, alias_register = add_legacy_aliases(coefficient)
    checks = {
        "frozen_wrapper_hash": sha256_file(wrapper_path) == EXPECTED_BASE_SHA256,
        "frozen_receipt_hash": sha256_file(receipt_path)
        == EXPECTED_SOURCE_RECEIPT_SHA256,
        **validate_process_records(receipt),
        **payload_checks,
        "alias_register_pass": alias_register["pass"] is True,
        "alias_count_four": alias_register["alias_count"] == 4,
        "existing_values_changed_zero": alias_register[
            "existing_values_changed"
        ]
        == 0,
        "no_worker_or_solver_calls": True,
    }
    if not all(checks.values()):
        failed = sorted(name for name, passed in checks.items() if not passed)
        raise RuntimeError("KMPC-140 preflight failed: " + ",".join(failed))
    return receipt_path, normalized, exact, alias_register, checks


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Read-only KMPC-140 parent aggregation of the frozen KMPC-139 "
            "four coefficient plus two exact payloads."
        )
    )
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--smoke", action="store_true")
    action.add_argument("--audit", action="store_true")
    parser.add_argument("--mode", choices=(MODE,), required=True)
    parser.add_argument("--k", type=float, choices=(K_MPC,), required=True)
    parser.add_argument("--result-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--max-runtime-seconds", type=float, default=MAX_RUNTIME_SECONDS
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if (args.mode, args.k) != (MODE, K_MPC):
        raise ValueError("KMPC-140 is frozen to BI/k=0.15")
    if args.max_runtime_seconds != MAX_RUNTIME_SECONDS:
        raise ValueError("KMPC-140 read-only limit must remain exactly 4.8 s")
    result_dir = args.result_dir.resolve()
    started = time.monotonic()
    receipt_path, coefficient, exact, alias_register, checks = preflight(result_dir)
    if args.smoke:
        payload = {
            "run_id": RUN_ID,
            "mode": "SMOKE_NO_PHYSICS",
            "identity": {"mode": MODE, "k_Mpc_inverse": K_MPC},
            "checks": checks,
            "schema_alias_register": alias_register,
            "source_receipt": receipt_path.name,
            "source_receipt_sha256": EXPECTED_SOURCE_RECEIPT_SHA256,
            "physics_executed": False,
            "worker_calls": 0,
            "solver_calls": 0,
            "pass": all(checks.values()),
        }
        print(json.dumps(payload, indent=2, sort_keys=True, allow_nan=False))
        return 0 if payload["pass"] else 2

    output = (
        args.output.resolve()
        if args.output is not None
        else (result_dir / OUTPUT_NAME).resolve()
    )
    if output.parent != result_dir or output.name != OUTPUT_NAME:
        raise ValueError("official output must use the frozen name inside result-dir")
    if output.exists():
        raise FileExistsError(f"immutable output already exists: {output}")
    runner_path = Path(__file__).resolve()
    try:
        payload = c3.aggregate_shards(
            coefficient,
            exact,
            result_dir,
            parent_runtime_seconds=time.monotonic() - started,
            temporary_handoffs_removed=True,
        )
        elapsed = time.monotonic() - started
        if elapsed > args.max_runtime_seconds:
            raise TimeoutError("KMPC-140 read-only parent runtime exceeded 4.8 s")
        payload["run_id"] = RUN_ID
        payload["test"] = (
            "A2-K4 P5.3g7 C3 BI/.15 read-only recovery of completed "
            "KMPC-139 four-plus-two worker evidence"
        )
        payload["identity"]["physical_receipt"] = (
            "KMPC139_4_coefficient_plus_2_local45_exact_read_only_parent"
        )
        payload["process_architecture"]["read_only_parent_recovery"] = {
            "source_run_id": SOURCE_RUN_ID,
            "source_receipt": receipt_path.name,
            "source_receipt_sha256": EXPECTED_SOURCE_RECEIPT_SHA256,
            "worker_calls": 0,
            "solver_calls": 0,
            "CPQR_calls": 0,
            "physics_repeated": False,
            "child_payloads_recomputed": False,
            "child_run_ids_changed": 0,
            "schema_alias_register": alias_register,
            "coefficient_payload_count": 4,
            "exact_payload_count": 2,
            "coefficient_limit_seconds": 4.8,
            "exact_limit_seconds": EXACT_RUNTIME_SECONDS,
            "read_only_parent_limit_seconds": MAX_RUNTIME_SECONDS,
        }
        payload["source_hashes"][receipt_path.name] = (
            EXPECTED_SOURCE_RECEIPT_SHA256
        )
        payload["source_hashes"][runner_path.name] = sha256_file(runner_path)
        payload["runtime_seconds"] = elapsed
        if payload.get("pair_pass") is True:
            payload["candidate_interpretation_not_verdict"] = (
                "PASS_C3_BI_K0P15_ZERO_PAIR_LOCAL_45S_HP_M1_EXACT_RESUME_"
                "READ_ONLY_AGGREGATE_CANDIDATE_ONLY"
            )
        else:
            payload["candidate_interpretation_not_verdict"] = (
                "REVIEW_C3_BI_K0P15_READ_ONLY_AGGREGATE_UNCLOSED"
            )
        write_immutable_json(output, payload)
    except Exception as exc:
        failure_path = result_dir / FAILURE_NAME
        failure = {
            "run_id": RUN_ID,
            "execution_status": "TECHNICAL_FAILURE_NO_PHYSICS_VERDICT",
            "physics_verdict": "NONE_TECHNICAL_FAILURE",
            "authorship": {
                "theory_author": "Martin Jambor",
                "script_creator": "Codex (OpenAI)",
            },
            "identity": {"mode": MODE, "k_Mpc_inverse": K_MPC},
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            "traceback": traceback.format_exc(),
            "source_receipt": receipt_path.name,
            "source_receipt_sha256": EXPECTED_SOURCE_RECEIPT_SHA256,
            "schema_alias_register": alias_register,
            "physics_executed": False,
            "worker_calls": 0,
            "solver_calls": 0,
            "score_effect": "NONE",
            "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
            "source_hashes": {
                Path(c3.__file__).name: EXPECTED_BASE_SHA256,
                receipt_path.name: EXPECTED_SOURCE_RECEIPT_SHA256,
                runner_path.name: sha256_file(runner_path),
            },
        }
        write_immutable_json(failure_path, failure)
        print(f"{RUN_ID} technical failure receipt: {failure_path}", file=sys.stderr)
        return 3
    print(json.dumps({
        "run_id": RUN_ID,
        "output": str(output),
        "candidate_interpretation_not_verdict": payload[
            "candidate_interpretation_not_verdict"
        ],
        "pair_pass": payload["pair_pass"],
        "HP_M1_exact_resume_pass": payload["HP_M1_exact_resume_pass"],
        "runtime_seconds": payload["runtime_seconds"],
        "worker_calls": 0,
        "solver_calls": 0,
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
