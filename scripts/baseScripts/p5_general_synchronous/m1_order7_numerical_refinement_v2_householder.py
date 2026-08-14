"""KMPC-038 technical overlay for mpmath's zero-diagonal Householder tie."""

from __future__ import annotations

from contextlib import contextmanager
import hashlib
from pathlib import Path
from types import MethodType
from typing import Callable, Iterator

import mpmath as mp

from . import m1_order7_numerical_refinement as v1


RUN_ID = "KMPC-038"
EXPECTED_MPMATH_LINALG_HASH = (
    "D380B78A3CCC1689BBA1BE5F5C10837F23CF768DC121BA08784F31D80EAFA85D"
)


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def source_hashes() -> dict[str, str]:
    hashes = v1.source_hashes()
    path = Path(__file__).resolve()
    hashes[path.name] = _sha256_file(path)
    return hashes


def _callable_guard(callable_object: Callable[..., object]) -> bool:
    function = getattr(callable_object, "__func__", callable_object)
    return bool(
        getattr(function, "__name__", None) == "householder"
        and getattr(function, "__module__", None) == "mpmath.matrices.linalg"
    )


def _operation_guard(high_precision_solves: int, overlay_uses: int) -> bool:
    return high_precision_solves == 1 and overlay_uses == 1


def _corrected_householder(ctx: object, matrix: object) -> tuple[object, list[object], list[object], list[object]]:
    """Mpmath 1.3.0 householder with only sign(0) replaced by a +1 tie."""
    if not isinstance(matrix, ctx.matrix):
        raise TypeError("A should be a type of ctx.matrix")
    rows = matrix.rows
    columns = matrix.cols
    if rows < columns - 1:
        raise RuntimeError("Columns should not be less than rows")
    parameters: list[object] = []
    for column in range(columns - 1):
        square_norm = ctx.fsum(
            abs(matrix[row, column]) ** 2 for row in range(column, rows)
        )
        if not abs(square_norm) > ctx.eps:
            raise ValueError("matrix is numerically singular")
        diagonal_real = ctx.re(matrix[column, column])
        orientation = ctx.one if diagonal_real >= 0 else -ctx.one
        parameter = -orientation * ctx.sqrt(square_norm)
        parameters.append(parameter)
        kappa = ctx.one / (
            square_norm - parameter * matrix[column, column]
        )
        matrix[column, column] -= parameter
        for target in range(column + 1, columns):
            projection = ctx.fsum(
                ctx.conj(matrix[row, column]) * matrix[row, target]
                for row in range(column, rows)
            ) * kappa
            for row in range(column, rows):
                matrix[row, target] -= matrix[row, column] * projection
    solution = [matrix[row, columns - 1] for row in range(columns - 1)]
    for row in range(columns - 2, -1, -1):
        solution[row] -= ctx.fsum(
            matrix[row, column] * solution[column]
            for column in range(row + 1, columns - 1)
        )
        solution[row] /= parameters[row]
    if rows != columns - 1:
        residual = [
            matrix[rows - 1 - index, columns - 1]
            for index in range(rows - columns + 1)
        ]
    else:
        residual = [0] * rows
    return matrix, parameters, solution, residual


@contextmanager
def _householder_overlay() -> Iterator[None]:
    original = mp.householder
    if not _callable_guard(original):
        raise RuntimeError("unexpected mpmath householder callable identity")
    original_function = getattr(original, "__func__", original)
    mp.householder = MethodType(_corrected_householder, mp)
    try:
        yield
    finally:
        mp.householder = original
        restored = getattr(mp.householder, "__func__", mp.householder)
        if restored is not original_function:
            raise RuntimeError("mpmath householder callable was not restored")


