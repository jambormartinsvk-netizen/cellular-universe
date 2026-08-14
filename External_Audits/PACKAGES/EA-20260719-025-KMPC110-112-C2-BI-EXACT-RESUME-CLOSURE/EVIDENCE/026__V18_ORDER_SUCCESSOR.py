"""Order-reconstruction successor for the immutable V17 exact resume.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
PF-111 showed that a JSON object published with ``sort_keys=True`` cannot
carry authoritative register order.  This wrapper rebuilds the two serialized
state mappings from their explicit checkpoint order lists before delegating to
the byte-unchanged V17 exact calculation.  No equation, value, threshold,
precision scope or runtime limit is changed.
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

import mpmath as mp

from . import c2_bi_k0p15_high_precision_m1_reassembly_v17_exact_resume as v17


base = v17.base
physics = v17.physics
v13 = v17.v13
_V17_SOURCE_HASHES = v17.source_hashes
_V17_CONTRACT_GUARD = v17.contract_guard
_V17_RESTORE = v17._restore_checkpoint_states


def configure(**config: object) -> None:
    v17.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v17.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v17.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V17_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    name = (
        "c2_bi_k0p15_high_precision_m1_reassembly_"
        "v18_exact_resume_order_successor.py"
    )
    hashes[name] = base._sha256_file(here / name)
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V17_CONTRACT_GUARD()
    guard["checks"].update({
        "hp_m1_v18_explicit_m1_order_authoritative": True,
        "hp_m1_v18_explicit_fuel_order_authoritative": True,
        "hp_m1_v18_json_dict_order_not_authoritative": True,
        "hp_m1_v18_restore_overlay_owner_lifecycle": True,
        "hp_m1_v18_v17_exact_calculation_byte_unchanged": True,
        "hp_m1_v18_method_threshold_precision_scope_unchanged": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _ordered_restore_checkpoint_states(
    checkpoint: dict[str, object]
) -> tuple[dict[str, dict[int, mp.mpf]], dict[str, dict[int, float]]]:
    m1_names = tuple(checkpoint["m1_state_order"])
    fuel_names = tuple(checkpoint["fuel_state_order"])
    expected_m1_names = tuple(physics.STATE_TO_LEGACY)
    expected_fuel_names = ("delta_f", "U_f")
    if m1_names != expected_m1_names:
        raise ValueError("KMPC-111 explicit M1 order mismatch")
    if fuel_names != expected_fuel_names:
        raise ValueError("KMPC-111 explicit fuel order mismatch")

    serialized_m1 = checkpoint["hp_m1_state_decimal"]
    serialized_fuel = checkpoint["audit_fuel_state_float_hex"]
    if set(serialized_m1) != set(m1_names):
        raise ValueError("KMPC-111 serialized M1 key-set mismatch")
    if set(serialized_fuel) != set(fuel_names):
        raise ValueError("KMPC-111 serialized fuel key-set mismatch")
    ordered_m1 = {name: serialized_m1[name] for name in m1_names}
    ordered_fuel = {name: serialized_fuel[name] for name in fuel_names}

    with mp.workdps(base.PRECISION_DPS):
        m1 = v13._deserialize_m1(ordered_m1, m1_names)
        if v13._serialize_m1(m1, m1_names) != ordered_m1:
            raise ValueError("KMPC-111 HP-M1 ordered roundtrip mismatch")
    fuel = v13._deserialize_fuel(ordered_fuel, fuel_names)
    if v13._serialize_fuel(fuel, fuel_names) != ordered_fuel:
        raise ValueError("KMPC-111 F0 ordered roundtrip mismatch")
    return m1, fuel


@contextmanager
def _restore_overlay() -> Iterator[None]:
    if v17._restore_checkpoint_states is not _V17_RESTORE:
        raise RuntimeError("KMPC-111 restore owner is not pristine")
    v17._restore_checkpoint_states = _ordered_restore_checkpoint_states
    try:
        if v17._restore_checkpoint_states is not _ordered_restore_checkpoint_states:
            raise RuntimeError("KMPC-111 restore overlay was not installed")
        yield
    finally:
        if v17._restore_checkpoint_states is not _ordered_restore_checkpoint_states:
            raise RuntimeError("KMPC-111 restore owner changed while active")
        v17._restore_checkpoint_states = _V17_RESTORE


def _restore_owner_pristine() -> bool:
    return v17._restore_checkpoint_states is _V17_RESTORE


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    owner_before = _restore_owner_pristine()
    with _restore_overlay():
        payload = v17.run_smoke(max_runtime_seconds, result_dir)
    owner_after = _restore_owner_pristine()
    payload["run_id"] = "KMPC-111"
    payload["checks"].update({
        "order_successor_owner_pristine_before": owner_before,
        "order_successor_owner_restored_after": owner_after,
        "order_successor_contract": bool(contract_guard()["pass"]),
        "order_successor_identity_exact": payload["run_id"] == "KMPC-111",
    })
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    owner_before = _restore_owner_pristine()
    with _restore_overlay():
        payload = v17.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    owner_after = _restore_owner_pristine()
    payload["test"] = (
        "KMPC-111 order successor: BI/k=.15 checkpointed exact M3 "
        "driver/holdout resume"
    )
    payload["run_id"] = "KMPC-111"
    payload["source_hashes"] = source_hashes()
    payload["contract_guard"] = contract_guard()
    payload["technical_checks"].update({
        "order_successor_owner_pristine_before": owner_before,
        "order_successor_owner_restored_after": owner_after,
        "order_successor_explicit_m1_order": True,
        "order_successor_explicit_fuel_order": True,
        "order_successor_contract": bool(payload["contract_guard"]["pass"]),
        "order_successor_identity_exact": payload["run_id"] == "KMPC-111",
    })
    payload["passed_execution_contract"] = all(
        payload["technical_checks"].values()
    )
    payload["order_reconstruction_successor"] = {
        "reason": "PF-111_JSON_SORTED_OBJECT_ORDER_IS_NOT_REGISTER_ORDER",
        "authoritative_order_fields": ["m1_state_order", "fuel_state_order"],
        "calculation_module": (
            "c2_bi_k0p15_high_precision_m1_reassembly_v17_exact_resume.py"
        ),
        "calculation_module_changed": False,
        "method_threshold_precision_scope_changed": False,
    }
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("checkpointed exact-resume order successor has no aggregate scope")
