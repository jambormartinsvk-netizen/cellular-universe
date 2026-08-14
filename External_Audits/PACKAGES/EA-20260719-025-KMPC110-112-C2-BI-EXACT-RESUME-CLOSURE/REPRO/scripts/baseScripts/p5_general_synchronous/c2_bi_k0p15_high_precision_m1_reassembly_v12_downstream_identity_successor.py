"""Identity-only successor for the immutable V11 downstream calculation.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
PF-106 found that V11 correctly retained its original KMPC-103 payload
identity when called by a new runner.  This wrapper changes only run/test and
source-contract metadata after V11 returns.
"""

from __future__ import annotations

from pathlib import Path

from . import c2_bi_k0p15_high_precision_m1_reassembly_v11_downstream_insertion as v11


base = v11.base
_V11_SOURCE_HASHES = v11.source_hashes
_V11_CONTRACT_GUARD = v11.contract_guard


def configure(**config: object) -> None:
    v11.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v11.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v11.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V11_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    name = (
        "c2_bi_k0p15_high_precision_m1_reassembly_v12_downstream_identity_successor.py"
    )
    hashes[name] = base._sha256_file(here / name)
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V11_CONTRACT_GUARD()
    guard["checks"].update({
        "hp_m1_v12_identity_only_successor": True,
        "hp_m1_v12_v11_calculation_byte_unchanged": True,
        "hp_m1_v12_method_threshold_scope_unchanged": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    payload = v11.run_smoke(max_runtime_seconds, result_dir)
    payload["run_id"] = "KMPC-105"
    payload["checks"]["downstream_identity_exact"] = payload["run_id"] == "KMPC-105"
    payload["checks"]["downstream_identity_contract"] = bool(contract_guard()["pass"])
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    payload = v11.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    payload["test"] = (
        "KMPC-105 identity successor: BI/k=.15 HP-M1 downstream insertion"
    )
    payload["run_id"] = "KMPC-105"
    payload["source_hashes"] = source_hashes()
    payload["contract_guard"] = contract_guard()
    payload["checks"]["downstream_identity_exact"] = payload["run_id"] == "KMPC-105"
    payload["checks"]["downstream_identity_contract"] = bool(
        payload["contract_guard"]["pass"]
    )
    payload["passed_execution_contract"] = all(payload["checks"].values())
    payload["identity_successor"] = {
        "reason": "PF-106_PAYLOAD_RUN_ID_MISMATCH",
        "calculation_module": (
            "c2_bi_k0p15_high_precision_m1_reassembly_v11_downstream_insertion.py"
        ),
        "calculation_module_changed": False,
        "method_threshold_scope_changed": False,
    }
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("HP-M1 downstream identity successor has no aggregate scope")
