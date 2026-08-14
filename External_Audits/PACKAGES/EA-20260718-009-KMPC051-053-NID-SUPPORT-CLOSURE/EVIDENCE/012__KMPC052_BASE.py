"""KMPC-052 same-matrix numerical boundary audit for NID depth-7 M3.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
"""

from __future__ import annotations

import json
import math
import numbers
from pathlib import Path
import time
from typing import Callable, Mapping

import mpmath as mpmath_module
import numpy as np

from . import m1_order7_numerical_refinement as numeric
from . import m1_order7_numerical_refinement_v2_householder as householder
from . import m1_order7_numerical_refinement_v3_context_owner as context_owner
from . import nid_m1_depth_5_7 as k51


k50 = k51.k50
v1 = k51.v1
physics = k51.physics
RUN_ID = "KMPC-052"
PRECISION_DPS = 80
CORRECTION_ABS_MAX = 1.0e-14
COMMON_TOL = 1.0e-8
SMOKE_LIMIT_SECONDS = 12.0
AUDIT_LIMIT_SECONDS = 45.0
KMPC051 = (
    "RUN_KMPC_051_P5_3G7_NID_M1_DEPTH_5_7.json",
    "AF088030BA709F08D40D825B9477C9A84BA330705CDDFB1C12C52B0DD3FC1E5E",
)


def source_hashes() -> dict[str, str]:
    here = Path(__file__).resolve().parent
    hashes = dict(k51.source_hashes())
    for name in (
        "m1_order7_numerical_refinement.py",
        "m1_order7_numerical_refinement_v2_householder.py",
        "m1_order7_numerical_refinement_v3_context_owner.py",
        "nid_depth7_numerical_boundary.py",
    ):
        hashes[name] = v1.sha256_file(here / name)
    return hashes


def _load_prerequisite(result_dir: Path) -> tuple[dict[str, object], str]:
    path = result_dir / KMPC051[0]
    observed = v1.sha256_file(path)
    if observed != KMPC051[1]:
        raise RuntimeError("immutable KMPC-051 prerequisite hash mismatch")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not (
        payload.get("baseline_pass") is True
        and payload.get("M1_depth7_pass") is True
        and payload.get("common_pass") is True
        and payload.get("depth7_core_pass") is False
    ):
        raise RuntimeError("immutable KMPC-051 state mismatch")
    return payload, observed


def _deadline(limit: float) -> tuple[float, Callable[[], None]]:
    if limit not in (SMOKE_LIMIT_SECONDS, AUDIT_LIMIT_SECONDS):
        raise ValueError("KMPC-052 runtime must be exactly 12 or 45 seconds")
    started = time.monotonic()

    def check() -> None:
        if time.monotonic() - started > limit:
            raise TimeoutError("KMPC-052 deadline exceeded")

    return started, check


def _all_finite(value: object) -> bool:
    if isinstance(value, Mapping):
        return all(_all_finite(item) for item in value.values())
    if isinstance(value, (list, tuple)):
        return all(_all_finite(item) for item in value)
    if isinstance(value, np.ndarray):
        return bool(np.all(np.isfinite(value)))
    if isinstance(value, np.generic):
        return _all_finite(value.item())
    if isinstance(value, numbers.Real):
        return math.isfinite(float(value))
    return True


def _build_system(deadline: Callable[[], None]) -> dict[str, object]:
    inputs = physics._variant_inputs(v1.VARIANT)
    standard, m1meta = k51._standard_depth(7, inputs, deadline)
    solved, captured = k50._capture_support(inputs, standard, deadline)
    return {
        "inputs": inputs,
        "standard": standard,
        "M1_metadata": m1meta,
        "solved": solved,
        "captured": captured,
        "matrix": k51._matrix_summary(captured),
    }


