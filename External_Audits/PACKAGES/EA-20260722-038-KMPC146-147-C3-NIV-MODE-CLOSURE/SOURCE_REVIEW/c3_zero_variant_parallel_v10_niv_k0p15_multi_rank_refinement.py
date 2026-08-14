"""KMPC-146 four-shard same-matrix multi-rank refinement for C3 NIV/.15.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
No equation, matrix entry, RHS, support, depth, rcond, threshold, or
independent holdout is changed.
"""

from __future__ import annotations

from contextlib import contextmanager
import json
from pathlib import Path
from typing import Iterator, Mapping

from . import c2_same_matrix_refinement_v2_multi_rank as refinement
from . import c3_zero_variant_parallel_v3_support_shards as v3


scientific = v3.scientific
RUN_ID = "KMPC-146"
TARGET = ("NIV", 0.15)
MODES = ("NIV",)
K_VALUES = (0.15,)
VARIANTS = v3.VARIANTS
SHARDS = v3.SHARDS
PREDECESSOR_NAME = (
    "RUN_KMPC_131_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR.json"
)
PREDECESSOR_SHA256 = (
    "88DFD9AAD5F378CBD9F7E7D1AA9738C40855CA0EC9FD191A77C682D643A0CFE6"
)
EXPECTED_V3_SHA256 = (
    "7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23"
)
EXPECTED_REFINEMENT_SHA256 = (
    "1E2600C366590B7FC56289D1FBC386EF24DA50DA9ED5686AE5FB5A50E0992F08"
)
EXPECTED_TARGET_RANK = {"accepted": 104, "audit": 130}
_ORIGINAL_SOLVER = scientific.physics._solve_equilibrated

# The inherited aggregate validates worker identity through this
# process-local owner.  Frozen source files remain bytewise unchanged.
v3.RUN_ID = RUN_ID


def sha256_file(path: Path) -> str:
    return scientific.sha256_file(path)


def shard_key(variant: str, level: str) -> str:
    return v3.shard_key(variant, level)


def output_name(mode: str, k_mpc: float) -> str:
    if (mode, k_mpc) != TARGET:
        raise ValueError("KMPC-146 is frozen to NIV/k=0.15")
    return (
        "RUN_KMPC_146_P5_3G7_C3_NIV_K0p15_"
        "ZERO_VARIANT_PAIR_MULTI_RANK_REFINEMENT.json"
    )


def failure_name(mode: str, k_mpc: float) -> str:
    return output_name(mode, k_mpc).replace(
        ".json", "_TECHNICAL_FAILURE.json"
    )


def _predecessor_path(result_dir: Path) -> Path:
    return result_dir / PREDECESSOR_NAME


def _predecessor_hash_pass(result_dir: Path) -> bool:
    path = _predecessor_path(result_dir)
    return path.is_file() and sha256_file(path) == PREDECESSOR_SHA256


def successor_contract_guard() -> dict[str, object]:
    support = scientific.SUPPORTS[TARGET]
    checks = {
        "target_identity_exact": TARGET == ("NIV", 0.15),
        "support_minus1_6_minus1_8_exact": support.accepted == (-1, 6)
        and support.audit == (-1, 8)
        and support.m1_depth == 8,
        "four_shards_exact": SHARDS
        == (
            ("gamma0", "accepted"),
            ("gamma0", "audit"),
            ("af0", "accepted"),
            ("af0", "audit"),
        ),
        "target_ranks_104_130_exact": refinement.TARGET_RANKS == (104, 130),
        "rank_by_level_exact": EXPECTED_TARGET_RANK
        == {"accepted": 104, "audit": 130},
        "three_iterations_exact": refinement.ITERATIONS == 3,
        "shared_physics_owner": refinement.physics is scientific.physics,
        "original_solver_identity": refinement._ORIGINAL_SOLVER
        is _ORIGINAL_SOLVER,
        "v3_source_frozen": sha256_file(Path(v3.__file__).resolve())
        == EXPECTED_V3_SHA256,
        "refinement_source_frozen": sha256_file(
            Path(refinement.__file__).resolve()
        )
        == EXPECTED_REFINEMENT_SHA256,
    }
    return {"checks": checks, "pass": all(checks.values())}


