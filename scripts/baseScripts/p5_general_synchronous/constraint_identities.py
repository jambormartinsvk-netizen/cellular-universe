"""Exact structural constraints for P5.2; no ODE or numerical evolution."""

from __future__ import annotations

import sympy as sp


def build_constraint_identities() -> tuple[dict[str, sp.Expr], dict[str, sp.Expr]]:
    a, e, q, hc, delta, gamma = sp.symbols("a E q hc delta gamma", nonzero=True)
    xc, xf, xb, xg, xn, xs = sp.symbols("Xc Xf Xb Xg Xn Xs")
    uc, uf, ub, ug, un, us = sp.symbols("Uc Uf Ub Ug Un Us")
    eta, hx, etax, hxx, etaxx = sp.symbols("eta hx eta_x hx_x eta_xx")
    density, pressure, shear, dx, mx = sp.symbols("D P S D_x M_x")
    ae2 = (a * e) ** 2
    momentum = xc * uc + delta * xf * uf + xb * ub + sp.Rational(4, 3) * (xg * ug + xn * un + xs * us)
    enthalpy = xc + delta * xf + xb + sp.Rational(4, 3) * (xg + xn + xs)
    s2 = sp.symbols("s2")
    hx_from_00 = 2 * (q**2 * eta + sp.Rational(3, 2) * a**2 * density) / ae2
    etax_from_0i = sp.Rational(3, 2) * momentum / e**2
    hxx_from_trace = (2 * q**2 * eta - 9 * a**2 * pressure) / ae2 - (hc + 2) * hx
    etaxx_from_traceless = (
        (2 * q**2 * eta - 9 * a**2 * shear) / ae2
        - hxx
        - (hc + 2) * (hx + 6 * etax)
    ) / 6
    w = enthalpy
    dx_expected = -3 * (density + pressure) - s2 * momentum - sp.Rational(1, 2) * hx * w
    mx_expected = (hc - 4) * momentum + pressure - shear
    transfer_background = sp.Symbol("Q") - sp.Symbol("Q")
    uc_transfer = gamma * xf / xc * sp.Symbol("beta") * (uf - uc)
    uf_transfer = gamma / delta * (2 * uf - sp.Symbol("Ud"))
    identities = {
        "full_momentum_species_content": momentum - (xc * uc + delta * xf * uf + xb * ub + sp.Rational(4, 3) * (xg * ug + xn * un + xs * us)),
        "constraint_00_reconstruction": (q**2 * eta - sp.Rational(1, 2) * ae2 * hx + sp.Rational(3, 2) * a**2 * density).subs(hx, hx_from_00),
        "constraint_0i_reconstruction": (etax - sp.Rational(3, 2) * momentum / e**2).subs(etax, etax_from_0i),
        "constraint_trace_reconstruction": (ae2 * (hxx + (hc + 2) * hx) - 2 * q**2 * eta + 9 * a**2 * pressure).subs(hxx, hxx_from_trace),
        "constraint_traceless_reconstruction": (ae2 * (hxx + 6 * etaxx + (hc + 2) * (hx + 6 * etax)) - 2 * q**2 * eta + 9 * a**2 * shear).subs(etaxx, etaxx_from_traceless),
        "energy_product_ledger": dx - dx_expected,
        "momentum_product_ledger": mx - mx_expected,
        "paired_transfer_cancels": transfer_background,
        "uc_transfer_vanishes_gamma_zero": uc_transfer.subs(gamma, 0),
        "uf_transfer_vanishes_gamma_zero": uf_transfer.subs(gamma, 0),
        "photon_baryon_slip_definition": (sp.Symbol("Slip") - (ug - ub)).subs(sp.Symbol("Slip"), ug - ub),
    }
    metadata = {
        "momentum": momentum,
        "enthalpy": enthalpy,
        "hx_from_00": hx_from_00,
        "etax_from_0i": etax_from_0i,
        "hxx_from_trace": hxx_from_trace,
        "etaxx_from_traceless": etaxx_from_traceless,
        "dx_expected": dx_expected,
        "mx_expected": mx_expected,
        "state_symbols": (uc, uf, ub, ug, un, us),
        "slip_raw": sp.Symbol("Slip") - (ug - ub),
    }
    return identities, metadata
