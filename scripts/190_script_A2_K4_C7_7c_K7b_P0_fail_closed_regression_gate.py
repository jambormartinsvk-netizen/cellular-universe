#!/usr/bin/env python
"""Bounded positive and negative regression gate for K7b P0.

The gate compares the NID physics payload from 189 bit-for-bit with 175,
runs the unchanged NIV coefficient gates, and proves that three synthetic
missing-rank-key cases fail closed.  It does not integrate an ODE or add score.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time


HERE = Path(__file__).resolve().parent
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
EXPECTED = {
    ("NID", "deep"): (5.9511e-3, 9.4022e-6, 8.5918e-13),
    ("NID", "shallow"): (1.0921e-4, 8.0083e-6, 6.3485e-12),
    ("NIV", "deep"): (None, 3.2127e-5, 3.5503e-11),
    ("NIV", "shallow"): (None, 3.8442e-5, 2.6233e-10),
}


def parse_json(text: str) -> dict[str, object]:
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        raise RuntimeError("child returned no JSON object")
    return json.loads(text[start:end + 1])


def fingerprint(payload: dict[str, object], keys: tuple[str, ...]) -> str:
    subset = {key: payload.get(key) for key in keys}
    canonical = json.dumps(
        subset, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def rounded_regression_ok(actual: object, expected: float) -> bool:
    value = float(actual)
    return abs(value - expected) / max(abs(expected), 1e-300) <= 1e-4


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, required=True)
    parser.add_argument("--child-runtime-seconds", type=float, default=8.0)
    args = parser.parse_args()
    if not 10.0 <= args.max_runtime_seconds <= 20.0:
        parser.error("max-runtime-seconds must be in [10,20]")
    if not 5.0 <= args.child_runtime_seconds <= 8.0:
        parser.error("child-runtime-seconds must be in [5,8]")

    started = time.monotonic()
    checks: dict[str, bool] = {}
    results: dict[str, object] = {}

    def run(script: str, arguments: list[str]) -> tuple[int, dict[str, object]]:
        remaining = args.max_runtime_seconds - (time.monotonic() - started)
        if remaining <= 0.5:
            raise TimeoutError("P0 aggregate deadline exceeded before child")
        completed = subprocess.run(
            [sys.executable, str(HERE / script), *arguments],
            capture_output=True,
            text=True,
            timeout=min(args.child_runtime_seconds + 1.0, remaining),
            check=False,
        )
        return completed.returncode, parse_json(completed.stdout)

    def profile_args(mode: str, surface: str) -> list[str]:
        return [
            "--max-runtime-seconds", str(args.child_runtime_seconds),
            "--source-runtime-seconds", "5",
            "--mode", mode,
            "--surface", surface,
            "--dps", "80",
        ]

    positive_deep_dynamics_fingerprint = ""
    for mode, surface in EXPECTED:
        key = f"{mode}_{surface}"
        expected_d, expected_state, expected_rhs = EXPECTED[(mode, surface)]
        arguments = profile_args(mode, surface)

        if mode == "NID":
            base_exit, baseline = run(
                "175_script_A2_K4_C7_7c_K7b3b1_physical_mu_constraint_gate.py",
                arguments,
            )
            candidate_exit, candidate = run(
                "189_script_A2_K4_C7_7c_K7b3b2_fail_closed_physical_mu_gate.py",
                arguments,
            )
            base_fp = fingerprint(baseline, PHYSICS_KEYS)
            candidate_fp = fingerprint(candidate, PHYSICS_KEYS)
            dynamics_fp = fingerprint(candidate, DYNAMICS_KEYS)
            if surface == "deep":
                positive_deep_dynamics_fingerprint = dynamics_fp
            child_checks = dict(candidate.get("checks", {}))
            solver = dict(candidate.get(
                "K7b3b_hard_constrained_standard_solver", {}
            ))
            request = dict(candidate.get("profile_request", {}))
            checks[f"{key}_baseline_exit_zero"] = base_exit == 0
            checks[f"{key}_candidate_exit_zero"] = candidate_exit == 0
            checks[f"{key}_candidate_pass_verdict"] = (
                candidate.get("execution_verdict")
                == "PASS_C7_7C_K7B3B2_FAIL_CLOSED_PHYSICAL_MU_GATE"
            )
            checks[f"{key}_profile_identity"] = (
                request.get("mode") == mode and request.get("surface") == surface
            )
            checks[f"{key}_all_candidate_checks_true"] = (
                bool(child_checks) and all(bool(value) for value in child_checks.values())
            )
            checks[f"{key}_physics_fingerprint_exact"] = base_fp == candidate_fp
            checks[f"{key}_rank_gate_true"] = all(
                child_checks.get(name) is True for name in RANK_CHECKS
            )
            checks[f"{key}_solver_counts_exact"] = (
                solver.get("fixed_count") == 30
                and solver.get("free_count") == 58
                and solver.get("reduced_rank") == 58
                and solver.get("hard_conflict_count") == 0
                and float(solver.get("fixed_max_absolute_error", "inf")) < 1e-60
            )
            payload = candidate
            results[key] = {
                "baseline_exit": base_exit,
                "candidate_exit": candidate_exit,
                "execution_verdict": candidate.get("execution_verdict"),
                "baseline_physics_sha256": base_fp,
                "candidate_physics_sha256": candidate_fp,
            }
        else:
            child_exit, payload = run(
                "166_script_A2_K4_C7_7c_K7b1_high_precision_coefficient_constraint_audit.py",
                arguments,
            )
            child_checks = dict(payload.get("checks", {}))
            request = dict(payload.get("profile_request", {}))
            checks[f"{key}_exit_zero"] = child_exit == 0
            checks[f"{key}_pass_verdict"] = (
                payload.get("execution_verdict")
                == "PASS_C7_7C_K7B1_COEFFICIENT_CONSTRAINT_AUDIT"
            )
            checks[f"{key}_profile_identity"] = (
                request.get("mode") == mode and request.get("surface") == surface
            )
            checks[f"{key}_all_checks_true"] = (
                bool(child_checks) and all(bool(value) for value in child_checks.values())
            )
            results[key] = {
                "exit": child_exit,
                "execution_verdict": payload.get("execution_verdict"),
            }

        actual_state = payload.get("worst_state_residual_over_allowance")
        actual_rhs = payload.get("worst_rhs_residual_over_allowance")
        checks[f"{key}_rounded_state_regression"] = rounded_regression_ok(
            actual_state, expected_state
        )
        checks[f"{key}_rounded_rhs_regression"] = rounded_regression_ok(
            actual_rhs, expected_rhs
        )
        if expected_d is not None:
            checks[f"{key}_rounded_D_activity_regression"] = rounded_regression_ok(
                payload.get("D_activity_relative_error"), expected_d
            )
        results[key].update({
            "D_activity_relative_error": payload.get("D_activity_relative_error"),
            "worst_state_residual_over_allowance": actual_state,
            "worst_rhs_residual_over_allowance": actual_rhs,
        })

    negative: dict[str, object] = {}
    for fault in ("reduced_rank", "free_count", "both"):
        arguments = profile_args("NID", "deep") + [
            "--fault-remove-rank-key", fault
        ]
        exit_code, payload = run(
            "189_script_A2_K4_C7_7c_K7b3b2_fail_closed_physical_mu_gate.py",
            arguments,
        )
        child_checks = dict(payload.get("checks", {}))
        failed = {name for name, value in child_checks.items() if not bool(value)}
        metadata = dict(payload.get("rank_fault_injection", {}))
        expected_removed = (
            {"reduced_rank", "free_count"} if fault == "both" else {fault}
        )
        checks[f"negative_{fault}_exit_one"] = exit_code == 1
        checks[f"negative_{fault}_review_verdict"] = (
            payload.get("execution_verdict")
            == "REVIEW_C7_7C_K7B3B2_FAIL_CLOSED_PHYSICAL_MU_UNCLOSED"
        )
        checks[f"negative_{fault}_exact_failed_checks"] = failed == RANK_CHECKS
        checks[f"negative_{fault}_metadata_exact"] = (
            metadata.get("requested") == fault
            and set(metadata.get("removed", [])) == expected_removed
        )
        checks[f"negative_{fault}_dynamics_unchanged"] = (
            fingerprint(payload, DYNAMICS_KEYS)
            == positive_deep_dynamics_fingerprint
        )
        negative[fault] = {
            "exit": exit_code,
            "execution_verdict": payload.get("execution_verdict"),
            "failed_checks": sorted(failed),
            "removed": metadata.get("removed"),
        }

    passed = bool(checks) and all(checks.values())
    output = {
        "test": "A2-K4 C7.7c K7b P0 fail-closed regression gate",
        "positive_profiles": results,
        "negative_controls": negative,
        "checks": checks,
        "execution_verdict": (
            "PASS_C7_7C_K7B_P0_FAIL_CLOSED_REGRESSION"
            if passed else "REVIEW_C7_7C_K7B_P0_FAIL_CLOSED_UNCLOSED"
        ),
        "physical_verdict": (
            "rank metadata gate hardened; prior K7b physics unchanged; no ODE claim"
            if passed else "no K4 death verdict; audit first failed regression check"
        ),
        "fine_depth": "66.5/100",
        "score_effect": "NONE",
        "runtime_limits_seconds": {
            "total": args.max_runtime_seconds,
            "per_child": args.child_runtime_seconds,
        },
        "runtime_seconds": time.monotonic() - started,
        "scope_limit": "metadata validation and coefficient/constraint regression only",
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.TimeoutExpired as exc:
        print(json.dumps({
            "execution_verdict": "TIMEOUT_UNCLOSED",
            "error": repr(exc),
        }, indent=2))
        raise SystemExit(124)
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

