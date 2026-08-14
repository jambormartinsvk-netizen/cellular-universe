#!/usr/bin/env python3
"""Reconstruct the A2-K5-K1 canonical coupled-scalar action on A1-K1.

Candidate action (Einstein frame):

  S = integral sqrt(-g)[Mpl^2 R/2 - (partial phi)^2/2 - V(phi)]
      + S_c[A(phi)^2 g, psi_c] + S_b[g] + S_r[g].

With varphi=phi/Mpl and beta=d ln A/d varphi, the A1-K1 background fixes

  varphi_x = sqrt(3 delta X_f)/E,
  beta      = lambda sqrt(X_f)/(X_c sqrt(3 delta)),
  V/(3 H0^2 Mpl^2) = (1-w_f)X_f/2.

The script checks exact recovery of Q=Gamma rho_f, reconstructs A(varphi)
and V(varphi), and estimates the scalar/effective mass and massless-limit
dark fifth-force factor 1+2 beta^2.  It does not compute a likelihood.
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
SPEC = importlib.util.spec_from_file_location("k5_k1_background", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load validated background: {BASE_PATH}")
BASE13 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE13
SPEC.loader.exec_module(BASE13)


def cumulative_trapezoid(values: np.ndarray, xs: np.ndarray) -> np.ndarray:
    out = np.zeros_like(values)
    increments = 0.5 * (values[1:] + values[:-1]) * np.diff(xs)
    out[1:] = np.cumsum(increments)
    return out


def interpolate(xs: np.ndarray, values: np.ndarray, x: float) -> float:
    return float(np.interp(x, xs, values))


def run(step: float) -> dict:
    p = BASE13.BASE.ModelParameters()
    x_star = -math.log1p(p.z_star)
    settings = BASE13.BASE.IntegrationSettings(x_min=x_star, step=step)
    xs_desc, states_desc, xb0 = BASE13.integrate_background(p, settings)
    xs = xs_desc[::-1]
    states = states_desc[::-1]

    xf, xm, xr = states.T
    xb = xb0 * np.exp(-3.0 * xs)
    xc = xm - xb
    e = np.sqrt(xf + xm + xr)
    w = -1.0 + p.delta

    varphi_x = np.sqrt(3.0 * p.delta * xf) / e
    varphi = cumulative_trapezoid(varphi_x, xs)
    varphi -= varphi[-1]  # varphi(today)=0; past values are negative.

    beta = p.lam * np.sqrt(xf) / (xc * math.sqrt(3.0 * p.delta))
    dln_a_dx = beta * varphi_x
    ln_a_integrated = cumulative_trapezoid(dln_a_dx, xs)
    ln_a_integrated -= ln_a_integrated[-1]
    ln_a_mass_identity = np.log(xc * np.exp(3.0 * xs) / xc[-1])

    potential = 0.5 * (1.0 - w) * xf
    xf_x = -3.0 * p.delta * xf - p.lam * xf / e
    potential_x = 0.5 * (1.0 - w) * xf_x
    potential_varphi = potential_x / varphi_x
    potential_varphi2 = np.gradient(
        potential_varphi, xs, edge_order=2
    ) / varphi_x
    beta_varphi = np.gradient(beta, xs, edge_order=2) / varphi_x

    scalar_mass2_over_h02 = 3.0 * potential_varphi2
    effective_mass2_over_h02 = 3.0 * (
        potential_varphi2 + xc * (beta_varphi + beta**2)
    )
    massless_geff_over_g = 1.0 + 2.0 * beta**2

    source_ratio = beta * xc * e * varphi_x / (p.lam * xf)
    reconstruction_error = np.max(np.abs(source_ratio - 1.0))
    mass_identity_error = np.max(
        np.abs(ln_a_integrated - ln_a_mass_identity)
    )

    sample_redshifts = [p.z_star, 10.0, 3.0, 1.0, 0.0]
    samples = {}
    for z in sample_redshifts:
        x = -math.log1p(z)
        key = f"z={z:g}"
        samples[key] = {
            "varphi": interpolate(xs, varphi, x),
            "beta": interpolate(xs, beta, x),
            "A_over_A0": math.exp(interpolate(xs, ln_a_integrated, x)),
            "V_over_3H0sqMplsq": interpolate(xs, potential, x),
            "mphi2_over_H0sq": interpolate(xs, scalar_mass2_over_h02, x),
            "meff2_over_H0sq": interpolate(xs, effective_mass2_over_h02, x),
            "massless_Geff_over_G": interpolate(xs, massless_geff_over_g, x),
        }

    checks = {
        "positive_background_densities": bool(
            np.all(xf > 0.0) and np.all(xc > 0.0)
        ),
        "canonical_kinetic_energy_positive": bool(
            np.all(p.delta * xf > 0.0)
        ),
        "field_is_monotonic": bool(np.all(varphi_x > 0.0)),
        "Q_equals_Gamma_rho_f": bool(reconstruction_error < 1.0e-12),
        "mass_function_identity_recovered": bool(mass_identity_error < 1.0e-7),
        "all_reconstructed_functions_finite": bool(
            np.all(np.isfinite(varphi))
            and np.all(np.isfinite(beta))
            and np.all(np.isfinite(potential))
            and np.all(np.isfinite(effective_mass2_over_h02))
        ),
    }
    passed = all(checks.values())
    return {
        "step": step,
        "parameters": {
            "lambda": p.lam,
            "delta": p.delta,
            "w_f": w,
            "z_star": p.z_star,
        },
        "field_excursion_varphi_zstar_to_today": float(-varphi[0]),
        "beta_min": float(np.min(beta)),
        "beta_today": float(beta[-1]),
        "massless_Geff_over_G_today": float(massless_geff_over_g[-1]),
        "scalar_mass2_over_H0sq_today": float(scalar_mass2_over_h02[-1]),
        "effective_mass2_over_H0sq_today": float(effective_mass2_over_h02[-1]),
        "max_abs_Q_reconstruction_error": float(reconstruction_error),
        "max_abs_lnA_mass_identity_error": float(mass_identity_error),
        "samples": samples,
        "checks": checks,
        "status": "PASS_ACTION_RECONSTRUCTION" if passed else "FAIL",
    }


def main() -> int:
    coarse = run(5.0e-4)
    fine = run(2.5e-4)
    keys = [
        "field_excursion_varphi_zstar_to_today",
        "beta_today",
        "massless_Geff_over_G_today",
        "scalar_mass2_over_H0sq_today",
        "effective_mass2_over_H0sq_today",
    ]
    convergence = {
        key: abs(coarse[key] - fine[key]) / max(abs(fine[key]), 1.0e-300)
        for key in keys
    }
    converged = all(value < 1.0e-5 for value in convergence.values())
    passed = (
        coarse["status"] == "PASS_ACTION_RECONSTRUCTION"
        and fine["status"] == "PASS_ACTION_RECONSTRUCTION"
        and converged
    )
    output = {
        "test": "A2-K5-K1 canonical coupled-scalar reconstruction",
        "action": (
            "Einstein gravity + canonical phi + V(phi) + "
            "CDM coupled to A(phi)^2 g; baryons/radiation minimal"
        ),
        "coarse": coarse,
        "fine": fine,
        "convergence_relative_differences": convergence,
        "convergence_threshold": 1.0e-5,
        "status": "PASS_K5_K1_ACTION_GATE" if passed else "REQUIRES_REVIEW",
        "warning": (
            "Passing reconstruction, ghost, and gradient gates is not an "
            "observational verdict. beta and the fifth force require a full "
            "linear-growth audit."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