def _float_rows(
    matrix: np.ndarray,
    constant: np.ndarray,
    vector: np.ndarray,
    labels: tuple[str, ...],
    relative_tolerance: float,
) -> dict[str, object]:
    residual = matrix @ vector + constant
    scale = np.abs(constant) + np.sum(
        np.abs(matrix * vector[np.newaxis, :]), axis=1
    )
    rows: list[dict[str, object]] = []
    passed = True
    for index, label in enumerate(labels):
        if scale[index] > physics.ABS_FALLBACK_NORM:
            branch = "relative"
            metric = abs(residual[index]) / scale[index]
            row_pass = metric <= relative_tolerance
        else:
            branch = "absolute"
            metric = abs(residual[index])
            row_pass = metric <= physics.ABS_FALLBACK_TOL
        passed = passed and bool(row_pass)
        rows.append(
            {
                "label": label,
                "branch": branch,
                "residual": float(residual[index]),
                "term_norm": float(scale[index]),
                "metric": float(metric),
                "pass": bool(row_pass),
            }
        )
    worst = max(rows, key=lambda item: float(item["metric"]))
    failed = [row["label"] for row in rows if not row["pass"]]
    return {
        "row_count": len(rows),
        "failed_count": len(failed),
        "failed_rows": failed,
        "worst": worst,
        "pass": bool(passed),
    }


def _mp_rows(
    matrix: np.ndarray,
    constant: np.ndarray,
    vector: list[mpmath_module.mpf],
    labels: tuple[str, ...],
    relative_tolerance: float,
) -> dict[str, object]:
    ctx = mpmath_module.mp
    relative_limit = ctx.mpf(str(relative_tolerance))
    norm_branch = ctx.mpf(str(physics.ABS_FALLBACK_NORM))
    absolute_limit = ctx.mpf(str(physics.ABS_FALLBACK_TOL))
    rows: list[dict[str, object]] = []
    passed = True
    for row_index, label in enumerate(labels):
        raw = numeric._float_to_mpf(float(constant[row_index]))
        norm = abs(raw)
        for column, value in enumerate(vector):
            term = numeric._float_to_mpf(float(matrix[row_index, column])) * value
            raw += term
            norm += abs(term)
        if norm > norm_branch:
            branch = "relative"
            metric = abs(raw) / norm
            row_pass = metric <= relative_limit
        else:
            branch = "absolute"
            metric = abs(raw)
            row_pass = metric <= absolute_limit
        passed = passed and bool(row_pass)
        rows.append(
            {
                "label": label,
                "branch": branch,
                "residual_decimal": ctx.nstr(raw, 30),
                "term_norm_decimal": ctx.nstr(norm, 30),
                "metric": float(metric),
                "metric_decimal": ctx.nstr(metric, 30),
                "pass": bool(row_pass),
            }
        )
    worst = max(rows, key=lambda item: float(item["metric"]))
    failed = [row["label"] for row in rows if not row["pass"]]
    return {
        "row_count": len(rows),
        "failed_count": len(failed),
        "failed_rows": failed,
        "worst": worst,
        "pass": bool(passed),
    }


def _equilibrated_correction(
    matrix: np.ndarray, constant: np.ndarray, vector: np.ndarray
) -> tuple[np.ndarray, dict[str, object]]:
    residual = matrix @ vector + constant
    row_scale = np.maximum(
        np.maximum(np.max(np.abs(matrix), axis=1), np.abs(constant)), 1.0e-300
    )
    row_matrix = matrix / row_scale[:, np.newaxis]
    column_scale = np.maximum(np.max(np.abs(row_matrix), axis=0), 1.0e-300)
    equilibrated = row_matrix / column_scale[np.newaxis, :]
    y, _, rank, singular = np.linalg.lstsq(
        equilibrated, -residual / row_scale, rcond=physics.RCOND
    )
    correction = y / column_scale
    corrected = vector + correction
    maximum = float(np.max(np.abs(correction)))
    return corrected, {
        "method": "one equilibrated same-matrix float64 residual correction",
        "correction_count": 1,
        "rank": int(rank),
        "correction_max_abs": maximum,
        "correction_relative_to_max_solution_or_one": maximum
        / max(float(np.max(np.abs(vector))), 1.0),
        "singular_max": float(singular[0]),
        "singular_min": float(singular[-1]),
    }


