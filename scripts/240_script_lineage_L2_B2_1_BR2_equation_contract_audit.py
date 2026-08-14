#!/usr/bin/env python
"""Bounded source-equation audit of BR2 K4 energy-frame terms; no imports/ODE."""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import re
import time


ROOT = Path(__file__).resolve().parent.parent
TARGETS = (
    "89_script_A2_K4_3b_RG_BR2_backreacted_superhorizon_evolution.py",
    "90_script_A2_K4_3b_RG_BR2_conditioned_DAE_constraint_audit.py",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def write_once(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f"refusing to overwrite immutable output: {path}")
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def contains(compact: str, expression: str) -> bool:
    return expression in compact


def main() -> int:
    args = parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        raise ValueError("max-runtime-seconds must be in (0, 5]")
    started = time.monotonic()
    rows: dict[str, object] = {}
    for filename in TARGETS:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("L2-B2.1 internal deadline exceeded")
        path = ROOT / "scripts" / filename
        text = path.read_text(encoding="utf-8")
        ast.parse(text, filename=str(path))
        c = re.sub(r"\s+", "", text)
        metric_dc = (
            contains(c, "out[DC]=-s2*z[UC]-0.5*z[HX]+g*r*(z[DF]-z[DC])")
            or contains(c, "out[DC]=-s2*z[UC]-hx/2.0+g*r*(z[DF]-z[DC])")
        )
        rows[filename] = {
            "gamma_equals_lambda_over_E": contains(c, "g=p.lam/e"),
            "energy_frame_Ud": contains(c, "ud=(1.0-beta)*z[UC]+beta*z[UF]"),
            "beta_enthalpy_weight": contains(c, "beta=p.delta*xf/(xc+p.delta*xf)"),
            "cdm_continuity": metric_dc,
            "cdm_euler": contains(c, "out[UC]=(hc-1.0)*z[UC]+g*r*beta*(z[UF]-z[UC])"),
            "fuel_euler": contains(c, "out[UF]=(hc+2.0)*z[UF]+z[DF]/p.delta+g/p.delta*(2.0*z[UF]-ud)"),
            "momentum_contains_cdm_fuel_baryon": contains(c, "xc*z[UC]+p.delta*xf*z[UF]+xb*z[UG]"),
            "k_is_argument_not_fixed_background": (
                contains(c, "q=args.k_mpc/(100.0*p.h/299792.458)")
                and "K_MPC=0.05" not in c and "k_mpc=0.05" not in c
            ),
        }
    checks = {f"{Path(name).stem}_{key}": bool(value) for name, row in rows.items() for key, value in row.items()}
    payload = {
        "test": "LINEAGE-L2-B2.1 BR2 exact source-equation contract audit",
        "scope": "syntax/text contract only; no model import, ODE, score, or source rewrite",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "checks": checks,
        "targets": rows,
        "unclosed_scope": ["fuel continuity full derivation", "all Einstein constraints", "lambda_to_zero", "hierarchy convergence", "numerical evolution"],
        "verdict": "PASS_L2_B2_1_BR2_CORE_CONTRACT" if all(checks.values()) else "STOP_L2_B2_1_BR2_CONTRACT_MISMATCH",
    }
    write_once(args.output, payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
