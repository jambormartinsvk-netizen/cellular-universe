#!/usr/bin/env python
"""Bounded symbolic leading adiabatic P5 seed ledger; no ODE."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import time

import sympy as sp

from baseScripts.p5_general_synchronous.adiabatic_seed_identities import build_adiabatic_seed_identities


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--max-runtime-seconds", type=float, default=5.0)
    p.add_argument("--output", type=Path, required=True)
    return p.parse_args()


def write_once(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f"refusing to overwrite immutable output: {path}")
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        raise ValueError("max-runtime-seconds must be in (0, 5]")
    started = time.monotonic()
    identities, metadata = build_adiabatic_seed_identities()
    checks: dict[str, bool] = {}
    residuals: dict[str, str] = {}
    for name, expression in identities.items():
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("P5.3b internal deadline exceeded")
        reduced = sp.simplify(expression)
        residuals[name] = str(reduced)
        checks[name] = bool(reduced == 0)
    delta_symbol = next(symbol for symbol in metadata["uc_power"].free_symbols if symbol.name == "delta")
    checks["uc_power_is_higher_than_adiabatic_metric_power_at_frozen_A1_delta"] = bool(float(metadata["uc_power"].subs(delta_symbol, sp.Rational(2297, 100000))) > 2.0)
    payload = {
        "test": "KMPC-006 P5.3b leading radiation-era adiabatic seed ledger",
        "scope": "leading adiabatic Puiseux terms only; no isocurvature, higher orders, gauge proof, ODE, score, or G8",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "checks": checks,
        "residuals": residuals,
        "leading_coefficients": {name: str(value) for name, value in metadata.items()},
        "verdict": "PASS_P5_3B_ADIABATIC_LEADING_SEED" if all(checks.values()) else "STOP_P5_3B_ADIABATIC_LEADING_SEED",
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