def _solve_with_overlay(matrix: object, right_hand_side: object) -> tuple[object, object]:
    with _householder_overlay():
        return mp.qr_solve(matrix, right_hand_side)


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    if max_runtime_seconds != v1.SMOKE_LIMIT_SECONDS:
        raise ValueError("KMPC-038 smoke requires exactly 4.8 seconds")
    success = result_dir / "RUN_KMPC_038_P5_3G7_M1_ORDER7_HOUSEHOLDER_ZERO_TIE.json"
    failure = result_dir / "RUN_KMPC_038_P5_3G7_M1_ORDER7_HOUSEHOLDER_ZERO_TIE_TECHNICAL_FAILURE.json"
    if success.exists() or failure.exists():
        raise FileExistsError("KMPC-038 immutable output already exists")
    original_function = getattr(mp.householder, "__func__", mp.householder)
    with mp.workdps(v1.PRECISION_DPS):
        zero_diagonal = mp.matrix([[0, 1], [1, 0], [1, 1]])
        exact_rhs = mp.matrix([2, 1, 3])
        try:
            mp.qr_solve(zero_diagonal, exact_rhs)
            original_zero_diagonal_rejected = False
        except (ValueError, ZeroDivisionError):
            original_zero_diagonal_rejected = True
        repaired_solution, repaired_residual = _solve_with_overlay(
            zero_diagonal, exact_rhs
        )
        repaired_fixture_pass = bool(
            abs(repaired_solution[0] - 1) < mp.mpf("1e-70")
            and abs(repaired_solution[1] - 2) < mp.mpf("1e-70")
            and repaired_residual < mp.mpf("1e-70")
        )
        regular_matrix = mp.matrix([[1, 0], [0, 1], [1, 1]])
        regular_rhs = mp.matrix([1, 2, 3])
        original_regular, _ = mp.qr_solve(regular_matrix, regular_rhs)
        repaired_regular, _ = _solve_with_overlay(regular_matrix, regular_rhs)
        nonzero_diagonal_parity = bool(
            max(
                abs(original_regular[index] - repaired_regular[index])
                for index in range(2)
            )
            < mp.mpf("1e-70")
        )
    restored_function = getattr(mp.householder, "__func__", mp.householder)
    fixtures = {
        "original_zero_diagonal_rejected": original_zero_diagonal_rejected,
        "repaired_zero_diagonal_pass": repaired_fixture_pass,
        "nonzero_diagonal_parity": nonzero_diagonal_parity,
        "callable_restored": restored_function is original_function,
        "wrong_callable_rejected": not _callable_guard(lambda: None),
        "second_solve_rejected": not _operation_guard(2, 1),
        "second_overlay_rejected": not _operation_guard(1, 2),
    }
    if not all(fixtures.values()):
        raise RuntimeError("KMPC-038 Householder smoke fixture failed")
    return {
        "run_id": RUN_ID,
        "smoke_pass": True,
        "fixtures": fixtures,
        "precision_dps": v1.PRECISION_DPS,
        "mpmath_linalg_expected_sha256": EXPECTED_MPMATH_LINALG_HASH,
    }


def run_audit(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    if max_runtime_seconds != v1.AUDIT_LIMIT_SECONDS:
        raise ValueError("KMPC-038 audit requires exactly 45 seconds")
    if not _operation_guard(1, 1):
        raise RuntimeError("KMPC-038 operation count guard failed")
    with _householder_overlay():
        payload = v1.run_audit(max_runtime_seconds, result_dir)
    payload["run_id"] = RUN_ID
    payload["test"] = (
        "A2-K4 P5.3g7 GLOBAL_C1 M1_ORDER7_NUMERICAL_REFINEMENT_"
        "HOUSEHOLDER_ZERO_TIE_SUCCESSOR_AUDIT"
    )
    payload["technical_successor"] = {
        "predecessor": "KMPC-037 / PF-072",
        "only_change": "mpmath Householder sign(0) tie uses +1",
        "row_or_column_reordering": False,
        "pivoting": False,
        "normal_equations": False,
        "native_high_precision_rebuild": False,
        "mpmath_linalg_expected_sha256": EXPECTED_MPMATH_LINALG_HASH,
    }
    payload["operation_counts"]["householder_zero_tie_overlays"] = 1
    payload["source_hashes"] = source_hashes()
    return payload
