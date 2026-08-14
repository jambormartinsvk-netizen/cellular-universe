"""80-dps independent-holdout boundary for C2 BI/k=.15.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
The holdout is evaluated on, but never added to, the frozen driver solve.
"""

from __future__ import annotations

from contextlib import contextmanager
import hashlib
import math
from pathlib import Path
from typing import Iterator

import mpmath as mp

from . import c2_single_atom_adapter as adapter
from . import m1_order7_numerical_refinement as numeric


legacy = adapter.legacy
physics = legacy.physics
np = physics.np
PRECISION_DPS = 80
TARGET_RANK = 104
HP_SOLVE_LIMIT = 1
_ORIGINAL_SOLVER = physics._solve_equilibrated
_ORIGINAL_HOLDOUT = physics._holdout_metrics
_ADAPTER_SOURCE_HASHES = adapter.source_hashes
_ADAPTER_CONTRACT_GUARD = adapter.contract_guard
_HP_SOLUTION: list[mp.mpf] | None = None
_HP_DRIVER: dict[str, object] | None = None
_HP_HOLDOUT: dict[str, object] | None = None
_HP_SOLVES = 0


def configure(**config: object) -> None:
    adapter.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return adapter.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return adapter.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_ADAPTER_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["m1_order7_numerical_refinement.py"] = legacy.sha256_file(
        here / "m1_order7_numerical_refinement.py"
    )
    hashes["c2_bi_k0p15_high_precision_holdout.py"] = legacy.sha256_file(
        here / "c2_bi_k0p15_high_precision_holdout.py"
    )
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _ADAPTER_CONTRACT_GUARD()
    guard["checks"].update({
        "precision_dps_exact": PRECISION_DPS == 80,
        "target_rank_exact": TARGET_RANK == 13 * 8,
        "one_high_precision_solve": HP_SOLVE_LIMIT == 1,
        "holdout_not_fit": physics.contract.AUTHORITATIVE_HOLDOUT
        == ("Einstein_00", "Einstein_0i"),
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _mp(value: float) -> mp.mpf:
    return numeric._float_to_mpf(float(value))


def _matrix_fingerprint(matrix: object, constant: object) -> str:
    digest = hashlib.sha256()
    digest.update(np.asarray(matrix, dtype=np.float64).tobytes(order="C"))
    digest.update(np.asarray(constant, dtype=np.float64).tobytes(order="C"))
    return digest.hexdigest().upper()


def _mp_metrics(
    matrix: object, constant: object, solution: list[mp.mpf],
    labels: list[str] | None, threshold: float, pass_key: str,
) -> dict[str, object]:
    rows = int(matrix.shape[0])
    relative_max = mp.mpf("0")
    absolute_max = mp.mpf("0")
    relative_worst: int | None = None
    absolute_worst: int | None = None
    relative_count = 0
    absolute_count = 0
    norm_floor = _mp(physics.ABS_FALLBACK_NORM)
    for row in range(rows):
        residual = _mp(constant[row])
        term_norm = abs(_mp(constant[row]))
        for column, x_value in enumerate(solution):
            term = _mp(matrix[row, column]) * x_value
            residual += term
            term_norm += abs(term)
        if term_norm > norm_floor:
            relative_count += 1
            metric = abs(residual) / term_norm
            if metric > relative_max:
                relative_max, relative_worst = metric, row
        else:
            absolute_count += 1
            metric = abs(residual)
            if metric > absolute_max:
                absolute_max, absolute_worst = metric, row
    passed = bool(
        relative_max <= _mp(threshold)
        and absolute_max <= _mp(physics.ABS_FALLBACK_TOL)
    )
    return {
        "precision_dps": PRECISION_DPS,
        "max_relative_residual": float(relative_max),
        "max_relative_residual_decimal": mp.nstr(relative_max, 50),
        "max_absolute_fallback_residual": float(absolute_max),
        "max_absolute_fallback_residual_decimal": mp.nstr(absolute_max, 50),
        "relative_row_count": relative_count,
        "absolute_fallback_row_count": absolute_count,
        "worst_relative_row": labels[relative_worst]
        if labels is not None and relative_worst is not None else relative_worst,
        "worst_absolute_fallback_row": labels[absolute_worst]
        if labels is not None and absolute_worst is not None else absolute_worst,
        pass_key: passed,
    }


def _high_precision_solution(matrix: object, constant: object) -> list[mp.mpf]:
    with mp.workdps(PRECISION_DPS):
        row_scale = np.maximum(
            np.maximum(np.max(np.abs(matrix), axis=1), np.abs(constant)), 1.0e-300
        )
        row_matrix = matrix / row_scale[:, np.newaxis]
        column_scale = np.maximum(np.max(np.abs(row_matrix), axis=0), 1.0e-300)
        a = mp.matrix([
            [_mp(matrix[i, j]) / _mp(row_scale[i]) / _mp(column_scale[j])
             for j in range(matrix.shape[1])]
            for i in range(matrix.shape[0])
        ])
        b = mp.matrix([
            -_mp(constant[i]) / _mp(row_scale[i]) for i in range(matrix.shape[0])
        ])
        y = mp.lu_solve(a, b)
        return [y[i] / _mp(column_scale[i]) for i in range(len(y))]


def _solve_equilibrated(
    matrix: object, constant: object, expected_rank: int,
    row_labels: list[str] | None = None, deadline=None,
):
    global _HP_SOLUTION, _HP_DRIVER, _HP_SOLVES
    solution, metadata = _ORIGINAL_SOLVER(
        matrix, constant, expected_rank, row_labels=row_labels, deadline=deadline
    )
    if expected_rank != TARGET_RANK:
        return solution, metadata
    if _HP_SOLVES >= HP_SOLVE_LIMIT:
        raise RuntimeError("more than one high-precision solve requested")
    _HP_SOLVES += 1
    with mp.workdps(PRECISION_DPS):
        hp_solution = _high_precision_solution(matrix, constant)
        hp_driver = _mp_metrics(
            matrix, constant, hp_solution, row_labels,
            physics.DRIVER_TOL, "pass_driver",
        )
    hp_driver.update({
        "matrix_identity": "EXACT_SAME_FLOAT64_ASSEMBLED_MATRIX_AND_CONSTANT",
        "matrix_constant_sha256": _matrix_fingerprint(matrix, constant),
        "shape": list(matrix.shape),
        "holdout_rows_added_to_solve": 0,
        "solver": "mpmath.lu_solve",
        "float64_baseline": {
            "max_relative_residual": metadata["max_relative_residual"],
            "max_absolute_fallback_residual": metadata[
                "max_absolute_fallback_residual"
            ],
        },
    })
    _HP_SOLUTION, _HP_DRIVER = hp_solution, hp_driver
    enriched = dict(metadata)
    enriched["high_precision_boundary"] = hp_driver
    if deadline is not None:
        deadline()
    return solution, enriched


def _holdout_metrics(matrix, constant, solution, labels=None):
    global _HP_HOLDOUT
    base = _ORIGINAL_HOLDOUT(matrix, constant, solution, labels)
    if _HP_SOLUTION is None or matrix.shape[1] != TARGET_RANK:
        return base
    with mp.workdps(PRECISION_DPS):
        hp = _mp_metrics(
            matrix, constant, _HP_SOLUTION, labels,
            physics.HOLDOUT_TOL, "pass_holdout",
        )
    hp.update({
        "matrix_role": "INDEPENDENT_HOLDOUT_NOT_FIT",
        "matrix_constant_sha256": _matrix_fingerprint(matrix, constant),
        "rows_added_to_driver_solve": 0,
        "float64_baseline": dict(base),
    })
    _HP_HOLDOUT = hp
    enriched = dict(base)
    enriched["high_precision_boundary"] = hp
    return enriched


@contextmanager
def _overlay() -> Iterator[None]:
    global _HP_SOLUTION, _HP_DRIVER, _HP_HOLDOUT, _HP_SOLVES
    before = (physics._solve_equilibrated, physics._holdout_metrics,
              adapter.source_hashes, adapter.contract_guard)
    _HP_SOLUTION = _HP_DRIVER = _HP_HOLDOUT = None
    _HP_SOLVES = 0
    try:
        physics._solve_equilibrated = _solve_equilibrated
        physics._holdout_metrics = _holdout_metrics
        adapter.source_hashes = source_hashes
        adapter.contract_guard = contract_guard
        yield
    finally:
        (physics._solve_equilibrated, physics._holdout_metrics,
         adapter.source_hashes, adapter.contract_guard) = before


def _owners_restored() -> bool:
    return bool(
        physics._solve_equilibrated is _ORIGINAL_SOLVER
        and physics._holdout_metrics is _ORIGINAL_HOLDOUT
        and adapter.source_hashes is _ADAPTER_SOURCE_HASHES
        and adapter.contract_guard is _ADAPTER_CONTRACT_GUARD
    )


def _fixture() -> dict[str, object]:
    matrix = np.diag(np.array([1.0, 2.0, 4.0], dtype=float))
    constant = np.array([-1.0, 4.0, -12.0], dtype=float)
    with mp.workdps(PRECISION_DPS):
        solution = _high_precision_solution(matrix, constant)
        metrics = _mp_metrics(matrix, constant, solution, ["a", "b", "c"],
                              physics.DRIVER_TOL, "pass_driver")
    exact = all(abs(solution[i] - _mp(value)) <= mp.mpf("1e-70")
                for i, value in enumerate((1.0, -2.0, 3.0)))
    bridge = _mp(0.1) == mp.mpf(0.1.as_integer_ratio()[0]) / 0.1.as_integer_ratio()[1]
    return {"exact_solution": bool(exact), "driver_pass": metrics["pass_driver"],
            "exact_float_bridge": bool(bridge), "precision_exact": mp.mp.dps != PRECISION_DPS}


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = adapter.run_smoke(max_runtime_seconds, result_dir)
        fixture = _fixture()
        payload["checks"].update({f"hp_{key}": value for key, value in fixture.items()})
        payload["passed"] = all(payload["checks"].values())
    payload["checks"]["owners_restored"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(mode: str, k_mpc: float, max_runtime_seconds: float,
             result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = adapter.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored() or _HP_DRIVER is None or _HP_HOLDOUT is None:
        raise RuntimeError("high-precision boundary lifecycle incomplete")
    false_checks = sorted(
        name for name, value in payload["audit_solve"]["checks"].items() if not value
    )
    other_gates = bool(
        payload["M1"]["pass"] and payload["common_pass"] and payload["tail_pass"]
        and payload["background_guard"]["pass"] and payload["S_C0_actual_guard"]["pass"]
        and false_checks == ["M3_independent_00_0i_holdout"]
    )
    boundary_pass = bool(
        _HP_SOLVES == 1 and _HP_DRIVER["pass_driver"]
        and _HP_HOLDOUT["pass_holdout"] and other_gates
    )
    payload["high_precision_holdout_boundary"] = {
        "precision_dps": PRECISION_DPS,
        "high_precision_solve_count": _HP_SOLVES,
        "driver": _HP_DRIVER,
        "holdout": _HP_HOLDOUT,
        "float64_false_checks": false_checks,
        "all_other_frozen_gates_pass": other_gates,
        "pass": boundary_pass,
        "scope": "SOLVE_AND_EVALUATION_ROUNDOFF_OF_FLOAT64_ASSEMBLED_SYSTEM",
    }
    payload["core_pass_high_precision_boundary"] = boundary_pass
    payload["candidate_interpretation_not_verdict"] = (
        "PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY"
        if boundary_pass else "REVIEW_C2_BI_K0p15_EXACT_ASSEMBLY_REQUIRED"
    )
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("high-precision holdout boundary has no aggregate scope")
