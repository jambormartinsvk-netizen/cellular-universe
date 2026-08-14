"""AR50 overlay for the P5 mode-resolved Puiseux seed algebra.

V1 is preserved as an immutable REVIEW implementation.  This overlay changes
only the standard-seed normalization: the accepted M1 h coefficient is
eliminated from the least-squares unknowns and inserted exactly.  All species
rows, background series, fractional solver, holdouts, thresholds, and physical
inputs remain owned by V1.
"""

from __future__ import annotations

from typing import Callable

import numpy as np

from . import mode_resolved_puiseux as v1


FrozenInputs = v1.FrozenInputs
symbolic_identities = v1.symbolic_identities


def solve_hard_anchored_linear_system(
    matrix: np.ndarray,
    constant: np.ndarray,
    anchor_index: int,
    anchor_value: float,
) -> tuple[np.ndarray, int, np.ndarray]:
    """Solve M*x+constant=0 after exactly eliminating one anchored variable."""
    if matrix.ndim != 2 or constant.ndim != 1:
        raise ValueError("matrix must be 2D and constant must be 1D")
    if matrix.shape[0] != constant.size:
        raise ValueError("row count and constant size differ")
    if not 0 <= anchor_index < matrix.shape[1]:
        raise IndexError("anchor_index is outside the coefficient vector")
    remaining = [column for column in range(matrix.shape[1]) if column != anchor_index]
    reduced = matrix[:, remaining]
    right_hand_side = -constant - matrix[:, anchor_index] * anchor_value
    reduced_solution, _, rank, singular = np.linalg.lstsq(
        reduced, right_hand_side, rcond=None
    )
    solution = np.empty(matrix.shape[1], dtype=float)
    solution[anchor_index] = anchor_value
    solution[remaining] = reduced_solution
    return solution, int(rank), singular


def solve_standard_seed_anchored(
    mode: str,
    k_mpc: float,
    inputs: FrozenInputs,
    deadline: Callable[[], None],
    order: int = 5,
) -> tuple[dict[str, dict[int, float]], dict[str, object], dict[str, object]]:
    """V1 standard seed with the preregistered M1 amplitude as a hard anchor."""
    series = v1.Series(-4, order + 5)
    exponents = list(range(-1, order + 1))
    background = v1._standard_background(k_mpc, inputs, series)
    index = {
        (name, power): position
        for position, (name, power) in enumerate(
            (pair for name in v1.VARS for pair in ((name, exponent) for exponent in exponents))
        )
    }
    count = len(index)

    def unpack(vector: np.ndarray) -> dict[str, dict[int, float]]:
        return {
            name: {power: vector[index[(name, power)]] for power in exponents}
            for name in v1.VARS
        }

    initial = v1._initial_constraints(
        mode, inputs.radiation_weights[1], inputs.radiation_weights[0]
    )

    def ledger(vector: np.ndarray) -> np.ndarray:
        row_map = v1._standard_rows(unpack(vector), background, series)
        output = [
            series.coef(row_map[row], power)
            for row in v1.DRIVER_ROWS
            for power in exponents
        ]
        output.extend(
            vector[index[(name, power)]] - value for name, power, value in initial
        )
        return np.asarray(output, dtype=float)

    zero = np.zeros(count)
    constant = ledger(zero)
    matrix = np.empty((constant.size, count))
    for column in range(count):
        basis = np.zeros(count)
        basis[column] = 1.0
        matrix[:, column] = ledger(basis) - constant

    target_power, expected_h = v1._m1_expected_h(mode, background, inputs)
    anchor_index = index[("h", target_power)]
    solution, rank, singular = solve_hard_anchored_linear_system(
        matrix, constant, anchor_index, expected_h
    )
    state = unpack(solution)
    row_map = v1._standard_rows(state, background, series)
    checked_hi = max(target_power, v1.MODE_SPECS[mode]["f_max"])
    driver_max = max(
        abs(series.coef(row_map[row], power))
        for row in v1.DRIVER_ROWS
        for power in exponents
        if power <= checked_hi
    )
    holdout_max = max(
        abs(series.coef(row_map[row], power))
        for row in v1.HOLDOUT_ROWS
        for power in exponents
        if power <= checked_hi
    )
    observed_h = state["h"].get(target_power, 0.0)
    anchor_difference = abs(observed_h - expected_h)
    scale = max(
        max(abs(value) for values in state.values() for value in values.values()),
        abs(expected_h),
        1.0e-14,
    )
    resolved_condition = (
        float(singular[0] / singular[max(rank - 1, 0)])
        if singular.size and rank
        else float("inf")
    )
    metadata = {
        "rank": rank,
        "unknowns": count - 1,
        "full_vector_unknowns": count,
        "hard_anchor_method": "exact_column_elimination",
        "hard_anchor_variable": f"h[{target_power}]",
        "hard_anchor_absolute_difference": float(anchor_difference),
        "condition_resolved": resolved_condition,
        "driver_scaled_residual": float(driver_max / scale),
        "holdout_scaled_residual": float(holdout_max / scale),
        "m1_h_power": target_power,
        "m1_expected_h_coefficient": expected_h,
        "m1_observed_h_coefficient": observed_h,
        "m1_h_relative_difference": anchor_difference / max(abs(expected_h), 1.0e-14),
    }
    deadline()
    return state, background, metadata


def run_m3_tca0_anchored(
    max_runtime_seconds: float,
    k_values: tuple[float, ...] = (0.005, 0.05, 0.15),
    a_values: tuple[float, float] = (1.0e-6, 1.0e-4),
) -> dict[str, object]:
    """Run the unchanged V1 M3 audit with only its standard solver replaced."""
    original_solver = v1.solve_standard_seed
    if original_solver is not v1.solve_standard_seed:
        raise RuntimeError("unexpected standard solver identity before overlay")
    try:
        v1.solve_standard_seed = solve_standard_seed_anchored
        payload = v1.run_m3_tca0(max_runtime_seconds, k_values, a_values)
    finally:
        v1.solve_standard_seed = original_solver

    checks = payload["checks"]
    for k_mpc, by_mode in payload["mode_results"].items():
        for mode, result in by_mode.items():
            standard = result["standard"]
            checks[f"{k_mpc}_{mode}_M1_hard_anchor"] = (
                standard["hard_anchor_absolute_difference"] < 1.0e-14
            )
            checks[f"{k_mpc}_{mode}_standard_reduced_full_rank"] = (
                standard["rank"] == standard["unknowns"] == 76
                and standard["full_vector_unknowns"] == 77
            )
    passed = bool(checks) and all(bool(value) for value in checks.values())
    payload["test"] = "KMPC-024 P5.3g7 M3-TCA0 RERUN2 hard-M1-anchored seed"
    payload["normalization_correction"] = {
        "rule": "AR50",
        "method": "exact M1 h-column elimination",
        "V1_species_background_fractional_rows_changed": False,
    }
    payload["verdict"] = (
        "PASS_M3_TCA0_CONDITIONAL" if passed else "REVIEW_M3_TCA0_UNCLOSED"
    )
    payload["P5_3g7_verdict"] = (
        "REVIEW_BLOCKED_FINITE_OPACITY_AND_S_M" if passed else "REVIEW_BLOCKED_M3"
    )
    return payload

