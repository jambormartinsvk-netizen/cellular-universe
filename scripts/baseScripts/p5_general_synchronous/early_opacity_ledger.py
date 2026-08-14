"""Symbolic early-opacity and synchronous-constraint identities for P5.3g5.

The module is intentionally limited to the fully ionized radiation-era limit.
It is not a recombination calculation and cannot supply x_e(a) through
recombination.
"""

from __future__ import annotations

import sympy as sp


def early_opacity_identities() -> dict[str, sp.Expr]:
    """Return exact fully-ionized opacity/TCA expressions."""
    a, ne0, sigma_t, h_r, k = sp.symbols("a n_e0 sigma_T H_r k", positive=True)
    opacity = ne0 * sigma_t / a**2
    tau_c = 1 / opacity
    h_conf = h_r / a
    return {
        "a": a,
        "opacity": opacity,
        "tau_c": tau_c,
        "h_conf": h_conf,
        "hconf_tau_c": sp.simplify(h_conf * tau_c),
        "k_tau_c": sp.simplify(k * tau_c),
        "opacity_times_a_squared": sp.simplify(opacity * a**2),
    }


def synchronous_constraint_sources() -> dict[str, sp.Expr]:
    """Return independently assembled total sources for 00 and 0i constraints."""
    q, a, e, delta = sp.symbols("q a E delta", positive=True)
    eta, h_x, eta_x = sp.symbols("eta h_x eta_x")
    xc, xf, xb, xg, xn, xs = sp.symbols("Xc Xf Xb Xg Xn Xs", positive=True)
    dc, df, db, dg, dn, ds = sp.symbols("dc df db dg dn ds")
    uc, uf, ub, ug, un, us = sp.symbols("Uc Uf Ub Ug Un Us")
    drho = xc * dc + xf * df + xb * db + xg * dg + xn * dn + xs * ds
    momentum = xc * uc + delta * xf * uf + xb * ub + sp.Rational(4, 3) * (xg * ug + xn * un + xs * us)
    return {
        "C00": q**2 * eta - sp.Rational(1, 2) * (a * e) ** 2 * h_x + sp.Rational(3, 2) * a**2 * drho,
        "C0i": eta_x - sp.Rational(3, 2) * momentum / e**2,
        "drho": drho,
        "momentum": momentum,
        "Uc": uc,
        "Ub": ub,
        "Uf": uf,
        "Xc": xc,
        "Xb": xb,
        "Xf": xf,
        "delta": delta,
    }
