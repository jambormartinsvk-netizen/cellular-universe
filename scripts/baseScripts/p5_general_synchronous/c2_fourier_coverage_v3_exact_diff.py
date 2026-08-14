"""KMPC-059 exact-diff successor for the KMPC-058 PF-078 smoke.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
The only contract change is the observed stale S1 set: CDI and BI.
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from . import c2_fourier_coverage_v2_c1_closed_support as v2


RUN_ID = "KMPC-059"
MODES = v2.MODES
K_VALUES = v2.K_VALUES
VARIANT = v2.VARIANT
SUPPORTS = v2.SUPPORTS
C1_PREREQUISITES = v2.C1_PREREQUISITES
legacy = v2.legacy

_V2_RUN_ID = v2.RUN_ID
_V2_CONTRACT_GUARD = v2.contract_guard
_V2_SOURCE_HASHES = v2.source_hashes
_V2_ATOM_OUTPUT_NAME = v2.atom_output_name
_V2_ATOM_FAILURE_NAME = v2.atom_failure_name


def atom_output_name(mode: str, k_mpc: float) -> str:
    if mode not in MODES:
        raise ValueError(mode)
    return f"RUN_KMPC_059_P5_3G7_C2_{mode}_K{legacy.k_token(k_mpc)}_NOMINAL.json"


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return atom_output_name(mode, k_mpc).replace(".json", "_TECHNICAL_FAILURE.json")


def source_hashes() -> dict[str, str]:
    hashes = dict(_V2_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_fourier_coverage_v3_exact_diff.py"] = legacy.sha256_file(
        here / "c2_fourier_coverage_v3_exact_diff.py"
    )
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V2_CONTRACT_GUARD()
    checks = dict(guard["checks"])
    checks.pop("PF077_stale_map_differs_exactly_CDI_BI_NID_NIV")
    stale_modes = tuple(
        mode for mode in MODES
        if v2.HISTORICAL_S1_EXTENDED[mode] != v2.CLOSED_C1_SUPPORTS[mode]
    )
    checks["PF077_stale_map_differs_exactly_CDI_BI"] = stale_modes == ("CDI", "BI")
    return {"derived": guard["derived"], "checks": checks, "pass": all(checks.values())}


@contextmanager
def _v2_overlay() -> Iterator[None]:
    before = (v2.RUN_ID, v2.contract_guard, v2.source_hashes, v2.atom_output_name, v2.atom_failure_name)
    try:
        v2.RUN_ID = RUN_ID
        v2.contract_guard = contract_guard
        v2.source_hashes = source_hashes
        v2.atom_output_name = atom_output_name
        v2.atom_failure_name = atom_failure_name
        yield
    finally:
        v2.RUN_ID, v2.contract_guard, v2.source_hashes, v2.atom_output_name, v2.atom_failure_name = before


def _v2_owners_restored() -> bool:
    return bool(
        v2.RUN_ID == _V2_RUN_ID
        and v2.contract_guard is _V2_CONTRACT_GUARD
        and v2.source_hashes is _V2_SOURCE_HASHES
        and v2.atom_output_name is _V2_ATOM_OUTPUT_NAME
        and v2.atom_failure_name is _V2_ATOM_FAILURE_NAME
    )


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    old_guard = v2._LEGACY_CONTRACT_GUARD()
    old_false = tuple(sorted(name for name, value in old_guard["checks"].items() if not value))
    with _v2_overlay():
        with v2._owner_overlay():
            payload = legacy.run_smoke(max_runtime_seconds, result_dir)
    checks = {
        "PF077_old_false_checks_exact_CDI_BI": old_false == (
            "BI_accepted_matches_closed_C1", "CDI_accepted_matches_closed_C1"
        ),
        "corrected_contract_guard": contract_guard()["pass"],
        "legacy_owners_restored": v2._owners_restored(),
        "v2_owners_restored": _v2_owners_restored(),
        "successor_source_hash_present": "c2_fourier_coverage_v3_exact_diff.py" in source_hashes(),
    }
    payload["technical_successor"] = "PF-077/PF-078 / EXACT_DIFF_GUARD_ONLY"
    payload["observed_old_false_checks"] = list(old_false)
    payload["successor_checks"] = checks
    payload["passed"] = bool(payload["passed"] and all(checks.values()))
    return payload


def run_atom(mode: str, k_mpc: float, max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _v2_overlay():
        with v2._owner_overlay():
            payload = legacy.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not v2._owners_restored() or not _v2_owners_restored():
        raise RuntimeError("KMPC-059 owner overlay was not restored")
    payload["technical_successor"] = "PF-077/PF-078 / EXACT_DIFF_GUARD_ONLY"
    payload["overlay_owners_restored"] = True
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _v2_overlay():
        with v2._owner_overlay():
            payload = legacy.run_aggregate(max_runtime_seconds, result_dir)
    if not v2._owners_restored() or not _v2_owners_restored():
        raise RuntimeError("KMPC-059 owner overlay was not restored")
    payload["technical_successor"] = "PF-077/PF-078 / EXACT_DIFF_GUARD_ONLY"
    payload["overlay_owners_restored"] = True
    return payload
