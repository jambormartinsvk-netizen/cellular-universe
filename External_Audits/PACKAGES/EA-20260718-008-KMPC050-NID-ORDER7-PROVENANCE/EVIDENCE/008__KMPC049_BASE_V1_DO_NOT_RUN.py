"""Capture-only NID M3 order-7 provenance audit for KMPC-049.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
No equation, support, threshold, or published state is changed.
"""

from __future__ import annotations

import hashlib
import json
import math
import numbers
from pathlib import Path
import time
from typing import Callable, Mapping

import numpy as np

from . import cdi_support_ladder as regression_tools
from . import full_ra_m3_seed as physics
from . import nid_c1_coverage as nid1
from . import nid_support_step2 as step2


RUN_ID = "KMPC-049"
MODE = "NID"
K_MPC = 0.05
VARIANT = "nominal"
SUPPORT = (0, 7)
EXPECTED_COUNT = 104
CORRECTION_ABS_MAX = 1.0e-12
CORRECTION_REL_MAX = 1.0e-12
KMPC048 = (
    "RUN_KMPC_048_P5_3G7_NID_SUPPORT_STEP_2_05_07.json",
    "B4F320F5D850DCF78FD9EC2A5BDDEBDA87D590DA2988CF505FA7D5B25B49BF32",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def source_hashes() -> dict[str, str]:
    here = Path(__file__).resolve().parent
    hashes = dict(step2.source_hashes())
    hashes["nid_order7_m3_provenance.py"] = sha256_file(
        here / "nid_order7_m3_provenance.py"
    )
    return hashes


def make_deadline(limit: float) -> tuple[float, Callable[[], None]]:
    if not math.isfinite(limit) or limit <= 0.0 or limit > 4.8:
        raise ValueError("KMPC-049 runtime must be in (0, 4.8] seconds")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > limit:
            raise TimeoutError("KMPC-049 NID order-7 provenance deadline exceeded")

    return started, deadline


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


def _array_hash(value: np.ndarray) -> str:
    array = np.ascontiguousarray(value, dtype=np.float64)
    return hashlib.sha256(array.tobytes(order="C")).hexdigest().upper()


def _load_prerequisite(result_dir: Path) -> tuple[dict[str, object], str]:
    path = result_dir / KMPC048[0]
    observed = sha256_file(path)
    if observed != KMPC048[1]:
        raise RuntimeError("immutable KMPC-048 prerequisite hash mismatch")
    return json.loads(path.read_text(encoding="utf-8")), observed


def _owner_fixture() -> dict[str, bool]:
    solve_owner = physics._solve_equilibrated
    holdout_owner = physics._holdout_metrics

    def solve_wrapper(*args: object, **kwargs: object) -> object:
        return solve_owner(*args, **kwargs)

    def holdout_wrapper(*args: object, **kwargs: object) -> object:
        return holdout_owner(*args, **kwargs)

    restored_after_exception = False
    wrong_owner_rejected = physics._solve_equilibrated is not holdout_owner
    try:
        if physics._solve_equilibrated is not solve_owner:
            raise RuntimeError("wrong solve owner before fixture")
        if physics._holdout_metrics is not holdout_owner:
            raise RuntimeError("wrong holdout owner before fixture")
        physics._solve_equilibrated = solve_wrapper
        physics._holdout_metrics = holdout_wrapper
        if physics._solve_equilibrated is not solve_wrapper:
            raise RuntimeError("solve bridge attach failed")
        if physics._holdout_metrics is not holdout_wrapper:
            raise RuntimeError("holdout bridge attach failed")
        raise LookupError("synthetic restore probe")
    except LookupError:
        pass
    finally:
        physics._solve_equilibrated = solve_owner
        physics._holdout_metrics = holdout_owner
        restored_after_exception = bool(
            physics._solve_equilibrated is solve_owner
            and physics._holdout_metrics is holdout_owner
        )
    return {
        "solve_owner_callable": callable(solve_owner),
        "holdout_owner_callable": callable(holdout_owner),
        "wrong_owner_rejected": wrong_owner_rejected,
        "restored_after_exception": restored_after_exception,
    }


def _capture_support(
    inputs: object,
    standard: Mapping[str, Mapping[int, float]],
    deadline: Callable[[], None],
) -> tuple[dict[str, object], dict[str, object]]:
    original_solve = physics._solve_equilibrated
    original_holdout = physics._holdout_metrics
    captured: dict[str, object] = {}
    counts = {"solve": 0, "holdout": 0}

    def solve_capture(
        matrix: np.ndarray,
        constant: np.ndarray,
        expected_rank: int,
        row_labels: list[str] | None = None,
        deadline: Callable[[], None] | None = None,
    ) -> tuple[np.ndarray, dict[str, object]]:
        counts["solve"] += 1
        if counts["solve"] != 1:
            raise RuntimeError("KMPC-049 expected exactly one captured M3 solve")
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
            raise RuntimeError("KMPC-049 expected exactly one captured holdout")
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

    if original_solve is not physics._solve_equilibrated:
        raise RuntimeError("solve owner identity changed before capture")
    if original_holdout is not physics._holdout_metrics:
        raise RuntimeError("holdout owner identity changed before capture")
    try:
        physics._solve_equilibrated = solve_capture
        physics._holdout_metrics = holdout_capture
        solved = step2._solve_support(SUPPORT, inputs, standard, deadline)
    finally:
        physics._solve_equilibrated = original_solve
        physics._holdout_metrics = original_holdout
    captured["capture_counts"] = counts
    captured["owners_restored"] = bool(
        physics._solve_equilibrated is original_solve
        and physics._holdout_metrics is original_holdout
    )
    return solved, captured


def _row_details(
    matrix: np.ndarray,
    constant: np.ndarray,
    solution: np.ndarray,
    labels: tuple[str, ...],
    suffix: str,
    relative_tolerance: float,
) -> dict[str, object]:
    residual = matrix @ solution + constant
    scale = np.abs(constant) + np.sum(
        np.abs(matrix * solution[np.newaxis, :]), axis=1
    )
    details: dict[str, object] = {}
    passed = True
    for index, label in enumerate(labels):
        if not label.endswith(suffix):
            continue
        if scale[index] > physics.ABS_FALLBACK_NORM:
            branch = "relative"
            metric = abs(residual[index]) / scale[index]
            row_pass = metric <= relative_tolerance
        else:
            branch = "absolute"
            metric = abs(residual[index])
            row_pass = metric <= physics.ABS_FALLBACK_TOL
        passed = passed and row_pass
        details[label] = {
            "residual": float(residual[index]),
            "term_norm_scale": float(scale[index]),
            "branch": branch,
            "metric": float(metric),
            "pass": bool(row_pass),
        }
    return {"rows": details, "row_count": len(details), "pass": passed}


def _correction_diagnostic(
    matrix: np.ndarray,
    constant: np.ndarray,
    solution: np.ndarray,
    driver_labels: tuple[str, ...],
    holdout_matrix: np.ndarray,
    holdout_constant: np.ndarray,
    holdout_labels: tuple[str, ...],
) -> dict[str, object]:
    residual = matrix @ solution + constant
    row_scale = np.maximum(
        np.maximum(np.max(np.abs(matrix), axis=1), np.abs(constant)), 1.0e-300
    )
    row_matrix = matrix / row_scale[:, np.newaxis]
    column_scale = np.maximum(np.max(np.abs(row_matrix), axis=0), 1.0e-300)
    equilibrated = row_matrix / column_scale[np.newaxis, :]
    y, _, _, _ = np.linalg.lstsq(
        equilibrated, -residual / row_scale, rcond=physics.RCOND
    )
    correction = y / column_scale
    corrected = solution + correction
    before_driver = physics._row_residual_metrics(
        matrix, constant, solution, list(driver_labels)
    )
    after_driver = physics._row_residual_metrics(
        matrix, constant, corrected, list(driver_labels)
    )
    before_holdout = physics._holdout_metrics(
        holdout_matrix, holdout_constant, solution, list(holdout_labels)
    )
    after_holdout = physics._holdout_metrics(
        holdout_matrix, holdout_constant, corrected, list(holdout_labels)
    )
    correction_abs = float(np.max(np.abs(correction)))
    correction_rel = correction_abs / max(float(np.max(np.abs(solution))), 1.0)
    denominator = (
        np.linalg.norm(matrix, ord=np.inf) * np.linalg.norm(solution, ord=np.inf)
        + np.linalg.norm(constant, ord=np.inf)
    )
    backward_error = float(
        np.linalg.norm(residual, ord=np.inf) / max(float(denominator), 1.0e-300)
    )
    return {
        "method": "one same-matrix equilibrated least-squares correction; diagnostic only",
        "correction_max_abs": correction_abs,
        "correction_Linf_relative_to_max_solution_or_one": correction_rel,
        "normalized_backward_error_Linf": backward_error,
        "before_driver": before_driver,
        "after_driver": after_driver,
        "before_holdout": before_holdout,
        "after_holdout": after_holdout,
        "pass_numerical_boundary_pattern": bool(
            correction_abs <= CORRECTION_ABS_MAX
            and correction_rel <= CORRECTION_REL_MAX
            and after_driver["pass_driver"]
            and after_holdout["pass_holdout"]
        ),
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    _, deadline = make_deadline(max_runtime_seconds)
    immutable, immutable_hash = _load_prerequisite(result_dir)
    owner = _owner_fixture()
    checks = {
        "immutable_KMPC048_hash": immutable_hash == KMPC048[1],
        "immutable_identity": immutable["identity"]
        == {"mode": MODE, "k_Mpc_inverse": K_MPC, "variant": VARIANT},
        "immutable_candidate": immutable["candidate_interpretation_not_verdict"]
        == "REVIEW_NID_SUPPORT_STEP_2_CORE_GATE_UNCLOSED",
        "support_exact_07": SUPPORT == (0, 7) and EXPECTED_COUNT == 104,
        "correction_thresholds_exact": CORRECTION_ABS_MAX == CORRECTION_REL_MAX == 1.0e-12,
        "owner_fixture": all(owner.values()),
    }
    json.dumps({"numpy": np.float64(1.0).item(), "checks": checks}, allow_nan=False)
    deadline()
    return {"run_id": RUN_ID, "mode": "SMOKE_NO_RESULT_FILE", "owner": owner, "checks": checks, "passed": all(checks.values())}


def run_audit(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    started, deadline = make_deadline(max_runtime_seconds)
    immutable, immutable_hash = _load_prerequisite(result_dir)
    inputs = physics._variant_inputs(VARIANT)
    standard, standard_meta = physics._standard_state(MODE, K_MPC, inputs, deadline)
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
        "F0": regression_tools._regression_metric(
            regression_tools._restore_series(immutable_solved["fuel"]["state"]),
            solved["fuel"]["state"],
        ),
        "M3": regression_tools._regression_metric(
            regression_tools._restore_series(immutable_solved["m3"]["fractional_state"]),
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
        "raw_rank_rcond": int(np.sum(raw_singular > physics.RCOND * raw_singular[0])),
        "equilibrated_rank_rcond": int(np.sum(eq_singular > physics.RCOND * eq_singular[0])),
        "raw_singular_ratio": float(raw_singular[-1] / raw_singular[0]),
        "equilibrated_singular_ratio": float(eq_singular[-1] / eq_singular[0]),
        "driver_matrix_sha256_float64_C": _array_hash(matrix),
        "driver_constant_sha256_float64_C": _array_hash(constant),
        "holdout_matrix_sha256_float64_C": _array_hash(holdout_matrix),
        "holdout_constant_sha256_float64_C": _array_hash(holdout_constant),
    }
    matrix_guard["pass"] = bool(
        matrix.shape == (104, 104)
        and holdout_matrix.shape == (16, 104)
        and len(labels) == 104
        and len(holdout_labels) == 16
        and captured["expected_rank"] == 104
        and matrix_guard["raw_rank_rcond"] == 104
        and matrix_guard["equilibrated_rank_rcond"] == 104
        and captured["capture_counts"] == {"solve": 1, "holdout": 1}
        and captured["owners_restored"]
    )
    driver7 = _row_details(
        matrix, constant, solution, labels, "[7]", physics.DRIVER_TOL
    )
    holdout7 = _row_details(
        holdout_matrix,
        holdout_constant,
        solution,
        holdout_labels,
        "[7]",
        physics.HOLDOUT_TOL,
    )
    correction = _correction_diagnostic(
        matrix,
        constant,
        solution,
        labels,
        holdout_matrix,
        holdout_constant,
        holdout_labels,
    )
    rfs = nid1._combined_rfs_guard(standard, inputs)
    finite = _all_finite(
        {"solved": solved, "matrix_guard": matrix_guard, "driver7": driver7, "holdout7": holdout7, "correction": correction}
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
        candidate = "PASS_NID_ORDER7_PROVENANCE_NUMERICAL_BOUNDARY_CANDIDATE_ONLY"
    deadline()
    return {
        "test": "A2-K4 P5.3g7 NID order-7 M3 capture-only provenance",
        "run_id": RUN_ID,
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "candidate_interpretation_not_verdict": candidate,
        "authorship": {"theory_author": "Martin Jambor", "script_creator": "Codex (OpenAI)"},
        "identity": {"mode": MODE, "k_Mpc_inverse": K_MPC, "variant": VARIANT, "support": list(SUPPORT)},
        "immutable_KMPC048": {"file": KMPC048[0], "sha256": immutable_hash},
        "scope": {"included": "same NID [0,7] M3 matrix capture, row-7 residual provenance and one diagnostic correction", "excluded": "new equations/support/thresholds, corrected state publication, [0,9], NIV, other k/variants, S-M, ODE, G8/G9"},
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
        "thresholds": {"driver_relative": physics.DRIVER_TOL, "holdout_relative": physics.HOLDOUT_TOL, "absolute_fallback_norm": physics.ABS_FALLBACK_NORM, "absolute_fallback": physics.ABS_FALLBACK_TOL, "correction_abs_max": CORRECTION_ABS_MAX, "correction_rel_max": CORRECTION_REL_MAX},
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "score_effect": "NONE",
        "release_trigger": "NONE",
        "prediction_table_effect": "NONE",
        "zenodo_trigger": "NONE",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }

