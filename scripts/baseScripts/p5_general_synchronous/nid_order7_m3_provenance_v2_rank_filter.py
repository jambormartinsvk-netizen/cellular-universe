"""Rank-filtered successor for the KMPC-049 NID provenance capture.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Only the shared-solver capture routing changes; physics and thresholds do not.
"""

from __future__ import annotations

import json
from pathlib import Path
import time
from typing import Callable, Mapping

import numpy as np

from . import nid_order7_m3_provenance as v1


RUN_ID = "KMPC-050"
EXPECTED_COUNT = v1.EXPECTED_COUNT
KMPC049_FAILURE = (
    "RUN_KMPC_049_P5_3G7_NID_ORDER7_M3_PROVENANCE_TECHNICAL_FAILURE.json",
    "EB5EA48145CB52C95826A3111ABBD2DF0C05AC531B8471DF704E2032FA0B6E35",
)


def source_hashes() -> dict[str, str]:
    here = Path(__file__).resolve().parent
    hashes = dict(v1.source_hashes())
    hashes["nid_order7_m3_provenance_v2_rank_filter.py"] = v1.sha256_file(
        here / "nid_order7_m3_provenance_v2_rank_filter.py"
    )
    return hashes


def _load_failure_prerequisite(result_dir: Path) -> str:
    path = result_dir / KMPC049_FAILURE[0]
    observed = v1.sha256_file(path)
    if observed != KMPC049_FAILURE[1]:
        raise RuntimeError("immutable KMPC-049 failure prerequisite hash mismatch")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("execution_status") != "TECHNICAL_FAILURE_NO_PHYSICS_VERDICT":
        raise RuntimeError("KMPC-049 failure prerequisite status mismatch")
    return observed


def _target_signature(matrix: np.ndarray, expected_rank: int) -> bool:
    """Return whether a shared solver call is the frozen 104x104 M3 target."""
    shape = tuple(np.shape(matrix))
    if expected_rank != EXPECTED_COUNT:
        return False
    if shape != (EXPECTED_COUNT, EXPECTED_COUNT):
        raise RuntimeError("KMPC-050 target rank arrived with a non-104x104 shape")
    return True


def _capture_support(
    inputs: object,
    standard: Mapping[str, Mapping[int, float]],
    deadline: Callable[[], None],
) -> tuple[dict[str, object], dict[str, object]]:
    physics = v1.physics
    original_solve = physics._solve_equilibrated
    original_holdout = physics._holdout_metrics
    captured: dict[str, object] = {}
    counts = {"passthrough": 0, "target": 0, "holdout": 0}

    def solve_capture(
        matrix: np.ndarray,
        constant: np.ndarray,
        expected_rank: int,
        row_labels: list[str] | None = None,
        deadline: Callable[[], None] | None = None,
    ) -> tuple[np.ndarray, dict[str, object]]:
        if not _target_signature(matrix, expected_rank):
            counts["passthrough"] += 1
            return original_solve(
                matrix, constant, expected_rank, row_labels, deadline
            )
        counts["target"] += 1
        if counts["target"] != 1:
            raise RuntimeError("KMPC-050 rejected a second 104x104 target solve")
        solution, diagnostics = original_solve(
            matrix, constant, expected_rank, row_labels, deadline
        )
        captured.update(
            {
                "driver_matrix": np.array(matrix, copy=True),
                "driver_constant": np.array(constant, copy=True),
                "driver_labels": tuple(row_labels or ()),
                "solution": np.array(solution, copy=True),
                "driver_diagnostics": dict(diagnostics),
                "expected_rank": int(expected_rank),
            }
        )
        return solution, diagnostics

    def holdout_capture(
        matrix: np.ndarray,
        constant: np.ndarray,
        solution: np.ndarray,
        labels: list[str] | None = None,
    ) -> dict[str, object]:
        counts["holdout"] += 1
        if counts["holdout"] != 1:
            raise RuntimeError("KMPC-050 rejected a second M3 holdout call")
        metrics = original_holdout(matrix, constant, solution, labels)
        captured.update(
            {
                "holdout_matrix": np.array(matrix, copy=True),
                "holdout_constant": np.array(constant, copy=True),
                "holdout_labels": tuple(labels or ()),
                "holdout_diagnostics": dict(metrics),
            }
        )
        return metrics

    try:
        physics._solve_equilibrated = solve_capture
        physics._holdout_metrics = holdout_capture
        solved = v1.step2._solve_support(v1.SUPPORT, inputs, standard, deadline)
    finally:
        physics._solve_equilibrated = original_solve
        physics._holdout_metrics = original_holdout
    captured["capture_counts"] = counts
    captured["owners_restored"] = bool(
        physics._solve_equilibrated is original_solve
        and physics._holdout_metrics is original_holdout
    )
    return solved, captured


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    _, deadline = v1.make_deadline(max_runtime_seconds)
    failure_hash = _load_failure_prerequisite(result_dir)
    inherited = v1.run_smoke(max_runtime_seconds, result_dir)
    wrong_shape_rejected = False
    try:
        _target_signature(np.zeros((2, 2)), EXPECTED_COUNT)
    except RuntimeError:
        wrong_shape_rejected = True
    checks = {
        "inherited_KMPC049_smoke": bool(inherited["passed"]),
        "immutable_KMPC049_failure_hash": failure_hash == KMPC049_FAILURE[1],
        "synthetic_2x2_passthrough": not _target_signature(np.zeros((2, 2)), 2),
        "synthetic_104x104_target": _target_signature(
            np.zeros((EXPECTED_COUNT, EXPECTED_COUNT)), EXPECTED_COUNT
        ),
        "target_rank_wrong_shape_rejected": wrong_shape_rejected,
        "exception_owner_restore": bool(
            inherited["owner"]["restored_after_exception"]
        ),
    }
    deadline()
    return {
        "run_id": RUN_ID,
        "mode": "SMOKE_NO_RESULT_FILE",
        "inherited": inherited,
        "checks": checks,
        "passed": all(checks.values()),
    }


