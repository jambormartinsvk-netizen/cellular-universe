#!/usr/bin/env python
"""Bounded symbolic P5.2 constraint ledger; no ODE or numerical evolution."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import time

import sympy as sp

from baseScripts.p5_general_synchronous.constraint_identities import build_constraint_identities


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
    identities, metadata = build_constraint_identities()
    residuals: dict[str, str] = {}
    checks: dict[str, bool] = {}
    reconstruction_names = {
        "full_momentum_species_content", "constraint_00_reconstruction",
        "constraint_0i_reconstruction", "constraint_trace_reconstruction",
        "constraint_traceless_reconstruction", "paired_transfer_cancels",
        "uc_transfer_vanishes_gamma_zero", "uf_transfer_vanishes_gamma_zero",
        "photon_baryon_slip_definition",
    }
    for name, expression in identities.items():
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("P5.2 internal deadline exceeded")
        reduced = sp.simplify(expression)
        residuals[name] = str(reduced)
        if name in reconstruction_names:
            checks[name] = bool(reduced == 0)
    momentum_text = str(metadata["momentum"])
    checks["momentum_has_Uc_Uf_Ub_Ugamma_Unu_Usteam"] = all(token in momentum_text for token in ("Uc", "Uf", "Ub", "Ug", "Un", "Us"))
    checks["photon_baryon_velocities_remain_distinct_symbols"] = "Ug" in str(metadata["slip_raw"]) and "Ub" in str(metadata["slip_raw"])
    checks["energy_product_ledger_is_independent_not_tautological"] = residuals["energy_product_ledger"] == "D_x - M*s2 + M*hc - 4*M + P - S + W*hx/2" or residuals["energy_product_ledger"] != "0"
    checks["momentum_product_ledger_is_independent_not_tautological"] = residuals["momentum_product_ledger"] != "0"
    payload = {
        "test": "KMPC-004 P5.2 full species-first structural constraint ledger",
        "scope": "symbolic reconstruction/ledger only; no ODE, no numerical constraint conservation, no score, no G8",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "checks": checks,
        "residuals": residuals,
        "independent_ledgers": {
            "energy_product_ledger": residuals["energy_product_ledger"],
            "momentum_product_ledger": residuals["momentum_product_ledger"],
        },
        "state_basis": "separate U_c, U_b, U_f, U_gamma, U_nu, U_steam and explicit photon-baryon slip",
        "verdict": "PASS_P5_2_STRUCTURAL_CONSTRAINT_LEDGER" if all(checks.values()) else "STOP_P5_2_STRUCTURAL_CONSTRAINT_LEDGER",
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
