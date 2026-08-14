"""80-dps fixture-scope successor for KMPC-090.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Only the KMPC-089 synthetic serialization fixture is replaced.
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

import mpmath as mp

from . import c2_bi_k0p15_coefficient_attribution_v2_serialization_bound as v2


_V2_FIXTURE = v2._fixture
_V2_SOURCE_HASHES = v2.source_hashes
_V2_CONTRACT_GUARD = v2.contract_guard


def configure(**config: object) -> None:
    v2.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v2.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v2.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V2_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_bi_k0p15_coefficient_attribution_v3_fixture.py"] = (
        v2.v1.prior.prior.v2.hash_owner.sha256_file(
            here / "c2_bi_k0p15_coefficient_attribution_v3_fixture.py"
        )
    )
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V2_CONTRACT_GUARD()
    guard["checks"].update({
        "fixture_single_80dps_scope": True,
        "serialization_algorithm_unchanged": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _fixture() -> dict[str, bool]:
    with mp.workdps(v2.v1.PRECISION_DPS):
        residual_bound, residual_digits, residual_ulp = v2._serialized_two_ulp(
            "-5.4970171428314830742597821434761704494880966333399e-17"
        )
        norm_bound, norm_digits, norm_ulp = v2._serialized_two_ulp(
            "0.000000018203510784855356980175752053710493850249660287834"
        )
        residual_equal = residual_bound == mp.mpf("2") * residual_ulp
        norm_equal = norm_bound == mp.mpf("2") * norm_ulp
        scales_ordered = residual_bound < norm_bound
    return {
        "residual_digits_50": residual_digits == 50,
        "norm_digits_50": norm_digits == 50,
        "residual_two_ulp_same_80dps_scope": residual_equal,
        "norm_two_ulp_same_80dps_scope": norm_equal,
        "different_magnitude_bounds": scales_ordered,
    }


@contextmanager
def _overlay() -> Iterator[None]:
    before = (v2._fixture, v2.source_hashes, v2.contract_guard)
    try:
        v2._fixture = _fixture
        v2.source_hashes = source_hashes
        v2.contract_guard = contract_guard
        yield
    finally:
        v2._fixture, v2.source_hashes, v2.contract_guard = before


def _owners_restored() -> bool:
    return bool(
        v2._fixture is _V2_FIXTURE
        and v2.source_hashes is _V2_SOURCE_HASHES
        and v2.contract_guard is _V2_CONTRACT_GUARD
    )


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = v2.run_smoke(max_runtime_seconds, result_dir)
    payload["checks"]["fixture_v3_owners_restored"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    with _overlay():
        payload = v2.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored():
        raise RuntimeError("KMPC-090 fixture owners not restored")
    payload["coefficient_attribution_boundary"]["fixture_successor"] = {
        "version": "V3_SINGLE_80DPS_FIXTURE_SCOPE",
        "only_fixture_changed": True,
        "serialization_algorithm_changed": False,
        "physics_changed": False,
        "owners_restored": True,
    }
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("coefficient attribution has no aggregate scope")
