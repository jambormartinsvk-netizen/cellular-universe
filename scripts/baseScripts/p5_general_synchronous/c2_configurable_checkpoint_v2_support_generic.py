"""Frozen-ladder successor for NIV C2 checkpoint/resume support.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).

The predecessor was numerically configurable but retained NID-specific
support/candidate labels.  This successor changes only those ownership
guards and labels for the explicitly frozen NIV ladder.
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from . import c2_configurable_checkpoint as base


_BASE_CONTRACT_GUARD = base.contract_guard
_BASE_SOURCE_HASHES = base.source_hashes
_ALLOWED_LADDERS = {
    ("NIV", (-1, 6), (-1, 8), 8),
}


def configure(**config: object) -> None:
    identity = (
        str(config.get("mode")),
        tuple(config.get("accepted", ())),
        tuple(config.get("audit", ())),
        int(config.get("m1_depth", -1)),
    )
    if identity not in _ALLOWED_LADDERS:
        raise ValueError("support-generic successor received an unfrozen ladder")
    base.configure(**config)


def source_hashes() -> dict[str, str]:
    hashes = dict(_BASE_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    name = "c2_configurable_checkpoint_v2_support_generic.py"
    hashes[name] = base.v1.legacy.sha256_file(here / name)
    return hashes


def contract_guard() -> dict[str, object]:
    payload = _BASE_CONTRACT_GUARD()
    cfg = base._cfg()
    identity = (
        str(cfg["mode"]), tuple(cfg["accepted"]), tuple(cfg["audit"]),
        int(cfg["m1_depth"]),
    )
    checks = dict(payload["checks"])
    checks["support_exact"] = identity in _ALLOWED_LADDERS
    checks["successor_scope_exact"] = identity == (
        "NIV", (-1, 6), (-1, 8), 8,
    )
    payload["checks"] = checks
    payload["pass"] = all(checks.values())
    payload["successor_scope"] = {
        "mode": "NIV", "accepted": [-1, 6], "audit": [-1, 8],
        "m1_depth": 8,
    }
    return payload


@contextmanager
def _public_owner_overlay() -> Iterator[None]:
    before = (base.contract_guard, base.source_hashes)
    try:
        base.contract_guard = contract_guard
        base.source_hashes = source_hashes
        yield
    finally:
        base.contract_guard, base.source_hashes = before


def _public_owners_restored() -> bool:
    return bool(
        base.contract_guard is _BASE_CONTRACT_GUARD
        and base.source_hashes is _BASE_SOURCE_HASHES
    )


def atom_output_name(mode: str, k_mpc: float) -> str:
    return base.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return base.atom_failure_name(mode, k_mpc)


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    with _public_owner_overlay():
        payload = base.run_smoke(max_runtime_seconds, result_dir)
    payload["checks"]["successor_public_owners_restored"] = (
        _public_owners_restored()
    )
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str, k_mpc: float, max_runtime_seconds: float, result_dir: Path,
) -> dict[str, object]:
    with _public_owner_overlay():
        payload = base.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _public_owners_restored():
        raise RuntimeError("support-generic public owners were not restored")
    cfg = base._cfg()
    accepted_end = int(tuple(cfg["accepted"])[1])
    audit_end = int(tuple(cfg["audit"])[1])
    phase = str(cfg["phase"])
    payload["atom_id"] = (
        f"{cfg['mode']}/k={cfg['k_mpc']}/support_{accepted_end:02d}_"
        f"{audit_end:02d}/{phase}"
    )
    if phase == "resume":
        token = base.v1.legacy.k_token(float(cfg["k_mpc"]))
        if payload["core_pass"] and payload["common_pass"] and payload["tail_pass"]:
            candidate = (
                f"PASS_C2_{cfg['mode']}_K{token}_SUPPORT_"
                f"{accepted_end:02d}_ADEQUATE_CANDIDATE_ONLY"
            )
        elif payload["core_pass"] and payload["common_pass"]:
            candidate = (
                f"REVIEW_C2_{cfg['mode']}_K{token}_SUPPORT_"
                f"{audit_end:02d}_{audit_end + 2:02d}_REQUIRED"
            )
        else:
            candidate = payload["candidate_interpretation_not_verdict"]
        payload["candidate_interpretation_not_verdict"] = candidate
    payload["support_generic_successor"] = {
        "base_immutable": True,
        "frozen_ladder": contract_guard()["successor_scope"],
        "public_owners_restored": True,
    }
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("support-generic checkpoint has no aggregate scope")
