"""Phase-aware state-order successor for checkpointed C2 resume.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
Only ordered-register reconstruction is changed; physics is unchanged.
"""

from __future__ import annotations

from contextlib import contextmanager
import json
from pathlib import Path
from typing import Iterator

from . import c2_checkpointed_single_atom as v1


_V1_SOURCE_HASHES = v1.source_hashes
_V1_RESTORE_STATE = v1._restore_state
_V1_LOAD_CHECKPOINT = v1._load_checkpoint


def configure(**config: object) -> None:
    v1.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v1.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v1.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V1_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    hashes["c2_checkpointed_single_atom_v3_phase_order.py"] = v1.legacy.sha256_file(
        here / "c2_checkpointed_single_atom_v3_phase_order.py"
    )
    return hashes


def contract_guard() -> dict[str, object]:
    return v1.contract_guard()


def _restore_state(raw: dict[str, object]) -> dict[str, dict[int, float]]:
    authoritative = tuple(v1.legacy.ra_contract.AUTHORITATIVE_STATE)
    raw_names = set(raw)
    ordered_subset = tuple(name for name in authoritative if name in raw_names)
    if set(ordered_subset) != raw_names or len(ordered_subset) != len(raw):
        raise RuntimeError("checkpoint standard-state subset differs from authoritative contract")
    return {
        name: {int(power): float(value) for power, value in raw[name].items()}
        for name in ordered_subset
    }


def _load_checkpoint(result_dir: Path) -> tuple[dict[str, object], dict[str, object]]:
    current = v1.source_hashes
    v1.source_hashes = _V1_SOURCE_HASHES
    try:
        return _V1_LOAD_CHECKPOINT(result_dir)
    finally:
        v1.source_hashes = current


@contextmanager
def _overlay() -> Iterator[None]:
    before = (v1.source_hashes, v1._restore_state, v1._load_checkpoint)
    try:
        v1.source_hashes = source_hashes
        v1._restore_state = _restore_state
        v1._load_checkpoint = _load_checkpoint
        yield
    finally:
        v1.source_hashes, v1._restore_state, v1._load_checkpoint = before


def _owners_restored() -> bool:
    return bool(
        v1.source_hashes is _V1_SOURCE_HASHES
        and v1._restore_state is _V1_RESTORE_STATE
        and v1._load_checkpoint is _V1_LOAD_CHECKPOINT
    )


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    cfg = v1._cfg()
    with _overlay():
        payload = v1.run_smoke(max_runtime_seconds, result_dir)
        path = result_dir / str(cfg["checkpoint_name"])
        checkpoint = json.loads(path.read_text(encoding="utf-8"))
        standard = _restore_state(checkpoint["standard_state"])
        authoritative = tuple(v1.legacy.ra_contract.AUTHORITATIVE_STATE)
        expected_standard = tuple(name for name in authoritative if name not in {"delta_f", "U_f"})
        combined = tuple(standard) + ("delta_f", "U_f")
        payload["checks"].update({
            "standard_11_state_order": tuple(standard) == expected_standard,
            "combined_13_state_order": combined == authoritative,
            "standard_state_count": len(standard) == 11,
        })
        payload["passed"] = all(payload["checks"].values())
    payload["checks"]["owners_restored"] = _owners_restored()
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str, k_mpc: float, max_runtime_seconds: float, result_dir: Path
) -> dict[str, object]:
    with _overlay():
        payload = v1.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    if not _owners_restored():
        raise RuntimeError("checkpoint phase-order overlay owners were not restored")
    observed = tuple(payload["audit_solve"]["m3"]["diagnostics"]
                     ["production_contract"]["implemented_state"])
    authoritative = tuple(v1.legacy.ra_contract.AUTHORITATIVE_STATE)
    payload["state_order_successor"] = {
        "authoritative_tuple": list(authoritative),
        "observed_tuple": list(observed),
        "pass": observed == authoritative,
        "delta": "PHASE_AWARE_TOP_LEVEL_STATE_INSERTION_ORDER_ONLY",
    }
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("checkpoint phase-order successor has no aggregate scope")
