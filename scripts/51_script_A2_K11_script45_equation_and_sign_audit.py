#!/usr/bin/env python3
"""Audit successor for script 45 (proposed A2-K11/K1b drag track).

The original script 45 is preserved unchanged.  This successor implements
the already sign-audited A2-K1 equations and adds a genuine momentum force.

Conventions:
  metric signature (-,+,+,+), theta_A=-k^2 v_A,
  u_A=H0 theta_A/k^2, x=ln(a), Gamma=lambda H0,
  gamma_drag=g H0 is a *physical* proper-time rate.

Energy transfer:
  Q_c^mu = Gamma rho_f u_c^mu + F_c^mu,
  Q_f^mu = -Q_c^mu.

For a damping force on c the sign must be
  F_c^mu = +gamma rho_c h_c^{mu nu} u_{f,nu},
not the minus sign printed in the submitted claim.  The plus sign gives
dv_c/dt=gamma(v_f-v_c).  The submitted minus sign is also tested and is
labelled anti_drag.

The complete fuel equations include the rest-frame sound-speed conversion
for c_s,f^2=1 and the sign-audited A2-K1 term
Gamma/(1+w_f)*(2 theta_f-theta_c).  Interaction rates in x-time scale as
lambda/E and gamma/E, not lambda/(aE) or gamma/(aE).
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np
from scipy.integrate import solve_ivp


BASE_PATH = Path(__file__).with_name(
    "13_script_A1_K1_cdm_background_audit_exact_zstar.py"
)
SPEC = importlib.util.spec_from_file_location("a1_background_k11_audit", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load validated A1 background: {BASE_PATH}")
BASE13 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE13
SPEC.loader.exec_module(BASE13)

DC, UC, DF, UF, DB, UB, DR, UR, PHI = range(9)


def build_background(lam: float, step: float) -> tuple[object, np.ndarray, dict]:
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
    x_star = -math.log1p(p.z_star)
    settings = BASE13.BASE.IntegrationSettings(x_min=x_star, step=step)
    xs_desc, states_desc, xb0 = BASE13.integrate_background(p, settings)
    xs = xs_desc[::-1]
    states = states_desc[::-1]
    xf, xm, xr = states.T
    xb = xb0 * np.exp(-3.0 * xs)
    xc = xm - xb
    e = np.sqrt(xf + xm + xr)
    return p, xs, {"xf": xf, "xc": xc, "xb": xb, "xr": xr, "E": e}


def interp_coeff(x: float, xs: np.ndarray, coeff: dict) -> dict[str, float]:
    return {key: float(np.interp(x, xs, value)) for key, value in coeff.items()}


def phi_x(y: np.ndarray, c: dict, delta: float, x: float) -> float:
    a = math.exp(x)
    momentum = (
        c["xc"] * y[UC]
        + c["xb"] * y[UB]
        + (4.0 / 3.0) * c["xr"] * y[UR]
        + delta * c["xf"] * y[UF]
    )
    return -y[PHI] + 1.5 * a * momentum / c["E"]


def corrected_rhs(
    x: float,
    y: np.ndarray,
    c: dict,
    q: float,
    lam: float,
    delta: float,
    gamma_signed: float,
) -> np.ndarray:
    """Full audited fluid equations plus signed physical drag."""
    a = math.exp(x)
    e = c["E"]
    w = -1.0 + delta
    phix = phi_x(y, c, delta, x)
    energy_rate_x = lam / e
    drag_rate_x = gamma_signed / e

    out = np.zeros_like(y)

    # CDM: Q || u_c leaves its Euler equation unchanged; only F_c acts.
    out[DC] = (
        -(q * q) * y[UC] / (a * e)
        + 3.0 * phix
        + energy_rate_x * c["xf"] / c["xc"]
        * (y[DF] - y[DC] + y[PHI])
    )
    out[UC] = (
        -y[UC]
        + y[PHI] / (a * e)
        + drag_rate_x * (y[UF] - y[UC])
    )

    # Fuel continuity includes the c_s^2=1 to Newtonian-gauge conversion.
    out[DF] = (
        -3.0 * (1.0 - w) * y[DF]
        - delta * (q * q) * y[UF] / (a * e)
        - 9.0 * a * e * (1.0 - w * w) * y[UF]
        + 3.0 * delta * phix
        - energy_rate_x * y[PHI]
        - 3.0 * a * lam * (1.0 - w) * y[UF]
    )

    # The energy-transfer term is anti-damping for fuel->CDM:
    # +(lambda/delta E)*(2u_f-u_c).  Momentum drag is the separate damping
    # +(gamma/delta E)*(rho_c/rho_f)*(u_c-u_f).
    out[UF] = (
        2.0 * y[UF]
        + (y[DF] / delta + y[PHI]) / (a * e)
        + energy_rate_x / delta * (2.0 * y[UF] - y[UC])
        + drag_rate_x * c["xc"] / (delta * c["xf"])
        * (y[UC] - y[UF])
    )

    out[DB] = -(q * q) * y[UB] / (a * e) + 3.0 * phix
    out[UB] = -y[UB] + y[PHI] / (a * e)
    out[DR] = -(4.0 / 3.0) * (q * q) * y[UR] / (a * e) + 4.0 * phix
    out[UR] = (y[DR] / 4.0 + y[PHI]) / (a * e)
    out[PHI] = phix
    return out


def initial_relative_mode(c0: dict, delta: float) -> np.ndarray:
    inertia = c0["xc"] + delta * c0["xf"]
    y = np.zeros(9)
    y[UF] = c0["xc"] / inertia
    y[UC] = -delta * c0["xf"] / inertia
    return y


def constraint(x: float, y: np.ndarray, dy: np.ndarray, c: dict, q: float) -> tuple[float, float]:
    a = math.exp(x)
    density = (
        c["xc"] * y[DC] + c["xb"] * y[DB]
        + c["xr"] * y[DR] + c["xf"] * y[DF]
    )
    terms = np.array(
        [
            q * q * y[PHI],
            3.0 * (a * c["E"]) ** 2 * (dy[PHI] + y[PHI]),
            1.5 * a * a * density,
        ]
    )
    return abs(float(np.sum(terms))), float(np.sum(np.abs(terms)))


def run(step: float, q: float, lam: float, gamma_signed: float) -> dict:
    p, xs, coeff = build_background(lam, step)
    c0 = {key: float(value[0]) for key, value in coeff.items()}
    y0 = initial_relative_mode(c0, p.delta)
    rel0 = y0[UF] - y0[UC]

    def ode(x: float, y: np.ndarray) -> np.ndarray:
        c = interp_coeff(x, xs, coeff)
        return corrected_rhs(x, y, c, q, lam, p.delta, gamma_signed)

    sol = solve_ivp(
        ode,
        (float(xs[0]), float(xs[-1])),
        y0,
        method="Radau",
        t_eval=xs,
        rtol=2.0e-9,
        atol=2.0e-11,
    )
    if not sol.success:
        raise RuntimeError(sol.message)

    residuals = []
    norms = []
    for x, y in zip(xs, sol.y.T):
        c = interp_coeff(float(x), xs, coeff)
        dy = corrected_rhs(float(x), y, c, q, lam, p.delta, gamma_signed)
        residual, norm = constraint(float(x), y, dy, c, q)
        residuals.append(residual)
        norms.append(norm)
    residuals = np.asarray(residuals)
    norms = np.asarray(norms)
    active = norms > max(float(np.max(norms)) * 1.0e-10, 1.0e-20)
    max_relative_active = float(
        np.max(residuals[active] / norms[active]) if np.any(active) else 0.0
    )

    yf = sol.y[:, -1]
    relf = yf[UF] - yf[UC]
    return {
        "step": step,
        "q": q,
        "lambda": lam,
        "gamma_signed": gamma_signed,
        "force_interpretation": (
            "physical_drag_plus_projector" if gamma_signed > 0.0
            else "submitted_minus_projector_anti_drag" if gamma_signed < 0.0
            else "no_drag"
        ),
        "initial_relative_velocity": float(rel0),
        "final_relative_velocity": float(relf),
        "absolute_transfer": float(abs(relf / rel0)),
        "final_delta_c": float(yf[DC]),
        "final_delta_f": float(yf[DF]),
        "final_Phi": float(yf[PHI]),
        "max_abs_state": float(np.max(np.abs(sol.y))),
        "max_abs_00_residual": float(np.max(residuals)),
        "max_relative_00_residual_active": max_relative_active,
        "max_00_term_norm": float(np.max(norms)),
        "all_finite": bool(np.all(np.isfinite(sol.y))),
    }


def main() -> int:
    q = 1.0e-5
    lam = 0.15
    gamma = 0.03
    fine_step = 1.25e-4
    coarse_step = 2.5e-4

    no_drag = run(fine_step, q, lam, 0.0)
    physical_drag = run(fine_step, q, lam, +gamma)
    physical_drag_coarse = run(coarse_step, q, lam, +gamma)
    physical_drag_half_k = run(fine_step, q / 2.0, lam, +gamma)
    submitted_minus = run(fine_step, q, lam, -gamma)
    full_null = run(fine_step, q, 0.0, 0.0)

    step_log_error = abs(
        math.log(max(physical_drag["absolute_transfer"], 1.0e-300))
        - math.log(max(physical_drag_coarse["absolute_transfer"], 1.0e-300))
    ) / max(abs(math.log(max(physical_drag["absolute_transfer"], 1.0e-300))), 1.0)
    k_log_error = abs(
        math.log(max(physical_drag["absolute_transfer"], 1.0e-300))
        - math.log(max(physical_drag_half_k["absolute_transfer"], 1.0e-300))
    ) / max(abs(math.log(max(physical_drag["absolute_transfer"], 1.0e-300))), 1.0)

    output = {
        "test": "Audit successor of script 45 / proposed A2-K11 direct drag",
        "equation_corrections": {
            "proper_time_rates_in_x": "lambda/E and gamma/E; script45 used extra 1/a",
            "cdm_Euler_energy_term": "zero for Q parallel u_c; script45 added Q/rho_c damping",
            "fuel_energy_Euler": "+lambda/(delta E)*(2u_f-u_c); script45 used opposite damping",
            "fuel_pressure": "delta_f/delta plus full nonadiabatic continuity terms",
            "force_sign": "plus projector is damping; submitted minus projector is anti-drag",
        },
        "no_drag_correct_K1": no_drag,
        "physical_drag_gamma_plus_0p03": physical_drag,
        "physical_drag_coarse": physical_drag_coarse,
        "physical_drag_half_k": physical_drag_half_k,
        "submitted_minus_force": submitted_minus,
        "lambda_gamma_zero_null": full_null,
        "step_log_transfer_relative_difference": step_log_error,
        "k_log_transfer_relative_difference": k_log_error,
        "drag_gain_relative_to_correct_K1": (
            physical_drag["absolute_transfer"] / no_drag["absolute_transfer"]
        ),
        "submitted_minus_gain_relative_to_correct_K1": (
            submitted_minus["absolute_transfer"] / no_drag["absolute_transfer"]
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
