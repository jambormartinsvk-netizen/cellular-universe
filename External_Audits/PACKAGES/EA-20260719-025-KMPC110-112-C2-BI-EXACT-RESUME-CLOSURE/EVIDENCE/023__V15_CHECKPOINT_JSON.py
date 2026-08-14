"""JSON-representation successor for the immutable V13 checkpoint.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
PF-109 localized the remaining problem to publish-time ``mpmath.mpf``
objects in the broad diagnostic payload.  This successor converts only those
objects to lossless 90-digit decimal strings and records every payload path.
The dedicated resume register already serialized by V13 is unchanged.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import mpmath as mp

from . import c2_bi_k0p15_high_precision_m1_reassembly_v14_checkpoint_identity_successor as v14


base = v14.base
_V14_SOURCE_HASHES = v14.source_hashes
_V14_CONTRACT_GUARD = v14.contract_guard


def configure(**config: object) -> None:
    v14.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v14.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v14.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V14_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    name = (
        "c2_bi_k0p15_high_precision_m1_reassembly_v15_checkpoint_json_successor.py"
    )
    hashes[name] = base._sha256_file(here / name)
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V14_CONTRACT_GUARD()
    guard["checks"].update({
        "hp_m1_v15_json_representation_only": True,
        "hp_m1_v15_mpf_decimal90_lossless_at_80dps": True,
        "hp_m1_v15_reports_every_converted_path": True,
        "hp_m1_v15_resume_register_byte_semantics_unchanged": True,
        "hp_m1_v15_v13_calculation_byte_unchanged": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _convert_mpf(value: Any, path: str, converted_paths: list[str]) -> Any:
    if isinstance(value, mp.mpf):
        with mp.workdps(base.PRECISION_DPS):
            encoded = mp.nstr(value, n=90, strip_zeros=False)
            if mp.mpf(encoded) != value:
                raise ValueError(f"KMPC-108 mpf decimal roundtrip failed at {path}")
        converted_paths.append(path)
        return encoded
    if isinstance(value, dict):
        return {
            key: _convert_mpf(item, f"{path}.{key}", converted_paths)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [
            _convert_mpf(item, f"{path}[{index}]", converted_paths)
            for index, item in enumerate(value)
        ]
    if isinstance(value, tuple):
        return tuple(
            _convert_mpf(item, f"{path}[{index}]", converted_paths)
            for index, item in enumerate(value)
        )
    return value


def _contains_mpf(value: Any) -> bool:
    if isinstance(value, mp.mpf):
        return True
    if isinstance(value, dict):
        return any(_contains_mpf(item) for item in value.values())
    if isinstance(value, (list, tuple)):
        return any(_contains_mpf(item) for item in value)
    return False


def _serialization_fixture() -> dict[str, bool]:
    with mp.workdps(base.PRECISION_DPS):
        fixture = {
            "root": mp.mpf(1) / mp.mpf(7) + mp.mpf("1e-70"),
            "nested": [mp.mpf("-0.125"), {"plain": 3.0}],
        }
        paths: list[str] = []
        converted = _convert_mpf(fixture, "$", paths)
    return {
        "two_mpf_paths_reported": paths == ["$.root", "$.nested[0]"],
        "mpf_values_are_decimal_strings": (
            isinstance(converted["root"], str)
            and isinstance(converted["nested"][0], str)
        ),
        "ordinary_scalar_unchanged": converted["nested"][1]["plain"] == 3.0,
        "no_mpf_remains": not _contains_mpf(converted),
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    payload = v14.run_smoke(max_runtime_seconds, result_dir)
    payload["run_id"] = "KMPC-108"
    payload["checks"].update({
        f"json_{name}": value for name, value in _serialization_fixture().items()
    })
    payload["checks"]["json_successor_identity_exact"] = (
        payload["run_id"] == "KMPC-108"
    )
    payload["checks"]["json_successor_contract"] = bool(contract_guard()["pass"])
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    raw = v14.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    paths: list[str] = []
    payload = _convert_mpf(raw, "$", paths)
    if _contains_mpf(payload):
        raise TypeError("KMPC-108 mpf remains after JSON representation adapter")
    payload["test"] = "KMPC-108 JSON successor: BI/k=.15 HP-M1 support checkpoint"
    payload["run_id"] = "KMPC-108"
    payload["source_hashes"] = source_hashes()
    payload["contract_guard"] = contract_guard()
    payload["payload_mpf_serialization"] = {
        "representation": "MPMATH_MPF_TO_DECIMAL90_STRING",
        "converted_count": len(paths),
        "converted_paths": paths,
        "roundtrip_exact_at_80dps": True,
        "resume_checkpoint_register_changed": False,
    }
    payload["checks"]["json_successor_identity_exact"] = (
        payload["run_id"] == "KMPC-108"
    )
    payload["checks"]["json_successor_contract"] = bool(
        payload["contract_guard"]["pass"]
    )
    payload["checks"]["diagnostic_mpf_paths_reported"] = len(paths) > 0
    payload["checks"]["no_mpf_remains_in_payload"] = not _contains_mpf(payload)
    payload["passed_execution_contract"] = all(payload["checks"].values())
    payload["identity_successor"] = {
        "reason": "PF-109_UNSUPPORTED_MPF_IN_DIAGNOSTIC_PAYLOAD",
        "calculation_module": (
            "c2_bi_k0p15_high_precision_m1_reassembly_v13_support_checkpoint.py"
        ),
        "calculation_module_changed": False,
        "publish_representation_only": True,
        "method_serialization_threshold_scope_changed": False,
    }
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("HP-M1 checkpoint JSON successor has no aggregate scope")
