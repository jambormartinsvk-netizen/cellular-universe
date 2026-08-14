"""KMPC-136 BI/.15 C3 two-wave HP-M1 exact-resume adapter.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Four binary64 coefficient workers finish before two audit-only decimal80
exact-boundary workers. Exact evidence may supersede only the audit M3 driver
and independent holdout.
"""

from __future__ import annotations

from copy import deepcopy
from contextlib import contextmanager
import hashlib
import json
from pathlib import Path
import time
from typing import Iterator, Mapping

import mpmath as mp
import numpy as np

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
RUN_ID = "KMPC-136"
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
        raise ValueError("KMPC-136 is frozen to BI/k=0.15")
    return "RUN_KMPC_136_P5_3G7_C3_BI_K0p15_ZERO_VARIANT_PAIR_TWO_WAVE_HP_M1_EXACT_RESUME.json"


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
        "c3_zero_variant_parallel_v8_bi_k0p15_two_wave_exact_resume.py": sha256_file(
            Path(__file__).resolve()
        ),
    })
    return hashes


def handoff_hash(payload: Mapping[str, object]) -> str:
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest().upper()


@contextmanager
def _audit_float_capture() -> Iterator[dict[str, object]]:
    original = scientific.physics._solve_equilibrated
    captured: dict[str, object] = {}

    def capture(matrix, constant, expected_rank, row_labels=None, deadline=None):
        if expected_rank == driver.EXPECTED_COLUMNS:
            if captured:
                raise RuntimeError("KMPC-136 more than one audit driver capture")
            captured.update({
                "matrix": matrix.copy(),
                "constant": constant.copy(),
                "count": 1,
            })
        return original(
            matrix,
            constant,
            expected_rank,
            row_labels=row_labels,
            deadline=deadline,
        )

    scientific.physics._solve_equilibrated = capture
    try:
        yield captured
        if captured.get("count") != 1:
            raise RuntimeError("KMPC-136 audit driver capture missing")
    finally:
        scientific.physics._solve_equilibrated = original


def _coefficient_solve(
    mode: str,
    k_mpc: float,
    variant: str,
    level: str,
    standard_m1: dict[str, dict[int, object]],
    deadline: object,
) -> tuple[dict[str, object], dict[str, object], dict[str, object] | None]:
    support_spec = scientific.SUPPORTS[TARGET]
    support = support_spec.accepted if level == "accepted" else support_spec.audit
    inputs = scientific.physics._variant_inputs(variant)
    representation_ok = not _contains_mpf(standard_m1)
    if level == "accepted":
        solve = scientific.c2._solve_support(
            mode, k_mpc, support, inputs, standard_m1, deadline
        )
        evidence = {
            "applicable": False,
            "status": "ACCEPTED_RANK_NOT_EXACT_RESUMED",
            "superseded_checks": [],
            "checks": {
                "accepted_rank_not_exact_resumed": True,
                "coefficient_solve_binary64_projection": representation_ok,
            },
        }
        evidence["pass"] = all(evidence["checks"].values())
        return _floatify(solve), evidence, None

    with _audit_float_capture() as captured:
        solve = scientific.c2._solve_support(
            mode, k_mpc, support, inputs, standard_m1, deadline
        )
    if scientific.physics._solve_equilibrated is not v11._PHYSICS_SOLVE:
        raise RuntimeError("KMPC-136 coefficient capture owner not restored")
    matrix = captured["matrix"]
    constant = captured["constant"]
    variant_fuel = _floatify(solve["fuel"]["state"])
    capture = {
        "audit_driver_capture_count": captured["count"],
        "shape": list(matrix.shape),
        "matrix_constant_sha256": driver.hp._matrix_fingerprint(matrix, constant),
    }
    handoff = {
        "run_id": RUN_ID,
        "identity": {
            "mode": mode,
            "k_Mpc_inverse": k_mpc,
            "variant": variant,
            "support_level": "audit",
        },
        "variant_fuel": variant_fuel,
        "variant_fuel_fingerprint": v11._state_fingerprint(
            variant_fuel, ("delta_f", "U_f")
        ),
        "float_driver_capture": capture,
        "float_driver_matrix": matrix.tolist(),
        "float_driver_constant": constant.tolist(),
    }
    evidence = {
        "applicable": True,
        "status": "EXACT_BOUNDARY_PENDING_SECOND_WAVE",
        "superseded_checks": [],
        "float_driver_capture": capture,
        "checks": {
            "coefficient_solve_binary64_projection": representation_ok,
            "capture_once": capture["audit_driver_capture_count"] == 1,
            "capture_shape_104": capture["shape"] == [104, 104],
        },
    }
    evidence["pass"] = all(evidence["checks"].values())
    return _floatify(solve), evidence, handoff


