#!/usr/bin/env python
"""Bounded corrected P5.3g3 derivation using seed84 returned qn, not tn."""

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
    poly = sp.Poly(sp.expand(expr), y)
    if poly.is_zero:
        return None
    return min(monomial[0] for monomial, coefficient in poly.terms() if coefficient != 0)


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
    required = (
        "qn = 4.0 * tn / (3.0 * k)" in source
        and "return np.array([dg, db, dc, dn, qg, qn, eta_s]" in source
    )
    if not required:
        raise RuntimeError("seed84 returned qn mapping is unavailable")
    y, q, om, fnu, fg, fb, fc = sp.symbols("y q om fnu fg fb fc", nonzero=True)
    omt = om * y / q
    dg_ad = -y**2 / 3 * (1 - omt / 5)
    tn_ad = -q * y**3 / 36 / (4 * fnu + 15) * (4 * fnu + 23 - 3 * (8 * fnu**2 + 50 * fnu + 275) / (20 * (2 * fnu + 15)) * omt)
    eta_ad = 1 - y**2 / (12 * (15 + 4 * fnu)) * (5 + 4 * fnu - (16 * fnu**2 + 280 * fnu + 325) / (10 * (2 * fnu + 15)) * omt)
    dg_cdi = fc * omt * (-sp.Rational(2, 3) + omt / 4)
    tn_cdi = -fc * om * y**2 / 12
    eta_cdi = -fc * omt * (sp.Rational(1, 6) - omt / 16)
    dg_bi = fb * omt * (-sp.Rational(2, 3) + omt / 4)
    tn_bi = -fb * om * y**2 / 12
    eta_bi = -fb * omt * (sp.Rational(1, 6) - omt / 16)
    tn_nid = q * y / 4
    eta_nid = -fnu * y**2 / (6 * (4 * fnu + 15))
    dc_nid = -fnu * fb * y**2 * omt / (80 * fg)
    tn_niv = sp.Rational(3, 4) * q * (1 - y**2 * (4 * fnu + 9) / (6 * (4 * fnu + 5)))
    eta_niv = fnu * y * (-1 / (4 * fnu + 5) + (-sp.Rational(3, 64) * fb / fg + sp.Rational(15, 4) / (4 * fnu + 15) / (4 * fnu + 5)) * omt)
    dc_niv = -sp.Rational(9, 64) * fnu * fb * y * omt / fg
    modes = {
        "AD": (sp.Rational(3, 4) * dg_ad, sp.Rational(4, 3) * tn_ad / q, eta_ad),
        "CDI": (1 + sp.Rational(3, 4) * dg_cdi, sp.Rational(4, 3) * tn_cdi / q, eta_cdi),
        "BI": (sp.Rational(3, 4) * dg_bi, sp.Rational(4, 3) * tn_bi / q, eta_bi),
        "NID": (dc_nid, sp.Rational(4, 3) * tn_nid / q, eta_nid),
        "NIV": (dc_niv, sp.Rational(4, 3) * tn_niv / q, eta_niv),
    }
    checks: dict[str, bool] = {"source84_returned_qn_mapping_present": required}
    rows: dict[str, object] = {}
    niv_f2 = None
    for name, (dc, f1, eta) in modes.items():
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("P5.3g3 RERUN1 internal deadline exceeded")
        hy = -2 * sp.diff(dc, y)
        driving = sp.simplify(sp.Rational(2, 5) * f1 + sp.Rational(4, 15) * hy + sp.Rational(8, 5) * sp.diff(eta, y))
        f2_low = integrate_zero(driving, y)
        f3_first = integrate_zero(sp.Rational(3, 7) * f2_low, y)
        f2 = integrate_zero(driving - sp.Rational(3, 5) * f3_first, y)
        residual = sp.simplify(sp.diff(f2, y) - (driving - sp.Rational(3, 5) * f3_first))
        p2, p3 = lead_power(f2, y), lead_power(f3_first, y)
        checks.update({
            f"{name}_F2_at_origin_zero": bool(sp.simplify(f2.subs(y, 0)) == 0),
            f"{name}_F2_has_positive_leading_power": p2 is not None and p2 > 0,
            f"{name}_F3_starts_later_than_F2": p2 is not None and p3 is not None and p3 > p2,
            f"{name}_truncated_l2_residual_zero": bool(residual == 0),
        })
        rows[name] = {
            "F1_returned_qn": str(sp.factor(f1)),
            "F2_candidate": str(sp.factor(f2)),
            "F2_leading_power_in_y": p2,
            "F3_leading_power_in_y": p3,
            "l2_residual": str(residual),
        }
        if name == "NIV":
            niv_f2 = f2
    niv_leading = sp.expand(niv_f2).coeff(y, 1) if niv_f2 is not None else sp.nan
    expected_niv = 2 / (4 * fnu + 5)
    checks["NIV_F2_leading_matches_two_over_4fnu_plus_5"] = bool(sp.simplify(niv_leading - expected_niv) == 0)
    passed = all(checks.values())
    payload = {
        "test": "KMPC-017 P5.3g3 RERUN1 standard neutrino l=2 from returned qn",
        "scope": "source-bound corrected candidate derivation; no independent Einstein residual, photon TCA, ODE, score, or G8",
        "source84_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "checks": checks,
        "NIV_F2_leading": str(niv_leading),
        "NIV_sigma_leading": str(sp.simplify(niv_leading / 2)),
        "modes": rows,
        "next_step": "independent Einstein/constraint ledger plus photon l=2/TCA seed" if passed else "review corrected l=2 derivation before any P5.4 work",
        "verdict": "DERIVATION_PASS_P5_3G3_RERUN1_NEUTRINO_L2_QN" if passed else "REVIEW_BLOCKED_P5_3G3_RERUN1_NEUTRINO_L2_QN",
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
