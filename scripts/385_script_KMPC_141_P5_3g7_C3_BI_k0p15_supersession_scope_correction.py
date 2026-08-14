"""Read-only correction of the KMPC-140 supersession-scope predicate.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
No physical worker, solver, or CPQR operation is imported or called.
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


RUN_ID = "KMPC-141"
SOURCE_RUN_ID = "KMPC-140"
MODE = "BI"
K_MPC = 0.15
MAX_RUNTIME_SECONDS = 4.8
SOURCE_NAME = (
    "RUN_KMPC_140_P5_3G7_C3_BI_K0p15_ZERO_VARIANT_PAIR_"
    "LOCAL_45S_HP_M1_EXACT_RESUME_READ_ONLY_AGGREGATE.json"
)
EXPECTED_SOURCE_SHA256 = (
    "DF45DF6A937177A84832826400725553D5A0EADD104981E8F3992DC3FCC1638F"
)
OUTPUT_NAME = (
    "RUN_KMPC_141_P5_3G7_C3_BI_K0p15_ZERO_VARIANT_PAIR_"
    "LOCAL_45S_HP_M1_EXACT_RESUME_SUPERSESSION_SCOPE_CORRECTED.json"
)
FAILURE_NAME = OUTPUT_NAME.replace(".json", "_TECHNICAL_FAILURE.json")
VARIANTS = ("gamma0", "af0")
DRIVER_CHECK = "M3_driver"
HOLDOUT_CHECK = "M3_independent_00_0i_holdout"
DECLARED_SCOPE = {DRIVER_CHECK, HOLDOUT_CHECK}


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


def require_mapping(value: object, label: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise RuntimeError(f"KMPC-141 expected mapping: {label}")
    return value


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


def load_source(result_dir: Path) -> tuple[Path, dict[str, object]]:
    path = (result_dir / SOURCE_NAME).resolve()
    if not path.is_file():
        raise FileNotFoundError(f"KMPC-141 frozen source missing: {path}")
    if sha256_file(path) != EXPECTED_SOURCE_SHA256:
        raise RuntimeError("KMPC-141 frozen source hash mismatch")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise RuntimeError("KMPC-141 source root must be an object")
    return path, payload


def scientific_snapshot(payload: Mapping[str, object]) -> dict[str, object]:
    variants = require_mapping(payload.get("variants"), "variants")
    snapshot_variants: dict[str, object] = {}
    for variant in VARIANTS:
        row = require_mapping(variants.get(variant), f"variant {variant}")
        accepted = deepcopy(require_mapping(row.get("accepted_solve"), "accepted solve"))
        audit = deepcopy(require_mapping(row.get("audit_solve"), "audit solve"))
        accepted.pop("pass", None)
        audit.pop("pass", None)
        exact = audit.pop("exact_resume_supersession", None)
        exact_mapping = require_mapping(exact, "exact resume evidence")
        snapshot_variants[variant] = {
            "inputs": row.get("inputs"),
            "combined_R_fs_guard": row.get("combined_R_fs_guard"),
            "accepted_solve_without_pass": accepted,
            "audit_solve_without_pass_or_exact_composer": audit,
            "common": row.get("common"),
            "tails": row.get("tails"),
            "S_C0_actual_guard": row.get("S_C0_actual_guard"),
            "background_guard": row.get("background_guard"),
            "null_limit": row.get("null_limit"),
            "nominal_vs_af0_coefficient_bridges": row.get(
                "nominal_vs_af0_coefficient_bridges"
            ),
            "high_precision_boundary": exact_mapping.get(
                "high_precision_boundary"
            ),
            "combined_register_handoff": exact_mapping.get(
                "combined_register_handoff"
            ),
            "float_driver_capture": exact_mapping.get("float_driver_capture"),
        }
    return {
        "nominal_reference": payload.get("nominal_reference"),
        "contract_guard": payload.get("contract_guard"),
        "frozen_contract": payload.get("frozen_contract"),
        "independent_contract_valid": payload.get("independent_contract_valid"),
        "frozen_B1_left_null_Bianchi": payload.get(
            "frozen_B1_left_null_Bianchi"
        ),
        "production_TCA0_bridge": payload.get("production_TCA0_bridge"),
        "support_depth_spec": payload.get("support_depth_spec"),
        "M1": payload.get("M1"),
        "thresholds": payload.get("thresholds"),
        "variants": snapshot_variants,
    }


def validate_source(payload: Mapping[str, object]) -> dict[str, bool]:
    checks: dict[str, bool] = {
        "source_run_id": payload.get("run_id") == SOURCE_RUN_ID,
        "source_execution_complete": payload.get("execution_status")
        == "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "source_pair_false": payload.get("pair_pass") is False,
        "source_exact_pass_false": payload.get("HP_M1_exact_resume_pass") is False,
        "source_candidate_review": payload.get(
            "candidate_interpretation_not_verdict"
        )
        == "REVIEW_C3_BI_K0P15_READ_ONLY_AGGREGATE_UNCLOSED",
    }
    architecture = require_mapping(
        require_mapping(payload.get("process_architecture"), "architecture").get(
            "read_only_parent_recovery"
        ),
        "read-only recovery",
    )
    checks.update({
        "source_worker_calls_zero": architecture.get("worker_calls") == 0,
        "source_solver_calls_zero": architecture.get("solver_calls") == 0,
        "source_physics_not_repeated": architecture.get("physics_repeated")
        is False,
    })
    variants = require_mapping(payload.get("variants"), "variants")
    hp_audit = require_mapping(
        payload.get("HP_M1_exact_resume_audit"), "HP exact audit"
    )
    for variant in VARIANTS:
        row = require_mapping(variants.get(variant), f"variant {variant}")
        audit = require_mapping(row.get("audit_solve"), f"audit solve {variant}")
        evidence = require_mapping(
            audit.get("exact_resume_supersession"), f"evidence {variant}"
        )
        evidence_checks = require_mapping(
            evidence.get("checks"), f"evidence checks {variant}"
        )
        original_false = evidence.get("original_false_checks")
        checks[f"{variant}/original_false_exact_driver_only"] = (
            original_false == [DRIVER_CHECK]
        )
        checks[f"{variant}/declared_scope_legacy_two"] = set(
            evidence.get("superseded_checks", [])
        ) == DECLARED_SCOPE
        checks[f"{variant}/legacy_equality_false"] = (
            evidence_checks.get("original_false_set_exact") is False
        )
        checks[f"{variant}/all_other_evidence_checks_true"] = all(
            value is True
            for name, value in evidence_checks.items()
            if name != "original_false_set_exact"
        )
        checks[f"{variant}/exact_evidence_false_only_from_legacy"] = (
            evidence.get("pass") is False
        )
        boundary = require_mapping(
            evidence.get("high_precision_boundary"), f"boundary {variant}"
        )
        driver = require_mapping(boundary.get("driver"), f"driver {variant}")
        holdout = require_mapping(boundary.get("holdout"), f"holdout {variant}")
        checks[f"{variant}/exact_driver_pass"] = driver.get("pass_driver") is True
        checks[f"{variant}/exact_holdout_pass"] = (
            holdout.get("pass_holdout") is True
            and holdout.get("rows_added_to_driver_solve") == 0
        )
        checks[f"{variant}/audit_checks_already_true"] = all(
            value is True
            for value in require_mapping(audit.get("checks"), "audit checks").values()
        )
        checks[f"{variant}/audit_pass_false_from_composer"] = audit.get("pass") is False
        core_checks = require_mapping(row.get("core_checks"), f"core {variant}")
        checks[f"{variant}/core_false_only_audit_solve"] = sorted(
            name for name, value in core_checks.items() if value is False
        ) == ["audit_solve"]
        checks[f"{variant}/all_noncore_gates_true"] = all((
            row.get("common_pass") is True,
            row.get("tail_pass") is True,
            require_mapping(row.get("background_guard"), "background").get("pass")
            is True,
            require_mapping(row.get("null_limit"), "null").get("pass") is True,
            require_mapping(
                row.get("nominal_vs_af0_coefficient_bridges"), "bridge"
            ).get("pass")
            is True,
        ))
        hp_row = require_mapping(hp_audit.get(variant), f"HP audit {variant}")
        checks[f"{variant}/hp_audit_false"] = hp_row.get("pass") is False
    return checks


def corrected_evidence(
    evidence: Mapping[str, object], variant: str
) -> tuple[dict[str, object], dict[str, object]]:
    row = deepcopy(evidence)
    original_false = list(row["original_false_checks"])
    declared_scope = list(row["superseded_checks"])
    original_set = set(original_false)
    declared_set = set(declared_scope)
    boundary = require_mapping(row.get("high_precision_boundary"), "boundary")
    driver = require_mapping(boundary.get("driver"), "driver")
    holdout = require_mapping(boundary.get("holdout"), "holdout")
    legacy_checks = require_mapping(row.get("checks"), "evidence checks")
    legacy_value = legacy_checks.pop("original_false_set_exact")
    if legacy_value is not False:
        raise RuntimeError(f"KMPC-141 legacy predicate is not false: {variant}")
    corrected_checks = {
        "original_false_set_nonempty": bool(original_set),
        "original_false_set_within_declared_scope": original_set.issubset(
            declared_set
        ),
        "no_original_false_outside_declared_scope": not (
            original_set - declared_set
        ),
        "original_M3_driver_closed_by_exact_driver": (
            DRIVER_CHECK in original_set and driver.get("pass_driver") is True
        ),
        "holdout_false_closed_or_preexisting_pass_exactly_confirmed": (
            holdout.get("pass_holdout") is True
            and holdout.get("rows_added_to_driver_solve") == 0
        ),
    }
    legacy_checks.update(corrected_checks)
    actual_superseded = sorted(original_set & declared_set)
    confirmed = sorted(declared_set - original_set)
    correction = {
        "variant": variant,
        "legacy_predicate": "original_false_set == declared_supersession_scope",
        "legacy_predicate_value": False,
        "corrected_predicate": (
            "original_false_set_nonempty_and_subset_of_scope_with_exact_closure"
        ),
        "declared_supersession_scope": sorted(declared_set),
        "original_false_checks": original_false,
        "actual_superseded_false_checks": actual_superseded,
        "already_passing_exactly_confirmed": confirmed,
        "scientific_values_may_change": False,
        "pass": all(corrected_checks.values()),
    }
    row["legacy_original_false_set_exact_diagnostic"] = {
        "value": False,
        "retained_outside_active_checks": True,
    }
    row["declared_supersession_scope"] = sorted(declared_set)
    row["superseded_checks"] = actual_superseded
    row["already_passing_exactly_confirmed"] = confirmed
    row["supersession_scope_correction"] = correction
    row["pass"] = all(legacy_checks.values()) and correction["pass"] is True
    return row, correction


def apply_correction(
    source: Mapping[str, object], source_path: Path, runner_path: Path
) -> tuple[dict[str, object], dict[str, object]]:
    payload = deepcopy(source)
    protected_before = canonical_sha256(scientific_snapshot(payload))
    variants = require_mapping(payload.get("variants"), "variants")
    hp_audit = require_mapping(
        payload.get("HP_M1_exact_resume_audit"), "HP exact audit"
    )
    corrections: dict[str, object] = {}
    for variant in VARIANTS:
        row = require_mapping(variants.get(variant), f"variant {variant}")
        audit = require_mapping(row.get("audit_solve"), f"audit solve {variant}")
        evidence, correction = corrected_evidence(
            require_mapping(
                audit.get("exact_resume_supersession"), f"evidence {variant}"
            ),
            variant,
        )
        audit["exact_resume_supersession"] = evidence
        audit["pass"] = bool(
            all(require_mapping(audit.get("checks"), "audit checks").values())
            and evidence["pass"] is True
        )
        core_checks = require_mapping(row.get("core_checks"), f"core {variant}")
        core_checks["audit_solve"] = audit["pass"]
        row["core_pass"] = all(core_checks.values())
        variant_pass = all((
            row["core_pass"] is True,
            row.get("common_pass") is True,
            row.get("tail_pass") is True,
            require_mapping(row.get("background_guard"), "background").get("pass")
            is True,
            require_mapping(row.get("null_limit"), "null").get("pass") is True,
            require_mapping(
                row.get("nominal_vs_af0_coefficient_bridges"), "bridge"
            ).get("pass")
            is True,
        ))
        row["logical_atom_pass"] = variant_pass
        row["candidate_interpretation_not_verdict"] = (
            f"PASS_C3_{variant.upper()}_ATOM_CANDIDATE_ONLY"
            if variant_pass
            else f"REVIEW_C3_{variant.upper()}_ATOM_UNCLOSED"
        )
        hp_row = require_mapping(hp_audit.get(variant), f"HP audit {variant}")
        hp_row["exact_resume"] = deepcopy(evidence)
        coefficient_checks = require_mapping(
            hp_row.get("coefficient_and_null_checks"), "coefficient checks"
        )
        coefficient_checks["core_pass"] = row["core_pass"]
        hp_row["pass"] = bool(
            evidence["pass"] is True and all(coefficient_checks.values())
        )
        corrections[variant] = correction
    payload["HP_M1_exact_resume_pass"] = all(
        require_mapping(hp_audit.get(variant), f"HP audit {variant}").get("pass")
        is True
        for variant in VARIANTS
    )
    payload["pair_pass"] = all(
        require_mapping(variants.get(variant), f"variant {variant}").get(
            "logical_atom_pass"
        )
        is True
        for variant in VARIANTS
    ) and payload["HP_M1_exact_resume_pass"] is True
    payload["run_id"] = RUN_ID
    payload["test"] = (
        "A2-K4 P5.3g7 C3 BI/.15 read-only supersession-scope correction "
        "over frozen KMPC-140 parent receipt"
    )
    payload["identity"]["physical_receipt"] = (
        "KMPC140_read_only_parent_with_corrected_exact_supersession_scope"
    )
    payload["candidate_interpretation_not_verdict"] = (
        "PASS_C3_BI_K0P15_ZERO_PAIR_LOCAL_45S_HP_M1_EXACT_RESUME_"
        "SUPERSESSION_SCOPE_CORRECTED_CANDIDATE_ONLY"
        if payload["pair_pass"] is True
        else "REVIEW_C3_BI_K0P15_SUPERSESSION_SCOPE_UNCLOSED"
    )
    protected_after = canonical_sha256(scientific_snapshot(payload))
    if protected_after != protected_before:
        raise RuntimeError("KMPC-141 protected scientific values changed")
    architecture = require_mapping(
        payload.get("process_architecture"), "process architecture"
    )
    architecture["read_only_supersession_scope_correction"] = {
        "source_run_id": SOURCE_RUN_ID,
        "source_receipt": source_path.name,
        "source_receipt_sha256": EXPECTED_SOURCE_SHA256,
        "worker_calls": 0,
        "solver_calls": 0,
        "CPQR_calls": 0,
        "physics_executed": False,
        "thresholds_changed": False,
        "scientific_values_changed": 0,
        "protected_scientific_snapshot_sha256_before": protected_before,
        "protected_scientific_snapshot_sha256_after": protected_after,
        "corrections": corrections,
    }
    source_hashes = require_mapping(payload.get("source_hashes"), "source hashes")
    source_hashes[source_path.name] = EXPECTED_SOURCE_SHA256
    source_hashes[runner_path.name] = sha256_file(runner_path)
    return payload, architecture[
        "read_only_supersession_scope_correction"
    ]


def validate_corrected(payload: Mapping[str, object]) -> dict[str, bool]:
    variants = require_mapping(payload.get("variants"), "variants")
    hp_audit = require_mapping(
        payload.get("HP_M1_exact_resume_audit"), "HP exact audit"
    )
    checks = {
        "run_id_corrected": payload.get("run_id") == RUN_ID,
        "pair_pass": payload.get("pair_pass") is True,
        "exact_pass": payload.get("HP_M1_exact_resume_pass") is True,
    }
    for variant in VARIANTS:
        row = require_mapping(variants.get(variant), f"variant {variant}")
        evidence = require_mapping(
            require_mapping(row.get("audit_solve"), "audit solve").get(
                "exact_resume_supersession"
            ),
            "exact evidence",
        )
        checks[f"{variant}/actual_supersession_driver_only"] = (
            evidence.get("superseded_checks") == [DRIVER_CHECK]
        )
        checks[f"{variant}/holdout_confirmed"] = (
            evidence.get("already_passing_exactly_confirmed") == [HOLDOUT_CHECK]
        )
        checks[f"{variant}/evidence_pass"] = evidence.get("pass") is True
        checks[f"{variant}/audit_pass"] = require_mapping(
            row.get("audit_solve"), "audit solve"
        ).get("pass") is True
        checks[f"{variant}/core_pass"] = row.get("core_pass") is True
        checks[f"{variant}/logical_pass"] = row.get("logical_atom_pass") is True
        checks[f"{variant}/hp_audit_pass"] = require_mapping(
            hp_audit.get(variant), "HP audit variant"
        ).get("pass") is True
    return checks


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Read-only KMPC-141 correction of the frozen KMPC-140 "
            "supersession-scope equality false negative."
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
        raise ValueError("KMPC-141 is frozen to BI/k=0.15")
    if args.max_runtime_seconds != MAX_RUNTIME_SECONDS:
        raise ValueError("KMPC-141 read-only limit must remain exactly 4.8 s")
    result_dir = args.result_dir.resolve()
    started = time.monotonic()
    source_path, source = load_source(result_dir)
    source_checks = validate_source(source)
    if not all(source_checks.values()):
        failed = sorted(name for name, value in source_checks.items() if not value)
        raise RuntimeError("KMPC-141 source validation failed: " + ",".join(failed))
    runner_path = Path(__file__).resolve()
    corrected, correction_register = apply_correction(
        source, source_path, runner_path
    )
    corrected_checks = validate_corrected(corrected)
    if not all(corrected_checks.values()):
        failed = sorted(name for name, value in corrected_checks.items() if not value)
        raise RuntimeError("KMPC-141 correction validation failed: " + ",".join(failed))
    elapsed = time.monotonic() - started
    if elapsed > args.max_runtime_seconds:
        raise TimeoutError("KMPC-141 read-only runtime exceeded 4.8 s")
    if args.smoke:
        print(json.dumps({
            "run_id": RUN_ID,
            "mode": "SMOKE_NO_PHYSICS",
            "source_checks": source_checks,
            "corrected_checks": corrected_checks,
            "correction_register": correction_register,
            "physics_executed": False,
            "worker_calls": 0,
            "solver_calls": 0,
            "pass": True,
        }, indent=2, sort_keys=True, allow_nan=False))
        return 0
    output = (
        args.output.resolve()
        if args.output is not None
        else (result_dir / OUTPUT_NAME).resolve()
    )
    if output.parent != result_dir or output.name != OUTPUT_NAME:
        raise ValueError("official output must use the frozen name inside result-dir")
    corrected["runtime_seconds"] = elapsed
    try:
        write_immutable_json(output, corrected)
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
            "source_receipt": source_path.name,
            "source_receipt_sha256": EXPECTED_SOURCE_SHA256,
            "physics_executed": False,
            "worker_calls": 0,
            "solver_calls": 0,
            "score_effect": "NONE",
            "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
            "source_hashes": {runner_path.name: sha256_file(runner_path)},
        }
        write_immutable_json(failure_path, failure)
        print(f"{RUN_ID} technical failure receipt: {failure_path}", file=sys.stderr)
        return 3
    print(json.dumps({
        "run_id": RUN_ID,
        "output": str(output),
        "candidate_interpretation_not_verdict": corrected[
            "candidate_interpretation_not_verdict"
        ],
        "pair_pass": corrected["pair_pass"],
        "HP_M1_exact_resume_pass": corrected["HP_M1_exact_resume_pass"],
        "runtime_seconds": elapsed,
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
