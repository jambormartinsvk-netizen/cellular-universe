#!/usr/bin/env python
"""Bounded P5.3f gauge/hierarchy source audit; no imports or ODE."""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import sympy as sp
import time


ROOT = Path(__file__).resolve().parent.parent
FILES = {
    "80": "80_script_A2_K4_3b_RG_internal_nu_steam_exact_regular_series.py",
    "84": "84_script_A2_K4_3b_RG_CLASS_analytic_collective_seed_CAMB_crosscheck.py",
    "89": "89_script_A2_K4_3b_RG_BR2_backreacted_superhorizon_evolution.py",
    "90": "90_script_A2_K4_3b_RG_BR2_conditioned_DAE_constraint_audit.py",
}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--max-runtime-seconds", type=float, default=5.0)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        raise ValueError("max-runtime-seconds must be in (0,5]")
    started = time.monotonic()
    texts = {}
    for key, name in FILES.items():
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("P5.3f internal deadline exceeded")
        text = (ROOT / "scripts" / name).read_text(encoding="utf-8")
        ast.parse(text, filename=name)
        texts[key] = text
    uc, uf, shift = sp.symbols("Uc Uf G")
    relative_residual = sp.simplify((uf + shift) - (uc + shift) - (uf - uc))
    initial89 = texts["89"][texts["89"].find("def initial"):texts["89"].find("def integrate")]
    initial90 = texts["90"][texts["90"].find("def initial"):texts["90"].find("def audit")]
    checks = {
        "relative_velocity_invariant_under_common_shift": bool(relative_residual == 0),
        "internal_source_80_has_exact_hierarchy_operator": "dF/dy = A F" in texts["80"],
        "internal_source_80_has_l2_and_higher_regular_orders": "regular_multipole_orders" in texts["80"],
        "standard_source_84_exports_only_l0_l1_variables": "pi_neutrino" not in texts["84"] and "sigma" not in texts["84"],
        "BR2_89_standard_initial_assigns_only_l0_l1": "z[N0] = seed[3]" in initial89 and "z[N0 + 1] = seed[5]" in initial89 and "z[N0 + 2]" not in initial89,
        "BR2_90_standard_initial_assigns_only_l0_l1": "z[N0]=v[3]" in initial90 and "z[N0+1]=v[5]" in initial90 and "z[N0+2]" not in initial90,
    }
    payload = {
        "test": "KMPC-010 P5.3f gauge-invariant relative velocity and hierarchy seed audit",
        "scope": "symbolic gauge identity and source map only; no hierarchy derivation, ODE, score, or G8",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "checks": checks,
        "relative_velocity_residual": str(relative_residual),
        "physical_verdict": "P5.4_BLOCKED_STANDARD_L2_PLUS_HIERARCHY_SEED_MISSING",
        "next_step": "derive or import auditable standard photon/neutrino l>=2 regular seed",
        "verdict": "PASS_P5_3F_GAUGE_HIERARCHY_GAP_MAPPED" if all(checks.values()) else "STOP_P5_3F_GAUGE_HIERARCHY_MAP_UNCLOSED",
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
