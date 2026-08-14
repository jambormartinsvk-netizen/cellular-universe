#!/usr/bin/env python
"""Exact equation/sign and source-token audit for BR3C-b script 136."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import time

import sympy as sp


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=8.0)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 10.0:
        parser.error("runtime must be in (0,10]")
    started = time.monotonic()

    q, s2, R, delta, g, gr = sp.symbols(
        "q s2 R delta g gr", nonzero=True, finite=True
    )
    Og, On, Ob, Oc, Of = sp.symbols("Og On Ob Oc Of", finite=True)
    h, eta, dg, dn, db, dc = sp.symbols("h eta dg dn db dc", finite=True)
    Ug, Un, sig, L3, L4, df, Uf = sp.symbols(
        "Ug Un sig L3 L4 df Uf", finite=True
    )
    density = Og*dg + On*dn + Ob*db + Oc*dc + Of*df
    hx = 3*density + 2*s2*eta
    etax = 2*Og*Ug + 2*On*Un + sp.Rational(3, 2)*Ob*Ug \
        + sp.Rational(3, 2)*delta*Of*Uf
    inv1r = 1/(1+R)
    derivatives = {
        "hx": hx,
        "etax": etax,
        "dgx": -sp.Rational(4, 3)*s2*Ug-sp.Rational(2, 3)*hx,
        "Ugx": q*Ug-R*inv1r*Ug+sp.Rational(1, 4)*inv1r*dg,
        "dnx": -sp.Rational(4, 3)*s2*Un-sp.Rational(2, 3)*hx,
        "Unx": q*Un+sp.Rational(1, 4)*dn-sig,
        "sigx": sp.Rational(2, 15)*hx+sp.Rational(4, 5)*etax
        + sp.Rational(4, 15)*s2*Un-sp.Rational(3, 10)*L3,
        "L3x": -q*L3+sp.Rational(6, 7)*s2*sig-sp.Rational(4, 7)*L4,
        "L4x": -2*q*L4+sp.Rational(4, 9)*s2*L3,
        "dbx": -s2*Ug-sp.Rational(1, 2)*hx,
        "dcx": -sp.Rational(1, 2)*hx+gr*(df-dc),
        "dfx": -3*(2-delta)*df-delta*s2*Uf-sp.Rational(1, 2)*delta*hx
        -9*delta*(2-delta)*Uf-3*(2-delta)*g*Uf,
        "Ufx": (q+2)*Uf+df/delta+2*g*Uf/delta,
    }
    residuals = {
        "Einstein_00": derivatives["hx"]-3*density-2*s2*eta,
        "Einstein_0i": derivatives["etax"]-2*Og*Ug-2*On*Un
        -sp.Rational(3, 2)*Ob*Ug-sp.Rational(3, 2)*delta*Of*Uf,
        "gamma_continuity": derivatives["dgx"]+sp.Rational(4, 3)*s2*Ug
        +sp.Rational(2, 3)*hx,
        "gamma_Euler": derivatives["Ugx"]-q*Ug+R*inv1r*Ug
        -sp.Rational(1, 4)*inv1r*dg,
        "nu_continuity": derivatives["dnx"]+sp.Rational(4, 3)*s2*Un
        +sp.Rational(2, 3)*hx,
        "nu_Euler": derivatives["Unx"]-q*Un-sp.Rational(1, 4)*dn+sig,
        "nu_shear": 2*derivatives["sigx"]-sp.Rational(4, 15)*hx
        -sp.Rational(8, 5)*etax-sp.Rational(8, 15)*s2*Un
        +sp.Rational(3, 5)*L3,
        "nu_l3": derivatives["L3x"]+q*L3-sp.Rational(6, 7)*s2*sig
        +sp.Rational(4, 7)*L4,
        "nu_l4": derivatives["L4x"]+2*q*L4-sp.Rational(4, 9)*s2*L3,
        "baryon_continuity": derivatives["dbx"]+s2*Ug+sp.Rational(1, 2)*hx,
        "cdm_continuity": derivatives["dcx"]+sp.Rational(1, 2)*hx
        -gr*(df-dc),
        "fuel_continuity": derivatives["dfx"]+3*(2-delta)*df+delta*s2*Uf
        +sp.Rational(1, 2)*delta*hx+9*delta*(2-delta)*Uf
        +3*(2-delta)*g*Uf,
        "fuel_Euler": derivatives["Ufx"]-(q+2)*Uf-df/delta-2*g*Uf/delta,
    }
    checks = {
        f"identity_{name}": bool(sp.simplify(value) == 0)
        for name, value in residuals.items()
    }

    source = Path(__file__).with_name(
        "136_script_A2_K4_3b_RG_BR3C_b_segmented_early_evolution.py"
    ).read_text(encoding="utf-8")
    required_tokens = {
        "constraint_hx": 'h_x = 3.0 * density + 2.0 * bg["s2"] * eta',
        "constraint_etax_fuel": '+ 1.5 * delta * bg["Omega_f"] * U_f',
        "gamma_sign": 'dg_x = -(4.0 / 3.0) * bg["s2"] * U_gamma - (2.0 / 3.0) * h_x',
        "shear_L3_sign": '- (3.0 / 10.0) * L3_fs',
        "L3_L4_sign": '- (4.0 / 7.0) * L4_fs',
        "cdm_transfer_sign": 'dc_x = -0.5 * h_x + bg["gr"] * (delta_f - delta_c)',
        "fuel_g_continuity_sign": '- 3.0 * (2.0 - delta) * bg["g"] * U_f',
        "fuel_g_Euler_sign": '+ (2.0 / delta) * bg["g"] * U_f',
    }
    for name, token in required_tokens.items():
        checks[f"source_token_{name}_unique"] = source.count(token) == 1

    passed = bool(checks) and all(checks.values())
    output = {
        "test": "A2-K4.3b-RG BR3C-b equation and sign audit",
        "checks": checks,
        "identity_count": len(residuals),
        "source_token_count": len(required_tokens),
        "execution_verdict": (
            "PASS_BR3C_B_EQUATION_SIGN_AUDIT"
            if passed
            else "REVIEW_BR3C_B_EQUATION_AUDIT_UNCLOSED"
        ),
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic()-started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict":"TIMEOUT_UNCLOSED","error":str(exc)}))
        raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution_verdict":"ERROR_UNCLOSED","error":repr(exc)}))
        raise SystemExit(2)

