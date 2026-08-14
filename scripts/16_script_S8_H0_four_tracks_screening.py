"""First-pass numerical screening of four proposed S8/H0 tracks.

This script is intentionally a set of transparent arithmetic and toy-model
checks, not a Boltzmann solver or a likelihood analysis.  It checks:

1. the sign and approximate magnitude of a late constant drag term needed to
   suppress linear growth from S8=0.874 to 0.815;
2. the fraction of a pre-existing component that decays in 13.8 Gyr for the
   proposed 50--100 Gyr lifetimes;
3. the entropy-dilution scaling of a decoupled light relic's Delta N_eff;
4. the FLRW distance shift caused by Omega_K=0.002 in a fixed-density toy
   background.

All conclusions remain conditional until the cellular-space model supplies
covariant perturbation equations, initial conditions, and a data likelihood.
"""

from __future__ import annotations

import json
import math

import numpy as np


OMEGA_M = 0.315
OMEGA_R = 9.2e-5
S8_MODEL = 0.874
S8_TARGET = 0.815
AGE_GYR = 13.8
DELTA_NEFF_BASE = 0.0535
GSTAR_BASE = 106.75
H0_BASE = 66.4
H0_CURVATURE_CLAIM = 67.5


def rk4_growth(drag: float, drag_sign: float = 1.0, a_on: float = 0.5) -> float:
    """Solve a toy linear-growth equation with drag active after a_on.

    Prime means d/d ln(a).  Positive drag_sign implements genuine friction:
      D'' + [2 + H'/H + drag] D' - 3 Omega_m(a) D / 2 = 0.
    """
    x0 = math.log(1.0e-3)
    x1 = 0.0
    steps = 20000
    step = (x1 - x0) / steps
    a0 = math.exp(x0)
    y = np.array([a0, a0], dtype=float)

    def derivative(x: float, state: np.ndarray) -> np.ndarray:
        a = math.exp(x)
        e2 = OMEGA_M * a ** -3 + (1.0 - OMEGA_M)
        omega_m_a = OMEGA_M * a ** -3 / e2
        dlnh_dln_a = -1.5 * omega_m_a
        active_drag = drag_sign * drag if a >= a_on else 0.0
        return np.array(
            [
                state[1],
                1.5 * omega_m_a * state[0]
                - (2.0 + dlnh_dln_a + active_drag) * state[1],
            ]
        )

    x = x0
    for _ in range(steps):
        k1 = derivative(x, y)
        k2 = derivative(x + step / 2.0, y + step * k1 / 2.0)
        k3 = derivative(x + step / 2.0, y + step * k2 / 2.0)
        k4 = derivative(x + step, y + step * k3)
        y += step * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        x += step
    return float(y[0])


def find_drag_for_ratio(target_ratio: float) -> float:
    base = rk4_growth(0.0)
    low, high = 0.0, 10.0
    for _ in range(80):
        middle = (low + high) / 2.0
        ratio = rk4_growth(middle) / base
        if ratio > target_ratio:
            low = middle
        else:
            high = middle
    return (low + high) / 2.0


def delta_neff_entropy_scaling(gstar_new: float) -> float:
    """Standard scaling for the same decoupled relativistic species."""
    return DELTA_NEFF_BASE * (GSTAR_BASE / gstar_new) ** (4.0 / 3.0)


def required_gstar_for_delta_neff(target: float) -> float:
    return GSTAR_BASE * (DELTA_NEFF_BASE / target) ** (3.0 / 4.0)


def dimensionless_transverse_distance(z: float, omega_k: float) -> tuple[float, float]:
    """Return radial chi and H0*D_M/c for a simple FLRW background."""
    omega_lambda = 1.0 - OMEGA_M - OMEGA_R - omega_k
    x_start = math.log(1.0 / (1.0 + z))
    x = np.linspace(x_start, 0.0, 200001)
    a = np.exp(x)
    e = np.sqrt(
        OMEGA_R * a ** -4
        + OMEGA_M * a ** -3
        + omega_k * a ** -2
        + omega_lambda
    )
    chi = float(np.trapezoid(1.0 / (a * e), x))
    if abs(omega_k) < 1.0e-14:
        return chi, chi
    root = math.sqrt(abs(omega_k))
    if omega_k > 0.0:
        dm = math.sinh(root * chi) / root
    else:
        dm = math.sin(root * chi) / root
    return chi, dm


