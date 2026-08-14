"""KMPC-132 AD/.05 C3 support successor with six isolated shards.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
The frozen KMPC-128 equations and gates are reused without modification.
"""

from __future__ import annotations

from pathlib import Path
import time
from typing import Mapping

from . import c3_zero_variant_parallel_v3_support_shards as v3


scientific = v3.scientific
RUN_ID = "KMPC-132"
TARGET = ("AD", 0.05)
BASE_SUPPORTS = dict(scientific.SUPPORTS)
ORIGINAL_SUPPORT = BASE_SUPPORTS[TARGET]
SUCCESSOR_SUPPORT = scientific.SupportSpec((0, 4), (0, 6), 6)
VARIANTS = ("nominal", "gamma0", "af0")
SUPPORT_LEVELS = ("accepted", "audit")
SHARDS = tuple(
    (variant, level) for variant in VARIANTS for level in SUPPORT_LEVELS
)
EXPECTED_V3_SHA256 = (
    "7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23"
)


def sha256_file(path: Path) -> str:
    return scientific.sha256_file(path)


def shard_key(variant: str, level: str) -> str:
    if (variant, level) not in SHARDS:
        raise ValueError(f"unsupported KMPC-132 shard {variant}/{level}")
    return f"{variant}/{level}"


def output_name(mode: str, k_mpc: float) -> str:
    if (mode, k_mpc) != TARGET:
        raise ValueError("KMPC-132 is frozen to AD/k=0.05")
    return "RUN_KMPC_132_P5_3G7_C3_AD_K0p05_ZERO_VARIANT_PAIR_SUPPORT_04_06.json"


def failure_name(mode: str, k_mpc: float) -> str:
    return output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def _activate_successor_support() -> None:
    scientific.SUPPORTS[TARGET] = SUCCESSOR_SUPPORT


def _load_original_nominal(result_dir: Path) -> dict[str, object]:
    observed = scientific.SUPPORTS[TARGET]
    scientific.SUPPORTS[TARGET] = ORIGINAL_SUPPORT
    try:
        return scientific._load_nominal_reference(result_dir, *TARGET)
    finally:
        scientific.SUPPORTS[TARGET] = observed


def successor_contract_guard() -> dict[str, object]:
    _activate_successor_support()
    inherited = scientific.contract_guard()
    unchanged_others = all(
        scientific.SUPPORTS[key] == value
        for key, value in BASE_SUPPORTS.items()
        if key != TARGET
    )
    checks = {
        "inherited_C3_contract": bool(inherited["pass"]),
        "target_identity_exact": TARGET == ("AD", 0.05),
        "original_support_exact": ORIGINAL_SUPPORT
        == scientific.SupportSpec((0, 2), (0, 4), 5),
        "successor_support_exact": scientific.SUPPORTS[TARGET]
        == scientific.SupportSpec((0, 4), (0, 6), 6),
        "all_other_supports_unchanged": unchanged_others,
        "six_shards_exact": SHARDS
        == tuple(
            (variant, level)
            for variant in ("nominal", "gamma0", "af0")
            for level in ("accepted", "audit")
        ),
        "v3_source_hash_frozen": sha256_file(Path(v3.__file__).resolve())
        == EXPECTED_V3_SHA256,
    }
    return {"inherited": inherited, "checks": checks, "pass": all(checks.values())}


