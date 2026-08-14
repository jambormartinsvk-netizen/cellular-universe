#!/usr/bin/env python
"""Bounded formula-provenance ledger closing the BR2 F1/qnu bridge."""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import re
import time

import sympy as sp


ROOT = Path(__file__).resolve().parent.parent
FILES = {
    "84": "84_script_A2_K4_3b_RG_CLASS_analytic_collective_seed_CAMB_crosscheck.py",
    "90": "90_script_A2_K4_3b_RG_BR2_conditioned_DAE_constraint_audit.py",
    "111": "111_script_A2_K4_3b_RG_BR3B2f2_NID_NIV_baryon_fraction_difference.py",
}


def compact(text: str) -> str:
    return re.sub(r"(?<![0-9])([0-9]+)\.0(?![0-9])", r"\1", re.sub(r"\s+", "", text))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        raise ValueError("max-runtime-seconds must be in (0,5]")
    started = time.monotonic()
    text: dict[str, str] = {}
    for key, filename in FILES.items():
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("P5.3g2 internal deadline exceeded")
        value = (ROOT / "scripts" / filename).read_text(encoding="utf-8")
        ast.parse(value, filename=filename)
        text[key] = compact(value)
    H0, a, E, q, k, hconf, F1, qnu = sp.symbols("H0 a E q k hconf F1 qnu", nonzero=True)
    u_br2 = 3 * a * E * F1 / (4 * q)
    u_camb = 3 * hconf * qnu / (4 * k)
    bridge = {hconf: H0 * a * E, k: H0 * q}
    residual_general = sp.factor((u_br2 - u_camb.subs(bridge)))
    residual_after_identification = sp.simplify(residual_general.subs(F1, qnu))
    solved = sp.solve(sp.Eq(u_br2, u_camb.subs(bridge)), F1)
    checks = {
        "seed84_declares_qnu_equals_4theta_over_3k": "q_i=4theta_i/(3k)" in text["84"],
        "BR2_defines_q_as_k_over_H0": "q=args.k_mpc/(100*p.h/299792.458)" in text["90"],
        "BR2_defines_U_nu_from_F1": "un=3*a*e*fn[1]/(4*q)" in text["90"],
        "CAMB_audit_defines_U_from_qnu": "U=Htheta/k^2=3Hq/(4k)" in text["111"],
        "algebraic_bridge_residual_is_zero_after_F1_equals_qnu": bool(residual_after_identification == 0),
        "unique_bridge_solution_is_F1_equals_qnu": solved == [qnu],
    }
    passed = all(checks.values())
    payload = {
        "test": "KMPC-013 P5.3g2 BR2 F1/qnu formula-provenance bridge",
        "scope": "normalization bridge only; no l>=2 coefficient derivation, ODE, score, or G8",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "checks": checks,
        "equations": {
            "U_BR2": str(u_br2),
            "U_CAMB_after_units": str(sp.simplify(u_camb.subs(bridge))),
            "difference_before_identification": str(residual_general),
            "difference_after_F1_equals_qnu": str(residual_after_identification),
            "solution_of_equal_U": [str(item) for item in solved],
        },
        "next_step": "derive the regular l=2 and l>=3 standard seed coefficients from the BR2 hierarchy" if passed else "keep P5.3g blocked; repair missing bridge source",
        "verdict": "PASS_P5_3G2_F1_QNU_NORMALIZATION_BRIDGE" if passed else "REVIEW_BLOCKED_P5_3G2_NORMALIZATION_BRIDGE_UNCLOSED",
    }
    if args.output.exists():
        raise FileExistsError(args.output)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if passed else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as error:
        print(json.dumps({"verdict": "TIMEOUT_UNCLOSED", "error": str(error)}))
        raise SystemExit(124)
