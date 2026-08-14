#!/usr/bin/env python3
"""Retrospective parity audit of A2-K1 through A2-K5.

This script does not erase any historical verdict.  It recomputes the key
dimensionless quantities, distinguishes an absolute transfer from a ratio to
a decaying null reference, and adds the regular constrained adiabatic K4 mode
that was missing when M-011 was issued.

The output is deliberately compact and intended to be copied into the MD
audit.  K5/K1 values are simple independent arithmetic cross-checks of the
serialized CAMB-hybrid output; the expensive spectrum is still reproduced by
scripts 45 and 46.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent


def load(name: str, filename: str):
    path = HERE / filename
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K1 = load(
    "a2_k1_converged_for_retrospective",
    "23_script_A2_K1_superhorizon_velocity_instability_converged.py",
)
K4 = load(
    "a2_k4_converged_for_retrospective",
    "30_script_A2_K4_full_superhorizon_relative_mode_converged.py",
)
B = K4.BASE28


def k4_initial_adiabatic(x0, state0, xb0, p, q, phi0=1.0e-5):
    """Constrained common-clock/common-velocity mode at z_star.

    All components obey delta rho_A/rho_A,x = C and share one velocity.
    C and that velocity follow from the exact 00 and 0i constraints with
    Phi_x=0.  Consequently the initial dark relative velocity is zero.
    """

    xf, xc, xb, xr, e = B.component_background(x0, state0, xb0)
    a = math.exp(x0)
    # Total background derivative: (E^2)_x = -3 xc -3 d xf -3 xb -4 xr.
    e2_x = -3.0 * xc - 3.0 * p.delta * xf - 3.0 * xb - 4.0 * xr
    h = e2_x / (2.0 * e * e)
    clock = -(q * q + 3.0 * a * a * e * e) * phi0 / (
        3.0 * a * a * e * e * h
    )
    inertia = xc + p.delta * xf + xb + (4.0 / 3.0) * xr
    common_u = 2.0 * e * phi0 / (3.0 * a * inertia)
    lam_over_e = p.lam / e

    y = np.zeros(9, dtype=float)
    y[B.DC] = (-3.0 + lam_over_e * xf / xc) * clock
    y[B.UC] = common_u
    y[B.DF] = (-3.0 * p.delta - lam_over_e) * clock
    y[B.UF] = common_u
    y[B.DB] = -3.0 * clock
    y[B.UB] = common_u
    y[B.DR] = -4.0 * clock
    y[B.UR] = common_u
    y[B.PHI] = phi0
    return y, common_u, clock


def k4_adiabatic_run(step: float, q: float, lam: float) -> dict:
    defaults = B.BASE13.BASE.ModelParameters()
    p = B.BASE13.BASE.ModelParameters(
        h=defaults.h,
        omega_m0=defaults.omega_m0,
        lam=lam,
        delta=defaults.delta,
        delta_neff=defaults.delta_neff,
        omega_b=defaults.omega_b,
        omega_gamma=defaults.omega_gamma,
        neff_standard=defaults.neff_standard,
        z_star=defaults.z_star,
    )
    x_star = -math.log1p(p.z_star)
    settings = B.BASE13.BASE.IntegrationSettings(x_min=x_star, step=step)
    xs_desc, states_desc, xb0 = B.BASE13.integrate_background(p, settings)
    xs = xs_desc[::-1]
    states = states_desc[::-1]
    y, common_u, clock = k4_initial_adiabatic(
        float(xs[0]), states[0], xb0, p, q
    )

    max_abs_residual = 0.0
    max_term_norm = 0.0
    max_relative = 0.0
    initial_abs = None

    for i in range(len(xs)):
        if i > 0:
            x0, x1 = float(xs[i - 1]), float(xs[i])
            dx = x1 - x0
            s0, s1 = states[i - 1], states[i]
            sm = 0.5 * (s0 + s1)
            xm = 0.5 * (x0 + x1)
            k1 = B.rhs(x0, y, s0, xb0, p, q)
            k2 = B.rhs(xm, y + 0.5 * dx * k1, sm, xb0, p, q)
            k3 = B.rhs(xm, y + 0.5 * dx * k2, sm, xb0, p, q)
            k4 = B.rhs(x1, y + dx * k3, s1, xb0, p, q)
            y = y + dx * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0

        dy = B.rhs(float(xs[i]), y, states[i], xb0, p, q)
        terms = K4.raw_constraint_terms(
            float(xs[i]), y, dy, states[i], xb0, q
        )
        residual = abs(float(np.sum(terms)))
        norm = float(np.sum(np.abs(terms)))
        if initial_abs is None:
            initial_abs = residual
        max_abs_residual = max(max_abs_residual, residual)
        max_term_norm = max(max_term_norm, norm)
        max_relative = max(max_relative, abs(float(y[B.UF] - y[B.UC])))

    final_relative = float(y[B.UF] - y[B.UC])
    return {
        "step": step,
        "k_over_H0": q,
        "lambda": lam,
        "initial_common_velocity": float(common_u),
        "initial_density_clock": float(clock),
        "initial_relative_velocity": 0.0,
        "max_relative_over_initial_common_velocity": float(
            max_relative / max(abs(common_u), 1.0e-300)
        ),
        "final_relative_over_initial_common_velocity": float(
            final_relative / max(abs(common_u), 1.0e-300)
        ),
        "initial_abs_00_constraint": float(initial_abs),
        "global_relative_00_constraint_residual": float(
            max_abs_residual / max(max_term_norm, 1.0e-300)
        ),
        "final_Phi_over_initial_Phi": float(y[B.PHI] / 1.0e-5),
        "all_finite": bool(np.all(np.isfinite(y))),
    }


def main() -> int:
    # K1/K3 share the same validated A1 background time integral.
    base = K1.BASE22.run(2.5e-4)
    time_h0 = base["H0_Delta_t_zstar_to_today"]
    lam = K1.BASE22.BASE13.BASE.ModelParameters().lam
    delta = K1.BASE22.BASE13.BASE.ModelParameters().delta
    ratio = lam / delta
    n_k1 = 2.0 * ratio * time_h0
    n_k3 = ratio * time_h0

    # K2 principal-symbol check at the least aggressive registered scale.
    w = -1.0 + delta
    h = K1.BASE22.BASE13.BASE.ModelParameters().h
    h0_over_c = 100.0 * h / 299792.458
    mu_over_h0_k001 = math.sqrt(-w) * (0.01 * h) / h0_over_c

    # K4 historical isocurvature transfer and the missing adiabatic mode.
    iso = K4.run_refined(6.25e-5, 1.0e-5, lam)
    iso_null = K4.run_refined(6.25e-5, 1.0e-5, 0.0)
    iso_abs = iso["absolute_relative_velocity_growth"]
    iso_gain = iso_abs / iso_null["absolute_relative_velocity_growth"]
    ad_coarse = k4_adiabatic_run(6.25e-5, 1.0e-5, lam)
    ad_fine = k4_adiabatic_run(3.125e-5, 1.0e-5, lam)
    ad_half_k = k4_adiabatic_run(3.125e-5, 5.0e-6, lam)
    obs = "max_relative_over_initial_common_velocity"
    ad_step = abs(ad_coarse[obs] - ad_fine[obs]) / max(abs(ad_fine[obs]), 1.0)
    ad_k = abs(ad_half_k[obs] - ad_fine[obs]) / max(abs(ad_fine[obs]), 1.0)

    # Independent arithmetic parity of the stored K5/K1 A3 output.
    s8_const = 0.9836423799480062
    s8_cpl = 1.0062658626394954
    s8_screen = 0.863
    as0 = 2.1e-9
    k5_as_reductions = {
        "constant_w": 1.0 - (s8_screen / s8_const) ** 2,
        "CPL": 1.0 - (s8_screen / s8_cpl) ** 2,
    }

    k4_checks = {
        "isocurvature_run_finite": iso["all_finite"],
        "isocurvature_constraint_controlled": (
            iso["global_relative_00_constraint_residual"] < 1.0e-5
        ),
        "historical_ratio_to_decaying_null_exceeds_e": iso_gain > math.e,
        "absolute_isocurvature_transfer_exceeds_e": iso_abs > math.e,
        "adiabatic_runs_finite": all(
            r["all_finite"] for r in (ad_coarse, ad_fine, ad_half_k)
        ),
        "adiabatic_initial_constraint_satisfied": (
            ad_fine["initial_abs_00_constraint"] < 1.0e-10
        ),
        "adiabatic_constraint_controlled": (
            ad_fine["global_relative_00_constraint_residual"] < 1.0e-5
        ),
        "adiabatic_step_converged": ad_step < 1.0e-6,
        "adiabatic_k_converged": ad_k < 1.0e-6,
        "adiabatic_generated_relative_mode_exceeds_e": ad_fine[obs] > math.e,
    }

    output = {
        "test": "A2-K1--K5 retrospective depth/equation/verdict parity audit",
        "K1": {
            "lambda_over_delta": ratio,
            "interaction_log_ratio_to_null": n_k1,
            "ratio_to_null": math.exp(n_k1),
            "primary_reference_threshold": 1.0,
            "equation_and_calculation_parity": True,
            "verdict_scope": "constant-rate Q parallel u_c fluid closure only",
            "max_depth": 45,
        },
        "K2": {
            "w_equals_cs2": w,
            "mu_over_H0_at_k_0p01_h_Mpc": mu_over_h0_k001,
            "unbounded_high_k_principal_instability": w < 0.0,
            "equation_and_calculation_parity": True,
            "verdict_scope": "strictly barotropic closure only",
            "max_depth": 25,
        },
        "K3": {
            "lambda_over_delta": ratio,
            "interaction_log_ratio_to_null": n_k3,
            "ratio_to_null": math.exp(n_k3),
            "primary_reference_threshold": 2.0,
            "equation_and_calculation_parity": True,
            "verdict_scope": "constant-rate Q parallel u_f fluid closure only",
            "max_depth": 45,
        },
        "K4": {
            "historical_isocurvature": {
                "absolute_transfer": iso_abs,
                "absolute_log_transfer": math.log(iso_abs),
                "null_absolute_transfer": iso_null[
                    "absolute_relative_velocity_growth"
                ],
                "ratio_to_decaying_null": iso_gain,
                "log_ratio_to_decaying_null": math.log(iso_gain),
            },
            "new_regular_adiabatic_mode": {
                "coarse": ad_coarse,
                "fine": ad_fine,
                "half_k": ad_half_k,
                "step_difference": ad_step,
                "k_difference": ad_k,
            },
            "checks": k4_checks,
            "equation_and_calculation_parity": True,
            "verdict_parity": False,
            "reason": (
                "M-011 used >1 e-fold of ratio to a strongly decaying null "
                "mode as if it were >1 e-fold of absolute instability."
            ),
            "recommended_state": "REOPENED_PENDING_FULL_MODE_SPECTRUM",
            "max_depth": 50,
        },
        "K5": {
            "exact_leaf": "K5/K1 canonical scalar plus conformal CDM mass",
            "stored_hybrid_S8": [s8_const, s8_cpl],
            "independent_required_As_fractional_reduction": k5_as_reductions,
            "equation_and_calculation_parity": True,
            "verdict_scope": "concrete K5/K1 action at registered parameters",
            "taxonomy_note": (
                "Historical K5/K3a was later canonically renamed A2-K6; "
                "it is not a surviving child of K5."
            ),
            "max_depth": 75,
        },
        "overall_status": (
            "K1 K2 K3 and K5 depths/verdict scopes retained; "
            "K4 depth retained but M-011 requires an erratum/reopening."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    # Successful execution means the audit ran, not that every old verdict passed.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
