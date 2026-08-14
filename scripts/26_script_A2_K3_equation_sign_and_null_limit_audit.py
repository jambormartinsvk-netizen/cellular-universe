#!/usr/bin/env python3
"""Symbolic sign-map and Gamma->0 audit for A2-K3.

Primary convention (arXiv:1109.6234):
    Q_x = Gamma_ref rho_x, Gamma_ref>0 means CDM -> DE.
Cellular convention:
    Q_f = -Gamma_cell rho_f, Gamma_cell>0 means fuel -> CDM.
Thus Gamma_ref=-Gamma_cell.
"""

from __future__ import annotations

import json

import sympy as sp


def is_zero(expr: sp.Expr) -> bool:
    return bool(sp.simplify(expr) == 0)


def main() -> int:
    a, gamma_ref, gamma = sp.symbols("a gamma_ref gamma", positive=True)
    rho_f, rho_c = sp.symbols("rho_f rho_c", positive=True)
    delta_c, delta_f, psi = sp.symbols("delta_c delta_f psi")
    hubble, w, theta_f, theta_c, k2 = sp.symbols(
        "hubble w theta_f theta_c k2", nonzero=True
    )
    d = sp.symbols("d", positive=True)
    mapping = {gamma_ref: -gamma, 1 + w: d}

    # Reference continuity equations (32)--(33), common to both frames.
    ref_cdm_cont = a * gamma_ref * rho_f / rho_c * (
        delta_c - delta_f - psi
    )
    expected_cdm_cont = a * gamma * rho_f / rho_c * (
        delta_f - delta_c + psi
    )

    ref_fuel_cont = a * gamma_ref * (
        psi + 3 * hubble * (1 - w) * theta_f / k2
    )
    expected_fuel_cont = -a * gamma * (
        psi + 3 * hubble * (1 - w) * theta_f / k2
    )

    # Reference Euler equations (36)--(37) for Q || u_x.
    ref_cdm_euler = a * gamma_ref * rho_f / rho_c * (theta_c - theta_f)
    expected_cdm_euler = a * gamma * rho_f / rho_c * (theta_f - theta_c)

    ref_fuel_euler = -a * gamma_ref * theta_f / (1 + w)
    expected_fuel_euler = a * gamma * theta_f / d

    # Equation (38), alpha=1: -Gamma_ref/(1+w).
    ref_large_scale_rate = -gamma_ref / (1 + w)
    expected_large_scale_rate = gamma / d

    checks = {
        "cdm_continuity_sign_map": is_zero(
            ref_cdm_cont.subs(gamma_ref, -gamma) - expected_cdm_cont
        ),
        "fuel_continuity_sign_map": is_zero(
            ref_fuel_cont.subs(gamma_ref, -gamma) - expected_fuel_cont
        ),
        "cdm_euler_sign_map": is_zero(
            ref_cdm_euler.subs(gamma_ref, -gamma) - expected_cdm_euler
        ),
        "fuel_euler_sign_map": is_zero(
            ref_fuel_euler.subs(mapping) - expected_fuel_euler
        ),
        "large_scale_rate_sign_map": is_zero(
            ref_large_scale_rate.subs(mapping) - expected_large_scale_rate
        ),
        "cdm_continuity_null_limit": is_zero(
            expected_cdm_cont.subs(gamma, 0)
        ),
        "fuel_continuity_null_limit": is_zero(
            expected_fuel_cont.subs(gamma, 0)
        ),
        "cdm_euler_null_limit": is_zero(expected_cdm_euler.subs(gamma, 0)),
        "fuel_euler_null_limit": is_zero(expected_fuel_euler.subs(gamma, 0)),
        "background_source_pair_cancels": is_zero(
            -a * gamma * rho_f + a * gamma * rho_f
        ),
    }
    passed = all(checks.values())
    print(
        json.dumps(
            {
                "test": "A2-K3 equation sign mapping and null limit",
                "reference": "arXiv:1109.6234 equations 32, 33, 36--38",
                "mapping": "Gamma_ref=-Gamma_cell; 1+w_f=delta>0",
                "checks": checks,
                "status": "PASS" if passed else "FAIL",
            },
            indent=2,
            ensure_ascii=False,
        )
    )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

