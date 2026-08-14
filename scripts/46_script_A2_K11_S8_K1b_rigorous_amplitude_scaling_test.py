#!/usr/bin/env python3
"""Rigorous amplitude scaling and constraint conservation test for A2_K11_S8_K1b.

This script runs the superhorizon relative-velocity test under three different
initial amplitudes: A = 1.0, A = 1e4, and A = 1e8.
It uses an extremely fine background grid (step = 1e-5) and tight ODE tolerances
(rtol = 1e-12, atol = 1e-16) to verify:
1. Linear scaling (transfer ratio is constant).
2. Active constraint cancellation (relative residual drops to 0 for large A).
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np
from scipy.integrate import solve_ivp

# Import validated background from script 13
BASE_PATH = Path(__file__).with_name(
    "13_script_A1_K1_cdm_background_audit_exact_zstar.py"
)
SPEC = importlib.util.spec_from_file_location("s8_k1b_background", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load validated background: {BASE_PATH}")
BASE13 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE13
SPEC.loader.exec_module(BASE13)

# Indices:
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

    coeff = {
        "xf": xf,
        "xc": xc,
        "xb": xb,
        "xr": xr,
        "E": e,
        "E_x_over_E": e_x_over_e,
    }
    return p, xs, coeff


def at_index(coeff, i):
    return {key: float(value[i]) for key, value in coeff.items()}


def phi_x_and_momentum(x, y, c, p_delta):
    a = math.exp(x)
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

    G_c = (lam * c["xf"] / c["xc"] + gamma_drag) / e
    G_f = (lam + gamma_drag * c["xc"] / c["xf"]) / (p_delta * e)

    out = np.zeros_like(y)
    # 1. CDM
    out[DC] = -(q * q) * y[UC] / (a * e) + 3.0 * phi_x + (lam * c["xf"] / c["xc"] / e) * (y[DF] - y[DC])
    out[UC] = -(1.0 + G_c) * y[UC] + y[PHI] / (a * e) + (gamma_drag / e) * y[UF]

    # 2. Fuel
    out[DF] = -p_delta * (q * q) * y[UF] / (a * e) + 3.0 * p_delta * phi_x - (lam / e) * (y[DF] - y[DC])
    out[UF] = 2.0 * y[UF] + (y[DF] + y[PHI]) / (a * e) + G_f * (y[UC] - y[UF])

    # 3. Baryons
    out[DB] = -(q * q) * y[UB] / (a * e) + 3.0 * phi_x
    out[UB] = -y[UB] + y[PHI] / (a * e)

    # 4. Radiation
    out[DR] = -(4.0 / 3.0) * (q * q) * y[UR] / (a * e) + 4.0 * phi_x
    out[UR] = (y[DR] / 4.0 + y[PHI]) / (a * e)

    # 5. Potential
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


def initial_relative_mode(x0, c0, p_delta, amplitude):
    inertia = c0["xc"] + p_delta * c0["xf"]
    uf = amplitude * c0["xc"] / inertia
    uc = -amplitude * p_delta * c0["xf"] / inertia

    y = np.zeros(9, dtype=float)
    y[UC] = uc
    y[UF] = uf
    return y


def run_amplitude(amplitude: float, xs, coeff, p_delta, lam, gamma_drag, q=1.0e-5) -> dict:
    c0 = at_index(coeff, 0)
    y0 = initial_relative_mode(float(xs[0]), c0, p_delta, amplitude)
    initial_relative = y0[UF] - y0[UC]

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
        return rhs(x_val, y_val, c_interp, q, lam, p_delta, gamma_drag)

    # Solve with stiff Radau solver at extreme precision
    sol = solve_ivp(rhs_ode, (float(xs[0]), float(xs[-1])), y0, method="Radau", t_eval=xs, rtol=1e-12, atol=1e-16)

    # Evaluate final step constraints
    y_final = sol.y[:, -1]
    c_final = at_index(coeff, -1)
    dy_final = rhs(float(xs[-1]), y_final, c_final, q, lam, p_delta, gamma_drag)
    terms_final = constraint_terms(float(xs[-1]), y_final, dy_final, c_final, q, p_delta)
    
    res_final = abs(float(np.sum(terms_final)))
    norm_final = float(np.sum(np.abs(terms_final)))
    rel_res_final = res_final / max(norm_final, 1.0e-300)

    final_relative = y_final[UF] - y_final[UC]
    transfer = abs(final_relative / initial_relative)

    return {
        "amplitude": amplitude,
        "initial_relative": float(initial_relative),
        "final_relative": float(final_relative),
        "transfer_ratio": float(transfer),
        "final_absolute_residual": float(res_final),
        "final_term_norm": float(norm_final),
        "final_relative_residual": float(rel_res_final),
    }


def main() -> int:
    # Build background with extremely high resolution (step = 1e-5)
    print("Building background with step = 1e-5...", flush=True)
    p, xs, coeff = build_background(0.15, 1.0e-5)
    
    amplitudes = [1.0, 1.0e4, 1.0e8]
    results = []
    
    for amp in amplitudes:
        print(f"Running simulation for amplitude A = {amp:.1e}...", flush=True)
        res = run_amplitude(amp, xs, coeff, p.delta, 0.15, 0.03)
        results.append(res)
        
    output = {
        "test": "A2-K11 S8_K1b Rigorous Amplitude Scaling and Constraint Audit",
        "background_steps": len(xs),
        "background_integration_step": 1.0e-5,
        "ode_tolerances": {"rtol": 1e-12, "atol": 1e-16},
        "results": results,
    }
    
    print(json.dumps(output, indent=2, ensure_ascii=False))
    
    # Validation gates:
    # 1. Linear scaling check: transfer ratio must be constant within 1e-5 relative difference
    r1, r2, r3 = results
    t_diff_1 = abs(r1["transfer_ratio"] - r2["transfer_ratio"]) / r1["transfer_ratio"]
    t_diff_2 = abs(r1["transfer_ratio"] - r3["transfer_ratio"]) / r1["transfer_ratio"]
    linear_scaling_ok = (t_diff_1 < 1e-5) and (t_diff_2 < 1e-5)
    
    # 2. Relative constraint residual check: at A = 1e8, relative residual must be < 1e-5
    # (since the state is far above the solver's 1e-16 noise floor)
    constraint_conservation_ok = r3["final_relative_residual"] < 1.0e-5
    
    passed = linear_scaling_ok and constraint_conservation_ok
    
    verdict = "PASS_RIGOROUS_S8_K1b_AUDIT" if passed else "FAIL_AUDIT"
    print(f"\nVERDICT: {verdict}")
    print(f"  Linear scaling check: {'PASS' if linear_scaling_ok else 'FAIL'} (diffs: {t_diff_1:.2e}, {t_diff_2:.2e})")
    print(f"  Constraint conservation check at A=1e8: {'PASS' if constraint_conservation_ok else 'FAIL'} (rel_res: {r3['final_relative_residual']:.2e})")
    
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
