#!/usr/bin/env python3
"""A2-K6.1: exact high-k G_ij and growth gate for energy+momentum transfer.

The audited action is, in the conventions of Kase & Tsujikawa (2020),

    G2 = X - V(phi),
    f  = -f1(phi) rho_c + eta Z^2,
    Z  = u_c^mu partial_mu phi.

The density called rho_c in that paper is the bare Schutz-Sorkin density.
The A1 background uses the physical/effective density

    rho_c_hat = A rho_c,  A = 1 + f1.

Consequently the paper's G_cc and G_bc must be divided by A before they
are interpreted as couplings multiplying rho_c_hat.  Missing this mapping
would manufacture a false suppression/enhancement.

This script reconstructs the validated A1 background, evaluates q_c,
beta_nc, the exact quasi-static r1/r2 expressions and all four G_ij,
checks both algebraic null limits, and integrates the resulting high-k
two-fluid growth system as a diagnostic.  The growth diagnostic begins at
z=100 and is not a CMB likelihood or a Boltzmann calculation.

Primary formula source: arXiv:2005.13809, especially Eqs. (5.17)-(5.24).
"""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path
import sys

import numpy as np


BASE_PATH = Path(__file__).with_name(
    "13_script_A1_K1_cdm_background_audit_exact_zstar.py"
)
SPEC = importlib.util.spec_from_file_location("a1_background_k6", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load validated A1 background: {BASE_PATH}")
BASE13 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE13
SPEC.loader.exec_module(BASE13)


ETA_GRID = (0.0, 0.1, 0.5, 1.0, 2.0, 5.0)
Z_GROWTH_INITIAL = 100.0


def cumulative_trapezoid(values: np.ndarray, xs: np.ndarray) -> np.ndarray:
    out = np.zeros_like(values)
    out[1:] = np.cumsum(0.5 * (values[1:] + values[:-1]) * np.diff(xs))
    return out


def log_derivative(values: np.ndarray, xs: np.ndarray) -> np.ndarray:
    if np.any(values <= 0.0):
        raise ValueError("log_derivative received a non-positive value")
    return np.gradient(np.log(values), xs, edge_order=2)


def reconstruct(eta: float, step: float) -> dict[str, np.ndarray | float]:
    if eta < 0.0:
        raise ValueError("The preregistered K6.1 gate uses eta >= 0")

    p = BASE13.BASE.ModelParameters()
    x_star = -math.log1p(p.z_star)
    settings = BASE13.BASE.IntegrationSettings(x_min=x_star, step=step)
    xs_desc, states_desc, xb0 = BASE13.integrate_background(p, settings)
    xs = xs_desc[::-1]
    states = states_desc[::-1]
    xf, xm, xr = states.T
    xb = xb0 * np.exp(-3.0 * xs)
    xchat = xm - xb
    e2 = xf + xm + xr
    e = np.sqrt(e2)

    # Exact A1 coupling reconstruction.  s=d ln A/dx is fixed by the
    # already-audited energy transfer and is eta independent.
    s = p.lam * xf / (e * xchat)
    ln_a = cumulative_trapezoid(s, xs)
    ln_a -= ln_a[-1]
    coupling_a = np.exp(ln_a)
    f1 = coupling_a - 1.0

    # varphi=phi/Mpl.  The eta Z^2 term rescales the background kinetic term.
    varphi_x2 = 3.0 * p.delta * xf / ((1.0 + 2.0 * eta) * e2)
    varphi_x = np.sqrt(varphi_x2)

    # Work in H0=Mpl=1 units.  rho_hat=3*xchat and dotphi=H*varphi_x.
    rho_hat = 3.0 * xchat
    h = e
    dotphi = h * varphi_x
    f1_phi = coupling_a * s / varphi_x
    f2_z = 2.0 * eta * dotphi

    beta_nc = -f1
    q_c = coupling_a + dotphi * f2_z / (rho_hat / coupling_a)
    delta2 = 0.5 * varphi_x2
    delta3 = coupling_a * s

    eps_h = log_derivative(h, xs)
    eps_qc = log_derivative(q_c, xs)
    eps_delta2 = log_derivative(delta2, xs)
    eps_delta3 = log_derivative(delta3, xs)

    # Scalar no-ghost and propagation coefficients.
    qs_over_2mpl2 = np.full_like(xs, 1.0 + 2.0 * eta)
    hat_cs2 = np.full_like(xs, 1.0 / (1.0 + 2.0 * eta))
    cs2_over_hat = 1.0 + f2_z**2 / (rho_hat + dotphi * f2_z)
    cs2 = hat_cs2 * cs2_over_hat

    # Exact r1/r2 for alpha_B=alpha_M=0, G2_X=1, f2_X=0.
    c_bracket = 1.0 - eps_qc + eps_h + eps_delta2 - eps_delta3
    r1 = (
        -2.0
        * h
        * f1_phi
        / rho_hat
        * (f2_z * c_bracket - rho_hat * eps_qc / dotphi)
    )
    r2 = (dotphi * f2_z + f2_z**2) / rho_hat

    # Couplings as printed in the paper: CDM source is the bare rho_c.
    paper_gcc = (coupling_a + r1) / (1.0 + r2)
    paper_gcb = 1.0 / (1.0 + r2)
    paper_gbc = coupling_a
    paper_gbb = np.ones_like(xs)

    # Couplings multiplying the physical A1 density rho_hat=A*rho_c.
    mu_cc = paper_gcc / coupling_a
    mu_cb = paper_gcb
    mu_bc = paper_gbc / coupling_a
    mu_bb = paper_gbb

    # CDM high-k friction coefficient c1 in
    # ddot(delta_c)+c1 H dot(delta_c)=sources.  eta=0 is the regular
    # conformal limit of the general expression (the raw form is 0/0).
    if eta == 0.0:
        c1 = 2.0 + eps_qc
    else:
        hat_over_cs = 1.0 / cs2_over_hat
        denominator = 1.0 - beta_nc - q_c
        mixing_piece = (2.0 * delta3 - 2.0 * q_c * eps_qc) / denominator
        c1 = (
            (2.0 + eps_qc) * hat_over_cs
            + (
                mixing_piece
                - 1.0
                - eps_delta2
                - 2.0 * eps_h
            )
            * (1.0 - hat_over_cs)
        )

    return {
        "eta": eta,
        "xs": xs,
        "xf": xf,
        "xm": xm,
        "xr": xr,
        "xb": xb,
        "xchat": xchat,
        "e": e,
        "A": coupling_a,
        "s": s,
        "varphi_x": varphi_x,
        "beta_nc": beta_nc,
        "q_c": q_c,
        "delta2": delta2,
        "delta3": delta3,
        "eps_h": eps_h,
        "eps_qc": eps_qc,
        "eps_delta2": eps_delta2,
        "eps_delta3": eps_delta3,
        "qs_over_2mpl2": qs_over_2mpl2,
        "hat_cs2": hat_cs2,
        "cs2": cs2,
        "r1": r1,
        "r2": r2,
        "paper_gcc": paper_gcc,
        "paper_gcb": paper_gcb,
        "paper_gbc": paper_gbc,
        "paper_gbb": paper_gbb,
        "mu_cc": mu_cc,
        "mu_cb": mu_cb,
        "mu_bc": mu_bc,
        "mu_bb": mu_bb,
        "c1": c1,
    }


def interp(arr: np.ndarray, x: float, xs: np.ndarray) -> float:
    return float(np.interp(x, xs, arr))


def growth_rhs(x: float, y: np.ndarray, data: dict) -> np.ndarray:
    xs = data["xs"]
    eps_h = interp(data["eps_h"], x, xs)
    c1 = interp(data["c1"], x, xs)
    mu_cc = interp(data["mu_cc"], x, xs)
    mu_cb = interp(data["mu_cb"], x, xs)
    e2 = interp(data["e"] ** 2, x, xs)
    omega_chat = interp(data["xchat"], x, xs) / e2
    omega_b = interp(data["xb"], x, xs) / e2
    dc, vc, db, vb = y
    return np.array(
        [
            vc,
            -(c1 + eps_h) * vc
            + 1.5 * (mu_cc * omega_chat * dc + mu_cb * omega_b * db),
            vb,
            -(2.0 + eps_h) * vb
            + 1.5 * (omega_chat * dc + omega_b * db),
        ]
    )


def integrate_growth(data: dict) -> dict[str, float]:
    xs_all = data["xs"]
    x0 = -math.log1p(Z_GROWTH_INITIAL)
    xs = xs_all[xs_all >= x0]
    if xs[0] > x0 + 1.0e-12:
        xs = np.concatenate(([x0], xs))
    y = np.array([1.0, 1.0, 1.0, 1.0])
    for xa, xb in zip(xs[:-1], xs[1:]):
        dx = xb - xa
        xm = 0.5 * (xa + xb)
        k1 = growth_rhs(xa, y, data)
        k2 = growth_rhs(xm, y + 0.5 * dx * k1, data)
        k3 = growth_rhs(xm, y + 0.5 * dx * k2, data)
        k4 = growth_rhs(xb, y + dx * k3, data)
        y += dx * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
    dc, vc, db, vb = y
    xchat0 = float(data["xchat"][-1])
    xb0 = float(data["xb"][-1])
    xm0 = float(data["xm"][-1])
    dm = (xchat0 * dc + xb0 * db) / xm0
    return {
        "delta_c_today": float(dc),
        "delta_b_today": float(db),
        "delta_m_today": float(dm),
        "d_delta_c_dx_today": float(vc),
        "d_delta_b_dx_today": float(vb),
    }


def summarize(data: dict) -> dict[str, float | bool]:
    xs = data["xs"]
    late = xs >= -math.log1p(10.0)
    beta = data["s"] / data["varphi_x"]
    expected_eta0 = 1.0 + 2.0 * beta**2
    eta = float(data["eta"])

    # Algebraic pure-momentum limit f1->0: r1=0 and A=1.  The two
    # independently derived expressions must coincide.
    pure_momentum_from_r2 = 1.0 / (1.0 + data["r2"])
    pure_momentum_closed = 1.0 / (
        1.0 + 2.0 * eta * data["xf"] * BASE13.BASE.ModelParameters().delta
        / data["xchat"]
    )
    null_f1_error = float(
        np.max(np.abs(pure_momentum_from_r2 - pure_momentum_closed))
    )
    null_eta_error = (
        float(np.max(np.abs(data["mu_cc"] - expected_eta0)))
        if eta == 0.0
        else math.nan
    )
    stability = bool(
        np.all(data["qs_over_2mpl2"] > 0.0)
        and np.all(data["q_c"] > 0.0)
        and np.all(data["hat_cs2"] > 0.0)
        and np.all(data["cs2"] > 0.0)
        and all(
            np.all(np.isfinite(data[name]))
            for name in ("mu_cc", "mu_cb", "mu_bc", "mu_bb", "c1")
        )
    )
    weak_late = bool(
        np.all(data["mu_cc"][late] > 0.0)
        and np.all(data["mu_cc"][late] <= 1.0 + 1.0e-10)
        and np.all(data["mu_cb"][late] > 0.0)
        and np.all(data["mu_cb"][late] <= 1.0 + 1.0e-10)
    )
    return {
        "eta": eta,
        "A_rec": float(data["A"][0]),
        "q_c_min": float(np.min(data["q_c"])),
        "hat_cs2": float(data["hat_cs2"][-1]),
        "cs2_min": float(np.min(data["cs2"])),
        "cs2_max": float(np.max(data["cs2"])),
        "mu_cc_today": float(data["mu_cc"][-1]),
        "mu_cb_today": float(data["mu_cb"][-1]),
        "mu_cc_zle10_min": float(np.min(data["mu_cc"][late])),
        "mu_cc_zle10_max": float(np.max(data["mu_cc"][late])),
        "mu_cb_zle10_min": float(np.min(data["mu_cb"][late])),
        "c1_zle10_min": float(np.min(data["c1"][late])),
        "c1_zle10_max": float(np.max(data["c1"][late])),
        "eta_to_zero_null_max_abs_error": null_eta_error,
        "f1_to_zero_null_max_abs_error": null_f1_error,
        "stable_and_finite": stability,
        "strict_weak_gravity_for_0leqzleq10": weak_late,
    }


def markdown_report(step: float = 2.5e-4) -> tuple[str, bool]:
    datasets = [reconstruct(eta, step) for eta in ETA_GRID]
    summaries = [summarize(data) for data in datasets]
    growth = [integrate_growth(data) for data in datasets]
    baseline_growth = growth[0]["delta_m_today"]

    lines = [
        "# A2-K6.1 — reprodukovateľný numerický výstup Gij a rastovej brány",
        "",
        "- akcia: `G2=X-V(phi)`, `f=-f1(phi) rho_c+eta Z^2`;",
        "- fyzická hustota A1: `rho_c_hat=(1+f1)rho_c`;",
        f"- integračný krok backgroundu: `{step:g}` v `x=ln(a)`;",
        f"- rastový diagnostický interval: `z={Z_GROWTH_INITIAL:g} -> 0`;",
        "- primárny zdroj rovníc: arXiv:2005.13809, rovnice (5.17)-(5.24).",
        "",
        "## Nulové limity a stabilita",
        "",
        "| eta | A_rec | min(q_c) | hat(c_s)^2 | rozsah c_s^2 | chyba eta->0 | chyba f1->0 | stabilná |",
        "|---:|---:|---:|---:|---:|---:|---:|:---:|",
    ]
    for s in summaries:
        eta_error = s["eta_to_zero_null_max_abs_error"]
        eta_text = "—" if math.isnan(eta_error) else f"{eta_error:.3e}"
        lines.append(
            f"| {s['eta']:.1f} | {s['A_rec']:.9f} | {s['q_c_min']:.6f} | "
            f"{s['hat_cs2']:.6f} | {s['cs2_min']:.6f}–{s['cs2_max']:.6f} | "
            f"{eta_text} | {s['f1_to_zero_null_max_abs_error']:.3e} | "
            f"{'áno' if s['stable_and_finite'] else 'nie'} |"
        )

    lines += [
        "",
        "## Fyzicky mapovaná gravitačná matica",
        "",
        "Hodnoty `mu_cc` násobia `rho_c_hat`; preto je `mu_cc=Gcc/(A G)`, "
        "nie papierové `Gcc/G`, ktoré násobí holú `rho_c`.",
        "",
        "| eta | mu_cc(0) | mu_cb(0) | rozsah mu_cc, z<=10 | min mu_cb, z<=10 | c1, z<=10 | slabá gravitácia na celom z<=10 |",
        "|---:|---:|---:|---:|---:|---:|:---:|",
    ]
    for s in summaries:
        lines.append(
            f"| {s['eta']:.1f} | {s['mu_cc_today']:.6f} | {s['mu_cb_today']:.6f} | "
            f"{s['mu_cc_zle10_min']:.6f}–{s['mu_cc_zle10_max']:.6f} | "
            f"{s['mu_cb_zle10_min']:.6f} | "
            f"{s['c1_zle10_min']:.6f}–{s['c1_zle10_max']:.6f} | "
            f"{'áno' if s['strict_weak_gravity_for_0leqzleq10'] else 'nie'} |"
        )

    lines += [
        "",
        "## Subhorizontový rastový diagnostický test",
        "",
        "Toto nie je CMB normalizácia. Všetky eta začínajú pri z=100 rovnakými "
        "`delta_c=delta_b=1` a deriváciami `d delta/d ln(a)=1`.",
        "",
        "| eta | delta_c(0) | delta_b(0) | delta_m(0) | delta_m / eta=0 |",
        "|---:|---:|---:|---:|---:|",
    ]
    for s, g in zip(summaries, growth):
        lines.append(
            f"| {s['eta']:.1f} | {g['delta_c_today']:.6f} | "
            f"{g['delta_b_today']:.6f} | {g['delta_m_today']:.6f} | "
            f"{g['delta_m_today']/baseline_growth:.6f} |"
        )

    null_ok = bool(
        summaries[0]["eta_to_zero_null_max_abs_error"] < 2.0e-8
        and all(s["f1_to_zero_null_max_abs_error"] < 2.0e-12 for s in summaries)
    )
    stable_ok = all(s["stable_and_finite"] for s in summaries)
    weak_candidates = [
        s["eta"]
        for s in summaries
        if s["strict_weak_gravity_for_0leqzleq10"]
    ]
    passed = null_ok and stable_ok and bool(weak_candidates)
    lines += [
        "",
        "## Strojový rozsudok nutnej K6.1 brány",
        "",
        f"- oba nulové limity: `{'PASS' if null_ok else 'FAIL'}`;",
        f"- bez ducha, gradientového znamienka, pólu a NaN: `{'PASS' if stable_ok else 'FAIL'}`;",
        f"- predregistrované eta so striktne kladným `mu_cc,mu_cb<=1` na `0<=z<=10`: `{weak_candidates}`;",
        f"- výsledok nutnej brány: `{'PASS' if passed else 'FAIL'}`.",
        "",
        "PASS ešte nie je observačný fit. Vyžaduje plné superhorizontové "
        "rovnice, adiabaticitu a CMB/Boltzmannovu normalizáciu.",
        "",
    ]
    return "\n".join(lines), passed


def main() -> int:
    report, passed = markdown_report()
    print(report)
    return 0 if passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
