"""KMPC-051 diagnostic comparison of NID M1 depth 5 versus 7.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
The M3 support, equations, state registry, and thresholds remain unchanged.
"""

from __future__ import annotations

import json
import math
import numbers
from pathlib import Path
import time
from typing import Callable, Mapping

import numpy as np

from . import nid_order7_m3_provenance_v2_rank_filter as k50


v1 = k50.v1
physics = v1.physics
anchor = physics.m1_anchor
legacy = physics.legacy
RUN_ID = "KMPC-051"
M1_BASELINE_DEPTH = 5
M1_CANDIDATE_DEPTH = 7
COMMON_TOL = 1.0e-8
KMPC050 = (
    "RUN_KMPC_050_P5_3G7_NID_ORDER7_M3_PROVENANCE_RANK_FILTER.json",
    "8D527E822959D861EB33994233D22BDF752C368025AC66F28C6F820DEF479F65",
)


def source_hashes() -> dict[str, str]:
    here = Path(__file__).resolve().parent
    hashes = dict(k50.source_hashes())
    hashes["nid_m1_depth_5_7.py"] = v1.sha256_file(here / "nid_m1_depth_5_7.py")
    return hashes


def _load_prerequisite(result_dir: Path) -> tuple[dict[str, object], str]:
    path = result_dir / KMPC050[0]
    observed = v1.sha256_file(path)
    if observed != KMPC050[1]:
        raise RuntimeError("immutable KMPC-050 prerequisite hash mismatch")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("candidate_interpretation_not_verdict") != (
        "REVIEW_NID_ORDER7_NONNUMERICAL_CORE_UNCLOSED"
    ):
        raise RuntimeError("immutable KMPC-050 candidate mismatch")
    return payload, observed


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


def _standard_depth(
    depth: int,
    inputs: object,
    deadline: Callable[[], None],
) -> tuple[dict[str, dict[int, float]], dict[str, object]]:
    state_legacy, background, metadata = anchor.solve_standard_seed_anchored(
        v1.MODE, v1.K_MPC, inputs, deadline, order=depth
    )
    state = {
        target: dict(state_legacy[source])
        for target, source in physics.STATE_TO_LEGACY.items()
    }
    series = legacy.Series(-4, depth + 5)
    rows = legacy._standard_rows(state_legacy, background, series)
    exponents = tuple(range(-1, depth + 1))
    scale = max(
        max(abs(float(value)) for values in state.values() for value in values.values()),
        1.0e-14,
    )
    driver_max = max(
        abs(series.coef(rows[row], power))
        for row in legacy.DRIVER_ROWS
        for power in exponents
    )
    holdout_max = max(
        abs(series.coef(rows[row], power))
        for row in legacy.HOLDOUT_ROWS
        for power in exponents
    )
    full = {
        "depth": depth,
        "exponents": list(exponents),
        "full_vector_unknowns_expected": 11 * (depth + 2),
        "reduced_unknowns_expected": 11 * (depth + 2) - 1,
        "driver_max_absolute": float(driver_max),
        "holdout_max_absolute": float(holdout_max),
        "state_scale": float(scale),
        "driver_global_state_scaled": float(driver_max / scale),
        "holdout_global_state_scaled": float(holdout_max / scale),
        "finite": _all_finite({"state": state, "metadata": metadata}),
    }
    full["rank_count_anchor_pass"] = bool(
        metadata["rank"] == metadata["unknowns"] == full["reduced_unknowns_expected"]
        and metadata["full_vector_unknowns"] == full["full_vector_unknowns_expected"]
        and metadata["hard_anchor_absolute_difference"] <= physics.ABS_FALLBACK_TOL
        and full["finite"]
    )
    full["solver_metadata"] = dict(metadata)
    deadline()
    return state, full


def _restrict(
    state: Mapping[str, Mapping[int, float]], lo: int, hi: int
) -> dict[str, dict[int, float]]:
    return {
        name: {power: float(values.get(power, 0.0)) for power in range(lo, hi + 1)}
        for name, values in state.items()
    }


def _regression(
    baseline: Mapping[str, Mapping[int, float]],
    candidate: Mapping[str, Mapping[int, float]],
) -> dict[str, object]:
    exact_state_set = set(baseline) == set(candidate)
    exact_power_sets = exact_state_set and all(
        set(baseline[name]) == set(candidate[name]) for name in baseline
    )
    rows: list[tuple[str, float, float, float, float]] = []
    if exact_power_sets:
        for name in sorted(baseline):
            for power in sorted(baseline[name]):
                left = float(baseline[name][power])
                right = float(candidate[name][power])
                absolute = abs(right - left)
                relative = absolute / max(abs(left), abs(right), 1.0)
                rows.append((f"{name}[{power}]", left, right, absolute, relative))
    worst = max(rows, key=lambda row: row[4]) if rows else ("NONE", 0.0, 0.0, float("inf"), float("inf"))
    finite = _all_finite(rows)
    return {
        "coefficient_count": len(rows),
        "exact_state_set": exact_state_set,
        "exact_power_sets": exact_power_sets,
        "finite": finite,
        "worst_coefficient": worst[0],
        "baseline_value": worst[1],
        "candidate_value": worst[2],
        "max_absolute_difference": worst[3],
        "max_relative_to_max_or_one": worst[4],
        "frozen_limit": COMMON_TOL,
        "pass_frozen_limit": bool(
            exact_power_sets and finite and worst[4] <= COMMON_TOL
        ),
    }


