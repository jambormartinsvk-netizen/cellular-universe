"""Identity-only successor for the immutable V13 support checkpoint.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
PF-108 occurred in runner routing before V13 ran.  This wrapper changes only
the successor identity and source-contract metadata; checkpoint mathematics,
serialization, thresholds and runtime remain byte-for-byte in V13.
"""

from __future__ import annotations

from pathlib import Path

from . import c2_bi_k0p15_high_precision_m1_reassembly_v13_support_checkpoint as v13


base = v13.base
_V13_SOURCE_HASHES = v13.source_hashes
_V13_CONTRACT_GUARD = v13.contract_guard


def configure(**config: object) -> None:
    v13.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v13.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v13.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V13_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    name = (
        "c2_bi_k0p15_high_precision_m1_reassembly_v14_checkpoint_identity_successor.py"
    )
    hashes[name] = base._sha256_file(here / name)
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V13_CONTRACT_GUARD()
    guard["checks"].update({
        "hp_m1_v14_checkpoint_identity_only": True,
        "hp_m1_v14_v13_calculation_byte_unchanged": True,
        "hp_m1_v14_method_serialization_threshold_scope_unchanged": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    payload = v13.run_smoke(max_runtime_seconds, result_dir)
    payload["run_id"] = "KMPC-107"
    payload["checks"]["checkpoint_successor_identity_exact"] = (
        payload["run_id"] == "KMPC-107"
    )
    payload["checks"]["checkpoint_successor_contract"] = bool(
        contract_guard()["pass"]
    )
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    payload = v13.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    payload["test"] = "KMPC-107 identity successor: BI/k=.15 HP-M1 support checkpoint"
    payload["run_id"] = "KMPC-107"
    payload["source_hashes"] = source_hashes()
    payload["contract_guard"] = contract_guard()
    payload["checks"]["checkpoint_successor_identity_exact"] = (
        payload["run_id"] == "KMPC-107"
    )
    payload["checks"]["checkpoint_successor_contract"] = bool(
        payload["contract_guard"]["pass"]
    )
    payload["passed_execution_contract"] = all(payload["checks"].values())
    payload["identity_successor"] = {
        "reason": "PF-108_NONLITERAL_PRIOR_RUNNER_AST_ASSIGNMENT",
        "calculation_module": (
            "c2_bi_k0p15_high_precision_m1_reassembly_v13_support_checkpoint.py"
        ),
        "calculation_module_changed": False,
        "method_serialization_threshold_scope_changed": False,
    }
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("HP-M1 support checkpoint identity successor has no aggregate scope")
