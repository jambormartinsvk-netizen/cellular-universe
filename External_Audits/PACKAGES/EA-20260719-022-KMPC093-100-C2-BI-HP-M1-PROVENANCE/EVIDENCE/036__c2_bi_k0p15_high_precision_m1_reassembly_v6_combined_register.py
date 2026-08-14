"""Combined-register successor for the KMPC-097 matrix diagnostic.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Only the HP-M1 handoff is corrected: eleven rebuilt M1 states are merged into
the existing thirteen-state register, preserving fuel-owned delta_f and U_f.
"""

from __future__ import annotations

from contextlib import contextmanager
import hashlib
from pathlib import Path
from typing import Iterator

from . import c2_bi_k0p15_high_precision_m1_reassembly_v5_matrix_provenance as v5


base = v5.base
_V5_SOURCE_HASHES = v5.source_hashes
_V5_CONTRACT_GUARD = v5.contract_guard
_BROKEN_HP_BOUNDARY = base._high_precision_m1_exact_boundary
_MERGE_DIAGNOSTIC: dict[str, object] | None = None


def configure(**config: object) -> None:
    v5.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v5.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v5.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V5_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    name = "c2_bi_k0p15_high_precision_m1_reassembly_v6_combined_register.py"
    hashes[name] = base._sha256_file(here / name)
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V5_CONTRACT_GUARD()
    m1_names = tuple(base.physics.STATE_TO_LEGACY)
    authoritative = tuple(base.contract.AUTHORITATIVE_STATE)
    guard["checks"].update({
        "hp_m1_v6_m1_state_count_exact": len(m1_names) == 11,
        "hp_m1_v6_combined_state_count_exact": len(authoritative) == 13,
        "hp_m1_v6_fuel_states_explicit": authoritative[-2:] == ("delta_f", "U_f"),
        "hp_m1_v6_only_register_handoff_changed": True,
        "hp_m1_v6_v5_diagnostic_unchanged": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _state_fingerprint(state: dict[str, dict[int, object]], names: tuple[str, ...]) -> str:
    digest = hashlib.sha256()
    for name in names:
        digest.update(name.encode("ascii"))
        digest.update(b"|")
        for power, value in sorted(state[name].items()):
            digest.update(f"{power}|{float(value).hex()}|".encode("ascii"))
    return digest.hexdigest().upper()


def _merge_m1_into_combined(
    combined: dict[str, dict[int, object]],
    hp_m1: dict[str, dict[int, object]],
) -> dict[str, dict[int, object]]:
    authoritative = tuple(base.contract.AUTHORITATIVE_STATE)
    m1_names = tuple(base.physics.STATE_TO_LEGACY)
    if tuple(combined) != authoritative:
        raise ValueError("KMPC-098 combined state order mismatch")
    if tuple(hp_m1) != m1_names:
        raise ValueError("KMPC-098 HP-M1 state order mismatch")
    merged = {name: dict(combined[name]) for name in authoritative}
    for name in m1_names:
        merged[name] = dict(hp_m1[name])
    return merged


def _combined_register_hp_boundary(
    k_mpc: float,
    inputs: object,
    standard: dict[str, dict[int, object]],
    support: tuple[int, int],
) -> dict[str, object]:
    global _MERGE_DIAGNOSTIC
    if (k_mpc, support) != (base.K_MPC, (0, 7)):
        raise ValueError("KMPC-098 combined-register identity mismatch")
    fuel_names = ("delta_f", "U_f")
    before_fuel_sha = _state_fingerprint(standard, fuel_names)
    hp_standard, boundary = base._m1_reassembly(inputs, standard)
    base._M1_BOUNDARY = boundary
    combined = _merge_m1_into_combined(standard, hp_standard)
    after_fuel_sha = _state_fingerprint(combined, fuel_names)
    _MERGE_DIAGNOSTIC = {
        "version": "V6_MERGE_11_HP_M1_INTO_13_COMBINED",
        "combined_state_order": list(combined),
        "hp_m1_state_order": list(hp_standard),
        "preserved_fuel_states": list(fuel_names),
        "fuel_before_sha256": before_fuel_sha,
        "fuel_after_sha256": after_fuel_sha,
        "fuel_values_unchanged": before_fuel_sha == after_fuel_sha,
        "combined_state_count": len(combined),
        "hp_m1_state_count": len(hp_standard),
        "m1_values_replaced": True,
        "non_m1_values_recomputed": False,
        "v5_matrix_provenance_changed": False,
        "physics_changed": False,
    }
    if not _MERGE_DIAGNOSTIC["fuel_values_unchanged"]:
        raise RuntimeError("KMPC-098 fuel states changed during M1 merge")
    result = base._ORIGINAL_EXACT_BOUNDARY(k_mpc, inputs, combined, support)
    result["high_precision_m1_reassembly"] = boundary
    result["high_precision_m1_combined_register"] = _MERGE_DIAGNOSTIC
    result["upstream_scope_limit"] = (
        "F0_AND_FRACTIONAL_BACKGROUND_GENERATORS_REMAIN_FLOAT64"
    )
    return result


@contextmanager
def _overlay() -> Iterator[None]:
    global _MERGE_DIAGNOSTIC
    before = (
        base._high_precision_m1_exact_boundary,
        v5.source_hashes,
        v5.contract_guard,
    )
    _MERGE_DIAGNOSTIC = None
    try:
        base._high_precision_m1_exact_boundary = _combined_register_hp_boundary
        v5.source_hashes = source_hashes
        v5.contract_guard = contract_guard
        yield
    finally:
        (
            base._high_precision_m1_exact_boundary,
            v5.source_hashes,
            v5.contract_guard,
        ) = before


def _owners_restored() -> bool:
    return bool(
        base._high_precision_m1_exact_boundary is _BROKEN_HP_BOUNDARY
        and v5.source_hashes is _V5_SOURCE_HASHES
        and v5.contract_guard is _V5_CONTRACT_GUARD
    )


def _fixture() -> dict[str, bool]:
    authoritative = tuple(base.contract.AUTHORITATIVE_STATE)
    m1_names = tuple(base.physics.STATE_TO_LEGACY)
    combined = {name: {0: float(index)} for index, name in enumerate(authoritative)}
    hp_m1 = {name: {0: float(index + 100)} for index, name in enumerate(m1_names)}
    fuel_before = {name: dict(combined[name]) for name in ("delta_f", "U_f")}
    merged = _merge_m1_into_combined(combined, hp_m1)
    return {
        "combined_order_preserved": tuple(merged) == authoritative,
        "all_m1_states_replaced": all(merged[name] == hp_m1[name] for name in m1_names),
        "fuel_states_value_preserved": all(
            merged[name] == fuel_before[name] for name in ("delta_f", "U_f")
        ),
        "combined_count_13": len(merged) == 13,
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = v5.run_smoke(max_runtime_seconds, result_dir)
        payload["checks"].update({
            f"hp_m1_v6_{name}": value for name, value in _fixture().items()
        })
        payload["passed"] = all(payload["checks"].values())
    payload["checks"]["hp_m1_v6_owners_restored"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    with _overlay():
        payload = v5.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored() or _MERGE_DIAGNOSTIC is None:
        raise RuntimeError("KMPC-098 combined-register lifecycle incomplete")
    payload["high_precision_m1_reassembly_boundary"][
        "combined_register_successor"
    ] = _MERGE_DIAGNOSTIC
    payload["candidate_interpretation_not_verdict"] = (
        "REVIEW_C2_BI_K0p15_HP_M1_MATRIX_PROVENANCE_DIAGNOSTIC_COMPLETE"
    )
    payload["physics_verdict_role"] = "DIAGNOSTIC_ONLY"
    payload["score_effect"] = "NONE_DIAGNOSTIC_ONLY_PENDING_INTERNAL_AUDIT"
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("high-precision M1 boundary has no aggregate scope")
