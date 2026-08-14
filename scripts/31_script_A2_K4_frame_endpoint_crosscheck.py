#!/usr/bin/env python3
"""Cross-check that the general K4 transfer frame interpolates K1 and K3.

For theta_q=(1-beta)theta_c+beta theta_f, beta=0 must reproduce Q||u_c
and beta=1 must reproduce Q||u_f.  This is independent of the background
value beta=delta rho_f/(rho_c+delta rho_f) used by K4.
"""

from __future__ import annotations

import json

import sympy as sp


def zero(expr):
    return bool(sp.simplify(expr) == 0)


def main() -> int:
    gamma, r, d, beta = sp.symbols("gamma r d beta", positive=True)
    vc, vf = sp.symbols("vc vf")
    vd = (1-beta)*vc+beta*vf

    k4_c = gamma*r*(vd-vc)
    k4_f = gamma/d*(2*vf-vd)
    k1_c = 0
    k1_f = gamma/d*(2*vf-vc)
    k3_c = gamma*r*(vf-vc)
    k3_f = gamma/d*vf

    checks = {
        "beta_zero_cdm_is_K1": zero(k4_c.subs(beta, 0)-k1_c),
        "beta_zero_fuel_is_K1": zero(k4_f.subs(beta, 0)-k1_f),
        "beta_one_cdm_is_K3": zero(k4_c.subs(beta, 1)-k3_c),
        "beta_one_fuel_is_K3": zero(k4_f.subs(beta, 1)-k3_f),
        "relative_velocity_is_frame_invariant": zero(
            (vf-vd)+(vd-vc)-(vf-vc)
        ),
    }
    passed = all(checks.values())
    print(json.dumps({
        "test": "A2-K4 transfer-frame endpoint cross-check",
        "checks": checks,
        "status": "PASS" if passed else "FAIL",
    }, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

