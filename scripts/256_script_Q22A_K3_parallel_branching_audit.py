#!/usr/bin/env python3
"""Bounded algebraic audit of the minimal parallel F->C and F->R ledger."""

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

    gamma, rho_f, b = sp.symbols("Gamma rho_F b", finite=True)
    q_f = -gamma * rho_f
    q_c = b * gamma * rho_f
    q_r = (1 - b) * gamma * rho_f
    conservation = sp.simplify(q_f + q_c + q_r)
    k1_residuals = [sp.simplify(v.subs(b, 1) - target) for v, target in zip((q_f, q_c, q_r), (-gamma * rho_f, gamma * rho_f, 0))]
    k2_residuals = [sp.simplify(v.subs(b, 0) - target) for v, target in zip((q_f, q_c, q_r), (-gamma * rho_f, 0, gamma * rho_f))]
    derivative_wrt_b = [sp.simplify(sp.diff(v, b)) for v in (q_f, q_c, q_r)]
    underdetermination_identity = sp.simplify(sp.diff(conservation, b))
    elapsed = time.monotonic() - started
    if elapsed > args.max_runtime_seconds:
        raise TimeoutError("Q22a-K3 internal deadline exceeded")

    checks = {
        "exact_total_source_conservation": conservation == 0,
        "b_equals_one_exactly_reduces_to_K1": all(v == 0 for v in k1_residuals),
        "b_equals_zero_exactly_reduces_to_K2": all(v == 0 for v in k2_residuals),
        "conservation_does_not_fix_b": underdetermination_identity == 0,
    }
    result = {
        "test": "Q22a-K3 minimal parallel-branching algebra audit",
        "status": "PASS_ALGEBRA_REVIEW_BLOCKED" if all(checks.values()) else "STOP",
        "physical_verdict": (
            "REVIEW_BLOCKED_UNDERIVED_BRANCH_RATIO_B"
            if all(checks.values()) else "STOP_LEDGER_OR_LIMIT_MISMATCH"
        ),
        "scope": "exact conservation and null-limit structure; no assertion that b is physically derived",
        "equations": {"Q_F": str(q_f), "Q_C": str(q_c), "Q_R": str(q_r), "Q_total": str(conservation)},
        "branch_sensitivity": {"dQF_db": str(derivative_wrt_b[0]), "dQC_db": str(derivative_wrt_b[1]), "dQR_db": str(derivative_wrt_b[2]), "dQtotal_db": str(underdetermination_identity)},
        "checks": checks,
        "limits": {"internal_seconds": args.max_runtime_seconds, "elapsed_seconds": elapsed},
    }
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
