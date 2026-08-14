"""KMPC-129 process-only successor for parallel C3 zero-variant workers.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
No physical equation, support, input or threshold is changed from KMPC-128.
"""

from __future__ import annotations

import math
from pathlib import Path
import time
from typing import Mapping

from . import c3_zero_variant_pair as v1


RUN_ID = "KMPC-129"
MODES = v1.MODES
K_VALUES = v1.K_VALUES
VARIANTS = v1.VARIANTS


def sha256_file(path: Path) -> str:
    return v1.sha256_file(path)


def output_name(mode: str, k_mpc: float) -> str:
    if (mode, k_mpc) not in v1.SUPPORTS:
        raise ValueError("KMPC-129 pair identity outside frozen matrix")
    return f"RUN_KMPC_129_P5_3G7_C3_{mode}_K{v1.k_token(k_mpc)}_ZERO_VARIANT_PAIR.json"


def failure_name(mode: str, k_mpc: float) -> str:
    return output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def run_variant_worker(
    mode: str,
    k_mpc: float,
    variant: str,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    if variant not in VARIANTS or (mode, k_mpc) not in v1.SUPPORTS:
        raise ValueError("KMPC-129 worker identity outside frozen matrix")
    started, deadline = v1._make_deadline(max_runtime_seconds)
    nominal = v1._load_nominal_reference(result_dir, mode, k_mpc)
    deadline()
    guard = v1.contract_guard()
    frozen_contract = v1.physics.validate_frozen_contract()
    independent_contract = v1.c2.ra_contract.validate_contract(
        v1.c2.collective_contract.EXPECTED_STATE,
        v1.c2.collective_contract.EXPECTED_DRIVER,
        v1.c2.collective_contract.EXPECTED_HOLDOUT,
    )
    frozen_b1 = v1.physics.b1_guard.build_contract_guard(
        max_runtime_seconds=min(1.0, max_runtime_seconds)
    )
    tca0 = v1.physics.production_tca0_reduction_guard()
    shared_checks = {
        "C3_contract": bool(guard["pass"]),
        "nominal_reference": True,
        "frozen_contract": bool(frozen_contract["valid"]),
        "independent_contract": bool(independent_contract.valid),
        "B1_left_null_Bianchi": (
            frozen_b1["execution_verdict"]
            == "PASS_R_A_B1_CONTRACT_GUARD_ONLY"
        ),
        "production_TCA0_bridge": bool(tca0["pass"]),
    }
    support = v1.SUPPORTS[(mode, k_mpc)]
    standard, m1 = v1.c2._standard_depth(
        mode,
        k_mpc,
        support.m1_depth,
        v1.physics._variant_inputs("nominal"),
        deadline,
    )
    result = v1._solve_variant(
        mode,
        k_mpc,
        variant,
        support,
        standard,
        m1,
        nominal,
        shared_checks,
        deadline,
    )
    deadline()
    payload = {
        "run_id": RUN_ID,
        "worker_role": "C3_ZERO_VARIANT_ISOLATED_WORKER",
        "identity": {
            "mode": mode,
            "k_Mpc_inverse": k_mpc,
            "variant": variant,
        },
        "authorship": {
            "theory_author": "Martin Jambor",
            "script_creator": "Codex (OpenAI)",
        },
        "nominal_reference": {
            key: value for key, value in nominal.items() if key != "states"
        },
        "contract_guard": guard,
        "frozen_contract": frozen_contract,
        "independent_contract_valid": independent_contract.valid,
        "frozen_B1_left_null_Bianchi": frozen_b1,
        "production_TCA0_bridge": tca0,
        "support_depth_spec": {
            "accepted": list(support.accepted),
            "audit": list(support.audit),
            "M1_depth": support.m1_depth,
        },
        "M1": m1,
        "variant_result": result,
        "thresholds": {
            "driver": v1.physics.DRIVER_TOL,
            "holdout": v1.physics.HOLDOUT_TOL,
            "common": v1.physics.LOW_COEFFICIENT_TOL,
            "tail": v1.physics.TAIL_TOL,
            "absolute_fallback": v1.physics.ABS_FALLBACK_TOL,
            "background_relative": v1.physics.BACKGROUND_K_TOL,
        },
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "physics_verdict": "NONE_WORKER_EVIDENCE_ONLY",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
        "source_hashes": {
            "c3_zero_variant_pair.py": sha256_file(Path(v1.__file__).resolve()),
            "c3_zero_variant_parallel.py": sha256_file(Path(__file__).resolve()),
        },
    }
    if not v1.c2.finite_owner._all_finite(payload):
        raise FloatingPointError("non-finite value in KMPC-129 worker payload")
    return payload


def run_worker_smoke(
    mode: str, k_mpc: float, variant: str, result_dir: Path
) -> dict[str, object]:
    if variant not in VARIANTS:
        raise ValueError(variant)
    base_smoke = v1.run_smoke(mode, k_mpc, result_dir)
    checks = {
        "KMPC128_schema_smoke": bool(base_smoke["pass"]),
        "variant_identity": variant in VARIANTS,
        "worker_does_not_write": True,
        "physics_executed": False,
    }
    return {
        "run_id": RUN_ID,
        "worker_role": "C3_ZERO_VARIANT_SMOKE_WORKER",
        "identity": {"mode": mode, "k_Mpc_inverse": k_mpc, "variant": variant},
        "checks": checks,
        "pass": all(checks.values()),
        "physics_executed": False,
    }


def _require_worker(
    payload: Mapping[str, object], mode: str, k_mpc: float, variant: str
) -> None:
    if payload.get("run_id") != RUN_ID:
        raise RuntimeError(f"{variant} worker run_id mismatch")
    if payload.get("worker_role") != "C3_ZERO_VARIANT_ISOLATED_WORKER":
        raise RuntimeError(f"{variant} worker role mismatch")
    if payload.get("identity") != {
        "mode": mode,
        "k_Mpc_inverse": k_mpc,
        "variant": variant,
    }:
        raise RuntimeError(f"{variant} worker identity mismatch")
    if payload.get("runtime_limit_seconds") != 4.8:
        raise RuntimeError(f"{variant} worker runtime limit mismatch")
    runtime = payload.get("runtime_seconds")
    if isinstance(runtime, bool) or not isinstance(runtime, (int, float)):
        raise TypeError(f"{variant} worker runtime is not numeric")
    if not math.isfinite(float(runtime)) or float(runtime) > 4.8:
        raise RuntimeError(f"{variant} worker runtime exceeded")


def aggregate_workers(
    mode: str,
    k_mpc: float,
    workers: Mapping[str, Mapping[str, object]],
    parent_runtime_seconds: float,
) -> dict[str, object]:
    if set(workers) != set(VARIANTS):
        raise RuntimeError("KMPC-129 exact two-worker register mismatch")
    for variant in VARIANTS:
        _require_worker(workers[variant], mode, k_mpc, variant)
    gamma0 = workers["gamma0"]
    af0 = workers["af0"]
    parity_checks = {
        "nominal_reference": gamma0.get("nominal_reference") == af0.get("nominal_reference"),
        "contract_guard": gamma0.get("contract_guard") == af0.get("contract_guard"),
        "support_depth_spec": gamma0.get("support_depth_spec") == af0.get("support_depth_spec"),
        "M1_recomputed_exact_parity": gamma0.get("M1") == af0.get("M1"),
        "thresholds": gamma0.get("thresholds") == af0.get("thresholds"),
        "source_hashes": gamma0.get("source_hashes") == af0.get("source_hashes"),
    }
    if not all(parity_checks.values()):
        raise RuntimeError(
            "KMPC-129 worker shared-contract parity failed: "
            + ",".join(name for name, passed in parity_checks.items() if not passed)
        )
    variants = {
        variant: workers[variant]["variant_result"] for variant in VARIANTS
    }
    pair_pass = all(
        isinstance(result, dict) and result.get("logical_atom_pass") is True
        for result in variants.values()
    )
    candidate = (
        "PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY"
        if pair_pass
        else "REVIEW_C3_ZERO_VARIANT_PAIR_UNCLOSED"
    )
    return {
        "test": "A2-K4 P5.3g7 C3 parallel gamma0/af0 pair receipt",
        "run_id": RUN_ID,
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "candidate_interpretation_not_verdict": candidate,
        "authorship": {
            "theory_author": "Martin Jambor",
            "script_creator": "Codex (OpenAI)",
        },
        "identity": {
            "mode": mode,
            "k_Mpc_inverse": k_mpc,
            "physical_receipt": "parallel_gamma0_af0_pair",
        },
        "logical_atom_accounting": {
            "existing_nominal": 1,
            "new_zero_variants": 2,
            "total": 3,
        },
        "scope": {
            "included": "one mode-k C3 pair from two isolated bounded workers",
            "excluded": "other mode-k pairs, S-M, finite opacity, full hierarchy, P5.4, G8/G9 and data",
        },
        "process_architecture": {
            "parallel_workers": list(VARIANTS),
            "worker_internal_limit_seconds": 4.8,
            "worker_intermediate_files": 0,
            "shared_M1_memory_object": False,
            "M1_recomputed_exact_parity": parity_checks["M1_recomputed_exact_parity"],
        },
        "worker_parity_checks": parity_checks,
        "nominal_reference": gamma0["nominal_reference"],
        "contract_guard": gamma0["contract_guard"],
        "frozen_contract": gamma0["frozen_contract"],
        "independent_contract_valid": gamma0["independent_contract_valid"],
        "frozen_B1_left_null_Bianchi": gamma0["frozen_B1_left_null_Bianchi"],
        "production_TCA0_bridge": gamma0["production_TCA0_bridge"],
        "support_depth_spec": gamma0["support_depth_spec"],
        "M1": gamma0["M1"],
        "variants": variants,
        "worker_runtime_seconds": {
            variant: workers[variant]["runtime_seconds"] for variant in VARIANTS
        },
        "pair_pass": pair_pass,
        "thresholds": gamma0["thresholds"],
        "source_hashes": gamma0["source_hashes"],
        "runtime_seconds": parent_runtime_seconds,
        "score_effect": "NONE",
        "K4_score_effect": "NONE_60_OF_100_UNCHANGED",
        "release_trigger": "NONE",
        "zenodo_trigger": "NONE",
        "prediction_table_effect": "NONE",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }


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