def _vector_state(vector: np.ndarray) -> dict[str, dict[int, float]]:
    names = tuple(physics.contract.AUTHORITATIVE_STATE)
    exponents = tuple(range(0, 8))
    return {
        name: {
            power: float(vector[name_index * len(exponents) + power_index])
            for power_index, power in enumerate(exponents)
        }
        for name_index, name in enumerate(names)
    }


def _high_precision_solve(
    matrix: np.ndarray,
    constant: np.ndarray,
    deadline: Callable[[], None],
) -> tuple[list[mpmath_module.mpf], dict[str, object]]:
    ctx = mpmath_module.mp
    original_function = getattr(ctx.householder, "__func__", ctx.householder)
    with ctx.workdps(PRECISION_DPS):
        mp_matrix = ctx.matrix(
            [
                [numeric._float_to_mpf(float(value)) for value in row]
                for row in matrix
            ]
        )
        mp_rhs = ctx.matrix(
            [numeric._float_to_mpf(float(-value)) for value in constant]
        )
        with context_owner._context_owner_bridge():
            with householder._householder_overlay():
                solution, qr_residual = ctx.qr_solve(mp_matrix, mp_rhs)
        values = [solution[index] for index in range(len(solution))]
        qr_decimal = ctx.nstr(qr_residual, 30)
    restored_function = getattr(ctx.householder, "__func__", ctx.householder)
    deadline()
    return values, {
        "precision_dps": PRECISION_DPS,
        "float64_transfer": "exact float.as_integer_ratio",
        "high_precision_solve_count": 1,
        "householder_overlay_count": 1,
        "context_owner_bridge_count": 1,
        "qr_residual_decimal": qr_decimal,
        "householder_owner_restored": restored_function is original_function,
    }


