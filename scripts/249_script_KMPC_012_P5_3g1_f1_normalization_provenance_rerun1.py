#!/usr/bin/env python
"""Bounded, formatting-tolerant rerun of P5.3g1 provenance audit."""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import re
import time


ROOT = Path(__file__).resolve().parent.parent
FILES = {
    "84": "84_script_A2_K4_3b_RG_CLASS_analytic_collective_seed_CAMB_crosscheck.py",
    "89": "89_script_A2_K4_3b_RG_BR2_backreacted_superhorizon_evolution.py",
    "90": "90_script_A2_K4_3b_RG_BR2_conditioned_DAE_constraint_audit.py",
}


def compact(text: str) -> str:
    """Remove whitespace and insignificant `.0` literals for fixed source shapes."""
    return re.sub(r"(?<![0-9])([0-9]+)\.0(?![0-9])", r"\1", re.sub(r"\s+", "", text))


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
            raise TimeoutError("P5.3g1 RERUN1 internal deadline exceeded")
        text = (ROOT / "scripts" / filename).read_text(encoding="utf-8")
        ast.parse(text, filename=filename)
        texts[key] = text
    normalized = {key: compact(value) for key, value in texts.items()}
    combined = "\n".join(texts.values())
    checks = {
        "seed84_declares_qnu_output": "Return[dg,db,dc,dnu,qg,qnu,eta_s]" in normalized["84"],
        "seed84_declares_qnu_normalization": "q_i=4theta_i/(3k)" in normalized["84"],
        "BR2_89_assigns_seed5_to_hierarchy_l1": "z[N0+1]=seed[5]" in normalized["89"],
        "BR2_90_assigns_seed5_to_hierarchy_l1": "z[N0+1]=v[5]" in normalized["90"],
        "BR2_89_has_l1_hierarchy_equation": "out[start+1]=kh*(f[0]-2*f[2])/3" in normalized["89"],
        "BR2_90_has_l1_hierarchy_equation": "out[start+1]=kh*(f[0]-2*f[2])/3" in normalized["90"],
        "explicit_F1_equals_qnu_equivalence_present": any(
            marker in compact(combined)
            for marker in ("F1=qnu", "F_1=q_nu", "f[1]=qnu")
        ),
    }
    mapping_closed = all(value for key, value in checks.items() if key != "explicit_F1_equals_qnu_equivalence_present")
    equivalence_closed = checks["explicit_F1_equals_qnu_equivalence_present"]
    verdict = "PASS_MAPY_F1_NORMALIZATION_CLOSED" if mapping_closed and equivalence_closed else "REVIEW_BLOCKED_F1_NORMALIZATION_UNPROVEN"
    payload = {
        "test": "KMPC-012 P5.3g1 F1/qnu normalization provenance RERUN1",
        "scope": "formatting-tolerant source/provenance audit; no coefficient derivation, ODE, score, or G8",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "checks": checks,
        "mapping_closed_except_equivalence": mapping_closed,
        "next_step": "record or import an authoritative same-convention F1=qnu definition before deriving l>=2",
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
