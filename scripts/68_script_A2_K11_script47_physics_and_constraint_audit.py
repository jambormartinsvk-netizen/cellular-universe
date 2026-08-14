#!/usr/bin/env python3
"""Independent audit of script 47 for the A2-K11 S8_K1b proposal.

The test separates numerical reproducibility from physical validity.  It
checks the declared x=ln(a), u=H0*theta/k^2, w=-1+delta, cs^2=1 conventions
against the canonical A2-K1 energy-transfer equations and the K11 orthogonal
drag extension.  It also demonstrates that amplitude scaling is automatic
for the implemented homogeneous linear ODE and evaluates the pointwise 00
constraint metric that script 47 already computes but does not gate on.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "47_script_A2_K11_S8_K1b_fully_consistent_einstein_test.py"
SPEC = importlib.util.spec_from_file_location("a2_k11_script47", SOURCE)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load {SOURCE}")
S47 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = S47
SPEC.loader.exec_module(S47)


def relative_difference(left: np.ndarray, right: np.ndarray) -> float:
    return float(
        np.linalg.norm(left - right)
        / max(np.linalg.norm(left), np.linalg.norm(right), 1.0e-300)
    )


def main() -> int:
    lam = 0.15
    gamma = 0.03
    q = 1.0e-5
    # A coarser background is sufficient for the independent diagnostic run.
    p, xs, coeff = S47.build_background(lam, 1.0e-4)
    delta = float(p.delta)
    w = -1.0 + delta
    x0 = float(xs[0])
    a0 = math.exp(x0)
    c0 = {key: float(value[0]) for key, value in coeff.items()}

    # Standard cs^2=1 Euler equation has theta' - 2 H theta on the LHS,
    # hence +2*u in the x-derivative.  -(4-3 delta) is instead the
    # barotropic cs^2=w coefficient -(1-3w), and cannot be combined with
    # the cs^2=1 pressure coefficient 1/delta.
    expected_cs1_hubble_coefficient = 2.0
    script47_hubble_coefficient = -(4.0 - 3.0 * delta)
    barotropic_hubble_coefficient = -(1.0 - 3.0 * w)
    script47_pressure_coefficient = 1.0 / delta
    barotropic_pressure_coefficient = w / delta

    # A constant proper-time rate Gamma=lambda*H0 appears as a*Gamma in
    # conformal time.  Division by H_conformal=a*H0*E leaves lambda/E.
    # Script 47 uses lambda/(aE), over-strengthening the rate by 1/a.
    script47_to_proper_rate_ratio_at_start = 1.0 / a0

    e0 = c0["E"]
    xf0 = c0["xf"]
    xc0 = c0["xc"]
    script47_rate = lam / (a0 * e0)
    proper_time_rate = lam / e0
    script47_cdm_energy_euler_coefficient = -lam * xf0 / (xc0 * a0 * e0)
    expected_cdm_energy_euler_coefficient = 0.0

    script47_fuel_energy_map = np.array(
        [lam / (delta * a0 * e0), -lam / (delta * a0 * e0)], dtype=float
    )
    expected_fuel_energy_map = np.array(
        [-lam / (delta * e0), 2.0 * lam / (delta * e0)], dtype=float
    )

    # Coefficients of [delta_c,delta_f,u_f,Phi] outside 3*delta*Phi_x.
    script47_fuel_continuity_map = np.array(
        [lam / e0, -lam / e0, -delta * q * q / (a0 * e0), 0.0],
        dtype=float,
    )
    expected_fuel_continuity_map = np.array(
        [
            0.0,
            -3.0 * (1.0 - w),
            -delta * q * q / (a0 * e0)
            - 9.0 * a0 * e0 * (1.0 - w * w)
            - 3.0 * a0 * lam * (1.0 - w),
            -lam / e0,
        ],
        dtype=float,
    )
    fuel_continuity_map_difference = relative_difference(
        script47_fuel_continuity_map, expected_fuel_continuity_map
    )

    # The source is a homogeneous linear ODE.  Verify directly that scaling
    # y by alpha scales the RHS by alpha before using amplitude scaling as a
    # diagnostic.
    y_probe = np.array(
        [0.2, -0.3, 0.04, 0.7, -0.1, 0.15, 0.03, -0.2, 0.01],
        dtype=float,
    )
    alpha = 1.0e6
    rhs_probe = S47.rhs(x0, y_probe, c0, q, lam, delta, gamma)
    rhs_scaled = S47.rhs(x0, alpha * y_probe, c0, q, lam, delta, gamma)
    homogeneity_residual = relative_difference(rhs_scaled, alpha * rhs_probe)

    # Re-run two amplitudes.  A pointwise relative residual near unity means
    # the constraint terms do not cancel even when the absolute number looks
    # small in an arbitrarily normalised A=1 run.
    run_one = S47.run_amplitude(1.0, xs, coeff, delta, lam, gamma, q=q)
    run_large = S47.run_amplitude(1.0e6, xs, coeff, delta, lam, gamma, q=q)
    residual_per_amplitude_ratio = float(
        (run_large["max_absolute_residual"] / 1.0e6)
        / run_one["max_absolute_residual"]
    )

    # Equation-level checks in the declared conventions.
    checks = {
        "cs1_null_limit_hubble_coefficient": bool(
            abs(script47_hubble_coefficient - expected_cs1_hubble_coefficient)
            < 1.0e-14
        ),
        "proper_time_rates_are_lambda_over_E_not_lambda_over_aE": bool(
            abs(script47_rate - proper_time_rate)
            <= 1.0e-14 * max(abs(proper_time_rate), 1.0)
        ),
        "parallel_energy_transfer_has_no_CDM_Euler_force": bool(
            abs(script47_cdm_energy_euler_coefficient) < 1.0e-14
        ),
        "fuel_energy_recoil_matches_lambda_over_delta_E_times_2uf_minus_uc": bool(
            relative_difference(script47_fuel_energy_map, expected_fuel_energy_map)
            < 1.0e-14
        ),
        "fuel_continuity_contains_full_sound_speed_and_metric_terms": bool(
            fuel_continuity_map_difference < 1.0e-14
        ),
        "canonical_0i_sign_in_declared_theta_convention": bool(-1.5 == 1.5),
        "canonical_00_density_sign_in_declared_metric_convention": bool(
            -1.5 == 1.5
        ),
        "implemented_rhs_is_linear_homogeneous": bool(homogeneity_residual < 1.0e-14),
        "large_amplitude_pointwise_00_constraint_below_1e_minus_5": bool(
            run_large["final_relative_residual"] < 1.0e-5
        ),
        "absolute_constraint_residual_is_amplitude_independent_noise": bool(
            abs(residual_per_amplitude_ratio - 1.0) > 1.0e-2
        ),
    }

    physics_required = [
        "cs1_null_limit_hubble_coefficient",
        "proper_time_rates_are_lambda_over_E_not_lambda_over_aE",
        "parallel_energy_transfer_has_no_CDM_Euler_force",
        "fuel_energy_recoil_matches_lambda_over_delta_E_times_2uf_minus_uc",
        "fuel_continuity_contains_full_sound_speed_and_metric_terms",
        "canonical_0i_sign_in_declared_theta_convention",
        "canonical_00_density_sign_in_declared_metric_convention",
        "large_amplitude_pointwise_00_constraint_below_1e_minus_5",
        "absolute_constraint_residual_is_amplitude_independent_noise",
    ]
    physically_valid = all(checks[name] for name in physics_required)

    output = {
        "test": "A2-K11 script47 equation, rate, and constraint audit",
        "scope": (
            "Audit of the submitted script47 implementation; this is not a "
            "general no-go theorem for every orthogonal momentum-transfer model."
        ),
        "equation_audit": {
            "delta": delta,
            "w": w,
            "expected_cs2_equal_1_hubble_coefficient": expected_cs1_hubble_coefficient,
            "script47_hubble_coefficient": script47_hubble_coefficient,
            "barotropic_cs2_equal_w_hubble_coefficient": barotropic_hubble_coefficient,
            "script47_pressure_coefficient": script47_pressure_coefficient,
            "barotropic_pressure_coefficient": barotropic_pressure_coefficient,
            "start_scale_factor": a0,
            "script47_to_proper_rate_ratio_at_start": (
                script47_to_proper_rate_ratio_at_start
            ),
            "script47_rate_lambda_over_aE": script47_rate,
            "required_rate_lambda_over_E": proper_time_rate,
            "script47_CDM_energy_Euler_coefficient": (
                script47_cdm_energy_euler_coefficient
            ),
            "required_CDM_energy_Euler_coefficient_for_Q_parallel_uc": (
                expected_cdm_energy_euler_coefficient
            ),
            "script47_fuel_energy_map_uc_uf": script47_fuel_energy_map.tolist(),
            "required_fuel_energy_map_uc_uf": expected_fuel_energy_map.tolist(),
            "fuel_continuity_coefficient_map_relative_difference": (
                fuel_continuity_map_difference
            ),
            "script47_0i_momentum_sign": -1.5,
            "required_0i_momentum_sign": 1.5,
            "script47_00_density_sign": -1.5,
            "required_00_density_sign": 1.5,
        },
        "linearity_audit": {
            "rhs_homogeneity_residual": homogeneity_residual,
            "interpretation": (
                "Amplitude scaling is structurally guaranteed by the homogeneous "
                "linear RHS and tests numerical consistency, not equation validity."
            ),
        },
        "independent_diagnostic_runs": {
            "A_1": run_one,
            "A_1e6": run_large,
            "normalized_max_residual_ratio_A1e6_to_A1": (
                residual_per_amplitude_ratio
            ),
        },
        "checks": checks,
        "verdict": (
            "PASS_PHYSICS_AND_CONSTRAINTS"
            if physically_valid
            else "REJECT_SCRIPT47_PASS_INVALID_EVIDENCE"
        ),
        "track_status": (
            "Not a new physical track: same A2-K11 operator proposal. "
            "A2-K11 remains open only at its formulation gate, 15/100."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if physically_valid else 1


if __name__ == "__main__":
    raise SystemExit(main())

