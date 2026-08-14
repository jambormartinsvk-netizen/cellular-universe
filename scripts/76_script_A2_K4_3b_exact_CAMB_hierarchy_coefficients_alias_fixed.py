#!/usr/bin/env python
"""Alias-corrected successor to K4.3b script 75."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import time

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
LOCAL_DEPS = ROOT / ".deps" / "python"
if LOCAL_DEPS.exists():
    sys.path.insert(0, str(LOCAL_DEPS))

import camb  # noqa: E402
import camb.symbolic as cs  # noqa: E402


def brightness(name: str, ell: int):
    if name == "J":
        if ell == 1:
            return cs.q_g
        if ell == 2:
            return cs.pi_g
    if name == "G":
        if ell == 1:
            return cs.q_r
        if ell == 2:
            return cs.pi_r
    return cs._make_index_func(name, ell)


def j_expected(ell: int):
    current = brightness("J", ell)
    previous = brightness("J", ell - 1)
    following = brightness("J", ell + 1)
    rhs = -cs.k / (2 * ell + 1) * (
        (ell + 1) * cs.Kf[ell] * following - ell * previous
    ) - cs.opacity * current
    if ell == 2:
        rhs += sp.Rational(8, 15) * cs.k * cs.sigma + cs.opacity * cs.polter
    return sp.simplify(rhs)


def g_expected(ell: int):
    current = brightness("G", ell)
    previous = brightness("G", ell - 1)
    following = brightness("G", ell + 1)
    rhs = -cs.k / (2 * ell + 1) * (
        (ell + 1) * cs.Kf[ell] * following - ell * previous
    )
    if ell == 2:
        rhs += sp.Rational(8, 15) * cs.k * cs.sigma
    return sp.simplify(rhs)


def e_expected(ell: int):
    current = cs._make_index_func("E", ell)
    previous = 0 if ell == 2 else cs._make_index_func("E", ell - 1)
    following = cs._make_index_func("E", ell + 1)
    rhs = -cs.k / (2 * ell + 1) * (
        (ell + 3) * (ell - 1) * cs.Kf[ell] * following / (ell + 1)
        - ell * previous
    ) - cs.opacity * current
    if ell == 2:
        rhs += cs.polter * cs.opacity
    return sp.simplify(rhs)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=20.0)
    args = parser.parse_args()
    if not (0.0 < args.max_runtime_seconds <= 50.0):
        parser.error("--max-runtime-seconds must be in (0, 50]")
    started = time.monotonic()
    residuals: dict[str, str] = {}
    checks: dict[str, bool] = {}

    for ell in range(2, 9):
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("internal alias-fixed CAMB hierarchy deadline exceeded")
        comparisons = {
            f"J_l{ell}": sp.simplify(cs.J_eq(ell).rhs - j_expected(ell)),
            f"G_l{ell}": sp.simplify(cs.G_eq(ell).rhs - g_expected(ell)),
            f"E_l{ell}": sp.simplify(cs.E_eq(ell).rhs - e_expected(ell)),
        }
        for name, residual in comparisons.items():
            residuals[name] = str(residual)
            checks[name] = bool(residual == 0)

    expected_polter = sp.Rational(2, 15) * (
        sp.Rational(3, 4) * cs.pi_g + sp.Rational(9, 2) * cs.E_2
    )
    residual = sp.simplify(cs.polter_sub.rhs - expected_polter)
    residuals["polarization_source"] = str(residual)
    checks["polarization_source"] = bool(residual == 0)
    passed = all(checks.values())

    output = {
        "test": "A2-K4.3b exact CAMB hierarchy coefficients, alias-fixed successor to script 75",
        "CAMB_version": camb.__version__,
        "successor_to": "75_script_A2_K4_3b_exact_CAMB_hierarchy_coefficient_crosscheck.py",
        "correction": "map J_2->pi_g and G_2->pi_r in expected l=3 backward coupling",
        "ell_range": [2, 8],
        "exact_checks": len(checks),
        "checks": checks,
        "symbolic_residuals": residuals,
        "verdict": "PASS_EXACT_CAMB_HIERARCHY_COEFFICIENTS_ALIAS_FIXED" if passed else "COEFFICIENT_MISMATCH_REVIEW",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"verdict": "ERROR_UNCLOSED", "error": repr(exc)}))
        raise SystemExit(2)

