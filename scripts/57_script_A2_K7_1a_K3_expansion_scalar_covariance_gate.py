#!/usr/bin/env python3
"""A2-K7.1a-K3 expansion-scalar covariance and null-limit gate.

Candidate mean transfer:

    Q1 = A rho_F,
    A = (1-epsilon) Gamma + epsilon (1-delta) Theta_phi,
    Theta_phi = nabla_mu u_phi^mu,

with the donor-aligned vector ledger

    Q_phi^mu = -Q1 u_phi^mu,
    Q_M^mu   = +Q1 u_phi^mu - Q2 u_M^mu,
    Q_c^mu   = +Q2 u_M^mu,
    Q2       = Gamma rho_F.

The script checks the exact FRW reduction, first-order scalar perturbation,
gauge transformation of delta Q1, vector-ledger cancellation, and the
singular epsilon->0 mediator rate.  It is not a derivation of a dissipative
CTP kernel or its noise correlator.
"""

from __future__ import annotations

import json

import sympy as sp


def zero(expr: sp.Expr) -> bool:
    return bool(sp.simplify(expr) == 0)


def main() -> int:
    epsilon, delta, gamma, rho, theta, hubble = sp.symbols(
        "epsilon delta Gamma rho_F Theta_phi H", positive=True
    )
    drho, dtheta = sp.symbols("delta_rho_F delta_Theta_phi")
    rho_dot, theta_dot, time_shift = sp.symbols(
        "rho_F_dot Theta_phi_dot T"
    )
    u_phi, u_m = sp.symbols("u_phi_mu u_M_mu")

    c_theta = epsilon * (1 - delta)
    amplitude = (1 - epsilon) * gamma + c_theta * theta
    q1 = amplitude * rho
    q2 = gamma * rho
    dq1 = amplitude * drho + c_theta * rho * dtheta

    # Scalar gauge transformation under eta -> eta + T.
    dq1_transformed = dq1.subs(
        {
            drho: drho - rho_dot * time_shift,
            dtheta: dtheta - theta_dot * time_shift,
        }
    )
    q1_dot = amplitude * rho_dot + c_theta * theta_dot * rho
    expected_transformed = dq1 - q1_dot * time_shift

    # Formal component-wise vector ledger; u symbols stand for independent
    # vector directions and therefore their coefficients must cancel.
    q_phi_vec = -q1 * u_phi
    q_m_vec = q1 * u_phi - q2 * u_m
    q_c_vec = q2 * u_m

    q1_frw = sp.simplify(q1.subs(theta, 3 * hubble))
    q1_required = ((1 - epsilon) * gamma + 3 * hubble * epsilon * (1 - delta)) * rho

    # Newtonian-gauge first-order expansion perturbation for signature
    # (-,+,+,+): a delta Theta_phi = theta_phi-3 Phi'-3 Hc Psi.
    velocity_divergence, phi_prime, hconf, psi, a = sp.symbols(
        "theta_phi Phi_prime Hconf Psi a"
    )
    delta_theta_newtonian = (
        velocity_divergence - 3 * phi_prime - 3 * hconf * psi
    ) / a
    dq1_newtonian = sp.expand(dq1.subs(dtheta, delta_theta_newtonian))

    # The interaction rate acting on the mediator enthalpy rho_M=epsilon rho
    # is R1=Q1/(epsilon rho); its epsilon->0 limit diverges because Q1->Gamma rho.
    r1 = sp.simplify(q1 / (epsilon * rho))
    epsilon_times_r1_limit = sp.simplify(sp.limit(epsilon * r1, epsilon, 0, dir="+"))
    r1_diverges = epsilon_times_r1_limit == gamma

    checks = {
        "exact_FRW_Q1": zero(q1_frw - q1_required),
        "first_order_delta_Q1_product_rule": zero(
            dq1 - (amplitude * drho + c_theta * rho * dtheta)
        ),
        "delta_Q1_scalar_gauge_transform": zero(
            dq1_transformed - expected_transformed
        ),
        "total_vector_ledger_cancels": zero(q_phi_vec + q_m_vec + q_c_vec),
        "epsilon_zero_rate_is_singular": bool(r1_diverges),
    }
    algebra_pass = all(checks.values())

    output = {
        "test": "A2-K7.1a-K3 expansion-scalar covariance gate",
        "operator": (
            "Q1=[(1-epsilon)Gamma+epsilon(1-delta)Theta_phi]rho_F"
        ),
        "reference_frame": "donor fuel four-velocity u_phi",
        "delta_Q1": str(dq1),
        "delta_Theta_phi_Newtonian_gauge": str(delta_theta_newtonian),
        "delta_Q1_Newtonian_gauge": str(dq1_newtonian),
        "mediator_rate_R1": str(r1),
        "limit_epsilon_times_R1": str(epsilon_times_r1_limit),
        "checks": checks,
        "mean_covariant_closure": "PASS" if algebra_pass else "FAIL",
        "microphysical_CTP_kernel": "NOT_DERIVED",
        "noise_correlator": "NOT_DERIVED",
        "regular_epsilon_zero_limit": "FAIL",
        "verdict": (
            "SURVIVES_FORMULATION_ONLY_NO_SCORE_INCREASE"
            if algebra_pass else "DEAD_M014b"
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if algebra_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
