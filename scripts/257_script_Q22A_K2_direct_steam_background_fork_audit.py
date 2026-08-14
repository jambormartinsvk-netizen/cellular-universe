#!/usr/bin/env python3
"""Bounded structural audit showing that Q22a-K2 forks A1-K1 background."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import time

import sympy as sp


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--json-output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    started = time.monotonic()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        raise ValueError("internal runtime limit must be in (0, 5]")
    gamma, rho_f = sp.symbols("Gamma rho_F", positive=True, finite=True)
    k1 = (-gamma * rho_f, gamma * rho_f, sp.Integer(0))
    k2 = (-gamma * rho_f, sp.Integer(0), gamma * rho_f)
    source_difference = tuple(sp.simplify(a - b) for a, b in zip(k2, k1))
    checks = {
        "K2_exact_total_source_conservation": sp.simplify(sum(k2)) == 0,
        "K1_exact_total_source_conservation": sp.simplify(sum(k1)) == 0,
        "K2_differs_from_K1_for_nonzero_transfer": any(term != 0 for term in source_difference),
        "lambda_zero_common_null_limit": all(sp.simplify(term.subs(gamma, 0)) == 0 for term in (*k1, *k2)),
    }
    elapsed = time.monotonic() - started
    if elapsed > args.max_runtime_seconds:
        raise TimeoutError("Q22a-K2 internal deadline exceeded")
    result = {
        "test": "Q22a-K2 direct-steam versus A1-K1 background-fork audit",
        "status": "PASS_BACKGROUND_FORK_REQUIRED" if all(checks.values()) else "STOP",
        "physical_verdict": (
            "NOT_COMPATIBLE_WITH_FROZEN_A1_K1_BACKGROUND; SEPARATE_A1_BRANCH_REQUIRED"
            if all(checks.values()) else "STOP_ALGEBRA_MISMATCH"
        ),
        "scope": "structural source comparison only; no BBN, CMB, or viability claim",
        "K1_sources_F_C_R": [str(v) for v in k1],
        "K2_sources_F_C_R": [str(v) for v in k2],
        "K2_minus_K1_F_C_R": [str(v) for v in source_difference],
        "checks": checks,
        "limits": {"internal_seconds": args.max_runtime_seconds, "elapsed_seconds": elapsed},
    }
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
