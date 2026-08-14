#!/usr/bin/env python3
"""A2-K1 first superhorizon test on the validated A1-K1 background.

For the active transfer

    Q_f^mu = -Gamma rho_f u_c^mu,
    Q_c^mu = +Gamma rho_f u_c^mu,

with w_f = -1 + delta and rest-frame c_s,f^2 = 1, the homogeneous
large-scale relative-velocity mode obeys

    d ln(V_f / V_f,uncoupled) / dt = 2 Gamma / delta.

This script imports the validated background integrator used by script 13,
computes H0 Delta t, and evaluates the interaction-induced amplification.
It does not integrate the full k-dependent perturbation system.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np


BASE_PATH = Path(__file__).with_name(
    "13_script_A1_K1_cdm_background_audit_exact_zstar.py"
)
SPEC = importlib.util.spec_from_file_location("a2_k1_background_base", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load validated background: {BASE_PATH}")
BASE13 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE13
SPEC.loader.exec_module(BASE13)


def dimensionless_time_between(
    xs: np.ndarray,
    states: np.ndarray,
    x_start: float,
    x_stop: float = 0.0,
) -> float:
    """Return H0 Delta t = integral dx/E between two grid points."""
    if not x_start < x_stop:
        raise ValueError("Expected x_start < x_stop")

    matches_start = np.flatnonzero(np.isclose(xs, x_start, rtol=0.0, atol=1e-13))
    matches_stop = np.flatnonzero(np.isclose(xs, x_stop, rtol=0.0, atol=1e-13))
    if len(matches_start) != 1 or len(matches_stop) != 1:
        raise ValueError("Requested endpoints must be exact integration-grid points")

    i_start = int(matches_start[0])
    i_stop = int(matches_stop[0])
    lo, hi = sorted((i_start, i_stop))
    x_segment = xs[lo : hi + 1]
    e_segment = np.sqrt(np.sum(states[lo : hi + 1], axis=1))

    order = np.argsort(x_segment)
    return float(np.trapezoid(1.0 / e_segment[order], x_segment[order]))


def run(step: float) -> dict[str, float]:
    p = BASE13.BASE.ModelParameters()
    settings = BASE13.BASE.IntegrationSettings(x_min=-25.0, step=step)
    xs, states, _ = BASE13.integrate_background(p, settings)

    x_star = -math.log1p(p.z_star)
    h0_dt_star = dimensionless_time_between(xs, states, x_star, 0.0)
    h0_dt_full = dimensionless_time_between(xs, states, settings.x_min, 0.0)

    rate_over_h0 = p.lam / p.delta
    exponent_star = 2.0 * rate_over_h0 * h0_dt_star
    exponent_full = 2.0 * rate_over_h0 * h0_dt_full

    return {
        "step": step,
        "lambda_over_delta": rate_over_h0,
        "H0_Delta_t_zstar_to_today": h0_dt_star,
        "H0_Delta_t_xmin_to_today": h0_dt_full,
        "interaction_exponent_zstar_to_today": exponent_star,
        "interaction_exponent_xmin_to_today": exponent_full,
        "amplification_zstar_to_today": math.exp(exponent_star),
        "amplification_xmin_to_today": math.exp(exponent_full),
    }


def main() -> int:
    coarse = run(1.0e-3)
    fine = run(5.0e-4)

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
        "derivation": (
            "d ln(V_f/V_f_uncoupled)/dt = 2 Gamma/delta; "
            "Gamma=lambda H0"
        ),
        "parameters": {
            "lambda": BASE13.BASE.ModelParameters().lam,
            "delta": BASE13.BASE.ModelParameters().delta,
            "z_star": BASE13.BASE.ModelParameters().z_star,
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
            "closure if the derived large-scale homogeneous mode is admitted; "
            "does not test alternative transfer tracks."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if dead else 1


if __name__ == "__main__":
    raise SystemExit(main())

