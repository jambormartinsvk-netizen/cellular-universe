"""PF-076 owner-only overlay for KMPC-056.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

import numpy as np

from . import nid_c1_coverage as finite_owner
from . import niv_support_step2 as v1


RUN_ID = "KMPC-056"


def source_hashes() -> dict[str, str]:
    here = Path(__file__).resolve().parent
    hashes = dict(v1.source_hashes())
    hashes["niv_support_step2_v2_finite_owner.py"] = v1.sha256_file(
        here / "niv_support_step2_v2_finite_owner.py"
    )
    return hashes


def _owner_guard() -> dict[str, object]:
    callable_owner = callable(finite_owner._all_finite)
    function_name = getattr(finite_owner._all_finite, "__name__", "")
    function_module = getattr(finite_owner._all_finite, "__module__", "")
    v1_missing_before = not hasattr(v1.niv1, "_all_finite")
    fixture = {
        "native": 1.0,
        "numpy": np.float64(2.0),
        "nested": [True, {"finite": 3}],
    }
    fixture_pass = bool(finite_owner._all_finite(fixture))
    negative_nonfinite_rejected = not finite_owner._all_finite({"bad": float("inf")})
    return {
        "callable": callable_owner,
        "name": function_name,
        "module": function_module,
        "v1_target_missing_before_overlay": v1_missing_before,
        "nested_native_numpy_fixture": fixture_pass,
        "nonfinite_fixture_rejected": negative_nonfinite_rejected,
        "pass": bool(
            callable_owner
            and function_name == "_all_finite"
            and function_module.endswith("nid_c1_coverage")
            and v1_missing_before
            and fixture_pass
            and negative_nonfinite_rejected
        ),
    }


@contextmanager
def _temporary_owner_overlay() -> Iterator[dict[str, object]]:
    guard = _owner_guard()
    if not guard["pass"]:
        raise RuntimeError("KMPC-056 exact finite-owner guard failed")
    if hasattr(v1.niv1, "_all_finite"):
        raise RuntimeError("KMPC-056 refuses to overwrite an existing NIV helper")
    setattr(v1.niv1, "_all_finite", finite_owner._all_finite)
    try:
        if v1.niv1._all_finite is not finite_owner._all_finite:
            raise RuntimeError("KMPC-056 finite-owner overlay identity mismatch")
        yield guard
    finally:
        if hasattr(v1.niv1, "_all_finite"):
            delattr(v1.niv1, "_all_finite")


def run_smoke(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    guard = _owner_guard()
    with _temporary_owner_overlay():
        overlay_callable = bool(v1.niv1._all_finite({"numpy": np.float64(1.0)}))
        payload = v1.run_smoke(max_runtime_seconds, result_dir)
    restored = not hasattr(v1.niv1, "_all_finite")
    overlay_checks = {
        "exact_finite_owner_guard": bool(guard["pass"]),
        "overlay_callable_behavior": overlay_callable,
        "owner_namespace_restored": restored,
    }
    payload["run_id"] = RUN_ID
    payload["PF076_owner_overlay_checks"] = overlay_checks
    payload["passed"] = bool(payload["passed"] and all(overlay_checks.values()))
    return payload


def run_audit(max_runtime_seconds: float, result_dir: Path) -> dict[str, object]:
    guard = _owner_guard()
    with _temporary_owner_overlay():
        payload = v1.run_audit(max_runtime_seconds, result_dir)
    restored = not hasattr(v1.niv1, "_all_finite")
    if not restored:
        raise RuntimeError("KMPC-056 finite-owner namespace restoration failed")
    payload["run_id"] = RUN_ID
    payload["execution_status"] = "TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT"
    payload["PF076_owner_overlay"] = {
        "guard": guard,
        "owner_namespace_restored": restored,
        "scope": "OWNER_ONLY_NO_PHYSICS_CHANGE",
    }
    payload["source_hashes"] = source_hashes()
    if not finite_owner._all_finite(payload):
        raise FloatingPointError("non-finite value in final KMPC-056 payload")
    return payload

