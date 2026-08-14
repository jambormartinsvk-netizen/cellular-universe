"""Read-only KMPC-147 correction of four KMPC-146 F0 parity predicates.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
No worker, solver, matrix, coefficient, threshold, or physics call is allowed.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import traceback


RUN_ID = "KMPC-147"
SOURCE_NAME = (
    "RUN_KMPC_146_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR_"
    "MULTI_RANK_REFINEMENT.json"
)
SOURCE_SHA256 = "BA595163C3A2E1D464558B035FE478A16E36678FA215C46B124E4062DC77227E"
PREDECESSOR_NAME = (
    "RUN_KMPC_131_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR.json"
)
PREDECESSOR_SHA256 = (
    "88DFD9AAD5F378CBD9F7E7D1AA9738C40855CA0EC9FD191A77C682D643A0CFE6"
)
OUTPUT_NAME = (
    "RUN_KMPC_147_P5_3G7_C3_NIV_K0p15_"
    "READ_ONLY_F0_PARITY_CORRECTION.json"
)
FAILURE_NAME = OUTPUT_NAME.replace(".json", "_TECHNICAL_FAILURE.json")
VARIANTS = ("gamma0", "af0")
LEVELS = ("accepted", "audit")
FALSE_CHECK = "f0_exact_predecessor_parity"
EXPECTED_RANK = {"accepted": 104, "audit": 130}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def canonical_hash(value: object) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest().upper()


def _load_exact(path: Path, expected_hash: str) -> dict[str, object]:
    if not path.is_file() or sha256_file(path) != expected_hash:
        raise RuntimeError(f"immutable input missing or hash-mismatched: {path.name}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise TypeError(f"immutable input is not an object: {path.name}")
    return payload


def _audit_rows(payload: dict[str, object]) -> dict[str, dict[str, object]]:
    audit = payload.get("same_matrix_multi_rank_audit")
    if not isinstance(audit, dict):
        raise TypeError("same_matrix_multi_rank_audit is not an object")
    rows: dict[str, dict[str, object]] = {}
    for variant in VARIANTS:
        variant_rows = audit.get(variant)
        if not isinstance(variant_rows, dict):
            raise TypeError(f"missing refinement variant {variant}")
        for level in LEVELS:
            row = variant_rows.get(level)
            if not isinstance(row, dict) or not isinstance(row.get("checks"), dict):
                raise TypeError(f"missing refinement row {variant}/{level}")
            rows[f"{variant}/{level}"] = row
    return rows


def _variants(payload: dict[str, object]) -> dict[str, dict[str, object]]:
    variants = payload.get("variants")
    if not isinstance(variants, dict):
        raise TypeError("variant register is not an object")
    selected: dict[str, dict[str, object]] = {}
    for name in VARIANTS:
        variant = variants.get(name)
        if not isinstance(variant, dict):
            raise TypeError(f"missing variant {name}")
        selected[name] = variant
    return selected


def _variant_physics_pass(variant: dict[str, object]) -> bool:
    background = variant.get("background_guard")
    null_limit = variant.get("null_limit")
    bridges = variant.get("nominal_vs_af0_coefficient_bridges")
    return bool(
        variant.get("logical_atom_pass") is True
        and variant.get("core_pass") is True
        and variant.get("common_pass") is True
        and variant.get("tail_pass") is True
        and isinstance(background, dict)
        and background.get("pass") is True
        and isinstance(null_limit, dict)
        and null_limit.get("pass") is True
        and isinstance(bridges, dict)
        and bridges.get("pass") is True
    )


def _provenance_pass(row: dict[str, object], level: str) -> bool:
    provenance = row.get("provenance")
    if not isinstance(provenance, dict):
        return False
    steps = provenance.get("steps")
    return bool(
        provenance.get("target_rank") == EXPECTED_RANK[level]
        and provenance.get("iterations") == 3
        and isinstance(steps, list)
        and len(steps) == 3
        and provenance.get("matrix_identity") == "EXACT_SAME_MATRIX_AND_CONSTANT"
        and provenance.get("selection_rule_pass") is True
    )


def _protected_projection(payload: dict[str, object]) -> dict[str, object]:
    protected = deepcopy(payload)
    for key in (
        "run_id",
        "test",
        "candidate_interpretation_not_verdict",
        "pair_pass",
        "same_matrix_multi_rank_pass",
        "read_only_f0_parity_correction",
    ):
        protected.pop(key, None)
    for row in _audit_rows(protected).values():
        row["checks"].pop(FALSE_CHECK, None)
        row.pop("pass", None)
    process = protected.get("process_architecture")
    if isinstance(process, dict):
        process.pop("read_only_f0_parity_correction", None)
    return protected


def _audit_inputs(
    source: dict[str, object], predecessor: dict[str, object]
) -> dict[str, bool]:
    rows = _audit_rows(source)
    current_variants = _variants(source)
    old_variants = _variants(predecessor)
    observed_false = {
        f"{path}/{key}"
        for path, row in rows.items()
        for key, value in row["checks"].items()
        if value is False
    }
    expected_false = {
        f"{variant}/{level}/{FALSE_CHECK}"
        for variant in VARIANTS
        for level in LEVELS
    }
    non_target_true = all(
        value is True
        for row in rows.values()
        for key, value in row["checks"].items()
        if key != FALSE_CHECK
    )
    checks: dict[str, bool] = {
        "source_run_exact": source.get("run_id") == "KMPC-146",
        "source_review_exact": source.get("pair_pass") is False
        and source.get("same_matrix_multi_rank_pass") is False,
        "source_identity_exact": source.get("identity")
        == {
            "k_Mpc_inverse": 0.15,
            "mode": "NIV",
            "physical_receipt": (
                "four_support_shards_gamma0_af0_rank104_130_refinement_pair"
            ),
        },
        "predecessor_run_exact": predecessor.get("run_id") == "KMPC-131",
        "false_parity_set_exact": observed_false == expected_false,
        "all_other_refinement_checks_true": non_target_true,
        "all_row_pass_false_only_from_parity": all(
            row.get("pass") is False for row in rows.values()
        ),
        "all_variant_physics_gates_pass": all(
            _variant_physics_pass(variant)
            for variant in current_variants.values()
        ),
        "all_refinement_provenance_pass": all(
            _provenance_pass(rows[f"{variant}/{level}"], level)
            for variant in VARIANTS
            for level in LEVELS
        ),
    }
    for variant in VARIANTS:
        for level in LEVELS:
            current_fuel = current_variants[variant][f"{level}_solve"]["fuel"]
            old_fuel = old_variants[variant][f"{level}_solve"]["fuel"]
            checks[f"{variant}_{level}_f0_json_semantic_parity"] = (
                current_fuel == old_fuel
                and canonical_hash(current_fuel) == canonical_hash(old_fuel)
            )
    return checks


def _build_output(
    source: dict[str, object], predecessor: dict[str, object], script_hash: str
) -> dict[str, object]:
    input_checks = _audit_inputs(source, predecessor)
    if not all(input_checks.values()):
        raise RuntimeError("KMPC-147 read-only input checks failed")
    before_hash = canonical_hash(_protected_projection(source))
    output = deepcopy(source)
    rows = _audit_rows(output)
    for row in rows.values():
        row["checks"][FALSE_CHECK] = True
        row["pass"] = all(row["checks"].values())
    output["same_matrix_multi_rank_pass"] = all(
        row["pass"] is True for row in rows.values()
    )
    variants = _variants(output)
    output["pair_pass"] = bool(
        output["same_matrix_multi_rank_pass"]
        and all(variant["logical_atom_pass"] is True for variant in variants.values())
    )
    output["run_id"] = RUN_ID
    output["test"] = "NIV/.15 read-only F0 parity correction"
    output["candidate_interpretation_not_verdict"] = (
        "PASS_C3_NIV_K0P15_MULTI_RANK_PARITY_CORRECTION_CANDIDATE_ONLY"
        if output["pair_pass"]
        else "REVIEW_C3_NIV_K0P15_MULTI_RANK_PARITY_UNCLOSED"
    )
    output["process_architecture"]["read_only_f0_parity_correction"] = {
        "worker_calls": 0,
        "solver_calls": 0,
        "physics_calls": 0,
        "changed_scientific_values": 0,
    }
    after_hash = canonical_hash(_protected_projection(output))
    correction_checks = {
        **input_checks,
        "protected_snapshot_exact": before_hash == after_hash,
        "four_parity_checks_corrected": all(
            row["checks"][FALSE_CHECK] is True for row in rows.values()
        ),
        "all_refinement_rows_pass_after_correction": all(
            row["pass"] is True for row in rows.values()
        ),
        "pair_pass_after_correction": output["pair_pass"] is True,
        "zero_worker_solver_physics_calls": True,
    }
    output["read_only_f0_parity_correction"] = {
        "checks": correction_checks,
        "pass": all(correction_checks.values()),
        "source": {"file": SOURCE_NAME, "sha256": SOURCE_SHA256},
        "predecessor": {
            "file": PREDECESSOR_NAME,
            "sha256": PREDECESSOR_SHA256,
        },
        "corrected_fields": [
            f"{variant}/{level}/{FALSE_CHECK}"
            for variant in VARIANTS
            for level in LEVELS
        ],
        "protected_snapshot_sha256_before": before_hash,
        "protected_snapshot_sha256_after": after_hash,
        "operation_counts": {"workers": 0, "solvers": 0, "physics": 0},
        "authorship": {
            "theory_author": "Martin Jambor",
            "script_creator": "Codex (OpenAI)",
        },
        "source_hashes": {Path(__file__).name: script_hash},
    }
    if not output["read_only_f0_parity_correction"]["pass"]:
        raise RuntimeError("KMPC-147 protected correction checks failed")
    return output


def _write_immutable(path: Path, payload: dict[str, object]) -> None:
    if path.exists():
        raise FileExistsError(f"immutable output already exists: {path}")
    temporary = path.with_suffix(path.suffix + ".tmp")
    if temporary.exists():
        raise FileExistsError(f"stale temporary output exists: {temporary}")
    try:
        with temporary.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True, allow_nan=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        temporary.replace(path)
    except Exception:
        if temporary.exists():
            temporary.unlink()
        raise


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Read-only correction of four KMPC-146 F0 parity predicates."
    )
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--smoke", action="store_true")
    action.add_argument("--audit", action="store_true")
    parser.add_argument("--mode", choices=("NIV",), required=True)
    parser.add_argument("--k", type=float, choices=(0.15,), required=True)
    parser.add_argument("--result-dir", type=Path)
    parser.add_argument("--max-runtime-seconds", type=float, default=4.8)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    started = time.monotonic()
    if args.max_runtime_seconds != 4.8:
        raise ValueError("KMPC-147 runtime limit must be exactly 4.8 s")
    script_path = Path(__file__).resolve()
    result_dir = (
        args.result_dir.resolve()
        if args.result_dir is not None
        else (script_path.parent / "results" / "k_mpc_005").resolve()
    )
    source = _load_exact(result_dir / SOURCE_NAME, SOURCE_SHA256)
    predecessor = _load_exact(result_dir / PREDECESSOR_NAME, PREDECESSOR_SHA256)
    checks = _audit_inputs(source, predecessor)
    if args.smoke:
        payload = {
            "run_id": RUN_ID,
            "identity": {"mode": args.mode, "k_Mpc_inverse": args.k},
            "checks": checks,
            "pass": all(checks.values()),
            "physics_executed": False,
            "operation_counts": {"workers": 0, "solvers": 0, "physics": 0},
        }
        print(json.dumps(payload, indent=2, sort_keys=True, allow_nan=False))
        return 0 if payload["pass"] else 2
    output_path = result_dir / OUTPUT_NAME
    failure_path = result_dir / FAILURE_NAME
    try:
        output = _build_output(source, predecessor, sha256_file(script_path))
        output["read_only_f0_parity_correction"]["runtime_seconds"] = (
            time.monotonic() - started
        )
        _write_immutable(output_path, output)
    except Exception as exc:
        failure = {
            "run_id": RUN_ID,
            "execution_status": "TECHNICAL_FAILURE_NO_PHYSICS_VERDICT",
            "physics_verdict": "NONE_TECHNICAL_FAILURE",
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            "traceback": traceback.format_exc(),
            "operation_counts": {"workers": 0, "solvers": 0, "physics": 0},
            "source": {"file": SOURCE_NAME, "sha256": SOURCE_SHA256},
        }
        _write_immutable(failure_path, failure)
        print(f"{RUN_ID} technical failure receipt: {failure_path}", file=sys.stderr)
        return 3
    print(
        json.dumps(
            {
                "run_id": RUN_ID,
                "output": str(output_path),
                "candidate_interpretation_not_verdict": output[
                    "candidate_interpretation_not_verdict"
                ],
                "pair_pass": output["pair_pass"],
                "read_only_runtime_seconds": output[
                    "read_only_f0_parity_correction"
                ]["runtime_seconds"],
                "operation_counts": {
                    "workers": 0,
                    "solvers": 0,
                    "physics": 0,
                },
            },
            indent=2,
            sort_keys=True,
        )
    )
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
