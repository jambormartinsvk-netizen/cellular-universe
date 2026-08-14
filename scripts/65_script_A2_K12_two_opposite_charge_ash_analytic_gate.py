#!/usr/bin/env python3
"""A2-K12.0: analytic gate for two ash species with opposite scalar charge.

The script uses the local K5 normalization

    mu_ij = 1 + 2 beta_i beta_j

in the light-scalar quasistatic limit.  It checks the force matrix, its two
eigenmodes, and the background cancellation of scalar-mediated energy flow.
This is an analytic diagnostic, not a Boltzmann or nonlinear simulation.
"""

from __future__ import annotations

import math


BETA_K5 = 1.52883


def force_coefficients(beta: float) -> tuple[float, float]:
    """Return same-charge and opposite-charge G_eff/G coefficients."""
    scalar = 2.0 * beta * beta
    return 1.0 + scalar, 1.0 - scalar


def weighted_growth_eigenvalues(beta: float, asymmetry: float) -> tuple[float, float]:
    """Eigenvalues of B_ij=f_j*(1+2*beta_i*beta_j).

    asymmetry=(rho_plus-rho_minus)/(rho_plus+rho_minus), with |asymmetry|<=1.
    The returned values are ordered from largest to smallest.
    """
    if abs(asymmetry) > 1.0:
        raise ValueError("|asymmetry| must not exceed 1")
    scalar = 2.0 * beta * beta
    discriminant = (1.0 - scalar) ** 2 + 4.0 * scalar * asymmetry**2
    root = math.sqrt(discriminant)
    return (0.5 * (1.0 + scalar + root), 0.5 * (1.0 + scalar - root))


def background_transfer_fraction(asymmetry: float) -> float:
    """Q_total/Q_single for equal |beta| and the same scalar velocity."""
    return asymmetry


def beta_for_fixed_single_species_transfer(beta_single: float, asymmetry: float) -> float:
    """beta needed to keep beta*asymmetry fixed at beta_single."""
    if asymmetry == 0.0:
        return math.inf
    return abs(beta_single / asymmetry)


def main() -> None:
    mu_same, mu_opposite = force_coefficients(BETA_K5)
    symmetric_eigs = weighted_growth_eigenvalues(BETA_K5, 0.0)
    scalar_mode = 2.0 * BETA_K5 * BETA_K5

    assert math.isclose(mu_same + mu_opposite, 2.0, rel_tol=0.0, abs_tol=1e-14)
    assert math.isclose(symmetric_eigs[0], max(1.0, scalar_mode), rel_tol=1e-13)
    assert math.isclose(symmetric_eigs[1], min(1.0, scalar_mode), rel_tol=1e-13)
    assert background_transfer_fraction(0.0) == 0.0
    assert background_transfer_fraction(1.0) == 1.0

    print("A2-K12.0 TWO OPPOSITE SCALAR CHARGES - ANALYTIC GATE")
    print(f"beta_K5={BETA_K5:.8f}")
    print(f"mu_same=1+2 beta^2={mu_same:.10f}")
    print(f"mu_opposite=1-2 beta^2={mu_opposite:.10f}")
    print(f"symmetric_total_mode_eigenvalue=1.0000000000")
    print(f"symmetric_charge_separation_eigenvalue={scalar_mode:.10f}")
    print("symmetric_scalar_background_transfer_fraction=0.0000000000")
    print()
    print("asymmetry  Qscalar/Qsingle  lambda_max  lambda_min  beta_keep_Q  scalar_mode_keep_Q")
    for asymmetry in (0.0, 0.01, 0.10, 0.25, 0.50, 0.75, 1.0):
        hi, lo = weighted_growth_eigenvalues(BETA_K5, asymmetry)
        beta_keep = beta_for_fixed_single_species_transfer(BETA_K5, asymmetry)
        scalar_keep = math.inf if math.isinf(beta_keep) else 2.0 * beta_keep**2
        print(
            f"{asymmetry:9.2f}  {background_transfer_fraction(asymmetry):15.8f}"
            f"  {hi:10.6f}  {lo:10.6f}  {beta_keep:11.6g}  {scalar_keep:18.6g}"
        )

    print()
    print("GATE_ACTION_AND_CONSERVATION=PASS")
    print("GATE_EQUAL_PAIR_NET_SCALAR_ENERGY_TRANSFER=FAIL_ZERO")
    print("GATE_EQUAL_PAIR_LINEAR_TOTAL_GROWTH_REDUCTION=FAIL_GR_LIKE")
    print("GATE_CHARGE_SEPARATION_MODE=RED")
    print("VERDICT=PURE_SYMMETRIC_CONFORMAL_BRANCH_DOES_NOT_MEET_THE_COMBINED_TARGET")


if __name__ == "__main__":
    main()
