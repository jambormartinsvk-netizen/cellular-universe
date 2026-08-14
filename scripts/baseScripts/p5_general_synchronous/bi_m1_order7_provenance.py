"""BI M1 order-7 provenance audit for KMPC-043 without new physics."""

from __future__ import annotations

import hashlib
import json
import math
import numbers
from pathlib import Path
import time
from typing import Callable, Mapping

import numpy as np

from . import m1_order7_provenance as reference
from . import mode_resolved_puiseux as v1
from . import mode_resolved_puiseux_v2_m1_anchored as anchor


RUN_ID = "KMPC-043"
OUTPUT_NAME = "RUN_KMPC_043_P5_3G7_BI_M1_ORDER7_PROVENANCE_GATE.json"
FAILURE_NAME = "RUN_KMPC_043_P5_3G7_BI_M1_ORDER7_PROVENANCE_GATE_TECHNICAL_FAILURE.json"
MODE = "BI"
K_MPC = 0.05
VARIANT = "nominal"
ORDER_BASE = 5
ORDER_AUDIT = 7
REL_TOL = 1.0e-10
ABS_TOL = 1.0e-12
REGRESSION_REL_TOL = 1.0e-12
REGRESSION_ABS_TOL = 1.0e-14
ANCHOR_TOL = 1.0e-14
INVERSE_CONDITION_MIN = 1.0e-10
KMPC042 = (
    "RUN_KMPC_042_P5_3G7_BI_SUPPORT_STEP_2_03_05.json",
    "E5F18DA4DE5A718C4448D095804F6D41FE88445A95FB99645EFBCCB48D48CA61",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def source_hashes() -> dict[str, str]:
    here = Path(__file__).resolve().parent
    hashes = dict(reference.source_hashes())
    hashes["bi_m1_order7_provenance.py"] = sha256_file(
        here / "bi_m1_order7_provenance.py"
    )
    return hashes


def make_deadline(limit: float) -> tuple[float, Callable[[], None]]:
    if not math.isfinite(limit) or limit <= 0.0 or limit > 4.8:
        raise ValueError("KMPC-043 runtime must be in (0, 4.8] seconds")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > limit:
            raise TimeoutError("KMPC-043 BI M1 order-7 internal deadline exceeded")

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


def _load_prerequisite(result_dir: Path) -> tuple[dict[str, object], str]:
    path = result_dir / KMPC042[0]
    observed = sha256_file(path)
    if observed != KMPC042[1]:
        raise RuntimeError("immutable KMPC-042 prerequisite hash mismatch")
    return json.loads(path.read_text(encoding="utf-8")), observed


def _affine_system(
    order: int, inputs: v1.FrozenInputs, deadline: Callable[[], None]
) -> dict[str, object]:
    series = v1.Series(-4, order + 5)
    powers = tuple(range(-1, order + 1))
    background = v1._standard_background(K_MPC, inputs, series)
    pairs = tuple((name, power) for name in v1.VARS for power in powers)
    index = {pair: position for position, pair in enumerate(pairs)}
    initial = tuple(
        v1._initial_constraints(
            MODE, inputs.radiation_weights[1], inputs.radiation_weights[0]
        )
    )
    driver_labels = tuple(f"{row}[{power}]" for row in v1.DRIVER_ROWS for power in powers)
    initial_labels = tuple(f"initial:{name}[{power}]" for name, power, _ in initial)
    holdout_labels = tuple(f"{row}[{power}]" for row in v1.HOLDOUT_ROWS for power in powers)

    def unpack(vector: np.ndarray) -> dict[str, dict[int, float]]:
        return {
            name: {power: float(vector[index[(name, power)]]) for power in powers}
            for name in v1.VARS
        }

    def driver_initial(vector: np.ndarray) -> np.ndarray:
        rows = v1._standard_rows(unpack(vector), background, series)
        values = [
            series.coef(rows[row], power)
            for row in v1.DRIVER_ROWS
            for power in powers
        ]
        values.extend(
            vector[index[(name, power)]] - value for name, power, value in initial
        )
        return np.asarray(values, dtype=float)

    def holdout(vector: np.ndarray) -> np.ndarray:
        rows = v1._standard_rows(unpack(vector), background, series)
        return np.asarray(
            [
                series.coef(rows[row], power)
                for row in v1.HOLDOUT_ROWS
                for power in powers
            ],
            dtype=float,
        )

    zero = np.zeros(len(pairs), dtype=float)
    driver_constant = driver_initial(zero)
    holdout_constant = holdout(zero)
    driver_matrix = np.empty((driver_constant.size, len(pairs)), dtype=float)
    holdout_matrix = np.empty((holdout_constant.size, len(pairs)), dtype=float)
    for column in range(len(pairs)):
        deadline()
        basis = np.zeros(len(pairs), dtype=float)
        basis[column] = 1.0
        driver_matrix[:, column] = driver_initial(basis) - driver_constant
        holdout_matrix[:, column] = holdout(basis) - holdout_constant
    target_power, expected_h = v1._m1_expected_h(MODE, background, inputs)
    return {
        "series": series,
        "powers": powers,
        "background": background,
        "pairs": pairs,
        "index": index,
        "driver_labels": driver_labels + initial_labels,
        "holdout_labels": holdout_labels,
        "driver_constant": driver_constant,
        "driver_matrix": driver_matrix,
        "holdout_constant": holdout_constant,
        "holdout_matrix": holdout_matrix,
        "anchor_index": index[("h", target_power)],
        "anchor_power": target_power,
        "anchor_value": expected_h,
    }


def _fixture_guard(
    order: int,
    mode: str,
    state_names: tuple[str, ...],
    powers: tuple[int, ...],
    anchor_label: str,
    holdout_labels: tuple[str, ...],
) -> bool:
    expected_holdouts = tuple(
        f"{row}[{power}]" for row in v1.HOLDOUT_ROWS for power in range(-1, 8)
    )
    return bool(
        order == ORDER_AUDIT
        and mode == MODE
        and state_names == tuple(v1.VARS)
        and powers == tuple(range(-1, 8))
        and anchor_label == "h[1]"
        and holdout_labels == expected_holdouts
        and len(set(holdout_labels)) == len(holdout_labels)
        and 6 in powers
        and 7 in powers
    )


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    _, deadline = make_deadline(max_runtime_seconds)
    immutable, immutable_hash = _load_prerequisite(result_dir)
    powers = tuple(range(-1, 8))
    holdouts = tuple(f"{row}[{power}]" for row in v1.HOLDOUT_ROWS for power in powers)
    canonical = _fixture_guard(7, MODE, tuple(v1.VARS), powers, "h[1]", holdouts)
    negative = {
        "wrong_mode_CDI_rejected": not _fixture_guard(
            7, "CDI", tuple(v1.VARS), powers, "h[1]", holdouts
        ),
        "wrong_order_rejected": not _fixture_guard(
            5, MODE, tuple(v1.VARS), powers, "h[1]", holdouts
        ),
        "reordered_state_rejected": not _fixture_guard(
            7, MODE, tuple(reversed(v1.VARS)), powers, "h[1]", holdouts
        ),
        "missing_high_power_rejected": not _fixture_guard(
            7, MODE, tuple(v1.VARS), powers[:-1], "h[1]", holdouts
        ),
        "missing_anchor_rejected": not _fixture_guard(
            7, MODE, tuple(v1.VARS), powers, "", holdouts
        ),
        "missing_holdout_rejected": not _fixture_guard(
            7, MODE, tuple(v1.VARS), powers, "h[1]", holdouts[:-1]
        ),
    }
    dimensions = reference.expected_dimensions(7)
    checks = {
        "canonical_BI_fixture": canonical,
        "all_negative_fixtures": all(negative.values()),
        "dimensions_exact": bool(
            dimensions["augmented_shape"] == [121, 99]
            and dimensions["reduced_shape"] == [121, 98]
            and dimensions["holdout_rows"] == 18
        ),
        "immutable_KMPC042_hash": immutable_hash == KMPC042[1],
        "immutable_KMPC042_identity": immutable["identity"]
        == {"mode": MODE, "k_Mpc_inverse": K_MPC, "variant": VARIANT},
        "immutable_KMPC042_candidate": immutable["candidate_interpretation_not_verdict"]
        == "REVIEW_BI_SUPPORT_STEP_2_SUPPORT_03_REMAINDER_UNCLOSED",
    }
    deadline()
    return {
        "run_id": RUN_ID,
        "mode": "SMOKE_NO_RESULT_FILE",
        "negative_fixtures": negative,
        "checks": checks,
        "passed": all(checks.values()),
    }


def run_audit(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    started, deadline = make_deadline(max_runtime_seconds)
    immutable, immutable_hash = _load_prerequisite(result_dir)
    inputs = v1.FrozenInputs()
    state5, background5, meta5 = anchor.solve_standard_seed_anchored(
        MODE, K_MPC, inputs, deadline, order=ORDER_BASE
    )
    state7, background7, meta7 = anchor.solve_standard_seed_anchored(
        MODE, K_MPC, inputs, deadline, order=ORDER_AUDIT
    )
    system7 = _affine_system(ORDER_AUDIT, inputs, deadline)
    vector7 = reference._vector_from_state(state7, system7["pairs"])
    driver_initial = reference._residual_metrics(
        system7["driver_matrix"],
        system7["driver_constant"],
        vector7,
        system7["driver_labels"],
    )
    holdout = reference._residual_metrics(
        system7["holdout_matrix"],
        system7["holdout_constant"],
        vector7,
        system7["holdout_labels"],
    )
    dimensions = reference.expected_dimensions(ORDER_AUDIT)
    reduced = np.delete(system7["driver_matrix"], system7["anchor_index"], axis=1)
    recomputed_rank = int(np.linalg.matrix_rank(reduced))
    shapes_pass = bool(
        list(system7["driver_matrix"].shape) == dimensions["augmented_shape"]
        and list(reduced.shape) == dimensions["reduced_shape"]
        and list(system7["holdout_matrix"].shape) == [18, 99]
        and int(meta7["full_vector_unknowns"]) == 99
        and int(meta7["unknowns"]) == 98
    )
    rank_pass = bool(int(meta7["rank"]) == 98 and recomputed_rank == 98)
    anchor_pass = bool(
        meta7["hard_anchor_variable"] == "h[1]"
        and float(meta7["hard_anchor_absolute_difference"]) <= ANCHOR_TOL
    )
    condition_pass = 1.0 / float(meta7["condition_resolved"]) >= INVERSE_CONDITION_MIN
    state_guard = reference._exact_state_guard(state7, ORDER_AUDIT)
    common_state = reference._hybrid_regression(state5, state7, tuple(range(-1, 6)))
    common_background = reference._background_regression(background5, background7)
    immutable_meta = reference._immutable_metadata_regression(
        meta5, immutable["M1_standard_metadata"]
    )
    finite = _all_finite(
        {
            "state5": state5,
            "state7": state7,
            "meta5": meta5,
            "meta7": meta7,
            "driver": driver_initial,
            "holdout": holdout,
            "background5": background5,
            "background7": background7,
        }
    )
    core_pass = bool(
        shapes_pass
        and rank_pass
        and anchor_pass
        and condition_pass
        and state_guard["pass"]
        and driver_initial["pass"]
        and holdout["pass"]
        and finite
    )
    regression_pass = bool(
        immutable_meta["pass"] and common_state["pass"] and common_background["pass"]
    )
    if not regression_pass:
        candidate = "REVIEW_BI_M1_ORDER7_REGRESSION_DRIFT"
    elif not core_pass:
        candidate = "REVIEW_BI_M1_ORDER7_CORE_OR_HOLDOUT_UNCLOSED"
    else:
        candidate = "PASS_BI_M1_ORDER7_PROVENANCE_CANDIDATE_ONLY"
    payload = {
        "test": "A2-K4 P5.3g7 GLOBAL_C1 BI_M1_ORDER7_PROVENANCE_GATE",
        "run_id": RUN_ID,
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "candidate_interpretation_not_verdict": candidate,
        "identity": {
            "mode": MODE,
            "k_Mpc_inverse": K_MPC,
            "variant": VARIANT,
            "order": ORDER_AUDIT,
        },
        "scope": {
            "included": "BI anchored standard M1 order-5 to order-7 provenance and full-power residual/holdout audit",
            "excluded": "CDI state/correction transfer, refinement, high precision, BI support step 3, [0,7], NID/NIV, other k/variants, S-M, ODE, P5.4, G8/G9, CLASS/CMB/BBN/S8/H0",
        },
        "immutable_prerequisite": {"file": KMPC042[0], "sha256": immutable_hash},
        "dimensions": dimensions,
        "shapes_pass": shapes_pass,
        "rank_pass": rank_pass,
        "independently_recomputed_reduced_rank": recomputed_rank,
        "anchor_pass": anchor_pass,
        "condition_pass": condition_pass,
        "state_guard": state_guard,
        "driver_and_initial_full_power": driver_initial,
        "holdout_full_power": holdout,
        "order5_immutable_metadata_regression": immutable_meta,
        "order5_to_order7_common_state_regression": common_state,
        "order5_to_order7_common_background_regression": common_background,
        "M1_order5_metadata": meta5,
        "M1_order7_metadata": meta7,
        "M1_order7_state": state7,
        "M1_order7_background": background7,
        "finite_pass": finite,
        "regression_pass": regression_pass,
        "core_pass": core_pass,
        "source_hashes": source_hashes(),
        "thresholds": {
            "residual_relative": REL_TOL,
            "residual_absolute": ABS_TOL,
            "regression_relative": REGRESSION_REL_TOL,
            "regression_absolute": REGRESSION_ABS_TOL,
            "anchor_absolute": ANCHOR_TOL,
            "inverse_condition_min": INVERSE_CONDITION_MIN,
        },
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "score_effect": "NONE",
        "release_trigger": "NONE",
        "zenodo_trigger": "NONE",
        "prediction_table_effect": "NONE",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }
    if not _all_finite(payload):
        raise FloatingPointError("non-finite value in final KMPC-043 payload")
    deadline()
    return payload
