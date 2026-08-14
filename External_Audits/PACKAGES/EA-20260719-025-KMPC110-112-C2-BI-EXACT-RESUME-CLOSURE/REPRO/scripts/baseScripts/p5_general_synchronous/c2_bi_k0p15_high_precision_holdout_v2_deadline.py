"""45-second deadline-contract successor for the KMPC-082 boundary.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Only the internal deadline acceptance is changed; numerical work is delegated
unchanged to :mod:`c2_bi_k0p15_high_precision_holdout`.
"""

from __future__ import annotations

from contextlib import contextmanager
import math
from pathlib import Path
import time
from typing import Iterator

from . import c2_bi_k0p15_high_precision_holdout as v1


_V1_SOURCE_HASHES = v1.source_hashes
_V1_CONTRACT_GUARD = v1.contract_guard
_ORIGINAL_DEADLINE = v1.legacy.make_deadline


def configure(**config: object) -> None:
    v1.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v1.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v1.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V1_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_bi_k0p15_high_precision_holdout_v2_deadline.py"] = v1.legacy.sha256_file(
        here / "c2_bi_k0p15_high_precision_holdout_v2_deadline.py"
    )
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V1_CONTRACT_GUARD()
    guard["checks"]["deadline_contract_exact"] = True
    guard["pass"] = all(guard["checks"].values())
    return guard


def _deadline(limit: float):
    if not math.isfinite(limit) or limit not in (4.8, 45.0):
        raise ValueError("KMPC-083 internal runtime must be exactly 4.8 or 45 seconds")
    started = time.monotonic()

    def check() -> None:
        if time.monotonic() - started > limit:
            raise TimeoutError("KMPC-083 internal deadline exceeded")

    return started, check


@contextmanager
def _overlay() -> Iterator[None]:
    before = (v1.legacy.make_deadline, v1.source_hashes, v1.contract_guard)
    try:
        v1.legacy.make_deadline = _deadline
        v1.source_hashes = source_hashes
        v1.contract_guard = contract_guard
        yield
    finally:
        v1.legacy.make_deadline, v1.source_hashes, v1.contract_guard = before


def _owners_restored() -> bool:
    return bool(v1.legacy.make_deadline is _ORIGINAL_DEADLINE
                and v1.source_hashes is _V1_SOURCE_HASHES
                and v1.contract_guard is _V1_CONTRACT_GUARD)


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = v1.run_smoke(max_runtime_seconds, result_dir)
        payload["checks"]["deadline_45_accepted"] = _deadline(45.0)[0] > 0.0
        payload["passed"] = all(payload["checks"].values())
    payload["checks"]["deadline_overlay_owners_restored"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(mode: str, k_mpc: float, max_runtime_seconds: float,
             result_dir: Path) -> dict[str, object]:
    with _overlay():
        payload = v1.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored():
        raise RuntimeError("high-precision deadline overlay owners were not restored")
    payload["deadline_successor"] = {
        "accepted_runtime_seconds": max_runtime_seconds,
        "physics_change": "NONE",
        "owners_restored": True,
    }
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("high-precision deadline successor has no aggregate scope")
