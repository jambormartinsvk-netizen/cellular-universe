#!/usr/bin/env python
"""Bounded P5.3g1 provenance audit for the BR2 neutrino dipole."""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import time


ROOT = Path(__file__).resolve().parent.parent
FILES = {
    "84": "84_script_A2_K4_3b_RG_CLASS_analytic_collective_seed_CAMB_crosscheck.py",
    "89": "89_script_A2_K4_3b_RG_BR2_backreacted_superhorizon_evolution.py",
    "90": "90_script_A2_K4_3b_RG_BR2_conditioned_DAE_constraint_audit.py",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        raise ValueError("max-runtime-seconds must be in (0,5]")
    started = time.monotonic()
    texts: dict[str, str] = {}
    for key, filename in FILES.items():
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("P5.3g1 internal deadline exceeded")
        text = (ROOT / "scripts" / filename).read_text(encoding="utf-8")
        ast.parse(text, filename=filename)
        texts[key] = text
    seed_contract = "Return [dg,db,dc,dnu,qg,qnu,eta_s]" in texts["84"]
    qnu_definition = "q_i=4 theta_i/(3 k)" in texts["84"]
    assignment_89 = "z[N0 + 1] = seed[5]" in texts["89"]
    assignment_90 = "z[N0+1]=v[5]" in texts["90"]
    f1_equation_89 = "out[start + 1] = kh * (f[0] - 2.0 * f[2]) / 3.0" in texts["89"]
    f1_equation_90 = "out[j+1]=kh*(f[0]-2*f[2])/3" in texts["90"]
    explicit_equivalence_markers = (
        "F1=qnu",
        "F_1=q_nu",
        "f[1]=qnu",
        "F1 = qnu",
    )
    explicit_equivalence = any(
        marker in (texts["84"] + texts["89"] + texts["90"])
        for marker in explicit_equivalence_markers
    )
    checks = {
        "seed84_declares_qnu_output": seed_contract,
        "seed84_declares_qnu_normalization": qnu_definition,
        "BR2_89_assigns_seed5_to_hierarchy_l1": assignment_89,
        "BR2_90_assigns_seed5_to_hierarchy_l1": assignment_90,
        "BR2_89_has_l1_hierarchy_equation": f1_equation_89,
        "BR2_90_has_l1_hierarchy_equation": f1_equation_90,
        "explicit_F1_equals_qnu_equivalence_present": explicit_equivalence,
    }
    verdict = "PASS_MAPY_F1_NORMALIZATION_CLOSED" if all(checks.values()) else "REVIEW_BLOCKED_F1_NORMALIZATION_UNPROVEN"
    payload = {
        "test": "KMPC-011 P5.3g1 F1/qnu normalization provenance audit",
        "scope": "source/provenance only; no coefficient derivation, ODE, score, or G8",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "checks": checks,
        "next_step": (
            "derive l>=2 regular coefficients from the BR2 hierarchy"
            if verdict.startswith("PASS")
            else "record or import an authoritative same-convention F1=qnu definition before deriving l>=2"
        ),
        "verdict": verdict,
    }
    if args.output.exists():
        raise FileExistsError(args.output)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if verdict.startswith("PASS") else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as error:
        print(json.dumps({"verdict": "TIMEOUT_UNCLOSED", "error": str(error)}))
        raise SystemExit(124)
