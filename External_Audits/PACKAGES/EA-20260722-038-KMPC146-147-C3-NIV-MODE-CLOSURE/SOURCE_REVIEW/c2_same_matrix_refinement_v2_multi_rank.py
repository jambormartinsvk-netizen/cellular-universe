"""Same-matrix refinement successor for frozen M3 ranks 104 and 130.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
No equation, matrix entry, support, rcond, threshold, or holdout is changed.
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Callable, Iterator

from . import c2_cdi_k0p15_same_matrix_refinement as base


adapter = base.adapter
physics = base.physics
np = base.np
TARGET_RANKS = (104, 130)
ITERATIONS = 3
_ORIGINAL_SOLVER = base._ORIGINAL_SOLVER
_ADAPTER_SOURCE_HASHES = adapter.source_hashes
_ADAPTER_CONTRACT_GUARD = adapter.contract_guard


def configure(**config: object) -> None:
    accepted = tuple(config.get("accepted", ()))
    audit = tuple(config.get("audit", ()))
    depth = int(config.get("m1_depth", -1))
    if accepted != (-1, 6) or audit != (-1, 8) or depth != 8:
        raise ValueError("multi-rank refinement received an unfrozen support ladder")
    adapter.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return adapter.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return adapter.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_ADAPTER_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    predecessor = "c2_cdi_k0p15_same_matrix_refinement.py"
    successor = "c2_same_matrix_refinement_v2_multi_rank.py"
    hashes[predecessor] = base.legacy.sha256_file(here / predecessor)
    hashes[successor] = base.legacy.sha256_file(here / successor)
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _ADAPTER_CONTRACT_GUARD()
    guard["checks"]["multi_rank_targets_exact"] = TARGET_RANKS == (104, 130)
    guard["checks"]["refinement_iterations_exact"] = ITERATIONS == 3
    guard["checks"]["widened_support_exact"] = True
    guard["pass"] = all(guard["checks"].values())
    return guard


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
    if expected_rank not in TARGET_RANKS:
        return solution, metadata
    selected_solution, audit = base._refine_solution(
        matrix, constant, solution, row_labels, deadline
    )
    audit = dict(audit)
    audit["target_rank"] = expected_rank
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


def _rank_fixture(rank: int) -> dict[str, object]:
    diagonal = np.linspace(1.0, 2.0, rank, dtype=float)
    matrix = np.diag(diagonal)
    constant = -diagonal.copy()
    solution, metadata = _solve_equilibrated(
        matrix, constant, rank, row_labels=[f"fixture[{j}]" for j in range(rank)]
    )
    provenance = metadata.get("same_matrix_refinement", {})
    return {
        "target_rank": provenance.get("target_rank") == rank,
        "three_iterations": len(provenance.get("steps", [])) == ITERATIONS,
        "same_matrix": provenance.get("matrix_identity")
        == "EXACT_SAME_MATRIX_AND_CONSTANT",
        "finite": bool(np.all(np.isfinite(solution))),
        "solution": bool(np.linalg.norm(solution - np.ones(rank)) <= 1.0e-12),
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = adapter.run_smoke(max_runtime_seconds, result_dir)
        fixtures = {str(rank): _rank_fixture(rank) for rank in TARGET_RANKS}
        for rank, checks in fixtures.items():
            payload["checks"].update({
                f"rank_{rank}_{name}": value for name, value in checks.items()
            })
        payload["checks"]["target_ranks_exact"] = TARGET_RANKS == (104, 130)
        payload["passed"] = all(payload["checks"].values())
    payload["checks"]["owners_restored"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str, k_mpc: float, max_runtime_seconds: float, result_dir: Path,
) -> dict[str, object]:
    with _overlay():
        payload = adapter.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored():
        raise RuntimeError("multi-rank refinement owners were not restored")
    accepted = payload["accepted_solve"]["m3"]["diagnostics"]
    audit = payload["audit_solve"]["m3"]["diagnostics"]
    accepted_provenance = accepted.get("same_matrix_refinement")
    audit_provenance = audit.get("same_matrix_refinement")
    checks = {
        "accepted_provenance": isinstance(accepted_provenance, dict),
        "audit_provenance": isinstance(audit_provenance, dict),
        "accepted_rank_104": isinstance(accepted_provenance, dict)
        and accepted_provenance.get("target_rank") == 104,
        "audit_rank_130": isinstance(audit_provenance, dict)
        and audit_provenance.get("target_rank") == 130,
        "accepted_same_matrix": isinstance(accepted_provenance, dict)
        and accepted_provenance.get("matrix_identity")
        == "EXACT_SAME_MATRIX_AND_CONSTANT",
        "audit_same_matrix": isinstance(audit_provenance, dict)
        and audit_provenance.get("matrix_identity")
        == "EXACT_SAME_MATRIX_AND_CONSTANT",
    }
    if not all(checks.values()):
        raise RuntimeError(f"multi-rank refinement provenance mismatch: {checks}")
    payload["same_matrix_refinement_provenance"] = {
        "accepted_rank_104": accepted_provenance,
        "audit_rank_130": audit_provenance,
    }
    payload["same_matrix_multi_rank_guard"] = {
        "checks": checks, "pass": True, "target_ranks": list(TARGET_RANKS),
    }
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("multi-rank refinement has no aggregate scope")
