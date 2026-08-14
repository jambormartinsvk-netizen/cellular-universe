"""KMPC-036 M1 order-7 provenance audit without new physics equations."""

from __future__ import annotations

import hashlib
import math
import numbers
from pathlib import Path
import time
from typing import Callable, Mapping

import numpy as np

from . import mode_resolved_puiseux as v1
from . import mode_resolved_puiseux_v2_m1_anchored as anchor


RUN_ID = "KMPC-036"
MODE = "CDI"
K_MPC = 0.05
VARIANT = "nominal"
ORDER_BASE = 5
ORDER_AUDIT = 7
STATE_COUNT = 11
DRIVER_COUNT = 11
HOLDOUT_COUNT = 2
INITIAL_COUNT = 22
REL_TOL = 1.0e-10
ABS_TOL = 1.0e-12
REGRESSION_REL_TOL = 1.0e-12
REGRESSION_ABS_TOL = 1.0e-14
ANCHOR_TOL = 1.0e-14
INVERSE_CONDITION_MIN = 1.0e-10
EXPECTED_RESULT = (
    "RUN_KMPC_035_P5_3G7_CDI_C2_SUPPORT_03_05_LADDER.json",
    "A9BD519F9124B80E648EE327A3C2175A5E9DC3D65B02EB1CFD7F119333E42A01",
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
    )
    return {name: sha256_file(root / name) for name in names}


def make_deadline(limit: float) -> tuple[float, Callable[[], None]]:
    if not math.isfinite(limit) or limit <= 0.0 or limit > 4.8:
        raise ValueError("KMPC-036 runtime must be in (0, 4.8]")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > limit:
            raise TimeoutError("KMPC-036 M1 order-7 internal deadline exceeded")

    return started, deadline


def expected_dimensions(order: int) -> dict[str, object]:
    powers = order + 2
    full = STATE_COUNT * powers
    driver = DRIVER_COUNT * powers
    rows = driver + INITIAL_COUNT
    return {
        "order": order,
        "powers": list(range(-1, order + 1)),
        "power_count": powers,
        "full_unknowns": full,
        "solved_unknowns": full - 1,
        "driver_rows": driver,
        "initial_rows": INITIAL_COUNT,
        "augmented_shape": [rows, full],
        "reduced_shape": [rows, full - 1],
        "holdout_rows": HOLDOUT_COUNT * powers,
    }


def _all_finite(value: object) -> bool:
    if value is None or isinstance(value, (str, bool)):
        return True
    if isinstance(value, numbers.Real):
        return math.isfinite(float(value))
    if isinstance(value, np.ndarray):
        return bool(np.all(np.isfinite(value)))
    if isinstance(value, Mapping):
        return all(_all_finite(item) for item in value.values())
    if isinstance(value, (list, tuple)):
        return all(_all_finite(item) for item in value)
    return True


def _exact_state_guard(
    state: Mapping[str, Mapping[int, float]], order: int
) -> dict[str, object]:
    expected_states = tuple(v1.VARS)
    expected_powers = tuple(range(-1, order + 1))
    state_names_exact = tuple(state) == expected_states
    powers_exact = {
        name: tuple(state.get(name, {})) == expected_powers for name in expected_states
    }
    high_powers_present = all(
        6 in state.get(name, {}) and 7 in state.get(name, {}) for name in expected_states
    )
    return {
        "expected_states": list(expected_states),
        "state_names_exact_ordered": state_names_exact,
        "powers_exact_ordered": powers_exact,
        "high_powers_6_7_present_for_all_states": high_powers_present,
        "pass": bool(state_names_exact and all(powers_exact.values()) and high_powers_present),
    }


