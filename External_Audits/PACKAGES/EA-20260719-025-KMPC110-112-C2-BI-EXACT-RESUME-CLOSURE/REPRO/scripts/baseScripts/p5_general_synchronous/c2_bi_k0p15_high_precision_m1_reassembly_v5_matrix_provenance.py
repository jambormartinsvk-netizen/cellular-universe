"""Diagnostic matrix-provenance successor for the KMPC-093 HP-M1 boundary.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
This module does not claim a high-precision M1 solve.  It compares the native
80-dps affine assembly, after binary64 projection, with an independent rebuild
of the frozen binary64 M1 system.  A disclosed binary64 least-squares bridge is
used only so the unchanged downstream diagnostic path can finish.
"""

from __future__ import annotations

from contextlib import contextmanager
import hashlib
from pathlib import Path
from typing import Iterator

import mpmath as mp
import numpy as np

from . import c2_bi_k0p15_high_precision_m1_reassembly_v4_scale_fixture as v4


v3 = v4.v3
base = v3.v1
legacy = base.legacy
_V4_SOURCE_HASHES = v4.source_hashes
_V4_CONTRACT_GUARD = v4.contract_guard
_COLUMN_SOLVE = v3._column_equilibrated_solve
_PROVENANCE: dict[str, object] | None = None


