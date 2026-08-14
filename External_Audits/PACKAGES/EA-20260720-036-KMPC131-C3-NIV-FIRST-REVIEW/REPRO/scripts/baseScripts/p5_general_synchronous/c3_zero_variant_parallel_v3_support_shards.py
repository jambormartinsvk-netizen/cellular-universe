"""KMPC-131 four support-shard C3 process architecture.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Scientific formulas and gates are delegated to frozen KMPC-128 code.
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import time
from typing import Mapping

from . import c3_zero_variant_parallel_v2_smoke_identity as v2


scientific = v2.v1.v1
RUN_ID = "KMPC-131"
MODES = scientific.MODES
K_VALUES = scientific.K_VALUES
VARIANTS = scientific.VARIANTS
SUPPORT_LEVELS = ("accepted", "audit")
SHARDS = tuple(
    (variant, level) for variant in VARIANTS for level in SUPPORT_LEVELS
)


def sha256_file(path: Path) -> str:
    return scientific.sha256_file(path)


def shard_key(variant: str, level: str) -> str:
    if (variant, level) not in SHARDS:
        raise ValueError(f"unsupported KMPC-131 shard {variant}/{level}")
    return f"{variant}/{level}"


def output_name(mode: str, k_mpc: float) -> str:
    if (mode, k_mpc) not in scientific.SUPPORTS:
        raise ValueError("KMPC-131 pair identity outside frozen matrix")
    return f"RUN_KMPC_131_P5_3G7_C3_{mode}_K{scientific.k_token(k_mpc)}_ZERO_VARIANT_PAIR.json"


def failure_name(mode: str, k_mpc: float) -> str:
    return output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def _source_hashes() -> dict[str, str]:
    return {
        "c3_zero_variant_pair.py": sha256_file(Path(scientific.__file__).resolve()),
        "c3_zero_variant_parallel.py": sha256_file(Path(v2.v1.__file__).resolve()),
        "c3_zero_variant_parallel_v2_smoke_identity.py": sha256_file(Path(v2.__file__).resolve()),
        "c3_zero_variant_parallel_v3_support_shards.py": sha256_file(Path(__file__).resolve()),
    }


def run_support_worker(
    mode: str,
    k_mpc: float,
    variant: str,
    level: str,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    if (variant, level) not in SHARDS or (mode, k_mpc) not in scientific.SUPPORTS:
        raise ValueError("KMPC-131 support-worker identity outside frozen matrix")
    started, deadline = scientific._make_deadline(max_runtime_seconds)
    nominal = scientific._load_nominal_reference(result_dir, mode, k_mpc)
    deadline()
    guard = scientific.contract_guard()
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
    support = scientific.SUPPORTS[(mode, k_mpc)]
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
        "worker_role": "C3_ZERO_VARIANT_SUPPORT_SHARD",
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
        "nominal_reference": {
            key: value for key, value in nominal.items() if key != "states"
        },
        "contract_guard": guard,
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
        raise FloatingPointError("non-finite KMPC-131 support-worker payload")
    return payload


def run_worker_smoke(
    mode: str,
    k_mpc: float,
    variant: str,
    level: str,
    result_dir: Path,
) -> dict[str, object]:
    if (variant, level) not in SHARDS:
        raise ValueError("invalid smoke shard")
    base_smoke = scientific.run_smoke(mode, k_mpc, result_dir)
    checks = {
        "KMPC128_schema_smoke": bool(base_smoke["pass"]),
        "shard_identity": (variant, level) in SHARDS,
        "worker_does_not_write": True,
        "no_physics_executed": base_smoke["physics_executed"] is False,
    }
    return {
        "run_id": RUN_ID,
        "worker_role": "C3_ZERO_VARIANT_SUPPORT_SHARD_SMOKE",
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
    mode: str,
    k_mpc: float,
    variant: str,
    level: str,
) -> None:
    if payload.get("run_id") != RUN_ID or payload.get("worker_role") != "C3_ZERO_VARIANT_SUPPORT_SHARD":
        raise RuntimeError(f"worker contract mismatch: {variant}/{level}")
    if payload.get("identity") != {
        "mode": mode,
        "k_Mpc_inverse": k_mpc,
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


def _restore_background(value: object) -> dict[str, dict[int, float]]:
    if not isinstance(value, dict):
        raise TypeError("background is not an object")
    restored: dict[str, dict[int, float]] = {}
    for name, series in value.items():
        if not isinstance(series, dict):
            raise TypeError(f"background series is invalid: {name}")
        restored[name] = {int(power): float(coefficient) for power, coefficient in series.items()}
    return restored


def _restore_solve(value: object, label: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise TypeError(f"{label} solve is not an object")
    solve = deepcopy(value)
    solve["fuel"]["state"] = scientific._restore_state(
        solve["fuel"]["state"], f"{label}.F0"
    )
    solve["m3"]["fractional_state"] = scientific._restore_state(
        solve["m3"]["fractional_state"], f"{label}.M3"
    )
    solve["m3"]["background"] = _restore_background(
        solve["m3"]["background"]
    )
    return solve


def _variant_from_shards(
    mode: str,
    k_mpc: float,
    variant: str,
    accepted_worker: Mapping[str, object],
    audit_worker: Mapping[str, object],
    nominal: Mapping[str, object],
) -> dict[str, object]:
    support = scientific.SUPPORTS[(mode, k_mpc)]
    accepted = _restore_solve(accepted_worker["solve"], f"{variant}.accepted")
    audit = _restore_solve(audit_worker["solve"], f"{variant}.audit")
    standard = scientific._restore_state(
        accepted_worker["standard_state"], f"{variant}.standard"
    )
    common = {
        "F0": scientific.c2._common_bridge(
            accepted["fuel"]["state"], audit["fuel"]["state"], support.accepted
        ),
        "M3": scientific.c2._common_bridge(
            accepted["m3"]["fractional_state"], audit["m3"]["fractional_state"], support.accepted
        ),
    }
    tails = {
        "F0": scientific.c2._tail(
            audit["fuel"]["state"], tuple(sorted(audit["fuel"]["state"])), support.accepted, support.audit
        ),
        "M3": scientific.c2._tail(
            audit["m3"]["fractional_state"], tuple(scientific.c2.ra_contract.AUTHORITATIVE_STATE), support.accepted, support.audit
        ),
    }
    s_c0 = scientific.c2.support_tools.c1._s_c0_actual_coefficient_guard({
        "m3_primary": {"fractional_state": accepted["m3"]["fractional_state"]},
        "m3_extended": {"fractional_state": audit["m3"]["fractional_state"]},
    })
    inputs = scientific.physics._variant_inputs(variant)
    background = scientific.c2._background_guard(inputs, k_mpc, support.audit[1])
    null_limit = scientific._null_limit(
        variant, inputs, k_mpc, support.audit[1], standard, accepted, audit
    )
    bridges: dict[str, object] = {"applicable": False, "pass": True}
    if variant == "af0":
        nominal_states = nominal.get("states")
        if not isinstance(nominal_states, dict):
            raise TypeError("nominal state bundle missing")
        bridges = {
            "applicable": True,
            **scientific._nominal_af0_bridges(
                nominal_states, accepted, audit, support
            ),
        }
    common_pass = all(row["pass"] for row in common.values())
    tail_pass = all(row["pass"] for row in tails.values())
    shared = accepted_worker["shared_checks"]
    if not isinstance(shared, dict):
        raise TypeError("shared check schema mismatch")
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
    core_pass = all(core_checks.values())
    candidate = scientific._variant_candidate(
        core_pass,
        common_pass,
        tail_pass,
        bool(background["pass"]),
        bool(null_limit["pass"]),
        bool(bridges["pass"]),
        variant,
    )
    return {
        "logical_atom_id": f"{mode}/k={k_mpc}/{variant}",
        "identity": {"mode": mode, "k_Mpc_inverse": k_mpc, "variant": variant},
        "candidate_interpretation_not_verdict": candidate,
        "inputs": {"lam": inputs.lam, "af": inputs.af},
        "core_checks": core_checks,
        "core_pass": core_pass,
        "combined_R_fs_guard": accepted_worker["combined_R_fs_guard"],
        "accepted_solve": accepted,
        "audit_solve": audit,
        "common": common,
        "common_pass": common_pass,
        "tails": tails,
        "tail_pass": tail_pass,
        "S_C0_actual_guard": s_c0,
        "background_guard": background,
        "null_limit": null_limit,
        "nominal_vs_af0_coefficient_bridges": bridges,
        "logical_atom_pass": candidate.startswith("PASS_C3_"),
        "support_worker_runtime_seconds": {
            "accepted": accepted_worker["runtime_seconds"],
            "audit": audit_worker["runtime_seconds"],
        },
    }


def aggregate_shards(
    mode: str,
    k_mpc: float,
    shards: Mapping[str, Mapping[str, object]],
    result_dir: Path,
    parent_runtime_seconds: float,
) -> dict[str, object]:
    expected_keys = {shard_key(variant, level) for variant, level in SHARDS}
    if set(shards) != expected_keys:
        raise RuntimeError("KMPC-131 exact four-shard register mismatch")
    for variant, level in SHARDS:
        _require_shard(shards[shard_key(variant, level)], mode, k_mpc, variant, level)
    rows = list(shards.values())
    first = rows[0]
    parity_checks = {
        "nominal_reference": all(row["nominal_reference"] == first["nominal_reference"] for row in rows),
        "contract_guard": all(row["contract_guard"] == first["contract_guard"] for row in rows),
        "support_depth_spec": all(row["support_depth_spec"] == first["support_depth_spec"] for row in rows),
        "M1_recomputed_exact_parity": all(row["M1"] == first["M1"] for row in rows),
        "standard_state_exact_parity": all(row["standard_state"] == first["standard_state"] for row in rows),
        "thresholds": all(row["thresholds"] == first["thresholds"] for row in rows),
        "source_hashes": all(row["source_hashes"] == first["source_hashes"] for row in rows),
    }
    if not all(parity_checks.values()):
        raise RuntimeError(
            "KMPC-131 shared parity failed: "
            + ",".join(name for name, passed in parity_checks.items() if not passed)
        )
    nominal = scientific._load_nominal_reference(result_dir, mode, k_mpc)
    variants = {
        variant: _variant_from_shards(
            mode,
            k_mpc,
            variant,
            shards[shard_key(variant, "accepted")],
            shards[shard_key(variant, "audit")],
            nominal,
        )
        for variant in VARIANTS
    }
    pair_pass = all(row["logical_atom_pass"] for row in variants.values())
    candidate = (
        "PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY"
        if pair_pass else "REVIEW_C3_ZERO_VARIANT_PAIR_UNCLOSED"
    )
    payload = {
        "test": "A2-K4 P5.3g7 C3 four-support-shard gamma0/af0 pair receipt",
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
            "physical_receipt": "four_support_shards_gamma0_af0_pair",
        },
        "logical_atom_accounting": {
            "existing_nominal": 1,
            "new_zero_variants": 2,
            "technical_support_shards": 4,
            "total_logical_atoms": 3,
        },
        "scope": {
            "included": "one mode-k C3 pair from four isolated bounded support workers",
            "excluded": "other mode-k pairs, S-M, finite opacity, full hierarchy, P5.4, G8/G9 and data",
        },
        "process_architecture": {
            "parallel_support_workers": sorted(expected_keys),
            "worker_internal_limit_seconds": 4.8,
            "worker_intermediate_files": 0,
            "parent_solver_calls": 0,
        },
        "worker_parity_checks": parity_checks,
        "nominal_reference": {
            key: value for key, value in nominal.items() if key != "states"
        },
        "contract_guard": first["contract_guard"],
        "frozen_contract": first["frozen_contract"],
        "independent_contract_valid": first["independent_contract_valid"],
        "frozen_B1_left_null_Bianchi": first["frozen_B1_left_null_Bianchi"],
        "production_TCA0_bridge": first["production_TCA0_bridge"],
        "support_depth_spec": first["support_depth_spec"],
        "M1": first["M1"],
        "variants": variants,
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
        raise FloatingPointError("non-finite KMPC-131 aggregate payload")
    return payload


def aggregate_smoke_shards(
    mode: str,
    k_mpc: float,
    shards: Mapping[str, Mapping[str, object]],
) -> dict[str, object]:
    expected = {shard_key(variant, level) for variant, level in SHARDS}
    checks: dict[str, bool] = {"exact_four_shard_register": set(shards) == expected}
    for variant, level in SHARDS:
        key = shard_key(variant, level)
        payload = shards.get(key)
        checks[key] = bool(
            isinstance(payload, dict)
            and payload.get("run_id") == RUN_ID
            and payload.get("worker_role") == "C3_ZERO_VARIANT_SUPPORT_SHARD_SMOKE"
            and payload.get("identity") == {
                "mode": mode,
                "k_Mpc_inverse": k_mpc,
                "variant": variant,
                "support_level": level,
            }
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