def find_curvature_for_distance_ratio(z: float, target_ratio: float) -> float | None:
    _, flat_dm = dimensionless_transverse_distance(z, 0.0)
    low, high = 0.0, 0.1
    high_ratio = dimensionless_transverse_distance(z, high)[1] / flat_dm
    if high_ratio < target_ratio:
        return None
    for _ in range(60):
        middle = (low + high) / 2.0
        ratio = dimensionless_transverse_distance(z, middle)[1] / flat_dm
        if ratio < target_ratio:
            low = middle
        else:
            high = middle
    return (low + high) / 2.0


def main() -> int:
    desired_growth_ratio = S8_TARGET / S8_MODEL
    base_growth = rk4_growth(0.0)
    required_drag = find_drag_for_ratio(desired_growth_ratio)
    friction_ratio = rk4_growth(required_drag, drag_sign=1.0) / base_growth
    same_magnitude_wrong_sign_ratio = rk4_growth(required_drag, drag_sign=-1.0) / base_growth

    decay_fractions = {
        str(lifetime): 1.0 - math.exp(-AGE_GYR / lifetime)
        for lifetime in (50.0, 100.0, 137.0, 220.0)
    }

    neff_examples = {
        str(gstar): delta_neff_entropy_scaling(gstar)
        for gstar in (106.75, 150.0, 200.0, 300.0)
    }
    neff_required_gstar = {
        str(target): required_gstar_for_delta_neff(target)
        for target in (0.15, 0.20)
    }

    z_star = 1089.92
    _, dm_flat = dimensionless_transverse_distance(z_star, 0.0)
    chi_claim, dm_claim = dimensionless_transverse_distance(z_star, 0.002)
    distance_ratio_claim = dm_claim / dm_flat
    h0_ratio_claim = H0_CURVATURE_CLAIM / H0_BASE
    curvature_needed = find_curvature_for_distance_ratio(z_star, h0_ratio_claim)

    output = {
        "scope": "arithmetic_and_toy_model_screening_only",
        "track_1_late_drag": {
            "S8_model": S8_MODEL,
            "S8_target": S8_TARGET,
            "required_growth_ratio": desired_growth_ratio,
            "drag_active_for_a_greater_equal": 0.5,
            "required_dimensionless_constant_drag_toy_model": required_drag,
            "achieved_ratio_with_plus_drag": friction_ratio,
            "ratio_with_same_term_entering_with_minus_sign": same_magnitude_wrong_sign_ratio,
            "sign_result": "positive addition to the D-prime coefficient suppresses growth",
            "physical_status": "NOT_A_COVARIANT_PERTURBATION_MODEL",
        },
        "track_2_decay": {
            "age_Gyr": AGE_GYR,
            "fraction_of_pre_existing_component_decayed": decay_fractions,
            "warning": "ongoing production and daughter perturbations are not included",
        },
        "track_3_entropy": {
            "baseline_gstar": GSTAR_BASE,
            "baseline_delta_Neff": DELTA_NEFF_BASE,
            "same_relic_delta_Neff_for_higher_visible_gstar": neff_examples,
            "visible_gstar_required_for_target_under_same_scaling": neff_required_gstar,
            "sign_result": "higher visible-sector gstar dilutes, rather than raises, Delta Neff",
        },
        "track_4_curvature": {
            "z_star": z_star,
            "Omega_K_claim": 0.002,
            "radial_chi_at_claim": chi_claim,
            "dimensionless_transverse_distance_ratio_to_flat": distance_ratio_claim,
            "claimed_H0_ratio": h0_ratio_claim,
            "Omega_K_needed_in_this_fixed_density_distance_screen": curvature_needed,
            "warning": "not a CMB+BAO likelihood and not a derivation from graph topology",
        },
        "overall_status": "SCREEN_COMPLETED_NOT_FULLY_VERIFIED",
    }
    print(json.dumps(output, indent=2, sort_keys=True))

    numerical_checks = [
        abs(friction_ratio - desired_growth_ratio) < 1.0e-8,
        same_magnitude_wrong_sign_ratio > 1.0,
        neff_examples["200.0"] < DELTA_NEFF_BASE,
        decay_fractions["50.0"] > decay_fractions["100.0"],
    ]
    return 0 if all(numerical_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
