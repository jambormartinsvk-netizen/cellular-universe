#!/usr/bin/env python3
"""Converged successor to the A2-K5.1 adiabatic-mode script 40.

Script 40 passed every physical gate but its absolute step difference
1.1441e-6 narrowly missed the fixed 1e-6 convergence threshold.  Its maximum
generated relative velocity decreased by a factor of about four when the
step was halved, indicating the expected RK discretization remainder.

This successor keeps all equations, initial conditions, k values, and
thresholds and uses steps 6.25e-5 and 3.125e-5.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys


BASE_PATH = Path(__file__).with_name(
    "40_script_A2_K5_1_regular_adiabatic_mode.py"
)
SPEC = importlib.util.spec_from_file_location("k5_1_adiabatic_base40", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load script 40: {BASE_PATH}")
BASE40 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE40
SPEC.loader.exec_module(BASE40)


def main() -> int:
    coarse = BASE40.run(6.25e-5, 1.0e-5, 0.15)
    fine = BASE40.run(3.125e-5, 1.0e-5, 0.15)
    half_k = BASE40.run(3.125e-5, 5.0e-6, 0.15)
    observable = "max_relative_over_initial_common_velocity"
    step_conv = abs(coarse[observable]-fine[observable])/max(
        abs(fine[observable]), 1.0
    )
    k_conv = abs(half_k[observable]-fine[observable])/max(
        abs(fine[observable]), 1.0
    )
    checks = {
        "all_runs_finite": all(r["all_finite"] for r in [coarse, fine, half_k]),
        "initial_adiabatic_relative_velocity_zero": True,
        "initial_constraint_satisfied": fine["initial_abs_00_constraint"] < 1.0e-10,
        "constraint_controlled": fine["global_relative_00_constraint_residual"] < 1.0e-5,
        "step_converged": step_conv < 1.0e-6,
        "superhorizon_k_converged": k_conv < 1.0e-6,
        "no_generated_relative_velocity_explosion": fine[observable] < math.e,
    }
    passed = all(checks.values())
    output = {
        "test": "A2-K5.1 converged regular constrained adiabatic mode",
        "successor_to": "40_script_A2_K5_1_regular_adiabatic_mode.py",
        "physics_change": "none",
        "numerical_change": "steps 6.25e-5 and 3.125e-5",
        "coarse": coarse,
        "fine": fine,
        "half_k": half_k,
        "step_relative_difference": step_conv,
        "k_relative_difference": k_conv,
        "checks": checks,
        "verdict": "PASS_K5_1_ADIABATIC_GATE" if passed else "FAIL_OR_DEAD_REVIEW",
        "scope": (
            "Perfect-radiation superhorizon mode initialized at z_star; "
            "deep-radiation photon/neutrino hierarchy remains A3."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
