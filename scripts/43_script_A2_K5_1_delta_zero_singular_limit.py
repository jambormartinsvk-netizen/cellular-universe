#!/usr/bin/env python3
"""Exact scaling audit of the K5/K1 delta->0 limit at fixed transfer.

At fixed positive X_f, X_c, E, and nonzero lambda,

  varphi_x = sqrt(3 delta X_f)/E        proportional sqrt(delta),
  beta = lambda sqrt(X_f)/(X_c sqrt(3 delta)) proportional 1/sqrt(delta),

while beta*varphi_x=lambda X_f/(E X_c) remains finite.  The background
transfer therefore survives only through a divergent conformal coupling.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys


BASE_PATH = Path(__file__).with_name(
    "13_script_A1_K1_cdm_background_audit_exact_zstar.py"
)
SPEC = importlib.util.spec_from_file_location("k5_delta_limit_background", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load validated background: {BASE_PATH}")
BASE13 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE13
SPEC.loader.exec_module(BASE13)


def main() -> int:
    p = BASE13.BASE.ModelParameters()
    xf = 1.0-p.omega_m0-BASE13.BASE.omega_radiation_today(p)
    _, xb0 = BASE13.BASE.initial_state(p)
    xc = p.omega_m0-xb0
    e = 1.0

    deltas = [p.delta, p.delta/1.0e2, p.delta/1.0e4, p.delta/1.0e6]
    rows = []
    for delta in deltas:
        varphi_x = (3.0*delta*xf)**0.5/e
        beta = p.lam*xf**0.5/(xc*(3.0*delta)**0.5)
        rows.append({
            "delta": delta,
            "varphi_x": varphi_x,
            "beta": beta,
            "beta_varphi_x": beta*varphi_x,
        })

    beta_ratios = [rows[i+1]["beta"]/rows[i]["beta"] for i in range(3)]
    velocity_ratios = [
        rows[i+1]["varphi_x"]/rows[i]["varphi_x"] for i in range(3)
    ]
    product_spread = max(r["beta_varphi_x"] for r in rows)-min(
        r["beta_varphi_x"] for r in rows
    )
    checks = {
        "beta_grows_by_10_for_delta_divided_by_100": all(
            abs(r-10.0) < 1.0e-12 for r in beta_ratios
        ),
        "varphi_x_shrinks_by_10_for_delta_divided_by_100": all(
            abs(r-0.1) < 1.0e-12 for r in velocity_ratios
        ),
        "background_transfer_product_constant": product_spread < 1.0e-14,
    }
    passed = all(checks.values())
    output = {
        "test": "A2-K5.1 exact delta->0 singular-limit scaling",
        "fixed_quantities": {
            "lambda": p.lam,
            "X_f_today": xf,
            "X_c_today": xc,
            "E_today": e,
        },
        "rows": rows,
        "successive_beta_ratios": beta_ratios,
        "successive_varphi_x_ratios": velocity_ratios,
        "beta_varphi_x_spread": product_spread,
        "checks": checks,
        "status": "PASS_SINGULAR_LIMIT_CONFIRMED" if passed else "FAIL",
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
