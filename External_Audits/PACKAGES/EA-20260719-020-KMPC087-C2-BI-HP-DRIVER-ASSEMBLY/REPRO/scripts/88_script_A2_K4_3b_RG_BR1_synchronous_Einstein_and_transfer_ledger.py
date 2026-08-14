#!/usr/bin/env python
"""A2-K4.3b-RG-BR1: synchronous Einstein and K4 transfer ledger.

This is a symbolic sign/null/conservation audit.  It fixes one convention for
the scalar synchronous metric, converts the four Ma--Bertschinger Einstein
equations to x=ln(a), and verifies that the established K4 fluid equations
conserve the *total* perturbed stress-energy tensor.

It does not solve the back-reacted Puiseux coefficients.  A PASS here is only
permission to build BR2; it cannot close K4.3b or canonical gate G7.
"""

from __future__ import annotations

import argparse
import json
import time

import sympy as sp


def zero(expr: sp.Expr) -> bool:
    return bool(sp.simplify(sp.factor(expr)) == 0)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=8.0)
    args = parser.parse_args()
    if not (0.0 < args.max_runtime_seconds <= 10.0):
        parser.error("--max-runtime-seconds must be in (0,10]")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("BR1 symbolic deadline exceeded")

    # Background and perturbation symbols. X_A=rho_A/rho_crit,0 and
    # U_A=Hconf*theta_A/k^2.  The fuel has w_f=-1+d and rest sound speed 1.
    d, g, s2, hc = sp.symbols("d g s2 hc", positive=True)
    Xc, Xf, Xb = sp.symbols("Xc Xf Xb", positive=True)
    Xg, Xn, Xs = sp.symbols("Xg Xn Xs", positive=True)
    dc, df, db, dg, dn, ds = sp.symbols("dc df db dg dn ds")
    Uc, Uf, Ub, Ug, Un, Us = sp.symbols("Uc Uf Ub Ug Un Us")
    sg, sn, ss = sp.symbols("sg sn ss")
    hx = sp.symbols("hx")

    r = Xf / Xc
    beta = sp.simplify(d * Xf / (Xc + d * Xf))
    Ud = sp.simplify((1 - beta) * Uc + beta * Uf)

    # Exact background ledger in x=ln(a), for fuel -> ash at g=Gamma/H.
    Xc_x = -3 * Xc + g * Xf
    Xf_x = -(3 * d + g) * Xf
    Xb_x = -3 * Xb
    Xg_x = -4 * Xg
    Xn_x = -4 * Xn
    Xs_x = -4 * Xs

    # Full K4 dark-sector equations in general synchronous gauge A=0.
    dc_x = -s2 * Uc - hx / 2 + g * r * (df - dc)
    Uc_x = (hc - 1) * Uc + g * r * beta * (Uf - Uc)
    df_x = (
        -3 * (2 - d) * df
        - d * (s2 * Uf + hx / 2)
        - 9 * d * (2 - d) * Uf
        - 3 * g * (2 - d) * Uf
    )
    Uf_x = (hc + 2) * Uf + df / d + g / d * (2 * Uf - Ud)

    # Standard uncoupled species, written only to prove the total ledger.
    db_x = -s2 * Ub - hx / 2
    Ub_x = (hc - 1) * Ub
    dg_x = -sp.Rational(4, 3) * s2 * Ug - sp.Rational(2, 3) * hx
    dn_x = -sp.Rational(4, 3) * s2 * Un - sp.Rational(2, 3) * hx
    ds_x = -sp.Rational(4, 3) * s2 * Us - sp.Rational(2, 3) * hx
    Ug_x = hc * Ug + dg / 4 - sg
    Un_x = hc * Un + dn / 4 - sn
    Us_x = hc * Us + ds / 4 - ss

    # The interaction-dependent non-adiabatic fuel pressure is compulsory.
    # delta p_f/rho_f = df + (c_s^2-c_a^2)(3(1+w)+g)U_f.
    Pf = sp.simplify(Xf * (df + (2 - d) * (3 * d + g) * Uf))
    Drho = Xc * dc + Xf * df + Xb * db + Xg * dg + Xn * dn + Xs * ds
    Dpress = Pf + (Xg * dg + Xn * dn + Xs * ds) / 3
    Momentum = (
        Xc * Uc
        + d * Xf * Uf
        + Xb * Ub
        + sp.Rational(4, 3) * (Xg * Ug + Xn * Un + Xs * Us)
    )
    Shear = sp.Rational(4, 3) * (Xg * sg + Xn * sn + Xs * ss)

    # Absolute density perturbation derivatives.  The +g Xf df and
    # -g Xf df transfer terms must cancel only after the background product
    # rule is included; comparing fractional equations alone is misleading.
    Dc_x = sp.expand(Xc_x * dc + Xc * dc_x)
    Df_x = sp.expand(Xf_x * df + Xf * df_x)
    Db_x = sp.expand(Xb_x * db + Xb * db_x)
    Dg_x = sp.expand(Xg_x * dg + Xg * dg_x)
    Dn_x = sp.expand(Xn_x * dn + Xn * dn_x)
    Ds_x = sp.expand(Xs_x * ds + Xs * ds_x)
    Drho_x = sp.expand(Dc_x + Df_x + Db_x + Dg_x + Dn_x + Ds_x)
    total_energy_expected = -3 * (Drho + Dpress) - s2 * Momentum - hx * (
        Xc / 2 + d * Xf / 2 + Xb / 2
        + sp.Rational(2, 3) * (Xg + Xn + Xs)
    )

    # Momentum product-rule audit.  The apparent residual g(2-d)Xf Uf in
    # the Euler equations is precisely the g-dependent part of delta p_f.
    Mc_x = sp.expand(Xc_x * Uc + Xc * Uc_x)
    Mf_x = sp.expand(d * Xf_x * Uf + d * Xf * Uf_x)
    Mb_x = sp.expand(Xb_x * Ub + Xb * Ub_x)
    Mg_x = sp.expand(sp.Rational(4, 3) * (Xg_x * Ug + Xg * Ug_x))
    Mn_x = sp.expand(sp.Rational(4, 3) * (Xn_x * Un + Xn * Un_x))
    Ms_x = sp.expand(sp.Rational(4, 3) * (Xs_x * Us + Xs * Us_x))
    Momentum_x = sp.expand(Mc_x + Mf_x + Mb_x + Mg_x + Mn_x + Ms_x)
    total_momentum_expected = (hc - 4) * Momentum + Dpress - Shear

    deadline()

    # Convert the four flat synchronous Einstein equations from conformal
    # time to x.  q=k/H0, Hconf=a E H0, rho_crit,0=3H0^2/(8 pi G).
    a, E, q = sp.symbols("a E q", positive=True)
    eta, etax, etaxx, hxx = sp.symbols("eta etax etaxx hxx")
    C00 = q**2 * eta - sp.Rational(1, 2) * (a * E) ** 2 * hx + sp.Rational(3, 2) * a**2 * Drho
    C0i = etax - sp.Rational(3, 2) * Momentum / E**2
    Ctr = (
        (a * E) ** 2 * (hxx + (hc + 2) * hx)
        - 2 * q**2 * eta
        + 9 * a**2 * Dpress
    )
    Ctl = (
        (a * E) ** 2
        * (hxx + 6 * etaxx + (hc + 2) * (hx + 6 * etax))
        - 2 * q**2 * eta
        + 9 * a**2 * Shear
    )

    # A direct algebraic conformal-time conversion check for all coefficients.
    H0, Hconf, k = sp.symbols("H0 Hconf k", positive=True)
    fourpiGa2rhoc = sp.Rational(3, 2) * H0**2 * a**2
    raw00 = k**2 * eta - Hconf**2 * hx / 2 + fourpiGa2rhoc * Drho
    raw0i = k**2 * Hconf * etax - fourpiGa2rhoc * k**2 * Momentum / Hconf
    rawtr = Hconf**2 * (hxx + (hc + 2) * hx) - 2 * k**2 * eta + 6 * fourpiGa2rhoc * Dpress
    rawtl = (
        Hconf**2 * (hxx + 6 * etaxx + (hc + 2) * (hx + 6 * etax))
        - 2 * k**2 * eta
        + 6 * fourpiGa2rhoc * Shear
    )
    repl = {k: q * H0, Hconf: a * E * H0}

    # Two internal nu--steam modes are metric-null when every weighted
    # hierarchy moment cancels.  Density, pressure, momentum and shear are
    # the first four source projections.
    z0, z1, z2 = sp.symbols("z0 z1 z2")
    internal = {
        dn: z0,
        ds: -Xn * z0 / Xs,
        Un: z1,
        Us: -Xn * z1 / Xs,
        sn: z2,
        ss: -Xn * z2 / Xs,
        dg: 0,
        Ug: 0,
        sg: 0,
        dc: 0,
        df: 0,
        db: 0,
        Uc: 0,
        Uf: 0,
        Ub: 0,
    }

    # Null-limit equations retained explicitly as a regression target.
    standard_null = {
        "dc": -s2 * Uc - hx / 2,
        "Uc": (hc - 1) * Uc,
        "df": -3 * (2 - d) * df - d * (s2 * Uf + hx / 2) - 9 * d * (2 - d) * Uf,
        "Uf": (hc + 2) * Uf + df / d,
    }

    checks = {
        "background_energy_transfer_pair_cancels": zero((Xc_x + 3 * Xc) + (Xf_x + 3 * d * Xf)),
        "theta_d_is_enthalpy_weighted": zero(Ud - (Xc * Uc + d * Xf * Uf) / (Xc + d * Xf)),
        "ash_absolute_deltaQ_is_plus_g_Xf_df": zero(Dc_x - (-3 * Xc * dc - Xc * (s2 * Uc + hx / 2) + g * Xf * df)),
        "fuel_absolute_deltaQ_is_minus_g_Xf_df": zero(Df_x - (-3 * (Xf * df + Pf) - d * Xf * (s2 * Uf + hx / 2) - g * Xf * df)),
        "total_perturbed_energy_conserved": zero(Drho_x - total_energy_expected),
        "total_perturbed_momentum_conserved": zero(Momentum_x - total_momentum_expected),
        "fuel_pressure_contains_required_g_piece": zero(sp.diff(Pf, g) - Xf * (2 - d) * Uf),
        "lambda_zero_dc_standard": zero(dc_x.subs(g, 0) - standard_null["dc"]),
        "lambda_zero_Uc_standard": zero(Uc_x.subs(g, 0) - standard_null["Uc"]),
        "lambda_zero_df_standard": zero(df_x.subs(g, 0) - standard_null["df"]),
        "lambda_zero_Uf_standard": zero(Uf_x.subs(g, 0) - standard_null["Uf"]),
        "00_conformal_to_x": zero(raw00.subs(repl) / H0**2 - C00),
        "0i_conformal_to_x": zero(raw0i.subs(repl) / (q**2 * a * E * H0**3) - C0i),
        "trace_ij_conformal_to_x": zero(rawtr.subs(repl) / H0**2 - Ctr),
        "traceless_ij_conformal_to_x": zero(rawtl.subs(repl) / H0**2 - Ctl),
        "internal_mode_density_source_zero": zero(Drho.subs(internal)),
        "internal_mode_pressure_source_zero": zero(Dpress.subs(internal)),
        "internal_mode_momentum_source_zero": zero(Momentum.subs(internal)),
        "internal_mode_shear_source_zero": zero(Shear.subs(internal)),
    }
    deadline()

    passed = all(checks.values())
    output = {
        "test": "A2-K4.3b-RG-BR1 synchronous Einstein and transfer ledger",
        "metric_convention": "ds^2=a^2[-deta^2+(delta_ij+h_ij)dx^i dx^j], h_ij=khat_i khat_j h+6(khat_i khat_j-delta_ij/3)eta_s",
        "variable_convention": "x=ln(a), q=k/H0, U_A=Hconf*theta_A/k^2, w_f=-1+delta, cs_f^2=1",
        "transfer_convention": "Q_c^mu=+Gamma rho_f u_d^mu, Q_f^mu=-Gamma rho_f u_d^mu, u_d enthalpy weighted",
        "fuel_pressure_over_rhocrit0": str(Pf),
        "einstein_residuals": {
            "00": str(C00),
            "0i": str(C0i),
            "trace_ij": str(Ctr),
            "traceless_ij": str(Ctl),
        },
        "checks": checks,
        "execution_verdict": "PASS_BR1_FORMULATION_LEDGER" if passed else "FAIL_BR1_FORMULATION_LEDGER",
        "K4_3b_RG_verdict": "NEUZAVRETA_BACKREACTED_PUISEUX_COEFFICIENTS_MISSING",
        "canonical_score": "60/100 = G6",
        "next_step": "BR2 solve the coupled Puiseux coefficients and test all four residuals at two depths",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
    print(json.dumps(output, indent=2, ensure_ascii=False, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
