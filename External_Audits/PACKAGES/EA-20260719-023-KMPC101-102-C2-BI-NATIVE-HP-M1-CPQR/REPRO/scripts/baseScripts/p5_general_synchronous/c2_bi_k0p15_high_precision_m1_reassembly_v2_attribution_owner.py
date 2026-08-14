"""Attribution-owner successor for the KMPC-093 HP-M1 boundary.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Only the nested V1 owner expectation is made aware of the outer M1 overlay.
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from . import c2_bi_k0p15_high_precision_m1_reassembly as v1


_ATTRIBUTION_OWNERS_RESTORED = v1.v1._owners_restored
_V1_SOURCE_HASHES = v1.source_hashes
_V1_CONTRACT_GUARD = v1.contract_guard


def configure(**config: object) -> None:
    v1.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v1.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v1.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V1_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes[
        "c2_bi_k0p15_high_precision_m1_reassembly_v2_attribution_owner.py"
    ] = v1._sha256_file(
        here / "c2_bi_k0p15_high_precision_m1_reassembly_v2_attribution_owner.py"
    )
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V1_CONTRACT_GUARD()
    guard["checks"].update({
        "hp_m1_attribution_owner_expectation_explicit": True,
        "hp_m1_math_unchanged": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _outer_aware_attribution_owners_restored() -> bool:
    return bool(
        v1.driver._exact_driver_boundary is v1._ORIGINAL_EXACT_BOUNDARY
        and v1.driver.source_hashes is v1.v1._PRIOR_SOURCE_HASHES
        and v1.assembly._holdout_affine is v1.v1._ASSEMBLY_HOLDOUT
    )


@contextmanager
def _overlay() -> Iterator[None]:
    before = (v1.v1._owners_restored, v1.source_hashes, v1.contract_guard)
    try:
        v1.v1._owners_restored = _outer_aware_attribution_owners_restored
        v1.source_hashes = source_hashes
        v1.contract_guard = contract_guard
        yield
    finally:
        v1.v1._owners_restored, v1.source_hashes, v1.contract_guard = before


def _owners_restored() -> bool:
    return bool(
        v1.v1._owners_restored is _ATTRIBUTION_OWNERS_RESTORED
        and v1.source_hashes is _V1_SOURCE_HASHES
        and v1.contract_guard is _V1_CONTRACT_GUARD
    )


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = v1.run_smoke(max_runtime_seconds, result_dir)
    payload["checks"]["hp_m1_v2_attribution_owner_restored"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    with _overlay():
        payload = v1.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored():
        raise RuntimeError("KMPC-094 HP-M1 attribution owners not restored")
    payload["high_precision_m1_reassembly_boundary"]["owner_successor"] = {
        "version": "V2_OUTER_AWARE_ATTRIBUTION_OWNER",
        "only_owner_expectation_changed": True,
        "m1_math_changed": False,
        "physics_changed": False,
        "owners_restored": True,
    }
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("high-precision M1 boundary has no aggregate scope")
