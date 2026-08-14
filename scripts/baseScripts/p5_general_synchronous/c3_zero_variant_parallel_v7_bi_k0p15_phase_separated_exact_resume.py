"""KMPC-135 BI/.15 C3 phase-separated HP-M1 exact-resume adapter.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
The adapter uses an explicit binary64 HP-M1 projection for ordinary
coefficient solves and the original decimal80 state only at the exact audit
boundary. Exact evidence may supersede only the audit M3 driver and holdout.
"""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import time
from typing import Mapping

import mpmath as mp

from . import (
    c2_bi_k0p15_high_precision_m1_reassembly_v19_exact_resume_json_parity_successor
    as hp,
)
from . import c3_zero_variant_parallel_v3_support_shards as v3


scientific = v3.scientific
v18 = hp.v18
v17 = v18.v17
v16 = v17.v16
v11 = v17.v11
driver = v17.driver
base = v17.base
RUN_ID = "KMPC-135"
TARGET = ("BI", 0.15)
SHARDS = v3.SHARDS
EXPECTED_V3_SHA256 = (
    "7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23"
)
EXPECTED_HP_SHA256 = (
    "067CFDBBA95712B04FCD8D571537D751A441B41F4B479FCFB54D7F7AAB281DA5"
)


def sha256_file(path: Path) -> str:
    return scientific.sha256_file(path)


def shard_key(variant: str, level: str) -> str:
    return v3.shard_key(variant, level)


def output_name(mode: str, k_mpc: float) -> str:
    if (mode, k_mpc) != TARGET:
        raise ValueError("KMPC-135 is frozen to BI/k=0.15")
    return "RUN_KMPC_135_P5_3G7_C3_BI_K0p15_ZERO_VARIANT_PAIR_PHASE_SEPARATED_HP_M1_EXACT_RESUME.json"


def failure_name(mode: str, k_mpc: float) -> str:
    return output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def successor_contract_guard() -> dict[str, object]:
    support = scientific.SUPPORTS[TARGET]
    checks = {
        "target_identity_exact": TARGET == ("BI", 0.15),
        "support_05_07_exact": support.accepted == (0, 5)
        and support.audit == (0, 7)
        and support.m1_depth == 7,
        "four_shards_exact": SHARDS
        == (("gamma0", "accepted"), ("gamma0", "audit"),
            ("af0", "accepted"), ("af0", "audit")),
        "precision_80dps_exact": base.PRECISION_DPS == 80,
        "driver_rank_104_exact": driver.EXPECTED_ROWS == 104
        and driver.EXPECTED_COLUMNS == 104,
        "checkpoint_hash_frozen": v16.CHECKPOINT_SHA256
        == "683D867D19324B7B45F3724545FFB1D975DFBED883936298D790C12836E9D995",
        "serialized_fingerprint_frozen": v16.SERIALIZED_STATE_SHA256
        == "402B42E11C3582B4E3E46D047EA917A4C256E552F65C9DB070589150675EBF40",
        "receipt_hash_frozen": v17.RECEIPT_SHA256
        == "21EF9A9BF8D6E437CC848BD76EC026C5621534F35C0D88F99D2BFAFAD28118F9",
        "v3_source_hash_frozen": sha256_file(Path(v3.__file__).resolve())
        == EXPECTED_V3_SHA256,
        "hp_json_parity_source_hash_frozen": sha256_file(Path(hp.__file__).resolve())
        == EXPECTED_HP_SHA256,
    }
    return {"checks": checks, "pass": all(checks.values())}


