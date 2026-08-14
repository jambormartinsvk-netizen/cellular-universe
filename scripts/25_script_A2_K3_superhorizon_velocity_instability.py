#!/usr/bin/env python3
"""A2-K3 superhorizon relative-velocity test on the A1-K1 background.

Track A2-K3 uses

    Q_f^mu = -Gamma rho_f u_f^mu,
    Q_c^mu = +Gamma rho_f u_f^mu,

with w_f=-1+delta and c_s,f^2=1.  Mapping equations (36)--(38) of
arXiv:1109.6234 requires Gamma_ref=-Gamma_cell.  The admitted
large-scale homogeneous fuel-velocity mode therefore obeys

    d ln(V_f/V_f,Gamma=0)/dt = Gamma/delta.

The relative velocity V_f-V_c is gauge invariant.  This script reuses the
same validated background integrator and convergence gate as A2-K1.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys


BASE_PATH = Path(__file__).with_name(
    "22_script_A2_K1_superhorizon_velocity_instability.py"
)
SPEC = importlib.util.spec_from_file_location("a2_k1_background_tools", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load background tools: {BASE_PATH}")
BASE22 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE22
SPEC.loader.exec_module(BASE22)


def evaluate(step: float) -> dict[str, float]:
    base = BASE22.run(step)
    exponent = 0.5 * base["interaction_exponent_zstar_to_today"]
    return {
        "step": step,
        "lambda_over_delta": base["lambda_over_delta"],
        "H0_Delta_t_zstar_to_today": base["H0_Delta_t_zstar_to_today"],
        "interaction_exponent_zstar_to_today": exponent,
        "amplification_zstar_to_today": math.exp(exponent),
    }


def main() -> int:
    coarse = evaluate(5.0e-4)
    fine = evaluate(2.5e-4)
    relative_difference = abs(
        coarse["interaction_exponent_zstar_to_today"]
        - fine["interaction_exponent_zstar_to_today"]
    ) / abs(fine["interaction_exponent_zstar_to_today"])

    checks = {
        "background_time_converged": relative_difference < 1.0e-8,
        # Clemson et al. Eq. (41): threshold is approximately 2 for Q || u_f.
        "reference_K3_instability_threshold_exceeded": (
            fine["lambda_over_delta"] > 2.0
        ),
        "more_than_one_interaction_efold_since_recombination": (
            fine["interaction_exponent_zstar_to_today"] > 1.0
        ),
    }
    dead = all(checks.values())

    output = {
        "test": "A2-K3 gauge-invariant superhorizon relative-velocity mode",
        "model": "Q_f^mu=-Gamma rho_f u_f^mu; Gamma=lambda H0>0",
        "mapping": "Gamma_ref=-Gamma_cell; 1+w_f=delta>0; alpha=1",
        "parameters": {
            "lambda": BASE22.BASE13.BASE.ModelParameters().lam,
            "delta": BASE22.BASE13.BASE.ModelParameters().delta,
            "z_star": BASE22.BASE13.BASE.ModelParameters().z_star,
        },
        "coarse": coarse,
        "fine": fine,
        "convergence": {
            "relative_exponent_difference": relative_difference,
            "threshold": 1.0e-8,
        },
        "checks": checks,
        "verdict": "MRTVA_A2_K3" if dead else "REQUIRES_FULL_REVIEW",
        "scope": (
            "Tests the constant-rate, w_f>-1, c_s,f^2=1, Q^mu parallel "
            "u_f closure. It does not decide A2-K4 or A2-K5."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if dead else 1


if __name__ == "__main__":
    raise SystemExit(main())