def _source_hashes() -> dict[str, str]:
    return {
        "c3_zero_variant_pair.py": sha256_file(Path(scientific.__file__).resolve()),
        "c3_zero_variant_parallel_v3_support_shards.py": sha256_file(
            Path(v3.__file__).resolve()
        ),
        "c3_zero_variant_parallel_v4_ad_k0p05_support_04_06.py": sha256_file(
            Path(__file__).resolve()
        ),
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
        raise ValueError("KMPC-132 support-worker identity outside preregistration")
    started, deadline = scientific._make_deadline(max_runtime_seconds)
    nominal_reference = _load_original_nominal(result_dir)
    deadline()
    guard = successor_contract_guard()
    frozen_contract = scientific.physics.validate_frozen_contract()
    independent_contract = scientific.c2.ra_contract.validate_contract(
        scientific.c2.collective_contract.EXPECTED_STATE,
        scientific.c2.collective_contract.EXPECTED_DRIVER,
        scientific.c2.collective_contract.EXPECTED_HOLDOUT,
    )
    frozen_b1 = scientific.physics.b1_guard.build_contract_guard(
        max_runtime_seconds=min(1.0, max_runtime_seconds)
    )
    tca0 = scientific.physics.production_tca0_reduction_guard()
    shared_checks = {
        "C3_successor_contract": bool(guard["pass"]),
        "original_nominal_reference": True,
        "frozen_contract": bool(frozen_contract["valid"]),
        "independent_contract": bool(independent_contract.valid),
        "B1_left_null_Bianchi": (
            frozen_b1["execution_verdict"]
            == "PASS_R_A_B1_CONTRACT_GUARD_ONLY"
        ),
        "production_TCA0_bridge": bool(tca0["pass"]),
    }
    support = scientific.SUPPORTS[TARGET]
    standard, m1 = scientific.c2._standard_depth(
        mode,
        k_mpc,
        support.m1_depth,
        scientific.physics._variant_inputs("nominal"),
        deadline,
    )
    inputs = scientific.physics._variant_inputs(variant)
    rfs = scientific.c2._rfs_guard(mode, standard, inputs)
    selected_support = support.accepted if level == "accepted" else support.audit
    solve = scientific.c2._solve_support(
        mode, k_mpc, selected_support, inputs, standard, deadline
    )
    deadline()
    payload = {
        "run_id": RUN_ID,
        "worker_role": "C3_SUPPORT_04_06_SHARD",
        "identity": {
            "mode": mode,
            "k_Mpc_inverse": k_mpc,
            "variant": variant,
            "support_level": level,
        },
        "authorship": {
            "theory_author": "Martin Jambor",
            "script_creator": "Codex (OpenAI)",
        },
        "original_nominal_reference": {
            key: value
            for key, value in nominal_reference.items()
            if key != "states"
        },
        "successor_contract_guard": guard,
        "frozen_contract": frozen_contract,
        "independent_contract_valid": independent_contract.valid,
        "frozen_B1_left_null_Bianchi": frozen_b1,
        "production_TCA0_bridge": tca0,
        "shared_checks": shared_checks,
        "support_depth_spec": {
            "accepted": list(support.accepted),
            "audit": list(support.audit),
            "M1_depth": support.m1_depth,
        },
        "selected_support": list(selected_support),
        "M1": m1,
        "standard_state": standard,
        "combined_R_fs_guard": rfs,
        "solve": solve,
        "thresholds": {
            "driver": scientific.physics.DRIVER_TOL,
            "holdout": scientific.physics.HOLDOUT_TOL,
            "common": scientific.physics.LOW_COEFFICIENT_TOL,
            "tail": scientific.physics.TAIL_TOL,
            "absolute_fallback": scientific.physics.ABS_FALLBACK_TOL,
            "background_relative": scientific.physics.BACKGROUND_K_TOL,
        },
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "physics_verdict": "NONE_SUPPORT_SHARD_EVIDENCE_ONLY",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
        "source_hashes": _source_hashes(),
    }
    if not scientific.c2.finite_owner._all_finite(payload):
        raise FloatingPointError("non-finite KMPC-132 support-worker payload")
    return payload


def run_worker_smoke(
    mode: str,
    k_mpc: float,
    variant: str,
    level: str,
    result_dir: Path,
) -> dict[str, object]:
    if (mode, k_mpc) != TARGET or (variant, level) not in SHARDS:
        raise ValueError("invalid KMPC-132 smoke shard")
    nominal = _load_original_nominal(result_dir)
    guard = successor_contract_guard()
    inputs = scientific.physics._variant_inputs(variant)
    checks = {
        "successor_contract": bool(guard["pass"]),
        "original_nominal_loaded": nominal["sha256"]
        == scientific._nominal_spec(*TARGET).sha256,
        "variant_identity": (
            (variant == "nominal" and inputs.lam != 0.0 and inputs.af != 0.0)
            or (variant == "gamma0" and inputs.lam == 0.0 and inputs.af != 0.0)
            or (variant == "af0" and inputs.af == 0.0 and inputs.lam != 0.0)
        ),
        "shard_identity": (variant, level) in SHARDS,
        "worker_does_not_write": True,
        "no_physics_executed": True,
    }
    return {
        "run_id": RUN_ID,
        "worker_role": "C3_SUPPORT_04_06_SHARD_SMOKE",
        "identity": {
            "mode": mode,
            "k_Mpc_inverse": k_mpc,
            "variant": variant,
            "support_level": level,
        },
        "checks": checks,
        "pass": all(checks.values()),
        "physics_executed": False,
    }


def _require_shard(
    payload: Mapping[str, object],
    variant: str,
    level: str,
) -> None:
    if payload.get("run_id") != RUN_ID or payload.get("worker_role") != "C3_SUPPORT_04_06_SHARD":
        raise RuntimeError(f"worker contract mismatch: {variant}/{level}")
    if payload.get("identity") != {
        "mode": TARGET[0],
        "k_Mpc_inverse": TARGET[1],
        "variant": variant,
        "support_level": level,
    }:
        raise RuntimeError(f"worker identity mismatch: {variant}/{level}")
    if payload.get("runtime_limit_seconds") != 4.8:
        raise RuntimeError(f"worker runtime limit mismatch: {variant}/{level}")
    runtime = payload.get("runtime_seconds")
    if isinstance(runtime, bool) or not isinstance(runtime, (int, float)):
        raise TypeError(f"worker runtime is not numeric: {variant}/{level}")
    if not 0.0 <= float(runtime) <= 4.8:
        raise RuntimeError(f"worker runtime exceeded: {variant}/{level}")


def _bridge_pair(
    left: Mapping[str, object],
    right: Mapping[str, object],
    support: tuple[int, int],
) -> dict[str, object]:
    f0 = scientific.c2._common_bridge(left["F0"], right["F0"], support)
    m3 = scientific.c2._common_bridge(left["M3"], right["M3"], support)
    return {"F0": f0, "M3": m3, "pass": bool(f0["pass"] and m3["pass"])}


def _nominal_checkpoint(
    accepted_worker: Mapping[str, object],
    audit_worker: Mapping[str, object],
    original_nominal: Mapping[str, object],
) -> dict[str, object]:
    support = SUCCESSOR_SUPPORT
    accepted = v3._restore_solve(accepted_worker["solve"], "nominal.accepted")
    audit = v3._restore_solve(audit_worker["solve"], "nominal.audit")
    accepted_states = {
        "F0": accepted["fuel"]["state"],
        "M3": accepted["m3"]["fractional_state"],
    }
    audit_states = {
        "F0": audit["fuel"]["state"],
        "M3": audit["m3"]["fractional_state"],
    }
    old_states = original_nominal.get("states")
    if not isinstance(old_states, dict):
        raise TypeError("original nominal state bundle missing")
    lineage = {
        "old_accepted_02_to_new_accepted_04": _bridge_pair(
            old_states["accepted"], accepted_states, ORIGINAL_SUPPORT.accepted
        ),
        "old_audit_04_to_new_accepted_04": _bridge_pair(
            old_states["audit"], accepted_states, ORIGINAL_SUPPORT.audit
        ),
    }
    lineage_pass = all(row["pass"] for row in lineage.values())
    common = _bridge_pair(accepted_states, audit_states, support.accepted)
    tails = {
        "F0": scientific.c2._tail(
            audit["fuel"]["state"],
            tuple(sorted(audit["fuel"]["state"])),
            support.accepted,
            support.audit,
        ),
        "M3": scientific.c2._tail(
            audit["m3"]["fractional_state"],
            tuple(scientific.c2.ra_contract.AUTHORITATIVE_STATE),
            support.accepted,
            support.audit,
        ),
    }
    tail_pass = all(row["pass"] for row in tails.values())
    s_c0 = scientific.c2.support_tools.c1._s_c0_actual_coefficient_guard({
        "m3_primary": {"fractional_state": accepted["m3"]["fractional_state"]},
        "m3_extended": {"fractional_state": audit["m3"]["fractional_state"]},
    })
    inputs = scientific.physics._variant_inputs("nominal")
    background = scientific.c2._background_guard(inputs, TARGET[1], support.audit[1])
    shared = accepted_worker["shared_checks"]
    if not isinstance(shared, dict):
        raise TypeError("nominal shared check schema mismatch")
    core_checks = {
        **shared,
        "M1": bool(accepted_worker["M1"]["pass"] and audit_worker["M1"]["pass"]),
        "combined_R_fs": bool(
            accepted_worker["combined_R_fs_guard"]["pass"]
            and audit_worker["combined_R_fs_guard"]["pass"]
        ),
        "accepted_solve": bool(accepted["pass"]),
        "audit_solve": bool(audit["pass"]),
        "S_C0_actual": bool(s_c0["pass"]),
    }
    checkpoint_pass = bool(
        all(core_checks.values())
        and lineage_pass
        and common["pass"]
        and tail_pass
        and background["pass"]
    )
    return {
        "role": "DEEPER_NOMINAL_SUPPORT_CHECKPOINT_NOT_NEW_LOGICAL_ATOM",
        "candidate_interpretation_not_verdict": (
            "PASS_NOMINAL_SUPPORT_CHECKPOINT_CANDIDATE_ONLY"
            if checkpoint_pass
            else "REVIEW_C3_NOMINAL_SUPPORT_CHECKPOINT_UNCLOSED"
        ),
        "core_checks": core_checks,
        "lineage_bridges": lineage,
        "lineage_pass": lineage_pass,
        "accepted_solve": accepted,
        "audit_solve": audit,
        "common": common,
        "tails": tails,
        "tail_pass": tail_pass,
        "S_C0_actual_guard": s_c0,
        "background_guard": background,
        "checkpoint_pass": checkpoint_pass,
        "support_worker_runtime_seconds": {
            "accepted": accepted_worker["runtime_seconds"],
            "audit": audit_worker["runtime_seconds"],
        },
    }


def aggregate_shards(
    shards: Mapping[str, Mapping[str, object]],
    result_dir: Path,
    parent_runtime_seconds: float,
) -> dict[str, object]:
    expected_keys = {shard_key(variant, level) for variant, level in SHARDS}
    if set(shards) != expected_keys:
        raise RuntimeError("KMPC-132 exact six-shard register mismatch")
    for variant, level in SHARDS:
        _require_shard(shards[shard_key(variant, level)], variant, level)
    rows = list(shards.values())
    first = rows[0]
    parity_checks = {
        "original_nominal_reference": all(
            row["original_nominal_reference"] == first["original_nominal_reference"]
            for row in rows
        ),
        "successor_contract_guard": all(
            row["successor_contract_guard"] == first["successor_contract_guard"]
            for row in rows
        ),
        "support_depth_spec": all(
            row["support_depth_spec"] == first["support_depth_spec"] for row in rows
        ),
        "M1_recomputed_exact_parity": all(row["M1"] == first["M1"] for row in rows),
        "standard_state_exact_parity": all(
            row["standard_state"] == first["standard_state"] for row in rows
        ),
        "thresholds": all(row["thresholds"] == first["thresholds"] for row in rows),
        "source_hashes": all(row["source_hashes"] == first["source_hashes"] for row in rows),
    }
    if not all(parity_checks.values()):
        raise RuntimeError(
            "KMPC-132 shared parity failed: "
            + ",".join(name for name, passed in parity_checks.items() if not passed)
        )
    original_nominal = _load_original_nominal(result_dir)
    _activate_successor_support()
    checkpoint = _nominal_checkpoint(
        shards[shard_key("nominal", "accepted")],
        shards[shard_key("nominal", "audit")],
        original_nominal,
    )
    deeper_nominal = {
        "states": {
            "accepted": {
                "F0": checkpoint["accepted_solve"]["fuel"]["state"],
                "M3": checkpoint["accepted_solve"]["m3"]["fractional_state"],
            },
            "audit": {
                "F0": checkpoint["audit_solve"]["fuel"]["state"],
                "M3": checkpoint["audit_solve"]["m3"]["fractional_state"],
            },
        }
    }
    variants = {
        variant: v3._variant_from_shards(
            TARGET[0],
            TARGET[1],
            variant,
            shards[shard_key(variant, "accepted")],
            shards[shard_key(variant, "audit")],
            deeper_nominal,
        )
        for variant in ("gamma0", "af0")
    }
    zero_pair_pass = all(row["logical_atom_pass"] for row in variants.values())
    pair_pass = bool(checkpoint["checkpoint_pass"] and zero_pair_pass)
    if not checkpoint["checkpoint_pass"]:
        candidate = "REVIEW_C3_NOMINAL_SUPPORT_CHECKPOINT_UNCLOSED"
    elif pair_pass:
        candidate = "PASS_C3_AD_K0P05_ZERO_PAIR_SUPPORT_04_ADEQUATE_CANDIDATE_ONLY"
    else:
        candidate = "REVIEW_C3_ZERO_VARIANT_PAIR_UNCLOSED"
    payload = {
        "test": "A2-K4 P5.3g7 C3 AD/.05 support 04/06 six-shard successor",
        "run_id": RUN_ID,
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "candidate_interpretation_not_verdict": candidate,
        "authorship": {
            "theory_author": "Martin Jambor",
            "script_creator": "Codex (OpenAI)",
        },
        "identity": {
            "mode": TARGET[0],
            "k_Mpc_inverse": TARGET[1],
            "physical_receipt": "zero_pair_support_04_06_with_nominal_checkpoint",
        },
        "logical_atom_accounting": {
            "existing_nominal": 1,
            "new_zero_variants": 2,
            "nominal_support_checkpoint_new_logical_atoms": 0,
            "technical_support_shards": 6,
            "total_logical_atoms": 3,
        },
        "scope": {
            "included": "AD/.05 C3 support successor only",
            "excluded": "AD/.15, other modes, S-M, P5.4, G8/G9 and data",
        },
        "process_architecture": {
            "parallel_support_workers": sorted(expected_keys),
            "worker_internal_limit_seconds": 4.8,
            "worker_intermediate_files": 0,
            "parent_solver_calls": 0,
        },
        "worker_parity_checks": parity_checks,
        "original_nominal_reference": {
            key: value for key, value in original_nominal.items() if key != "states"
        },
        "successor_contract_guard": first["successor_contract_guard"],
        "frozen_contract": first["frozen_contract"],
        "independent_contract_valid": first["independent_contract_valid"],
        "frozen_B1_left_null_Bianchi": first["frozen_B1_left_null_Bianchi"],
        "production_TCA0_bridge": first["production_TCA0_bridge"],
        "support_depth_spec": first["support_depth_spec"],
        "M1": first["M1"],
        "nominal_support_checkpoint": checkpoint,
        "variants": variants,
        "zero_pair_pass": zero_pair_pass,
        "pair_pass": pair_pass,
        "thresholds": first["thresholds"],
        "source_hashes": first["source_hashes"],
        "runtime_seconds": parent_runtime_seconds,
        "score_effect": "NONE",
        "K4_score_effect": "NONE_60_OF_100_UNCHANGED",
        "release_trigger": "NONE",
        "zenodo_trigger": "NONE",
        "prediction_table_effect": "NONE",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }
    if not scientific.c2.finite_owner._all_finite(payload):
        raise FloatingPointError("non-finite KMPC-132 aggregate payload")
    return payload


def aggregate_smoke_shards(
    shards: Mapping[str, Mapping[str, object]],
) -> dict[str, object]:
    expected = {shard_key(variant, level) for variant, level in SHARDS}
    checks: dict[str, bool] = {"exact_six_shard_register": set(shards) == expected}
    for variant, level in SHARDS:
        key = shard_key(variant, level)
        payload = shards.get(key)
        checks[key] = bool(
            isinstance(payload, dict)
            and payload.get("run_id") == RUN_ID
            and payload.get("worker_role") == "C3_SUPPORT_04_06_SHARD_SMOKE"
            and payload.get("identity")
            == {
                "mode": TARGET[0],
                "k_Mpc_inverse": TARGET[1],
                "variant": variant,
                "support_level": level,
            }
            and payload.get("pass") is True
            and payload.get("physics_executed") is False
        )
    return {
        "run_id": RUN_ID,
        "identity": {"mode": TARGET[0], "k_Mpc_inverse": TARGET[1]},
        "checks": checks,
        "pass": all(checks.values()),
        "physics_executed": False,
    }