@contextmanager
def _overlay() -> Iterator[None]:
    if scientific.physics._solve_equilibrated is not _ORIGINAL_SOLVER:
        raise RuntimeError("KMPC-146 solver owner was already modified")
    try:
        scientific.physics._solve_equilibrated = refinement._solve_equilibrated
        yield
    finally:
        scientific.physics._solve_equilibrated = _ORIGINAL_SOLVER


def _owners_restored() -> bool:
    return scientific.physics._solve_equilibrated is _ORIGINAL_SOLVER


def _provenance_checks(
    provenance: object, level: str, diagnostics: Mapping[str, object]
) -> dict[str, bool]:
    expected_rank = EXPECTED_TARGET_RANK[level]
    return {
        "provenance_present": isinstance(provenance, dict),
        "target_rank_exact": isinstance(provenance, dict)
        and provenance.get("target_rank") == expected_rank,
        "three_iterations": isinstance(provenance, dict)
        and provenance.get("iterations") == 3
        and len(provenance.get("steps", ())) == 3,
        "same_matrix_and_constant": isinstance(provenance, dict)
        and provenance.get("matrix_identity")
        == "EXACT_SAME_MATRIX_AND_CONSTANT",
        "selection_rule": isinstance(provenance, dict)
        and provenance.get("selection_rule_pass") is True,
        "driver_pass_after_refinement": diagnostics.get("pass_driver") is True,
    }


