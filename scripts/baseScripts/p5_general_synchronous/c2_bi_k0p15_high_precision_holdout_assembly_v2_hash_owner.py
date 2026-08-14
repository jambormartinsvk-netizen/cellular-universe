"""Hash-owner successor for the KMPC-084 holdout assembly audit.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Only source-hash ownership is corrected; all numerical work remains in V1.
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from . import c2_bi_k0p15_high_precision_holdout_assembly as v1


hash_owner = v1.hp.legacy
algebra_owner = v1.legacy
_V1_SOURCE_HASHES = v1.source_hashes


def configure(**config: object) -> None:
    v1.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v1.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v1.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(v1._V2_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_bi_k0p15_high_precision_holdout_assembly.py"] = hash_owner.sha256_file(
        here / "c2_bi_k0p15_high_precision_holdout_assembly.py"
    )
    hashes["c2_bi_k0p15_high_precision_holdout_assembly_v2_hash_owner.py"] = (
        hash_owner.sha256_file(
            here / "c2_bi_k0p15_high_precision_holdout_assembly_v2_hash_owner.py"
        )
    )
    return hashes


def contract_guard() -> dict[str, object]:
    guard = v1.contract_guard()
    guard["checks"].update({
        "algebra_owner_exact": hasattr(algebra_owner, "Series")
        and hasattr(algebra_owner, "PairSeries"),
        "hash_owner_exact": callable(getattr(hash_owner, "sha256_file", None)),
        "owners_separated": algebra_owner is not hash_owner,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


@contextmanager
def _overlay() -> Iterator[None]:
    before = v1.source_hashes
    try:
        v1.source_hashes = source_hashes
        yield
    finally:
        v1.source_hashes = before


def _owners_restored() -> bool:
    return v1.source_hashes is _V1_SOURCE_HASHES


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = v1.run_smoke(max_runtime_seconds, result_dir)
        payload["checks"].update({
            "assembly_v2_algebra_owner": hasattr(algebra_owner, "Series"),
            "assembly_v2_hash_owner": callable(getattr(hash_owner, "sha256_file", None)),
            "assembly_v2_owners_separated": algebra_owner is not hash_owner,
        })
        payload["passed"] = all(payload["checks"].values())
    payload["checks"]["assembly_v2_owner_restored"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(mode: str, k_mpc: float, max_runtime_seconds: float,
             result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = v1.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored():
        raise RuntimeError("assembly hash-owner overlay was not restored")
    payload["hash_owner_successor"] = {
        "physics_change": "NONE",
        "algebra_owner": algebra_owner.__name__,
        "hash_owner": hash_owner.__name__,
        "owners_separated": True,
        "owners_restored": True,
    }
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("assembly hash-owner successor has no aggregate scope")
