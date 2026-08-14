"""Same-matrix numerical refinement for the CDI/k=.15 C2 audit M3 solve.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
No equation, matrix entry, support, rcond, or threshold is changed.
"""

from __future__ import annotations

from contextlib import contextmanager
import math
from pathlib import Path
from typing import Callable, Iterator

from . import c2_single_atom_adapter as adapter


legacy = adapter.legacy
physics = legacy.physics
np = physics.np
TARGET_RANK = 104
ITERATIONS = 3
_ORIGINAL_SOLVER = physics._solve_equilibrated
_ADAPTER_SOURCE_HASHES = adapter.source_hashes
_ADAPTER_CONTRACT_GUARD = adapter.contract_guard


def configure(**config: object) -> None:
    adapter.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return adapter.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return adapter.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_ADAPTER_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_cdi_k0p15_same_matrix_refinement.py"] = legacy.sha256_file(
        here / "c2_cdi_k0p15_same_matrix_refinement.py"
    )
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _ADAPTER_CONTRACT_GUARD()
    guard["checks"]["same_matrix_target_rank_exact"] = TARGET_RANK == 13 * 8
    guard["checks"]["refinement_iterations_exact"] = ITERATIONS == 3
    guard["pass"] = all(guard["checks"].values())
    return guard


def _refine_solution(
    matrix: object,
    constant: object,
    solution: object,
    row_labels: list[str] | None,
    deadline: Callable[[], None] | None,
) -> tuple[object, dict[str, object]]:
    row_scale = np.maximum(
        np.maximum(np.max(np.abs(matrix), axis=1), np.abs(constant)), 1.0e-300
    )
    row_matrix = matrix / row_scale[:, np.newaxis]
    row_constant = constant / row_scale
    column_scale = np.maximum(np.max(np.abs(row_matrix), axis=0), 1.0e-300)
    equilibrated = row_matrix / column_scale[np.newaxis, :]
    current = np.asarray(solution, dtype=float).copy()
    baseline = physics._row_residual_metrics(matrix, constant, current, row_labels)
    steps: list[dict[str, object]] = []
    for index in range(1, ITERATIONS + 1):
        y = current * column_scale
        scaled_residual = equilibrated @ y + row_constant
        correction_y = np.linalg.solve(equilibrated, -scaled_residual)
        trial = (y + correction_y) / column_scale
        metrics = physics._row_residual_metrics(matrix, constant, trial, row_labels)
        correction_relative = float(
            np.linalg.norm(trial - current) / max(np.linalg.norm(current), 1.0e-300)
        )
        steps.append({
            "iteration": index,
            "correction_relative_l2": correction_relative,
            **metrics,
        })
        current = trial
        if deadline is not None:
            deadline()
    final = steps[-1]
    finite = bool(np.all(np.isfinite(current)))
    selected = bool(
        finite
        and final["max_relative_residual"] < baseline["max_relative_residual"]
        and final["max_absolute_fallback_residual"]
        <= baseline["max_absolute_fallback_residual"]
    )
    audit = {
        "matrix_identity": "EXACT_SAME_MATRIX_AND_CONSTANT",
        "target_rank": TARGET_RANK,
        "iterations": ITERATIONS,
        "baseline": baseline,
        "steps": steps,
        "finite": finite,
        "selection_rule_pass": selected,
    }
    return (current if selected else solution), audit


def _solve_equilibrated(
    matrix: object,
    constant: object,
    expected_rank: int,
    row_labels: list[str] | None = None,
    deadline: Callable[[], None] | None = None,
) -> tuple[object, dict[str, object]]:
    solution, metadata = _ORIGINAL_SOLVER(
        matrix, constant, expected_rank, row_labels=row_labels, deadline=deadline
    )
    if expected_rank != TARGET_RANK:
        return solution, metadata
    selected_solution, audit = _refine_solution(
        matrix, constant, solution, row_labels, deadline
    )
    selected_metrics = physics._row_residual_metrics(
        matrix, constant, selected_solution, row_labels
    )
    refined = dict(metadata)
    refined.update(selected_metrics)
    refined["same_matrix_refinement"] = audit
    return selected_solution, refined


@contextmanager
def _overlay() -> Iterator[None]:
    before = (physics._solve_equilibrated, adapter.source_hashes, adapter.contract_guard)
    try:
        physics._solve_equilibrated = _solve_equilibrated
        adapter.source_hashes = source_hashes
        adapter.contract_guard = contract_guard
        yield
    finally:
        physics._solve_equilibrated, adapter.source_hashes, adapter.contract_guard = before


def _owners_restored() -> bool:
    return bool(
        physics._solve_equilibrated is _ORIGINAL_SOLVER
        and adapter.source_hashes is _ADAPTER_SOURCE_HASHES
        and adapter.contract_guard is _ADAPTER_CONTRACT_GUARD
    )


def _fixture() -> dict[str, object]:
    matrix = np.diag(np.array([1.0, 2.0, 3.0], dtype=float))
    constant = np.array([-1.0, 4.0, -9.0], dtype=float)
    exact = np.array([1.0, -2.0, 3.0], dtype=float)
    perturbed = exact + np.array([1.0e-7, -1.0e-7, 1.0e-7])
    refined, audit = _refine_solution(matrix, constant, perturbed, ["a", "b", "c"], None)
    return {
        "three_iterations": len(audit["steps"]) == ITERATIONS,
        "same_matrix_label": audit["matrix_identity"] == "EXACT_SAME_MATRIX_AND_CONSTANT",
        "residual_improved": audit["steps"][-1]["max_relative_residual"]
        < audit["baseline"]["max_relative_residual"],
        "exact_solution_recovered": bool(np.linalg.norm(refined - exact) <= 1.0e-14),
        "finite": audit["finite"] and math.isfinite(float(np.linalg.norm(refined))),
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = adapter.run_smoke(max_runtime_seconds, result_dir)
        fixture = _fixture()
        payload["checks"].update({f"refinement_{key}": value for key, value in fixture.items()})
        payload["checks"]["target_rank_exact"] = TARGET_RANK == 104
        payload["passed"] = all(payload["checks"].values())
    payload["checks"]["owners_restored"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str, k_mpc: float, max_runtime_seconds: float, result_dir: Path
) -> dict[str, object]:
    with _overlay():
        payload = adapter.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored():
        raise RuntimeError("same-matrix refinement owners were not restored")
    payload["same_matrix_refinement_provenance"] = payload["audit_solve"]["m3"]
    payload["same_matrix_refinement_provenance"] = payload["same_matrix_refinement_provenance"][
        "diagnostics"
    ]["same_matrix_refinement"]
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("CDI/k=.15 same-matrix refinement has no aggregate scope")