def _affine_system(
    order: int,
    inputs: v1.FrozenInputs,
    deadline: Callable[[], None],
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
        values.extend(vector[index[(name, power)]] - value for name, power, value in initial)
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


def _vector_from_state(
    state: Mapping[str, Mapping[int, float]], pairs: tuple[tuple[str, int], ...]
) -> np.ndarray:
    return np.asarray([state[name][power] for name, power in pairs], dtype=float)


def _residual_metrics(
    matrix: np.ndarray,
    constant: np.ndarray,
    vector: np.ndarray,
    labels: tuple[str, ...],
) -> dict[str, object]:
    residual = matrix @ vector + constant
    term_norm = np.abs(constant) + np.abs(matrix * vector[np.newaxis, :]).sum(axis=1)
    rows: list[dict[str, object]] = []
    passed = True
    for label, raw, norm in zip(labels, residual, term_norm, strict=True):
        if norm > ABS_TOL:
            branch = "relative"
            metric = abs(float(raw)) / float(norm)
            row_pass = metric <= REL_TOL
        else:
            branch = "absolute"
            metric = abs(float(raw))
            row_pass = metric <= ABS_TOL
        passed = passed and row_pass
        rows.append(
            {
                "label": label,
                "branch": branch,
                "residual": float(raw),
                "term_norm": float(norm),
                "metric": float(metric),
                "pass": bool(row_pass),
            }
        )
    worst = max(rows, key=lambda item: float(item["metric"]))
    return {
        "row_count": len(rows),
        "rows": rows,
        "worst": worst,
        "pass": bool(passed),
    }


def _hybrid_regression(
    left: Mapping[str, Mapping[int, float]],
    right: Mapping[str, Mapping[int, float]],
    powers: tuple[int, ...],
) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    passed = True
    for name in v1.VARS:
        for power in powers:
            a = float(left[name][power])
            b = float(right[name][power])
            difference = abs(a - b)
            bound = max(
                REGRESSION_ABS_TOL,
                REGRESSION_REL_TOL * max(abs(a), abs(b)),
            )
            row_pass = difference <= bound
            passed = passed and row_pass
            rows.append(
                {
                    "label": f"{name}[{power}]",
                    "difference": difference,
                    "bound": bound,
                    "pass": bool(row_pass),
                }
            )
    worst = max(rows, key=lambda item: float(item["difference"]) / float(item["bound"]))
    return {"rows": rows, "worst": worst, "pass": bool(passed)}


def _background_regression(
    left: Mapping[str, object], right: Mapping[str, object]
) -> dict[str, object]:
    names = ("D", "invD", "hc", "s2", "Og", "Ofs", "Ob", "Oc", "loading", "inv1R", "load_fraction")
    rows: list[dict[str, object]] = []
    passed = True
    for name in names:
        a_series = left[name]
        b_series = right[name]
        for power in range(-4, 6):
            a = float(a_series.get(power, 0.0))
            b = float(b_series.get(power, 0.0))
            difference = abs(a - b)
            bound = max(REGRESSION_ABS_TOL, REGRESSION_REL_TOL * max(abs(a), abs(b)))
            row_pass = difference <= bound
            passed = passed and row_pass
            rows.append({"label": f"{name}[{power}]", "difference": difference, "bound": bound, "pass": bool(row_pass)})
    worst = max(rows, key=lambda item: float(item["difference"]) / float(item["bound"]))
    return {"rows": rows, "worst": worst, "pass": bool(passed)}


def _immutable_metadata_regression(
    current: Mapping[str, object], immutable: Mapping[str, object]
) -> dict[str, object]:
    exact = {
        "rank": int(current["rank"]) == int(immutable["rank"]),
        "unknowns": int(current["unknowns"]) == int(immutable["unknowns"]),
        "full_vector_unknowns": int(current["full_vector_unknowns"]) == int(immutable["full_vector_unknowns"]),
        "hard_anchor_variable": current["hard_anchor_variable"] == immutable["hard_anchor_variable"],
        "hard_anchor_method": current["hard_anchor_method"] == immutable["hard_anchor_method"],
        "m1_h_power": int(current["m1_h_power"]) == int(immutable["m1_h_power"]),
        "expected_matrix_shape": immutable["expected_matrix_shape_before_anchor"] == [99, 77],
        "expected_unknowns_after_anchor": int(immutable["expected_unknowns_after_anchor"]) == 76,
    }
    floats = {}
    for name in (
        "condition_resolved",
        "driver_scaled_residual",
        "holdout_scaled_residual",
        "hard_anchor_absolute_difference",
        "m1_expected_h_coefficient",
        "m1_observed_h_coefficient",
        "m1_h_relative_difference",
    ):
        a = float(current[name])
        b = float(immutable[name])
        floats[name] = abs(a - b) <= max(REGRESSION_ABS_TOL, REGRESSION_REL_TOL * max(abs(a), abs(b)))
    return {"exact": exact, "floats": floats, "pass": bool(all(exact.values()) and all(floats.values()))}


def _fixture_guard(
    order: int,
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
    success_path = result_dir / "RUN_KMPC_036_P5_3G7_M1_ORDER7_PROVENANCE_GATE.json"
    failure_path = result_dir / "RUN_KMPC_036_P5_3G7_M1_ORDER7_PROVENANCE_GATE_TECHNICAL_FAILURE.json"
    if success_path.exists() or failure_path.exists():
        raise FileExistsError("KMPC-036 immutable output already exists")
    powers = tuple(range(-1, 8))
    holdouts = tuple(f"{row}[{power}]" for row in v1.HOLDOUT_ROWS for power in powers)
    canonical = _fixture_guard(7, tuple(v1.VARS), powers, "h[1]", holdouts)
    negative = {
        "wrong_order": not _fixture_guard(5, tuple(v1.VARS), powers, "h[1]", holdouts),
        "reordered_state": not _fixture_guard(7, tuple(reversed(v1.VARS)), powers, "h[1]", holdouts),
        "missing_high_power": not _fixture_guard(7, tuple(v1.VARS), powers[:-1], "h[1]", holdouts),
        "missing_anchor": not _fixture_guard(7, tuple(v1.VARS), powers, "", holdouts),
        "missing_holdout": not _fixture_guard(7, tuple(v1.VARS), powers, "h[1]", holdouts[:-1]),
        "duplicate_holdout": not _fixture_guard(7, tuple(v1.VARS), powers, "h[1]", holdouts[:-1] + (holdouts[-2],)),
    }
    dimensions = expected_dimensions(7)
    deadline()
    passed = bool(
        canonical
        and all(negative.values())
        and dimensions["augmented_shape"] == [121, 99]
        and dimensions["reduced_shape"] == [121, 98]
        and dimensions["holdout_rows"] == 18
    )
    if not passed:
        raise RuntimeError("KMPC-036 smoke fixture failed")
    return {"run_id": RUN_ID, "smoke_pass": True, "negative_fixtures": negative}


def run_audit(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    started, deadline = make_deadline(max_runtime_seconds)
    prerequisite = result_dir / EXPECTED_RESULT[0]
    if sha256_file(prerequisite) != EXPECTED_RESULT[1]:
        raise RuntimeError("immutable KMPC-035 prerequisite hash mismatch")
    import json

    immutable = json.loads(prerequisite.read_text(encoding="utf-8"))
    inputs = v1.FrozenInputs()
    state5, background5, meta5 = anchor.solve_standard_seed_anchored(
        MODE, K_MPC, inputs, deadline, order=ORDER_BASE
    )
    state7, background7, meta7 = anchor.solve_standard_seed_anchored(
        MODE, K_MPC, inputs, deadline, order=ORDER_AUDIT
    )
    system7 = _affine_system(ORDER_AUDIT, inputs, deadline)
    vector7 = _vector_from_state(state7, system7["pairs"])
    driver_initial = _residual_metrics(
        system7["driver_matrix"], system7["driver_constant"], vector7, system7["driver_labels"]
    )
    holdout = _residual_metrics(
        system7["holdout_matrix"], system7["holdout_constant"], vector7, system7["holdout_labels"]
    )
    dimensions = expected_dimensions(ORDER_AUDIT)
    reduced = np.delete(system7["driver_matrix"], system7["anchor_index"], axis=1)
    independently_recomputed_rank = int(np.linalg.matrix_rank(reduced))
    shapes_pass = bool(
        list(system7["driver_matrix"].shape) == dimensions["augmented_shape"]
        and list(reduced.shape) == dimensions["reduced_shape"]
        and list(system7["holdout_matrix"].shape) == [18, 99]
        and int(meta7["full_vector_unknowns"]) == 99
        and int(meta7["unknowns"]) == 98
    )
    rank_pass = bool(int(meta7["rank"]) == 98 and independently_recomputed_rank == 98)
    anchor_pass = bool(
        meta7["hard_anchor_variable"] == "h[1]"
        and float(meta7["hard_anchor_absolute_difference"]) <= ANCHOR_TOL
    )
    condition_pass = 1.0 / float(meta7["condition_resolved"]) >= INVERSE_CONDITION_MIN
    state_guard = _exact_state_guard(state7, ORDER_AUDIT)
    common_state = _hybrid_regression(state5, state7, tuple(range(-1, 6)))
    common_background = _background_regression(background5, background7)
    immutable_meta = _immutable_metadata_regression(meta5, immutable["M1_standard_metadata"])
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
    regression_pass = bool(immutable_meta["pass"] and common_state["pass"] and common_background["pass"])
    if not regression_pass:
        candidate = "REVIEW_M1_ORDER7_REGRESSION_DRIFT"
    elif not core_pass:
        candidate = "REVIEW_M1_ORDER7_CORE_OR_HOLDOUT_UNCLOSED"
    else:
        candidate = "PASS_M1_ORDER7_PROVENANCE_CANDIDATE_ONLY"
    payload = {
        "test": "A2-K4 P5.3g7 GLOBAL_C1 M1_ORDER7_PROVENANCE_GATE",
        "run_id": RUN_ID,
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "candidate_interpretation_not_verdict": candidate,
        "identity": {"mode": MODE, "k_Mpc_inverse": K_MPC, "variant": VARIANT, "order": 7},
        "scope": {
            "included": "anchored standard M1 order-5 to order-7 provenance and full-power residual/holdout audit",
            "excluded": "CDI support step 3, Fourier C2, BI/NID/NIV, other k/variants, S-M, full hierarchy, ODE, G8/G9, BBN/CMB/CLASS/S8/H0",
        },
        "immutable_prerequisite": {"file": EXPECTED_RESULT[0], "sha256": EXPECTED_RESULT[1]},
        "dimensions": dimensions,
        "shapes_pass": shapes_pass,
        "rank_pass": rank_pass,
        "independently_recomputed_reduced_rank": independently_recomputed_rank,
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
        raise FloatingPointError("non-finite value in KMPC-036 payload")
    deadline()
    return payload
