#!/usr/bin/env python
"""Bounded derivation of BR2 standard-mode neutrino l=2 seed candidates."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import time

import sympy as sp


ROOT = Path(__file__).resolve().parent.parent
SOURCE84 = ROOT / "scripts" / "84_script_A2_K4_3b_RG_CLASS_analytic_collective_seed_CAMB_crosscheck.py"


def lead_power(expr: sp.Expr, y: sp.Symbol) -> int | None:
    expanded = sp.Poly(sp.expand(expr), y)
    if expanded.is_zero:
        return None
    return min(monomial[0] for monomial, coefficient in expanded.terms() if coefficient != 0)


def integrate_zero(expr: sp.Expr, y: sp.Symbol) -> sp.Expr:
    return sp.simplify(sp.integrate(expr, (y, 0, y)))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        raise ValueError("max-runtime-seconds must be in (0,5]")
    started = time.monotonic()
    source = SOURCE84.read_text(encoding="utf-8")
    ast.parse(source, filename=SOURCE84.name)
    required_branches = all(f'mode == "initial_{name}"' in source for name in ("adiabatic", "iso_CDM", "iso_baryon", "iso_neutrino", "iso_neutrino_vel"))
    if not required_branches:
        raise RuntimeError("source 84 standard seed branches are not all present")
    y, q, om, fnu, fg, fb, fc = sp.symbols("y q om fnu fg fb fc", nonzero=True)
    omt = om * y / q
    dg_ad = -y**2 / 3 * (1 - omt / 5)
    f1_ad = -q * y**3 / 36 / (4 * fnu + 15) * (4 * fnu + 23 - 3 * (8 * fnu**2 + 50 * fnu + 275) / (20 * (2 * fnu + 15)) * omt)
    eta_ad = 1 - y**2 / (12 * (15 + 4 * fnu)) * (5 + 4 * fnu - (16 * fnu**2 + 280 * fnu + 325) / (10 * (2 * fnu + 15)) * omt)
    dg_cdi = fc * omt * (-sp.Rational(2, 3) + omt / 4)
    f1_cdi = -fc * om * y**2 / 12
    eta_cdi = -fc * omt * (sp.Rational(1, 6) - omt / 16)
    dg_bi = fb * omt * (-sp.Rational(2, 3) + omt / 4)
    f1_bi = -fb * om * y**2 / 12
    eta_bi = -fb * omt * (sp.Rational(1, 6) - omt / 16)
    f1_nid = q * y / 4
    eta_nid = -fnu * y**2 / (6 * (4 * fnu + 15))
    dc_nid = -fnu * fb * y**2 * omt / (80 * fg)
    f1_niv = sp.Rational(3, 4) * q * (1 - y**2 * (4 * fnu + 9) / (6 * (4 * fnu + 5)))
    eta_niv = fnu * y * (-1 / (4 * fnu + 5) + (-sp.Rational(3, 64) * fb / fg + sp.Rational(15, 4) / (4 * fnu + 15) / (4 * fnu + 5)) * omt)
    dc_niv = -sp.Rational(9, 64) * fnu * fb * y * omt / fg
    modes = {
        "AD": (sp.Rational(3, 4) * dg_ad, f1_ad, eta_ad),
        "CDI": (1 + sp.Rational(3, 4) * dg_cdi, f1_cdi, eta_cdi),
        "BI": (sp.Rational(3, 4) * dg_bi, f1_bi, eta_bi),
        "NID": (dc_nid, f1_nid, eta_nid),
        "NIV": (dc_niv, f1_niv, eta_niv),
    }
    checks: dict[str, bool] = {"source84_all_standard_branches_present": required_branches}
    rows: dict[str, object] = {}
    for name, (dc, f1, eta) in modes.items():
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("P5.3g3 internal deadline exceeded")
        hy = -2 * sp.diff(dc, y)
        driving = sp.simplify(sp.Rational(2, 5) * f1 + sp.Rational(4, 15) * hy + sp.Rational(8, 5) * sp.diff(eta, y))
        f2_low = integrate_zero(driving, y)
        f3_first = integrate_zero(sp.Rational(3, 7) * f2_low, y)
        f2 = integrate_zero(driving - sp.Rational(3, 5) * f3_first, y)
        l2_residual = sp.simplify(sp.diff(f2, y) - (driving - sp.Rational(3, 5) * f3_first))
        power2 = lead_power(f2, y)
        power3 = lead_power(f3_first, y)
        mode_checks = {
            "F2_at_origin_zero": bool(sp.simplify(f2.subs(y, 0)) == 0),
            "F2_has_positive_leading_power": power2 is not None and power2 > 0,
            "F3_starts_later_than_F2": power2 is not None and power3 is not None and power3 > power2,
            "truncated_l2_residual_zero": bool(l2_residual == 0),
        }
        checks.update({f"{name}_{key}": value for key, value in mode_checks.items()})
        rows[name] = {
            "F2_candidate": str(sp.factor(f2)),
            "F3_first_induced": str(sp.factor(f3_first)),
            "F2_leading_power_in_y": power2,
            "F3_leading_power_in_y": power3,
            "l2_residual": str(l2_residual),
        }
    passed = all(checks.values())
    payload = {
        "test": "KMPC-014 P5.3g3 standard-mode neutrino l=2 regular seed derivation",
        "scope": "source-bound candidate derivation; no independent Einstein residual, photon TCA, ODE, score, or G8",
        "source84_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "checks": checks,
        "modes": rows,
        "next_step": "independent Einstein/constraint ledger for these l=2 candidates" if passed else "review the standard l=2 derivation before any P5.4 work",
        "verdict": "DERIVATION_PASS_P5_3G3_NEUTRINO_L2_CANDIDATES" if passed else "REVIEW_BLOCKED_P5_3G3_NEUTRINO_L2",
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
