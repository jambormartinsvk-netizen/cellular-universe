#!/usr/bin/env python
"""Offline-only aggregate of the nine preregistered K7b P0 segment files."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "Audit"
MANIFEST = AUDIT / "A2_K4_K7B_P0_SEGMENT_MANIFEST_2026-07-15.json"
PHYSICS_KEYS = (
    "background",
    "projected_seeds",
    "state_comparison",
    "projected_rhs_audit",
    "worst_state_residual_over_allowance",
    "worst_rhs_residual_over_allowance",
    "D_activity_relative_error",
    "K7b3b_hard_constrained_standard_solver",
)
DYNAMICS_KEYS = tuple(
    key for key in PHYSICS_KEYS
    if key != "K7b3b_hard_constrained_standard_solver"
)
RANK_CHECKS = {
    "reduced_standard_rank_keys_present",
    "reduced_standard_rank_values_plain_int",
    "reduced_standard_system_full_rank",
}
EXPECTED_METRICS = {
    "B-NID-D": (5.9511e-3, 9.4022e-6, 8.5918e-13),
    "B-NID-S": (1.0921e-4, 8.0083e-6, 6.3485e-12),
    "C-NID-D": (5.9511e-3, 9.4022e-6, 8.5918e-13),
    "C-NID-S": (1.0921e-4, 8.0083e-6, 6.3485e-12),
    "NIV-D": (None, 3.2127e-5, 3.5503e-11),
    "NIV-S": (None, 3.8442e-5, 2.6233e-10),
}
EXPECTED_POSITIVE_VERDICTS = {
    "B-NID-D": "PASS_C7_7C_K7B3B1_PHYSICAL_MU_CONSTRAINT_GATE",
    "B-NID-S": "PASS_C7_7C_K7B3B1_PHYSICAL_MU_CONSTRAINT_GATE",
    "C-NID-D": "PASS_C7_7C_K7B3B2A_FAIL_CLOSED_PHYSICAL_MU_GATE",
    "C-NID-S": "PASS_C7_7C_K7B3B2A_FAIL_CLOSED_PHYSICAL_MU_GATE",
    "NIV-D": "PASS_C7_7C_K7B1_COEFFICIENT_CONSTRAINT_AUDIT",
    "NIV-S": "PASS_C7_7C_K7B1_COEFFICIENT_CONSTRAINT_AUDIT",
}
EXPECTED_FAULT = {"F-R": "reduced_rank", "F-F": "free_count", "F-B": "both"}


def canonical_fingerprint(payload: dict[str, object], keys: tuple[str, ...]) -> str:
    subset = {key: payload.get(key) for key in keys}
    encoded = json.dumps(
        subset, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def rounded_ok(actual: object, expected: float) -> bool:
    value = float(actual)
    return abs(value - expected) / max(abs(expected), 1e-300) <= 1e-4


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, required=True)
    args = parser.parse_args()
    if not 1.0 <= args.max_runtime_seconds <= 5.0:
        parser.error("max-runtime-seconds must be in [1,5]")
    started = time.monotonic()

    manifest_bytes = MANIFEST.read_bytes()
    manifest = json.loads(manifest_bytes.decode("utf-8"))
    case_meta = dict(manifest.get("cases", {}))
    expected_case_names = set(EXPECTED_METRICS) | set(EXPECTED_FAULT)
    checks: dict[str, bool] = {
        "manifest_case_names_exact": set(case_meta) == expected_case_names,
    }
    payloads: dict[str, dict[str, object]] = {}
    raw_hashes: dict[str, str] = {}

    for case in sorted(expected_case_names):
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("offline aggregate deadline exceeded")
        meta = dict(case_meta.get(case, {}))
        path = AUDIT / str(meta.get("file", ""))
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest().upper()
        raw_hashes[case] = digest
        checks[f"{case}_raw_hash_matches_manifest"] = (
            digest == str(meta.get("sha256", "")).upper()
        )
        expected_exit = 0 if case in EXPECTED_METRICS else 1
        checks[f"{case}_observed_exit_matches_preregistration"] = (
            meta.get("observed_exit") == expected_exit
        )
        payloads[case] = json.loads(raw.decode("utf-8"))

    for case, (expected_d, expected_state, expected_rhs) in EXPECTED_METRICS.items():
        payload = payloads[case]
        child_checks = dict(payload.get("checks", {}))
        checks[f"{case}_positive_verdict"] = (
            payload.get("execution_verdict") == EXPECTED_POSITIVE_VERDICTS[case]
        )
        checks[f"{case}_all_child_checks_true"] = (
            bool(child_checks) and all(bool(value) for value in child_checks.values())
        )
        checks[f"{case}_state_metric_regression"] = rounded_ok(
            payload.get("worst_state_residual_over_allowance"), expected_state
        )
        checks[f"{case}_rhs_metric_regression"] = rounded_ok(
            payload.get("worst_rhs_residual_over_allowance"), expected_rhs
        )
        if expected_d is not None:
            checks[f"{case}_D_metric_regression"] = rounded_ok(
                payload.get("D_activity_relative_error"), expected_d
            )

    for baseline, candidate in (("B-NID-D", "C-NID-D"), ("B-NID-S", "C-NID-S")):
        checks[f"{candidate}_physics_fingerprint_exact"] = (
            canonical_fingerprint(payloads[baseline], PHYSICS_KEYS)
            == canonical_fingerprint(payloads[candidate], PHYSICS_KEYS)
        )
        solver = dict(payloads[candidate].get(
            "K7b3b_hard_constrained_standard_solver", {}
        ))
        child_checks = dict(payloads[candidate].get("checks", {}))
        checks[f"{candidate}_rank_checks_true"] = all(
            child_checks.get(name) is True for name in RANK_CHECKS
        )
        checks[f"{candidate}_solver_counts_exact"] = (
            solver.get("fixed_count") == 30
            and solver.get("free_count") == 58
            and solver.get("reduced_rank") == 58
            and solver.get("hard_conflict_count") == 0
            and float(solver.get("fixed_max_absolute_error", "inf")) < 1e-60
        )

    positive_deep_dynamics = canonical_fingerprint(
        payloads["C-NID-D"], DYNAMICS_KEYS
    )
    for case, fault in EXPECTED_FAULT.items():
        payload = payloads[case]
        child_checks = dict(payload.get("checks", {}))
        failed = {name for name, value in child_checks.items() if not bool(value)}
        metadata = dict(payload.get("rank_fault_injection", {}))
        expected_removed = (
            {"reduced_rank", "free_count"} if fault == "both" else {fault}
        )
        checks[f"{case}_review_verdict"] = (
            payload.get("execution_verdict")
            == "REVIEW_C7_7C_K7B3B2A_FAIL_CLOSED_PHYSICAL_MU_UNCLOSED"
        )
        checks[f"{case}_exact_failed_rank_checks"] = failed == RANK_CHECKS
        checks[f"{case}_fault_metadata_exact"] = (
            metadata.get("requested") == fault
            and set(metadata.get("removed", [])) == expected_removed
        )
        checks[f"{case}_dynamics_fingerprint_exact"] = (
            canonical_fingerprint(payload, DYNAMICS_KEYS)
            == positive_deep_dynamics
        )

    passed = bool(checks) and all(checks.values())
    output = {
        "test": "A2-K4 K7b P0 segmented offline fail-closed aggregate",
        "manifest_sha256": hashlib.sha256(manifest_bytes).hexdigest(),
        "raw_output_sha256": raw_hashes,
        "physics_fingerprints": {
            case: canonical_fingerprint(payloads[case], PHYSICS_KEYS)
            for case in ("B-NID-D", "B-NID-S", "C-NID-D", "C-NID-S")
        },
        "checks": checks,
        "execution_verdict": (
            "PASS_C7_7C_K7B_P0_SEGMENTED_FAIL_CLOSED_REGRESSION"
            if passed else "REVIEW_C7_7C_K7B_P0_SEGMENTED_UNCLOSED"
        ),
        "physical_verdict": (
            "fail-open metadata defect closed; prior K7b physics exactly preserved; no ODE claim"
            if passed else "no K4 death verdict; inspect first failed offline predicate"
        ),
        "fine_depth": "66.5/100",
        "score_effect": "NONE",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "scope_limit": "offline validation only; observed exits are fixed by the signed manifest",
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({
            "execution_verdict": "TIMEOUT_UNCLOSED",
            "error": str(exc),
        }, indent=2))
        raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({
            "execution_verdict": "ERROR_UNCLOSED",
            "error": repr(exc),
        }, indent=2))
        raise SystemExit(1)

