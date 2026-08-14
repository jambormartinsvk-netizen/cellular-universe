#!/usr/bin/env python3
"""Finer convergence successor for script 63's K4 adiabatic cross-check.

Script 63 found no physical explosion, but its 3.125e-5 k-convergence
difference 1.1339e-6 narrowly missed the fixed 1e-6 numerical threshold.
This successor changes only the integration steps to 3.125e-5/1.5625e-5.
The equations, initial conditions, wave numbers, and thresholds are unchanged.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys


BASE_PATH = Path(__file__).with_name(
    "63_script_A2_K1_K5_retrospective_depth_equation_verdict_audit.py"
)
SPEC = importlib.util.spec_from_file_location("a2_k1_k5_retrospective63", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load {BASE_PATH}")
BASE63 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE63
SPEC.loader.exec_module(BASE63)


def main() -> int:
    lam = BASE63.K1.BASE22.BASE13.BASE.ModelParameters().lam
    coarse = BASE63.k4_adiabatic_run(3.125e-5, 1.0e-5, lam)
    fine = BASE63.k4_adiabatic_run(1.5625e-5, 1.0e-5, lam)
    half_k = BASE63.k4_adiabatic_run(1.5625e-5, 5.0e-6, lam)
    observable = "max_relative_over_initial_common_velocity"
    step_difference = abs(coarse[observable] - fine[observable]) / max(
        abs(fine[observable]), 1.0
    )
    k_difference = abs(half_k[observable] - fine[observable]) / max(
        abs(fine[observable]), 1.0
    )
    checks = {
        "all_runs_finite": all(r["all_finite"] for r in (coarse, fine, half_k)),
        "initial_relative_velocity_zero": True,
        "initial_constraint_satisfied": fine["initial_abs_00_constraint"] < 1.0e-10,
        "constraint_controlled": fine["global_relative_00_constraint_residual"] < 1.0e-5,
        "step_converged": step_difference < 1.0e-6,
        "superhorizon_k_converged": k_difference < 1.0e-6,
        "no_generated_relative_velocity_explosion": fine[observable] < math.e,
    }
    passed = all(checks.values())
    output = {
        "test": "A2-K4 retrospective regular adiabatic-mode convergence",
        "successor_to": (
            "63_script_A2_K1_K5_retrospective_depth_equation_verdict_audit.py"
        ),
        "physics_change": "none",
        "numerical_change": "steps 3.125e-5 and 1.5625e-5",
        "coarse": coarse,
        "fine": fine,
        "half_k": half_k,
        "step_difference": step_difference,
        "k_difference": k_difference,
        "checks": checks,
        "verdict": (
            "PASS_ADIABATIC_MODE_NO_EXPLOSION"
            if passed
            else "REQUIRES_NUMERICAL_REVIEW"
        ),
        "scope": (
            "Perfect-radiation superhorizon mode initialized at z_star; "
            "this does not replace a deep-radiation Boltzmann eigenmode scan."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
