"""KMPC-133 same-matrix refinement overlay for the C3 CDI/.15 pair.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
No equation, matrix entry, RHS, support, rcond, or threshold is changed.
"""

from __future__ import annotations

from contextlib import contextmanager
from copy import deepcopy
from pathlib import Path
from typing import Iterator, Mapping

from . import c2_cdi_k0p15_same_matrix_refinement as refinement
from . import c3_zero_variant_parallel_v3_support_shards as v3


scientific = v3.scientific
RUN_ID = "KMPC-133"
TARGET = ("CDI", 0.15)
SHARDS = v3.SHARDS
EXPECTED_V3_SHA256 = (
    "7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23"
)
EXPECTED_REFINEMENT_SHA256 = (
    "EA589E4CBAD3AD618DEBC41C81B271EAC23F229AEA82C80E962CD792091468F6"
)
_ORIGINAL_SOLVER = scientific.physics._solve_equilibrated


def sha256_file(path: Path) -> str:
    return scientific.sha256_file(path)


def shard_key(variant: str, level: str) -> str:
    return v3.shard_key(variant, level)


def output_name(mode: str, k_mpc: float) -> str:
    if (mode, k_mpc) != TARGET:
        raise ValueError("KMPC-133 is frozen to CDI/k=0.15")
    return "RUN_KMPC_133_P5_3G7_C3_CDI_K0p15_ZERO_VARIANT_PAIR_SAME_MATRIX_REFINEMENT.json"


def failure_name(mode: str, k_mpc: float) -> str:
    return output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def successor_contract_guard() -> dict[str, object]:
    support = scientific.SUPPORTS[TARGET]
    checks = {
        "target_identity_exact": TARGET == ("CDI", 0.15),
        "support_05_07_exact": support.accepted == (0, 5)
        and support.audit == (0, 7)
        and support.m1_depth == 7,
        "four_shards_exact": SHARDS
        == (("gamma0", "accepted"), ("gamma0", "audit"),
            ("af0", "accepted"), ("af0", "audit")),
        "target_rank_104_exact": refinement.TARGET_RANK == 104,
        "three_iterations_exact": refinement.ITERATIONS == 3,
        "shared_physics_owner": refinement.physics is scientific.physics,
        "original_solver_identity": refinement._ORIGINAL_SOLVER is _ORIGINAL_SOLVER,
        "v3_source_hash_frozen": sha256_file(Path(v3.__file__).resolve())
        == EXPECTED_V3_SHA256,
        "refinement_source_hash_frozen": sha256_file(
            Path(refinement.__file__).resolve()
        ) == EXPECTED_REFINEMENT_SHA256,
    }
    return {"checks": checks, "pass": all(checks.values())}


@contextmanager
def _overlay() -> Iterator[None]:
    if scientific.physics._solve_equilibrated is not _ORIGINAL_SOLVER:
        raise RuntimeError("KMPC-133 solver owner was already modified")
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
        raise ValueError("KMPC-133 worker identity outside preregistration")
    guard = successor_contract_guard()
    with _overlay():
        payload = v3.run_support_worker(
            mode, k_mpc, variant, level, max_runtime_seconds, result_dir
        )
    if not _owners_restored():
        raise RuntimeError("KMPC-133 solver owner was not restored")
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
    payload["run_id"] = RUN_ID
    payload["worker_role"] = "C3_CDI_K0P15_SAME_MATRIX_REFINEMENT_SHARD"
    payload["shared_checks"]["same_matrix_refinement_contract"] = bool(
        guard["pass"]
    )
    payload["same_matrix_refinement_contract"] = guard
    payload["same_matrix_refinement_worker_checks"] = refinement_checks
    payload["source_hashes"].update({
        "c2_cdi_k0p15_same_matrix_refinement.py": sha256_file(
            Path(refinement.__file__).resolve()
        ),
        "c3_zero_variant_parallel_v5_cdi_k0p15_same_matrix_refinement.py": sha256_file(
            Path(__file__).resolve()
        ),
    })
    if not all(refinement_checks.values()):
        raise RuntimeError("KMPC-133 worker refinement contract failed")
    return payload


