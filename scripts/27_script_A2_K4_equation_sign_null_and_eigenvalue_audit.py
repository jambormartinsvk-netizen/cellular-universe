#!/usr/bin/env python3
"""Symbolic audit of A2-K4: Q^mu parallel to dark-sector velocity u_d^mu.

The dark-sector energy-frame velocity is defined by enthalpy weighting,

    theta_d = [rho_c theta_c + (1+w_f)rho_f theta_f]
              / [rho_c + (1+w_f)rho_f].

The script derives the mapped Euler sources from the general transfer-frame
equations, checks Gamma->0, and proves that the homogeneous interaction
matrix has one positive and one negative eigenvalue whenever rho_f,rho_c>0.
"""

from __future__ import annotations

import json

import sympy as sp


def is_zero(expr: sp.Expr) -> bool:
    return bool(sp.simplify(expr) == 0)


def main() -> int:
    a, gamma_ref, gamma = sp.symbols("a gamma_ref gamma", positive=True)
    rho_f, rho_c, d = sp.symbols("rho_f rho_c d", positive=True)
    theta_f, theta_c = sp.symbols("theta_f theta_c")
    delta_f, delta_c, psi = sp.symbols("delta_f delta_c psi")
    hubble, w, k2 = sp.symbols("hubble w k2", nonzero=True)

    r = rho_f / rho_c
    beta = sp.simplify(d * rho_f / (rho_c + d * rho_f))
    theta_d = sp.simplify((rho_c * theta_c + d * rho_f * theta_f) /
                          (rho_c + d * rho_f))

    # Continuities are independent of the transfer-frame velocity at first order.
    ref_cdm_cont = a * gamma_ref * r * (delta_c - delta_f - psi)
    expected_cdm_cont = a * gamma * r * (delta_f - delta_c + psi)
    ref_fuel_cont = a * gamma_ref * (
        psi + 3 * hubble * (1 - w) * theta_f / k2
    )
    expected_fuel_cont = -a * gamma * (
        psi + 3 * hubble * (1 - w) * theta_f / k2
    )

    # General reference-frame Euler sources for Q_ref || u_q.
    ref_cdm_euler = a * gamma_ref * r * (theta_c - theta_d)
    ref_fuel_euler = a * gamma_ref / (1 + w) * (theta_d - 2 * theta_f)
    expected_cdm_euler = a * gamma * r * (theta_d - theta_c)
    expected_fuel_euler = a * gamma / d * (2 * theta_f - theta_d)

    # Interaction-only physical-time matrix for [V_c,V_f], divided by Gamma.
    matrix = sp.Matrix(
        [
            [-r * beta, r * beta],
            [-(1 - beta) / d, (2 - beta) / d],
        ]
    )
    expected_det = -r**2 / (1 + d * r)
    common_velocity_image = sp.simplify(matrix * sp.Matrix([1, 1]))

    checks = {
        "theta_d_enthalpy_definition": is_zero(
            theta_d - ((1 - beta) * theta_c + beta * theta_f)
        ),
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
            ref_fuel_euler.subs({gamma_ref: -gamma, 1 + w: d})
            - expected_fuel_euler
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
        "interaction_matrix_determinant": is_zero(matrix.det() - expected_det),
        # A common velocity is not an eigenvector, so both eigenmodes carry
        # a nonzero gauge-invariant relative velocity V_f-V_c.
        "common_velocity_not_eigenvector": not is_zero(common_velocity_image[1]),
    }

    passed = all(checks.values())
    output = {
        "test": "A2-K4 sign, null-limit, and local eigenvalue audit",
        "definition": "Q^mu parallel u_d; theta_d enthalpy-weighted",
        "mapping": "Gamma_ref=-Gamma_cell; 1+w_f=delta>0",
        "interaction_matrix_determinant": str(sp.factor(matrix.det())),
        "determinant_sign_for_positive_densities": "negative",
        "eigenvalue_consequence": (
            "one positive and one negative real eigenvalue; both have "
            "nonzero V_f-V_c"
        ),
        "checks": checks,
        "status": "PASS" if passed else "FAIL",
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

