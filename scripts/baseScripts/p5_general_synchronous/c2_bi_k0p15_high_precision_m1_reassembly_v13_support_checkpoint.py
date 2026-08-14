"""Verdict-free HP-M1 plus F0/M3 support checkpoint for BI/k=.15.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
PF-107 showed that CPQR, two support solves and the exact 104x104 boundary
do not belong in one 45-second atom.  This module executes only the reusable
prefix and serializes it losslessly for a separately preregistered resume.
It never assigns a C2 physics PASS.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
import time

import mpmath as mp

from . import c2_bi_k0p15_high_precision_m1_reassembly_v12_downstream_identity_successor as v12
from . import c2_fourier_coverage as coverage


v11 = v12.v11
v9 = v11.v9
base = v11.base
physics = v11.physics
_V12_SOURCE_HASHES = v12.source_hashes
_V12_CONTRACT_GUARD = v12.contract_guard


def configure(**config: object) -> None:
    v12.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v12.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v12.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V12_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    name = (
        "c2_bi_k0p15_high_precision_m1_reassembly_v13_support_checkpoint.py"
    )
    hashes[name] = base._sha256_file(here / name)
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V12_CONTRACT_GUARD()
    guard["checks"].update({
        "hp_m1_v13_checkpoint_has_no_exact_driver": True,
        "hp_m1_v13_checkpoint_has_no_physics_pass": True,
        "hp_m1_v13_decimal_m1_serialization": True,
        "hp_m1_v13_float_hex_fuel_serialization": True,
        "hp_m1_v13_resume_requires_immutable_sha": True,
        "hp_m1_v13_runtime_limit_unchanged": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _serialize_m1(
    state: dict[str, dict[int, object]], names: tuple[str, ...]
) -> dict[str, dict[str, str]]:
    if tuple(state) != names:
        raise ValueError("KMPC-106 M1 state order mismatch")
    return {
        name: {
            str(power): mp.nstr(mp.mpf(value), n=90, strip_zeros=False)
            for power, value in sorted(state[name].items())
        }
        for name in names
    }


def _deserialize_m1(
    payload: dict[str, dict[str, str]], names: tuple[str, ...]
) -> dict[str, dict[int, mp.mpf]]:
    if tuple(payload) != names:
        raise ValueError("KMPC-106 serialized M1 order mismatch")
    return {
        name: {int(power): mp.mpf(value) for power, value in values.items()}
        for name, values in payload.items()
    }


def _serialize_fuel(
    state: dict[str, dict[int, object]], names: tuple[str, ...]
) -> dict[str, dict[str, str]]:
    if tuple(state) != names:
        raise ValueError("KMPC-106 fuel state order mismatch")
    return {
        name: {
            str(power): float(value).hex()
            for power, value in sorted(state[name].items())
        }
        for name in names
    }


def _deserialize_fuel(
    payload: dict[str, dict[str, str]], names: tuple[str, ...]
) -> dict[str, dict[int, float]]:
    if tuple(payload) != names:
        raise ValueError("KMPC-106 serialized fuel order mismatch")
    return {
        name: {int(power): float.fromhex(value) for power, value in values.items()}
        for name, values in payload.items()
    }


def _serialized_fingerprint(
    m1: dict[str, dict[str, str]], fuel: dict[str, dict[str, str]]
) -> str:
    digest = hashlib.sha256()
    for owner, state in (("M1", m1), ("F0", fuel)):
        digest.update(f"{owner}|".encode("ascii"))
        for name, values in state.items():
            digest.update(f"{name}|".encode("ascii"))
            for power, value in values.items():
                digest.update(f"{power}|{value}|".encode("ascii"))
    return digest.hexdigest().upper()


def _roundtrip_fixture() -> dict[str, bool]:
    m1_names = tuple(physics.STATE_TO_LEGACY)
    fuel_names = ("delta_f", "U_f")
    with mp.workdps(base.PRECISION_DPS):
        special = mp.mpf(1) / mp.mpf(7) + mp.mpf("1e-70")
        m1 = {
            name: {0: special + index, 1: special - index}
            for index, name in enumerate(m1_names)
        }
        encoded_m1 = _serialize_m1(m1, m1_names)
        decoded_m1 = _deserialize_m1(encoded_m1, m1_names)
        m1_exact = all(
            decoded_m1[name][power] == value
            for name, values in m1.items()
            for power, value in values.items()
        )
    fuel = {
        "delta_f": {0: -0.0, 1: 0.1},
        "U_f": {0: 1.0e-300, 1: -3.25},
    }
    encoded_fuel = _serialize_fuel(fuel, fuel_names)
    decoded_fuel = _deserialize_fuel(encoded_fuel, fuel_names)
    fuel_exact = all(
        decoded_fuel[name][power].hex() == value.hex()
        for name, values in fuel.items()
        for power, value in values.items()
    )
    fingerprint = _serialized_fingerprint(encoded_m1, encoded_fuel)
    return {
        "m1_decimal_roundtrip_80dps": m1_exact,
        "fuel_float_hex_roundtrip_exact": fuel_exact,
        "serialized_fingerprint_sha256": len(fingerprint) == 64,
        "authoritative_m1_order": tuple(encoded_m1) == m1_names,
        "authoritative_fuel_order": tuple(encoded_fuel) == fuel_names,
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    payload = v12.run_smoke(max_runtime_seconds, result_dir)
    payload["run_id"] = "KMPC-106"
    payload["checks"].update({
        f"checkpoint_{name}": value for name, value in _roundtrip_fixture().items()
    })
    payload["checks"]["checkpoint_contract_guard"] = bool(contract_guard()["pass"])
    payload["checks"]["checkpoint_identity_exact"] = payload["run_id"] == "KMPC-106"
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    if (mode, k_mpc) != ("BI", 0.15):
        raise ValueError("KMPC-106 checkpoint atom identity mismatch")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError("KMPC-106 support checkpoint deadline exceeded")

    prerequisites = coverage._load_c1(result_dir)
    guard = contract_guard()
    frozen_contract = physics.validate_frozen_contract()
    independent_contract = coverage.ra_contract.validate_contract(
        coverage.collective_contract.EXPECTED_STATE,
        coverage.collective_contract.EXPECTED_DRIVER,
        coverage.collective_contract.EXPECTED_HOLDOUT,
    )
    frozen_b1 = physics.b1_guard.build_contract_guard(
        max_runtime_seconds=min(1.0, max_runtime_seconds)
    )
    tca0 = physics.production_tca0_reduction_guard()
    inputs = physics._variant_inputs(coverage.VARIANT)
    accepted_support = tuple(coverage.SUPPORTS["BI"]["accepted"])
    audit_support = tuple(coverage.SUPPORTS["BI"]["audit"])

    reference_legacy, _, reference_metadata = (
        physics.m1_anchor.solve_standard_seed_anchored(
            mode, k_mpc, inputs, deadline, order=base.ORDER
        )
    )
    reference_standard = {
        target: dict(reference_legacy[source])
        for target, source in physics.STATE_TO_LEGACY.items()
    }
    with mp.workdps(base.PRECISION_DPS):
        with v9._solver_overlay():
            hp_standard, m1_boundary = base._m1_reassembly(
                inputs, reference_standard
            )
            cpqr = dict(v9._CPQR_DIAGNOSTIC or {})
    deadline()

    m1_pass = bool(
        cpqr.get("rank") == 98
        and cpqr.get("rank_full")
        and cpqr.get("orthogonality_pass")
        and cpqr.get("factorization_pass")
        and cpqr.get("normal_residual_pass")
        and m1_boundary["pass"]
    )
    rfs = coverage._rfs_guard(mode, hp_standard, inputs)
    accepted = coverage._solve_support(
        mode, k_mpc, accepted_support, inputs, hp_standard, deadline
    )
    audit = coverage._solve_support(
        mode, k_mpc, audit_support, inputs, hp_standard, deadline
    )
    combined, merge = v11._merge_m1_and_fuel(
        hp_standard, audit["fuel"]["state"]
    )
    deadline()

    common = {
        "F0": coverage._common_bridge(
            accepted["fuel"]["state"], audit["fuel"]["state"], accepted_support
        ),
        "M3": coverage._common_bridge(
            accepted["m3"]["fractional_state"],
            audit["m3"]["fractional_state"],
            accepted_support,
        ),
    }
    tails = {
        "F0": coverage._tail(
            audit["fuel"]["state"], tuple(sorted(audit["fuel"]["state"])),
            accepted_support, audit_support,
        ),
        "M3": coverage._tail(
            audit["m3"]["fractional_state"],
            tuple(coverage.ra_contract.AUTHORITATIVE_STATE),
            accepted_support, audit_support,
        ),
    }
    s_c0 = coverage.support_tools.c1._s_c0_actual_coefficient_guard({
        "m3_primary": {"fractional_state": accepted["m3"]["fractional_state"]},
        "m3_extended": {"fractional_state": audit["m3"]["fractional_state"]},
    })
    background = coverage._background_guard(inputs, k_mpc, audit_support[1])
    common_pass = all(row["pass"] for row in common.values())
    tail_pass = all(row["pass"] for row in tails.values())
    pre_exact_core_pass = bool(
        guard["pass"]
        and len(prerequisites) == 5
        and frozen_contract["valid"]
        and independent_contract.valid
        and frozen_b1["execution_verdict"] == "PASS_R_A_B1_CONTRACT_GUARD_ONLY"
        and tca0["pass"]
        and m1_pass
        and rfs["pass"]
        and accepted["pass"]
        and audit["pass"]
        and s_c0["pass"]
    )
    m1_names = tuple(physics.STATE_TO_LEGACY)
    fuel_names = ("delta_f", "U_f")
    with mp.workdps(base.PRECISION_DPS):
        serialized_m1 = _serialize_m1(hp_standard, m1_names)
        roundtrip_m1 = _deserialize_m1(serialized_m1, m1_names)
        m1_roundtrip_exact = all(
            roundtrip_m1[name][power] == mp.mpf(value)
            for name, values in hp_standard.items()
            for power, value in values.items()
        )
    serialized_fuel = _serialize_fuel(audit["fuel"]["state"], fuel_names)
    roundtrip_fuel = _deserialize_fuel(serialized_fuel, fuel_names)
    fuel_roundtrip_exact = all(
        roundtrip_fuel[name][power].hex() == float(value).hex()
        for name, values in audit["fuel"]["state"].items()
        for power, value in values.items()
    )
    serialized_sha = _serialized_fingerprint(serialized_m1, serialized_fuel)
    checks = {
        "contract_guard": bool(guard["pass"]),
        "native_hp_m1_complete": m1_pass,
        "accepted_support_complete": bool(accepted["pass"]),
        "audit_support_complete": bool(audit["pass"]),
        "combined_register_13": len(combined) == 13,
        "fuel_merge_unchanged": bool(merge["fuel_values_unchanged"]),
        "m1_decimal_roundtrip_80dps": m1_roundtrip_exact,
        "fuel_float_hex_roundtrip_exact": fuel_roundtrip_exact,
        "pre_exact_core_complete": pre_exact_core_pass,
        "common_complete": common_pass,
        "tail_complete": tail_pass,
        "background_complete": bool(background["pass"]),
        "owners_restored": v11._owners_restored() and v9._owners_restored(),
        "physics_pass_suppressed": True,
    }
    deadline()
    candidate = (
        "REVIEW_C2_BI_K0p15_HP_M1_SUPPORT_CHECKPOINT_COMPLETE"
        if all(checks.values())
        else "REVIEW_C2_BI_K0p15_HP_M1_SUPPORT_CHECKPOINT_UNCLOSED"
    )
    m1_boundary.update({
        "solver": "NATIVE_MPMATH_80DPS_TWO_PASS_MGS_CPQR",
        "native_rank_revealing_diagnostic": cpqr,
        "authoritative_high_precision_m1_solve_count": 1,
        "pass": m1_pass,
    })
    return {
        "test": "KMPC-106 BI/k=.15 HP-M1 plus support checkpoint",
        "run_id": "KMPC-106",
        "execution_status": "COMPLETED_CHECKPOINT_NO_PHYSICS_VERDICT",
        "authorship": {
            "theory_author": "Martin Jambor",
            "script_creator": "Codex (OpenAI)",
        },
        "atom_id": "BI/k=0.15/nominal/checkpoint",
        "identity": {"mode": mode, "k_Mpc_inverse": k_mpc, "variant": "nominal"},
        "scope": {
            "included": "native HP-M1 CPQR; accepted/audit F0/M3; lossless resume checkpoint",
            "excluded": "exact driver; independent holdout; C2 PASS; other atoms; S-M; ODE; data",
        },
        "source_hashes": source_hashes(),
        "contract_guard": guard,
        "C1_prerequisites": prerequisites,
        "frozen_contract": frozen_contract,
        "independent_contract_valid": independent_contract.valid,
        "frozen_B1_left_null_Bianchi": frozen_b1,
        "production_TCA0_bridge": tca0,
        "frozen_reference_standard": {
            "method": "LIVE_FROZEN_BINARY64_HARD_ANCHORED_M1",
            "metadata": reference_metadata,
        },
        "M1": {"pass": m1_pass, "boundary": m1_boundary},
        "combined_R_fs_guard": rfs,
        "accepted_solve": accepted,
        "audit_solve": audit,
        "common": common,
        "common_pass": common_pass,
        "tails": tails,
        "tail_pass": tail_pass,
        "S_C0_actual_guard": s_c0,
        "background_guard": background,
        "core_pass": pre_exact_core_pass,
        "combined_register_handoff": merge,
        "resume_checkpoint": {
            "schema": "KMPC106_HP_M1_DECIMAL90_PLUS_AUDIT_FUEL_FLOAT_HEX_V1",
            "m1_state_order": list(m1_names),
            "fuel_state_order": list(fuel_names),
            "combined_state_order": list(combined),
            "hp_m1_state_decimal": serialized_m1,
            "audit_fuel_state_float_hex": serialized_fuel,
            "serialized_state_sha256": serialized_sha,
            "m1_roundtrip_exact_at_80dps": m1_roundtrip_exact,
            "fuel_roundtrip_exact_binary64": fuel_roundtrip_exact,
            "resume_must_verify_file_sha256": True,
        },
        "checks": checks,
        "passed_execution_contract": all(checks.values()),
        "candidate_interpretation_not_verdict": candidate,
        "physics_verdict_role": "CHECKPOINT_ONLY_NO_PHYSICS_VERDICT",
        "pass_c2_atom_candidate": False,
        "thresholds": {
            "driver": physics.DRIVER_TOL,
            "holdout": physics.HOLDOUT_TOL,
            "common": physics.LOW_COEFFICIENT_TOL,
            "tail": physics.TAIL_TOL,
            "absolute_fallback": physics.ABS_FALLBACK_TOL,
            "background_relative": physics.BACKGROUND_K_TOL,
            "cpqr_rank_relative": "1e-60",
        },
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "score_effect": "NONE_CHECKPOINT_ONLY",
        "release_trigger": "NONE",
        "zenodo_trigger": "NONE",
        "prediction_table_effect": "NONE",
        "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
    }


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("HP-M1 support checkpoint has no aggregate scope")
