#!/usr/bin/env python3
"""Converged successor to script 22 for the A2-K1 superhorizon test.

Script 22 obtained the physical amplification but failed its deliberately
strict 1e-8 integration-convergence gate when comparing steps 1e-3 and 5e-4.
This successor preserves script 22 and repeats the same calculation with
steps 5e-4 and 2.5e-4.  No physics equation or threshold is changed.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys


BASE_PATH = Path(__file__).with_name(
    "22_script_A2_K1_superhorizon_velocity_instability.py"
)
SPEC = importlib.util.spec_from_file_location("a2_k1_superhorizon_base", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load script 22: {BASE_PATH}")
BASE22 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE22
SPEC.loader.exec_module(BASE22)


def main() -> int:
    coarse = BASE22.run(5.0e-4)
    fine = BASE22.run(2.5e-4)

    exponent_rel_difference = abs(
        coarse["interaction_exponent_zstar_to_today"]
        - fine["interaction_exponent_zstar_to_today"]
    ) / abs(fine["interaction_exponent_zstar_to_today"])

    checks = {
        "background_time_converged": exponent_rel_difference < 1.0e-8,
        "instability_rate_exceeds_H0": fine["lambda_over_delta"] > 1.0,
        "more_than_one_interaction_efold_since_recombination": (
            fine["interaction_exponent_zstar_to_today"] > 1.0
        ),
    }
    dead = all(checks.values())

    output = {
        "test": "A2-K1 first superhorizon relative-velocity mode",
        "successor_to": "22_script_A2_K1_superhorizon_velocity_instability.py",
        "derivation": (
            "d ln(V_f/V_f_uncoupled)/dt = 2 Gamma/delta; "
            "Gamma=lambda H0"
        ),
        "parameters": {
            "lambda": BASE22.BASE13.BASE.ModelParameters().lam,
            "delta": BASE22.BASE13.BASE.ModelParameters().delta,
            "z_star": BASE22.BASE13.BASE.ModelParameters().z_star,
        },
        "coarse": coarse,
        "fine": fine,
        "convergence": {
            "relative_exponent_difference": exponent_rel_difference,
            "threshold": 1.0e-8,
        },
        "checks": checks,
        "verdict": "MRTVA_A2_K1" if dead else "REQUIRES_FULL_REVIEW",
        "scope": (
            "Kills the specified constant-rate, w>-1, Q^mu parallel u_c "
            "closure through its admitted gauge-invariant relative-velocity "
            "mode; it does not kill A1 background bookkeeping or alternative "
            "A2 transfer tracks."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if dead else 1


if __name__ == "__main__":
    raise SystemExit(main())

