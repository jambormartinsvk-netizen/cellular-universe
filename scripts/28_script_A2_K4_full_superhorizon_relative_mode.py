#!/usr/bin/env python3
"""Full first superhorizon test for A2-K4 on the A1-K1 background.

This integrates the k/H0 << 1 perfect-fluid system in Newtonian gauge using
V_A=theta_A/k^2 and u_A=H0 V_A.  The initial condition is a physical
dark-sector velocity-isocurvature mode: its total dark momentum vanishes,
while u_f-u_c=1.  Hence it is a representative of a gauge-invariant relative
velocity mode, not a common coordinate boost.

The coupled K4 model is compared with a separately conserved Gamma=0 model
having the same present-day density parameters.  Both backgrounds are
integrated by validated script 13.  The 00 Einstein constraint is monitored.
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
SPEC = importlib.util.spec_from_file_location("a2_k4_background", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load validated background: {BASE_PATH}")
BASE13 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE13
SPEC.loader.exec_module(BASE13)


# y = [delta_c,u_c,delta_f,u_f,delta_b,u_b,delta_r,u_r,Phi]
DC, UC, DF, UF, DB, UB, DR, UR, PHI = range(9)


def component_background(x: float, state: np.ndarray, xb0: float):
    xf, xm, xr = (float(v) for v in state)
    xb = xb0 * math.exp(-3.0 * x)
    xc = xm - xb
    e2 = xf + xm + xr
    if min(xf, xb, xc, xr, e2) <= 0.0:
        raise FloatingPointError("Non-positive background component in K4 test")
    return xf, xc, xb, xr, math.sqrt(e2)


def rhs(
    x: float,
    y: np.ndarray,
    state: np.ndarray,
    xb0: float,
    p,
    kappa: float,
) -> np.ndarray:
    xf, xc, xb, xr, e = component_background(x, state, xb0)
    a = math.exp(x)
    d = p.delta
    r = xf / xc
    zeta = d * xf / (xc + d * xf)
    lam_over_e = p.lam / e

    momentum = xc * y[UC] + d * xf * y[UF] + xb * y[UB] + (4.0/3.0) * xr * y[UR]
    dphi = -y[PHI] + 1.5 * a * momentum / e

    out = np.zeros_like(y)
    out[DC] = (
        -(kappa**2) * y[UC] / (a * e)
        + 3.0 * dphi
        + lam_over_e * r * (y[DF] - y[DC] + y[PHI])
    )
    out[UC] = (
        -y[UC]
        + y[PHI] / (a * e)
        + lam_over_e * r * zeta * (y[UF] - y[UC])
    )

    out[DF] = (
        -3.0 * (1.0 - p.delta + 1.0) * y[DF]
        - d * (kappa**2) * y[UF] / (a * e)
        - 9.0 * a * e * (1.0 - (-1.0 + d)**2) * y[UF]
        + 3.0 * d * dphi
        - lam_over_e * y[PHI]
        - 3.0 * a * p.lam * (1.0 - (-1.0 + d)) * y[UF]
    )
    out[UF] = (
        2.0 * y[UF]
        + (y[DF] / d + y[PHI]) / (a * e)
        + (lam_over_e / d)
        * ((2.0 - zeta) * y[UF] - (1.0 - zeta) * y[UC])
    )

    out[DB] = -(kappa**2) * y[UB] / (a * e) + 3.0 * dphi
    out[UB] = -y[UB] + y[PHI] / (a * e)
    out[DR] = -(4.0/3.0) * (kappa**2) * y[UR] / (a * e) + 4.0 * dphi
    out[UR] = (y[DR] / 4.0 + y[PHI]) / (a * e)
    out[PHI] = dphi
    return out


def constraint_residual(
    x: float,
    y: np.ndarray,
    dy: np.ndarray,
    state: np.ndarray,
    xb0: float,
    kappa: float,
) -> tuple[float, float]:
    xf, xc, xb, xr, e = component_background(x, state, xb0)
    a = math.exp(x)
    density = xc*y[DC] + xf*y[DF] + xb*y[DB] + xr*y[DR]
    terms = [
        (kappa**2) * y[PHI],
        3.0 * (a*e)**2 * (dy[PHI] + y[PHI]),
        1.5 * a**2 * density,
    ]
    residual = float(sum(terms))
    scale = max(sum(abs(v) for v in terms), 1.0e-300)
    return residual, abs(residual) / scale


def run(step: float, kappa: float, lam: float) -> dict[str, float | bool]:
    defaults = BASE13.BASE.ModelParameters()
    p = BASE13.BASE.ModelParameters(
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
    settings = BASE13.BASE.IntegrationSettings(x_min=-25.0, step=step)
    xs_desc, states_desc, xb0 = BASE13.integrate_background(p, settings)
    x_star = -math.log1p(p.z_star)
    i_star = int(np.flatnonzero(np.isclose(xs_desc, x_star, rtol=0.0, atol=1e-13))[0])
    xs = xs_desc[:i_star+1][::-1]
    states = states_desc[:i_star+1][::-1]

    xf0, xc0, _, _, _ = component_background(xs[0], states[0], xb0)
    inertia = xc0 + p.delta * xf0
    y = np.zeros(9, dtype=float)
    y[UC] = -p.delta * xf0 / inertia
    y[UF] = xc0 / inertia
    initial_relative = y[UF] - y[UC]

    max_constraint = 0.0
    initial_dy = rhs(xs[0], y, states[0], xb0, p, kappa)
    initial_abs_constraint, initial_rel_constraint = constraint_residual(
        xs[0], y, initial_dy, states[0], xb0, kappa
    )

    for i in range(len(xs)-1):
        x0, x1 = float(xs[i]), float(xs[i+1])
        dx = x1 - x0
        s0, s1 = states[i], states[i+1]
        sm = 0.5 * (s0+s1)
        xm = 0.5 * (x0+x1)
        k1 = rhs(x0, y, s0, xb0, p, kappa)
        k2 = rhs(xm, y+0.5*dx*k1, sm, xb0, p, kappa)
        k3 = rhs(xm, y+0.5*dx*k2, sm, xb0, p, kappa)
        k4 = rhs(x1, y+dx*k3, s1, xb0, p, kappa)
        y = y + dx*(k1+2*k2+2*k3+k4)/6.0
        dy = rhs(x1, y, s1, xb0, p, kappa)
        _, rel_constraint = constraint_residual(x1, y, dy, s1, xb0, kappa)
        max_constraint = max(max_constraint, rel_constraint)

    final_relative = float(y[UF]-y[UC])
    return {
        "step": step,
        "k_over_H0": kappa,
        "lambda": lam,
        "initial_relative_velocity": float(initial_relative),
        "initial_abs_00_constraint": initial_abs_constraint,
        "initial_relative_00_constraint": initial_rel_constraint,
        "final_relative_velocity": final_relative,
        "absolute_relative_velocity_growth": abs(final_relative/initial_relative),
        "final_delta_c": float(y[DC]),
        "final_delta_f": float(y[DF]),
        "final_Phi": float(y[PHI]),
        "max_relative_00_constraint_residual": max_constraint,
        "all_finite": bool(np.all(np.isfinite(y))),
    }


def main() -> int:
    default_lam = BASE13.BASE.ModelParameters().lam
    coupled_coarse = run(5.0e-4, 1.0e-5, default_lam)
    coupled_fine = run(2.5e-4, 1.0e-5, default_lam)
    coupled_khalf = run(2.5e-4, 5.0e-6, default_lam)
    uncoupled_fine = run(2.5e-4, 1.0e-5, 0.0)

    interaction_gain = (
        coupled_fine["absolute_relative_velocity_growth"]
        / uncoupled_fine["absolute_relative_velocity_growth"]
    )
    log_growth_coarse = math.log(coupled_coarse["absolute_relative_velocity_growth"])
    log_growth_fine = math.log(coupled_fine["absolute_relative_velocity_growth"])
    step_convergence = abs(log_growth_coarse-log_growth_fine) / abs(log_growth_fine)
    k_convergence = abs(
        math.log(coupled_khalf["absolute_relative_velocity_growth"])
        - log_growth_fine
    ) / abs(log_growth_fine)

    checks = {
        "all_runs_finite": all(
            r["all_finite"] for r in
            (coupled_coarse, coupled_fine, coupled_khalf, uncoupled_fine)
        ),
        "initial_00_constraint_satisfied": (
            coupled_fine["initial_abs_00_constraint"] < 1.0e-12
        ),
        "step_converged": step_convergence < 1.0e-7,
        "superhorizon_k_converged": k_convergence < 1.0e-7,
        "constraint_controlled": (
            coupled_fine["max_relative_00_constraint_residual"] < 1.0e-5
        ),
        "interaction_adds_more_than_one_efold": interaction_gain > math.e,
    }
    dead = all(checks.values())
    output = {
        "test": "A2-K4 full first superhorizon relative-velocity mode",
        "gauge_invariant_mode": (
            "initial total dark momentum zero; u_f-u_c=1; radiation frame fixed"
        ),
        "coupled_coarse": coupled_coarse,
        "coupled_fine": coupled_fine,
        "coupled_half_k": coupled_khalf,
        "uncoupled_fine": uncoupled_fine,
        "interaction_relative_velocity_gain": interaction_gain,
        "interaction_log_gain": math.log(interaction_gain),
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

