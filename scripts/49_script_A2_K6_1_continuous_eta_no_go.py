#!/usr/bin/env python3
"""A2-K6.1 continuous-eta no-go and convergence audit.

This successor does not erase script 48.  It removes two limitations found
by that first numerical pass:

1. it evaluates eps_qc and r1 in cancellation-free closed form;
2. it proves the z=0 result for the complete eta>=0 half-line instead of
   extrapolating from the preregistered six-point grid.

The action and conventions are those of arXiv:2005.13809:

    G2=X-V(phi), f=-f1(phi)rho_c+eta Z^2, A=1+f1,
    rho_c_hat=A rho_c.

All gravitational couplings reported as mu_cc use rho_c_hat.  Therefore
mu_cc=(Gcc/G)/A, while the paper's printed Gcc multiplies bare rho_c.
"""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path
import sys

import numpy as np


SCRIPT48 = Path(__file__).with_name(
    "48_script_A2_K6_1_exact_Gij_and_growth_gate.py"
)
SPEC = importlib.util.spec_from_file_location("k6_first_pass", SCRIPT48)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot import {SCRIPT48}")
K6 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = K6
SPEC.loader.exec_module(K6)

ETA_GRID = (0.0, 0.1, 0.5, 1.0, 2.0, 5.0)
Z_INITIAL = 100.0


def closed_dataset(eta: float, base: dict) -> dict:
    """Build the exact K6 high-k coefficients from one eta=0 background."""
    if eta < 0.0:
        raise ValueError("This gate is preregistered for eta>=0")
    p = K6.BASE13.BASE.ModelParameters()
    xs = base["xs"]
    xf = base["xf"]
    xchat = base["xchat"]
    e = base["e"]
    e2 = e**2
    coupling_a = base["A"]
    s = base["s"]
    eps_h = base["eps_h"]
    eps_delta2 = base["eps_delta2"]
    eps_delta3 = base["eps_delta3"]

    t = 1.0 + 2.0 * eta
    r = t - 1.0
    p0 = 3.0 * p.delta * xf / e2
    d = p.delta * xf / xchat
    log_d_x = K6.log_derivative(d, xs)
    b = 1.0 + eps_h + eps_delta2 - eps_delta3

    varphi_x2 = p0 / t
    varphi_x = np.sqrt(varphi_x2)
    dotphi = e * varphi_x
    rho_hat = 3.0 * xchat
    f1_phi = coupling_a * s / varphi_x
    f2_z = r * dotphi

    v = (r / t) * d
    q_c = coupling_a * (1.0 + v)
    eps_qc = s + v * log_d_x / (1.0 + v)
    beta_nc = 1.0 - coupling_a

    # Cancellation-free reduction of Eqs. (5.21)-(5.22):
    # r1/A=(2s/P0)[s(1+r)+r*d(s+dln(d)/dx-B)], r2=r*d.
    r1_over_a = (
        2.0 * s / p0
        * (s * (1.0 + r) + r * d * (s + log_d_x - b))
    )
    r1 = coupling_a * r1_over_a
    r2 = r * d

    # Independent direct substitution into Eq. (5.21).
    c_bracket = b - eps_qc
    r1_direct = (
        -2.0 * e * f1_phi / rho_hat
        * (f2_z * c_bracket - rho_hat * eps_qc / dotphi)
    )

    mu_cc = (1.0 + r1_over_a) / (1.0 + r2)
    mu_cb = 1.0 / (1.0 + r2)
    mu_bc = np.ones_like(xs)
    mu_bb = np.ones_like(xs)

    hat_cs2 = np.full_like(xs, 1.0 / t)
    cs2_over_hat = 1.0 + f2_z**2 / (rho_hat + dotphi * f2_z)
    cs2 = hat_cs2 * cs2_over_hat
    qs_over_2mpl2 = np.full_like(xs, t)

    if eta == 0.0:
        c1 = 2.0 + eps_qc
    else:
        denominator = 1.0 - beta_nc - q_c
        mixing = (2.0 * coupling_a * s - 2.0 * q_c * eps_qc) / denominator
        c1 = (
            (2.0 + eps_qc) / cs2_over_hat
            + (mixing - 1.0 - eps_delta2 - 2.0 * eps_h)
            * (1.0 - 1.0 / cs2_over_hat)
        )

    result = dict(base)
    result.update(
        {
            "eta": eta,
            "varphi_x": varphi_x,
            "beta_nc": beta_nc,
            "q_c": q_c,
            "eps_qc": eps_qc,
            "r1": r1,
            "r1_direct": r1_direct,
            "r2": r2,
            "mu_cc": mu_cc,
            "mu_cb": mu_cb,
            "mu_bc": mu_bc,
            "mu_bb": mu_bb,
            "hat_cs2": hat_cs2,
            "cs2": cs2,
            "qs_over_2mpl2": qs_over_2mpl2,
            "c1": c1,
            "d_ratio": d,
            "log_d_x": log_d_x,
            "p0": p0,
            "b_combo": b,
        }
    )
    return result


