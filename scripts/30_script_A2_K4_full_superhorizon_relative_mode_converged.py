#!/usr/bin/env python3
"""Converged successor to A2-K4 scripts 28 and 29.

Script 29 exposed two numerical-diagnostic issues: its 5e-4/2.5e-4 pair did
not satisfy the fixed 1e-7 step gate, and a pointwise relative Einstein
residual becomes ill-conditioned when all constraint terms cross zero.

This successor keeps script 28's equations, initial mode, physical thresholds,
and k values.  It uses steps 1.25e-4/6.25e-5 and reports the global constraint
norm max|C|/max(sum|C_i|), in addition to the preserved pointwise diagnostic.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np


BASE_PATH = Path(__file__).with_name(
    "28_script_A2_K4_full_superhorizon_relative_mode.py"
)
SPEC = importlib.util.spec_from_file_location("a2_k4_equations", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load script 28: {BASE_PATH}")
BASE28 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE28
SPEC.loader.exec_module(BASE28)


def raw_constraint_terms(x, y, dy, state, xb0, kappa):
    xf, xc, xb, xr, e = BASE28.component_background(x, state, xb0)
    a = math.exp(x)
    density = (
        xc*y[BASE28.DC] + xf*y[BASE28.DF]
        + xb*y[BASE28.DB] + xr*y[BASE28.DR]
    )
    return np.array(
        [
            (kappa**2)*y[BASE28.PHI],
            3.0*(a*e)**2*(dy[BASE28.PHI]+y[BASE28.PHI]),
            1.5*a**2*density,
        ],
        dtype=float,
    )


def run_refined(step: float, kappa: float, lam: float) -> dict:
    defaults = BASE28.BASE13.BASE.ModelParameters()
    p = BASE28.BASE13.BASE.ModelParameters(
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
    settings = BASE28.BASE13.BASE.IntegrationSettings(x_min=x_star, step=step)
    xs_desc, states_desc, xb0 = BASE28.BASE13.integrate_background(p, settings)
    xs = xs_desc[::-1]
    states = states_desc[::-1]

    xf0, xc0, _, _, _ = BASE28.component_background(xs[0], states[0], xb0)
    inertia = xc0+p.delta*xf0
    y = np.zeros(9, dtype=float)
    y[BASE28.UC] = -p.delta*xf0/inertia
    y[BASE28.UF] = xc0/inertia
    initial_relative = float(y[BASE28.UF]-y[BASE28.UC])

    max_abs_residual = 0.0
    max_term_norm = 0.0
    max_pointwise_relative = 0.0
    initial_abs = 0.0

    for i in range(len(xs)):
        if i > 0:
            x0, x1 = float(xs[i-1]), float(xs[i])
            dx = x1-x0
            s0, s1 = states[i-1], states[i]
            sm = 0.5*(s0+s1)
            xm = 0.5*(x0+x1)
            k1 = BASE28.rhs(x0, y, s0, xb0, p, kappa)
            k2 = BASE28.rhs(xm, y+0.5*dx*k1, sm, xb0, p, kappa)
            k3 = BASE28.rhs(xm, y+0.5*dx*k2, sm, xb0, p, kappa)
            k4 = BASE28.rhs(x1, y+dx*k3, s1, xb0, p, kappa)
            y = y+dx*(k1+2*k2+2*k3+k4)/6.0

        dy = BASE28.rhs(float(xs[i]), y, states[i], xb0, p, kappa)
        terms = raw_constraint_terms(float(xs[i]), y, dy, states[i], xb0, kappa)
        residual = abs(float(np.sum(terms)))
        term_norm = float(np.sum(np.abs(terms)))
        if i == 0:
            initial_abs = residual
        max_abs_residual = max(max_abs_residual, residual)
        max_term_norm = max(max_term_norm, term_norm)
        if term_norm > 1.0e-20:
            max_pointwise_relative = max(
                max_pointwise_relative, residual/term_norm
            )

    final_relative = float(y[BASE28.UF]-y[BASE28.UC])
    return {
        "step": float(step),
        "k_over_H0": float(kappa),
        "lambda": float(lam),
        "initial_relative_velocity": initial_relative,
        "initial_abs_00_constraint": float(initial_abs),
        "final_relative_velocity": final_relative,
        "absolute_relative_velocity_growth": float(
            abs(final_relative/initial_relative)
        ),
        "final_delta_c": float(y[BASE28.DC]),
        "final_delta_f": float(y[BASE28.DF]),
        "final_Phi": float(y[BASE28.PHI]),
        "max_abs_00_constraint_residual": float(max_abs_residual),
        "max_constraint_term_norm": float(max_term_norm),
        "global_relative_00_constraint_residual": float(
            max_abs_residual/max(max_term_norm, 1.0e-300)
        ),
        "max_pointwise_relative_00_residual_above_floor": float(
            max_pointwise_relative
        ),
        "all_finite": bool(np.all(np.isfinite(y))),
    }


def main() -> int:
    lam = BASE28.BASE13.BASE.ModelParameters().lam
    coupled_coarse = run_refined(1.25e-4, 1.0e-5, lam)
    coupled_fine = run_refined(6.25e-5, 1.0e-5, lam)
    coupled_half_k = run_refined(6.25e-5, 5.0e-6, lam)
    uncoupled_fine = run_refined(6.25e-5, 1.0e-5, 0.0)

    interaction_gain = float(
        coupled_fine["absolute_relative_velocity_growth"]
        / uncoupled_fine["absolute_relative_velocity_growth"]
    )
    log_coarse = math.log(coupled_coarse["absolute_relative_velocity_growth"])
    log_fine = math.log(coupled_fine["absolute_relative_velocity_growth"])
    step_convergence = float(abs(log_coarse-log_fine)/abs(log_fine))
    k_convergence = float(
        abs(
            math.log(coupled_half_k["absolute_relative_velocity_growth"])
            - log_fine
        )/abs(log_fine)
    )

    checks = {
        "all_runs_finite": bool(all(
            r["all_finite"] for r in
            (coupled_coarse, coupled_fine, coupled_half_k, uncoupled_fine)
        )),
        "initial_00_constraint_satisfied": bool(
            coupled_fine["initial_abs_00_constraint"] < 1.0e-12
        ),
        "step_converged": bool(step_convergence < 1.0e-7),
        "superhorizon_k_converged": bool(k_convergence < 1.0e-7),
        "constraint_controlled": bool(
            coupled_fine["global_relative_00_constraint_residual"] < 1.0e-5
        ),
        # Preserved physical kill threshold from scripts 28--29.
        "interaction_adds_more_than_one_efold": bool(interaction_gain > math.e),
    }
    dead = bool(all(checks.values()))
    output = {
        "test": "A2-K4 converged full first superhorizon relative mode",
        "successor_to": [
            "28_script_A2_K4_full_superhorizon_relative_mode.py",
            "29_script_A2_K4_full_superhorizon_relative_mode_serialized.py",
        ],
        "physics_change": "none",
        "numerical_change": (
            "steps 1.25e-4/6.25e-5; global Einstein-constraint norm"
        ),
        "coupled_coarse": coupled_coarse,
        "coupled_fine": coupled_fine,
        "coupled_half_k": coupled_half_k,
        "uncoupled_fine": uncoupled_fine,
        "interaction_relative_velocity_gain": interaction_gain,
        "interaction_log_gain": float(math.log(interaction_gain)),
        "step_log_growth_relative_difference": step_convergence,
        "k_log_growth_relative_difference": k_convergence,
        "checks": checks,
        "verdict": "MRTVA_A2_K4" if dead else "REQUIRES_FULL_REVIEW",
        "scope": (
            "First superhorizon perfect-fluid test. It includes densities, "
            "baryons, perfect radiation, Phi, 00/0i Einstein constraints, and "
            "the K4 interaction; it does not replace the A3 Boltzmann hierarchy."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if dead else 1


if __name__ == "__main__":
    raise SystemExit(main())

