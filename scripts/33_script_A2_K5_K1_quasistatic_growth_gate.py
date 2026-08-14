#!/usr/bin/env python3
"""First subhorizon growth gate for reconstructed A2-K5-K1.

Uses the standard coupled-quintessence Newtonian-limit equations, generalized
to the reconstructed beta(varphi) and effective scalar mass:

  delta_c,xx + [2+E_x/E+beta varphi_x] delta_c,x
    -3/2[Omega_c(1+2 beta^2 F)delta_c+Omega_b delta_b]=0,
  delta_b,xx + [2+E_x/E] delta_b,x
    -3/2[Omega_c delta_c+Omega_b delta_b]=0,

where F=q^2/(q^2+a^2 m_eff^2/H0^2), q=k/H0.  The sign of the
friction term follows from rho_c,x+3rho_c=+beta varphi_x rho_c.

This is a quasi-static gate, not a CMB-normalized CLASS/CAMB likelihood.
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
SPEC = importlib.util.spec_from_file_location("k5_k1_growth_background", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load background: {BASE_PATH}")
BASE13 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE13
SPEC.loader.exec_module(BASE13)


def coefficients(xs, states, xb0, p):
    xf, xm, xr = states.T
    xb = xb0*np.exp(-3.0*xs)
    xc = xm-xb
    e2 = xf+xm+xr
    e = np.sqrt(e2)
    w = -1.0+p.delta
    xf_x = -3.0*p.delta*xf-p.lam*xf/e
    xm_x = -3.0*xm+p.lam*xf/e
    xr_x = -4.0*xr
    e_x_over_e = 0.5*(xf_x+xm_x+xr_x)/e2

    varphi_x = np.sqrt(3.0*p.delta*xf)/e
    beta = p.lam*np.sqrt(xf)/(xc*math.sqrt(3.0*p.delta))
    potential_x = 0.5*(1.0-w)*xf_x
    potential_varphi = potential_x/varphi_x
    potential_varphi2 = np.gradient(
        potential_varphi, xs, edge_order=2
    )/varphi_x
    beta_varphi = np.gradient(beta, xs, edge_order=2)/varphi_x
    meff2 = 3.0*(potential_varphi2+xc*(beta_varphi+beta**2))
    return {
        "E": e,
        "E_x_over_E": e_x_over_e,
        "Omega_c": xc/e2,
        "Omega_b": xb/e2,
        "varphi_x": varphi_x,
        "beta": beta,
        "meff2_over_H0sq": meff2,
    }


def rhs(y, x, c, q, include_friction, include_fifth_force):
    dc, gc, db, gb = y
    a = math.exp(x)
    friction = c["beta"]*c["varphi_x"] if include_friction else 0.0
    if include_fifth_force:
        denominator = q*q+a*a*c["meff2_over_H0sq"]
        if denominator <= 0.0:
            raise FloatingPointError("Non-positive scalar propagator denominator")
        yukawa = q*q/denominator
    else:
        yukawa = 0.0
    geff = 1.0+2.0*c["beta"]**2*yukawa
    source_c = 1.5*(c["Omega_c"]*geff*dc+c["Omega_b"]*db)
    source_b = 1.5*(c["Omega_c"]*dc+c["Omega_b"]*db)
    return np.array([
        gc,
        -(2.0+c["E_x_over_E"]+friction)*gc+source_c,
        gb,
        -(2.0+c["E_x_over_E"])*gb+source_b,
    ])


def midpoint_coeff(c0, c1):
    return {key: 0.5*(c0[key]+c1[key]) for key in c0}


def integrate_mode(xs, coeff, q, include_friction, include_fifth_force):
    # Common growing matter mode at recombination; normalization is arbitrary.
    y = np.array([1.0, 1.0, 1.0, 1.0], dtype=float)
    for i in range(len(xs)-1):
        x0, x1 = float(xs[i]), float(xs[i+1])
        dx = x1-x0
        c0 = {key: value[i] for key, value in coeff.items()}
        c1 = {key: value[i+1] for key, value in coeff.items()}
        cm = midpoint_coeff(c0, c1)
        xm = 0.5*(x0+x1)
        k1 = rhs(y, x0, c0, q, include_friction, include_fifth_force)
        k2 = rhs(y+0.5*dx*k1, xm, cm, q, include_friction, include_fifth_force)
        k3 = rhs(y+0.5*dx*k2, xm, cm, q, include_friction, include_fifth_force)
        k4 = rhs(y+dx*k3, x1, c1, q, include_friction, include_fifth_force)
        y = y+dx*(k1+2*k2+2*k3+k4)/6.0
    return {
        "delta_c_today": float(y[0]),
        "growth_rate_c_today": float(y[1]/y[0]),
        "delta_b_today": float(y[2]),
        "growth_rate_b_today": float(y[3]/y[2]),
        "all_finite": bool(np.all(np.isfinite(y))),
    }


def run(step):
    p = BASE13.BASE.ModelParameters()
    x_star = -math.log1p(p.z_star)
    settings = BASE13.BASE.IntegrationSettings(x_min=x_star, step=step)
    xs_desc, states_desc, xb0 = BASE13.integrate_background(p, settings)
    xs = xs_desc[::-1]
    states = states_desc[::-1]
    coeff = coefficients(xs, states, xb0, p)

    results = {}
    for q in [30.0, 100.0, 300.0]:
        full = integrate_mode(xs, coeff, q, True, True)
        friction_only = integrate_mode(xs, coeff, q, True, False)
        gr_diagnostic = integrate_mode(xs, coeff, q, False, False)
        results[f"k_over_H0={q:g}"] = {
            "full_K5_K1": full,
            "friction_only": friction_only,
            "GR_like_same_background": gr_diagnostic,
            "full_to_GR_delta_c_ratio": (
                full["delta_c_today"]/gr_diagnostic["delta_c_today"]
            ),
            "friction_to_GR_delta_c_ratio": (
                friction_only["delta_c_today"]/gr_diagnostic["delta_c_today"]
            ),
            "full_to_friction_delta_c_ratio": (
                full["delta_c_today"]/friction_only["delta_c_today"]
            ),
        }
    return {"step": step, "results": results}


def main() -> int:
    coarse = run(5.0e-4)
    fine = run(2.5e-4)
    convergence = {}
    for key in fine["results"]:
        c = coarse["results"][key]["full_to_GR_delta_c_ratio"]
        f = fine["results"][key]["full_to_GR_delta_c_ratio"]
        convergence[key] = abs(c-f)/abs(f)

    converged = all(value < 1.0e-6 for value in convergence.values())
    finite = all(
        mode["all_finite"]
        for item in fine["results"].values()
        for mode in [
            item["full_K5_K1"],
            item["friction_only"],
            item["GR_like_same_background"],
        ]
    )
    ratios = [
        item["full_to_GR_delta_c_ratio"] for item in fine["results"].values()
    ]
    output = {
        "test": "A2-K5-K1 quasi-static growth gate",
        "coarse": coarse,
        "fine": fine,
        "convergence_relative_difference": convergence,
        "checks": {
            "all_runs_finite": finite,
            "step_converged": converged,
            "full_growth_enhanced_on_all_tested_scales": all(r > 1.0 for r in ratios),
        },
        "status": (
            "PASS_NUMERICS_GROWTH_RISK_CONFIRMED"
            if finite and converged and all(r > 1.0 for r in ratios)
            else "REQUIRES_REVIEW"
        ),
        "scope": (
            "Newtonian/quasi-static diagnostic from recombination; no CMB "
            "normalization, radiation perturbations, or likelihood."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if output["status"] == "PASS_NUMERICS_GROWTH_RISK_CONFIRMED" else 1


if __name__ == "__main__":
    raise SystemExit(main())