def _matrix_summary(captured: Mapping[str, object]) -> dict[str, object]:
    matrix = captured["driver_matrix"]
    constant = captured["driver_constant"]
    holdout_matrix = captured["holdout_matrix"]
    holdout_constant = captured["holdout_constant"]
    raw_singular = np.linalg.svd(matrix, compute_uv=False)
    row_scale = np.maximum(
        np.maximum(np.max(np.abs(matrix), axis=1), np.abs(constant)), 1.0e-300
    )
    row_matrix = matrix / row_scale[:, np.newaxis]
    column_scale = np.maximum(np.max(np.abs(row_matrix), axis=0), 1.0e-300)
    equilibrated = row_matrix / column_scale[np.newaxis, :]
    eq_singular = np.linalg.svd(equilibrated, compute_uv=False)
    summary = {
        "driver_shape": list(matrix.shape),
        "holdout_shape": list(holdout_matrix.shape),
        "capture_counts": captured["capture_counts"],
        "owners_restored": captured["owners_restored"],
        "raw_rank_rcond": int(np.sum(raw_singular > physics.RCOND * raw_singular[0])),
        "equilibrated_rank_rcond": int(
            np.sum(eq_singular > physics.RCOND * eq_singular[0])
        ),
        "driver_matrix_sha256_float64_C": v1._array_hash(matrix),
        "driver_constant_sha256_float64_C": v1._array_hash(constant),
        "holdout_matrix_sha256_float64_C": v1._array_hash(holdout_matrix),
        "holdout_constant_sha256_float64_C": v1._array_hash(holdout_constant),
    }
    summary["pass"] = bool(
        matrix.shape == (104, 104)
        and holdout_matrix.shape == (16, 104)
        and summary["raw_rank_rcond"] == summary["equilibrated_rank_rcond"] == 104
        and captured["capture_counts"]
        == {"passthrough": 1, "target": 1, "holdout": 1}
        and captured["owners_restored"]
    )
    return summary


def _array_difference(first: np.ndarray, second: np.ndarray) -> dict[str, float]:
    delta = np.asarray(second) - np.asarray(first)
    maximum = float(np.max(np.abs(delta)))
    scale = max(float(np.max(np.abs(first))), float(np.max(np.abs(second))), 1.0)
    return {"max_absolute": maximum, "max_relative_to_max_or_one": maximum / scale}


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    _, deadline = v1.make_deadline(max_runtime_seconds)
    immutable, observed = _load_prerequisite(result_dir)
    checks = {
        "immutable_KMPC050_hash": observed == KMPC050[1],
        "immutable_provenance_pass": immutable["provenance_pass"] is True,
        "immutable_correction_pattern_fail": immutable[
            "same_matrix_correction_diagnostic"
        ]["pass_numerical_boundary_pattern"]
        is False,
        "depths_exact": (M1_BASELINE_DEPTH, M1_CANDIDATE_DEPTH) == (5, 7),
        "depth7_counts_exact": 11 * (M1_CANDIDATE_DEPTH + 2) == 99,
        "common_threshold_exact": COMMON_TOL == 1.0e-8,
        "capture_signature_guard": k50._target_signature(
            np.zeros((104, 104)), 104
        ),
    }
    deadline()
    return {
        "run_id": RUN_ID,
        "mode": "SMOKE_NO_RESULT_FILE",
        "checks": checks,
        "passed": all(checks.values()),
    }


