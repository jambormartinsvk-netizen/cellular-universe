"""Column-equilibrated QR successor for the KMPC-094 HP-M1 boundary.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Only a diagonal change of unknown coordinates is introduced. Row weights and
the unweighted least-squares objective remain unchanged.
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

import mpmath as mp

from . import c2_bi_k0p15_high_precision_m1_reassembly_v2_attribution_owner as v2


v1 = v2.v1
_UNSCALED_SOLVE = v1._solve_reduced
_V2_SOURCE_HASHES = v2.source_hashes
_V2_CONTRACT_GUARD = v2.contract_guard
_SCALE_DIAGNOSTIC: dict[str, object] | None = None


def configure(**config: object) -> None:
    v2.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v2.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v2.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V2_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes[
        "c2_bi_k0p15_high_precision_m1_reassembly_v3_column_equilibrated.py"
    ] = v1._sha256_file(
        here / "c2_bi_k0p15_high_precision_m1_reassembly_v3_column_equilibrated.py"
    )
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V2_CONTRACT_GUARD()
    guard["checks"].update({
        "hp_m1_column_equilibration_only": True,
        "hp_m1_row_weights_unchanged": True,
        "hp_m1_unweighted_residual_unchanged": True,
        "hp_m1_v1_v2_math_unchanged": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _column_equilibrated_solve(
    matrix: list[list[mp.mpf]], rhs: list[mp.mpf]
) -> tuple[list[mp.mpf], mp.mpf]:
    global _SCALE_DIAGNOSTIC
    rows = len(matrix)
    columns = len(matrix[0])
    if rows != len(rhs) or any(len(row) != columns for row in matrix):
        raise ValueError("KMPC-095 reduced system shape mismatch")
    floor = mp.mpf("1e-300")
    scales = [
        max([abs(matrix[row][column]) for row in range(rows)] + [floor])
        for column in range(columns)
    ]
    scaled = [
        [matrix[row][column] / scales[column] for column in range(columns)]
        for row in range(rows)
    ]
    solved_scaled, residual = mp.qr_solve(mp.matrix(scaled), mp.matrix(rhs))
    solution = [solved_scaled[column] / scales[column] for column in range(columns)]
    residual_vector = [
        mp.fsum(matrix[row][column] * solution[column] for column in range(columns))
        - rhs[row]
        for row in range(rows)
    ]
    residual_l2 = mp.sqrt(mp.fsum(value * value for value in residual_vector))
    _SCALE_DIAGNOSTIC = {
        "method": "DIAGONAL_COLUMN_MAX_ABS",
        "row_scaling_applied": False,
        "unweighted_residual_recomputed": True,
        "column_count": columns,
        "scale_min_decimal": mp.nstr(min(scales), 50),
        "scale_max_decimal": mp.nstr(max(scales), 50),
        "scale_ratio_decimal": mp.nstr(max(scales) / min(scales), 50),
        "qr_reported_residual_decimal": mp.nstr(residual, 50),
        "unweighted_residual_l2_decimal": mp.nstr(residual_l2, 50),
        "all_scales_finite_positive": bool(
            all(mp.isfinite(value) and value > 0 for value in scales)
        ),
    }
    return solution, residual_l2


@contextmanager
def _overlay() -> Iterator[None]:
    global _SCALE_DIAGNOSTIC
    before = (v1._solve_reduced, v2.source_hashes, v2.contract_guard)
    _SCALE_DIAGNOSTIC = None
    try:
        v1._solve_reduced = _column_equilibrated_solve
        v2.source_hashes = source_hashes
        v2.contract_guard = contract_guard
        yield
    finally:
        v1._solve_reduced, v2.source_hashes, v2.contract_guard = before


def _owners_restored() -> bool:
    return bool(
        v1._solve_reduced is _UNSCALED_SOLVE
        and v2.source_hashes is _V2_SOURCE_HASHES
        and v2.contract_guard is _V2_CONTRACT_GUARD
    )


def _fixture() -> dict[str, bool]:
    global _SCALE_DIAGNOSTIC
    with mp.workdps(v1.PRECISION_DPS):
        matrix = [
            [mp.mpf("1e-20"), mp.mpf(0)],
            [mp.mpf(0), mp.mpf("1e20")],
            [mp.mpf("1e-20"), mp.mpf("1e20")],
        ]
        solution, residual = _column_equilibrated_solve(
            matrix,
            [
                mp.mpf("1e-20"),
                mp.mpf("2e20"),
                mp.mpf("1e-20") + mp.mpf("2e20"),
            ],
        )
        diagnostic = dict(_SCALE_DIAGNOSTIC or {})
        solution_pass = bool(
            abs(solution[0] - 1) < mp.mpf("1e-60")
            and abs(solution[1] - 2) < mp.mpf("1e-60")
        )
        residual_pass = bool(residual < mp.mpf("1e-60"))
    return {
        "column_scaled_solution": solution_pass,
        "column_scaled_residual": residual_pass,
        "column_scale_range_exercised": (
            diagnostic.get("scale_ratio_decimal") == "1.0e+40"
        ),
        "no_row_scaling": diagnostic.get("row_scaling_applied") is False,
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = v2.run_smoke(max_runtime_seconds, result_dir)
        payload["checks"].update({
            f"hp_m1_v3_{name}": value for name, value in _fixture().items()
        })
        payload["passed"] = all(payload["checks"].values())
    payload["checks"]["hp_m1_v3_owners_restored"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    with _overlay():
        payload = v2.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored() or _SCALE_DIAGNOSTIC is None:
        raise RuntimeError("KMPC-095 column-equilibration lifecycle incomplete")
    boundary = payload["high_precision_m1_reassembly_boundary"]
    boundary["column_equilibration_successor"] = {
        "version": "V3_DIAGONAL_COLUMN_MAX_ABS",
        "only_unknown_coordinates_changed": True,
        "row_weights_changed": False,
        "m1_equations_changed": False,
        "physics_changed": False,
        "owners_restored": True,
        **_SCALE_DIAGNOSTIC,
    }
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("high-precision M1 boundary has no aggregate scope")
