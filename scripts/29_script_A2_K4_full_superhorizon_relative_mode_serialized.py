#!/usr/bin/env python3
"""Serialized successor to A2-K4 script 28.

Script 28 completed all integrations but failed while encoding a NumPy bool
to JSON.  This successor imports the unchanged equations and run() function
from script 28 and converts output scalars to native Python types.  No
equation, initial condition, grid, or threshold is changed.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys


BASE_PATH = Path(__file__).with_name(
    "28_script_A2_K4_full_superhorizon_relative_mode.py"
)
SPEC = importlib.util.spec_from_file_location("a2_k4_full_base", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load script 28: {BASE_PATH}")
BASE28 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE28
SPEC.loader.exec_module(BASE28)


def native_run(step: float, kappa: float, lam: float) -> dict:
    raw = BASE28.run(step, kappa, lam)
    return {
        key: (bool(value) if key == "all_finite" else float(value))
        for key, value in raw.items()
    }


def main() -> int:
    default_lam = BASE28.BASE13.BASE.ModelParameters().lam
    coupled_coarse = native_run(5.0e-4, 1.0e-5, default_lam)
    coupled_fine = native_run(2.5e-4, 1.0e-5, default_lam)
    coupled_khalf = native_run(2.5e-4, 5.0e-6, default_lam)
    uncoupled_fine = native_run(2.5e-4, 1.0e-5, 0.0)

    interaction_gain = float(
        coupled_fine["absolute_relative_velocity_growth"]
        / uncoupled_fine["absolute_relative_velocity_growth"]
    )
    log_growth_coarse = math.log(
        coupled_coarse["absolute_relative_velocity_growth"]
    )
    log_growth_fine = math.log(coupled_fine["absolute_relative_velocity_growth"])
    step_convergence = float(
        abs(log_growth_coarse-log_growth_fine) / abs(log_growth_fine)
    )
    k_convergence = float(
        abs(
            math.log(coupled_khalf["absolute_relative_velocity_growth"])
            - log_growth_fine
        ) / abs(log_growth_fine)
    )

    checks = {
        "all_runs_finite": bool(
            all(
                r["all_finite"] for r in
                (coupled_coarse, coupled_fine, coupled_khalf, uncoupled_fine)
            )
        ),
        "initial_00_constraint_satisfied": bool(
            coupled_fine["initial_abs_00_constraint"] < 1.0e-12
        ),
        "step_converged": bool(step_convergence < 1.0e-7),
        "superhorizon_k_converged": bool(k_convergence < 1.0e-7),
        "constraint_controlled": bool(
            coupled_fine["max_relative_00_constraint_residual"] < 1.0e-5
        ),
        "interaction_adds_more_than_one_efold": bool(interaction_gain > math.e),
    }
    dead = bool(all(checks.values()))
    output = {
        "test": "A2-K4 full first superhorizon relative-velocity mode",
        "successor_to": "28_script_A2_K4_full_superhorizon_relative_mode.py",
        "change_from_script_28": "native JSON scalar conversion only",
        "gauge_invariant_mode": (
            "initial total dark momentum zero; u_f-u_c=1; radiation frame fixed"
        ),
        "coupled_coarse": coupled_coarse,
        "coupled_fine": coupled_fine,
        "coupled_half_k": coupled_khalf,
        "uncoupled_fine": uncoupled_fine,
        "interaction_relative_velocity_gain": interaction_gain,
        "interaction_log_gain": float(math.log(interaction_gain)),
        "step_log_growth_relative_difference": step_convergence,
        "k_log_growth_relative_difference": k_convergence,
        "checks": checks,
        "verdict": "MRTVA_A2_K4" if dead else "REQUIRES_FULL_REVIEW",
        "scope": (
            "First superhorizon perfect-fluid test only; no photon/neutrino "
            "anisotropic-stress hierarchy and no subhorizon likelihood."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if dead else 1


if __name__ == "__main__":
    raise SystemExit(main())

