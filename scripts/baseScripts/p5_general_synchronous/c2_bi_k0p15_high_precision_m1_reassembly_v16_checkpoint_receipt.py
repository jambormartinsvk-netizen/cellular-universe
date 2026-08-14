"""Read-only receipt for the immutable KMPC-108 support checkpoint.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
No equation or numerical solve is executed.  The receipt verifies the raw
file, its lossless resume register, and the exact false-check set before an
exact-driver resume may be preregistered.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import time

from . import c2_bi_k0p15_high_precision_m1_reassembly_v15_checkpoint_json_successor as v15


base = v15.base
v13 = v15.v14.v13
_V15_SOURCE_HASHES = v15.source_hashes
_V15_CONTRACT_GUARD = v15.contract_guard
CHECKPOINT_NAME = (
    "RUN_KMPC_108_P5_3G7_C2_BI_K0p15_HP_M1_SUPPORT_CHECKPOINT_JSON_SUCCESSOR.json"
)
CHECKPOINT_SHA256 = (
    "683D867D19324B7B45F3724545FFB1D975DFBED883936298D790C12836E9D995"
)
SERIALIZED_STATE_SHA256 = (
    "402B42E11C3582B4E3E46D047EA917A4C256E552F65C9DB070589150675EBF40"
)
EXPECTED_MPF_PATHS = (
    "$.accepted_solve.fuel.diagnostics.leading_expected.U_f",
    "$.accepted_solve.fuel.diagnostics.leading_expected.delta_f",
    "$.accepted_solve.fuel.diagnostics.leading_max_absolute_difference",
    "$.audit_solve.fuel.diagnostics.leading_expected.U_f",
    "$.audit_solve.fuel.diagnostics.leading_expected.delta_f",
    "$.audit_solve.fuel.diagnostics.leading_max_absolute_difference",
)


def configure(**config: object) -> None:
    v15.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v15.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v15.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V15_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    name = (
        "c2_bi_k0p15_high_precision_m1_reassembly_v16_checkpoint_receipt.py"
    )
    hashes[name] = base._sha256_file(here / name)
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V15_CONTRACT_GUARD()
    guard["checks"].update({
        "hp_m1_v16_read_only_receipt": True,
        "hp_m1_v16_no_solver_or_equation_execution": True,
        "hp_m1_v16_exact_checkpoint_file_sha": True,
        "hp_m1_v16_exact_false_check_set": True,
        "hp_m1_v16_no_physics_pass": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _checkpoint_fingerprint(checkpoint: dict[str, object]) -> str:
    digest = hashlib.sha256()
    groups = (
        ("M1", checkpoint["m1_state_order"], checkpoint["hp_m1_state_decimal"]),
        ("F0", checkpoint["fuel_state_order"], checkpoint["audit_fuel_state_float_hex"]),
    )
    for owner, names, state in groups:
        digest.update(f"{owner}|".encode("ascii"))
        for name in names:
            digest.update(f"{name}|".encode("ascii"))
            values = state[name]
            for power in sorted(values, key=int):
                digest.update(f"{power}|{values[power]}|".encode("ascii"))
    return digest.hexdigest().upper()


def _fingerprint_fixture() -> dict[str, bool]:
    checkpoint = {
        "m1_state_order": ["x"],
        "fuel_state_order": ["f"],
        "hp_m1_state_decimal": {"x": {"1": "2.0", "0": "1.0"}},
        "audit_fuel_state_float_hex": {"f": {"0": "0x1.0000000000000p+0"}},
    }
    first = _checkpoint_fingerprint(checkpoint)
    checkpoint["hp_m1_state_decimal"]["x"] = {"0": "1.0", "1": "2.0"}
    second = _checkpoint_fingerprint(checkpoint)
    checkpoint["hp_m1_state_decimal"]["x"]["1"] = "2.1"
    changed = _checkpoint_fingerprint(checkpoint)
    return {
        "fingerprint_order_reconstruction_stable": first == second,
        "fingerprint_value_change_detected": changed != second,
        "fingerprint_is_sha256": len(first) == 64,
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    checks = {
        "contract_guard": bool(contract_guard()["pass"]),
        **_fingerprint_fixture(),
        "checkpoint_present": (result_dir / CHECKPOINT_NAME).is_file(),
        "checkpoint_sha_exact": base._sha256_file(result_dir / CHECKPOINT_NAME)
        == CHECKPOINT_SHA256,
        "no_result_file_written": True,
    }
    return {
        "run_id": "KMPC-109",
        "mode": "SMOKE_NO_RESULT_FILE",
        "checks": checks,
        "passed": all(checks.values()),
    }


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    if (mode, k_mpc) != ("BI", 0.15):
        raise ValueError("KMPC-109 receipt atom identity mismatch")
    started = time.monotonic()
    path = result_dir / CHECKPOINT_NAME
    observed_sha = base._sha256_file(path)
    raw = json.loads(path.read_text(encoding="utf-8"))
    checkpoint = raw["resume_checkpoint"]
    m1_order = tuple(v13.physics.STATE_TO_LEGACY)
    fuel_order = ("delta_f", "U_f")
    combined_order = tuple(v13.coverage.ra_contract.AUTHORITATIVE_STATE)
    raw_false = {
        name for name, value in raw["checks"].items() if value is False
    }
    audit_false = {
        name for name, value in raw["audit_solve"]["checks"].items()
        if value is False
    }
    diagnostic = raw["audit_solve"]["m3"]["diagnostics"]
    observed_state_sha = _checkpoint_fingerprint(checkpoint)
    checks = {
        "contract_guard": bool(contract_guard()["pass"]),
        "checkpoint_file_sha_exact": observed_sha == CHECKPOINT_SHA256,
        "checkpoint_run_identity": raw["run_id"] == "KMPC-108",
        "checkpoint_completed_no_verdict": raw["execution_status"]
        == "COMPLETED_CHECKPOINT_NO_PHYSICS_VERDICT",
        "checkpoint_candidate_uncLOSED": raw["candidate_interpretation_not_verdict"]
        == "REVIEW_C2_BI_K0p15_HP_M1_SUPPORT_CHECKPOINT_UNCLOSED",
        "checkpoint_source_hashes_exact": raw["source_hashes"]
        == _V15_SOURCE_HASHES(),
        "checkpoint_schema_exact": checkpoint["schema"]
        == "KMPC106_HP_M1_DECIMAL90_PLUS_AUDIT_FUEL_FLOAT_HEX_V1",
        "m1_state_order_exact": tuple(checkpoint["m1_state_order"]) == m1_order,
        "fuel_state_order_exact": tuple(checkpoint["fuel_state_order"]) == fuel_order,
        "combined_state_order_exact": tuple(checkpoint["combined_state_order"])
        == combined_order,
        "serialized_state_sha_declared_exact": checkpoint["serialized_state_sha256"]
        == SERIALIZED_STATE_SHA256,
        "serialized_state_sha_recomputed_exact": observed_state_sha
        == SERIALIZED_STATE_SHA256,
        "checkpoint_roundtrips_pass": bool(
            checkpoint["m1_roundtrip_exact_at_80dps"]
            and checkpoint["fuel_roundtrip_exact_binary64"]
        ),
        "mpf_conversion_paths_exact": tuple(
            raw["payload_mpf_serialization"]["converted_paths"]
        ) == EXPECTED_MPF_PATHS,
        "mpf_conversion_count_exact": raw["payload_mpf_serialization"]["converted_count"]
        == len(EXPECTED_MPF_PATHS),
        "raw_false_checks_exact": raw_false
        == {"audit_support_complete", "pre_exact_core_complete"},
        "audit_false_checks_exact": audit_false == {"M3_driver"},
        "m1_and_accepted_complete": bool(raw["M1"]["pass"] and raw["accepted_solve"]["pass"]),
        "audit_f0_complete": bool(raw["audit_solve"]["fuel"]["diagnostics"]["pass_driver"]),
        "audit_m3_rank_and_contract": bool(
            diagnostic["pass_rank"] and diagnostic["pass_production_contract"]
        ),
        "audit_m3_holdout_pass": bool(diagnostic["holdout"]["pass_holdout"]),
        "audit_m3_only_driver_unclosed": bool(not diagnostic["pass_driver"]),
        "non_driver_support_gates_complete": bool(
            raw["common_pass"]
            and raw["tail_pass"]
            and raw["S_C0_actual_guard"]["pass"]
            and raw["background_guard"]["pass"]
        ),
        "physics_pass_suppressed": raw["pass_c2_atom_candidate"] is False,
    }
    resume_allowed = all(checks.values())
    return {
        "test": "KMPC-109 read-only receipt of KMPC-108 support checkpoint",
        "run_id": "KMPC-109",
        "execution_status": "COMPLETED_READ_ONLY_CHECKPOINT_RECEIPT",
        "authorship": {
            "theory_author": "Martin Jambor",
            "script_creator": "Codex (OpenAI)",
        },
        "atom_id": "BI/k=0.15/nominal/checkpoint-receipt",
        "identity": {"mode": mode, "k_Mpc_inverse": k_mpc, "variant": "nominal"},
        "scope": {
            "included": "read-only SHA/schema/register/false-check receipt of KMPC-108",
            "excluded": "all solves; equation execution; exact driver; C2 PASS; other atoms",
        },
        "source_hashes": source_hashes(),
        "contract_guard": contract_guard(),
        "checkpoint_receipt": {
            "file": CHECKPOINT_NAME,
            "expected_file_sha256": CHECKPOINT_SHA256,
            "observed_file_sha256": observed_sha,
            "expected_serialized_state_sha256": SERIALIZED_STATE_SHA256,
            "observed_serialized_state_sha256": observed_state_sha,
            "raw_false_checks": sorted(raw_false),
            "audit_false_checks": sorted(audit_false),
            "external_timeout_124_after_publish": True,
            "exact_driver_resume_allowed": resume_allowed,
        },
        "checks": checks,
        "passed_execution_contract": resume_allowed,
        "M1": {"pass": bool(raw["M1"]["pass"]), "role": "READ_ONLY_RECEIPT"},
        "core_pass": False,
        "common_pass": bool(raw["common_pass"]),
        "tail_pass": bool(raw["tail_pass"]),
        "background_guard": raw["background_guard"],
        "pass_c2_atom_candidate": False,
        "candidate_interpretation_not_verdict": (
            "REVIEW_C2_BI_K0p15_HP_M1_CHECKPOINT_RECEIPT_EXACT_RESUME_ALLOWED"
            if resume_allowed
            else "REVIEW_C2_BI_K0p15_HP_M1_CHECKPOINT_RECEIPT_UNCLOSED"
        ),
        "physics_verdict_role": "READ_ONLY_CHECKPOINT_RECEIPT_NO_PHYSICS_VERDICT",
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "score_effect": "NONE_READ_ONLY_RECEIPT",
        "release_trigger": "NONE",
        "zenodo_trigger": "NONE",
        "prediction_table_effect": "NONE",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("checkpoint receipt has no aggregate scope")
