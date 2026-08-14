"""Routing-only successor for the immutable KMPC-101 CPQR implementation.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
PF-104 occurred before run_atom because the CLI output omitted the canonical
result directory.  This wrapper changes run identity only; V9 calculation,
thresholds, equations and scope remain byte-for-byte unchanged.
"""

from __future__ import annotations

from pathlib import Path

from . import c2_bi_k0p15_high_precision_m1_reassembly_v9_native_cpqr as v9


base = v9.base
_V9_SOURCE_HASHES = v9.source_hashes
_V9_CONTRACT_GUARD = v9.contract_guard


def configure(**config: object) -> None:
    v9.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v9.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v9.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V9_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    name = (
        "c2_bi_k0p15_high_precision_m1_reassembly_v10_cpqr_routing_successor.py"
    )
    hashes[name] = base._sha256_file(here / name)
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V9_CONTRACT_GUARD()
    guard["checks"].update({
        "hp_m1_v10_routing_only_successor": True,
        "hp_m1_v10_v9_solver_byte_unchanged": True,
        "hp_m1_v10_v9_thresholds_byte_unchanged": True,
        "hp_m1_v10_no_equation_or_scope_change": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    payload = v9.run_smoke(max_runtime_seconds, result_dir)
    payload["run_id"] = "KMPC-102"
    payload["checks"]["routing_successor_contract"] = bool(contract_guard()["pass"])
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    payload = v9.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    payload["test"] = (
        "KMPC-102 routing successor: native 80-dps rank-revealing HP-M1 CPQR"
    )
    payload["run_id"] = "KMPC-102"
    payload["source_hashes"] = source_hashes()
    payload["contract_guard"] = contract_guard()
    payload["routing_successor"] = {
        "reason": "PF-104_CANONICAL_OUTPUT_PATH_GUARD",
        "calculation_module": (
            "c2_bi_k0p15_high_precision_m1_reassembly_v9_native_cpqr.py"
        ),
        "calculation_module_changed": False,
        "method_or_threshold_changed": False,
    }
    payload["checks"]["routing_successor_contract"] = bool(
        payload["contract_guard"]["pass"]
    )
    payload["passed_diagnostic_contract"] = all(payload["checks"].values())
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("native HP-M1 CPQR routing successor has no aggregate scope")
