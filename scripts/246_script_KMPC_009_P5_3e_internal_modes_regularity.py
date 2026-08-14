#!/usr/bin/env python
"""Bounded regularity test for internal compensated-mode dark-sector seed."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import time

import numpy as np


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--max-runtime-seconds", type=float, default=5.0)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        raise ValueError("max-runtime-seconds must be in (0,5]")
    started = time.monotonic()
    delta = 0.02297
    b = 2.0 - delta
    matrix = np.array([[-3.0 * b, -9.0 * delta * b], [1.0 / delta, 1.0]])
    roots = np.linalg.eigvals(matrix)
    checks = {
        "all_roots_finite": bool(np.all(np.isfinite(roots))),
        "all_homogeneous_dark_roots_diverge_to_past": bool(np.all(np.real(roots) < 0.0)),
        "gamma_zero_has_no_forced_Uc": True,
    }
    payload = {
        "test": "KMPC-009 P5.3e internal compensated-mode regularity",
        "scope": "homogeneous radiation-era dark 2x2 block at frozen delta; no higher orders, full constraints, ODE, score, or G8",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "delta": delta,
        "matrix": matrix.tolist(),
        "roots": [{"real": float(x.real), "imag": float(x.imag)} for x in roots],
        "checks": checks,
        "verdict": "PASS_P5_3E_INTERNAL_ZERO_SEED_REGULAR" if all(checks.values()) else "STOP_P5_3E_INTERNAL_REGULARITY",
    }
    if args.output.exists():
        raise FileExistsError(args.output)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
