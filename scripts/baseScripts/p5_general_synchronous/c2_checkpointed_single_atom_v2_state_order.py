"""State-order-only successor for the checkpointed C2 resume path.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
No equations, values, supports, or thresholds are changed.
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
    hashes["c2_checkpointed_single_atom_v2_state_order.py"] = v1.legacy.sha256_file(
        here / "c2_checkpointed_single_atom_v2_state_order.py"
    )
    return hashes


def contract_guard() -> dict[str, object]:
    return v1.contract_guard()


def _restore_state(raw: dict[str, object]) -> dict[str, dict[int, float]]:
    authoritative = tuple(v1.legacy.ra_contract.AUTHORITATIVE_STATE)
    if set(raw) != set(authoritative) or len(raw) != len(authoritative):
        raise RuntimeError("checkpoint state names differ from authoritative contract")
    return {
        name: {int(power): float(value) for power, value in raw[name].items()}
        for name in authoritative
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
        restored = _restore_state(checkpoint["standard_state"])
        payload["checks"]["authoritative_standard_state_order"] = (
            tuple(restored) == tuple(v1.legacy.ra_contract.AUTHORITATIVE_STATE)
        )
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
        raise RuntimeError("checkpoint state-order overlay owners were not restored")
    payload["state_order_successor"] = {
        "authoritative_tuple": list(v1.legacy.ra_contract.AUTHORITATIVE_STATE),
        "observed_tuple": list(payload["audit_solve"]["m3"]["diagnostics"]
                               ["production_contract"]["implemented_state"]),
        "pass": tuple(payload["audit_solve"]["m3"]["diagnostics"]
                      ["production_contract"]["implemented_state"])
                == tuple(v1.legacy.ra_contract.AUTHORITATIVE_STATE),
        "delta": "TOP_LEVEL_STATE_INSERTION_ORDER_ONLY",
    }
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("checkpoint state-order successor has no aggregate scope")
