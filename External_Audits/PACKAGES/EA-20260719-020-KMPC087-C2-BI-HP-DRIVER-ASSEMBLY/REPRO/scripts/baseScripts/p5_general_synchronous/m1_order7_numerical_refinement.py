"""KMPC-037 numerical refinement of the frozen KMPC-036 order-7 system."""

from __future__ import annotations

from contextlib import redirect_stdout
import hashlib
from io import StringIO
import json
import math
import platform
from pathlib import Path
import time
from typing import Callable, Mapping

import mpmath as mp
import numpy as np

from . import m1_order7_provenance as provenance
from . import mode_resolved_puiseux as v1


RUN_ID = "KMPC-037"
PRECISION_DPS = 80
REFINEMENT_LIMIT = 1
HIGH_PRECISION_SOLVE_LIMIT = 1
CORRECTION_ABS_MAX = 1.0e-14
AUDIT_LIMIT_SECONDS = 45.0
SMOKE_LIMIT_SECONDS = 4.8
EXPECTED_KMPC036 = (
    "RUN_KMPC_036_P5_3G7_M1_ORDER7_PROVENANCE_GATE.json",
    "39BB388669E74C9368BD823C5FF5C68A487B7FC1CD4F74EACBF64D9A08B7B497",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def source_hashes() -> dict[str, str]:
    root = Path(__file__).resolve().parent
    names = (
        "mode_resolved_puiseux.py",
        "mode_resolved_puiseux_v2_m1_anchored.py",
        "m1_order7_provenance.py",
        "m1_order7_numerical_refinement.py",
    )
    return {name: sha256_file(root / name) for name in names}


def _deadline(limit: float) -> tuple[float, Callable[[], None]]:
    if not math.isfinite(limit) or limit <= 0.0 or limit > AUDIT_LIMIT_SECONDS:
        raise ValueError("KMPC-037 runtime must be in (0,45]")
    started = time.monotonic()

    def check() -> None:
        if time.monotonic() - started > limit:
            raise TimeoutError("KMPC-037 internal deadline exceeded")

    return started, check


def _float_to_mpf(value: float) -> mp.mpf:
    number = float(value)
    if not math.isfinite(number):
        raise FloatingPointError("non-finite float64 input to high-precision solve")
    numerator, denominator = number.as_integer_ratio()
    return mp.mpf(numerator) / mp.mpf(denominator)


def _unpack_vector(
    vector: np.ndarray, pairs: tuple[tuple[str, int], ...]
) -> dict[str, dict[int, float]]:
    return {
        name: {
            power: float(vector[position])
            for position, (state, power) in enumerate(pairs)
            if state == name
        }
        for name in v1.VARS
    }


def _state_from_json(
    state: Mapping[str, Mapping[str, object]],
) -> dict[str, dict[int, float]]:
    """Restore integer Puiseux powers lost when the immutable state became JSON."""
    expected_powers = tuple(range(-1, 8))
    if set(state) != set(v1.VARS):
        raise ValueError("immutable JSON state registry mismatch")
    for name in v1.VARS:
        if set(state[name]) != {str(power) for power in expected_powers}:
            raise ValueError(f"immutable JSON power registry mismatch for {name}")
    return {
        name: {power: float(state[name][str(power)]) for power in expected_powers}
        for name in v1.VARS
    }


def _state_parity(state: Mapping[str, Mapping[int, float]]) -> bool:
    expected_powers = tuple(range(-1, 8))
    return bool(
        tuple(state) == tuple(v1.VARS)
        and all(tuple(state[name]) == expected_powers for name in v1.VARS)
    )


def _residual_invariants(metrics: Mapping[str, object]) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    passed = True
    raw_rows = metrics["rows"]
    if not isinstance(raw_rows, list):
        raise TypeError("residual rows must be a list")
    for row in raw_rows:
        scale = float(row["term_norm"]) if row["branch"] == "relative" else 1.0
        reconstructed = float(row["metric"]) * scale
        difference = abs(abs(float(row["residual"])) - reconstructed)
        bound = 8.0 * np.finfo(float).eps * max(
            abs(float(row["residual"])), abs(reconstructed), np.finfo(float).tiny
        )
        row_pass = difference <= bound
        passed = passed and row_pass
        rows.append(
            {
                "label": row["label"],
                "difference": difference,
                "roundoff_bound": bound,
                "pass": bool(row_pass),
            }
        )
    worst = max(
        rows,
        key=lambda item: float(item["difference"]) / float(item["roundoff_bound"]),
    )
    return {"rows": rows, "worst": worst, "pass": bool(passed)}


def _full_from_reduced(
    reduced_vector: np.ndarray, anchor_index: int, anchor_value: float, full_size: int
) -> np.ndarray:
    if reduced_vector.size != full_size - 1:
        raise ValueError("reduced vector size mismatch")
    full = np.empty(full_size, dtype=float)
    full[anchor_index] = anchor_value
    full[np.arange(full_size) != anchor_index] = reduced_vector
    return full


def _row_regression(
    current: Mapping[str, object], reference: Mapping[str, object]
) -> dict[str, object]:
    current_rows = current["rows"]
    reference_rows = reference["rows"]
    if not isinstance(current_rows, list) or not isinstance(reference_rows, list):
        raise TypeError("residual rows must be lists")
    if len(current_rows) != len(reference_rows):
        return {"pass": False, "reason": "row_count_mismatch"}
    rows: list[dict[str, object]] = []
    passed = True
    for observed, expected in zip(current_rows, reference_rows, strict=True):
        labels_equal = observed["label"] == expected["label"]
        residual_difference = abs(float(observed["residual"]) - float(expected["residual"]))
        residual_bound = max(
            provenance.REGRESSION_ABS_TOL,
            provenance.REGRESSION_REL_TOL
            * max(abs(float(observed["residual"])), abs(float(expected["residual"]))),
        )
        norm_difference = abs(float(observed["term_norm"]) - float(expected["term_norm"]))
        norm_bound = max(
            provenance.REGRESSION_ABS_TOL,
            provenance.REGRESSION_REL_TOL
            * max(abs(float(observed["term_norm"])), abs(float(expected["term_norm"]))),
        )
        row_pass = bool(
            labels_equal
            and observed["branch"] == expected["branch"]
            and residual_difference <= residual_bound
            and norm_difference <= norm_bound
        )
        passed = passed and row_pass
        rows.append(
            {
                "label": observed["label"],
                "residual_difference": residual_difference,
                "residual_bound": residual_bound,
                "term_norm_difference": norm_difference,
                "term_norm_bound": norm_bound,
                "pass": row_pass,
            }
        )
    worst = max(
        rows,
        key=lambda item: max(
            float(item["residual_difference"]) / float(item["residual_bound"]),
            float(item["term_norm_difference"]) / float(item["term_norm_bound"]),
        ),
    )
    return {"rows": rows, "worst": worst, "pass": bool(passed)}


def _float64_diagnostics(
    matrix: np.ndarray, right_hand_side: np.ndarray, vector: np.ndarray
) -> dict[str, float]:
    residual = matrix @ vector - right_hand_side
    denominator = (
        np.linalg.norm(matrix, ord=2) * np.linalg.norm(vector, ord=2)
        + np.linalg.norm(right_hand_side, ord=2)
    )
    backward_error = np.linalg.norm(residual, ord=2) / max(float(denominator), np.finfo(float).tiny)
    return {
        "residual_l2": float(np.linalg.norm(residual, ord=2)),
        "residual_linf": float(np.linalg.norm(residual, ord=np.inf)),
        "normal_equation_gradient_linf": float(
            np.linalg.norm(matrix.T @ residual, ord=np.inf)
        ),
        "normwise_backward_error": float(backward_error),
        "matrix_l2": float(np.linalg.norm(matrix, ord=2)),
        "solution_l2": float(np.linalg.norm(vector, ord=2)),
        "rhs_l2": float(np.linalg.norm(right_hand_side, ord=2)),
    }


def _mp_residual_metrics(
    matrix: np.ndarray,
    constant: np.ndarray,
    vector: list[mp.mpf],
    labels: tuple[str, ...],
) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    passed = True
    for row_index, label in enumerate(labels):
        raw = _float_to_mpf(float(constant[row_index]))
        norm = abs(raw)
        for column, value in enumerate(vector):
            coefficient = _float_to_mpf(float(matrix[row_index, column]))
            term = coefficient * value
            raw += term
            norm += abs(term)
        if norm > provenance.ABS_TOL:
            branch = "relative"
            metric = abs(raw) / norm
            row_pass = metric <= provenance.REL_TOL
        else:
            branch = "absolute"
            metric = abs(raw)
            row_pass = metric <= provenance.ABS_TOL
        invariant_difference = abs(abs(raw) - metric * (norm if branch == "relative" else 1))
        passed = passed and bool(row_pass)
        rows.append(
            {
                "label": label,
                "branch": branch,
                "residual": float(raw),
                "residual_decimal": mp.nstr(raw, 30),
                "term_norm": float(norm),
                "term_norm_decimal": mp.nstr(norm, 30),
                "metric": float(metric),
                "metric_decimal": mp.nstr(metric, 30),
                "invariant_difference_decimal": mp.nstr(invariant_difference, 12),
                "pass": bool(row_pass),
            }
        )
    worst = max(rows, key=lambda item: float(item["metric"]))
    return {"row_count": len(rows), "rows": rows, "worst": worst, "pass": bool(passed)}


def _environment() -> dict[str, object]:
    capture = StringIO()
    with redirect_stdout(capture):
        np.show_config()
    return {
        "python": platform.python_version(),
        "implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "numpy": np.__version__,
        "mpmath": mp.__version__,
        "mpmath_dps": PRECISION_DPS,
        "numpy_config": capture.getvalue(),
    }


def _fixture_guard(
    precision_dps: int,
    refinement_count: int,
    hp_solve_count: int,
    relative_tolerance: float,
    states: tuple[str, ...],
    powers: tuple[int, ...],
    anchor: str,
    driver_labels: tuple[str, ...],
    holdout_labels: tuple[str, ...],
) -> bool:
    expected_driver = tuple(
        [f"{row}[{power}]" for row in v1.DRIVER_ROWS for power in range(-1, 8)]
        + [
            f"initial:{name}[{power}]"
            for name, power, _ in v1._initial_constraints(
                provenance.MODE,
                v1.FrozenInputs().radiation_weights[1],
                v1.FrozenInputs().radiation_weights[0],
            )
        ]
    )
    expected_holdout = tuple(
        f"{row}[{power}]" for row in v1.HOLDOUT_ROWS for power in range(-1, 8)
    )
    return bool(
        precision_dps == PRECISION_DPS
        and refinement_count == REFINEMENT_LIMIT
        and hp_solve_count == HIGH_PRECISION_SOLVE_LIMIT
        and relative_tolerance == provenance.REL_TOL
        and states == tuple(v1.VARS)
        and powers == tuple(range(-1, 8))
        and anchor == "h[1]"
        and driver_labels == expected_driver
        and holdout_labels == expected_holdout
        and len(set(driver_labels)) == len(driver_labels)
        and len(set(holdout_labels)) == len(holdout_labels)
    )


def _prerequisite_hash_guard(observed: str) -> bool:
    return observed.upper() == EXPECTED_KMPC036[1]


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    if max_runtime_seconds != SMOKE_LIMIT_SECONDS:
        raise ValueError("KMPC-037 smoke requires exactly 4.8 seconds")
    _, deadline = _deadline(max_runtime_seconds)
    success = result_dir / "RUN_KMPC_037_P5_3G7_M1_ORDER7_NUMERICAL_REFINEMENT.json"
    failure = result_dir / "RUN_KMPC_037_P5_3G7_M1_ORDER7_NUMERICAL_REFINEMENT_TECHNICAL_FAILURE.json"
    if success.exists() or failure.exists():
        raise FileExistsError("KMPC-037 immutable output already exists")
    inputs = v1.FrozenInputs()
    powers = tuple(range(-1, 8))
    driver_labels = tuple(
        [f"{row}[{power}]" for row in v1.DRIVER_ROWS for power in powers]
        + [
            f"initial:{name}[{power}]"
            for name, power, _ in v1._initial_constraints(
                provenance.MODE, inputs.radiation_weights[1], inputs.radiation_weights[0]
            )
        ]
    )
    holdout_labels = tuple(
        f"{row}[{power}]" for row in v1.HOLDOUT_ROWS for power in powers
    )
    args = (
        PRECISION_DPS,
        REFINEMENT_LIMIT,
        HIGH_PRECISION_SOLVE_LIMIT,
        provenance.REL_TOL,
        tuple(v1.VARS),
        powers,
        "h[1]",
        driver_labels,
        holdout_labels,
    )
    canonical = _fixture_guard(*args)
    negative = {
        "wrong_prerequisite_hash": not _prerequisite_hash_guard("0" * 64),
        "wrong_dps": not _fixture_guard(60, *args[1:]),
        "second_refinement": not _fixture_guard(args[0], 2, *args[2:]),
        "second_hp_solve": not _fixture_guard(args[0], args[1], 2, *args[3:]),
        "changed_threshold": not _fixture_guard(*args[:3], 1.0e-9, *args[4:]),
        "reordered_state": not _fixture_guard(*args[:4], tuple(reversed(v1.VARS)), *args[5:]),
        "missing_power7": not _fixture_guard(*args[:5], powers[:-1], *args[6:]),
        "missing_anchor": not _fixture_guard(*args[:6], "", *args[7:]),
        "missing_driver": not _fixture_guard(*args[:7], driver_labels[:-1], args[8]),
        "duplicate_holdout": not _fixture_guard(*args[:8], holdout_labels[:-1] + (holdout_labels[-2],)),
    }
    with mp.workdps(PRECISION_DPS):
        probe_a = mp.matrix([[1, 0], [0, 1], [1, 1]])
        probe_b = mp.matrix([1, 2, 3])
        probe_x, _ = mp.qr_solve(probe_a, probe_b)
        qr_api_pass = bool(abs(probe_x[0] - 1) < mp.mpf("1e-70") and abs(probe_x[1] - 2) < mp.mpf("1e-70"))
        exact_transfer_pass = _float_to_mpf(0.1) == mp.mpf(0.1)
    deadline()
    passed = bool(canonical and all(negative.values()) and qr_api_pass and exact_transfer_pass)
    if not passed:
        raise RuntimeError("KMPC-037 smoke fixture failed")
    return {
        "run_id": RUN_ID,
        "smoke_pass": True,
        "negative_fixtures": negative,
        "mpmath_qr_api_pass": qr_api_pass,
        "exact_float64_transfer_pass": exact_transfer_pass,
        "environment": _environment(),
    }


def run_audit(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    if max_runtime_seconds != AUDIT_LIMIT_SECONDS:
        raise ValueError("KMPC-037 audit requires exactly 45 seconds")
    started, deadline = _deadline(max_runtime_seconds)
    prerequisite_path = result_dir / EXPECTED_KMPC036[0]
    if not _prerequisite_hash_guard(sha256_file(prerequisite_path)):
        raise RuntimeError("immutable KMPC-036 prerequisite hash mismatch")
    reference = json.loads(prerequisite_path.read_text(encoding="utf-8"))
    reference_state = _state_from_json(reference["M1_order7_state"])
    inputs = v1.FrozenInputs()
    system = provenance._affine_system(provenance.ORDER_AUDIT, inputs, deadline)
    full_matrix = system["driver_matrix"]
    full_constant = system["driver_constant"]
    anchor_index = int(system["anchor_index"])
    anchor_value = float(system["anchor_value"])
    reduced_matrix = np.delete(full_matrix, anchor_index, axis=1)
    right_hand_side = -full_constant - full_matrix[:, anchor_index] * anchor_value
    reference_vector = provenance._vector_from_state(
        reference_state, system["pairs"]
    )
    reference_reduced = np.delete(reference_vector, anchor_index)

    v0_driver = provenance._residual_metrics(
        full_matrix, full_constant, reference_vector, system["driver_labels"]
    )
    v0_holdout = provenance._residual_metrics(
        system["holdout_matrix"],
        system["holdout_constant"],
        reference_vector,
        system["holdout_labels"],
    )
    v0_driver_regression = _row_regression(
        v0_driver, reference["driver_and_initial_full_power"]
    )
    v0_holdout_regression = _row_regression(
        v0_holdout, reference["holdout_full_power"]
    )
    rank = int(np.linalg.matrix_rank(reduced_matrix))
    v0_pass = bool(
        list(full_matrix.shape) == [121, 99]
        and list(reduced_matrix.shape) == [121, 98]
        and rank == 98
        and tuple(system["powers"]) == tuple(range(-1, 8))
        and reference["identity"] == {
            "mode": "CDI", "k_Mpc_inverse": 0.05, "variant": "nominal", "order": 7
        }
        and _state_parity(reference_state)
        and system["anchor_power"] == 1
        and system["pairs"][anchor_index] == ("h", 1)
        and reference["M1_order7_metadata"]["hard_anchor_variable"] == "h[1]"
        and reference["M1_order7_metadata"]["hard_anchor_absolute_difference"] == 0.0
        and v0_driver_regression["pass"]
        and v0_holdout_regression["pass"]
    )
    if not v0_pass:
        return {
            "run_id": RUN_ID,
            "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
            "candidate_interpretation_not_verdict": "REVIEW_KMPC037_REFERENCE_OR_REGRESSION_UNCLOSED",
            "v0_pass": False,
            "v0_driver_regression": v0_driver_regression,
            "v0_holdout_regression": v0_holdout_regression,
            "score_effect": "NONE",
            "release_trigger": "NONE",
            "zenodo_trigger": "NONE",
            "prediction_table_effect": "NONE",
        }

    v1_diagnostics = _float64_diagnostics(
        reduced_matrix, right_hand_side, reference_reduced
    )
    v1_invariants = {
        "driver_and_initial": _residual_invariants(v0_driver),
        "holdout": _residual_invariants(v0_holdout),
    }
    residual = reduced_matrix @ reference_reduced - right_hand_side
    correction, _, correction_rank, correction_singular = np.linalg.lstsq(
        reduced_matrix, -residual, rcond=None
    )
    refined_reduced = reference_reduced + correction
    refined_full = _full_from_reduced(
        refined_reduced, anchor_index, anchor_value, full_matrix.shape[1]
    )
    v2_driver = provenance._residual_metrics(
        full_matrix, full_constant, refined_full, system["driver_labels"]
    )
    v2_holdout = provenance._residual_metrics(
        system["holdout_matrix"],
        system["holdout_constant"],
        refined_full,
        system["holdout_labels"],
    )
    refined_state = _unpack_vector(refined_full, system["pairs"])
    v2_lower = provenance._hybrid_regression(
        reference_state, refined_state, tuple(range(-1, 6))
    )
    correction_max = float(np.max(np.abs(correction)))
    v2_bounds_pass = bool(
        correction_max <= CORRECTION_ABS_MAX
        and int(correction_rank) == 98
        and v2_lower["pass"]
        and refined_full[anchor_index] == anchor_value
        and v2_holdout["pass"]
    )
    deadline()

    with mp.workdps(PRECISION_DPS):
        mp_matrix = mp.matrix(
            [
                [_float_to_mpf(float(value)) for value in row]
                for row in reduced_matrix
            ]
        )
        mp_rhs = mp.matrix([_float_to_mpf(float(value)) for value in right_hand_side])
        mp_solution, mp_qr_residual = mp.qr_solve(mp_matrix, mp_rhs)
        hp_reduced = [mp_solution[index] for index in range(len(mp_solution))]
        hp_full: list[mp.mpf] = []
        reduced_index = 0
        for column in range(full_matrix.shape[1]):
            if column == anchor_index:
                hp_full.append(_float_to_mpf(anchor_value))
            else:
                hp_full.append(hp_reduced[reduced_index])
                reduced_index += 1
        v3_driver = _mp_residual_metrics(
            full_matrix, full_constant, hp_full, system["driver_labels"]
        )
        v3_holdout = _mp_residual_metrics(
            system["holdout_matrix"],
            system["holdout_constant"],
            hp_full,
            system["holdout_labels"],
        )
        hp_difference_max = max(
            abs(hp_reduced[index] - _float_to_mpf(float(reference_reduced[index])))
            for index in range(reference_reduced.size)
        )
        hp_qr_residual_decimal = mp.nstr(mp_qr_residual, 30)
        hp_difference_max_decimal = mp.nstr(hp_difference_max, 30)
        hp_projected = np.asarray([float(value) for value in hp_full], dtype=float)
    deadline()

    v3_projected_driver = provenance._residual_metrics(
        full_matrix, full_constant, hp_projected, system["driver_labels"]
    )
    v3_projected_holdout = provenance._residual_metrics(
        system["holdout_matrix"],
        system["holdout_constant"],
        hp_projected,
        system["holdout_labels"],
    )
    hp_state = _unpack_vector(hp_projected, system["pairs"])
    v3_lower = provenance._hybrid_regression(
        reference_state, hp_state, tuple(range(-1, 6))
    )
    v3_bounds_pass = bool(
        float(hp_difference_max) <= CORRECTION_ABS_MAX
        and v3_lower["pass"]
        and hp_projected[anchor_index] == anchor_value
        and v3_holdout["pass"]
    )

    if not v2_bounds_pass or not v3_bounds_pass:
        candidate = "REVIEW_KMPC037_REFINEMENT_OUT_OF_BOUNDS"
    elif v2_driver["pass"] and v2_holdout["pass"] and v3_driver["pass"] and v3_holdout["pass"]:
        candidate = "PASS_M1_ORDER7_FLOAT64_SOLVER_FLOOR_CANDIDATE_ONLY"
    elif v3_driver["pass"] and v3_holdout["pass"]:
        candidate = "PASS_M1_ORDER7_FLOAT64_ROUNDING_FLOOR_CANDIDATE_ONLY"
    else:
        candidate = "REVIEW_M1_ORDER7_SAME_MATRIX_BOUNDARY_UNCLOSED"

    payload = {
        "test": "A2-K4 P5.3g7 GLOBAL_C1 M1_ORDER7_NUMERICAL_REFINEMENT_AND_BOUNDARY_CLOSURE_AUDIT",
        "run_id": RUN_ID,
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "candidate_interpretation_not_verdict": candidate,
        "identity": reference["identity"],
        "scope": {
            "included": "same frozen KMPC-036 float64 matrix: V0 regression, V1 diagnostics, one V2 refinement, one V3 80-dps QR solve",
            "excluded": "native high-precision rebuild, CDI support step 3, [0,9], new equations/parameters, BI/NID/NIV, other k/variants, S-M, ODE, G8/G9, CLASS/CMB/BBN/S8/H0",
        },
        "immutable_prerequisite": {"file": EXPECTED_KMPC036[0], "sha256": EXPECTED_KMPC036[1]},
        "dimensions": {"full": list(full_matrix.shape), "reduced": list(reduced_matrix.shape), "rank": rank},
        "v0": {
            "pass": v0_pass,
            "driver_regression": v0_driver_regression,
            "holdout_regression": v0_holdout_regression,
            "reference_open_driver_rows": [row["label"] for row in v0_driver["rows"] if not row["pass"]],
        },
        "v1_float64_diagnostics": {
            **v1_diagnostics,
            "residual_metric_invariants": v1_invariants,
        },
        "v2_single_bounded_refinement": {
            "refinement_count": 1,
            "correction_max_abs": correction_max,
            "correction_rank": int(correction_rank),
            "correction_singular_max": float(correction_singular[0]),
            "correction_singular_min_resolved": float(correction_singular[97]),
            "bounds_pass": v2_bounds_pass,
            "lower_regression": v2_lower,
            "driver_and_initial": v2_driver,
            "holdout": v2_holdout,
            "diagnostics_after": _float64_diagnostics(reduced_matrix, right_hand_side, refined_reduced),
        },
        "v3_same_float64_matrix_high_precision": {
            "high_precision_solve_count": 1,
            "method": "mpmath.qr_solve overdetermined least squares",
            "precision_dps": PRECISION_DPS,
            "float64_transfer": "exact float.as_integer_ratio",
            "qr_residual_decimal": hp_qr_residual_decimal,
            "solution_difference_max_decimal": hp_difference_max_decimal,
            "bounds_pass": v3_bounds_pass,
            "lower_regression_after_float64_projection": v3_lower,
            "driver_and_initial_high_precision": v3_driver,
            "holdout_high_precision": v3_holdout,
            "driver_and_initial_after_float64_projection": v3_projected_driver,
            "holdout_after_float64_projection": v3_projected_holdout,
        },
        "thresholds": {
            "residual_relative": provenance.REL_TOL,
            "residual_absolute": provenance.ABS_TOL,
            "regression_relative": provenance.REGRESSION_REL_TOL,
            "regression_absolute": provenance.REGRESSION_ABS_TOL,
            "anchor_absolute": provenance.ANCHOR_TOL,
            "correction_absolute_max": CORRECTION_ABS_MAX,
        },
        "operation_counts": {"refinements": 1, "high_precision_solves": 1, "native_rebuilds": 0},
        "source_hashes": source_hashes(),
        "environment": _environment(),
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "score_effect": "NONE",
        "release_trigger": "NONE",
        "zenodo_trigger": "NONE",
        "prediction_table_effect": "NONE",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }
    if not provenance._all_finite(payload):
        raise FloatingPointError("non-finite value in KMPC-037 payload")
    deadline()
    return payload