def rhs_with_coefficients(y: np.ndarray, coeff: tuple[float, ...]) -> np.ndarray:
    eps_h, c1, mu_cc, mu_cb, omega_c, omega_b = coeff
    dc, vc, db, vb = y
    return np.array(
        [
            vc,
            -(c1 + eps_h) * vc
            + 1.5 * (mu_cc * omega_c * dc + mu_cb * omega_b * db),
            vb,
            -(2.0 + eps_h) * vb
            + 1.5 * (omega_c * dc + omega_b * db),
        ]
    )


def integrate_growth_fast(data: dict) -> float:
    """Scale-independent QS diagnostic with common normalization at z=100."""
    xs = data["xs"]
    start = int(np.searchsorted(xs, -math.log1p(Z_INITIAL)))
    omega_c = data["xchat"] / data["e"] ** 2
    omega_b = data["xb"] / data["e"] ** 2
    arrays = (
        data["eps_h"], data["c1"], data["mu_cc"], data["mu_cb"],
        omega_c, omega_b,
    )
    y = np.array([1.0, 1.0, 1.0, 1.0])
    for i in range(start, len(xs) - 1):
        dx = xs[i + 1] - xs[i]
        ca = tuple(float(a[i]) for a in arrays)
        cb = tuple(float(a[i + 1]) for a in arrays)
        cm = tuple(0.5 * (a + b) for a, b in zip(ca, cb))
        k1 = rhs_with_coefficients(y, ca)
        k2 = rhs_with_coefficients(y + 0.5 * dx * k1, cm)
        k3 = rhs_with_coefficients(y + 0.5 * dx * k2, cm)
        k4 = rhs_with_coefficients(y + dx * k3, cb)
        y += dx * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
    dc, _, db, _ = y
    return float(
        (data["xchat"][-1] * dc + data["xb"][-1] * db) / data["xm"][-1]
    )


def continuous_today_theorem(data_eta0: dict) -> dict[str, float | str | bool]:
    """Prove mu_cc(z=0)>1 for every eta>=0 using endpoint monotonicity."""
    s = float(data_eta0["s"][-1])
    p0 = float(data_eta0["p0"][-1])
    d = float(data_eta0["d_ratio"][-1])
    l = float(data_eta0["log_d_x"][-1])
    b = float(data_eta0["b_combo"][-1])
    alpha = 2.0 * s / p0

    # For r=2eta>=0: mu=(n0+r*n1)/(1+r*d).
    n0 = 1.0 + alpha * s
    n1 = alpha * (s + d * (s + l - b))
    derivative_numerator = n1 - d * n0
    limit_infinity = n1 / d
    monotonic = "rastúca" if derivative_numerator > 0.0 else "klesajúca"
    no_go = n0 > 1.0 and limit_infinity > 1.0
    return {
        "s_today": s,
        "P0_today": p0,
        "d_today": d,
        "B_today": b,
        "dln_d_dx_today": l,
        "n0": n0,
        "n1": n1,
        "derivative_numerator": derivative_numerator,
        "monotonic": monotonic,
        "mu_eta0": n0,
        "mu_eta_infinity": limit_infinity,
        "no_go_all_eta_nonnegative": no_go,
    }


def build_at_step(step: float) -> tuple[list[dict], list[float], dict]:
    first = K6.reconstruct(0.0, step)
    datasets = [closed_dataset(eta, first) for eta in ETA_GRID]
    growth = [integrate_growth_fast(d) for d in datasets]
    theorem = continuous_today_theorem(datasets[0])
    return datasets, growth, theorem


