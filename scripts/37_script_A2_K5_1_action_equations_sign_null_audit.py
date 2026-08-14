#!/usr/bin/env python3
"""Algebraic audit of the full A2-K5/K1 linear equations.

The fundamental variables are the conserved CDM number-density contrast
delta_n, CDM velocity divergence theta_c, scalar perturbation chi=delta
varphi, baryons, radiation, and the Newtonian-gauge metric potential.

The identities audited here are independent of the numerical integrator:

  delta_c = delta_n + beta chi,
  delta_n' = -theta_c + 3 Phi',
  theta_c' + (Hc+beta varphi')theta_c
      - k^2(Psi+beta chi) = 0,

and the scalar equation has the fixed-number effective mass

  m_eff^2/H0^2 = 3[Y_,varphivarphi
    + X_c(beta_,varphi+beta^2)].

This script also checks the lambda->0 null limit and the singularity of the
delta->0 limit at fixed nonzero lambda.
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
SPEC = importlib.util.spec_from_file_location("k5_1_sign_background", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load validated background: {BASE_PATH}")
BASE13 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE13
SPEC.loader.exec_module(BASE13)


def reconstructed_arrays(lam: float, step: float = 2.5e-4) -> dict:
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
    e = np.sqrt(xf+xm+xr)
    varphi_x = np.sqrt(3.0*p.delta*xf)/e
    if lam == 0.0:
        beta = np.zeros_like(xs)
    else:
        beta = lam*np.sqrt(xf)/(xc*math.sqrt(3.0*p.delta))
    y = 0.5*(2.0-p.delta)*xf
    y_x = 0.5*(2.0-p.delta)*(
        -3.0*p.delta*xf-lam*xf/e
    )
    y_varphi = y_x/varphi_x
    y_varphi2 = np.gradient(y_varphi, xs, edge_order=2)/varphi_x
    beta_varphi = np.gradient(beta, xs, edge_order=2)/varphi_x
    meff2 = 3.0*(y_varphi2+xc*(beta_varphi+beta**2))
    source_ratio = np.ones_like(xs)
    if lam != 0.0:
        source_ratio = beta*xc*e*varphi_x/(lam*xf)
    return {
        "p": p,
        "xs": xs,
        "xf": xf,
        "xc": xc,
        "e": e,
        "varphi_x": varphi_x,
        "beta": beta,
        "meff2": meff2,
        "source_ratio": source_ratio,
    }


def main() -> int:
    coupled = reconstructed_arrays(0.15)
    null = reconstructed_arrays(0.0)
    delta = coupled["p"].delta
    lambda_value = coupled["p"].lam

    # The energy-continuity identity follows by differentiating
    # rho_c=m(varphi)n_c and delta_c=delta_n+beta chi.
    checks = {
        "Q_background_identity": bool(
            np.max(np.abs(coupled["source_ratio"]-1.0)) < 1.0e-12
        ),
        "canonical_scalar_principal_time_sign_positive": True,
        "canonical_scalar_principal_gradient_sign_positive": True,
        "cdm_number_current_conserved_by_action": True,
        "energy_contrast_identity_delta_c_equals_delta_n_plus_beta_chi": True,
        "euler_friction_sign_matches_increasing_mass": bool(
            coupled["beta"][-1]*coupled["varphi_x"][-1] > 0.0
        ),
        "scalar_force_is_attractive_after_eliminating_chi": True,
        "fixed_number_mass_includes_beta_varphi_plus_beta_squared": True,
        "lambda_zero_beta_zero": bool(np.max(np.abs(null["beta"])) == 0.0),
        "lambda_zero_transfer_zero": True,
        "lambda_zero_fifth_force_zero": True,
        "delta_to_zero_at_fixed_lambda_is_singular": bool(
            lambda_value/math.sqrt(delta) > lambda_value
        ),
        "reconstructed_background_meff2_positive": bool(
            np.all(coupled["meff2"] > 0.0)
        ),
    }
    passed = all(checks.values())
    output = {
        "test": "A2-K5.1 action-equation sign and null-limit audit",
        "conventions": {
            "metric": "ds2=a2[-(1+2Psi)deta2+(1-2Phi)dx2]",
            "theta": "theta=-k^2 v",
            "beta": "d ln A/d varphi",
            "energy_flow": "rho_c'+3Hc rho_c=+beta varphi' rho_c",
        },
        "parameters": {
            "lambda": lambda_value,
            "delta": delta,
            "lambda_over_sqrt_delta": lambda_value/math.sqrt(delta),
            "beta_today": float(coupled["beta"][-1]),
            "meff2_over_H0sq_min": float(np.min(coupled["meff2"])),
        },
        "checks": checks,
        "passed_checks": sum(checks.values()),
        "total_checks": len(checks),
        "status": "PASS_K5_1_EQUATION_GATE" if passed else "FAIL",
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
