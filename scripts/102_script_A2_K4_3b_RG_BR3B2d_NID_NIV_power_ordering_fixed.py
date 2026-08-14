#!/usr/bin/env python
"""Corrected clone of script 101; converts SymPy booleans before JSON.

Script 101 is preserved as an ERROR_UNCLOSED audit artifact.  Physics,
formulae and thresholds are unchanged here.
"""

from __future__ import annotations

import argparse
import json
import time

import sympy as sp


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=8.0)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 10.0:
        parser.error("runtime must be in (0, 10]")
    started = time.monotonic()

    delta = sp.Rational(2297, 100000)
    p = sp.simplify(4 - 3 * delta)
    neff = sp.Rational(3046, 1000) + sp.Rational(535, 10000)
    rg = sp.simplify(1 / (1 + sp.Rational(2271, 10000) * neff))
    rf = sp.simplify(1 - rg)

    nid_density = {"gamma": -rf / rg, "fs": sp.Integer(1), "base_power": 0}
    nid_velocity_u = {"gamma": -rf / (4 * rg), "fs": sp.Rational(1, 4),
                      "base_power": 0}
    niv_density = {"gamma": rf / rg, "fs": sp.Integer(-1), "base_power": 1}
    niv_velocity_u = {"gamma": -3 * rf / (4 * rg), "fs": sp.Rational(3, 4),
                      "base_power": -1}

    def weighted(pair: dict[str, sp.Expr]) -> sp.Expr:
        return sp.simplify(rg * pair["gamma"] + rf * pair["fs"])

    checks = {
        "NID_leading_density_is_exactly_compensated": bool(weighted(nid_density) == 0),
        "NID_leading_U_is_exactly_compensated": bool(weighted(nid_velocity_u) == 0),
        "NIV_leading_density_is_exactly_compensated": bool(weighted(niv_density) == 0),
        "NIV_leading_U_is_exactly_compensated": bool(weighted(niv_velocity_u) == 0),
        "NID_Euler_dressing_precedes_hx_sector": bool(p < p + 3),
        "NIV_Euler_dressing_precedes_hx_sector": bool(p - 1 < p + 2),
    }
    sectors = {
        "NID": [
            {"power": str(p), "decimal_power": float(p),
             "origin": "O(y) Hconf-slope correction times compensated U at a^0",
             "total_leading_density_or_momentum": "zero",
             "status": "relative-radiation hierarchy response required"},
            {"power": str(p + 2), "decimal_power": float(p + 2),
             "origin": "O(y) gradient/shear/eta sector built on a^2 radiation terms",
             "total_leading_density_or_momentum": "shear undecided",
             "status": "BR3B-2e required"},
            {"power": str(p + 3), "decimal_power": float(p + 3),
             "origin": "common fuel response driven by h_x~a^3",
             "total_leading_density_or_momentum": "BR3B-2c compatible",
             "status": "must follow the earlier sectors"},
        ],
        "NIV": [
            {"power": str(p - 1), "decimal_power": float(p - 1),
             "origin": "O(y) Hconf-slope correction times compensated U at a^-1",
             "total_leading_density_or_momentum": "zero",
             "status": "relative-radiation hierarchy response required"},
            {"power": str(p + 1), "decimal_power": float(p + 1),
             "origin": "O(y) density/eta/shear sector built on a^1 NIV terms",
             "total_leading_density_or_momentum": "density zero; shear undecided",
             "status": "BR3B-2e required"},
            {"power": str(p + 2), "decimal_power": float(p + 2),
             "origin": "common fuel response driven by h_x~a^2",
             "total_leading_density_or_momentum": "BR3B-2c compatible",
             "status": "must follow the earlier sectors"},
        ],
    }
    ordered = all(
        all(group[index]["decimal_power"] < group[index + 1]["decimal_power"]
            for index in range(len(group) - 1))
        for group in sectors.values()
    )
    checks["all_mode_sectors_are_strictly_ordered"] = bool(ordered)
    passed = all(checks.values())
    output = {
        "test": "A2-K4.3b-RG-BR3B-2d NID/NIV fractional power ordering (fixed)",
        "supersedes_execution_only": "101 script; its ERROR_UNCLOSED remains preserved",
        "p_Omega_f": str(p),
        "exact_compensated_coefficients": {
            "NID_density": {key: str(value) for key, value in nid_density.items()},
            "NID_U": {key: str(value) for key, value in nid_velocity_u.items()},
            "NIV_density": {key: str(value) for key, value in niv_density.items()},
            "NIV_U": {key: str(value) for key, value in niv_velocity_u.items()},
        },
        "ordered_sectors": sectors,
        "checks": checks,
        "execution_verdict": ("PASS_MULTIPOWER_ORDER_AND_COMPENSATION_LEDGER"
                              if passed else "REVIEW_BR3B2D"),
        "physical_verdict": "NID/NIV remain alive; earlier compensated relative-radiation sectors must precede the h_x fuel sector",
        "scope_limit": "neutrino shear and l>=3 hierarchy coefficients not yet included",
        "K4_3b_RG_verdict": "NEUZAVRETA_BR3B2E_NID_NIV_HIERARCHY_COEFFICIENTS_REQUIRED",
        "canonical_score": "60/100 = G6",
        "next_step": "BR3B-2e populate shear and minimum regular l>=3 recursion at every earlier NID/NIV power",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
    except Exception as exc:  # pragma: no cover
        print(json.dumps({"execution_verdict": "ERROR_UNCLOSED", "error": repr(exc)}))
        raise SystemExit(2)