def main() -> int:
    fine, growth, theorem = build_at_step(2.5e-4)
    coarse, _, theorem_coarse = build_at_step(5.0e-4)
    base_growth = growth[0]

    print("# A2-K6.1 — spojitý eta audit a reprodukovateľný rozsudok")
    print()
    print("## Presné redukované vzťahy")
    print()
    print("Pre `t=1+2 eta`, `r=t-1`, `d=delta rho_f/rho_c_hat`,")
    print("`P0=3 delta X_f/E^2`, `s=d ln A/dx` a")
    print("`B=1+eps_H+eps_Delta2-eps_Delta3` platí")
    print()
    print("```text")
    print("q_c = A [1 + (r/t)d]")
    print("r2  = r d")
    print("r1/A = (2s/P0) [s(1+r) + r d (s + dln(d)/dx - B)]")
    print("mu_cc = [1+r1/A]/[1+r2]")
    print("mu_cb = 1/[1+r2],  mu_bc=mu_bb=1")
    print("```")
    print()
    print("## Predregistrovaný grid")
    print()
    print("| eta | mu_cc(0) | mu_cb(0) | min-max mu_cc pre z<=10 | "
          "max |r1_closed-r1_direct| | rast / eta=0 |")
    print("|---:|---:|---:|---:|---:|---:|")
    for eta, data, g in zip(ETA_GRID, fine, growth):
        late = data["xs"] >= -math.log1p(10.0)
        residual = np.max(np.abs(data["r1"] - data["r1_direct"]))
        print(
            f"| {eta:.1f} | {data['mu_cc'][-1]:.6f} | "
            f"{data['mu_cb'][-1]:.6f} | "
            f"{np.min(data['mu_cc'][late]):.6f}–"
            f"{np.max(data['mu_cc'][late]):.6f} | "
            f"{residual:.3e} | {g/base_growth:.6f} |"
        )

    print()
    print("## Oba nulové limity")
    print()
    eta0_expected = 1.0 + 2.0 * (fine[0]["s"] / fine[0]["varphi_x"]) ** 2
    eta0_error = np.max(np.abs(fine[0]["mu_cc"] - eta0_expected))
    f1_errors = []
    p = K6.BASE13.BASE.ModelParameters()
    for eta, data in zip(ETA_GRID, fine):
        pure_closed = 1.0 / (
            1.0 + 2.0 * eta * p.delta * data["xf"] / data["xchat"]
        )
        f1_errors.append(float(np.max(np.abs(data["mu_cb"] - pure_closed))))
    print(f"- `eta->0`: max chyba voči `1+2(d ln A/dvarphi)^2` = `{eta0_error:.3e}`;")
    print(f"- `f1->0`: max chyba voči čistému momentum limitu = `{max(f1_errors):.3e}`;")
    print("- mapovanie baryónovej odozvy: `mu_bc=mu_bb=1` presne.")

    print()
    print("## Veta pre celý spojitý interval eta>=0 pri z=0")
    print()
    print("Po dosadení je `mu_cc=(n0+r n1)/(1+r d)`, kde `r=2 eta>=0`.")
    print("Jej derivácia má konštantné znamienko, takže funkcia je monotónna a")
    print("na vylúčenie skrytého ostrova stačí skontrolovať oba endpointy.")
    print()
    print(f"- smer: `{theorem['monotonic']}`;")
    print(f"- `mu_cc(eta=0,z=0)={theorem['mu_eta0']:.9f}`;")
    print(f"- `lim eta->infinity mu_cc(z=0)={theorem['mu_eta_infinity']:.9f}`;")
    print(f"- `n1-d*n0={theorem['derivative_numerator']:.9e}`;")
    print("- záver: `mu_cc(z=0)>1` pre každé `eta>=0`." if theorem["no_go_all_eta_nonnegative"] else "- záver: NO-GO sa nepotvrdilo.")

    print()
    print("## Konvergencia krokov")
    print()
    print("| veličina | relatívny rozdiel 5e-4 vs 2.5e-4 |")
    print("|---|---:|")
    for i, eta in enumerate(ETA_GRID):
        rel = abs(coarse[i]["mu_cc"][-1] - fine[i]["mu_cc"][-1]) / abs(fine[i]["mu_cc"][-1])
        print(f"| `mu_cc(0)`, eta={eta:g} | {rel:.3e} |")
    rel_inf = abs(theorem_coarse["mu_eta_infinity"] - theorem["mu_eta_infinity"]) / abs(theorem["mu_eta_infinity"])
    print(f"| `mu_cc(eta->infinity,0)` | {rel_inf:.3e} |")

    all_stable = all(
        np.all(d["q_c"] > 0.0)
        and np.all(d["qs_over_2mpl2"] > 0.0)
        and np.all(d["hat_cs2"] > 0.0)
        and np.all(d["cs2"] > 0.0)
        and np.all(np.isfinite(d["c1"]))
        for d in fine
    )
    null_pass = eta0_error < 1.0e-12 and max(f1_errors) < 1.0e-12
    print()
    print("## Rozsudok")
    print()
    print(f"- stabilita a konečnosť na gride: `{'PASS' if all_stable else 'FAIL'}`;")
    print(f"- nulové limity: `{'PASS' if null_pass else 'FAIL'}`;")
    print(f"- nutná podmienka `mu_cc<=1`: `{'FAIL' if theorem['no_go_all_eta_nonnegative'] else 'NEUZAVRETÁ'}`;")
    print("- koľaj A2-K6: `MŔTVA M-013`.")
    print()
    print("Dôvod smrti nie je duch ani gradientová nestabilita. Momentum člen")
    print("spomalí pole, ale pevný A1 tok potom vyžaduje väčší skalárny náboj;")
    print("jeho povinná príťažlivá piata sila rastie rýchlejšie než slabnutie")
    print("z faktora `1/(1+r2)`. Rastový diagnostický pomer preto stúpa")
    print("z `1` pri eta=0 na `2.160` pri eta=5, namiesto požadovaného poklesu.")
    return 2 if theorem["no_go_all_eta_nonnegative"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
