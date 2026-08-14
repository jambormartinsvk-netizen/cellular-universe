"""KMPC-144 af0/audit-only same-matrix refinement for C3 NID/.15.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
No equation, matrix entry, RHS, support, rcond, threshold or runtime changes.
"""

from __future__ import annotations

from contextlib import contextmanager
import json
from pathlib import Path
from typing import Iterator, Mapping

from . import c2_cdi_k0p15_same_matrix_refinement as refinement
from . import c3_zero_variant_parallel_v3_support_shards as v3


scientific = v3.scientific
RUN_ID = "KMPC-144"
TARGET = ("NID", 0.15)
TARGET_SHARD = ("af0", "audit")
MODES = ("NID",)
K_VALUES = (0.15,)
VARIANTS = v3.VARIANTS
SHARDS = v3.SHARDS
PREDECESSOR_NAME = "RUN_KMPC_131_P5_3G7_C3_NID_K0p15_ZERO_VARIANT_PAIR.json"
PREDECESSOR_SHA256 = (
    "3850A3D951E5A8A3E21C93A6DAE7F1A08CBE6430E7100BD01B75F573F21AF71B"
)
EXPECTED_V3_SHA256 = (
    "7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23"
)
EXPECTED_REFINEMENT_SHA256 = (
    "EA589E4CBAD3AD618DEBC41C81B271EAC23F229AEA82C80E962CD792091468F6"
)
_ORIGINAL_SOLVER = scientific.physics._solve_equilibrated

v3.RUN_ID = RUN_ID


def sha256_file(path: Path) -> str:
    return scientific.sha256_file(path)


def shard_key(variant: str, level: str) -> str:
    return v3.shard_key(variant, level)


def output_name(mode: str, k_mpc: float) -> str:
    if (mode, k_mpc) != TARGET:
        raise ValueError("KMPC-144 is frozen to NID/k=0.15")
    return (
        "RUN_KMPC_144_P5_3G7_C3_NID_K0p15_"
        "AF0_AUDIT_SAME_MATRIX_REFINEMENT.json"
    )


def failure_name(mode: str, k_mpc: float) -> str:
    return output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def _predecessor_path(result_dir: Path) -> Path:
    return result_dir / PREDECESSOR_NAME


def _predecessor_hash_pass(result_dir: Path) -> bool:
    path = _predecessor_path(result_dir)
    return path.is_file() and sha256_file(path) == PREDECESSOR_SHA256