def run_support_worker(
    mode: str,
    k_mpc: float,
    variant: str,
    level: str,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    if (mode, k_mpc) != TARGET or (variant, level) not in SHARDS:
        raise ValueError("KMPC-136 worker identity outside preregistration")
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
        raise RuntimeError("KMPC-136 binary64 projection still contains mpf")
    inputs = scientific.physics._variant_inputs(variant)
    rfs = scientific.c2._rfs_guard(mode, standard_float, inputs)
    solve, exact_evidence, handoff = _coefficient_solve(
        mode, k_mpc, variant, level, standard_float, deadline
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
        "worker_role": "C3_BI_K0P15_TWO_WAVE_COEFFICIENT_SHARD",
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
        "exact_boundary_handoff": handoff,
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
    }
    if not scientific.c2.finite_owner._all_finite(payload):
        raise FloatingPointError("non-finite KMPC-136 coefficient worker payload")
    return payload


def run_exact_worker(
    mode: str,
    k_mpc: float,
    variant: str,
    max_runtime_seconds: float,
    result_dir: Path,
    handoff_path: Path,
    expected_handoff_hash: str,
    expected_handoff_file_hash: str,
) -> dict[str, object]:
    if (mode, k_mpc) != TARGET or variant not in ("gamma0", "af0"):
        raise ValueError("KMPC-136 exact worker identity outside preregistration")
    started, deadline = scientific._make_deadline(max_runtime_seconds)
    if not handoff_path.is_file():
        raise FileNotFoundError("KMPC-136 exact handoff file missing")
    observed_file_hash = sha256_file(handoff_path)
    if observed_file_hash != expected_handoff_file_hash:
        raise RuntimeError("KMPC-136 handoff file SHA-256 mismatch")
    handoff = json.loads(handoff_path.read_text(encoding="utf-8"))
    observed_handoff_hash = handoff_hash(handoff)
    if observed_handoff_hash != expected_handoff_hash:
        raise RuntimeError("KMPC-136 canonical handoff hash mismatch")
    expected_identity = {
        "mode": mode,
        "k_Mpc_inverse": k_mpc,
        "variant": variant,
        "support_level": "audit",
    }
    if handoff.get("run_id") != RUN_ID or handoff.get("identity") != expected_identity:
        raise RuntimeError("KMPC-136 exact handoff identity mismatch")
    deadline()
    _checkpoint_raw, _receipt, hp_m1 = _load_checkpoint_bundle(result_dir)
    if not _contains_mpf(hp_m1):
        raise RuntimeError("KMPC-136 exact worker lost decimal80 HP-M1")
    variant_fuel = {
        name: {int(power): value for power, value in coefficients.items()}
        for name, coefficients in handoff["variant_fuel"].items()
    }
    fuel_fingerprint = v11._state_fingerprint(
        variant_fuel, ("delta_f", "U_f")
    )
    if fuel_fingerprint != handoff["variant_fuel_fingerprint"]:
        raise RuntimeError("KMPC-136 variant fuel handoff fingerprint mismatch")
    combined, merge = v11._merge_m1_and_fuel(hp_m1, variant_fuel)
    matrix = np.asarray(handoff["float_driver_matrix"], dtype=float)
    constant = np.asarray(handoff["float_driver_constant"], dtype=float)
    capture = handoff["float_driver_capture"]
    if list(matrix.shape) != [104, 104] or list(constant.shape) != [104]:
        raise RuntimeError("KMPC-136 handoff driver shape mismatch")
    if driver.hp._matrix_fingerprint(matrix, constant) != capture[
        "matrix_constant_sha256"
    ]:
        raise RuntimeError("KMPC-136 handoff driver fingerprint mismatch")
    before = (driver._FLOAT_MATRIX, driver._FLOAT_CONSTANT)
    try:
        driver._FLOAT_MATRIX = matrix
        driver._FLOAT_CONSTANT = constant
        with mp.workdps(base.PRECISION_DPS):
            boundary = driver._exact_driver_boundary(
                k_mpc,
                scientific.physics._variant_inputs(variant),
                combined,
                scientific.SUPPORTS[TARGET].audit,
            )
    finally:
        driver._FLOAT_MATRIX, driver._FLOAT_CONSTANT = before
    deadline()
    safe_boundary = _floatify(boundary)
    assembly_hash = safe_boundary["driver"][
        "assembly_difference_from_float64"
    ]["float64_matrix_constant_sha256"]
    technical_checks = {
        "handoff_file_hash_exact": observed_file_hash
        == expected_handoff_file_hash,
        "handoff_hash_exact": observed_handoff_hash == expected_handoff_hash,
        "handoff_identity_exact": handoff["identity"] == expected_identity,
        "capture_once": capture["audit_driver_capture_count"] == 1,
        "capture_shape_104": capture["shape"] == [104, 104],
        "float_matrix_fingerprint_preserved": assembly_hash
        == capture["matrix_constant_sha256"],
        "variant_fuel_fingerprint_preserved": fuel_fingerprint
        == handoff["variant_fuel_fingerprint"],
        "exact_boundary_original_decimal80_HP_M1": _contains_mpf(hp_m1),
        "one_exact_driver_solve": safe_boundary["exact_driver_solve_count"] == 1,
        "holdout_rows_not_fit": safe_boundary["holdout"][
            "rows_added_to_driver_solve"
        ] == 0,
        "precision_80dps": safe_boundary["precision_dps"] == 80,
        "driver_globals_restored": (
            driver._FLOAT_MATRIX is before[0]
            and driver._FLOAT_CONSTANT is before[1]
        ),
    }
    payload = {
        "run_id": RUN_ID,
        "worker_role": "C3_BI_K0P15_TWO_WAVE_EXACT_BOUNDARY_SHARD",
        "identity": expected_identity,
        "authorship": {
            "theory_author": "Martin Jambor",
            "script_creator": "Codex (OpenAI)",
        },
        "handoff_sha256": expected_handoff_hash,
        "handoff_file_sha256": expected_handoff_file_hash,
        "float_driver_capture": capture,
        "combined_register_handoff": merge,
        "high_precision_boundary": safe_boundary,
        "technical_checks": technical_checks,
        "technical_pass": all(technical_checks.values()),
        "exact_boundary_pass": bool(
            safe_boundary["driver"]["pass_driver"]
            and safe_boundary["holdout"]["pass_holdout"]
        ),
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "physics_verdict": "NONE_EXACT_BOUNDARY_SHARD_EVIDENCE_ONLY",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }
    if not scientific.c2.finite_owner._all_finite(payload):
        raise FloatingPointError("non-finite KMPC-136 exact worker payload")
    return payload


def run_worker_smoke(
    mode: str,
    k_mpc: float,
    variant: str,
    level: str,
    result_dir: Path,
) -> dict[str, object]:
    if (mode, k_mpc) != TARGET or (variant, level) not in SHARDS:
        raise ValueError("invalid KMPC-136 smoke shard")
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
        "canonical_handoff_hash_stable": handoff_hash({"b": 2, "a": 1})
        == handoff_hash({"a": 1, "b": 2}),
        "two_wave_roles_distinct": (
            "C3_BI_K0P15_TWO_WAVE_COEFFICIENT_SHARD"
            != "C3_BI_K0P15_TWO_WAVE_EXACT_BOUNDARY_SHARD"
        ),
        "shard_identity": (variant, level) in SHARDS,
        "worker_does_not_write": True,
        "no_physics_executed": True,
    }
    return {
        "run_id": RUN_ID,
        "worker_role": "C3_BI_K0P15_TWO_WAVE_COEFFICIENT_SHARD_SMOKE",
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


def run_exact_worker_smoke(
    mode: str,
    k_mpc: float,
    variant: str,
    result_dir: Path,
) -> dict[str, object]:
    if (mode, k_mpc) != TARGET or variant not in ("gamma0", "af0"):
        raise ValueError("invalid KMPC-136 exact smoke shard")
    raw, receipt, hp_m1 = _load_checkpoint_bundle(result_dir)
    fixture = {
        "run_id": RUN_ID,
        "identity": {
            "mode": mode,
            "k_Mpc_inverse": k_mpc,
            "variant": variant,
            "support_level": "audit",
        },
        "variant_fuel": {"delta_f": {0: 1.0}, "U_f": {0: 2.0}},
    }
    checks = {
        "successor_contract": bool(successor_contract_guard()["pass"]),
        "checkpoint_identity": raw["run_id"] == "KMPC-108",
        "receipt_identity": receipt["run_id"] == "KMPC-109",
        "original_checkpoint_state_retains_mpf": _contains_mpf(hp_m1),
        "canonical_handoff_hash_stable": handoff_hash(fixture)
        == handoff_hash(json.loads(json.dumps(fixture, sort_keys=True))),
        "exact_role_has_audit_support_only": fixture["identity"]["support_level"]
        == "audit",
        "worker_does_not_write": True,
        "no_physics_executed": True,
    }
    return {
        "run_id": RUN_ID,
        "worker_role": "C3_BI_K0P15_TWO_WAVE_EXACT_BOUNDARY_SHARD_SMOKE",
        "identity": fixture["identity"],
        "checks": checks,
        "pass": all(checks.values()),
        "physics_executed": False,
    }


def _require_shard(
    payload: Mapping[str, object], variant: str, level: str
) -> None:
    if payload.get("run_id") != RUN_ID:
        raise RuntimeError(f"KMPC-136 run identity mismatch: {variant}/{level}")
    if payload.get("worker_role") != "C3_BI_K0P15_TWO_WAVE_COEFFICIENT_SHARD":
        raise RuntimeError(f"KMPC-136 coefficient role mismatch: {variant}/{level}")
    if payload.get("identity") != {
        "mode": TARGET[0],
        "k_Mpc_inverse": TARGET[1],
        "variant": variant,
        "support_level": level,
    }:
        raise RuntimeError(f"KMPC-136 shard identity mismatch: {variant}/{level}")
    evidence = payload.get("exact_resume_evidence")
    if not isinstance(evidence, dict) or evidence.get("pass") is not True:
        raise RuntimeError(f"KMPC-136 coefficient evidence failed: {variant}/{level}")
    handoff = payload.get("exact_boundary_handoff")
    if (level == "audit") != isinstance(handoff, dict):
        raise RuntimeError(f"KMPC-136 handoff applicability mismatch: {variant}/{level}")


def _require_exact_shard(payload: Mapping[str, object], variant: str) -> None:
    if payload.get("run_id") != RUN_ID:
        raise RuntimeError(f"KMPC-136 exact run identity mismatch: {variant}")
    if payload.get("worker_role") != "C3_BI_K0P15_TWO_WAVE_EXACT_BOUNDARY_SHARD":
        raise RuntimeError(f"KMPC-136 exact worker role mismatch: {variant}")
    if payload.get("identity") != {
        "mode": TARGET[0],
        "k_Mpc_inverse": TARGET[1],
        "variant": variant,
        "support_level": "audit",
    }:
        raise RuntimeError(f"KMPC-136 exact shard identity mismatch: {variant}")
    if payload.get("technical_pass") is not True:
        raise RuntimeError(f"KMPC-136 exact technical checks failed: {variant}")


def aggregate_shards(
    shards: Mapping[str, Mapping[str, object]],
    exact_shards: Mapping[str, Mapping[str, object]],
    result_dir: Path,
    parent_runtime_seconds: float,
    temporary_handoffs_removed: bool,
) -> dict[str, object]:
    expected = {shard_key(variant, level) for variant, level in SHARDS}
    if set(shards) != expected:
        raise RuntimeError("KMPC-136 coefficient four-shard register mismatch")
    if set(exact_shards) != {"gamma0", "af0"}:
        raise RuntimeError("KMPC-136 exact two-shard register mismatch")
    source_hashes = _source_hashes()
    normalized: dict[str, dict[str, object]] = {}
    for variant, level in SHARDS:
        key = shard_key(variant, level)
        _require_shard(shards[key], variant, level)
        row = deepcopy(shards[key])
        if level == "audit":
            _require_exact_shard(exact_shards[variant], variant)
            exact = deepcopy(exact_shards[variant])
            solve = row["solve"]
            boundary = exact["high_precision_boundary"]
            original_false = sorted(
                name for name, passed in solve["checks"].items() if passed is False
            )
            driver_pass = bool(boundary["driver"]["pass_driver"])
            holdout_pass = bool(
                boundary["holdout"]["pass_holdout"]
                and boundary["holdout"]["rows_added_to_driver_solve"] == 0
            )
            exact_checks = dict(exact["technical_checks"])
            exact_checks.update({
                "original_false_set_exact": original_false
                == ["M3_driver", "M3_independent_00_0i_holdout"],
                "exact_driver_pass": driver_pass,
                "exact_nonfit_holdout_pass": holdout_pass,
            })
            exact_pass = all(exact_checks.values())
            evidence = {
                "applicable": True,
                "status": "EXACT_BOUNDARY_SECOND_WAVE_COMPLETE",
                "original_solve_pass": solve["pass"],
                "original_false_checks": original_false,
                "superseded_checks": [
                    "M3_driver",
                    "M3_independent_00_0i_holdout",
                ],
                "variant_fuel_recomputed": True,
                "checkpoint_nominal_fuel_used_as_variant_result": False,
                "representation_contract": {
                    "coefficient_solve_uses_binary64_projection": True,
                    "exact_boundary_uses_original_decimal80_HP_M1": True,
                },
                "handoff_sha256": exact["handoff_sha256"],
                "handoff_file_sha256": exact["handoff_file_sha256"],
                "combined_register_handoff": exact["combined_register_handoff"],
                "float_driver_capture": exact["float_driver_capture"],
                "high_precision_boundary": boundary,
                "checks": exact_checks,
                "pass": exact_pass,
            }
            solve["exact_resume_supersession"] = evidence
            solve["checks"]["M3_driver"] = driver_pass
            solve["checks"]["M3_independent_00_0i_holdout"] = holdout_pass
            solve["pass"] = all(solve["checks"].values()) and exact_pass
            row["exact_resume_evidence"] = evidence
            handoff = row["exact_boundary_handoff"]
            row["exact_boundary_handoff"] = {
                "identity": handoff["identity"],
                "variant_fuel_fingerprint": handoff[
                    "variant_fuel_fingerprint"
                ],
                "float_driver_capture": handoff["float_driver_capture"],
                "handoff_sha256": exact["handoff_sha256"],
                "handoff_file_sha256": exact["handoff_file_sha256"],
                "temporary_transport_not_published": True,
            }
        row["source_hashes"] = source_hashes
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
        "A2-K4 P5.3g7 C3 BI/.15 two-wave HP-M1 exact-resume pair"
    )
    payload["identity"]["physical_receipt"] = (
        "four_coefficient_plus_two_exact_shards_gamma0_af0_HP_M1_pair"
    )
    payload["process_architecture"]["HP_M1_exact_resume"] = {
        "checkpoint": v16.CHECKPOINT_NAME,
        "receipt": v17.RECEIPT_NAME,
        "precision_dps": 80,
        "coefficient_solve_representation": "binary64_projection",
        "exact_boundary_representation": "original_decimal80_HP_M1",
        "coefficient_worker_count": 4,
        "exact_boundary_worker_count": 2,
        "temporary_handoffs_removed": temporary_handoffs_removed,
        "source_hash_register_computed_parent_only": True,
        "CPQR_repeated": False,
        "parent_solver_calls": 0,
    }
    payload["HP_M1_exact_resume_audit"] = exact_audit
    payload["HP_M1_exact_resume_pass"] = exact_pass
    payload["pair_pass"] = pair_pass
    payload["candidate_interpretation_not_verdict"] = (
        "PASS_C3_BI_K0P15_ZERO_PAIR_TWO_WAVE_HP_M1_EXACT_RESUME_CANDIDATE_ONLY"
        if pair_pass
        else "REVIEW_C3_BI_K0P15_HP_M1_EXACT_BOUNDARY_UNCLOSED"
    )
    return payload


def aggregate_smoke_shards(
    shards: Mapping[str, Mapping[str, object]],
    exact_shards: Mapping[str, Mapping[str, object]],
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
            == "C3_BI_K0P15_TWO_WAVE_COEFFICIENT_SHARD_SMOKE"
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
    checks["exact_two_shard_register"] = set(exact_shards) == {"gamma0", "af0"}
    for variant in ("gamma0", "af0"):
        row = exact_shards.get(variant)
        checks[f"exact/{variant}"] = bool(
            isinstance(row, dict)
            and row.get("run_id") == RUN_ID
            and row.get("worker_role")
            == "C3_BI_K0P15_TWO_WAVE_EXACT_BOUNDARY_SHARD_SMOKE"
            and row.get("identity")
            == {
                "mode": TARGET[0],
                "k_Mpc_inverse": TARGET[1],
                "variant": variant,
                "support_level": "audit",
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
