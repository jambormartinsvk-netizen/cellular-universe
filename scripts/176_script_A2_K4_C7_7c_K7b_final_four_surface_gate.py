#!/usr/bin/env python
"""Bounded four-surface composite gate for final K7b adjudication.

NID uses the physical-mu hard-constrained gate 175. NIV retains the original
K7b.1 gate 166 because the preregistered NID D-prime coefficient floor was not
present there. This script adds no equation, tolerance, ODE or score.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import time


HERE = Path(__file__).resolve().parent


def parse_json(text: str) -> dict[str, object]:
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        raise RuntimeError("child returned no JSON object")
    return json.loads(text[start:end + 1])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, required=True)
    parser.add_argument("--child-runtime-seconds", type=float, default=8.0)
    args = parser.parse_args()
    if not 10 <= args.max_runtime_seconds <= 25:
        parser.error("max-runtime-seconds must be in [10,25]")
    if not 5 <= args.child_runtime_seconds <= 9:
        parser.error("child-runtime-seconds must be in [5,9]")

    started = time.monotonic()
    profiles = (
        ("NID", "deep", "175_script_A2_K4_C7_7c_K7b3b1_physical_mu_constraint_gate.py",
         "PASS_C7_7C_K7B3B1_PHYSICAL_MU_CONSTRAINT_GATE"),
        ("NID", "shallow", "175_script_A2_K4_C7_7c_K7b3b1_physical_mu_constraint_gate.py",
         "PASS_C7_7C_K7B3B1_PHYSICAL_MU_CONSTRAINT_GATE"),
        ("NIV", "deep", "166_script_A2_K4_C7_7c_K7b1_high_precision_coefficient_constraint_audit.py",
         "PASS_C7_7C_K7B1_COEFFICIENT_CONSTRAINT_AUDIT"),
        ("NIV", "shallow", "166_script_A2_K4_C7_7c_K7b1_high_precision_coefficient_constraint_audit.py",
         "PASS_C7_7C_K7B1_COEFFICIENT_CONSTRAINT_AUDIT"),
    )
    results: dict[str, object] = {}
    checks: dict[str, bool] = {}

    for mode, surface, script, expected in profiles:
        elapsed = time.monotonic() - started
        if elapsed >= args.max_runtime_seconds:
            raise TimeoutError("K7b composite deadline exceeded before next child")
        command = [
            sys.executable, str(HERE / script),
            "--max-runtime-seconds", str(args.child_runtime_seconds),
            "--source-runtime-seconds", "5",
            "--mode", mode, "--surface", surface, "--dps", "80",
        ]
        timeout = min(args.child_runtime_seconds + 1,
                      args.max_runtime_seconds - elapsed)
        child = subprocess.run(command, capture_output=True, text=True,
                               timeout=timeout, check=False)
        payload = parse_json(child.stdout)
        key = f"{mode}_{surface}"
        child_checks = dict(payload.get("checks", {}))
        checks[f"{key}_exit_zero"] = child.returncode == 0
        checks[f"{key}_expected_verdict"] = payload.get("execution_verdict") == expected
        checks[f"{key}_all_registered_checks_true"] = (
            bool(child_checks) and all(bool(value) for value in child_checks.values())
        )
        request = dict(payload.get("profile_request", {}))
        checks[f"{key}_profile_identity"] = (
            request.get("mode") == mode and request.get("surface") == surface
        )
        results[key] = {
            "script": script,
            "return_code": child.returncode,
            "execution_verdict": payload.get("execution_verdict"),
            "runtime_seconds": payload.get("runtime_seconds"),
            "D_activity_relative_error": payload.get("D_activity_relative_error"),
            "failed_checks": [name for name, value in child_checks.items() if not bool(value)],
            "worst_state_residual_over_allowance": payload.get(
                "worst_state_residual_over_allowance"
            ),
            "worst_rhs_residual_over_allowance": payload.get(
                "worst_rhs_residual_over_allowance"
            ),
        }

    passed = bool(checks) and all(checks.values())
    output = {
        "test": "A2-K4 C7.7c-K7b final four-surface composite gate",
        "profiles": results,
        "checks": checks,
        "execution_verdict": (
            "PASS_C7_7C_K7B_FINAL_FOUR_SURFACE_GATE"
            if passed else "REVIEW_C7_7C_K7B_FINAL_UNCLOSED"
        ),
        "physical_verdict": (
            "K7b coefficient and initial-constraint gate passed; no ODE claim"
            if passed else "no death verdict; audit first failed child"
        ),
        "fine_depth": "66.5/100",
        "scope_limit": "no ODE evolution, endpoint agreement, step convergence, or score award",
        "runtime_limits_seconds": {
            "total": args.max_runtime_seconds,
            "per_child": args.child_runtime_seconds,
        },
        "runtime_seconds": time.monotonic() - started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.TimeoutExpired as exc:
        print(json.dumps({"execution_verdict": "TIMEOUT_UNCLOSED",
                          "error": repr(exc)}, indent=2))
        raise SystemExit(124)
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict": "TIMEOUT_UNCLOSED",
                          "error": str(exc)}, indent=2))
        raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution_verdict": "ERROR_UNCLOSED",
                          "error": repr(exc)}, indent=2))
        raise SystemExit(1)
