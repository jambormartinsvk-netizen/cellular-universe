"""Affine-fixture successor for the BI/k=.15 holdout assembly audit.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Only the smoke fixture changes; numerical production work remains in V1.
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

import mpmath as mp

from . import c2_bi_k0p15_high_precision_holdout_assembly_v2_hash_owner as v2


v1 = v2.v1
_V2_SOURCE_HASHES = v2.source_hashes
_V1_FIXTURE = v1._fixture


def configure(**config: object) -> None:
    v2.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v2.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v2.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V2_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_bi_k0p15_high_precision_holdout_assembly_v3_fixture.py"] = (
        v2.hash_owner.sha256_file(
            here / "c2_bi_k0p15_high_precision_holdout_assembly_v3_fixture.py"
        )
    )
    return hashes


def contract_guard() -> dict[str, object]:
    guard = v2.contract_guard()
    guard["checks"]["affine_fixture_owner_exact"] = callable(_fixture)
    guard["pass"] = all(guard["checks"].values())
    return guard


def _fixture() -> dict[str, bool]:
    with mp.workdps(v1.PRECISION_DPS):
        a = v1._mp(0.1)
        b = v1._mp(1.25)
        zero = mp.mpf("0")
        one = mp.mpf("1")
        two = mp.mpf("2")

        def row(x: mp.mpf) -> mp.mpf:
            return a + b * x

        constant = row(zero)
        coefficient = row(one) - constant
        affine_value = constant + coefficient * two
        direct_value = row(two)
        numerator, denominator = 0.1.as_integer_ratio()
        exact_bridge = a == mp.mpf(numerator) / denominator
    return {
        "exact_float_bridge": bool(exact_bridge),
        "affine_reassembly_fixture": bool(affine_value == direct_value),
        "holdout_nonfit_contract": v1.contract.AUTHORITATIVE_HOLDOUT
        == ("Einstein_00", "Einstein_0i"),
    }


@contextmanager
def _overlay() -> Iterator[None]:
    before = (v1._fixture, v2.source_hashes)
    try:
        v1._fixture = _fixture
        v2.source_hashes = source_hashes
        yield
    finally:
        v1._fixture, v2.source_hashes = before


def _owners_restored() -> bool:
    return bool(v1._fixture is _V1_FIXTURE and v2.source_hashes is _V2_SOURCE_HASHES)


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = v2.run_smoke(max_runtime_seconds, result_dir)
        payload["checks"]["assembly_v3_corrected_fixture"] = all(_fixture().values())
        payload["passed"] = all(payload["checks"].values())
    payload["checks"]["assembly_v3_owners_restored"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(mode: str, k_mpc: float, max_runtime_seconds: float,
             result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = v2.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored():
        raise RuntimeError("assembly fixture overlay was not restored")
    payload["affine_fixture_successor"] = {
        "physics_change": "NONE", "corrected_fixture": True,
        "owners_restored": True,
    }
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("assembly fixture successor has no aggregate scope")
