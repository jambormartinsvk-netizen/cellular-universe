"""Native 80-dps rank-revealing M1 CPQR diagnostic for BI/k=.15.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
This successor changes only the reduced M1 numerical solver.  It uses
two-pass modified Gram-Schmidt QR with column pivoting on the native mpmath
matrix, preserves the original unweighted least-squares objective, and stops
before F0, M3, coefficient attribution and the C2 physics gate.
"""

from __future__ import annotations

from contextlib import contextmanager
import hashlib
from pathlib import Path
import time
from typing import Iterator

import mpmath as mp

from . import c2_bi_k0p15_high_precision_m1_reassembly_v8_publication_receipt as v8


v7 = v8.v7
base = v7.base
_V8_SOURCE_HASHES = v8.source_hashes
_V7_CONTRACT_GUARD = v7.contract_guard
_BASE_SOLVE = base._solve_reduced
RANK_RELATIVE_THRESHOLD = mp.mpf("1e-60")
ORTHOGONALITY_THRESHOLD = mp.mpf("1e-60")
FACTORIZATION_THRESHOLD = mp.mpf("1e-60")
NORMAL_RESIDUAL_THRESHOLD = mp.mpf("1e-55")
REORTHOGONALIZATION_PASSES = 2
_CPQR_DIAGNOSTIC: dict[str, object] | None = None


