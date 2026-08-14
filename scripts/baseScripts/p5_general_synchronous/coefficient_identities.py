"""Exact symbolic identities shared by the bounded P5 static ledger."""

from __future__ import annotations

import sympy as sp


def build_identities() -> tuple[dict[str, sp.Expr], dict[str, sp.Expr]]:
    a, delta, lam, e, xr, xb, xc, xf, k, h0, or0 = sp.symbols(
        "a delta lambda E Xr Xb Xc Xf k H0 Omega_r0", positive=True
    )
    gamma = lam / e
    p = 4 - 3 * delta
    of = xf / e**2
    ob = xb / e**2
    oc = xc / e**2
    ell = (4 - 3 * delta) * of + ob + oc
    beta_c = 1 + gamma * xf / xc
    beta_f = p - gamma
    xcx = -3 * xc + gamma * xf
    xfx = -3 * delta * xf - gamma * xf
    c_c = a**4 * xc
    c_f = a**4 * xf
    s2 = k**2 * a**2 / (h0**2 * or0 * sp.Symbol("D_A1", positive=True))
    beta_d = delta * xf / (xc + delta * xf)
    uc, uf, ub, ug, un = sp.symbols("Uc Uf Ub Ug Un")
    ud = (1 - beta_d) * uc + beta_d * uf
    m_full = 2 * sp.Symbol("Og") * ug + 2 * sp.Symbol("On") * un + sp.Rational(3, 2) * ob * ub + sp.Rational(3, 2) * oc * uc + sp.Rational(3, 2) * delta * of * uf
    identities = {
        "paired_background_transfer": sp.Symbol("Q") - sp.Symbol("Q"),
        "xc_scaled_derivative": (4 * xc + xcx) - beta_c * xc,
        "xf_scaled_derivative": (4 * xf + xfx) - beta_f * xf,
        "ell_from_total_derivative": ell - ((4 - 3 * delta) * xf + xb + xc) / e**2,
        "energy_frame_definition": ud - ((xc * uc + delta * xf * uf) / (xc + delta * xf)),
        "radiation_gamma_limit": gamma.subs(e, sp.sqrt(or0) / a**2) - lam * a**2 / sp.sqrt(or0),
    }
    metadata = {
        "background_ell": ell,
        "gamma": gamma,
        "beta_c": beta_c,
        "beta_f": beta_f,
        "s2": s2,
        "m_full": m_full,
        "k": k,
    }
    return identities, metadata