def run_audit(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    started, deadline = v1.make_deadline(max_runtime_seconds)
    failure_hash = _load_failure_prerequisite(result_dir)
    immutable, immutable_hash = v1._load_prerequisite(result_dir)
    physics = v1.physics
    inputs = physics._variant_inputs(v1.VARIANT)
    standard, standard_meta = physics._standard_state(
        v1.MODE, v1.K_MPC, inputs, deadline
    )
    solved, captured = _capture_support(inputs, standard, deadline)
    matrix = captured["driver_matrix"]
    constant = captured["driver_constant"]
    labels = captured["driver_labels"]
    solution = captured["solution"]
    holdout_matrix = captured["holdout_matrix"]
    holdout_constant = captured["holdout_constant"]
    holdout_labels = captured["holdout_labels"]
    immutable_solved = immutable["solved_supports"]["07"]
    regression = {
        "F0": v1.regression_tools._regression_metric(
            v1.regression_tools._restore_series(immutable_solved["fuel"]["state"]),
            solved["fuel"]["state"],
        ),
        "M3": v1.regression_tools._regression_metric(
            v1.regression_tools._restore_series(
                immutable_solved["m3"]["fractional_state"]
            ),
            solved["m3"]["fractional_state"],
        ),
    }
    regression_pass = all(row["pass"] for row in regression.values())
    raw_singular = np.linalg.svd(matrix, compute_uv=False)
    row_scale = np.maximum(
        np.maximum(np.max(np.abs(matrix), axis=1), np.abs(constant)), 1.0e-300
    )
    row_matrix = matrix / row_scale[:, np.newaxis]
    column_scale = np.maximum(np.max(np.abs(row_matrix), axis=0), 1.0e-300)
    equilibrated = row_matrix / column_scale[np.newaxis, :]
    eq_singular = np.linalg.svd(equilibrated, compute_uv=False)
    matrix_guard = {
        "driver_shape": list(matrix.shape),
        "holdout_shape": list(holdout_matrix.shape),
        "driver_labels": len(labels),
        "holdout_labels": len(holdout_labels),
        "expected_rank": captured["expected_rank"],
        "capture_counts": captured["capture_counts"],
        "owners_restored": captured["owners_restored"],
        "raw_rank_rcond": int(
            np.sum(raw_singular > physics.RCOND * raw_singular[0])
        ),
        "equilibrated_rank_rcond": int(
            np.sum(eq_singular > physics.RCOND * eq_singular[0])
        ),
        "raw_singular_ratio": float(raw_singular[-1] / raw_singular[0]),
        "equilibrated_singular_ratio": float(eq_singular[-1] / eq_singular[0]),
        "driver_matrix_sha256_float64_C": v1._array_hash(matrix),
        "driver_constant_sha256_float64_C": v1._array_hash(constant),
        "holdout_matrix_sha256_float64_C": v1._array_hash(holdout_matrix),
        "holdout_constant_sha256_float64_C": v1._array_hash(holdout_constant),
    }
    matrix_guard["pass"] = bool(
        matrix.shape == (104, 104)
        and holdout_matrix.shape == (16, 104)
        and len(labels) == 104
        and len(holdout_labels) == 16
        and captured["expected_rank"] == 104
        and matrix_guard["raw_rank_rcond"] == 104
        and matrix_guard["equilibrated_rank_rcond"] == 104
        and captured["capture_counts"]
        == {"passthrough": 1, "target": 1, "holdout": 1}
        and captured["owners_restored"]
    )
    driver7 = v1._row_details(
        matrix, constant, solution, labels, "[7]", physics.DRIVER_TOL
    )
    holdout7 = v1._row_details(
        holdout_matrix,
        holdout_constant,
        solution,
        holdout_labels,
        "[7]",
        physics.HOLDOUT_TOL,
    )
    correction = v1._correction_diagnostic(
        matrix,
        constant,
        solution,
        labels,
        holdout_matrix,
        holdout_constant,
        holdout_labels,
    )
    rfs = v1.nid1._combined_rfs_guard(standard, inputs)
    finite = v1._all_finite(
        {
            "solved": solved,
            "matrix_guard": matrix_guard,
            "driver7": driver7,
            "holdout7": holdout7,
            "correction": correction,
        }
    )
    provenance_pass = bool(
        regression_pass
        and matrix_guard["pass"]
        and standard_meta["pass"]
        and rfs["pass"]
        and finite
    )
    if not provenance_pass:
        candidate = "REVIEW_NID_ORDER7_PROVENANCE_OR_FORMULA_DRIFT"
    elif not correction["pass_numerical_boundary_pattern"]:
        candidate = "REVIEW_NID_ORDER7_NONNUMERICAL_CORE_UNCLOSED"
    else:
        candidate = (
            "PASS_NID_ORDER7_PROVENANCE_NUMERICAL_BOUNDARY_CANDIDATE_ONLY"
        )
    deadline()
    return {
        "test": "A2-K4 P5.3g7 KMPC-050 NID order-7 M3 provenance",
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
            "support": list(v1.SUPPORT),
        },
        "immutable_prerequisites": {
            "KMPC048": {"file": v1.KMPC048[0], "sha256": immutable_hash},
            "KMPC049_failure": {
                "file": KMPC049_FAILURE[0],
                "sha256": failure_hash,
            },
        },
        "scope": {
            "included": "same NID [0,7] M3 matrix capture with rank-filtered shared-solver routing",
            "excluded": "new equations/support/thresholds, corrected state publication, [0,9], NIV, other k/variants, S-M, ODE, G8/G9",
        },
        "M1_standard_metadata": standard_meta,
        "combined_R_fs_guard": rfs,
        "immutable_support07_regression": regression,
        "regression_pass": regression_pass,
        "matrix_provenance_guard": matrix_guard,
        "driver_order7_rows": driver7,
        "holdout_order7_rows": holdout7,
        "same_matrix_correction_diagnostic": correction,
        "original_solve_diagnostics": solved["m3"]["diagnostics"],
        "provenance_pass": provenance_pass,
        "finite_pass": finite,
        "source_hashes": source_hashes(),
        "thresholds": {
            "driver_relative": physics.DRIVER_TOL,
            "holdout_relative": physics.HOLDOUT_TOL,
            "absolute_fallback_norm": physics.ABS_FALLBACK_NORM,
            "absolute_fallback": physics.ABS_FALLBACK_TOL,
            "correction_abs_max": v1.CORRECTION_ABS_MAX,
            "correction_rel_max": v1.CORRECTION_REL_MAX,
        },
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "score_effect": "NONE",
        "release_trigger": "NONE",
        "prediction_table_effect": "NONE",
        "zenodo_trigger": "NONE",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }
