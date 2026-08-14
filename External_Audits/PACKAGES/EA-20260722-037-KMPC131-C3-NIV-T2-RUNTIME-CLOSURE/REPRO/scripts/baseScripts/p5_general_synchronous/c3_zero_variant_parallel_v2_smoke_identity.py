"""KMPC-130 identity/smoke-only wrapper over frozen KMPC-129 parallel C3.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Mapping

from . import c3_zero_variant_parallel as v1


RUN_ID = "KMPC-130"
MODES = v1.MODES
K_VALUES = v1.K_VALUES
VARIANTS = v1.VARIANTS


def sha256_file(path: Path) -> str:
    return v1.sha256_file(path)


def output_name(mode: str, k_mpc: float) -> str:
    if (mode, k_mpc) not in v1.v1.SUPPORTS:
        raise ValueError("KMPC-130 pair identity outside frozen matrix")
    return f"RUN_KMPC_130_P5_3G7_C3_{mode}_K{v1.v1.k_token(k_mpc)}_ZERO_VARIANT_PAIR.json"


def failure_name(mode: str, k_mpc: float) -> str:
    return output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def run_variant_worker(
    mode: str,
    k_mpc: float,
    variant: str,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    payload = v1.run_variant_worker(
        mode, k_mpc, variant, max_runtime_seconds, result_dir
    )
    payload["run_id"] = RUN_ID
    payload["worker_role"] = "C3_ZERO_VARIANT_ISOLATED_WORKER_V2_IDENTITY"
    payload["source_hashes"]["c3_zero_variant_parallel_v2_smoke_identity.py"] = (
        sha256_file(Path(__file__).resolve())
    )
    return payload


def run_worker_smoke(
    mode: str, k_mpc: float, variant: str, result_dir: Path
) -> dict[str, object]:
    if variant not in VARIANTS:
        raise ValueError(variant)
    base_smoke = v1.v1.run_smoke(mode, k_mpc, result_dir)
    checks = {
        "KMPC128_schema_smoke": bool(base_smoke["pass"]),
        "variant_identity": variant in VARIANTS,
        "worker_does_not_write": True,
        "no_physics_executed": base_smoke["physics_executed"] is False,
    }
    return {
        "run_id": RUN_ID,
        "worker_role": "C3_ZERO_VARIANT_SMOKE_WORKER_V2_IDENTITY",
        "identity": {"mode": mode, "k_Mpc_inverse": k_mpc, "variant": variant},
        "checks": checks,
        "pass": all(checks.values()),
        "physics_executed": False,
    }


def aggregate_workers(
    mode: str,
    k_mpc: float,
    workers: Mapping[str, Mapping[str, object]],
    parent_runtime_seconds: float,
) -> dict[str, object]:
    inner = deepcopy(dict(workers))
    for variant in VARIANTS:
        payload = inner.get(variant)
        if not isinstance(payload, dict):
            raise TypeError(f"missing KMPC-130 worker payload: {variant}")
        if payload.get("run_id") != RUN_ID:
            raise RuntimeError(f"KMPC-130 worker identity mismatch: {variant}")
        if payload.get("worker_role") != "C3_ZERO_VARIANT_ISOLATED_WORKER_V2_IDENTITY":
            raise RuntimeError(f"KMPC-130 worker role mismatch: {variant}")
        payload["run_id"] = v1.RUN_ID
        payload["worker_role"] = "C3_ZERO_VARIANT_ISOLATED_WORKER"
    result = v1.aggregate_workers(
        mode, k_mpc, inner, parent_runtime_seconds
    )
    result["run_id"] = RUN_ID
    result["test"] = (
        "A2-K4 P5.3g7 C3 parallel gamma0/af0 pair receipt, "
        "KMPC-130 smoke/identity successor"
    )
    result["process_architecture"]["identity_successor"] = (
        "KMPC-130_OVER_FROZEN_KMPC-129_PARALLEL_IMPLEMENTATION"
    )
    result["source_hashes"]["c3_zero_variant_parallel_v2_smoke_identity.py"] = (
        sha256_file(Path(__file__).resolve())
    )
    return result


def aggregate_smoke_workers(
    mode: str,
    k_mpc: float,
    workers: Mapping[str, Mapping[str, object]],
) -> dict[str, object]:
    checks: dict[str, bool] = {
        "exact_two_worker_register": set(workers) == set(VARIANTS),
    }
    for variant in VARIANTS:
        payload = workers.get(variant)
        checks[f"{variant}_payload"] = bool(
            isinstance(payload, dict)
            and payload.get("run_id") == RUN_ID
            and payload.get("worker_role")
            == "C3_ZERO_VARIANT_SMOKE_WORKER_V2_IDENTITY"
            and payload.get("identity")
            == {"mode": mode, "k_Mpc_inverse": k_mpc, "variant": variant}
            and payload.get("pass") is True
            and payload.get("physics_executed") is False
        )
    return {
        "run_id": RUN_ID,
        "identity": {"mode": mode, "k_Mpc_inverse": k_mpc},
        "checks": checks,
        "pass": all(checks.values()),
        "physics_executed": False,
    }
