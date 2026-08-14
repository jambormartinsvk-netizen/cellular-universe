"""BI same-matrix numerical boundary audit for KMPC-044."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import time
from typing import Callable, Mapping

import mpmath as mp
import numpy as np

from . import bi_m1_order7_provenance as provenance
from . import m1_order7_numerical_refinement as numeric
from . import m1_order7_numerical_refinement_v2_householder as householder
from . import m1_order7_numerical_refinement_v3_context_owner as context_owner
from . import mode_resolved_puiseux as v1


RUN_ID = "KMPC-044"
PRECISION_DPS = 80
REFINEMENT_LIMIT = 1
HIGH_PRECISION_SOLVE_LIMIT = 1
CORRECTION_ABS_MAX = 1.0e-14
SMOKE_LIMIT_SECONDS = 12.0
AUDIT_LIMIT_SECONDS = 45.0
EXPECTED_KMPC043 = (
    "RUN_KMPC_043_P5_3G7_BI_M1_ORDER7_PROVENANCE_GATE.json",
    "B02D1D16CFAE4331378B68F12258142F84A424419BB9D3A52AAEE87D0CC61EB0",
)
EXPECTED_OPEN_DRIVER = (
    "gamma_Euler[7]",
    "fs_Euler[6]",
    "fs_Euler[7]",
    "cdm_continuity[7]",
    "tight_coupling[7]",
)
EXPECTED_OPEN_HOLDOUT = ("Einstein_0i[7]",)
METHOD_DEPENDENCIES = (
    "mode_resolved_puiseux.py",
    "mode_resolved_puiseux_v2_m1_anchored.py",
    "m1_order7_provenance.py",
    "bi_m1_order7_provenance.py",
    "m1_order7_numerical_refinement.py",
    "m1_order7_numerical_refinement_v2_householder.py",
    "m1_order7_numerical_refinement_v3_context_owner.py",
    "bi_m1_order7_numerical_boundary.py",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def source_hashes() -> dict[str, str]:
    root = Path(__file__).resolve().parent
    return {name: sha256_file(root / name) for name in METHOD_DEPENDENCIES}


def _deadline(limit: float, expected: float) -> tuple[float, Callable[[], None]]:
    if not math.isfinite(limit) or limit != expected:
        raise ValueError(f"KMPC-044 runtime must be exactly {expected} seconds")
    started = time.monotonic()

    def check() -> None:
        if time.monotonic() - started > limit:
            raise TimeoutError("KMPC-044 internal deadline exceeded")

    return started, check


def _load_reference(result_dir: Path) -> tuple[dict[str, object], str]:
    path = result_dir / EXPECTED_KMPC043[0]
    observed = sha256_file(path)
    if observed != EXPECTED_KMPC043[1]:
        raise RuntimeError("immutable KMPC-043 prerequisite hash mismatch")
    return json.loads(path.read_text(encoding="utf-8")), observed


def _open_labels(metrics: Mapping[str, object]) -> tuple[str, ...]:
    rows = metrics["rows"]
    if not isinstance(rows, list):
        raise TypeError("residual rows must be a list")
    return tuple(str(row["label"]) for row in rows if not bool(row["pass"]))


def _fixture_guard(
    mode: str,
    precision_dps: int,
    refinements: int,
    hp_solves: int,
    relative_tolerance: float,
    states: tuple[str, ...],
    powers: tuple[int, ...],
    anchor: str,
    driver_labels: tuple[str, ...],
    holdout_labels: tuple[str, ...],
) -> bool:
    inputs = v1.FrozenInputs()
    expected_driver = tuple(
        [f"{row}[{power}]" for row in v1.DRIVER_ROWS for power in range(-1, 8)]
        + [
            f"initial:{name}[{power}]"
            for name, power, _ in v1._initial_constraints(
                provenance.MODE,
                inputs.radiation_weights[1],
                inputs.radiation_weights[0],
            )
        ]
    )
    expected_holdout = tuple(
        f"{row}[{power}]" for row in v1.HOLDOUT_ROWS for power in range(-1, 8)
    )
    return bool(
        mode == provenance.MODE
        and precision_dps == PRECISION_DPS
        and refinements == REFINEMENT_LIMIT
        and hp_solves == HIGH_PRECISION_SOLVE_LIMIT
        and relative_tolerance == provenance.REL_TOL
        and states == tuple(v1.VARS)
        and powers == tuple(range(-1, 8))
        and anchor == "h[1]"
        and driver_labels == expected_driver
        and holdout_labels == expected_holdout
        and len(set(driver_labels)) == len(driver_labels)
        and len(set(holdout_labels)) == len(holdout_labels)
    )


def _exact_matrix_qr_lifecycle(
    reduced_matrix: np.ndarray, right_hand_side: np.ndarray
) -> dict[str, object]:
    module_owner = householder.mp
    with mp.workdps(PRECISION_DPS):
        mp_matrix = mp.matrix(
            [
                [numeric._float_to_mpf(float(value)) for value in row]
                for row in reduced_matrix
            ]
        )
        mp_rhs = mp.matrix(
            [numeric._float_to_mpf(float(value)) for value in right_hand_side]
        )
        with context_owner._context_owner_bridge():
            solution, residual = householder._solve_with_overlay(mp_matrix, mp_rhs)
        solution_finite = all(mp.isfinite(value) for value in solution)
        residual_finite = mp.isfinite(residual)
    return {
        "exact_matrix_shape": list(reduced_matrix.shape),
        "solution_size": len(solution),
        "solution_finite": bool(solution_finite),
        "residual_finite": bool(residual_finite),
        "module_owner_restored": householder.mp is module_owner,
        "context_owner_guard": context_owner._owner_guard(mp, mp.mp),
        "pass": bool(
            list(reduced_matrix.shape) == [121, 98]
            and len(solution) == 98
            and solution_finite
            and residual_finite
            and householder.mp is module_owner
            and context_owner._owner_guard(mp, mp.mp)
        ),
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    started, deadline = _deadline(max_runtime_seconds, SMOKE_LIMIT_SECONDS)
    success = result_dir / "RUN_KMPC_044_P5_3G7_BI_M1_ORDER7_NUMERICAL_BOUNDARY.json"
    failure = result_dir / "RUN_KMPC_044_P5_3G7_BI_M1_ORDER7_NUMERICAL_BOUNDARY_TECHNICAL_FAILURE.json"
    if success.exists() or failure.exists():
        raise FileExistsError("KMPC-044 immutable output already exists")
    reference, observed_hash = _load_reference(result_dir)
    inputs = v1.FrozenInputs()
    system = provenance._affine_system(provenance.ORDER_AUDIT, inputs, deadline)
    powers = tuple(system["powers"])
    driver_labels = tuple(system["driver_labels"])
    holdout_labels = tuple(system["holdout_labels"])
    args = (
        provenance.MODE,
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
        "wrong_mode_CDI_rejected": not _fixture_guard("CDI", *args[1:]),
        "wrong_dps_rejected": not _fixture_guard(args[0], 60, *args[2:]),
        "second_refinement_rejected": not _fixture_guard(*args[:2], 2, *args[3:]),
        "second_hp_solve_rejected": not _fixture_guard(*args[:3], 2, *args[4:]),
        "changed_threshold_rejected": not _fixture_guard(*args[:4], 1.0e-9, *args[5:]),
        "reordered_state_rejected": not _fixture_guard(*args[:5], tuple(reversed(v1.VARS)), *args[6:]),
        "missing_power7_rejected": not _fixture_guard(*args[:6], powers[:-1], *args[7:]),
        "missing_anchor_rejected": not _fixture_guard(*args[:7], "", *args[8:]),
        "missing_driver_rejected": not _fixture_guard(*args[:8], driver_labels[:-1], args[9]),
        "duplicate_holdout_rejected": not _fixture_guard(*args[:9], holdout_labels[:-1] + (holdout_labels[-2],)),
        "wrong_prerequisite_hash_rejected": observed_hash != "0" * 64,
    }
    full_matrix = system["driver_matrix"]
    full_constant = system["driver_constant"]
    anchor_index = int(system["anchor_index"])
    anchor_value = float(system["anchor_value"])
    reduced_matrix = np.delete(full_matrix, anchor_index, axis=1)
    right_hand_side = -full_constant - full_matrix[:, anchor_index] * anchor_value
    lifecycle = _exact_matrix_qr_lifecycle(reduced_matrix, right_hand_side)
    checks = {
        "canonical_BI_fixture": canonical,
        "negative_fixtures": all(negative.values()),
        "immutable_hash": observed_hash == EXPECTED_KMPC043[1],
        "immutable_identity": reference["identity"]
        == {"mode": "BI", "k_Mpc_inverse": 0.05, "variant": "nominal", "order": 7},
        "immutable_open_driver": _open_labels(reference["driver_and_initial_full_power"])
        == EXPECTED_OPEN_DRIVER,
        "immutable_open_holdout": _open_labels(reference["holdout_full_power"])
        == EXPECTED_OPEN_HOLDOUT,
        "exact_matrix_qr_lifecycle": lifecycle["pass"],
    }
    deadline()
    if not all(checks.values()):
        raise RuntimeError("KMPC-044 exact-matrix smoke fixture failed")
    return {
        "run_id": RUN_ID,
        "smoke_pass": True,
        "checks": checks,
        "negative_fixtures": negative,
        "exact_matrix_qr_lifecycle": lifecycle,
        "precision_dps": PRECISION_DPS,
        "runtime_seconds": time.monotonic() - started,
    }


def run_audit(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    started, deadline = _deadline(max_runtime_seconds, AUDIT_LIMIT_SECONDS)
    reference, observed_hash = _load_reference(result_dir)
    reference_state = numeric._state_from_json(reference["M1_order7_state"])
    inputs = v1.FrozenInputs()
    system = provenance._affine_system(provenance.ORDER_AUDIT, inputs, deadline)
    full_matrix = system["driver_matrix"]
    full_constant = system["driver_constant"]
    anchor_index = int(system["anchor_index"])
    anchor_value = float(system["anchor_value"])
    reduced_matrix = np.delete(full_matrix, anchor_index, axis=1)
    right_hand_side = -full_constant - full_matrix[:, anchor_index] * anchor_value
    reference_vector = provenance.reference._vector_from_state(
        reference_state, system["pairs"]
    )
    reference_reduced = np.delete(reference_vector, anchor_index)

    v0_driver = provenance.reference._residual_metrics(
        full_matrix, full_constant, reference_vector, system["driver_labels"]
    )
    v0_holdout = provenance.reference._residual_metrics(
        system["holdout_matrix"],
        system["holdout_constant"],
        reference_vector,
        system["holdout_labels"],
    )
    v0_driver_regression = numeric._row_regression(
        v0_driver, reference["driver_and_initial_full_power"]
    )
    v0_holdout_regression = numeric._row_regression(
        v0_holdout, reference["holdout_full_power"]
    )
    rank = int(np.linalg.matrix_rank(reduced_matrix))
    v0_pass = bool(
        observed_hash == EXPECTED_KMPC043[1]
        and reference["identity"]
        == {"mode": "BI", "k_Mpc_inverse": 0.05, "variant": "nominal", "order": 7}
        and list(full_matrix.shape) == [121, 99]
        and list(reduced_matrix.shape) == [121, 98]
        and list(system["holdout_matrix"].shape) == [18, 99]
        and rank == 98
        and tuple(system["powers"]) == tuple(range(-1, 8))
        and numeric._state_parity(reference_state)
        and system["anchor_power"] == 1
        and system["pairs"][anchor_index] == ("h", 1)
        and reference["M1_order7_metadata"]["hard_anchor_variable"] == "h[1]"
        and float(reference["M1_order7_metadata"]["hard_anchor_absolute_difference"]) == 0.0
        and v0_driver_regression["pass"]
        and v0_holdout_regression["pass"]
        and _open_labels(v0_driver) == EXPECTED_OPEN_DRIVER
        and _open_labels(v0_holdout) == EXPECTED_OPEN_HOLDOUT
    )
    if not v0_pass:
        return {
            "test": "A2-K4 P5.3g7 BI M1 order-7 same-matrix numerical boundary",
            "run_id": RUN_ID,
            "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
            "candidate_interpretation_not_verdict": "REVIEW_BI_M1_ORDER7_REFERENCE_OR_REGRESSION_UNCLOSED",
            "identity": reference.get("identity"),
            "immutable_prerequisite": {"file": EXPECTED_KMPC043[0], "sha256": observed_hash},
            "v0": {
                "pass": False,
                "driver_regression": v0_driver_regression,
                "holdout_regression": v0_holdout_regression,
                "open_driver_rows": list(_open_labels(v0_driver)),
                "open_holdout_rows": list(_open_labels(v0_holdout)),
            },
            "source_hashes": source_hashes(),
            "score_effect": "NONE",
            "release_trigger": "NONE",
            "zenodo_trigger": "NONE",
            "prediction_table_effect": "NONE",
            "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
        }

    v1_diagnostics = numeric._float64_diagnostics(
        reduced_matrix, right_hand_side, reference_reduced
    )
    v1_invariants = {
        "driver_and_initial": numeric._residual_invariants(v0_driver),
        "holdout": numeric._residual_invariants(v0_holdout),
    }
    residual = reduced_matrix @ reference_reduced - right_hand_side
    correction, _, correction_rank, correction_singular = np.linalg.lstsq(
        reduced_matrix, -residual, rcond=None
    )
    refined_reduced = reference_reduced + correction
    refined_full = numeric._full_from_reduced(
        refined_reduced, anchor_index, anchor_value, full_matrix.shape[1]
    )
    v2_driver = provenance.reference._residual_metrics(
        full_matrix, full_constant, refined_full, system["driver_labels"]
    )
    v2_holdout = provenance.reference._residual_metrics(
        system["holdout_matrix"],
        system["holdout_constant"],
        refined_full,
        system["holdout_labels"],
    )
    refined_state = numeric._unpack_vector(refined_full, system["pairs"])
    v2_lower = provenance.reference._hybrid_regression(
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

    module_owner = householder.mp
    with mp.workdps(PRECISION_DPS):
        mp_matrix = mp.matrix(
            [[numeric._float_to_mpf(float(value)) for value in row] for row in reduced_matrix]
        )
        mp_rhs = mp.matrix(
            [numeric._float_to_mpf(float(value)) for value in right_hand_side]
        )
        with context_owner._context_owner_bridge():
            mp_solution, mp_qr_residual = householder._solve_with_overlay(
                mp_matrix, mp_rhs
            )
        hp_reduced = [mp_solution[index] for index in range(len(mp_solution))]
        hp_full: list[mp.mpf] = []
        reduced_index = 0
        for column in range(full_matrix.shape[1]):
            if column == anchor_index:
                hp_full.append(numeric._float_to_mpf(anchor_value))
            else:
                hp_full.append(hp_reduced[reduced_index])
                reduced_index += 1
        v3_driver = numeric._mp_residual_metrics(
            full_matrix, full_constant, hp_full, system["driver_labels"]
        )
        v3_holdout = numeric._mp_residual_metrics(
            system["holdout_matrix"],
            system["holdout_constant"],
            hp_full,
            system["holdout_labels"],
        )
        hp_difference_max = max(
            abs(hp_reduced[index] - numeric._float_to_mpf(float(reference_reduced[index])))
            for index in range(reference_reduced.size)
        )
        hp_qr_residual_decimal = mp.nstr(mp_qr_residual, 30)
        hp_difference_max_decimal = mp.nstr(hp_difference_max, 30)
        hp_projected = np.asarray([float(value) for value in hp_full], dtype=float)
    if householder.mp is not module_owner:
        raise RuntimeError("KMPC-044 mpmath module owner was not restored")
    deadline()

    v3_projected_driver = provenance.reference._residual_metrics(
        full_matrix, full_constant, hp_projected, system["driver_labels"]
    )
    v3_projected_holdout = provenance.reference._residual_metrics(
        system["holdout_matrix"],
        system["holdout_constant"],
        hp_projected,
        system["holdout_labels"],
    )
    hp_state = numeric._unpack_vector(hp_projected, system["pairs"])
    v3_lower = provenance.reference._hybrid_regression(
        reference_state, hp_state, tuple(range(-1, 6))
    )
    v3_bounds_pass = bool(
        float(hp_difference_max) <= CORRECTION_ABS_MAX
        and v3_lower["pass"]
        and hp_projected[anchor_index] == anchor_value
        and v3_holdout["pass"]
        and v3_projected_holdout["pass"]
    )
    v2_closed = bool(v2_driver["pass"] and v2_holdout["pass"])
    v3_closed = bool(
        v3_driver["pass"]
        and v3_holdout["pass"]
        and v3_projected_driver["pass"]
        and v3_projected_holdout["pass"]
    )
    if not v2_bounds_pass or not v3_bounds_pass:
        candidate = "REVIEW_BI_M1_ORDER7_REFINEMENT_OUT_OF_BOUNDS"
    elif v2_closed and v3_closed:
        candidate = "PASS_BI_M1_ORDER7_FLOAT64_SOLVER_FLOOR_CANDIDATE_ONLY"
    elif v3_closed:
        candidate = "PASS_BI_M1_ORDER7_FLOAT64_ROUNDING_FLOOR_CANDIDATE_ONLY"
    else:
        candidate = "REVIEW_BI_M1_ORDER7_SAME_MATRIX_BOUNDARY_UNCLOSED"

    payload = {
        "test": "A2-K4 P5.3g7 GLOBAL_C1 BI_M1_ORDER7_NUMERICAL_BOUNDARY_CLOSURE",
        "run_id": RUN_ID,
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "candidate_interpretation_not_verdict": candidate,
        "identity": reference["identity"],
        "scope": {
            "included": "same frozen KMPC-043 BI float64 matrix/RHS: V0, V1, one V2 correction, one V3 80-dps QR solve",
            "excluded": "CDI JSON/state/correction, native rebuild, BI support [0,7], tail, [0,9], NID/NIV, other k/variants, S-M, ODE, P5.4, G8/G9",
        },
        "immutable_prerequisite": {"file": EXPECTED_KMPC043[0], "sha256": observed_hash},
        "dimensions": {"full": list(full_matrix.shape), "reduced": list(reduced_matrix.shape), "rank": rank},
        "v0": {
            "pass": v0_pass,
            "driver_regression": v0_driver_regression,
            "holdout_regression": v0_holdout_regression,
            "reference_open_driver_rows": list(_open_labels(v0_driver)),
            "reference_open_holdout_rows": list(_open_labels(v0_holdout)),
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
            "diagnostics_after": numeric._float64_diagnostics(
                reduced_matrix, right_hand_side, refined_reduced
            ),
        },
        "v3_same_float64_matrix_high_precision": {
            "high_precision_solve_count": 1,
            "method": "owner-corrected mpmath Householder QR least squares",
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
        "operation_counts": {
            "refinements": 1,
            "high_precision_solves": 1,
            "householder_zero_tie_overlays": 1,
            "context_owner_bridges": 1,
            "native_rebuilds": 0,
        },
        "source_hashes": source_hashes(),
        "environment": numeric._environment(),
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "score_effect": "NONE",
        "release_trigger": "NONE",
        "zenodo_trigger": "NONE",
        "prediction_table_effect": "NONE",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }
    if not provenance._all_finite(payload):
        raise FloatingPointError("non-finite value in KMPC-044 payload")
    deadline()
    return payload
