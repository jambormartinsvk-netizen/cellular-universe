"""KMPC-061 guard-semantics successor after the KMPC-060 diagnostic.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from . import c2_fourier_coverage_v3_exact_diff as v3


RUN_ID = "KMPC-061"
MODES = v3.MODES
K_VALUES = v3.K_VALUES
VARIANT = v3.VARIANT
SUPPORTS = v3.SUPPORTS
C1_PREREQUISITES = v3.C1_PREREQUISITES
v2 = v3.v2
legacy = v3.legacy

_V3_RUN_ID = v3.RUN_ID
_V3_CONTRACT_GUARD = v3.contract_guard
_V3_SOURCE_HASHES = v3.source_hashes
_V3_ATOM_OUTPUT_NAME = v3.atom_output_name
_V3_ATOM_FAILURE_NAME = v3.atom_failure_name


def atom_output_name(mode: str, k_mpc: float) -> str:
    if mode not in MODES:
        raise ValueError(mode)
    return f"RUN_KMPC_061_P5_3G7_C2_{mode}_K{legacy.k_token(k_mpc)}_NOMINAL.json"


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return atom_output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def source_hashes() -> dict[str, str]:
    hashes = dict(_V3_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_fourier_coverage_v4_guard_semantics.py"] = legacy.sha256_file(
        here / "c2_fourier_coverage_v4_guard_semantics.py"
    )
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V3_CONTRACT_GUARD()
    checks = dict(guard["checks"])
    checks.pop("PF077_stale_map_differs_exactly_CDI_BI")
    stale_modes = tuple(
        mode for mode in MODES
        if v2.HISTORICAL_S1_EXTENDED[mode] != v2.CLOSED_C1_SUPPORTS[mode]
    )
    checks["historical_S1_extended_differs_exactly_AD_CDI_BI"] = stale_modes == ("AD", "CDI", "BI")
    return {"derived": guard["derived"], "checks": checks, "pass": all(checks.values())}


@contextmanager
def _v3_overlay() -> Iterator[None]:
    before = (v3.RUN_ID, v3.contract_guard, v3.source_hashes, v3.atom_output_name, v3.atom_failure_name)
    try:
        v3.RUN_ID = RUN_ID
        v3.contract_guard = contract_guard
        v3.source_hashes = source_hashes
        v3.atom_output_name = atom_output_name
        v3.atom_failure_name = atom_failure_name
        yield
    finally:
        v3.RUN_ID, v3.contract_guard, v3.source_hashes, v3.atom_output_name, v3.atom_failure_name = before


def _owners_restored() -> bool:
    return bool(
        v3.RUN_ID == _V3_RUN_ID
        and v3.contract_guard is _V3_CONTRACT_GUARD
        and v3.source_hashes is _V3_SOURCE_HASHES
        and v3.atom_output_name is _V3_ATOM_OUTPUT_NAME
        and v3.atom_failure_name is _V3_ATOM_FAILURE_NAME
    )


@contextmanager
def _full_overlay() -> Iterator[None]:
    with _v3_overlay():
        with v3._v2_overlay():
            with v2._owner_overlay():
                yield


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    old_guard = v2._LEGACY_CONTRACT_GUARD()
    old_false = tuple(sorted(name for name, value in old_guard["checks"].items() if not value))
    historical_diff = tuple(
        mode for mode in MODES
        if v2.HISTORICAL_S1_EXTENDED[mode] != v2.CLOSED_C1_SUPPORTS[mode]
    )
    with _full_overlay():
        payload = legacy.run_smoke(max_runtime_seconds, result_dir)
    checks = {
        "V1_false_checks_exact_BI_CDI": old_false == (
            "BI_accepted_matches_closed_C1", "CDI_accepted_matches_closed_C1"
        ),
        "historical_diff_exact_AD_CDI_BI": historical_diff == ("AD", "CDI", "BI"),
        "corrected_contract_guard": contract_guard()["pass"],
        "legacy_owners_restored": v2._owners_restored(),
        "v2_owners_restored": v3._v2_owners_restored(),
        "v3_owners_restored": _owners_restored(),
        "successor_source_hash_present": "c2_fourier_coverage_v4_guard_semantics.py" in source_hashes(),
    }
    payload["technical_successor"] = "PF-077/PF-078/PF-079 / GUARD_SEMANTICS_ONLY"
    payload["V1_false_checks"] = list(old_false)
    payload["historical_S1_vs_closed_diff"] = list(historical_diff)
    payload["successor_checks"] = checks
    payload["passed"] = bool(payload["passed"] and all(checks.values()))
    return payload


def run_atom(mode: str, k_mpc: float, max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _full_overlay():
        payload = legacy.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not v2._owners_restored() or not v3._v2_owners_restored() or not _owners_restored():
        raise RuntimeError("KMPC-061 owner overlay was not restored")
    payload["technical_successor"] = "PF-077/PF-078/PF-079 / GUARD_SEMANTICS_ONLY"
    payload["overlay_owners_restored"] = True
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _full_overlay():
        payload = legacy.run_aggregate(max_runtime_seconds, result_dir)
    if not v2._owners_restored() or not v3._v2_owners_restored() or not _owners_restored():
        raise RuntimeError("KMPC-061 owner overlay was not restored")
    payload["technical_successor"] = "PF-077/PF-078/PF-079 / GUARD_SEMANTICS_ONLY"
    payload["overlay_owners_restored"] = True
    return payload