def _floatify(value: object) -> object:
    if isinstance(value, mp.mpf):
        return float(value)
    if isinstance(value, dict):
        return {key: _floatify(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_floatify(item) for item in value]
    if hasattr(value, "item") and callable(getattr(value, "item")):
        return _floatify(value.item())
    return value


def _contains_mpf(value: object) -> bool:
    if isinstance(value, mp.mpf):
        return True
    if isinstance(value, dict):
        return any(_contains_mpf(item) for item in value.values())
    if isinstance(value, (list, tuple)):
        return any(_contains_mpf(item) for item in value)
    return False


def _load_checkpoint_bundle(
    result_dir: Path,
) -> tuple[dict[str, object], dict[str, object], dict[str, dict[int, object]]]:
    checkpoint_path = result_dir / v16.CHECKPOINT_NAME
    receipt_path = result_dir / v17.RECEIPT_NAME
    if sha256_file(checkpoint_path) != v16.CHECKPOINT_SHA256:
        raise RuntimeError("KMPC-108 checkpoint missing or hash-mismatched")
    if sha256_file(receipt_path) != v17.RECEIPT_SHA256:
        raise RuntimeError("KMPC-109 receipt missing or hash-mismatched")
    raw = json.loads(checkpoint_path.read_text(encoding="utf-8"))
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    checkpoint = raw["resume_checkpoint"]
    if v16._checkpoint_fingerprint(checkpoint) != v16.SERIALIZED_STATE_SHA256:
        raise RuntimeError("KMPC-108 serialized-state fingerprint mismatch")
    hp_m1, _checkpoint_fuel = v18._ordered_restore_checkpoint_states(checkpoint)
    allowed = bool(
        receipt["passed_execution_contract"]
        and receipt["checkpoint_receipt"]["exact_driver_resume_allowed"]
        and receipt["candidate_interpretation_not_verdict"]
        == "REVIEW_C2_BI_K0p15_HP_M1_CHECKPOINT_RECEIPT_EXACT_RESUME_ALLOWED"
    )
    if not allowed:
        raise RuntimeError("KMPC-109 receipt does not allow exact resume")
    return raw, receipt, hp_m1


def _source_hashes() -> dict[str, str]:
    hashes = dict(hp.source_hashes())
    hashes.update({
        "c3_zero_variant_pair.py": sha256_file(Path(scientific.__file__).resolve()),
        "c3_zero_variant_parallel_v3_support_shards.py": sha256_file(
            Path(v3.__file__).resolve()
        ),
        "c3_zero_variant_parallel_v7_bi_k0p15_phase_separated_exact_resume.py": sha256_file(
            Path(__file__).resolve()
        ),
    })
    return hashes


def _exact_resume_solve(
    mode: str,
    k_mpc: float,
    variant: str,
    level: str,
    standard_m1: dict[str, dict[int, object]],
    hp_m1: dict[str, dict[int, object]],
    deadline: object,
) -> tuple[dict[str, object], dict[str, object]]:
    support_spec = scientific.SUPPORTS[TARGET]
    support = support_spec.accepted if level == "accepted" else support_spec.audit
    inputs = scientific.physics._variant_inputs(variant)
    exact_evidence: dict[str, object] = {
        "applicable": False,
        "superseded_checks": [],
        "representation_contract": {
            "coefficient_solve_uses_binary64_projection": True,
            "exact_boundary_uses_original_decimal80_HP_M1": False,
        },
        "checks": {
            "accepted_rank_not_exact_resumed": level == "accepted",
            "coefficient_solve_binary64_projection": not _contains_mpf(standard_m1),
        },
        "pass": level == "accepted",
    }
    if level == "accepted":
        solve = scientific.c2._solve_support(
            mode, k_mpc, support, inputs, standard_m1, deadline
        )
        exact_evidence["pass"] = all(exact_evidence["checks"].values())
        return _floatify(solve), exact_evidence

    with v11._float_driver_capture():
        solve = scientific.c2._solve_support(
            mode, k_mpc, support, inputs, standard_m1, deadline
        )
        variant_fuel = solve["fuel"]["state"]
        combined, merge = v11._merge_m1_and_fuel(hp_m1, variant_fuel)
        with mp.workdps(base.PRECISION_DPS):
            boundary = driver._exact_driver_boundary(
                k_mpc, inputs, combined, support
            )
    capture = dict(v11._CAPTURE_DIAGNOSTIC or {})
    if not v11._owners_restored():
        raise RuntimeError("KMPC-135 float capture owners were not restored")
    safe_solve = _floatify(solve)
    safe_boundary = _floatify(boundary)
    original_false = sorted(
        name for name, passed in safe_solve["checks"].items() if passed is False
    )
    driver_pass = bool(safe_boundary["driver"]["pass_driver"])
    holdout_pass = bool(
        safe_boundary["holdout"]["pass_holdout"]
        and safe_boundary["holdout"]["rows_added_to_driver_solve"] == 0
    )
    exact_checks = {
        "original_false_set_exact": original_false
        == ["M3_driver", "M3_independent_00_0i_holdout"],
        "capture_once": capture.get("audit_driver_capture_count") == 1,
        "capture_shape_104": capture.get("shape") == [104, 104],
        "one_exact_driver_solve": safe_boundary["exact_driver_solve_count"] == 1,
        "exact_driver_pass": driver_pass,
        "exact_nonfit_holdout_pass": holdout_pass,
        "holdout_rows_not_fit": safe_boundary["holdout"][
            "rows_added_to_driver_solve"
        ] == 0,
        "precision_80dps": safe_boundary["precision_dps"] == 80,
        "owners_restored": v11._owners_restored(),
        "coefficient_solve_binary64_projection": not _contains_mpf(standard_m1),
        "exact_boundary_original_decimal80_HP_M1": _contains_mpf(hp_m1),
    }
    exact_pass = all(exact_checks.values())
    safe_solve["exact_resume_supersession"] = {
        "applicable": True,
        "original_solve_pass": safe_solve["pass"],
        "original_false_checks": original_false,
        "superseded_checks": ["M3_driver", "M3_independent_00_0i_holdout"],
        "variant_fuel_recomputed": True,
        "checkpoint_nominal_fuel_used_as_variant_result": False,
        "representation_contract": {
            "coefficient_solve_uses_binary64_projection": True,
            "exact_boundary_uses_original_decimal80_HP_M1": True,
        },
        "combined_register_handoff": merge,
        "float_driver_capture": capture,
        "high_precision_boundary": safe_boundary,
        "checks": exact_checks,
        "pass": exact_pass,
    }
    safe_solve["checks"]["M3_driver"] = driver_pass
    safe_solve["checks"]["M3_independent_00_0i_holdout"] = holdout_pass
    safe_solve["pass"] = all(safe_solve["checks"].values()) and exact_pass
    return safe_solve, safe_solve["exact_resume_supersession"]


def run_support_worker(
    mode: str,
    k_mpc: float,
    variant: str,
    level: str,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    if (mode, k_mpc) != TARGET or (variant, level) not in SHARDS:
        raise ValueError("KMPC-135 worker identity outside preregistration")
    started, deadline = scientific._make_deadline(max_runtime_seconds)
    nominal = scientific._load_nominal_reference(result_dir, mode, k_mpc)
    checkpoint_raw, receipt, hp_m1 = _load_checkpoint_bundle(result_dir)
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
    standard_float = _floatify(hp_m1)
    if _contains_mpf(standard_float):
        raise RuntimeError("KMPC-135 binary64 projection still contains mpf")
    inputs = scientific.physics._variant_inputs(variant)
    rfs = scientific.c2._rfs_guard(mode, standard_float, inputs)
    solve, exact_evidence = _exact_resume_solve(
        mode, k_mpc, variant, level, standard_float, hp_m1, deadline
    )
    deadline()
    shared_checks = {
        "C3_HP_M1_exact_resume_contract": bool(guard["pass"]),
        "nominal_reference": True,
        "checkpoint_fingerprint": True,
        "receipt_exact_resume_allowed": True,
        "frozen_contract": bool(frozen_contract["valid"]),
        "independent_contract": bool(independent_contract.valid),
        "B1_left_null_Bianchi": frozen_b1["execution_verdict"]
        == "PASS_R_A_B1_CONTRACT_GUARD_ONLY",
        "production_TCA0_bridge": bool(tca0["pass"]),
        "coefficient_solve_uses_binary64_projection": not _contains_mpf(
            standard_float
        ),
        "checkpoint_HP_M1_preserved_for_exact_boundary": _contains_mpf(hp_m1),
    }
    support = scientific.SUPPORTS[TARGET]
    payload = {
        "run_id": RUN_ID,
        "worker_role": "C3_BI_K0P15_PHASE_SEPARATED_HP_M1_EXACT_RESUME_SHARD",
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
        "checkpoint_inputs": {
            "checkpoint_file": v16.CHECKPOINT_NAME,
            "checkpoint_sha256": v16.CHECKPOINT_SHA256,
            "receipt_file": v17.RECEIPT_NAME,
            "receipt_sha256": v17.RECEIPT_SHA256,
            "serialized_state_sha256": v16.SERIALIZED_STATE_SHA256,
            "checkpoint_run_id": checkpoint_raw["run_id"],
            "receipt_run_id": receipt["run_id"],
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
        "selected_support": list(
            support.accepted if level == "accepted" else support.audit
        ),
        "M1": {
            "pass": bool(checkpoint_raw["M1"]["pass"]),
            "source": "KMPC-108_DECIMAL90_CHECKPOINT_NO_CPQR_RERUN",
            "state_count": len(hp_m1),
            "serialized_state_sha256": v16.SERIALIZED_STATE_SHA256,
        },
        "standard_state": standard_float,
        "combined_R_fs_guard": rfs,
        "solve": solve,
        "exact_resume_evidence": exact_evidence,
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
        raise FloatingPointError("non-finite KMPC-135 worker payload")
    return payload


def run_worker_smoke(
    mode: str,
    k_mpc: float,
    variant: str,
    level: str,
    result_dir: Path,
) -> dict[str, object]:
    if (mode, k_mpc) != TARGET or (variant, level) not in SHARDS:
        raise ValueError("invalid KMPC-135 smoke shard")
    nominal = scientific._load_nominal_reference(result_dir, mode, k_mpc)
    raw, receipt, hp_m1 = _load_checkpoint_bundle(result_dir)
    checks = {
        "successor_contract": bool(successor_contract_guard()["pass"]),
        "nominal_reference_loaded": nominal["run_id"] == "KMPC-112",
        "checkpoint_identity": raw["run_id"] == "KMPC-108",
        "receipt_identity": receipt["run_id"] == "KMPC-109",
        "ordered_HP_M1_restored": tuple(hp_m1)
        == tuple(scientific.physics.STATE_TO_LEGACY),
        "binary64_projection_contains_no_mpf": not _contains_mpf(_floatify(hp_m1)),
        "original_checkpoint_state_retains_mpf": _contains_mpf(hp_m1),
        "shard_identity": (variant, level) in SHARDS,
        "worker_does_not_write": True,
        "no_physics_executed": True,
    }
    return {
        "run_id": RUN_ID,
        "worker_role": "C3_BI_K0P15_PHASE_SEPARATED_HP_M1_EXACT_RESUME_SHARD_SMOKE",
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
    payload: Mapping[str, object], variant: str, level: str
) -> None:
    if payload.get("run_id") != RUN_ID:
        raise RuntimeError(f"KMPC-135 run identity mismatch: {variant}/{level}")
    if payload.get("worker_role") != "C3_BI_K0P15_PHASE_SEPARATED_HP_M1_EXACT_RESUME_SHARD":
        raise RuntimeError(f"KMPC-135 worker role mismatch: {variant}/{level}")
    if payload.get("identity") != {
        "mode": TARGET[0],
        "k_Mpc_inverse": TARGET[1],
        "variant": variant,
        "support_level": level,
    }:
        raise RuntimeError(f"KMPC-135 shard identity mismatch: {variant}/{level}")
    evidence = payload.get("exact_resume_evidence")
    if level == "audit" and (
        not isinstance(evidence, dict) or evidence.get("pass") is not True
    ):
        raise RuntimeError(f"KMPC-135 exact audit evidence failed: {variant}")


def aggregate_shards(
    shards: Mapping[str, Mapping[str, object]],
    result_dir: Path,
    parent_runtime_seconds: float,
) -> dict[str, object]:
    expected = {shard_key(variant, level) for variant, level in SHARDS}
    if set(shards) != expected:
        raise RuntimeError("KMPC-135 exact four-shard register mismatch")
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
    exact_audit: dict[str, object] = {}
    for variant in ("gamma0", "af0"):
        evidence = payload["variants"][variant]["audit_solve"][
            "exact_resume_supersession"
        ]
        coefficient_checks = {
            "core_pass": payload["variants"][variant]["core_pass"] is True,
            "common_pass": payload["variants"][variant]["common_pass"] is True,
            "tail_pass": payload["variants"][variant]["tail_pass"] is True,
            "background_pass": payload["variants"][variant]["background_guard"][
                "pass"
            ] is True,
            "null_pass": payload["variants"][variant]["null_limit"]["pass"] is True,
            "nominal_bridge_pass": payload["variants"][variant][
                "nominal_vs_af0_coefficient_bridges"
            ]["pass"] is True,
        }
        exact_audit[variant] = {
            "exact_resume": evidence,
            "coefficient_and_null_checks": coefficient_checks,
            "pass": bool(evidence["pass"] and all(coefficient_checks.values())),
        }
    exact_pass = all(row["pass"] for row in exact_audit.values())
    pair_pass = bool(payload["pair_pass"] and exact_pass)
    payload["run_id"] = RUN_ID
    payload["test"] = (
        "A2-K4 P5.3g7 C3 BI/.15 phase-separated HP-M1 exact-resume pair"
    )
    payload["identity"]["physical_receipt"] = (
        "four_support_shards_gamma0_af0_phase_separated_HP_M1_exact_resume_pair"
    )
    payload["process_architecture"]["HP_M1_exact_resume"] = {
        "checkpoint": v16.CHECKPOINT_NAME,
        "receipt": v17.RECEIPT_NAME,
        "precision_dps": 80,
        "coefficient_solve_representation": "binary64_projection",
        "exact_boundary_representation": "original_decimal80_HP_M1",
        "CPQR_repeated": False,
        "parent_solver_calls": 0,
    }
    payload["HP_M1_exact_resume_audit"] = exact_audit
    payload["HP_M1_exact_resume_pass"] = exact_pass
    payload["pair_pass"] = pair_pass
    payload["candidate_interpretation_not_verdict"] = (
        "PASS_C3_BI_K0P15_ZERO_PAIR_PHASE_SEPARATED_HP_M1_EXACT_RESUME_CANDIDATE_ONLY"
        if pair_pass
        else "REVIEW_C3_BI_K0P15_HP_M1_EXACT_BOUNDARY_UNCLOSED"
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
            == "C3_BI_K0P15_PHASE_SEPARATED_HP_M1_EXACT_RESUME_SHARD_SMOKE"
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
