"""Exact M3 driver/non-fit holdout resume from the KMPC-108 checkpoint.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
The native HP-M1 CPQR is not repeated.  The audit support solve is rerun only
to capture and fingerprint the frozen 104x104 float64 M3 matrix and to prove
field/fuel parity with the immutable checkpoint.  The final driver and
independent holdout are then reassembled and solved at 80 dps.
"""

from __future__ import annotations

import json
from pathlib import Path
import time

import mpmath as mp

from . import c2_bi_k0p15_high_precision_m1_reassembly_v16_checkpoint_receipt as v16


v15 = v16.v15
v13 = v16.v13
v11 = v13.v11
base = v13.base
physics = v13.physics
coverage = v13.coverage
driver = v11.driver
RECEIPT_NAME = (
    "RUN_KMPC_109_P5_3G7_C2_BI_K0p15_HP_M1_SUPPORT_CHECKPOINT_READ_ONLY_RECEIPT.json"
)
RECEIPT_SHA256 = (
    "21EF9A9BF8D6E437CC848BD76EC026C5621534F35C0D88F99D2BFAFAD28118F9"
)
_V16_SOURCE_HASHES = v16.source_hashes
_V16_CONTRACT_GUARD = v16.contract_guard


def configure(**config: object) -> None:
    v16.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v16.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v16.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V16_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    name = "c2_bi_k0p15_high_precision_m1_reassembly_v17_exact_resume.py"
    hashes[name] = base._sha256_file(here / name)
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V16_CONTRACT_GUARD()
    guard["checks"].update({
        "hp_m1_v17_no_cpqr_repetition": True,
        "hp_m1_v17_checkpoint_and_receipt_sha_required": True,
        "hp_m1_v17_audit_field_and_fuel_parity_required": True,
        "hp_m1_v17_one_104x104_capture": True,
        "hp_m1_v17_exact_driver_80dps": True,
        "hp_m1_v17_independent_holdout_nonfit": True,
        "hp_m1_v17_float_driver_supersession_conditional_only": True,
        "hp_m1_v17_thresholds_unchanged": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _load_json(path: Path, expected_sha: str) -> dict[str, object]:
    if base._sha256_file(path) != expected_sha:
        raise RuntimeError(f"KMPC-110 prerequisite SHA mismatch: {path.name}")
    return json.loads(path.read_text(encoding="utf-8"))


def _restore_checkpoint_states(
    checkpoint: dict[str, object]
) -> tuple[dict[str, dict[int, mp.mpf]], dict[str, dict[int, float]]]:
    m1_names = tuple(physics.STATE_TO_LEGACY)
    fuel_names = ("delta_f", "U_f")
    with mp.workdps(base.PRECISION_DPS):
        m1 = v13._deserialize_m1(
            checkpoint["hp_m1_state_decimal"], m1_names
        )
        if v13._serialize_m1(m1, m1_names) != checkpoint["hp_m1_state_decimal"]:
            raise ValueError("KMPC-110 HP-M1 checkpoint roundtrip mismatch")
    fuel = v13._deserialize_fuel(
        checkpoint["audit_fuel_state_float_hex"], fuel_names
    )
    if v13._serialize_fuel(fuel, fuel_names) != checkpoint["audit_fuel_state_float_hex"]:
        raise ValueError("KMPC-110 F0 checkpoint roundtrip mismatch")
    return m1, fuel


def _resume_fixture(result_dir: Path) -> dict[str, bool]:
    raw = _load_json(result_dir / v16.CHECKPOINT_NAME, v16.CHECKPOINT_SHA256)
    receipt = _load_json(result_dir / RECEIPT_NAME, RECEIPT_SHA256)
    checkpoint = raw["resume_checkpoint"]
    m1, fuel = _restore_checkpoint_states(checkpoint)
    observed = v16._checkpoint_fingerprint(checkpoint)
    return {
        "checkpoint_fingerprint_exact": observed == v16.SERIALIZED_STATE_SHA256,
        "m1_order_exact": tuple(m1) == tuple(physics.STATE_TO_LEGACY),
        "fuel_order_exact": tuple(fuel) == ("delta_f", "U_f"),
        "receipt_contract_complete": bool(receipt["passed_execution_contract"]),
        "receipt_resume_allowed": bool(
            receipt["checkpoint_receipt"]["exact_driver_resume_allowed"]
        ),
        "capture_owners_initial": v11._owners_restored(),
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    payload = v16.run_smoke(max_runtime_seconds, result_dir)
    payload["run_id"] = "KMPC-110"
    payload["checks"].update({
        f"resume_{name}": value for name, value in _resume_fixture(result_dir).items()
    })
    payload["checks"]["resume_contract_guard"] = bool(contract_guard()["pass"])
    payload["checks"]["resume_identity_exact"] = payload["run_id"] == "KMPC-110"
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    if (mode, k_mpc) != ("BI", 0.15):
        raise ValueError("KMPC-110 exact-resume atom identity mismatch")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError("KMPC-110 exact resume deadline exceeded")

    raw = _load_json(result_dir / v16.CHECKPOINT_NAME, v16.CHECKPOINT_SHA256)
    receipt = _load_json(result_dir / RECEIPT_NAME, RECEIPT_SHA256)
    checkpoint = raw["resume_checkpoint"]
    if v16._checkpoint_fingerprint(checkpoint) != v16.SERIALIZED_STATE_SHA256:
        raise RuntimeError("KMPC-110 serialized-state fingerprint mismatch")
    hp_m1, checkpoint_fuel = _restore_checkpoint_states(checkpoint)
    receipt_allowed = bool(
        receipt["passed_execution_contract"]
        and receipt["checkpoint_receipt"]["exact_driver_resume_allowed"]
        and receipt["candidate_interpretation_not_verdict"]
        == "REVIEW_C2_BI_K0p15_HP_M1_CHECKPOINT_RECEIPT_EXACT_RESUME_ALLOWED"
    )
    if not receipt_allowed:
        raise RuntimeError("KMPC-110 receipt does not allow exact resume")
    deadline()

    inputs = physics._variant_inputs(coverage.VARIANT)
    audit_support = tuple(coverage.SUPPORTS["BI"]["audit"])
    converted_paths: list[str] = []
    with v11._float_driver_capture():
        audit = coverage._solve_support(
            mode, k_mpc, audit_support, inputs, hp_m1, deadline
        )
        serialized_audit = v15._convert_mpf(
            audit, "$.audit_solve", converted_paths
        )
        regenerated_fuel = v13._serialize_fuel(
            audit["fuel"]["state"], ("delta_f", "U_f")
        )
        combined, merge = v11._merge_m1_and_fuel(hp_m1, checkpoint_fuel)
        with mp.workdps(base.PRECISION_DPS):
            exact_boundary = driver._exact_driver_boundary(
                k_mpc, inputs, combined, audit_support
            )
    capture = dict(v11._CAPTURE_DIAGNOSTIC or {})
    deadline()

    raw_false = {
        name for name, value in raw["checks"].items() if value is False
    }
    audit_false = {
        name for name, value in raw["audit_solve"]["checks"].items()
        if value is False
    }
    audit_diagnostic = raw["audit_solve"]["m3"]["diagnostics"]
    checkpoint_non_driver_pass = bool(
        raw["M1"]["pass"]
        and raw["accepted_solve"]["pass"]
        and raw["audit_solve"]["fuel"]["diagnostics"]["pass_driver"]
        and audit_diagnostic["pass_rank"]
        and audit_diagnostic["pass_production_contract"]
        and audit_diagnostic["holdout"]["pass_holdout"]
        and raw["common_pass"]
        and raw["tail_pass"]
        and raw["S_C0_actual_guard"]["pass"]
        and raw["background_guard"]["pass"]
    )
    target = exact_boundary["holdout"]["Einstein_0i_7"]
    exact_driver_pass = bool(exact_boundary["driver"]["pass_driver"])
    exact_holdout_pass = bool(
        exact_boundary["holdout"]["pass_holdout"]
        and exact_boundary["holdout"]["rows_added_to_driver_solve"] == 0
        and target["metric"] <= physics.HOLDOUT_TOL
    )
    technical_checks = {
        "contract_guard": bool(contract_guard()["pass"]),
        "checkpoint_file_sha_exact": base._sha256_file(
            result_dir / v16.CHECKPOINT_NAME
        ) == v16.CHECKPOINT_SHA256,
        "receipt_file_sha_exact": base._sha256_file(
            result_dir / RECEIPT_NAME
        ) == RECEIPT_SHA256,
        "receipt_exact_resume_allowed": receipt_allowed,
        "serialized_state_sha_exact": checkpoint["serialized_state_sha256"]
        == v16.SERIALIZED_STATE_SHA256,
        "audit_payload_field_parity": serialized_audit == raw["audit_solve"],
        "audit_fuel_float_hex_parity": regenerated_fuel
        == checkpoint["audit_fuel_state_float_hex"],
        "audit_false_set_exact": audit_false == {"M3_driver"},
        "raw_false_set_exact": raw_false
        == {"audit_support_complete", "pre_exact_core_complete"},
        "combined_register_13": merge["combined_state_count"] == 13,
        "checkpoint_fuel_merge_unchanged": bool(merge["fuel_values_unchanged"]),
        "float_driver_capture_once": capture.get("audit_driver_capture_count") == 1,
        "float_driver_capture_shape": capture.get("shape") == [104, 104],
        "capture_owners_restored": v11._owners_restored(),
        "one_exact_driver_solve": exact_boundary["exact_driver_solve_count"] == 1,
        "holdout_rows_not_fit": exact_boundary["holdout"]["rows_added_to_driver_solve"] == 0,
        "checkpoint_non_driver_gates_complete": checkpoint_non_driver_pass,
        "no_cpqr_repetition": True,
    }
    if not all(technical_checks.values()):
        false_names = sorted(name for name, value in technical_checks.items() if not value)
        raise RuntimeError(f"KMPC-110 technical resume contract failed: {false_names}")
    physics_checks = {
        "float_m3_driver_was_only_open_gate": audit_false == {"M3_driver"},
        "exact_driver_pass": exact_driver_pass,
        "exact_independent_holdout_pass": exact_holdout_pass,
    }
    candidate_pass = bool(all(physics_checks.values()))
    if not exact_driver_pass:
        candidate = "REVIEW_C2_BI_K0p15_HP_M1_EXACT_DRIVER_UNCLOSED"
    elif not exact_holdout_pass:
        candidate = "REVIEW_C2_BI_K0p15_HP_M1_EXACT_NONFIT_HOLDOUT_UNCLOSED"
    else:
        candidate = "PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_HP_M1_CANDIDATE_ONLY"

    payload: dict[str, object] = {
        "test": "KMPC-110 BI/k=.15 checkpointed exact M3 driver/holdout resume",
        "run_id": "KMPC-110",
        "execution_status": "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT",
        "authorship": {
            "theory_author": "Martin Jambor",
            "script_creator": "Codex (OpenAI)",
        },
        "atom_id": "BI/k=0.15/nominal",
        "identity": {"mode": mode, "k_Mpc_inverse": k_mpc, "variant": "nominal"},
        "scope": {
            "included": "checkpoint restore; audit matrix/fuel parity; exact 80-dps M3 driver and independent holdout",
            "excluded": "CPQR rerun; accepted solve rerun; other C2 atoms; [0,9]; S-M; ODE; P5.4; G8/G9; data",
        },
        "source_hashes": source_hashes(),
        "contract_guard": contract_guard(),
        "checkpoint_inputs": {
            "checkpoint_file": v16.CHECKPOINT_NAME,
            "checkpoint_sha256": v16.CHECKPOINT_SHA256,
            "receipt_file": RECEIPT_NAME,
            "receipt_sha256": RECEIPT_SHA256,
            "serialized_state_sha256": v16.SERIALIZED_STATE_SHA256,
        },
        "M1": {"pass": bool(raw["M1"]["pass"]), "source": "KMPC-108_DECIMAL90_CHECKPOINT"},
        "accepted_solve": {
            "pass": bool(raw["accepted_solve"]["pass"]),
            "source": "KMPC-108_READ_ONLY_NOT_RERUN",
        },
        "audit_solve": serialized_audit,
        "audit_resume": {
            "field_parity_with_KMPC108": True,
            "fuel_float_hex_parity": True,
            "converted_mpf_paths": converted_paths,
            "float_driver_capture": capture,
            "original_false_checks": sorted(audit_false),
        },
        "combined_register_handoff": merge,
        "high_precision_downstream_boundary": exact_boundary,
        "Einstein_0i_7_after_hp_m1_downstream": target,
        "upstream_precision_scope": {
            "M1": "KMPC108_DECIMAL90_RESTORED_MPMATH_80DPS",
            "F0": "KMPC108_AUDIT_FUEL_FLOAT_HEX_EXACT_BINARY64",
            "background_inputs": "FROZEN_BINARY64_EXACTLY_BRIDGED_TO_MPMATH",
            "inherited_exact_boundary_scope_label": exact_boundary["scope"],
        },
        "technical_checks": technical_checks,
        "physics_checks": physics_checks,
        "passed_execution_contract": all(technical_checks.values()),
        "all_candidate_gates_pass": candidate_pass,
        "pass_c2_atom_candidate": candidate_pass,
        "core_pass": bool(checkpoint_non_driver_pass and exact_driver_pass),
        "common_pass": bool(raw["common_pass"]),
        "tail_pass": bool(raw["tail_pass"]),
        "background_guard": raw["background_guard"],
        "candidate_interpretation_not_verdict": candidate,
        "physics_verdict_role": "CANDIDATE_ONLY_PENDING_INTERNAL_AUDIT",
        "thresholds": raw["thresholds"],
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "score_effect": "NONE_PENDING_INTERNAL_AUDIT",
        "release_trigger": "NONE",
        "zenodo_trigger": "NONE",
        "prediction_table_effect": "NONE",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }
    final_paths: list[str] = []
    safe_payload = v15._convert_mpf(payload, "$", final_paths)
    if v15._contains_mpf(safe_payload):
        raise TypeError("KMPC-110 mpf remains after final payload conversion")
    safe_payload["final_payload_mpf_serialization"] = {
        "converted_count": len(final_paths),
        "converted_paths": final_paths,
        "roundtrip_exact_at_80dps": True,
    }
    return safe_payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("checkpointed exact resume has no aggregate scope")