def successor_contract_guard() -> dict[str, object]:
    support = scientific.SUPPORTS[TARGET]
    checks = {
        "target_identity_exact": TARGET == ("NID", 0.15),
        "target_shard_af0_audit_exact": TARGET_SHARD == ("af0", "audit"),
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
        raise RuntimeError("KMPC-144 solver owner was already modified")
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
        raise ValueError("KMPC-144 worker identity outside preregistration")
    guard = successor_contract_guard()
    if (variant, level) == TARGET_SHARD:
        with _overlay():
            payload = v3.run_support_worker(
                mode, k_mpc, variant, level, max_runtime_seconds, result_dir
            )
    else:
        payload = v3.run_support_worker(
            mode, k_mpc, variant, level, max_runtime_seconds, result_dir
        )
    if not _owners_restored():
        raise RuntimeError("KMPC-144 solver owner was not restored")
    diagnostics = payload["solve"]["m3"]["diagnostics"]
    audit = diagnostics.get("same_matrix_refinement")
    is_target = (variant, level) == TARGET_SHARD
    refinement_checks = {
        "applicability_exact": is_target == isinstance(audit, dict),
        "non_target_shard_not_refined": is_target or audit is None,
        "target_shard_refined": not is_target
        or (
            isinstance(audit, dict)
            and audit.get("target_rank") == 104
            and audit.get("iterations") == 3
            and audit.get("matrix_identity") == "EXACT_SAME_MATRIX_AND_CONSTANT"
            and audit.get("selection_rule_pass") is True
        ),
        "owners_restored": _owners_restored(),
        "predecessor_hash_frozen": _predecessor_hash_pass(result_dir),
    }
    payload["shared_checks"]["af0_audit_refinement_contract"] = bool(
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
        raise RuntimeError("KMPC-144 worker refinement contract failed")
    return payload


def run_worker_smoke(
    mode: str,
    k_mpc: float,
    variant: str,
    level: str,
    result_dir: Path,
) -> dict[str, object]:
    if (mode, k_mpc) != TARGET or (variant, level) not in SHARDS:
        raise ValueError("invalid KMPC-144 smoke shard")
    payload = v3.run_worker_smoke(mode, k_mpc, variant, level, result_dir)
    fixture = refinement._fixture()
    guard = successor_contract_guard()
    payload["checks"].update(
        {
            "same_matrix_refinement_contract": bool(guard["pass"]),
            "predecessor_hash_frozen": _predecessor_hash_pass(result_dir),
            "target_shard_exact": TARGET_SHARD == ("af0", "audit"),
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
    if (mode, k_mpc) != TARGET or not _predecessor_hash_pass(result_dir):
        raise RuntimeError("KMPC-144 aggregate identity/predecessor mismatch")
    payload = v3.aggregate_shards(
        mode, k_mpc, shards, result_dir, parent_runtime_seconds
    )
    predecessor = json.loads(
        _predecessor_path(result_dir).read_text(encoding="utf-8")
    )
    diagnostics = payload["variants"]["af0"]["audit_solve"]["m3"][
        "diagnostics"
    ]
    audit = diagnostics.get("same_matrix_refinement")
    checks = {
        "audit_present": isinstance(audit, dict),
        "same_matrix_and_constant": isinstance(audit, dict)
        and audit.get("matrix_identity") == "EXACT_SAME_MATRIX_AND_CONSTANT",
        "rank_104": isinstance(audit, dict) and audit.get("target_rank") == 104,
        "three_iterations": isinstance(audit, dict)
        and len(audit.get("steps", ())) == 3,
        "selection_rule": isinstance(audit, dict)
        and audit.get("selection_rule_pass") is True,
        "driver_pass_after_refinement": diagnostics.get("pass_driver") is True,
        "gamma0_variant_exact_predecessor_parity": payload["variants"]["gamma0"]
        == predecessor["variants"]["gamma0"],
        "af0_accepted_exact_predecessor_parity": payload["variants"]["af0"][
            "accepted_solve"
        ]
        == predecessor["variants"]["af0"]["accepted_solve"],
        "gamma0_audit_not_refined": "same_matrix_refinement"
        not in payload["variants"]["gamma0"]["audit_solve"]["m3"][
            "diagnostics"
        ],
    }
    refinement_pass = all(checks.values())
    pair_pass = bool(payload["pair_pass"] and refinement_pass)
    payload["test"] = (
        "A2-K4 P5.3g7 C3 NID/.15 af0/audit-only same-matrix refinement"
    )
    payload["identity"]["physical_receipt"] = (
        "four_shards_with_af0_audit_only_same_matrix_refinement"
    )
    payload["process_architecture"]["same_matrix_refinement"] = {
        "target_shard": "af0/audit",
        "target_rank": 104,
        "iterations": 3,
        "matrix_rhs_support_threshold_changes": 0,
    }
    payload["same_matrix_refinement_audit"] = {
        "checks": checks,
        "pass": refinement_pass,
        "provenance": audit,
        "selected_driver_metrics": {
            "max_relative_residual": diagnostics.get("max_relative_residual"),
            "max_absolute_fallback_residual": diagnostics.get(
                "max_absolute_fallback_residual"
            ),
            "worst_relative_row": diagnostics.get("worst_relative_row"),
            "worst_absolute_fallback_row": diagnostics.get(
                "worst_absolute_fallback_row"
            ),
        },
    }
    payload["same_matrix_refinement_pass"] = refinement_pass
    payload["pair_pass"] = pair_pass
    payload["candidate_interpretation_not_verdict"] = (
        "PASS_C3_NID_K0P15_AF0_AUDIT_SAME_MATRIX_REFINEMENT_CANDIDATE_ONLY"
        if pair_pass
        else "REVIEW_C3_NID_K0P15_NUMERICAL_BOUNDARY_UNCLOSED"
    )
    return payload


def aggregate_smoke_shards(
    mode: str,
    k_mpc: float,
    shards: Mapping[str, Mapping[str, object]],
) -> dict[str, object]:
    if (mode, k_mpc) != TARGET:
        raise ValueError("KMPC-144 smoke aggregate outside preregistration")
    return v3.aggregate_smoke_shards(mode, k_mpc, shards)