def configure(**config: object) -> None:
    v4.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v4.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v4.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V4_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    name = "c2_bi_k0p15_high_precision_m1_reassembly_v5_matrix_provenance.py"
    hashes[name] = base._sha256_file(here / name)
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V4_CONTRACT_GUARD()
    guard["checks"].update({
        "hp_m1_v5_diagnostic_only": True,
        "hp_m1_v5_no_physics_pass": True,
        "hp_m1_v5_independent_float64_rebuild": True,
        "hp_m1_v5_binary64_bridge_disclosed": True,
        "hp_m1_v5_equations_support_thresholds_unchanged": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _array_sha256(*arrays: np.ndarray) -> str:
    digest = hashlib.sha256()
    for array in arrays:
        canonical = np.ascontiguousarray(array, dtype="<f8")
        digest.update(str(canonical.shape).encode("ascii"))
        digest.update(b"|")
        digest.update(canonical.tobytes(order="C"))
        digest.update(b"|")
    return digest.hexdigest().upper()


def _frozen_float64_rebuild() -> tuple[
    np.ndarray, np.ndarray, list[str], list[str], dict[str, object]
]:
    """Independently reproduce the live anchored M1 reduced system."""
    inputs = legacy.FrozenInputs()
    order = base.ORDER
    exponents = list(range(-1, order + 1))
    series = legacy.Series(-4, order + 5)
    background = legacy._standard_background(base.K_MPC, inputs, series)
    pairs = [
        (name, power)
        for name in legacy.VARS
        for power in exponents
    ]
    index = {pair: position for position, pair in enumerate(pairs)}

    def unpack(vector: np.ndarray) -> dict[str, dict[int, float]]:
        return {
            name: {
                power: float(vector[index[(name, power)]])
                for power in exponents
            }
            for name in legacy.VARS
        }

    initial = legacy._initial_constraints(
        base.MODE, inputs.radiation_weights[1], inputs.radiation_weights[0]
    )

    def ledger(vector: np.ndarray) -> np.ndarray:
        rows = legacy._standard_rows(unpack(vector), background, series)
        output = [
            series.coef(rows[row], power)
            for row in legacy.DRIVER_ROWS
            for power in exponents
        ]
        output.extend(
            vector[index[(name, power)]] - value
            for name, power, value in initial
        )
        return np.asarray(output, dtype=float)

    zero = np.zeros(len(pairs), dtype=float)
    constant = ledger(zero)
    matrix = np.empty((constant.size, len(pairs)), dtype=float)
    for column in range(len(pairs)):
        basis = np.zeros(len(pairs), dtype=float)
        basis[column] = 1.0
        matrix[:, column] = ledger(basis) - constant

    anchor_power, anchor_value = legacy._m1_expected_h(
        base.MODE, background, inputs
    )
    anchor_index = index[("h", anchor_power)]
    keep = [column for column in range(len(pairs)) if column != anchor_index]
    reduced = matrix[:, keep]
    rhs = -constant - matrix[:, anchor_index] * anchor_value
    row_labels = [
        f"{row}[{power}]"
        for row in legacy.DRIVER_ROWS
        for power in exponents
    ] + [f"initial:{name}[{power}]" for name, power, _ in initial]
    column_labels = [
        f"{name}[{power}]" for column, (name, power) in enumerate(pairs)
        if column != anchor_index
    ]
    identity = {
        "mode": base.MODE,
        "k_Mpc_inverse": base.K_MPC,
        "order": order,
        "hard_anchor": f"h[{anchor_power}]",
        "hard_anchor_value": float(anchor_value),
        "frozen_inputs": {
            "delta": inputs.delta,
            "lambda": inputs.lam,
            "h": inputs.h,
            "omega_m0": inputs.omega_m0,
            "ombh2": inputs.ombh2,
            "neff_nu": inputs.neff_nu,
            "neff_steam": inputs.neff_steam,
            "omega_gamma_h2": inputs.omega_gamma_h2,
            "A_f": inputs.af,
        },
    }
    return reduced, rhs, row_labels, column_labels, identity


def _spectrum(matrix: np.ndarray) -> tuple[int, np.ndarray, float]:
    singular = np.linalg.svd(matrix, compute_uv=False, full_matrices=False)
    rank = int(np.linalg.matrix_rank(matrix))
    condition = (
        float(singular[0] / singular[-1])
        if singular.size and singular[-1] > 0
        else float("inf")
    )
    return rank, singular, condition


def _matrix_provenance_bridge(
    matrix: list[list[mp.mpf]], rhs: list[mp.mpf]
) -> tuple[list[mp.mpf], mp.mpf]:
    """Compare assemblies and return a non-authoritative float64 bridge."""
    global _PROVENANCE
    if (len(matrix), len(matrix[0])) != base.EXPECTED_REDUCED_SHAPE:
        return _COLUMN_SOLVE(matrix, rhs)

    native = np.asarray([[float(value) for value in row] for row in matrix])
    native_rhs = np.asarray([float(value) for value in rhs], dtype=float)
    frozen, frozen_rhs, row_labels, column_labels, identity = (
        _frozen_float64_rebuild()
    )
    if native.shape != frozen.shape or native_rhs.shape != frozen_rhs.shape:
        raise RuntimeError("KMPC-097 M1 provenance shape mismatch")

    matrix_difference = native - frozen
    rhs_difference = native_rhs - frozen_rhs
    native_rank, native_singular, native_condition = _spectrum(native)
    frozen_rank, frozen_singular, frozen_condition = _spectrum(frozen)
    solution, residuals, bridge_rank, bridge_singular = np.linalg.lstsq(
        native, native_rhs, rcond=None
    )
    residual_vector = native @ solution - native_rhs
    residual_l2 = float(np.linalg.norm(residual_vector, ord=2))

    worst_matrix_flat = int(np.argmax(np.abs(matrix_difference)))
    worst_row, worst_column = np.unravel_index(
        worst_matrix_flat, matrix_difference.shape
    )
    worst_rhs_row = int(np.argmax(np.abs(rhs_difference)))
    matrix_scale = max(float(np.max(np.abs(frozen))), np.finfo(float).tiny)
    rhs_scale = max(float(np.max(np.abs(frozen_rhs))), np.finfo(float).tiny)
    matrix_norm = max(float(np.linalg.norm(frozen)), np.finfo(float).tiny)
    rhs_norm = max(float(np.linalg.norm(frozen_rhs)), np.finfo(float).tiny)
    native_column_norms = np.linalg.norm(native, axis=0)
    frozen_column_norms = np.linalg.norm(frozen, axis=0)
    native_row_norms = np.linalg.norm(native, axis=1)
    frozen_row_norms = np.linalg.norm(frozen, axis=1)
    _PROVENANCE = {
        "role": "DIAGNOSTIC_ONLY_NO_PHYSICS_VERDICT",
        "comparison": "NATIVE_80DPS_PROJECTED_TO_FLOAT64_VS_INDEPENDENT_FROZEN_FLOAT64_REBUILD",
        "identity": identity,
        "shape_native": list(native.shape),
        "shape_frozen": list(frozen.shape),
        "native_matrix_rhs_sha256": _array_sha256(native, native_rhs),
        "frozen_matrix_rhs_sha256": _array_sha256(frozen, frozen_rhs),
        "matrix_exact_float64_equal": bool(np.array_equal(native, frozen)),
        "rhs_exact_float64_equal": bool(np.array_equal(native_rhs, frozen_rhs)),
        "matrix_changed_entry_count": int(np.count_nonzero(matrix_difference)),
        "rhs_changed_entry_count": int(np.count_nonzero(rhs_difference)),
        "matrix_max_abs_difference": float(abs(matrix_difference[worst_row, worst_column])),
        "matrix_max_abs_difference_relative_to_global_scale": float(
            abs(matrix_difference[worst_row, worst_column]) / matrix_scale
        ),
        "matrix_frobenius_relative_difference": float(
            np.linalg.norm(matrix_difference) / matrix_norm
        ),
        "matrix_worst_row": row_labels[worst_row],
        "matrix_worst_column": column_labels[worst_column],
        "matrix_worst_native_value": float(native[worst_row, worst_column]),
        "matrix_worst_frozen_value": float(frozen[worst_row, worst_column]),
        "rhs_max_abs_difference": float(abs(rhs_difference[worst_rhs_row])),
        "rhs_max_abs_difference_relative_to_global_scale": float(
            abs(rhs_difference[worst_rhs_row]) / rhs_scale
        ),
        "rhs_l2_relative_difference": float(
            np.linalg.norm(rhs_difference) / rhs_norm
        ),
        "rhs_worst_row": row_labels[worst_rhs_row],
        "rhs_worst_native_value": float(native_rhs[worst_rhs_row]),
        "rhs_worst_frozen_value": float(frozen_rhs[worst_rhs_row]),
        "native_projected_rank": native_rank,
        "frozen_rank": frozen_rank,
        "expected_full_column_rank": native.shape[1],
        "native_projected_condition": native_condition,
        "frozen_condition": frozen_condition,
        "native_singular_max": float(native_singular[0]),
        "native_singular_min": float(native_singular[-1]),
        "frozen_singular_max": float(frozen_singular[0]),
        "frozen_singular_min": float(frozen_singular[-1]),
        "native_smallest_singular_values": [
            float(value) for value in native_singular[-10:]
        ],
        "frozen_smallest_singular_values": [
            float(value) for value in frozen_singular[-10:]
        ],
        "native_zero_column_count": int(np.count_nonzero(native_column_norms == 0)),
        "frozen_zero_column_count": int(np.count_nonzero(frozen_column_norms == 0)),
        "native_zero_row_count": int(np.count_nonzero(native_row_norms == 0)),
        "frozen_zero_row_count": int(np.count_nonzero(frozen_row_norms == 0)),
        "diagnostic_bridge": {
            "method": "numpy.linalg.lstsq_on_native_binary64_projection",
            "authoritative_high_precision_solve": False,
            "used_for_physics_pass": False,
            "rank": int(bridge_rank),
            "singular_min": float(bridge_singular[-1]),
            "reported_residual_sum_squares": (
                float(residuals[0]) if residuals.size else None
            ),
            "unweighted_residual_l2": residual_l2,
        },
    }
    v3._SCALE_DIAGNOSTIC = {
        "method": "DIAGNOSTIC_FLOAT64_BRIDGE_NO_COLUMN_SOLVE",
        "row_scaling_applied": False,
        "unweighted_residual_recomputed": True,
        "column_count": native.shape[1],
        "scale_min_decimal": "NOT_APPLICABLE",
        "scale_max_decimal": "NOT_APPLICABLE",
        "scale_ratio_decimal": "NOT_APPLICABLE",
        "qr_reported_residual_decimal": "NOT_APPLICABLE",
        "unweighted_residual_l2_decimal": format(residual_l2, ".17e"),
        "all_scales_finite_positive": True,
    }
    return [mp.mpf(float(value)) for value in solution], mp.mpf(residual_l2)


@contextmanager
def _overlay() -> Iterator[None]:
    global _PROVENANCE
    before = (
        v3._column_equilibrated_solve,
        v4.source_hashes,
        v4.contract_guard,
    )
    _PROVENANCE = None
    try:
        v3._column_equilibrated_solve = _matrix_provenance_bridge
        v4.source_hashes = source_hashes
        v4.contract_guard = contract_guard
        yield
    finally:
        (
            v3._column_equilibrated_solve,
            v4.source_hashes,
            v4.contract_guard,
        ) = before


def _owners_restored() -> bool:
    return bool(
        v3._column_equilibrated_solve is _COLUMN_SOLVE
        and v4.source_hashes is _V4_SOURCE_HASHES
        and v4.contract_guard is _V4_CONTRACT_GUARD
    )


def _fixture() -> dict[str, bool]:
    frozen, rhs, rows, columns, identity = _frozen_float64_rebuild()
    return {
        "frozen_rebuild_shape": frozen.shape == base.EXPECTED_REDUCED_SHAPE,
        "frozen_rebuild_rhs_shape": rhs.shape == (base.EXPECTED_REDUCED_SHAPE[0],),
        "frozen_rebuild_labels": (
            len(rows) == frozen.shape[0] and len(columns) == frozen.shape[1]
        ),
        "frozen_rebuild_identity": (
            identity["mode"] == base.MODE
            and identity["k_Mpc_inverse"] == base.K_MPC
            and identity["order"] == base.ORDER
        ),
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = v4.run_smoke(max_runtime_seconds, result_dir)
        payload["checks"].update({
            f"hp_m1_v5_{name}": value for name, value in _fixture().items()
        })
        payload["passed"] = all(payload["checks"].values())
    payload["checks"]["hp_m1_v5_owners_restored"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    with _overlay():
        payload = v4.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored() or _PROVENANCE is None:
        raise RuntimeError("KMPC-097 matrix-provenance lifecycle incomplete")
    boundary = payload["high_precision_m1_reassembly_boundary"]
    pipeline_completed = bool(boundary.get("pass"))
    boundary.update({
        "solver": "DIAGNOSTIC_BINARY64_BRIDGE_NOT_HP_M1_SOLVE",
        "high_precision_m1_solve_count": 0,
        "authoritative_high_precision_m1_solve_count": 0,
        "diagnostic_bridge_solve_count": 1,
        "diagnostic_pipeline_completed": pipeline_completed,
        "pass": False,
        "pass_c2_atom_candidate": False,
        "matrix_provenance_diagnostic": _PROVENANCE,
    })
    exact_solves = payload["high_precision_driver_assembly_boundary"][
        "total_high_precision_solve_count"
    ]
    boundary["total_high_precision_solves_including_m1"] = exact_solves
    payload["candidate_interpretation_not_verdict"] = (
        "REVIEW_C2_BI_K0p15_HP_M1_MATRIX_PROVENANCE_DIAGNOSTIC_COMPLETE"
    )
    payload["physics_verdict_role"] = "DIAGNOSTIC_ONLY"
    payload["score_effect"] = "NONE_DIAGNOSTIC_ONLY_PENDING_INTERNAL_AUDIT"
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("high-precision M1 boundary has no aggregate scope")
