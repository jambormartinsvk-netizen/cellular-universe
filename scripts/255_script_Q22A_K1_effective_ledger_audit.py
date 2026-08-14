#!/usr/bin/env python3
"""Bounded structural audit of the effective A1 F->C background ledger.

This is deliberately not an ODE solve and not a microscopic-sequence claim.
It verifies only the source terms already encoded in the two registered A1
background implementations.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import time

import sympy as sp


ROOT = Path(__file__).resolve().parent.parent
SOURCE_11 = ROOT / "scripts" / "11_script_A1_K1_cdm_background_audit.py"
SOURCE_BASE = ROOT / "scripts" / "baseScripts" / "k_mpc_005" / "af_from_a1_background.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--json-output", type=Path, required=True)
    return parser.parse_args()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    args = parse_args()
    started = time.monotonic()
    require(0.0 < args.max_runtime_seconds <= 5.0, "internal runtime limit must be in (0, 5]")
    source_11 = SOURCE_11.read_text(encoding="utf-8")
    source_base = SOURCE_BASE.read_text(encoding="utf-8")
    if time.monotonic() - started > args.max_runtime_seconds:
        raise TimeoutError("Q22a-K1 internal deadline exceeded while reading sources")

    gamma, rho_f = sp.symbols("Gamma rho_F", finite=True)
    q_f = -gamma * rho_f
    q_c = gamma * rho_f
    q_r = sp.Integer(0)
    conservation = sp.simplify(q_f + q_c + q_r)
    lambda_zero = [sp.simplify(term.subs(gamma, 0)) for term in (q_f, q_c, q_r)]

    # Exact source signatures, not a loose prose match.
    signatures = {
        "script_11_fuel_loss": "-3.0 * p.delta * x_f - transfer" in source_11,
        "script_11_matter_gain": "-3.0 * x_m + transfer" in source_11,
        "script_11_radiation_no_transfer": "-4.0 * x_r," in source_11,
        "base_fuel_loss": "-3.0 * p.delta * xf - transfer" in source_base,
        "base_matter_gain": "-3.0 * xm + transfer" in source_base,
        "base_radiation_no_transfer": "-4.0 * xr" in source_base,
        "both_define_transfer_lambda_xf_over_E": (
            "transfer = p.lam * x_f / e" in source_11
            and "transfer = p.lam * xf / math.sqrt(e2)" in source_base
        ),
    }
    checks = {
        "exact_total_source_conservation": conservation == 0,
        "direct_radiation_source_exact_zero": q_r == 0,
        "lambda_zero_null_limit": all(term == 0 for term in lambda_zero),
        "registered_a1_source_signatures": all(signatures.values()),
    }
    elapsed = time.monotonic() - started
    if elapsed > args.max_runtime_seconds:
        raise TimeoutError("Q22a-K1 internal deadline exceeded")

    result = {
        "test": "Q22a-K1 effective A1 F-to-C ledger structural audit",
        "status": "PASS" if all(checks.values()) else "STOP",
        "physical_verdict": (
            "BASELINE_EFFECTIVE_LEDGER_PASS_NOT_MICRO_SEQUENCE_DECISION"
            if all(checks.values()) else "STOP_PROVENANCE_OR_CONSERVATION_MISMATCH"
        ),
        "scope": "exact source-term algebra and registered-code provenance; no ODE; no microphysical order claim",
        "equations": {
            "Q_F": str(q_f),
            "Q_C": str(q_c),
            "Q_R": str(q_r),
            "Q_total": str(conservation),
        },
        "checks": checks,
        "source_signatures": signatures,
        "limits": {"internal_seconds": args.max_runtime_seconds, "elapsed_seconds": elapsed},
    }
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