def _reference_parity(
    immutable: Mapping[str, object], built: Mapping[str, object]
) -> dict[str, object]:
    matrix = built["matrix"]
    frozen = immutable["depth7_matrix"]
    captured = built["captured"]
    vector = captured["solution"]
    driver = _float_rows(
        captured["driver_matrix"],
        captured["driver_constant"],
        vector,
        captured["driver_labels"],
        physics.DRIVER_TOL,
    )
    holdout = _float_rows(
        captured["holdout_matrix"],
        captured["holdout_constant"],
        vector,
        captured["holdout_labels"],
        physics.HOLDOUT_TOL,
    )
    hash_match = all(
        matrix[key] == frozen[key]
        for key in (
            "driver_matrix_sha256_float64_C",
            "driver_constant_sha256_float64_C",
            "holdout_matrix_sha256_float64_C",
            "holdout_constant_sha256_float64_C",
        )
    )
    passed = bool(
        hash_match
        and matrix["pass"]
        and not driver["pass"]
        and driver["worst"]["label"] == "fuel_Euler[7]"
        and holdout["pass"]
        and built["M1_metadata"]["rank_count_anchor_pass"]
    )
    return {
        "matrix_hash_match_KMPC051": hash_match,
        "driver": driver,
        "holdout": holdout,
        "pass": passed,
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    if max_runtime_seconds != SMOKE_LIMIT_SECONDS:
        raise ValueError("KMPC-052 smoke requires exactly 12 seconds")
    started, deadline = _deadline(max_runtime_seconds)
    immutable, observed = _load_prerequisite(result_dir)
    built = _build_system(deadline)
    parity = _reference_parity(immutable, built)
    hp_solution, hp_meta = _high_precision_solve(
        built["captured"]["driver_matrix"],
        built["captured"]["driver_constant"],
        deadline,
    )
    hp_driver = _mp_rows(
        built["captured"]["driver_matrix"],
        built["captured"]["driver_constant"],
        hp_solution,
        built["captured"]["driver_labels"],
        physics.DRIVER_TOL,
    )
    checks = {
        "immutable_KMPC051_hash": observed == KMPC051[1],
        "exact_matrix_V0_parity": parity["pass"],
        "exact_matrix_80dps_driver": hp_driver["pass"],
        "householder_owner_restored": hp_meta["householder_owner_restored"],
        "precision_exact": hp_meta["precision_dps"] == PRECISION_DPS,
        "operation_counts_exact": hp_meta["high_precision_solve_count"] == 1
        and hp_meta["householder_overlay_count"] == 1
        and hp_meta["context_owner_bridge_count"] == 1,
    }
    deadline()
    return {
        "run_id": RUN_ID,
        "mode": "EXACT_MATRIX_LIFECYCLE_SMOKE_NO_RESULT_FILE",
        "checks": checks,
        "high_precision_lifecycle": hp_meta,
        "runtime_seconds": time.monotonic() - started,
        "passed": all(checks.values()),
    }


def run_audit(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    if max_runtime_seconds != AUDIT_LIMIT_SECONDS:
        raise ValueError("KMPC-052 audit requires exactly 45 seconds")
    started, deadline = _deadline(max_runtime_seconds)
    immutable, immutable_hash = _load_prerequisite(result_dir)
    built = _build_system(deadline)
    captured = built["captured"]
    reference = captured["solution"]
    parity = _reference_parity(immutable, built)
    rhs = -captured["driver_constant"]
    v1_invariants = numeric._float64_diagnostics(
        captured["driver_matrix"], rhs, reference
    )
    refined, refinement = _equilibrated_correction(
        captured["driver_matrix"], captured["driver_constant"], reference
    )
    v2_driver = _float_rows(
        captured["driver_matrix"],
        captured["driver_constant"],
        refined,
        captured["driver_labels"],
        physics.DRIVER_TOL,
    )
    v2_holdout = _float_rows(
        captured["holdout_matrix"],
        captured["holdout_constant"],
        refined,
        captured["holdout_labels"],
        physics.HOLDOUT_TOL,
    )
    v2_common = k51._regression(
        k51._restrict(_vector_state(reference), 0, 5),
        k51._restrict(_vector_state(refined), 0, 5),
    )
    hp_solution, hp_meta = _high_precision_solve(
        captured["driver_matrix"], captured["driver_constant"], deadline
    )
    v3_driver = _mp_rows(
        captured["driver_matrix"],
        captured["driver_constant"],
        hp_solution,
        captured["driver_labels"],
        physics.DRIVER_TOL,
    )
    v3_holdout = _mp_rows(
        captured["holdout_matrix"],
        captured["holdout_constant"],
        hp_solution,
        captured["holdout_labels"],
        physics.HOLDOUT_TOL,
    )
    hp_projected = np.asarray([float(value) for value in hp_solution], dtype=float)
    projected_driver = _float_rows(
        captured["driver_matrix"],
        captured["driver_constant"],
        hp_projected,
        captured["driver_labels"],
        physics.DRIVER_TOL,
    )
    projected_holdout = _float_rows(
        captured["holdout_matrix"],
        captured["holdout_constant"],
        hp_projected,
        captured["holdout_labels"],
        physics.HOLDOUT_TOL,
    )
    v3_difference = float(np.max(np.abs(hp_projected - reference)))
    v3_common = k51._regression(
        k51._restrict(_vector_state(reference), 0, 5),
        k51._restrict(_vector_state(hp_projected), 0, 5),
    )
    v2_pass = bool(
        refinement["rank"] == 104
        and refinement["correction_max_abs"] <= CORRECTION_ABS_MAX
        and v2_driver["pass"]
        and v2_holdout["pass"]
        and v2_common["pass_frozen_limit"]
    )
    v3_pass = bool(
        hp_meta["householder_owner_restored"]
        and v3_difference <= CORRECTION_ABS_MAX
        and v3_driver["pass"]
        and v3_holdout["pass"]
        and projected_driver["pass"]
        and projected_holdout["pass"]
        and v3_common["pass_frozen_limit"]
    )
    finite = _all_finite(
        {
            "parity": parity,
            "v1": v1_invariants,
            "refinement": refinement,
            "v2_driver": v2_driver,
            "v2_holdout": v2_holdout,
            "v3_driver": v3_driver,
            "v3_holdout": v3_holdout,
        }
    )
    if not parity["pass"] or not finite:
        candidate = "REVIEW_NID_DEPTH7_REFERENCE_UNCLOSED"
    elif not v2_pass and refinement["correction_max_abs"] > CORRECTION_ABS_MAX:
        candidate = "REVIEW_NID_DEPTH7_REFINEMENT_OUT_OF_BOUNDS"
    elif v2_pass and v3_pass:
        candidate = "PASS_NID_DEPTH7_FLOAT64_SOLVER_FLOOR_CANDIDATE_ONLY"
    elif v3_pass:
        candidate = "PASS_NID_DEPTH7_FLOAT64_ROUNDING_FLOOR_CANDIDATE_ONLY"
    else:
        candidate = "REVIEW_NID_DEPTH7_SAME_MATRIX_BOUNDARY_UNCLOSED"
    deadline()
    return {
        "test": "A2-K4 P5.3g7 KMPC-052 NID depth-7 same-matrix numerical boundary",
        "run_id": RUN_ID,
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "candidate_interpretation_not_verdict": candidate,
        "authorship": {
            "theory_author": "Martin Jambor",
            "script_creator": "Codex (OpenAI)",
        },
        "identity": {
            "mode": v1.MODE,
            "k_Mpc_inverse": v1.K_MPC,
            "variant": v1.VARIANT,
            "M1_depth": 7,
            "M3_support": list(v1.SUPPORT),
        },
        "immutable_KMPC051": {"file": KMPC051[0], "sha256": immutable_hash},
        "scope": {
            "included": "same depth-7 M1 plus NID [0,7] float64 matrix: V0, V1, one V2 correction, one V3 80-dps QR",
            "excluded": "native rebuild, second correction/HP solve, equation/support/threshold changes, [0,9], NIV, other k/variants, S-M, ODE, G8/G9",
        },
        "V0_reference_parity": parity,
        "V1_float64_invariants": v1_invariants,
        "V2_single_bounded_refinement": {
            **refinement,
            "driver": v2_driver,
            "holdout": v2_holdout,
            "common_0_5": v2_common,
            "pass": v2_pass,
        },
        "V3_single_80dps_same_matrix_QR": {
            **hp_meta,
            "driver": v3_driver,
            "holdout": v3_holdout,
            "difference_max_abs_from_V0": v3_difference,
            "common_0_5": v3_common,
            "float64_projection_driver": projected_driver,
            "float64_projection_holdout": projected_holdout,
            "pass": v3_pass,
        },
        "operation_counts": {
            "float64_refinements": 1,
            "high_precision_solves": 1,
            "householder_overlays": 1,
            "context_owner_bridges": 1,
            "native_rebuilds": 0,
        },
        "finite_pass": finite,
        "source_hashes": source_hashes(),
        "thresholds": {
            "driver_relative": physics.DRIVER_TOL,
            "holdout_relative": physics.HOLDOUT_TOL,
            "absolute_fallback_norm": physics.ABS_FALLBACK_NORM,
            "absolute_fallback": physics.ABS_FALLBACK_TOL,
            "correction_absolute_max": CORRECTION_ABS_MAX,
            "common_relative": COMMON_TOL,
            "precision_dps": PRECISION_DPS,
        },
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "score_effect": "NONE",
        "release_trigger": "NONE",
        "prediction_table_effect": "NONE",
        "zenodo_trigger": "NONE",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }
