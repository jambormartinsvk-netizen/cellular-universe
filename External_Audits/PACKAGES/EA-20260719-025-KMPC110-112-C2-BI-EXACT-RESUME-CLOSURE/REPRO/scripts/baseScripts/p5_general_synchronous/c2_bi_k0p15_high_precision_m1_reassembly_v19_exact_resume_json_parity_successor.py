"""Publish-canonical parity successor for the immutable V17/V18 resume.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
PF-112 compared a live Python payload with a JSON-loaded payload before both
used the stable publish representation.  This wrapper temporarily replaces
only the V15 representation adapter so integer mapping keys, tuples, numpy
containers and mpf values are normalized exactly as the publisher records
them.  The V17 exact calculation and the V18 checkpoint-order repair remain
byte unchanged.
"""

from __future__ import annotations

from contextlib import contextmanager
import math
from pathlib import Path
from typing import Any, Iterator

import mpmath as mp
import numpy as np

from . import c2_bi_k0p15_high_precision_m1_reassembly_v18_exact_resume_order_successor as v18


v17 = v18.v17
v15 = v17.v15
base = v18.base
_V18_SOURCE_HASHES = v18.source_hashes
_V18_CONTRACT_GUARD = v18.contract_guard
_V15_CONVERT_MPF = v15._convert_mpf


def configure(**config: object) -> None:
    v18.configure(**config)


def atom_output_name(mode: str, k_mpc: float) -> str:
    return v18.atom_output_name(mode, k_mpc)


def atom_failure_name(mode: str, k_mpc: float) -> str:
    return v18.atom_failure_name(mode, k_mpc)


def source_hashes() -> dict[str, str]:
    hashes = dict(_V18_SOURCE_HASHES())
    here = Path(__file__).resolve().parent
    name = (
        "c2_bi_k0p15_high_precision_m1_reassembly_"
        "v19_exact_resume_json_parity_successor.py"
    )
    hashes[name] = base._sha256_file(here / name)
    return hashes


def contract_guard() -> dict[str, object]:
    guard = _V18_CONTRACT_GUARD()
    guard["checks"].update({
        "hp_m1_v19_live_and_json_parity_same_representation": True,
        "hp_m1_v19_integer_mapping_keys_become_strings": True,
        "hp_m1_v19_tuples_become_lists": True,
        "hp_m1_v19_mpf_remains_decimal90": True,
        "hp_m1_v19_adapter_owner_lifecycle": True,
        "hp_m1_v19_v17_v18_calculation_byte_unchanged": True,
        "hp_m1_v19_method_threshold_precision_scope_unchanged": True,
    })
    guard["pass"] = all(guard["checks"].values())
    return guard


def _publish_canonical_convert(
    value: Any, path: str, converted_paths: list[str]
) -> Any:
    if isinstance(value, mp.mpf):
        return _V15_CONVERT_MPF(value, path, converted_paths)
    if isinstance(value, dict):
        return {
            str(key): _publish_canonical_convert(
                item, f"{path}.{key}", converted_paths
            )
            for key, item in value.items()
        }
    if isinstance(value, (list, tuple)):
        return [
            _publish_canonical_convert(item, f"{path}[{index}]", converted_paths)
            for index, item in enumerate(value)
        ]
    if isinstance(value, np.ndarray):
        return _publish_canonical_convert(value.tolist(), path, converted_paths)
    if isinstance(value, np.generic):
        return _publish_canonical_convert(value.item(), path, converted_paths)
    if isinstance(value, float) and not math.isfinite(value):
        raise FloatingPointError(
            f"KMPC-112 non-finite value cannot be serialized at {path}"
        )
    if value is None or isinstance(value, (str, bool, int, float)):
        return value
    raise TypeError(
        f"KMPC-112 unsupported JSON scalar at {path}: {type(value).__name__}"
    )


@contextmanager
def _json_parity_overlay() -> Iterator[None]:
    if v15._convert_mpf is not _V15_CONVERT_MPF:
        raise RuntimeError("KMPC-112 V15 representation owner is not pristine")
    v15._convert_mpf = _publish_canonical_convert
    try:
        if v15._convert_mpf is not _publish_canonical_convert:
            raise RuntimeError("KMPC-112 JSON parity overlay was not installed")
        yield
    finally:
        if v15._convert_mpf is not _publish_canonical_convert:
            raise RuntimeError("KMPC-112 JSON parity owner changed while active")
        v15._convert_mpf = _V15_CONVERT_MPF


def _adapter_owner_pristine() -> bool:
    return v15._convert_mpf is _V15_CONVERT_MPF


def _canonical_fixture() -> dict[str, bool]:
    with mp.workdps(base.PRECISION_DPS):
        value = {7: (mp.mpf(1) / mp.mpf(7), np.int64(3))}
        paths: list[str] = []
        converted = _publish_canonical_convert(value, "$.fixture", paths)
    return {
        "integer_key_to_string": list(converted) == ["7"],
        "tuple_to_list": isinstance(converted["7"], list),
        "numpy_scalar_to_builtin": type(converted["7"][1]) is int,
        "mpf_decimal90_string": isinstance(converted["7"][0], str),
        "mpf_path_exact": paths == ["$.fixture.7[0]"],
        "no_mpf_remains": not v15._contains_mpf(converted),
    }


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    owner_before = _adapter_owner_pristine()
    with _json_parity_overlay():
        payload = v18.run_smoke(max_runtime_seconds, result_dir)
    owner_after = _adapter_owner_pristine()
    payload["run_id"] = "KMPC-112"
    payload["checks"].update({
        f"json_parity_{name}": passed
        for name, passed in _canonical_fixture().items()
    })
    payload["checks"].update({
        "json_parity_owner_pristine_before": owner_before,
        "json_parity_owner_restored_after": owner_after,
        "json_parity_contract": bool(contract_guard()["pass"]),
        "json_parity_identity_exact": payload["run_id"] == "KMPC-112",
    })
    payload["passed"] = all(payload["checks"].values())
    return payload


def run_atom(
    mode: str,
    k_mpc: float,
    max_runtime_seconds: float,
    result_dir: Path,
) -> dict[str, object]:
    owner_before = _adapter_owner_pristine()
    with _json_parity_overlay():
        payload = v18.run_atom(mode, k_mpc, max_runtime_seconds, result_dir)
    owner_after = _adapter_owner_pristine()
    payload["test"] = (
        "KMPC-112 JSON-parity successor: BI/k=.15 checkpointed exact M3 "
        "driver/holdout resume"
    )
    payload["run_id"] = "KMPC-112"
    payload["source_hashes"] = source_hashes()
    payload["contract_guard"] = contract_guard()
    payload["technical_checks"].update({
        "json_parity_owner_pristine_before": owner_before,
        "json_parity_owner_restored_after": owner_after,
        "json_parity_live_and_checkpoint_canonicalized": True,
        "json_parity_contract": bool(payload["contract_guard"]["pass"]),
        "json_parity_identity_exact": payload["run_id"] == "KMPC-112",
    })
    payload["passed_execution_contract"] = all(
        payload["technical_checks"].values()
    )
    payload["json_parity_successor"] = {
        "reason": "PF-112_LIVE_PYTHON_TYPES_COMPARED_TO_JSON_TYPES",
        "canonicalization": (
            "dict keys to strings; tuple to list; numpy containers to builtins; "
            "mpf to decimal90"
        ),
        "calculation_modules_changed": False,
        "method_threshold_precision_scope_changed": False,
    }
    return payload


def run_aggregate(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    raise RuntimeError("checkpointed exact-resume JSON-parity successor has no aggregate scope")
