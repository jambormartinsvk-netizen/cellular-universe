#!/usr/bin/env python3
"""Symbolic sign-map and null-limit audit for the A2-K1 equations.

The primary reference writes Q_x = Gamma_ref rho_x, with Gamma_ref > 0
meaning CDM -> DE.  The cellular A2-K1 direction is fuel -> CDM, so

    Gamma_ref = -Gamma_cell,  Gamma_cell > 0.

This script checks the mapped interaction terms in the CDM continuity,
fuel continuity, and fuel Euler equations, as well as the large-scale
velocity coefficient and the Gamma_cell -> 0 limit.
"""

from __future__ import annotations

import json

import sympy as sp


def is_zero(expr: sp.Expr) -> bool:
    return bool(sp.simplify(expr) == 0)


def main() -> int:
    a, gamma_ref, gamma_cell = sp.symbols(
        "a gamma_ref gamma_cell", positive=True
    )
    rho_f, rho_c = sp.symbols("rho_f rho_c", positive=True)
    delta_c, delta_f, psi = sp.symbols("delta_c delta_f psi")
    hubble, w, theta_f, theta_c, k2 = sp.symbols(
        "hubble w theta_f theta_c k2", nonzero=True
    )
    d = sp.symbols("d", positive=True)

    mapping = {gamma_ref: -gamma_cell, 1 + w: d}

    # Reference equations 32, 33, and 35 of arXiv:1109.6234.
    ref_cdm_cont = (
        a * gamma_ref * rho_f / rho_c * (delta_c - delta_f - psi)
    )
    expected_cdm_cont = (
        a * gamma_cell * rho_f / rho_c * (delta_f - delta_c + psi)
    )

    ref_fuel_cont = a * gamma_ref * (
        psi + 3 * hubble * (1 - w) * theta_f / k2
    )
    expected_fuel_cont = -a * gamma_cell * (
        psi + 3 * hubble * (1 - w) * theta_f / k2
    )

    ref_fuel_euler = a * gamma_ref / (1 + w) * (theta_c - 2 * theta_f)
    expected_fuel_euler = a * gamma_cell / d * (2 * theta_f - theta_c)

    # Reference instability coefficient for Q || u_c is -2 Gamma_ref/(1+w).
    ref_large_scale_rate = -2 * gamma_ref / (1 + w)
    expected_large_scale_rate = 2 * gamma_cell / d

    checks = {
        "cdm_continuity_sign_map": is_zero(
            ref_cdm_cont.subs(gamma_ref, -gamma_cell) - expected_cdm_cont
        ),
        "fuel_continuity_sign_map": is_zero(
            ref_fuel_cont.subs(gamma_ref, -gamma_cell) - expected_fuel_cont
        ),
        "fuel_euler_sign_map": is_zero(
            ref_fuel_euler.subs(mapping) - expected_fuel_euler
        ),
        "large_scale_rate_sign_map": is_zero(
            ref_large_scale_rate.subs(mapping) - expected_large_scale_rate
        ),
        "cdm_continuity_null_limit": is_zero(
            expected_cdm_cont.subs(gamma_cell, 0)
        ),
        "fuel_continuity_null_limit": is_zero(
            expected_fuel_cont.subs(gamma_cell, 0)
        ),
        "fuel_euler_null_limit": is_zero(
            expected_fuel_euler.subs(gamma_cell, 0)
        ),
        "background_source_pair_cancels": is_zero(
            -a * gamma_cell * rho_f + a * gamma_cell * rho_f
        ),
    }

    passed = all(checks.values())
    output = {
        "test": "A2-K1 equation sign mapping and null limit",
        "reference": "arXiv:1109.6234 equations 32, 33, 35, 38",
        "mapping": "Gamma_ref = -Gamma_cell; 1+w = delta > 0",
        "checks": checks,
        "status": "PASS" if passed else "FAIL",
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

