#!/usr/bin/env python3
"""Full first relativistic superhorizon test for the new track A2_K11_S8_K1b.

This track implements:
1. An explicit momentum transfer force four-vector F_c^mu representing a drag
   force between dark matter (popol) and dark energy (palivo).
2. Separate Newtonian gauge equations of motion for baryons and dark matter (popol).
3. A superhorizon stability test (at k -> 0) to check if the relative velocity
   mode remains stable or explodes.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np
from scipy.integrate import solve_ivp

# Import the validated background from script 13
BASE_PATH = Path(__file__).with_name(
    "13_script_A1_K1_cdm_background_audit_exact_zstar.py"
)
SPEC = importlib.util.spec_from_file_location("s8_k1b_background", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load validated background: {BASE_PATH}")
BASE13 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE13
SPEC.loader.exec_module(BASE13)

# Variables: y = [delta_c, u_c, delta_f, u_f, delta_b, u_b, delta_r, u_r, Phi]
DC, UC, DF, UF, DB, UB, DR, UR, PHI = range(9)


def build_background(lam: float, step: float):
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
    e2 = xf + xm + xr
    e = np.sqrt(e2)

    xf_x = -3.0 * p.delta * xf - lam * xf / e
    xm_x = -3.0 * xm + lam * xf / e
    xr_x = -4.0 * xr
    e_x_over_e = 0.5 * (xf_x + xm_x + xr_x) / e2
    varphi_x = np.sqrt(3.0 * p.delta * xf) / e

    coeff = {
        "xf": xf,
        "xc": xc,
        "xb": xb,
        "xr": xr,
        "E": e,
        "E_x_over_E": e_x_over_e,
        "varphi_x": varphi_x,
    }
    return p, xs, coeff


def at_index(coeff, i):
    return {key: float(value[i]) for key, value in coeff.items()}


def phi_x_and_momentum(x, y, c, p_delta):
    a = math.exp(x)
    # Total momentum density (rho + p) * theta / H0^2
    momentum = (
        c["xc"] * y[UC]
        + c["xb"] * y[UB]
        + (4.0 / 3.0) * c["xr"] * y[UR]
        + p_delta * c["xf"] * y[UF]
    )
    phi_x = -y[PHI] + 1.5 * a * momentum / c["E"]
    return phi_x


def rhs(x, y, c, q, lam, p_delta, gamma_drag):
    a = math.exp(x)
    e = c["E"]
    phi_x = phi_x_and_momentum(x, y, c, p_delta)

    # Corrected coupling factors: physical rates divided by H = H0*E (no factor of a)
    G_c = (lam * c["xf"] / c["xc"] + gamma_drag) / e
    G_f = (lam + gamma_drag * c["xc"] / c["xf"]) / (p_delta * e)

    out = np.zeros_like(y)
    # 1. CDM (popol)
    out[DC] = -(q * q) * y[UC] / (a * e) + 3.0 * phi_x + (lam * c["xf"] / c["xc"] / e) * (y[DF] - y[DC])
    out[UC] = -(1.0 + G_c) * y[UC] + y[PHI] / (a * e) + (gamma_drag / e) * y[UF]

    # 2. Fuel (palivo)
    out[DF] = -p_delta * (q * q) * y[UF] / (a * e) + 3.0 * p_delta * phi_x - (lam / e) * (y[DF] - y[DC])
    out[UF] = 2.0 * y[UF] + (y[DF] + y[PHI]) / (a * e) + G_f * (y[UC] - y[UF])

    # 3. Baryons
    out[DB] = -(q * q) * y[UB] / (a * e) + 3.0 * phi_x
    out[UB] = -y[UB] + y[PHI] / (a * e)

    # 4. Radiation (photons/steam)
    out[DR] = -(4.0 / 3.0) * (q * q) * y[UR] / (a * e) + 4.0 * phi_x
    out[UR] = (y[DR] / 4.0 + y[PHI]) / (a * e)

    # 5. Gravitational potential
    out[PHI] = phi_x
    return out


def constraint_terms(x, y, dy, c, q, p_delta):
    a = math.exp(x)
    density = (
        c["xc"] * y[DC]
        + c["xb"] * y[DB]
        + c["xr"] * y[DR]
        + c["xf"] * y[DF]
    )
    return np.array([
        q * q * y[PHI],
        3.0 * (a * c["E"]) ** 2 * (dy[PHI] + y[PHI]),
        1.5 * a * a * density,
    ])


def initial_relative_mode(x0, c0, p_delta):
    inertia = c0["xc"] + p_delta * c0["xf"]
    uf = c0["xc"] / inertia
    uc = -p_delta * c0["xf"] / inertia

    y = np.zeros(9, dtype=float)
    y[UC] = uc
    y[UF] = uf
    return y


def run(step: float, q: float, lam: float, gamma_drag: float) -> dict:
    p, xs, coeff = build_background(lam, step)
    c0 = at_index(coeff, 0)
    y0 = initial_relative_mode(float(xs[0]), c0, p.delta)
    initial_relative = y0[UF] - y0[UC]

    # Pre-interpolate full background arrays for arbitrary step solver evaluation
    xf_arr = coeff["xf"]
    xc_arr = coeff["xc"]
    xb_arr = coeff["xb"]
    xr_arr = coeff["xr"]
    e_arr = coeff["E"]
    ex_arr = coeff["E_x_over_E"]

    def rhs_ode(x_val, y_val):
        xf_val = np.interp(x_val, xs, xf_arr)
        xc_val = np.interp(x_val, xs, xc_arr)
        xb_val = np.interp(x_val, xs, xb_arr)
        xr_val = np.interp(x_val, xs, xr_arr)
        e_val = np.interp(x_val, xs, e_arr)
        ex_val = np.interp(x_val, xs, ex_arr)

        c_interp = {
            "xf": xf_val,
            "xc": xc_val,
            "xb": xb_val,
            "xr": xr_val,
            "E": e_val,
            "E_x_over_E": ex_val
        }
        return rhs(x_val, y_val, c_interp, q, lam, p.delta, gamma_drag)

    # Solve with stiff Radau solver at extreme precision to resolve the physical floor
    sol = solve_ivp(rhs_ode, (float(xs[0]), float(xs[-1])), y0, method="Radau", t_eval=xs, rtol=1e-12, atol=1e-16)

    max_residual = 0.0
    max_term_norm = 0.0
    max_state = float(np.max(np.abs(y0)))
    initial_constraint = None

    y_table = sol.y.T # Shape (len(xs), 9)

    for i in range(len(xs)):
        y_val = y_table[i]
        c = at_index(coeff, i)
        dy = rhs(float(xs[i]), y_val, c, q, lam, p.delta, gamma_drag)
        terms = constraint_terms(float(xs[i]), y_val, dy, c, q, p.delta)
        residual = abs(float(np.sum(terms)))
        term_norm = float(np.sum(np.abs(terms)))
        if i == 0:
            initial_constraint = residual
        max_residual = max(max_residual, residual)
        max_term_norm = max(max_term_norm, term_norm)
        max_state = max(max_state, float(np.max(np.abs(y_val))))

    y_final = y_table[-1]
    final_relative = y_final[UF] - y_final[UC]
    
    return {
        "step": step,
        "k_over_H0": q,
        "lambda": lam,
        "gamma_drag": gamma_drag,
        "initial_relative_velocity": float(initial_relative),
        "final_relative_velocity": float(final_relative),
        "absolute_relative_velocity_transfer": float(
            abs(final_relative / initial_relative)
        ),
        "final_delta_c": float(y_final[DC]),
        "final_delta_f": float(y_final[DF]),
        "final_Phi": float(y_final[PHI]),
        "initial_abs_00_constraint": float(initial_constraint),
        "max_absolute_residual": float(max_residual),
        "global_relative_00_constraint_residual": float(
            max_residual / max(max_term_norm, 1.0e-300)
        ),
        "max_absolute_state": max_state,
        "all_finite": bool(np.all(np.isfinite(y_final))),
    }


def main() -> int:
    gamma_val = 0.03
    lam_val = 0.15
    q_val = 1.0e-5

    coupled_coarse = run(1.25e-4, q_val, lam_val, gamma_val)
    coupled_fine = run(6.25e-5, q_val, lam_val, gamma_val)
    coupled_half_k = run(6.25e-5, 5.0e-6, lam_val, gamma_val)
    uncoupled_fine = run(6.25e-5, q_val, lam_val, 0.0)

    transfer = coupled_fine["absolute_relative_velocity_transfer"]
    null_transfer = uncoupled_fine["absolute_relative_velocity_transfer"]
    gain = transfer / max(null_transfer, 1.0e-300)
    
    log_coarse = math.log(max(coupled_coarse["absolute_relative_velocity_transfer"], 1.0e-300))
    log_fine = math.log(max(transfer, 1.0e-300))
    step_conv = abs(log_coarse - log_fine) / max(abs(log_fine), 1.0)
    
    log_half_k = math.log(max(coupled_half_k["absolute_relative_velocity_transfer"], 1.0e-300))
    k_conv = abs(log_half_k - log_fine) / max(abs(log_fine), 1.0)

    # Damping checks
    is_damped = transfer < 1e-5 and coupled_coarse["absolute_relative_velocity_transfer"] < 1e-5

    checks = {
        "all_runs_finite": all(r["all_finite"] for r in [
            coupled_coarse, coupled_fine, coupled_half_k, uncoupled_fine
        ]),
        "initial_constraint_satisfied": coupled_fine["initial_abs_00_constraint"] < 1.0e-10,
        "step_converged": step_conv < 1.0e-6 or is_damped,
        "superhorizon_k_converged": k_conv < 1.0e-6 or is_damped,
        "constraint_controlled": (
            coupled_fine["global_relative_00_constraint_residual"] < 1.0e-5
            or coupled_fine["max_absolute_residual"] < 1.0e-8
        ),
        "no_explosive_transfer": transfer < 1.0,
    }
    passed = all(checks.values())

    output = {
        "test": "A2-K11 S8_K1b first superhorizon relative mode with momentum drag",
        "coupled_coarse": coupled_coarse,
        "coupled_fine": coupled_fine,
        "coupled_half_k": coupled_half_k,
        "uncoupled_fine": uncoupled_fine,
        "coupled_to_null_transfer_gain": gain,
        "coupled_to_null_log_gain": math.log(max(gain, 1.0e-300)),
        "step_log_transfer_relative_difference": step_conv,
        "k_log_transfer_relative_difference": k_conv,
        "checks": checks,
        "verdict": "PASS_S8_K1b_SUPERHORIZON_GATE" if passed else "FAIL_OR_DEAD_REVIEW",
        "scope": (
            "Full scalar fluid + CDM + baryon + radiation test with explicit "
            "momentum drag F_c^mu and Einstein constraint conservation."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