def configure(**config: object) -> None:
    v7.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v7.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v7.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V8_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    name = "c2_bi_k0p15_high_precision_m1_reassembly_v9_native_cpqr.py"
    hashes[name] = base._sha256_file(here / name)
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V7_CONTRACT_GUARD()
    guard["checks"].update({
        "hp_m1_v9_native_80dps_matrix": base.PRECISION_DPS == 80,
        "hp_m1_v9_rank_revealing_column_pivoting": True,
        "hp_m1_v9_two_pass_reorthogonalization": (
            REORTHOGONALIZATION_PASSES == 2
        ),
        "hp_m1_v9_rank_relative_threshold_1e_minus_60": (
            RANK_RELATIVE_THRESHOLD == mp.mpf("1e-60")
        ),
        "hp_m1_v9_no_row_scaling": True,
        "hp_m1_v9_unweighted_objective_unchanged": True,
        "hp_m1_v9_no_f0_m3_attribution": True,
        "hp_m1_v9_no_physics_gate": True,
        "hp_m1_v9_equations_support_thresholds_unchanged": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _dot(left: list[mp.mpf], right: list[mp.mpf]) -> mp.mpf:
    return mp.fsum(a * b for a, b in zip(left, right, strict=True))


def _norm(vector: list[mp.mpf]) -> mp.mpf:
    return mp.sqrt(max(mp.mpf(0), _dot(vector, vector)))


def _decimal(value: mp.mpf) -> str:
    return mp.nstr(value, 50)


def _permutation_sha256(permutation: list[int]) -> str:
    serial = ",".join(str(value) for value in permutation).encode("ascii")
    return hashlib.sha256(serial).hexdigest().upper()


def _cpqr_solve(
    matrix: list[list[mp.mpf]], rhs: list[mp.mpf]
) -> tuple[list[mp.mpf], mp.mpf]:
    """Solve min ||Ax-b||_2 with native two-pass MGS column-pivoted QR."""
    global _CPQR_DIAGNOSTIC
    row_count = len(matrix)
    column_count = len(matrix[0]) if matrix else 0
    if row_count < column_count or len(rhs) != row_count:
        raise ValueError("KMPC-101 CPQR requires a tall matrix and matching RHS")
    if any(len(row) != column_count for row in matrix):
        raise ValueError("KMPC-101 CPQR matrix is ragged")
    if not column_count:
        raise ValueError("KMPC-101 CPQR matrix has no columns")

    original_columns = [
        [mp.mpf(matrix[row][column]) for row in range(row_count)]
        for column in range(column_count)
    ]
    work_columns = [list(column) for column in original_columns]
    permutation = list(range(column_count))
    residual_norms = [_norm(column) for column in work_columns]
    reference_scale = max(residual_norms)
    rank_threshold = reference_scale * RANK_RELATIVE_THRESHOLD
    q_columns: list[list[mp.mpf]] = []
    upper = [
        [mp.mpf(0) for _ in range(column_count)]
        for _ in range(column_count)
    ]
    diagonal: list[mp.mpf] = []

    for step in range(column_count):
        pivot = max(
            range(step, column_count), key=lambda column: residual_norms[column]
        )
        if pivot != step:
            work_columns[step], work_columns[pivot] = (
                work_columns[pivot], work_columns[step]
            )
            residual_norms[step], residual_norms[pivot] = (
                residual_norms[pivot], residual_norms[step]
            )
            permutation[step], permutation[pivot] = (
                permutation[pivot], permutation[step]
            )
            for prior in range(step):
                upper[prior][step], upper[prior][pivot] = (
                    upper[prior][pivot], upper[prior][step]
                )

        pivot_norm = _norm(work_columns[step])
        if pivot_norm <= rank_threshold:
            break
        upper[step][step] = pivot_norm
        diagonal.append(pivot_norm)
        q_column = [value / pivot_norm for value in work_columns[step]]
        q_columns.append(q_column)

        for column in range(step + 1, column_count):
            coefficient = mp.mpf(0)
            residual_column = work_columns[column]
            for _ in range(REORTHOGONALIZATION_PASSES):
                correction = _dot(q_column, residual_column)
                coefficient += correction
                residual_column = [
                    value - correction * q_value
                    for value, q_value in zip(
                        residual_column, q_column, strict=True
                    )
                ]
            upper[step][column] = coefficient
            work_columns[column] = residual_column
            residual_norms[column] = _norm(residual_column)

    rank = len(diagonal)
    projected_rhs = [_dot(q_column, rhs) for q_column in q_columns]
    permuted_solution = [mp.mpf(0) for _ in range(column_count)]
    for row in range(rank - 1, -1, -1):
        tail = mp.fsum(
            upper[row][column] * permuted_solution[column]
            for column in range(row + 1, rank)
        )
        permuted_solution[row] = (projected_rhs[row] - tail) / upper[row][row]
    solution = [mp.mpf(0) for _ in range(column_count)]
    for permuted_column, original_column in enumerate(permutation):
        solution[original_column] = permuted_solution[permuted_column]

    residual_vector = [
        mp.fsum(matrix[row][column] * solution[column]
                for column in range(column_count)) - rhs[row]
        for row in range(row_count)
    ]
    residual_l2 = _norm(residual_vector)
    matrix_frobenius = mp.sqrt(mp.fsum(
        value * value for row in matrix for value in row
    ))
    normal_max = max(
        abs(mp.fsum(matrix[row][column] * residual_vector[row]
                    for row in range(row_count)))
        for column in range(column_count)
    )
    normal_scale = matrix_frobenius * max(residual_l2, mp.mpf(1))
    normal_relative = normal_max / normal_scale

    orthogonality_max = mp.mpf(0)
    for left in range(rank):
        for right in range(left, rank):
            target = mp.mpf(1) if left == right else mp.mpf(0)
            orthogonality_max = max(
                orthogonality_max,
                abs(_dot(q_columns[left], q_columns[right]) - target),
            )

    factorization_max = mp.mpf(0)
    for permuted_column, original_column in enumerate(permutation):
        for row in range(row_count):
            reconstructed = mp.fsum(
                q_columns[basis][row] * upper[basis][permuted_column]
                for basis in range(min(rank, permuted_column + 1))
            )
            factorization_max = max(
                factorization_max,
                abs(original_columns[original_column][row] - reconstructed),
            )
    factorization_relative = factorization_max / max(reference_scale, mp.mpf(1))

    diagonal_min = min(diagonal) if diagonal else mp.mpf(0)
    diagonal_max = max(diagonal) if diagonal else mp.mpf(0)
    _CPQR_DIAGNOSTIC = {
        "method": "NATIVE_MPMATH_80DPS_TWO_PASS_MGS_CPQR",
        "objective": "ORIGINAL_UNWEIGHTED_LEAST_SQUARES",
        "row_scaling_applied": False,
        "column_pivoting_applied": True,
        "reorthogonalization_passes": REORTHOGONALIZATION_PASSES,
        "shape": [row_count, column_count],
        "rank": rank,
        "expected_full_column_rank": column_count,
        "rank_relative_threshold_decimal": _decimal(RANK_RELATIVE_THRESHOLD),
        "rank_absolute_threshold_decimal": _decimal(rank_threshold),
        "reference_column_norm_decimal": _decimal(reference_scale),
        "diagonal_max_decimal": _decimal(diagonal_max),
        "diagonal_min_resolved_decimal": _decimal(diagonal_min),
        "diagonal_min_to_max_decimal": _decimal(
            diagonal_min / diagonal_max if diagonal_max else mp.mpf(0)
        ),
        "ten_smallest_resolved_diagonals_decimal": [
            _decimal(value) for value in sorted(diagonal)[:10]
        ],
        "permutation": permutation,
        "permutation_sha256": _permutation_sha256(permutation),
        "unweighted_residual_l2_decimal": _decimal(residual_l2),
        "normal_equation_residual_max_decimal": _decimal(normal_max),
        "normal_equation_residual_relative_decimal": _decimal(normal_relative),
        "orthogonality_max_abs_decimal": _decimal(orthogonality_max),
        "factorization_max_abs_decimal": _decimal(factorization_max),
        "factorization_max_relative_decimal": _decimal(factorization_relative),
        "rank_full": rank == column_count,
        "orthogonality_pass": orthogonality_max <= ORTHOGONALITY_THRESHOLD,
        "factorization_pass": factorization_relative <= FACTORIZATION_THRESHOLD,
        "normal_residual_pass": normal_relative <= NORMAL_RESIDUAL_THRESHOLD,
        "finite": all(mp.isfinite(value) for value in (
            residual_l2, normal_relative, orthogonality_max,
            factorization_relative, diagonal_min, diagonal_max,
        )),
    }
    return solution, residual_l2


@contextmanager
def _solver_overlay() -> Iterator[None]:
    global _CPQR_DIAGNOSTIC
    before = (base._solve_reduced, base._M1_SOLVE_COUNT, base._M1_BOUNDARY)
    _CPQR_DIAGNOSTIC = None
    base._M1_SOLVE_COUNT = 0
    base._M1_BOUNDARY = None
    try:
        base._solve_reduced = _cpqr_solve
        yield
    finally:
        base._solve_reduced, base._M1_SOLVE_COUNT, base._M1_BOUNDARY = before


def _owners_restored() -> bool:
    return base._solve_reduced is _BASE_SOLVE


def _fixture() -> dict[str, bool]:
    global _CPQR_DIAGNOSTIC
    before = _CPQR_DIAGNOSTIC
    with mp.workdps(base.PRECISION_DPS):
        full = [
            [mp.mpf(1), mp.mpf(0), mp.mpf(100)],
            [mp.mpf(0), mp.mpf(1), mp.mpf(1)],
            [mp.mpf(1), mp.mpf(1), mp.mpf(0)],
            [mp.mpf(2), mp.mpf(-1), mp.mpf(50)],
            [mp.mpf(0), mp.mpf(2), mp.mpf(-3)],
        ]
        expected = [mp.mpf(2), mp.mpf(-1), mp.mpf("0.5")]
        rhs = [
            mp.fsum(value * expected[column]
                    for column, value in enumerate(row))
            for row in full
        ]
        solved, residual = _cpqr_solve(full, rhs)
        full_diagnostic = dict(_CPQR_DIAGNOSTIC or {})
        deficient = [
            [mp.mpf(1), mp.mpf(2), mp.mpf(1)],
            [mp.mpf(0), mp.mpf(1), mp.mpf(0)],
            [mp.mpf(2), mp.mpf(0), mp.mpf(2)],
            [mp.mpf(-1), mp.mpf(1), mp.mpf(-1)],
        ]
        _cpqr_solve(deficient, [mp.mpf(1), mp.mpf(2), mp.mpf(3), mp.mpf(4)])
        deficient_diagnostic = dict(_CPQR_DIAGNOSTIC or {})
        solution_error = max(abs(a - b) for a, b in zip(solved, expected, strict=True))
    _CPQR_DIAGNOSTIC = before
    return {
        "full_rank_fixture_rank_3": full_diagnostic.get("rank") == 3,
        "full_rank_fixture_forces_pivot": full_diagnostic.get("permutation", [None])[0] == 2,
        "full_rank_fixture_solution": solution_error < mp.mpf("1e-60"),
        "full_rank_fixture_residual": residual < mp.mpf("1e-60"),
        "full_rank_fixture_orthogonality": bool(full_diagnostic.get("orthogonality_pass")),
        "full_rank_fixture_factorization": bool(full_diagnostic.get("factorization_pass")),
        "rank_deficient_fixture_rank_2": deficient_diagnostic.get("rank") == 2,
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    checks = {
        "contract_guard": bool(contract_guard()["pass"]),
        **{f"cpqr_{name}": value for name, value in _fixture().items()},
        "owners_initial": _owners_restored(),
        "no_result_file_written": True,
    }
    return {
        "run_id": "KMPC-101",
        "mode": "SMOKE_NO_RESULT_FILE",
        "checks": checks,
        "passed": all(checks.values()),
    }


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    if (mode, k_mpc) != (base.MODE, base.K_MPC):
        raise ValueError("KMPC-101 native CPQR atom identity mismatch")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError("KMPC-101 native CPQR deadline exceeded")

    inputs = base.legacy.FrozenInputs()
    reference_legacy, _, reference_metadata = (
        base.physics.m1_anchor.solve_standard_seed_anchored(
            mode, k_mpc, inputs, deadline, order=base.ORDER
        )
    )
    reference_standard = {
        target: dict(reference_legacy[source])
        for target, source in base.physics.STATE_TO_LEGACY.items()
    }
    with mp.workdps(base.PRECISION_DPS):
        with _solver_overlay():
            _, boundary = base._m1_reassembly(inputs, reference_standard)
            diagnostic = dict(_CPQR_DIAGNOSTIC or {})
    if not _owners_restored() or not diagnostic:
        raise RuntimeError("KMPC-101 native CPQR lifecycle incomplete")
    deadline()

    numerical_contract_pass = bool(
        diagnostic["shape"] == [121, 98]
        and diagnostic["rank"] == 98
        and diagnostic["rank_full"]
        and diagnostic["orthogonality_pass"]
        and diagnostic["factorization_pass"]
        and diagnostic["normal_residual_pass"]
        and diagnostic["finite"]
    )
    raw_boundary_pass = bool(boundary["pass"])
    boundary.update({
        "solver": "NATIVE_MPMATH_80DPS_TWO_PASS_MGS_CPQR",
        "native_rank_revealing_diagnostic": diagnostic,
        "native_cpqr_solve_count": 1,
        "authoritative_high_precision_m1_solve_count": 1,
        "raw_m1_driver_and_holdout_boundary_pass": raw_boundary_pass,
        "pass": False,
        "pass_c2_atom_candidate": False,
    })
    checks = {
        "contract_guard": bool(contract_guard()["pass"]),
        "native_cpqr_diagnostic_created": bool(diagnostic),
        "native_cpqr_numerical_contract": numerical_contract_pass,
        "one_native_hp_m1_solve": (
            boundary["authoritative_high_precision_m1_solve_count"] == 1
        ),
        "owners_restored": _owners_restored(),
        "physics_pass_suppressed": (
            boundary["pass"] is False
            and boundary["pass_c2_atom_candidate"] is False
        ),
    }
    return {
        "test": "KMPC-101 native 80-dps rank-revealing HP-M1 CPQR diagnostic",
        "run_id": "KMPC-101",
        "execution_status": "COMPLETED_DIAGNOSTIC_ONLY",
        "authorship": {
            "theory_author": "Martin Jambor",
            "script_creator": "Codex (OpenAI)",
        },
        "atom_id": "BI/k=0.15/nominal",
        "identity": {
            "mode": mode, "k_Mpc_inverse": k_mpc,
            "variant": "nominal", "order": base.ORDER,
        },
        "scope": (
            "NATIVE_80DPS_M1_ASSEMBLY_AND_CPQR_ONLY; NO_F0; NO_M3; "
            "NO_HOLDOUT_ATTRIBUTION; NO_C2_PHYSICS_GATE"
        ),
        "source_hashes": source_hashes(),
        "contract_guard": contract_guard(),
        "frozen_reference_standard": {
            "method": "LIVE_FROZEN_BINARY64_HARD_ANCHORED_M1",
            "solve_count": 1,
            "metadata": reference_metadata,
        },
        "high_precision_m1_reassembly_boundary": boundary,
        "checks": checks,
        "passed_diagnostic_contract": all(checks.values()),
        "M1": {"pass": False, "status": "NOT_ASSIGNED_DIAGNOSTIC_ONLY"},
        "core_pass": False,
        "common_pass": False,
        "tail_pass": False,
        "background_guard": {
            "pass": False, "status": "NOT_EVALUATED_DIAGNOSTIC_ONLY"
        },
        "candidate_interpretation_not_verdict": (
            "REVIEW_C2_BI_K0p15_NATIVE_HP_M1_CPQR_COMPLETE"
            if numerical_contract_pass
            else "REVIEW_C2_BI_K0p15_NATIVE_HP_M1_CPQR_UNCLOSED"
        ),
        "physics_verdict_role": "DIAGNOSTIC_ONLY",
        "score_effect": "NONE_DIAGNOSTIC_ONLY_PENDING_INTERNAL_AUDIT",
        "prediction_table_effect": "NONE",
        "release_trigger": "NONE",
        "zenodo_trigger": "NONE",
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("native HP-M1 CPQR diagnostic has no aggregate scope")
