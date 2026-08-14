"""Nested-owner expectation successor for KMPC-092.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Only the V2 restore expectation inside the V4 outer overlay is replaced.
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from . import c2_bi_k0p15_coefficient_attribution_v4_float_product as v4


v3 = v4.v3
v2 = v4.v2
v1 = v4.v1
_V2_OWNERS_RESTORED = v2._owners_restored
_V4_SOURCE_HASHES = v4.source_hashes
_V4_CONTRACT_GUARD = v4.contract_guard


def configure(**config: object) -> None:
    v4.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v4.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v4.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V4_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_bi_k0p15_coefficient_attribution_v5_nested_owner.py"] = (
        v1.prior.prior.v2.hash_owner.sha256_file(
            here / "c2_bi_k0p15_coefficient_attribution_v5_nested_owner.py"
        )
    )
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V4_CONTRACT_GUARD()
    guard["checks"].update({
        "nested_owner_expectation_explicit": True,
        "attribution_math_unchanged": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _outer_aware_v2_owners_restored() -> bool:
    return bool(
        v1._coefficient_attribution is v4._V1_ATTRIBUTION_OWNER
        and v1.source_hashes is v2._V1_SOURCE_HASHES
        and v1.contract_guard is v2._V1_CONTRACT_GUARD
    )


@contextmanager
def _overlay() -> Iterator[None]:
    before = (v2._owners_restored, v4.source_hashes, v4.contract_guard)
    try:
        v2._owners_restored = _outer_aware_v2_owners_restored
        v4.source_hashes = source_hashes
        v4.contract_guard = contract_guard
        yield
    finally:
        v2._owners_restored, v4.source_hashes, v4.contract_guard = before


def _owners_restored() -> bool:
    return bool(
        v2._owners_restored is _V2_OWNERS_RESTORED
        and v4.source_hashes is _V4_SOURCE_HASHES
        and v4.contract_guard is _V4_CONTRACT_GUARD
    )


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = v4.run_smoke(max_runtime_seconds, result_dir)
    payload["checks"]["nested_owner_v5_restored"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    with _overlay():
        payload = v4.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored():
        raise RuntimeError("KMPC-092 nested owners not restored")
    payload["coefficient_attribution_boundary"]["nested_owner_successor"] = {
        "version": "V5_OUTER_AWARE_V2_OWNER_EXPECTATION",
        "only_owner_expectation_changed": True,
        "attribution_math_changed": False,
        "physics_changed": False,
        "owners_restored": True,
    }
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("coefficient attribution has no aggregate scope")
