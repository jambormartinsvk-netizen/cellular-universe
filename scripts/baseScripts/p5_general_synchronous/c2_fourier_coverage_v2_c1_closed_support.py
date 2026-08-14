"""KMPC-058 technical successor for the KMPC-057 PF-077 support guard.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Only the closed-C1 support parity guard and successor identity are overlaid.
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from . import c2_fourier_coverage as legacy


RUN_ID = "KMPC-058"
MODES = legacy.MODES
K_VALUES = legacy.K_VALUES
VARIANT = legacy.VARIANT
SUPPORTS = legacy.SUPPORTS
C1_PREREQUISITES = legacy.C1_PREREQUISITES
CLOSED_C1_SUPPORTS = {
    "AD": (0, 2),
    "CDI": (0, 5),
    "BI": (0, 5),
    "NID": (0, 5),
    "NIV": (-1, 4),
}
HISTORICAL_S1_EXTENDED = {
    mode: tuple(legacy.collective_contract.MODE_SPEC[mode]["extended"])
    for mode in MODES
}

_LEGACY_RUN_ID = legacy.RUN_ID
_LEGACY_CONTRACT_GUARD = legacy.contract_guard
_LEGACY_SOURCE_HASHES = legacy.source_hashes
_LEGACY_ATOM_OUTPUT_NAME = legacy.atom_output_name
_LEGACY_ATOM_FAILURE_NAME = legacy.atom_failure_name


def atom_output_name(mode: str, k_mpc: float) -> str:
    if mode not in MODES:
        raise ValueError(mode)
    return f"RUN_KMPC_058_P5_3G7_C2_{mode}_K{legacy.k_token(k_mpc)}_NOMINAL.json"


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return atom_output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def source_hashes() -> dict[str, str]:
    hashes = dict(_LEGACY_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_fourier_coverage_v2_c1_closed_support.py"] = legacy.sha256_file(
        here / "c2_fourier_coverage_v2_c1_closed_support.py"
    )
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _LEGACY_CONTRACT_GUARD()
    checks = dict(guard["checks"])
    derived = dict(guard["derived"])
    for mode in MODES:
        checks.pop(f"{mode}_accepted_matches_closed_C1")
        accepted = tuple(SUPPORTS[mode]["accepted"])
        audit = tuple(SUPPORTS[mode]["audit"])
        checks[f"{mode}_accepted_matches_hashed_closed_C1"] = accepted == CLOSED_C1_SUPPORTS[mode]
        checks[f"{mode}_audit_is_closed_C1_plus2"] = audit == (accepted[0], accepted[1] + 2)
        derived[mode] = {
            **derived[mode],
            "closed_C1_support": list(CLOSED_C1_SUPPORTS[mode]),
            "historical_S1_extended_support": list(HISTORICAL_S1_EXTENDED[mode]),
            "closed_C1_prerequisite_file": C1_PREREQUISITES[mode][0],
            "closed_C1_prerequisite_sha256": C1_PREREQUISITES[mode][1],
        }
    stale_modes = tuple(
        mode for mode in MODES if HISTORICAL_S1_EXTENDED[mode] != CLOSED_C1_SUPPORTS[mode]
    )
    checks["PF077_stale_map_differs_exactly_CDI_BI_NID_NIV"] = stale_modes == ("CDI", "BI", "NID", "NIV")
    checks["closed_support_map_exact"] = tuple(CLOSED_C1_SUPPORTS) == MODES
    return {"derived": derived, "checks": checks, "pass": all(checks.values())}


@contextmanager
def _owner_overlay() -> Iterator[None]:
    before = (
        legacy.RUN_ID,
        legacy.contract_guard,
        legacy.source_hashes,
        legacy.atom_output_name,
        legacy.atom_failure_name,
    )
    try:
        legacy.RUN_ID = RUN_ID
        legacy.contract_guard = contract_guard
        legacy.source_hashes = source_hashes
        legacy.atom_output_name = atom_output_name
        legacy.atom_failure_name = atom_failure_name
        yield
    finally:
        (
            legacy.RUN_ID,
            legacy.contract_guard,
            legacy.source_hashes,
            legacy.atom_output_name,
            legacy.atom_failure_name,
        ) = before


def _owners_restored() -> bool:
    return bool(
        legacy.RUN_ID == _LEGACY_RUN_ID
        and legacy.contract_guard is _LEGACY_CONTRACT_GUARD
        and legacy.source_hashes is _LEGACY_SOURCE_HASHES
        and legacy.atom_output_name is _LEGACY_ATOM_OUTPUT_NAME
        and legacy.atom_failure_name is _LEGACY_ATOM_FAILURE_NAME
    )


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    old_guard = _LEGACY_CONTRACT_GUARD()
    old_false = tuple(sorted(name for name, value in old_guard["checks"].items() if not value))
    with _owner_overlay():
        payload = legacy.run_smoke(max_runtime_seconds, result_dir)
    successor_checks = {
        "PF077_old_false_checks_exact": old_false == (
            "BI_accepted_matches_closed_C1",
            "CDI_accepted_matches_closed_C1",
            "NID_accepted_matches_closed_C1",
            "NIV_accepted_matches_closed_C1",
        ),
        "corrected_contract_guard": contract_guard()["pass"],
        "overlay_owners_restored": _owners_restored(),
        "successor_source_hash_present": "c2_fourier_coverage_v2_c1_closed_support.py" in source_hashes(),
    }
    payload["technical_successor"] = "PF-077 / SUPPORT_GUARD_ONLY"
    payload["PF077_old_false_checks"] = list(old_false)
    payload["successor_checks"] = successor_checks
    payload["passed"] = bool(payload["passed"] and all(successor_checks.values()))
    return payload


def run_atom(mode: str, k_mpc: float, max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _owner_overlay():
        payload = legacy.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored():
        raise RuntimeError("KMPC-058 owner overlay was not restored")
    payload["technical_successor"] = "PF-077 / SUPPORT_GUARD_ONLY"
    payload["overlay_owners_restored"] = True
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _owner_overlay():
        payload = legacy.run_aggregate(max_runtime_seconds, result_dir)
    if not _owners_restored():
        raise RuntimeError("KMPC-058 owner overlay was not restored")
    payload["technical_successor"] = "PF-077 / SUPPORT_GUARD_ONLY"
    payload["overlay_owners_restored"] = True
    return payload
