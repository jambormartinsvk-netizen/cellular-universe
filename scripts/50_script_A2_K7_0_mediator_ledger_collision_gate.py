#!/usr/bin/env python3
"""A2-K7.0 finite-enthalpy mediator: exact A1 ledger and collision gate.

This script audits the coarse-grained three-component chain

    fuel phi -> massive mediator M -> cold ash c

while keeping the already validated A1 total background exactly fixed.
The original A1 fuel density is decomposed as

    rho_F = rho_phi + rho_M,
    rho_M = epsilon rho_F,
    p_M = 0,
    p_phi = w_F rho_F,

with constant 0 < epsilon < delta=1+w_F.  The upper bound follows from
positive canonical fuel enthalpy.  The required donor-aligned sources are

    Q_2 = Gamma rho_F,
    Q_1 = (1-epsilon) Gamma rho_F + 3 H epsilon (1-delta) rho_F.

Q_1 is fuel->M and Q_2 is M->c.  The local interaction-only velocity
operator in the relative basis (v_M-v_phi, v_c-v_M) is

    d/dt [Delta_Mphi] = [-R1,  0] [Delta_Mphi]
          [Delta_cM  ]   [ R1, -R2] [Delta_cM  ],

where R1=Q1/(rho_M+p_M)>0 and R2=Q2/rho_c>0.  This proves only the sign of
the collision operator.  It is not a full gauge-invariant cosmological
perturbation or Boltzmann test.
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
SPEC = importlib.util.spec_from_file_location("a1_background_k7", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load validated A1 background: {BASE_PATH}")
BASE13 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE13
SPEC.loader.exec_module(BASE13)


EPSILON_OVER_DELTA_GRID = (0.01, 0.05, 0.10, 0.25, 0.50, 0.90)


def background(step: float) -> dict:
    p = BASE13.BASE.ModelParameters()
    x_star = -math.log1p(p.z_star)
    settings = BASE13.BASE.IntegrationSettings(x_min=x_star, step=step)
    xs_desc, states_desc, xb0 = BASE13.integrate_background(p, settings)
    xs = xs_desc[::-1]
    states = states_desc[::-1]
    xf, xm, xr = states.T
    xb = xb0 * np.exp(-3.0 * xs)
    xc = xm - xb
    e = np.sqrt(xf + xm + xr)
    xf_x = -3.0 * p.delta * xf - p.lam * xf / e
    return {
        "p": p,
        "xs": xs,
        "xf": xf,
        "xm": xm,
        "xr": xr,
        "xb": xb,
        "xc": xc,
        "e": e,
        "xf_x": xf_x,
    }


def run_fraction(base: dict, fraction: float) -> dict:
    p = base["p"]
    xs = base["xs"]
    xf = base["xf"]
    xc = base["xc"]
    e = base["e"]
    xf_x = base["xf_x"]
    wf = -1.0 + p.delta
    epsilon = fraction * p.delta

    rho_m = epsilon * xf
    rho_phi = (1.0 - epsilon) * xf
    pressure_m = np.zeros_like(xf)
    pressure_phi = wf * xf
    enthalpy_m = rho_m
    enthalpy_phi = (p.delta - epsilon) * xf
    w_phi = wf / (1.0 - epsilon)

    # Sources divided by H*rho_crit,0, i.e. the terms appearing in dX/dx.
    q2_x = p.lam * xf / e
    q1_x = (
        (1.0 - epsilon) * p.lam * xf / e
        + 3.0 * epsilon * (1.0 - p.delta) * xf
    )

    rho_phi_x_from_split = (1.0 - epsilon) * xf_x
    rho_m_x_from_split = epsilon * xf_x
    rho_phi_x_from_ledger = -3.0 * enthalpy_phi - q1_x
    rho_m_x_from_ledger = -3.0 * enthalpy_m + q1_x - q2_x

    # Interaction-only rates per e-fold x=ln(a).
    alpha1 = q1_x / enthalpy_m
    alpha2 = q2_x / xc
    eig_fast = -alpha1
    eig_slow = -alpha2

    # Damping factors of the diagonal collision modes, quoted as log10 to
    # avoid underflow for the fast mediator mode.
    log10_damping_1 = -float(np.trapezoid(alpha1, xs)) / math.log(10.0)
    log10_damping_2 = -float(np.trapezoid(alpha2, xs)) / math.log(10.0)

    h0_inverse_gyr = 9.778 / p.h
    gamma_m_over_h0 = p.lam / epsilon
    mediator_lifetime_gyr = h0_inverse_gyr / gamma_m_over_h0

    residuals = {
        "rho_split": float(np.max(np.abs(rho_phi + rho_m - xf))),
        "pressure_split": float(
            np.max(np.abs(pressure_phi + pressure_m - wf * xf))
        ),
        "enthalpy_split": float(
            np.max(
                np.abs(enthalpy_phi + enthalpy_m - p.delta * xf)
            )
        ),
        "phi_ledger": float(
            np.max(np.abs(rho_phi_x_from_ledger - rho_phi_x_from_split))
        ),
        "mediator_ledger": float(
            np.max(np.abs(rho_m_x_from_ledger - rho_m_x_from_split))
        ),
    }
    checks = {
        "epsilon_strictly_inside_enthalpy_budget": bool(
            0.0 < epsilon < p.delta
        ),
        "canonical_phi_enthalpy_positive": bool(np.all(enthalpy_phi > 0.0)),
        "mediator_enthalpy_positive": bool(np.all(enthalpy_m > 0.0)),
        "both_sources_positive": bool(np.all(q1_x > 0.0) and np.all(q2_x > 0.0)),
        "collision_eigenvalues_nonpositive": bool(
            np.all(eig_fast < 0.0) and np.all(eig_slow < 0.0)
        ),
        "exact_A1_decomposition": bool(max(residuals.values()) < 1.0e-11),
        "all_finite": bool(
            all(
                np.all(np.isfinite(a))
                for a in (alpha1, alpha2, eig_fast, eig_slow)
            )
        ),
    }
    return {
        "fraction": fraction,
        "epsilon": epsilon,
        "omega_M0": float(rho_m[-1]),
        "w_phi": w_phi,
        "one_plus_w_phi": 1.0 + w_phi,
        "alpha1_at_recombination": float(alpha1[0]),
        "alpha1_today": float(alpha1[-1]),
        "alpha2_at_recombination": float(alpha2[0]),
        "alpha2_today": float(alpha2[-1]),
        "log10_damping_Mphi": log10_damping_1,
        "log10_damping_cM": log10_damping_2,
        "gamma_M_over_H0": gamma_m_over_h0,
        "mediator_lifetime_Gyr": mediator_lifetime_gyr,
        "residuals": residuals,
        "checks": checks,
        "passed": all(checks.values()),
    }


def evaluate(step: float) -> list[dict]:
    base = background(step)
    return [run_fraction(base, f) for f in EPSILON_OVER_DELTA_GRID]


def main() -> int:
    fine = evaluate(2.5e-4)
    coarse = evaluate(5.0e-4)
    all_pass = all(row["passed"] for row in fine)

    print("# A2-K7.0 — numerický výstup ledgerovej a collision-sign brány")
    print()
    print("Predregistrovaný grid: `epsilon/delta={0.01,0.05,0.10,0.25,0.50,0.90}`.")
    print("Mediátor je v tejto prvej realizácii tlakovo spriemerovaný masívny")
    print("kanonický skalár s `w_M=0`. Celkový A1 sektor zostáva `rho_F,p_F`.")
    print()
    print("| eps/delta | epsilon | Omega_M0 | w_phi | alpha1(rec) | alpha1(0) | "
          "alpha2(0) | log10 D_Mphi | log10 D_cM | tau_M [Gyr] | stav |")
    print("|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|")
    for row in fine:
        print(
            f"| {row['fraction']:.2f} | {row['epsilon']:.8f} | "
            f"{row['omega_M0']:.8f} | {row['w_phi']:.8f} | "
            f"{row['alpha1_at_recombination']:.6f} | "
            f"{row['alpha1_today']:.6f} | {row['alpha2_today']:.6f} | "
            f"{row['log10_damping_Mphi']:.6f} | "
            f"{row['log10_damping_cM']:.6f} | "
            f"{row['mediator_lifetime_Gyr']:.6f} | "
            f"{'PASS' if row['passed'] else 'FAIL'} |"
        )

    max_residual = max(
        value for row in fine for value in row["residuals"].values()
    )
    convergence = max(
        abs(f["alpha1_today"] - c["alpha1_today"])
        / abs(f["alpha1_today"])
        for f, c in zip(fine, coarse)
    )
    print()
    print("## Kontroly")
    print()
    print(f"- maximálne absolútne ledgerové rezíduum: `{max_residual:.3e}`;")
    print(f"- maximálny relatívny krokový rozdiel `alpha1(0)`: `{convergence:.3e}`;")
    print("- obe collision eigenhodnoty sú na celom intervale záporné;")
    print("- `alpha2` a jeho integrované tlmenie sú nezávislé od `epsilon`;")
    print("- limit `epsilon->0` je singulárny: `alpha1~Gamma/epsilon`.")
    print()
    print("## Rozsudok tejto brány")
    print()
    print(f"- ledger a entalpický rozpočet: `{'PASS' if all_pass else 'FAIL'}`;")
    print("- interaction-only anti-damping: `NEZISTENÝ`; collision operátor je kontraktívny;")
    print("- stav A2-K7.0: `PREŽÍVA 30/100`.")
    print()
    print("Toto nie je plná stabilita K7. Efektívne Q1 obsahuje člen úmerný H a")
    print("zatiaľ nebolo odvodené z CTP/Boltzmannovej redukcie lokálnej akcie.")
    print("Nasleduje K7.1: mikrofyzický pôvod sadzieb, šum/disipácia a úplné")
    print("gauge-invariantné trojzložkové perturbácie.")
    return 0 if all_pass else 2


if __name__ == "__main__":
    raise SystemExit(main())