def run_worker_smoke(
    mode: str,
    k_mpc: float,
    variant: str,
    level: str,
    result_dir: Path,
) -> dict[str, object]:
    if (mode, k_mpc) != TARGET or (variant, level) not in SHARDS:
        raise ValueError("invalid KMPC-133 smoke shard")
    payload = v3.run_worker_smoke(mode, k_mpc, variant, level, result_dir)
    fixture = refinement._fixture()
    guard = successor_contract_guard()
    payload["run_id"] = RUN_ID
    payload["worker_role"] = "C3_CDI_K0P15_SAME_MATRIX_REFINEMENT_SHARD_SMOKE"
    payload["checks"].update({
        "same_matrix_refinement_contract": bool(guard["pass"]),
        **{f"refinement_fixture_{key}": value for key, value in fixture.items()},
        "owners_restored": _owners_restored(),
    })
    payload["pass"] = all(payload["checks"].values())
    payload["physics_executed"] = False
    return payload


def _require_shard(
    payload: Mapping[str, object], variant: str, level: str
) -> None:
    if payload.get("run_id") != RUN_ID:
        raise RuntimeError(f"KMPC-133 run identity mismatch: {variant}/{level}")
    if payload.get("worker_role") != "C3_CDI_K0P15_SAME_MATRIX_REFINEMENT_SHARD":
        raise RuntimeError(f"KMPC-133 worker role mismatch: {variant}/{level}")
    if payload.get("identity") != {
        "mode": TARGET[0],
        "k_Mpc_inverse": TARGET[1],
        "variant": variant,
        "support_level": level,
    }:
        raise RuntimeError(f"KMPC-133 shard identity mismatch: {variant}/{level}")
    checks = payload.get("same_matrix_refinement_worker_checks")
    if not isinstance(checks, dict) or not all(checks.values()):
        raise RuntimeError(f"KMPC-133 refinement checks failed: {variant}/{level}")


def aggregate_shards(
    shards: Mapping[str, Mapping[str, object]],
    result_dir: Path,
    parent_runtime_seconds: float,
) -> dict[str, object]:
    expected = {shard_key(variant, level) for variant, level in SHARDS}
    if set(shards) != expected:
        raise RuntimeError("KMPC-133 exact four-shard register mismatch")
    normalized: dict[str, dict[str, object]] = {}
    for variant, level in SHARDS:
        key = shard_key(variant, level)
        _require_shard(shards[key], variant, level)
        row = deepcopy(shards[key])
        row["run_id"] = v3.RUN_ID
        row["worker_role"] = "C3_ZERO_VARIANT_SUPPORT_SHARD"
        normalized[key] = row
    payload = v3.aggregate_shards(
        TARGET[0], TARGET[1], normalized, result_dir, parent_runtime_seconds
    )
    refinement_audit: dict[str, object] = {}
    for variant in ("gamma0", "af0"):
        diagnostics = payload["variants"][variant]["audit_solve"]["m3"][
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
        }
        refinement_audit[variant] = {
            "checks": checks,
            "pass": all(checks.values()),
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
    refinement_pass = all(row["pass"] for row in refinement_audit.values())
    pair_pass = bool(payload["pair_pass"] and refinement_pass)
    payload["run_id"] = RUN_ID
    payload["test"] = (
        "A2-K4 P5.3g7 C3 CDI/.15 four-shard same-matrix refinement receipt"
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
        "PASS_C3_CDI_K0P15_ZERO_PAIR_SAME_MATRIX_REFINEMENT_CANDIDATE_ONLY"
        if pair_pass
        else "REVIEW_C3_CDI_K0P15_NUMERICAL_BOUNDARY_UNCLOSED"
    )
    return payload


def aggregate_smoke_shards(
    shards: Mapping[str, Mapping[str, object]],
) -> dict[str, object]:
    expected = {shard_key(variant, level) for variant, level in SHARDS}
    checks: dict[str, bool] = {"exact_four_shard_register": set(shards) == expected}
    for variant, level in SHARDS:
        key = shard_key(variant, level)
        row = shards.get(key)
        checks[key] = bool(
            isinstance(row, dict)
            and row.get("run_id") == RUN_ID
            and row.get("worker_role")
            == "C3_CDI_K0P15_SAME_MATRIX_REFINEMENT_SHARD_SMOKE"
            and row.get("identity")
            == {
                "mode": TARGET[0],
                "k_Mpc_inverse": TARGET[1],
                "variant": variant,
                "support_level": level,
            }
            and row.get("pass") is True
            and row.get("physics_executed") is False
        )
    return {
        "run_id": RUN_ID,
        "identity": {"mode": TARGET[0], "k_Mpc_inverse": TARGET[1]},
        "checks": checks,
        "pass": all(checks.values()),
        "physics_executed": False,
    }
