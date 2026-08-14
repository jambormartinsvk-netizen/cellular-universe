#!/usr/bin/env python3
"""Full first relativistic superhorizon test for A2-K5/K1.

Variables in Newtonian gauge (Psi=Phi; perfect radiation) are

  y = [delta_n, u_c, chi, chi_x, delta_b, u_b, delta_r, u_r, Phi],

where chi=delta varphi, u_A=H0 theta_A/k^2, and delta_n is the
conserved CDM number-density contrast.  The physical CDM energy contrast is
delta_c=delta_n+beta chi.  The scalar velocity is
u_phi=chi/(a E varphi_x), so u_phi-u_c is gauge invariant.

The 0i Einstein constraint evolves Phi.  The 00 constraint is monitored but
not imposed after the initial surface.  The initial condition is a pure
dark-sector relative-velocity mode with zero total momentum and zero density
perturbation.  This is the direct action analogue of the earlier A2 tests.
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
SPEC = importlib.util.spec_from_file_location("k5_1_full_background", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load validated background: {BASE_PATH}")
BASE13 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE13
SPEC.loader.exec_module(BASE13)

DN, UC, CHI, PIX, DB, UB, DR, UR, PHI = range(9)


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
    xb = xb0*np.exp(-3.0*xs)
    xc = xm-xb
    e2 = xf+xm+xr
    e = np.sqrt(e2)

    xf_x = -3.0*p.delta*xf-lam*xf/e
    xm_x = -3.0*xm+lam*xf/e
    xr_x = -4.0*xr
    e_x_over_e = 0.5*(xf_x+xm_x+xr_x)/e2
    varphi_x = np.sqrt(3.0*p.delta*xf)/e
    beta = np.zeros_like(xs)
    if lam != 0.0:
        beta = lam*np.sqrt(xf)/(xc*math.sqrt(3.0*p.delta))

    y_x = 0.5*(2.0-p.delta)*xf_x
    y_varphi = y_x/varphi_x
    y_varphi2 = np.gradient(y_varphi, xs, edge_order=2)/varphi_x
    beta_varphi = np.gradient(beta, xs, edge_order=2)/varphi_x
    meff2 = 3.0*(y_varphi2+xc*(beta_varphi+beta**2))

    coeff = {
        "xf": xf,
        "xc": xc,
        "xb": xb,
        "xr": xr,
        "E": e,
        "E_x_over_E": e_x_over_e,
        "varphi_x": varphi_x,
        "beta": beta,
        "Y_varphi": y_varphi,
        "meff2": meff2,
    }
    return p, xs, coeff


def at_index(coeff, i):
    return {key: float(value[i]) for key, value in coeff.items()}


def midpoint(c0, c1):
    return {key: 0.5*(c0[key]+c1[key]) for key in c0}


def phi_x_and_uphi(x, y, c):
    a = math.exp(x)
    uphi = y[CHI]/(a*c["E"]*c["varphi_x"])
    momentum = (
        c["xc"]*y[UC]
        + c["xb"]*y[UB]
        + (4.0/3.0)*c["xr"]*y[UR]
        + c["xf"]*c["varphi_x"]**2*c["E"]**2/3.0*uphi
    )
    # xf*delta equals E^2 varphi_x^2/3 identically; the latter expression
    # is used as a separate reconstruction cross-check of scalar enthalpy.
    phi_x = -y[PHI]+1.5*a*momentum/c["E"]
    return phi_x, uphi


def rhs(x, y, c, q):
    a = math.exp(x)
    e = c["E"]
    phi_x, _ = phi_x_and_uphi(x, y, c)
    out = np.zeros_like(y)
    out[DN] = -(q*q)*y[UC]/(a*e)+3.0*phi_x
    out[UC] = (
        -(1.0+c["beta"]*c["varphi_x"])*y[UC]
        +(y[PHI]+c["beta"]*y[CHI])/(a*e)
    )
    out[CHI] = y[PIX]
    out[PIX] = (
        -(3.0+c["E_x_over_E"])*y[PIX]
        -((q*q)/(a*a*e*e)+c["meff2"]/(e*e))*y[CHI]
        +4.0*c["varphi_x"]*phi_x
        -6.0*(c["Y_varphi"]+c["beta"]*c["xc"])*y[PHI]/(e*e)
        -3.0*c["beta"]*c["xc"]*y[DN]/(e*e)
    )
    out[DB] = -(q*q)*y[UB]/(a*e)+3.0*phi_x
    out[UB] = -y[UB]+y[PHI]/(a*e)
    out[DR] = -(4.0/3.0)*(q*q)*y[UR]/(a*e)+4.0*phi_x
    out[UR] = (y[DR]/4.0+y[PHI])/(a*e)
    out[PHI] = phi_x
    return out


def constraint_terms(x, y, dy, c, q):
    a = math.exp(x)
    delta_c = y[DN]+c["beta"]*y[CHI]
    delta_scalar = (
        (c["E"]**2/3.0)
        *(c["varphi_x"]*y[PIX]-c["varphi_x"]**2*y[PHI])
        +c["Y_varphi"]*y[CHI]
    )
    density = (
        c["xc"]*delta_c+c["xb"]*y[DB]+c["xr"]*y[DR]+delta_scalar
    )
    return np.array([
        q*q*y[PHI],
        3.0*(a*c["E"])**2*(dy[PHI]+y[PHI]),
        1.5*a*a*density,
    ])


def initial_relative_mode(x0, c0):
    a = math.exp(x0)
    scalar_enthalpy = c0["xf"]*c0["varphi_x"]**2*c0["E"]**2/3.0
    # This equals delta*X_f but does not insert the model parameter by hand.
    inertia = c0["xc"]+scalar_enthalpy
    uphi = c0["xc"]/inertia
    uc = -scalar_enthalpy/inertia
    chi = uphi*a*c0["E"]*c0["varphi_x"]

    y = np.zeros(9, dtype=float)
    y[UC] = uc
    y[CHI] = chi
    y[DN] = -c0["beta"]*chi
    y[PIX] = -3.0*c0["Y_varphi"]*chi/(
        c0["E"]**2*c0["varphi_x"]
    )
    return y


def run(step: float, q: float, lam: float) -> dict:
    p, xs, coeff = build_background(lam, step)
    c0 = at_index(coeff, 0)
    y = initial_relative_mode(float(xs[0]), c0)
    phi_x0, uphi0 = phi_x_and_uphi(float(xs[0]), y, c0)
    initial_relative = uphi0-y[UC]

    max_residual = 0.0
    max_term_norm = 0.0
    max_state = float(np.max(np.abs(y)))
    initial_constraint = None

    for i in range(len(xs)):
        if i > 0:
            x0, x1 = float(xs[i-1]), float(xs[i])
            dx = x1-x0
            c_left = at_index(coeff, i-1)
            c_right = at_index(coeff, i)
            c_mid = midpoint(c_left, c_right)
            xm = 0.5*(x0+x1)
            k1 = rhs(x0, y, c_left, q)
            k2 = rhs(xm, y+0.5*dx*k1, c_mid, q)
            k3 = rhs(xm, y+0.5*dx*k2, c_mid, q)
            k4 = rhs(x1, y+dx*k3, c_right, q)
            y = y+dx*(k1+2.0*k2+2.0*k3+k4)/6.0

        c = at_index(coeff, i)
        dy = rhs(float(xs[i]), y, c, q)
        terms = constraint_terms(float(xs[i]), y, dy, c, q)
        residual = abs(float(np.sum(terms)))
        term_norm = float(np.sum(np.abs(terms)))
        if i == 0:
            initial_constraint = residual
        max_residual = max(max_residual, residual)
        max_term_norm = max(max_term_norm, term_norm)
        max_state = max(max_state, float(np.max(np.abs(y))))

    c_final = at_index(coeff, -1)
    _, uphi_final = phi_x_and_uphi(float(xs[-1]), y, c_final)
    final_relative = uphi_final-y[UC]
    return {
        "step": step,
        "k_over_H0": q,
        "lambda": lam,
        "initial_relative_velocity": float(initial_relative),
        "final_relative_velocity": float(final_relative),
        "absolute_relative_velocity_transfer": float(
            abs(final_relative/initial_relative)
        ),
        "final_delta_n": float(y[DN]),
        "final_delta_c": float(y[DN]+c_final["beta"]*y[CHI]),
        "final_delta_varphi": float(y[CHI]),
        "final_Phi": float(y[PHI]),
        "initial_abs_00_constraint": float(initial_constraint),
        "global_relative_00_constraint_residual": float(
            max_residual/max(max_term_norm, 1.0e-300)
        ),
        "max_absolute_state": max_state,
        "all_finite": bool(np.all(np.isfinite(y))),
    }


def main() -> int:
    coupled_coarse = run(1.25e-4, 1.0e-5, 0.15)
    coupled_fine = run(6.25e-5, 1.0e-5, 0.15)
    coupled_half_k = run(6.25e-5, 5.0e-6, 0.15)
    uncoupled_fine = run(6.25e-5, 1.0e-5, 0.0)

    transfer = coupled_fine["absolute_relative_velocity_transfer"]
    null_transfer = uncoupled_fine["absolute_relative_velocity_transfer"]
    gain = transfer/max(null_transfer, 1.0e-300)
    log_coarse = math.log(max(coupled_coarse["absolute_relative_velocity_transfer"], 1e-300))
    log_fine = math.log(max(transfer, 1e-300))
    step_conv = abs(log_coarse-log_fine)/max(abs(log_fine), 1.0)
    log_half_k = math.log(max(coupled_half_k["absolute_relative_velocity_transfer"], 1e-300))
    k_conv = abs(log_half_k-log_fine)/max(abs(log_fine), 1.0)

    checks = {
        "all_runs_finite": all(r["all_finite"] for r in [
            coupled_coarse, coupled_fine, coupled_half_k, uncoupled_fine
        ]),
        "initial_constraint_satisfied": coupled_fine["initial_abs_00_constraint"] < 1.0e-10,
        "step_converged": step_conv < 1.0e-6,
        "superhorizon_k_converged": k_conv < 1.0e-6,
        "constraint_controlled": coupled_fine["global_relative_00_constraint_residual"] < 1.0e-5,
        "no_more_than_one_interaction_efold_relative_to_null": gain < math.e,
        "no_absolute_explosive_transfer": transfer < math.e,
    }
    passed = all(checks.values())
    output = {
        "test": "A2-K5.1 full first superhorizon relative mode",
        "coupled_coarse": coupled_coarse,
        "coupled_fine": coupled_fine,
        "coupled_half_k": coupled_half_k,
        "uncoupled_fine": uncoupled_fine,
        "coupled_to_null_transfer_gain": gain,
        "coupled_to_null_log_gain": math.log(max(gain, 1e-300)),
        "step_log_transfer_relative_difference": step_conv,
        "k_log_transfer_relative_difference": k_conv,
        "checks": checks,
        "verdict": "PASS_K5_1_SUPERHORIZON_GATE" if passed else "FAIL_OR_DEAD_REVIEW",
        "scope": (
            "Full scalar+CDM+baryon+perfect-radiation first-order test with "
            "00/0i Einstein constraints. It is not the photon/neutrino "
            "Boltzmann hierarchy or an observational likelihood."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