def run_audit(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    started, deadline = v1.make_deadline(max_runtime_seconds)
    immutable, immutable_hash = _load_prerequisite(result_dir)
    inputs = physics._variant_inputs(v1.VARIANT)
    standard5, m1meta5 = _standard_depth(M1_BASELINE_DEPTH, inputs, deadline)
    solved5, captured5 = k50._capture_support(inputs, standard5, deadline)
    standard7, m1meta7 = _standard_depth(M1_CANDIDATE_DEPTH, inputs, deadline)
    solved7, captured7 = k50._capture_support(inputs, standard7, deadline)
    matrix5 = _matrix_summary(captured5)
    matrix7 = _matrix_summary(captured7)
    immutable_matrix = immutable["matrix_provenance_guard"]
    baseline_hash_match = all(
        matrix5[key] == immutable_matrix[key]
        for key in (
            "driver_matrix_sha256_float64_C",
            "driver_constant_sha256_float64_C",
            "holdout_matrix_sha256_float64_C",
            "holdout_constant_sha256_float64_C",
        )
    )
    m1_common = _regression(
        _restrict(standard5, -1, 5), _restrict(standard7, -1, 5)
    )
    m3_common = _regression(
        _restrict(solved5["m3"]["fractional_state"], 0, 5),
        _restrict(solved7["m3"]["fractional_state"], 0, 5),
    )
    f0_common = _regression(
        _restrict(solved5["fuel"]["state"], 0, 5),
        _restrict(solved7["fuel"]["state"], 0, 5),
    )
    correction5 = v1._correction_diagnostic(
        captured5["driver_matrix"],
        captured5["driver_constant"],
        captured5["solution"],
        captured5["driver_labels"],
        captured5["holdout_matrix"],
        captured5["holdout_constant"],
        captured5["holdout_labels"],
    )
    correction7 = v1._correction_diagnostic(
        captured7["driver_matrix"],
        captured7["driver_constant"],
        captured7["solution"],
        captured7["driver_labels"],
        captured7["holdout_matrix"],
        captured7["holdout_constant"],
        captured7["holdout_labels"],
    )
    m3diag7 = solved7["m3"]["diagnostics"]
    depth7_core_pass = bool(
        m3diag7["pass_driver"] and m3diag7["holdout"]["pass_holdout"]
    )
    baseline_pass = bool(
        baseline_hash_match and matrix5["pass"] and solved5["pass"] is False
    )
    m1_depth7_pass = bool(m1meta7["rank_count_anchor_pass"])
    common_pass = bool(
        m1_common["pass_frozen_limit"]
        and m3_common["pass_frozen_limit"]
        and f0_common["pass_frozen_limit"]
    )
    finite = _all_finite(
        {
            "m1meta5": m1meta5,
            "m1meta7": m1meta7,
            "matrix5": matrix5,
            "matrix7": matrix7,
            "correction5": correction5,
            "correction7": correction7,
        }
    )
    if not baseline_pass or not finite:
        candidate = "REVIEW_NID_M1_DEPTH_BASELINE_DRIFT"
    elif not m1_depth7_pass or not matrix7["pass"]:
        candidate = "REVIEW_NID_M1_DEPTH7_EXTENSION_UNCLOSED"
    elif not common_pass:
        candidate = "REVIEW_NID_M1_DEPTH7_COMMON_REGRESSION"
    elif depth7_core_pass:
        candidate = "PASS_NID_M1_DEPTH_MISMATCH_CANDIDATE_ONLY"
    else:
        candidate = (
            "REVIEW_NID_M1_DEPTH_MISMATCH_REJECTED_CONSTRAINT_AUDIT_REQUIRED"
        )
    deadline()
    return {
        "test": "A2-K4 P5.3g7 KMPC-051 NID M1 depth 5-to-7 diagnostic",
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
            "M3_support": list(v1.SUPPORT),
            "M1_depths": [M1_BASELINE_DEPTH, M1_CANDIDATE_DEPTH],
        },
        "immutable_KMPC050": {"file": KMPC050[0], "sha256": immutable_hash},
        "scope": {
            "included": "same NID [0,7] M3 system under hard-anchored M1 depth 5 and 7",
            "excluded": "equation/support/threshold changes, [0,9], NIV, other k/variants, S-M, ODE, G8/G9",
        },
        "M1_depth5": m1meta5,
        "M1_depth7": m1meta7,
        "M1_common_minus1_5": m1_common,
        "F0_common_0_5": f0_common,
        "M3_common_0_5": m3_common,
        "baseline_matrix": matrix5,
        "depth7_matrix": matrix7,
        "matrix_differences_depth7_minus_depth5": {
            "driver_matrix": _array_difference(
                captured5["driver_matrix"], captured7["driver_matrix"]
            ),
            "driver_constant": _array_difference(
                captured5["driver_constant"], captured7["driver_constant"]
            ),
            "holdout_matrix": _array_difference(
                captured5["holdout_matrix"], captured7["holdout_matrix"]
            ),
            "holdout_constant": _array_difference(
                captured5["holdout_constant"], captured7["holdout_constant"]
            ),
        },
        "baseline_hash_match_KMPC050": baseline_hash_match,
        "baseline_pass": baseline_pass,
        "depth7_solve_checks": solved7["checks"],
        "depth7_original_M3_diagnostics": m3diag7,
        "depth7_core_pass": depth7_core_pass,
        "same_matrix_correction_depth5": correction5,
        "same_matrix_correction_depth7": correction7,
        "M1_depth7_pass": m1_depth7_pass,
        "common_pass": common_pass,
        "finite_pass": finite,
        "source_hashes": source_hashes(),
        "thresholds": {
            "common_relative": COMMON_TOL,
            "driver_relative": physics.DRIVER_TOL,
            "holdout_relative": physics.HOLDOUT_TOL,
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
