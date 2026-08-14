"""Read-only KMPC-145 correction of two KMPC-144 parity predicates.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
No worker, solver, CPQR, coefficient, threshold or physics call is allowed.
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


RUN_ID = "KMPC-145"
SOURCE_NAME = (
    "RUN_KMPC_144_P5_3G7_C3_NID_K0p15_"
    "AF0_AUDIT_SAME_MATRIX_REFINEMENT.json"
)
SOURCE_SHA256 = "7288ADE2BBC876D5F26677186ACF37BD3FE6B6DC439458C90A640B1C8FD103EB"
PREDECESSOR_NAME = "RUN_KMPC_131_P5_3G7_C3_NID_K0p15_ZERO_VARIANT_PAIR.json"
PREDECESSOR_SHA256 = "3850A3D951E5A8A3E21C93A6DAE7F1A08CBE6430E7100BD01B75F573F21AF71B"
OUTPUT_NAME = "RUN_KMPC_145_P5_3G7_C3_NID_K0p15_PARITY_SCOPE_CORRECTION.json"
FAILURE_NAME = OUTPUT_NAME.replace(".json", "_TECHNICAL_FAILURE.json")
FALSE_PARITY_SET = {
    "af0_accepted_exact_predecessor_parity",
    "gamma0_variant_exact_predecessor_parity",
}


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


def _gamma_scientific_projection(variant: dict[str, object]) -> dict[str, object]:
    projected = deepcopy(variant)
    projected.pop("support_worker_runtime_seconds", None)
    core = projected.get("core_checks")
    if not isinstance(core, dict):
        raise TypeError("gamma0 core_checks is not an object")
    core.pop("af0_audit_refinement_contract", None)
    return projected


def _protected_projection(payload: dict[str, object]) -> dict[str, object]:
    protected = deepcopy(payload)
    for key in (
        "run_id",
        "test",
        "candidate_interpretation_not_verdict",
        "pair_pass",
        "same_matrix_refinement_pass",
        "read_only_parity_scope_correction",
    ):
        protected.pop(key, None)
    audit = protected.get("same_matrix_refinement_audit")
    if not isinstance(audit, dict):
        raise TypeError("same_matrix_refinement_audit is not an object")
    checks = audit.get("checks")
    if not isinstance(checks, dict):
        raise TypeError("same_matrix_refinement_audit checks are not an object")
    for key in FALSE_PARITY_SET:
        checks.pop(key, None)
    audit.pop("pass", None)
    process = protected.get("process_architecture")
    if isinstance(process, dict):
        process.pop("read_only_parity_scope_correction", None)
    return protected


def _variant_physics_pass(variant: object) -> bool:
    if not isinstance(variant, dict):
        return False
    required = (
        variant.get("logical_atom_pass") is True,
        variant.get("core_pass") is True,
        variant.get("common_pass") is True,
        variant.get("tail_pass") is True,
        isinstance(variant.get("background_guard"), dict)
        and variant["background_guard"].get("pass") is True,
        isinstance(variant.get("null_limit"), dict)
        and variant["null_limit"].get("pass") is True,
        isinstance(variant.get("nominal_vs_af0_coefficient_bridges"), dict)
        and variant["nominal_vs_af0_coefficient_bridges"].get("pass") is True,
    )
    return all(required)


def _audit_inputs(
    source: dict[str, object], predecessor: dict[str, object]
) -> dict[str, bool]:
    audit = source.get("same_matrix_refinement_audit")
    if not isinstance(audit, dict) or not isinstance(audit.get("checks"), dict):
        raise TypeError("KMPC-144 refinement audit schema mismatch")
    refinement_checks = audit["checks"]
    observed_false = {
        key for key, value in refinement_checks.items() if value is False
    }
    non_target_true = all(
        value is True
        for key, value in refinement_checks.items()
        if key not in FALSE_PARITY_SET
    )
    source_variants = source.get("variants")
    predecessor_variants = predecessor.get("variants")
    if not isinstance(source_variants, dict) or not isinstance(
        predecessor_variants, dict
    ):
        raise TypeError("variant register mismatch")
    af0 = source_variants.get("af0")
    gamma0 = source_variants.get("gamma0")
    old_af0 = predecessor_variants.get("af0")
    old_gamma0 = predecessor_variants.get("gamma0")
    if not all(isinstance(row, dict) for row in (af0, gamma0, old_af0, old_gamma0)):
        raise TypeError("variant payload mismatch")
    provenance = audit.get("provenance")
    return {
        "source_run_exact": source.get("run_id") == "KMPC-144",
        "source_review_exact": source.get("pair_pass") is False
        and source.get("same_matrix_refinement_pass") is False,
        "predecessor_run_exact": predecessor.get("run_id") == "KMPC-131",
        "false_parity_set_exact": observed_false == FALSE_PARITY_SET,
        "all_other_refinement_checks_true": non_target_true,
        "af0_accepted_json_semantic_parity": af0.get("accepted_solve")
        == old_af0.get("accepted_solve"),
        "gamma0_scientific_projection_parity": _gamma_scientific_projection(
            gamma0
        )
        == _gamma_scientific_projection(old_gamma0),
        "af0_all_physics_gates_pass": _variant_physics_pass(af0),
        "gamma0_all_physics_gates_pass": _variant_physics_pass(gamma0),
        "refinement_provenance_pass": isinstance(provenance, dict)
        and provenance.get("selection_rule_pass") is True
        and provenance.get("matrix_identity") == "EXACT_SAME_MATRIX_AND_CONSTANT"
        and provenance.get("target_rank") == 104
        and provenance.get("iterations") == 3,
    }


def _build_output(
    source: dict[str, object], predecessor: dict[str, object], script_hash: str
) -> dict[str, object]:
    checks = _audit_inputs(source, predecessor)
    if not all(checks.values()):
        raise RuntimeError("KMPC-145 read-only input checks failed")
    before_hash = canonical_hash(_protected_projection(source))
    output = deepcopy(source)
    refinement_checks = output["same_matrix_refinement_audit"]["checks"]
    for key in FALSE_PARITY_SET:
        refinement_checks[key] = True
    output["same_matrix_refinement_audit"]["pass"] = all(
        refinement_checks.values()
    )
    output["same_matrix_refinement_pass"] = output[
        "same_matrix_refinement_audit"
    ]["pass"]
    output["pair_pass"] = bool(
        output["same_matrix_refinement_pass"]
        and output["variants"]["af0"]["logical_atom_pass"]
        and output["variants"]["gamma0"]["logical_atom_pass"]
    )
    output["run_id"] = RUN_ID
    output["test"] = "NID/.15 read-only parity-scope correction"
    output["candidate_interpretation_not_verdict"] = (
        "PASS_C3_NID_K0P15_PARITY_SCOPE_CORRECTION_CANDIDATE_ONLY"
        if output["pair_pass"]
        else "REVIEW_C3_NID_K0P15_PARITY_SCOPE_UNCLOSED"
    )
    output["process_architecture"]["read_only_parity_scope_correction"] = {
        "worker_calls": 0,
        "solver_calls": 0,
        "cpqr_calls": 0,
        "changed_scientific_values": 0,
    }
    after_hash = canonical_hash(_protected_projection(output))
    correction_checks = {
        **checks,
        "protected_snapshot_exact": before_hash == after_hash,
        "two_parity_checks_corrected": all(
            refinement_checks[key] is True for key in FALSE_PARITY_SET
        ),
        "pair_pass_after_correction": output["pair_pass"] is True,
        "zero_worker_solver_cpqr_calls": True,
    }
    output["read_only_parity_scope_correction"] = {
        "checks": correction_checks,
        "pass": all(correction_checks.values()),
        "source": {"file": SOURCE_NAME, "sha256": SOURCE_SHA256},
        "predecessor": {
            "file": PREDECESSOR_NAME,
            "sha256": PREDECESSOR_SHA256,
        },
        "corrected_fields": sorted(FALSE_PARITY_SET),
        "protected_snapshot_sha256_before": before_hash,
        "protected_snapshot_sha256_after": after_hash,
        "operation_counts": {"workers": 0, "solvers": 0, "cpqr": 0},
        "authorship": {
            "theory_author": "Martin Jambor",
            "script_creator": "Codex (OpenAI)",
        },
        "source_hashes": {Path(__file__).name: script_hash},
    }
    if not output["read_only_parity_scope_correction"]["pass"]:
        raise RuntimeError("KMPC-145 protected correction checks failed")
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
        description="Read-only correction of two KMPC-144 parity predicates."
    )
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--smoke", action="store_true")
    action.add_argument("--audit", action="store_true")
    parser.add_argument("--mode", choices=("NID",), required=True)
    parser.add_argument("--k", type=float, choices=(0.15,), required=True)
    parser.add_argument("--result-dir", type=Path)
    parser.add_argument("--max-runtime-seconds", type=float, default=4.8)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    started = time.monotonic()
    if args.max_runtime_seconds != 4.8:
        raise ValueError("KMPC-145 runtime limit must be exactly 4.8 s")
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
            "operation_counts": {"workers": 0, "solvers": 0, "cpqr": 0},
        }
        print(json.dumps(payload, indent=2, sort_keys=True, allow_nan=False))
        return 0 if payload["pass"] else 2
    output_path = result_dir / OUTPUT_NAME
    failure_path = result_dir / FAILURE_NAME
    try:
        output = _build_output(source, predecessor, sha256_file(script_path))
        output["runtime_seconds"] = time.monotonic() - started
        _write_immutable(output_path, output)
    except Exception as exc:
        failure = {
            "run_id": RUN_ID,
            "execution_status": "TECHNICAL_FAILURE_NO_PHYSICS_VERDICT",
            "physics_verdict": "NONE_TECHNICAL_FAILURE",
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            "traceback": traceback.format_exc(),
            "operation_counts": {"workers": 0, "solvers": 0, "cpqr": 0},
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
                "runtime_seconds": output["runtime_seconds"],
                "operation_counts": {"workers": 0, "solvers": 0, "cpqr": 0},
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
