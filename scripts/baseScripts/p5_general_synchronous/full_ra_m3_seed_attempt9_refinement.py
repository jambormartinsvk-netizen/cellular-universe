"""One-step numerical residual audit for preregistered KMPC-030.

The module defines no physical equation.  It captures matrices produced by
the frozen J8 builder, applies one deterministic correction in equilibrated
coordinates, and reuses the frozen residual/holdout/truncation metrics.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
import time
from typing import Callable

import numpy as np

from . import full_ra_m3_seed as physics
from . import full_ra_m3_seed_attempt8_ladder as ladder


RUN_ID = "KMPC-030"
OUTPUT_NAME = "RUN_KMPC_030_P5_3G7_M3_FULL_RA_J8_ONE_REFINEMENT_AUDIT.json"
J4_NAME = ladder.REFERENCE_NAME
J4_SHA256 = ladder.REFERENCE_SHA256
J6_NAME = "RUN_KMPC_029_P5_3G7_M3_FULL_RA_SUPPORT_J6.json"
J6_SHA256 = "658495A11A3C72262CDCBEC9B9515794E506A6C7F14F40865704AA26E6C4636A"
J8_NAME = "RUN_KMPC_029_P5_3G7_M3_FULL_RA_SUPPORT_J8.json"
J8_SHA256 = "1EE3FCDF3B77C6C7E4C26317A3F39AA45D4CFA5BA6B559E312E598BC3ED51AB8"
SUPPORT = 8
EXPECTED_F0 = 18
EXPECTED_M3 = 117
FROZEN_SCOPE = (
    "conditional Phi1 M3-TCA0 AD/k=0.05/nominal J8 one-refinement "
    "numerical audit only; no Phi2 CDM recoil, boundary closure, ODE, "
    "finite opacity, full hierarchy, CMB, S8, or S-M claim"
)


def _hash(path: Path) -> str:
    return physics.sha256_file(path)


def _row_provenance(
    matrix: np.ndarray,
    constant: np.ndarray,
    solution: np.ndarray,
    labels: list[str],
) -> list[dict[str, object]]:
    residual = matrix @ solution + constant
    term_norm = np.abs(constant) + np.sum(
        np.abs(matrix * solution[np.newaxis, :]), axis=1
    )
    row_scale = np.maximum(
        np.maximum(np.max(np.abs(matrix), axis=1), np.abs(constant)),
        1.0e-300,
    )
    output: list[dict[str, object]] = []
    for index, label in enumerate(labels):
        relative = bool(term_norm[index] > physics.ABS_FALLBACK_NORM)
        metric = (
            abs(residual[index]) / term_norm[index]
            if relative
            else abs(residual[index])
        )
        output.append(
            {
                "row": label,
                "signed_residual": float(residual[index]),
                "absolute_residual": float(abs(residual[index])),
                "term_norm": float(term_norm[index]),
                "metric_branch": "relative" if relative else "absolute",
                "metric_value": float(metric),
                "row_scale": float(row_scale[index]),
                "term_norm_over_branch_boundary": float(
                    term_norm[index] / physics.ABS_FALLBACK_NORM
                ),
            }
        )
    return output


def _row_contributions(
    matrix: np.ndarray,
    constant: np.ndarray,
    solution: np.ndarray,
    row_index: int,
    column_labels: list[str],
) -> dict[str, object]:
    contributions = matrix[row_index, :] * solution
    return {
        "constant": float(constant[row_index]),
        "affine_contributions": [
            {"column": label, "value": float(value)}
            for label, value in zip(column_labels, contributions, strict=True)
        ],
        "sum": float(constant[row_index] + np.sum(contributions)),
        "sum_absolute_terms": float(
            abs(constant[row_index]) + np.sum(np.abs(contributions))
        ),
    }


def _vector_to_fractional(vector: np.ndarray) -> dict[str, dict[int, float]]:
    exponents = list(range(0, SUPPORT + 1))
    index = 0
    state: dict[str, dict[int, float]] = {}
    for name in physics.contract.AUTHORITATIVE_STATE:
        state[name] = {}
        for power in exponents:
            state[name][power] = float(vector[index])
            index += 1
    if index != EXPECTED_M3:
        raise RuntimeError(f"refined vector map consumed {index}, expected {EXPECTED_M3}")
    return state


def _all_finite(*arrays: np.ndarray) -> bool:
    return all(bool(np.all(np.isfinite(array))) for array in arrays)


def _residual_vector_metrics(
    residual: np.ndarray,
    term_norm: np.ndarray,
    labels: list[str],
    relative_tolerance: float,
) -> dict[str, object]:
    """Audit an already evaluated residual with the frozen branch rule."""
    if residual.shape != term_norm.shape or residual.size != len(labels):
        raise ValueError("residual/term-norm/label shape mismatch")
    relative_mask = term_norm > physics.ABS_FALLBACK_NORM
    ratios = np.zeros_like(residual)
    ratios[relative_mask] = (
        np.abs(residual[relative_mask]) / term_norm[relative_mask]
    )
    relative_indices = np.flatnonzero(relative_mask)
    absolute_indices = np.flatnonzero(~relative_mask)
    relative_worst = (
        int(relative_indices[np.argmax(ratios[relative_mask])])
        if relative_indices.size
        else None
    )
    absolute_worst = (
        int(absolute_indices[np.argmax(np.abs(residual[~relative_mask]))])
        if absolute_indices.size
        else None
    )
    relative_max = (
        float(np.max(ratios[relative_mask])) if relative_indices.size else 0.0
    )
    absolute_max = (
        float(np.max(np.abs(residual[~relative_mask])))
        if absolute_indices.size
        else 0.0
    )
    return {
        "max_relative_residual": relative_max,
        "max_absolute_fallback_residual": absolute_max,
        "worst_relative_row": (
            labels[relative_worst] if relative_worst is not None else None
        ),
        "worst_absolute_fallback_row": (
            labels[absolute_worst] if absolute_worst is not None else None
        ),
        "relative_row_count": int(np.sum(relative_mask)),
        "absolute_fallback_row_count": int(np.sum(~relative_mask)),
        "relative_tolerance": relative_tolerance,
        "absolute_tolerance": physics.ABS_FALLBACK_TOL,
        "pass": bool(
            relative_max <= relative_tolerance
            and absolute_max <= physics.ABS_FALLBACK_TOL
        ),
    }


def run_audit(
    result_dir: Path,
    expected_source_hashes: dict[str, str],
    expected_ladder_hash: str,
    observed_ladder_hash: str,
    expected_wrapper_hash: str,
    observed_wrapper_hash: str,
    max_runtime_seconds: float,
    progress: dict[str, str],
) -> dict[str, object]:
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError(f"{RUN_ID} internal deadline exceeded")

    evidence_paths = {
        "J4": (result_dir / J4_NAME, J4_SHA256),
        "J6": (result_dir / J6_NAME, J6_SHA256),
        "J8": (result_dir / J8_NAME, J8_SHA256),
    }
    evidence: dict[str, object] = {}
    loaded: dict[str, dict[str, object]] = {}
    for label, (path, expected_hash) in evidence_paths.items():
        observed_hash = _hash(path)
        if observed_hash != expected_hash:
            raise RuntimeError(f"{label} evidence hash mismatch")
        loaded[label] = json.loads(path.read_text(encoding="utf-8"))
        evidence[label] = {"path": path.name, "sha256": observed_hash}
    progress["last_completed_phase"] = "IMMUTABLE_INPUTS"
    deadline()

    progress["current_phase"] = "FROZEN_GUARDS_AND_M1_F0"
    frozen_contract = physics.validate_frozen_contract()
    frozen_b1 = physics.b1_guard.build_contract_guard(
        max_runtime_seconds=min(1.0, max_runtime_seconds)
    )
    tca0_bridge = physics.production_tca0_reduction_guard()
    inputs = physics._variant_inputs("nominal")
    standard, standard_meta = ladder._standard_state_for_support(
        SUPPORT, inputs, deadline
    )
    before_counts = {
        "F0": physics.EXPECTED_F0_EXTENDED["AD"],
        "M3": physics.EXPECTED_M3_EXTENDED["AD"],
    }
    if before_counts != {"F0": 10, "M3": 65}:
        raise RuntimeError(f"unexpected shape guards {before_counts}")
    original_affine = physics._affine_system
    original_solver = physics._solve_equilibrated
    original_holdout_metrics = physics._holdout_metrics
    affine_calls: list[dict[str, object]] = []
    solver_capture: dict[str, object] = {}
    holdout_metric_capture: dict[str, object] = {}

    def capture_affine(
        ledger: Callable[[np.ndarray], np.ndarray],
        count: int,
        local_deadline: Callable[[], None] | None = None,
    ) -> tuple[np.ndarray, np.ndarray]:
        matrix, constant = original_affine(ledger, count, local_deadline)
        affine_calls.append(
            {"ledger": ledger, "matrix": matrix.copy(), "constant": constant.copy()}
        )
        return matrix, constant

    def capture_solver(
        matrix: np.ndarray,
        constant: np.ndarray,
        expected_rank: int,
        labels: list[str] | None = None,
        local_deadline: Callable[[], None] | None = None,
    ) -> tuple[np.ndarray, dict[str, object]]:
        solution, diagnostics = original_solver(
            matrix, constant, expected_rank, labels, local_deadline
        )
        if expected_rank != EXPECTED_M3:
            raise RuntimeError(f"captured unexpected M3 rank {expected_rank}")
        solver_capture.update(
            {
                "matrix": matrix.copy(),
                "constant": constant.copy(),
                "solution": solution.copy(),
                "diagnostics": dict(diagnostics),
                "labels": list(labels or []),
            }
        )
        return solution, diagnostics

    def capture_holdout_metrics(
        matrix: np.ndarray,
        constant: np.ndarray,
        solution: np.ndarray,
        labels: list[str] | None = None,
    ) -> dict[str, object]:
        metrics = original_holdout_metrics(matrix, constant, solution, labels)
        holdout_metric_capture.update(
            {
                "matrix": matrix.copy(),
                "constant": constant.copy(),
                "solution": solution.copy(),
                "labels": list(labels or []),
            }
        )
        return metrics

    progress["current_phase"] = "F0_AND_CAPTURE_FROZEN_J8"
    try:
        physics.EXPECTED_F0_EXTENDED["AD"] = EXPECTED_F0
        physics.EXPECTED_M3_EXTENDED["AD"] = EXPECTED_M3
        fuel, fuel_diag = physics._solve_fuel_zero(
            "AD", 0.05, inputs, standard, (0, SUPPORT), deadline
        )
        combined_standard = dict(standard)
        combined_standard.update(fuel)
        progress["last_completed_phase"] = "FROZEN_GUARDS_AND_M1_F0"
        try:
            physics._affine_system = capture_affine
            physics._solve_equilibrated = capture_solver
            physics._holdout_metrics = capture_holdout_metrics
            original_fractional, original_meta = physics._solve_m3(
                "AD", 0.05, inputs, combined_standard, (0, SUPPORT), deadline
            )
            progress["last_completed_phase"] = "CAPTURE_FROZEN_J8"
        finally:
            physics._affine_system = original_affine
            physics._solve_equilibrated = original_solver
            physics._holdout_metrics = original_holdout_metrics
    finally:
        physics.EXPECTED_F0_EXTENDED["AD"] = before_counts["F0"]
        physics.EXPECTED_M3_EXTENDED["AD"] = before_counts["M3"]

    hooks_restored = bool(
        physics._affine_system is original_affine
        and physics._solve_equilibrated is original_solver
        and physics._holdout_metrics is original_holdout_metrics
        and physics.EXPECTED_F0_EXTENDED["AD"] == before_counts["F0"]
        and physics.EXPECTED_M3_EXTENDED["AD"] == before_counts["M3"]
    )
    if len(affine_calls) != 2 or not solver_capture or not holdout_metric_capture:
        raise RuntimeError(
            f"expected driver+holdout affine captures, got {len(affine_calls)}"
        )
    driver_capture, holdout_capture = affine_calls
    matrix = driver_capture["matrix"]
    constant = driver_capture["constant"]
    ledger = driver_capture["ledger"]
    holdout_ledger = holdout_capture["ledger"]
    original_solution = solver_capture["solution"]
    driver_labels = solver_capture["labels"]
    expected_driver_labels = [
        f"{row}[{power}]"
        for row in physics.contract.AUTHORITATIVE_DRIVER
        for power in range(0, SUPPORT + 1)
    ]
    expected_holdout_labels = [
        f"{row}[{power}]"
        for row in physics.contract.AUTHORITATIVE_HOLDOUT
        for power in range(0, SUPPORT + 1)
    ]
    capture_contract = bool(
        matrix.shape == (EXPECTED_M3, EXPECTED_M3)
        and constant.shape == (EXPECTED_M3,)
        and holdout_capture["matrix"].shape == (EXPECTED_F0, EXPECTED_M3)
        and holdout_capture["constant"].shape == (EXPECTED_F0,)
        and driver_labels == expected_driver_labels
        and holdout_metric_capture["labels"] == expected_holdout_labels
        and np.array_equal(solver_capture["matrix"], matrix)
        and np.array_equal(solver_capture["constant"], constant)
        and np.array_equal(holdout_metric_capture["matrix"], holdout_capture["matrix"])
        and np.array_equal(
            holdout_metric_capture["constant"], holdout_capture["constant"]
        )
        and np.array_equal(holdout_metric_capture["solution"], original_solution)
    )
    if not capture_contract:
        raise RuntimeError("driver/holdout capture role or ordering mismatch")
    deadline()

    progress["current_phase"] = "ONE_DETERMINISTIC_REFINEMENT"
    row_scale = np.maximum(
        np.maximum(np.max(np.abs(matrix), axis=1), np.abs(constant)),
        1.0e-300,
    )
    row_matrix = matrix / row_scale[:, np.newaxis]
    row_constant = constant / row_scale
    column_scale = np.maximum(np.max(np.abs(row_matrix), axis=0), 1.0e-300)
    equilibrated = row_matrix / column_scale[np.newaxis, :]
    b_equilibrated = -row_constant
    y0 = original_solution * column_scale
    correction_rhs = b_equilibrated - equilibrated @ y0
    delta_y = np.linalg.solve(equilibrated, correction_rhs)
    y1 = y0 + delta_y
    refined_solution = y1 / column_scale
    correction_count = 1
    refined_fractional = _vector_to_fractional(refined_solution)
    leading_j = int(physics.legacy.MODE_SPECS["AD"]["leading_j"])
    refined_forbidden_max = max(
        abs(refined_fractional[name][power])
        for name in physics.contract.AUTHORITATIVE_STATE
        for power in range(0, min(leading_j, SUPPORT + 1))
    )
    refined_uc_lower_regular_max = max(
        abs(refined_fractional["U_c"][power])
        for power in range(0, min(leading_j, SUPPORT + 1))
    )
    original_metrics = physics._row_residual_metrics(
        matrix, constant, original_solution, driver_labels
    )
    refined_metrics = physics._row_residual_metrics(
        matrix, constant, refined_solution, driver_labels
    )
    holdout_matrix = holdout_capture["matrix"]
    holdout_constant = holdout_capture["constant"]
    holdout_labels = holdout_metric_capture["labels"]
    refined_holdout = physics._holdout_metrics(
        holdout_matrix,
        holdout_constant,
        refined_solution,
        holdout_labels,
    )
    direct_original = np.asarray(ledger(original_solution), dtype=float)
    direct_refined = np.asarray(ledger(refined_solution), dtype=float)
    direct_holdout_refined = np.asarray(holdout_ledger(refined_solution), dtype=float)
    affine_original = matrix @ original_solution + constant
    affine_refined = matrix @ refined_solution + constant
    affine_holdout_refined = holdout_matrix @ refined_solution + holdout_constant
    original_term_norm = np.abs(constant) + np.sum(
        np.abs(matrix * original_solution[np.newaxis, :]), axis=1
    )
    refined_term_norm = np.abs(constant) + np.sum(
        np.abs(matrix * refined_solution[np.newaxis, :]), axis=1
    )
    refined_holdout_term_norm = np.abs(holdout_constant) + np.sum(
        np.abs(holdout_matrix * refined_solution[np.newaxis, :]), axis=1
    )
    direct_original_metrics = _residual_vector_metrics(
        direct_original, original_term_norm, driver_labels, physics.DRIVER_TOL
    )
    direct_refined_metrics = _residual_vector_metrics(
        direct_refined, refined_term_norm, driver_labels, physics.DRIVER_TOL
    )
    direct_holdout_metrics = _residual_vector_metrics(
        direct_holdout_refined,
        refined_holdout_term_norm,
        holdout_labels,
        physics.HOLDOUT_TOL,
    )
    extraction_original_metrics = _residual_vector_metrics(
        direct_original - affine_original,
        original_term_norm,
        driver_labels,
        physics.DRIVER_TOL,
    )
    extraction_refined_metrics = _residual_vector_metrics(
        direct_refined - affine_refined,
        refined_term_norm,
        driver_labels,
        physics.DRIVER_TOL,
    )
    extraction_holdout_metrics = _residual_vector_metrics(
        direct_holdout_refined - affine_holdout_refined,
        refined_holdout_term_norm,
        holdout_labels,
        physics.HOLDOUT_TOL,
    )
    extraction_difference = {
        "original_max_abs": float(np.max(np.abs(direct_original - affine_original))),
        "refined_max_abs": float(np.max(np.abs(direct_refined - affine_refined))),
        "refined_holdout_max_abs": float(
            np.max(np.abs(direct_holdout_refined - affine_holdout_refined))
        ),
    }
    progress["last_completed_phase"] = "ONE_DETERMINISTIC_REFINEMENT"
    deadline()

    original_rows = _row_provenance(
        matrix, constant, original_solution, driver_labels
    )
    refined_rows = _row_provenance(
        matrix, constant, refined_solution, driver_labels
    )
    worst_label = str(original_metrics["worst_relative_row"])
    worst_index = driver_labels.index(worst_label)
    column_labels = [
        f"{name}[{power}]"
        for name in physics.contract.AUTHORITATIVE_STATE
        for power in range(0, SUPPORT + 1)
    ]
    worst_provenance = {
        "row": worst_label,
        "original": _row_contributions(
            matrix, constant, original_solution, worst_index, column_labels
        ),
        "refined": _row_contributions(
            matrix, constant, refined_solution, worst_index, column_labels
        ),
    }

    stored_j8 = ladder._restore_series(
        loaded["J8"]["m3"]["fractional_state"]
    )
    stored_j8_diag = loaded["J8"]["m3"]["diagnostics"]
    original_reproduction = physics._coefficient_metrics(
        stored_j8, original_fractional
    )
    refined_drift = physics._coefficient_metrics(
        original_fractional, refined_fractional
    )
    all_arrays_finite = _all_finite(
        matrix,
        constant,
        row_scale,
        row_matrix,
        row_constant,
        column_scale,
        equilibrated,
        b_equilibrated,
        y0,
        original_solution,
        correction_rhs,
        delta_y,
        y1,
        refined_solution,
        holdout_matrix,
        holdout_constant,
        direct_original,
        direct_refined,
        direct_holdout_refined,
        affine_original,
        affine_refined,
        affine_holdout_refined,
    )
    refined_series_finite = ladder._series_finite(refined_fractional)
    original_diag = original_meta["diagnostics"]
    incident_reproduced = bool(
        not bool(stored_j8_diag["pass_driver"])
        and stored_j8_diag["worst_relative_row"] == "fuel_Euler[8]"
        and not bool(original_metrics["pass_driver"])
        and original_metrics["worst_relative_row"] == "fuel_Euler[8]"
        and math.isclose(
            float(original_metrics["max_relative_residual"]),
            float(stored_j8_diag["max_relative_residual"]),
            rel_tol=1.0e-12,
            abs_tol=1.0e-18,
        )
    )
    numerical_checks = {
        "frozen_contract": bool(frozen_contract["valid"]),
        "frozen_B1": (
            frozen_b1["execution_verdict"]
            == "PASS_R_A_B1_CONTRACT_GUARD_ONLY"
        ),
        "TCA0_bridge": bool(tca0_bridge["pass"]),
        "M1": bool(standard_meta["pass"]),
        "F0": bool(
            fuel_diag["pass_rank"]
            and fuel_diag["pass_driver"]
            and fuel_diag["pass_leading_postcheck"]
        ),
        "original_rank": bool(
            original_diag["pass_rank"]
            and original_diag["equilibrated_rank_rcond"] == EXPECTED_M3
        ),
        "original_holdout": bool(original_diag["holdout"]["pass_holdout"]),
        "original_structural_guards": bool(
            original_diag["pass_forbidden_layers"]
            and original_diag["pass_forbidden_stress_guard"]
            and original_diag["pass_production_contract"]
            and original_diag["Uc_lower_regular_max_abs"] <= physics.LEADING_TOL
        ),
        "hooks_and_shape_guards_restored": hooks_restored,
        "original_reproduction": bool(original_reproduction["pass"]),
        "original_incident_reproduced": incident_reproduced,
        "capture_role_order_and_solver_identity": capture_contract,
        "exactly_one_correction": correction_count == 1,
        "all_arrays_and_refined_series_finite": bool(
            all_arrays_finite and refined_series_finite
        ),
        "direct_affine_extraction": bool(
            max(extraction_difference.values()) <= physics.ABS_FALLBACK_TOL
            and extraction_original_metrics["pass"]
            and extraction_refined_metrics["pass"]
            and extraction_holdout_metrics["pass"]
        ),
        "refined_driver": bool(refined_metrics["pass_driver"]),
        "refined_direct_driver": bool(direct_refined_metrics["pass"]),
        "refined_holdout": bool(refined_holdout["pass_holdout"]),
        "refined_direct_holdout": bool(direct_holdout_metrics["pass"]),
        "refined_forbidden_layers": bool(
            refined_forbidden_max <= physics.FORBIDDEN_TOL
        ),
        "refined_Uc_lower_regular": bool(
            refined_uc_lower_regular_max <= physics.LEADING_TOL
        ),
        "refined_coefficient_drift": bool(refined_drift["pass"]),
    }
    numerical_complete = bool(numerical_checks) and all(numerical_checks.values())

    progress["current_phase"] = "LADDER_CLOSURE_NO_SOLVE"
    j4 = ladder._restore_series(
        loaded["J4"]["result"]["m3_extended"]["fractional_state"]
    )
    j4_f0 = ladder._restore_series(
        loaded["J4"]["result"]["fuel_extended"]["state"]
    )
    j6 = ladder._restore_series(loaded["J6"]["m3"]["fractional_state"])
    j6_f0 = ladder._restore_series(loaded["J6"]["fuel"]["state"])
    bridges = {
        "J4_J6_M3": physics._coefficient_metrics(j4, j6),
        "J4_J6_F0": physics._coefficient_metrics(j4_f0, j6_f0),
        "J6_J8_refined_M3": physics._coefficient_metrics(j6, refined_fractional),
        "J6_J8_F0": physics._coefficient_metrics(j6_f0, fuel),
    }
    j4_j6_tail = physics._truncation_metrics("AD", j4, j6, inputs, 0.05)
    j6_j8_tail = physics._truncation_metrics(
        "AD", j6, refined_fractional, inputs, 0.05
    )
    tail_detail = {
        "J4_J6": ladder._per_state_tail_and_new_terms(j4, j6),
        "J6_J8_refined": ladder._per_state_tail_and_new_terms(
            j6, refined_fractional
        ),
    }
    exact_powers = bool(
        tail_detail["J4_J6"]["added_powers"] == [5, 6]
        and tail_detail["J6_J8_refined"]["added_powers"] == [7, 8]
    )
    dominant_membership = bool(
        all(
            item["power"] in tail_detail["J4_J6"]["added_powers"]
            for item in tail_detail["J4_J6"]["dominant_new_term_by_z"].values()
        )
        and all(
            item["power"] in tail_detail["J6_J8_refined"]["added_powers"]
            for item in tail_detail["J6_J8_refined"]["dominant_new_term_by_z"].values()
        )
    )
    normalized_tail_scalar_by_z = {
        str(z): {
            "J4_J6": ladder._normalized_tail_scalar(j4_j6_tail, z),
            "J6_J8_refined": ladder._normalized_tail_scalar(j6_j8_tail, z),
        }
        for z in physics.Z_SURFACES
    }
    monotone_by_z = {
        str(z): bool(
            normalized_tail_scalar_by_z[str(z)]["J6_J8_refined"]
            <= normalized_tail_scalar_by_z[str(z)]["J4_J6"]
        )
        for z in physics.Z_SURFACES
    }
    ladder_checks = {
        "all_F0_M3_common_coefficient_bridges": all(
            bool(value["pass"]) for value in bridges.values()
        ),
        "exact_added_powers": exact_powers,
        "dominant_new_power_membership": dominant_membership,
        "tail_monotone_on_both_surfaces": all(monotone_by_z.values()),
        "tail_details_finite": bool(
            tail_detail["J4_J6"]["finite"]
            and tail_detail["J6_J8_refined"]["finite"]
        ),
    }
    ladder_structural = all(ladder_checks.values())
    if numerical_complete and ladder_structural and j4_j6_tail["pass"] and j6_j8_tail["pass"]:
        candidate = "CANDIDATE_J4_PRODUCTION_ADEQUATE"
    elif numerical_complete and ladder_structural and (not j4_j6_tail["pass"]) and j6_j8_tail["pass"]:
        candidate = "CANDIDATE_J6_MINIMUM_PRODUCTION_SUPPORT"
    else:
        candidate = "REVIEW_LADDER_STILL_UNCLOSED"
    progress["last_completed_phase"] = "LADDER_CLOSURE_NO_SOLVE"
    deadline()

    return {
        "test": "KMPC-030 J8 residual provenance and one refinement",
        "run_id": RUN_ID,
        "scope": FROZEN_SCOPE,
        "evidence": evidence,
        "source_hashes": expected_source_hashes,
        "attempt8_ladder_wrapper_sha256": observed_ladder_hash,
        "attempt9_wrapper_sha256": observed_wrapper_hash,
        "thresholds": {
            **ladder.expected_thresholds(),
            "direct_affine_max_abs": physics.ABS_FALLBACK_TOL,
            "coefficient_drift_relative": physics.LOW_COEFFICIENT_TOL,
            "refined_forbidden_layer": physics.FORBIDDEN_TOL,
            "refined_Uc_lower_regular": physics.LEADING_TOL,
            "incident_reproduction_relative": 1.0e-12,
            "incident_reproduction_absolute": 1.0e-18,
        },
        "M1": standard_meta,
        "F0": {"state": fuel, "diagnostics": fuel_diag},
        "original_J8": {
            "diagnostics": original_diag,
            "reproduction_vs_immutable": original_reproduction,
            "driver_metrics_recomputed": original_metrics,
        },
        "one_refinement": {
            "correction_count": correction_count,
            "correction_rhs_max_abs": float(np.max(np.abs(correction_rhs))),
            "delta_y_max_abs": float(np.max(np.abs(delta_y))),
            "driver_metrics": refined_metrics,
            "direct_driver_metrics": direct_refined_metrics,
            "holdout_metrics": refined_holdout,
            "direct_holdout_metrics": direct_holdout_metrics,
            "refined_forbidden_max_abs": refined_forbidden_max,
            "refined_Uc_lower_regular_max_abs": refined_uc_lower_regular_max,
            "coefficient_drift": refined_drift,
            "fractional_state": refined_fractional,
        },
        "residual_provenance": {
            "original_rows": original_rows,
            "refined_rows": refined_rows,
            "worst_original_row_contributions": worst_provenance,
            "direct_vs_affine_max_abs": extraction_difference,
            "direct_original_metrics": direct_original_metrics,
            "direct_refined_metrics": direct_refined_metrics,
            "direct_holdout_refined_metrics": direct_holdout_metrics,
            "direct_vs_affine_branch_metrics": {
                "original_driver": extraction_original_metrics,
                "refined_driver": extraction_refined_metrics,
                "refined_holdout": extraction_holdout_metrics,
            },
        },
        "restoration": {
            "hooks_and_shape_guards_restored": hooks_restored,
            "before_shape_counts": before_counts,
            "after_shape_counts": {
                "F0": physics.EXPECTED_F0_EXTENDED["AD"],
                "M3": physics.EXPECTED_M3_EXTENDED["AD"],
            },
        },
        "numerical_checks": numerical_checks,
        "ladder_closure": {
            "checks": ladder_checks,
            "coefficient_bridges": bridges,
            "tails": {
                "J4_J6": j4_j6_tail,
                "J6_J8_refined": j6_j8_tail,
            },
            "per_state_tail_and_new_terms": tail_detail,
            "normalized_tail_scalar_by_z": normalized_tail_scalar_by_z,
            "tail_monotone_by_z": monotone_by_z,
            "status_if_numerical_gates_failed": (
                "DIAGNOSTIC_ONLY_NOT_A_CANDIDATE"
                if not numerical_complete
                else "ELIGIBLE_FOR_CANDIDATE_INTERPRETATION"
            ),
        },
        "execution_status": (
            "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT"
            if numerical_complete
            else "REVIEW_J8_RESIDUAL_PERSISTS_OR_PROVENANCE_UNCLOSED"
        ),
        "candidate_interpretation_not_verdict": candidate,
        "physics_verdict": "NONE_NOT_YET_AWARDED",
        "canonical_depth": "60/100",
        "score_effect": "NONE",
        "release_trigger": "NONE",
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