def run_support_worker(
    mode: str,
    k_mpc: float,
    variant: str,
    level: str,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    if (mode, k_mpc) != TARGET or (variant, level) not in SHARDS:
        raise ValueError("KMPC-146 worker identity outside preregistration")
    guard = successor_contract_guard()
    if not _predecessor_hash_pass(result_dir):
        raise RuntimeError("KMPC-146 predecessor missing or hash-mismatched")
    with _overlay():
        payload = v3.run_support_worker(
            mode, k_mpc, variant, level, max_runtime_seconds, result_dir
        )
    if not _owners_restored():
        raise RuntimeError("KMPC-146 solver owner was not restored")
    diagnostics = payload["solve"]["m3"]["diagnostics"]
    provenance = diagnostics.get("same_matrix_refinement")
    refinement_checks = {
        **_provenance_checks(provenance, level, diagnostics),
        "owners_restored": _owners_restored(),
        "predecessor_hash_frozen": _predecessor_hash_pass(result_dir),
        "successor_contract": bool(guard["pass"]),
    }
    payload["shared_checks"]["same_matrix_multi_rank_contract"] = bool(
        guard["pass"]
    )
    payload["same_matrix_multi_rank_contract"] = guard
    payload["same_matrix_multi_rank_worker_checks"] = refinement_checks
    payload["source_hashes"].update(
        {
            Path(refinement.__file__).name: sha256_file(
                Path(refinement.__file__).resolve()
            ),
            Path(__file__).name: sha256_file(Path(__file__).resolve()),
        }
    )
    if not all(refinement_checks.values()):
        raise RuntimeError(
            f"KMPC-146 worker refinement contract failed: {refinement_checks}"
        )
    return payload


def run_worker_smoke(
    mode: str,
    k_mpc: float,
    variant: str,
    level: str,
    result_dir: Path,
) -> dict[str, object]:
    if (mode, k_mpc) != TARGET or (variant, level) not in SHARDS:
        raise ValueError("invalid KMPC-146 smoke shard")
    payload = v3.run_worker_smoke(mode, k_mpc, variant, level, result_dir)
    fixtures = {
        str(rank): refinement._rank_fixture(rank)
        for rank in refinement.TARGET_RANKS
    }
    guard = successor_contract_guard()
    payload["checks"].update(
        {
            "same_matrix_multi_rank_contract": bool(guard["pass"]),
            "predecessor_hash_frozen": _predecessor_hash_pass(result_dir),
            "target_rank_for_level_exact": EXPECTED_TARGET_RANK[level]
            in refinement.TARGET_RANKS,
            **{
                f"rank_{rank}_{key}": value
                for rank, checks in fixtures.items()
                for key, value in checks.items()
            },
            "owners_restored": _owners_restored(),
        }
    )
    payload["pass"] = all(payload["checks"].values())
    payload["physics_executed"] = False
    return payload


def aggregate_shards(
    mode: str,
    k_mpc: float,
    shards: Mapping[str, Mapping[str, object]],
    result_dir: Path,
    parent_runtime_seconds: float,
) -> dict[str, object]:
    if (mode, k_mpc) != TARGET or not _predecessor_hash_pass(result_dir):
        raise RuntimeError("KMPC-146 aggregate identity/predecessor mismatch")
    payload = v3.aggregate_shards(
        mode, k_mpc, shards, result_dir, parent_runtime_seconds
    )
    predecessor = json.loads(
        _predecessor_path(result_dir).read_text(encoding="utf-8")
    )
    refinement_audit: dict[str, object] = {}
    for variant in VARIANTS:
        refinement_audit[variant] = {}
        for level in ("accepted", "audit"):
            diagnostics = payload["variants"][variant][f"{level}_solve"][
                "m3"
            ]["diagnostics"]
            provenance = diagnostics.get("same_matrix_refinement")
            baseline = (
                provenance.get("baseline", {})
                if isinstance(provenance, dict)
                else {}
            )
            predecessor_diagnostics = predecessor["variants"][variant][
                f"{level}_solve"
            ]["m3"]["diagnostics"]
            checks = {
                **_provenance_checks(provenance, level, diagnostics),
                "baseline_relative_exact_predecessor": baseline.get(
                    "max_relative_residual"
                )
                == predecessor_diagnostics.get("max_relative_residual"),
                "baseline_absolute_exact_predecessor": baseline.get(
                    "max_absolute_fallback_residual"
                )
                == predecessor_diagnostics.get(
                    "max_absolute_fallback_residual"
                ),
                "f0_exact_predecessor_parity": payload["variants"][variant][
                    f"{level}_solve"
                ]["fuel"]
                == predecessor["variants"][variant][f"{level}_solve"]["fuel"],
            }
            refinement_audit[variant][level] = {
                "checks": checks,
                "pass": all(checks.values()),
                "provenance": provenance,
                "selected_driver_metrics": {
                    "max_relative_residual": diagnostics.get(
                        "max_relative_residual"
                    ),
                    "max_absolute_fallback_residual": diagnostics.get(
                        "max_absolute_fallback_residual"
                    ),
                    "worst_relative_row": diagnostics.get(
                        "worst_relative_row"
                    ),
                    "worst_absolute_fallback_row": diagnostics.get(
                        "worst_absolute_fallback_row"
                    ),
                },
            }
    refinement_pass = all(
        refinement_audit[variant][level]["pass"]
        for variant in VARIANTS
        for level in ("accepted", "audit")
    )
    pair_pass = bool(payload["pair_pass"] and refinement_pass)
    payload["test"] = (
        "A2-K4 P5.3g7 C3 NIV/.15 four-shard same-matrix multi-rank "
        "refinement receipt"
    )
    payload["identity"]["physical_receipt"] = (
        "four_support_shards_gamma0_af0_rank104_130_refinement_pair"
    )
    payload["process_architecture"]["same_matrix_multi_rank_refinement"] = {
        "target_shards": [shard_key(*shard) for shard in SHARDS],
        "target_rank_by_level": EXPECTED_TARGET_RANK,
        "iterations_per_solve": 3,
        "matrix_rhs_support_depth_threshold_changes": 0,
        "independent_holdout_rows_added_to_driver": 0,
    }
    payload["predecessor_authority"] = {
        "file": PREDECESSOR_NAME,
        "sha256": PREDECESSOR_SHA256,
        "candidate": predecessor.get("candidate_interpretation_not_verdict"),
    }
    payload["same_matrix_multi_rank_audit"] = refinement_audit
    payload["same_matrix_multi_rank_pass"] = refinement_pass
    payload["pair_pass"] = pair_pass
    payload["candidate_interpretation_not_verdict"] = (
        "PASS_C3_NIV_K0P15_ZERO_PAIR_MULTI_RANK_REFINEMENT_CANDIDATE_ONLY"
        if pair_pass
        else "REVIEW_C3_NIV_K0P15_MULTI_RANK_NUMERICAL_BOUNDARY_UNCLOSED"
    )
    return payload


def aggregate_smoke_shards(
    mode: str,
    k_mpc: float,
    shards: Mapping[str, Mapping[str, object]],
) -> dict[str, object]:
    if (mode, k_mpc) != TARGET:
        raise ValueError("KMPC-146 smoke aggregate outside preregistration")
    return v3.aggregate_smoke_shards(mode, k_mpc, shards)
