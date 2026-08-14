#!/usr/bin/env python
"""Bounded no-ODE symbolic preflight for the P5 general-synchronous state."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import time

import sympy as sp

from baseScripts.p5_general_synchronous.coefficient_identities import build_identities


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


def main() -> int:
    args = parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        raise ValueError("max-runtime-seconds must be in (0, 5]")
    started = time.monotonic()
    identities, metadata = build_identities()
    checks: dict[str, bool] = {}
    residuals: dict[str, str] = {}
    for name, expression in identities.items():
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("P5.1 internal deadline exceeded")
        reduced = sp.simplify(expression)
        residuals[name] = str(reduced)
        checks[name] = bool(reduced == 0)
    k = metadata["k"]
    background_names = ("background_ell", "gamma", "beta_c", "beta_f")
    checks["k_absent_from_background_coefficients"] = all(not metadata[name].has(k) for name in background_names)
    checks["k_present_only_in_s2"] = bool(metadata["s2"].has(k) and metadata["s2"].as_powers_dict().get(k) == 2)
    m_full = str(metadata["m_full"])
    checks["state_contains_Uc_and_Ub_momentum"] = "Uc" in m_full and "Ub" in m_full
    payload = {
        "test": "KMPC-003 P5.1 exact-A1 general-synchronous static ledger",
        "scope": "symbolic identities only; no ODE, no score, no G8",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "checks": checks,
        "residuals": residuals,
        "state_basis": "includes U_c and U_b; M_full includes CDM/baryon momentum",
        "verdict": "PASS_P5_1_STATIC_LEDGER" if all(checks.values()) else "STOP_P5_1_STATIC_LEDGER",
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
