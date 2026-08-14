"""KMPC-143 same-matrix refinement for the C3 NID/.05 pair.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
No equation, matrix entry, RHS, support, rcond, threshold or runtime changes.
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator, Mapping

from . import c2_cdi_k0p15_same_matrix_refinement as refinement
from . import c3_zero_variant_parallel_v4_nid_k0p05_identity_adapter as v4


scientific = v4.scientific
RUN_ID = "KMPC-143"
TARGET = ("NID", 0.05)
MODES = ("NID",)
K_VALUES = (0.05,)
VARIANTS = v4.VARIANTS
SHARDS = v4.SHARDS
EXPECTED_V4_SHA256 = (
    "7151201BE9007263D8345FD63C54129BE2A1B2898C5D5CF02D0C9F4322853354"
)
EXPECTED_REFINEMENT_SHA256 = (
    "EA589E4CBAD3AD618DEBC41C81B271EAC23F229AEA82C80E962CD792091468F6"
)
_ORIGINAL_SOLVER = scientific.physics._solve_equilibrated

# The inherited aggregate validates run identity through this process-local
# owner. Frozen source files remain unchanged.
v4.legacy.RUN_ID = RUN_ID


def sha256_file(path: Path) -> str:
    return scientific.sha256_file(path)


def shard_key(variant: str, level: str) -> str:
    return v4.shard_key(variant, level)


def output_name(mode: str, k_mpc: float) -> str:
    if (mode, k_mpc) != TARGET:
        raise ValueError("KMPC-143 is frozen to NID/k=0.05")
    return (
        "RUN_KMPC_143_P5_3G7_C3_NID_K0p05_"
        "ZERO_VARIANT_PAIR_SAME_MATRIX_REFINEMENT.json"
    )


def failure_name(mode: str, k_mpc: float) -> str:
    return output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def successor_contract_guard() -> dict[str, object]:
    support = scientific.SUPPORTS[TARGET]
    checks = {
        "target_identity_exact": TARGET == ("NID", 0.05),
        "support_05_07_exact": support.accepted == (0, 5)
        and support.audit == (0, 7)
        and support.m1_depth == 7,
        "four_shards_exact": SHARDS
        == (
            ("gamma0", "accepted"),
            ("gamma0", "audit"),
            ("af0", "accepted"),
            ("af0", "audit"),
        ),
        "target_rank_104_exact": refinement.TARGET_RANK == 104,
        "three_iterations_exact": refinement.ITERATIONS == 3,
        "shared_physics_owner": refinement.physics is scientific.physics,
        "original_solver_identity": refinement._ORIGINAL_SOLVER is _ORIGINAL_SOLVER,
        "v4_identity_adapter_frozen": sha256_file(Path(v4.__file__).resolve())
        == EXPECTED_V4_SHA256,
        "refinement_source_frozen": sha256_file(
            Path(refinement.__file__).resolve()
        )
        == EXPECTED_REFINEMENT_SHA256,
    }
    return {"checks": checks, "pass": all(checks.values())}


@contextmanager
def _overlay() -> Iterator[None]:
    if scientific.physics._solve_equilibrated is not _ORIGINAL_SOLVER:
        raise RuntimeError("KMPC-143 solver owner was already modified")
    try:
        scientific.physics._solve_equilibrated = refinement._solve_equilibrated
        yield
    finally:
        scientific.physics._solve_equilibrated = _ORIGINAL_SOLVER


def _owners_restored() -> bool:
    return scientific.physics._solve_equilibrated is _ORIGINAL_SOLVER


def run_support_worker(
    mode: str,
    k_mpc: float,
    variant: str,
    level: str,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    if (mode, k_mpc) != TARGET or (variant, level) not in SHARDS:
        raise ValueError("KMPC-143 worker identity outside preregistration")
    guard = successor_contract_guard()
    with _overlay():
        payload = v4.run_support_worker(
            mode, k_mpc, variant, level, max_runtime_seconds, result_dir
        )
    if not _owners_restored():
        raise RuntimeError("KMPC-143 solver owner was not restored")
    diagnostics = payload["solve"]["m3"]["diagnostics"]
    audit = diagnostics.get("same_matrix_refinement")
    refinement_checks = {
        "applicability_exact": (level == "audit") == isinstance(audit, dict),
        "accepted_rank_not_refined": level != "accepted" or audit is None,
        "audit_rank_refined": level != "audit"
        or (
            isinstance(audit, dict)
            and audit.get("target_rank") == 104
            and audit.get("iterations") == 3
            and audit.get("matrix_identity") == "EXACT_SAME_MATRIX_AND_CONSTANT"
            and audit.get("selection_rule_pass") is True
        ),
        "owners_restored": _owners_restored(),
    }
    payload["shared_checks"]["same_matrix_refinement_contract"] = bool(
        guard["pass"]
    )
    payload["same_matrix_refinement_contract"] = guard
    payload["same_matrix_refinement_worker_checks"] = refinement_checks
    payload["source_hashes"].update(
        {
            Path(refinement.__file__).name: sha256_file(
                Path(refinement.__file__).resolve()
            ),
            Path(__file__).name: sha256_file(Path(__file__).resolve()),
        }
    )
    if not all(refinement_checks.values()):
        raise RuntimeError("KMPC-143 worker refinement contract failed")
    return payload


def run_worker_smoke(
    mode: str,
    k_mpc: float,
    variant: str,
    level: str,
    result_dir: Path,
) -> dict[str, object]:
    if (mode, k_mpc) != TARGET or (variant, level) not in SHARDS:
        raise ValueError("invalid KMPC-143 smoke shard")
    payload = v4.run_worker_smoke(mode, k_mpc, variant, level, result_dir)
    fixture = refinement._fixture()
    guard = successor_contract_guard()
    payload["checks"].update(
        {
            "same_matrix_refinement_contract": bool(guard["pass"]),
            **{
                f"refinement_fixture_{key}": value
                for key, value in fixture.items()
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
    if (mode, k_mpc) != TARGET:
        raise ValueError("KMPC-143 aggregate identity outside preregistration")
    payload = v4.aggregate_shards(
        mode, k_mpc, shards, result_dir, parent_runtime_seconds
    )
    refinement_audit: dict[str, object] = {}
    for variant in VARIANTS:
        diagnostics = payload["variants"][variant]["audit_solve"]["m3"][
            "diagnostics"
        ]
        audit = diagnostics.get("same_matrix_refinement")
        checks = {
            "audit_present": isinstance(audit, dict),
            "same_matrix_and_constant": isinstance(audit, dict)
            and audit.get("matrix_identity") == "EXACT_SAME_MATRIX_AND_CONSTANT",
            "rank_104": isinstance(audit, dict)
            and audit.get("target_rank") == 104,
            "three_iterations": isinstance(audit, dict)
            and len(audit.get("steps", ())) == 3,
            "selection_rule": isinstance(audit, dict)
            and audit.get("selection_rule_pass") is True,
            "driver_pass_after_refinement": diagnostics.get("pass_driver") is True,
        }
        refinement_audit[variant] = {
            "checks": checks,
            "pass": all(checks.values()),
            "provenance": audit,
            "selected_driver_metrics": {
                "max_relative_residual": diagnostics.get(
                    "max_relative_residual"
                ),
                "max_absolute_fallback_residual": diagnostics.get(
                    "max_absolute_fallback_residual"
                ),
                "worst_relative_row": diagnostics.get("worst_relative_row"),
                "worst_absolute_fallback_row": diagnostics.get(
                    "worst_absolute_fallback_row"
                ),
            },
        }
    refinement_pass = all(row["pass"] for row in refinement_audit.values())
    pair_pass = bool(payload["pair_pass"] and refinement_pass)
    payload["test"] = (
        "A2-K4 P5.3g7 C3 NID/.05 four-shard same-matrix refinement receipt"
    )
    payload["identity"]["physical_receipt"] = (
        "four_support_shards_gamma0_af0_same_matrix_refinement_pair"
    )
    payload["process_architecture"]["same_matrix_refinement"] = {
        "target_rank": 104,
        "iterations": 3,
        "matrix_rhs_support_threshold_changes": 0,
    }
    payload["same_matrix_refinement_audit"] = refinement_audit
    payload["same_matrix_refinement_pass"] = refinement_pass
    payload["pair_pass"] = pair_pass
    payload["candidate_interpretation_not_verdict"] = (
        "PASS_C3_NID_K0P05_ZERO_PAIR_SAME_MATRIX_REFINEMENT_CANDIDATE_ONLY"
        if pair_pass
        else "REVIEW_C3_NID_K0P05_NUMERICAL_BOUNDARY_UNCLOSED"
    )
    return payload


def aggregate_smoke_shards(
    mode: str,
    k_mpc: float,
    shards: Mapping[str, Mapping[str, object]],
) -> dict[str, object]:
    if (mode, k_mpc) != TARGET:
        raise ValueError("KMPC-143 smoke aggregate outside preregistration")
    return v4.aggregate_smoke_shards(mode, k_mpc, shards)
