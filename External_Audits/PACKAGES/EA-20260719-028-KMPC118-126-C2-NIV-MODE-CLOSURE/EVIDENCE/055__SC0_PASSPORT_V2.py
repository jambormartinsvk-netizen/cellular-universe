"""PF-069-only overlay for the KMPC-033 S-C0 passport rerun.

No equation, support, threshold, weight or source state is changed.  The
overlay only normalizes finite numbers.Real values to builtin float before
constructing a SymPy Rational, and restores the V1 helper in a finally block.
"""

from __future__ import annotations

import math
from numbers import Real
from pathlib import Path
from typing import Callable

import numpy as np
import sympy as sp

from . import s_c0_coefficient_passport as v1


RUN_ID = "KMPC-033"
OUTPUT_NAME = "RUN_KMPC_033_P5_3G7_S_C0_COEFFICIENT_PASSPORT_RERUN1.json"
FAILURE_NAME = (
    "RUN_KMPC_033_P5_3G7_S_C0_COEFFICIENT_PASSPORT_RERUN1_TECHNICAL_FAILURE.json"
)


def corrected_q(value: object) -> sp.Rational:
    if isinstance(value, sp.Rational):
        return value
    if isinstance(value, int):
        return sp.Rational(value)
    if isinstance(value, Real):
        converted = float(value)
        if not math.isfinite(converted):
            raise ValueError("non-finite M1 coefficient")
        return sp.Rational(repr(converted))
    return sp.Rational(str(value))


def _with_corrected_q(function: Callable[[float], dict[str, object]], max_runtime_seconds: float) -> dict[str, object]:
    original = v1._q
    if original is corrected_q:
        raise RuntimeError("PF-069 overlay unexpectedly active before entry")
    v1._q = corrected_q
    try:
        payload = function(max_runtime_seconds)
    finally:
        v1._q = original
    if v1._q is not original:
        raise RuntimeError("PF-069 helper was not restored")
    return payload


def source_hashes() -> dict[str, str]:
    hashes = dict(v1.source_hashes())
    path = Path(__file__).resolve()
    hashes[path.name] = v1.sha256_file(path)
    return hashes


def run_smoke(max_runtime_seconds: float) -> dict[str, object]:
    payload = _with_corrected_q(v1.run_smoke, max_runtime_seconds)
    builtin = corrected_q(0.125)
    numpy_scalar = corrected_q(np.float64(0.125))
    payload = dict(payload)
    payload["run_id"] = RUN_ID
    payload["correction"] = "PF-069_NUMPY_REAL_TO_BUILTIN_FLOAT_ONLY"
    payload["checks"] = dict(payload["checks"])
    payload["checks"].update(
        {
            "builtin_float_exact_one_eighth": builtin == sp.Rational(1, 8),
            "numpy_float64_exact_one_eighth": numpy_scalar == sp.Rational(1, 8),
            "builtin_numpy_exact_parity": builtin == numpy_scalar,
            "V1_q_restored": v1._q is not corrected_q,
        }
    )
    payload["passed"] = bool(payload["checks"]) and all(payload["checks"].values())
    return payload


def run_audit(max_runtime_seconds: float) -> dict[str, object]:
    payload = _with_corrected_q(v1.run_audit, max_runtime_seconds)
    payload = dict(payload)
    payload["test"] = "A2-K4 P5.3g7 S-C0 lower-moment coefficient passport RERUN1"
    payload["run_id"] = RUN_ID
    payload["technical_correction"] = {
        "id": "PF-069",
        "changed": "finite numbers.Real conversion only",
        "equations_weights_supports_thresholds_changed": False,
        "V1_q_restored_after_run": v1._q is not corrected_q,
    }
    payload["source_hashes"] = source_hashes()
    payload["checks"] = dict(payload["checks"])
    payload["checks"]["PF069_overlay_restored"] = v1._q is not corrected_q
    payload["all_checks_pass"] = bool(payload["checks"]) and all(payload["checks"].values())
    return payload

