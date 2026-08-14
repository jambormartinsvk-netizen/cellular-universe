#!/usr/bin/env python3
"""First action/background/stability gate for A2-K5/K3a.

Candidate interaction in the conventions of Kase & Tsujikawa (2020):

  f = -f1(phi) rho_c + eta Z^2,   Z = u_c^mu partial_mu phi,

with Einstein gravity and G2=X-V(phi).  The effective CDM density is
hat(rho_c)=(1+f1)rho_c.  Its energy equation depends only on f1, whereas
eta Z^2 supplies momentum transfer.  The exact A1-K1 background is
reconstructed for constant eta by

  (1+2 eta) dot(phi)^2 = (1+w_f) rho_f,
  V=(1-w_f)rho_f/2,
  d ln(1+f1)/dt = Gamma rho_f/hat(rho_c).

For this action, f_,ncnc=0, so the effective CDM sound speed vanishes.
The high-k scalar stability coefficients are

  q_s/(2 Mpl^2)=1+2 eta,
  hat(c_s)^2=1/(1+2 eta),

and q_c is positive for 1+f1>0 and eta>=0.  Passing these checks does not
establish G_eff,c<=G in the simultaneous energy+momentum model; that is the
next K3a perturbation/growth gate.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np


BASE_PATH = Path(__file__).with_name(
    "13_script_A1_K1_cdm_background_audit_exact_zstar.py"
)
SPEC = importlib.util.spec_from_file_location("k3a_background", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load validated A1 background: {BASE_PATH}")
BASE13 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE13
SPEC.loader.exec_module(BASE13)


def cumulative_trapezoid(values: np.ndarray, xs: np.ndarray) -> np.ndarray:
    out = np.zeros_like(values)
    out[1:] = np.cumsum(0.5 * (values[1:] + values[:-1]) * np.diff(xs))
    return out


def run_eta(eta: float, step: float) -> dict:
    if eta <= -0.5:
        raise ValueError("eta must satisfy 1+2 eta > 0")

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

    # Dimensionless varphi=phi/Mpl and x=ln a.
    varphi_x = np.sqrt(3.0 * p.delta * xf / (1.0 + 2.0 * eta)) / e
    varphi = cumulative_trapezoid(varphi_x, xs)
    varphi -= varphi[-1]

    # A=1+f1 is fixed by the already validated A1 energy-transfer identity.
    dln_a_dx = p.lam * xf / (e * xchat)
    ln_a = cumulative_trapezoid(dln_a_dx, xs)
    ln_a -= ln_a[-1]
    a_coupling = np.exp(ln_a)
    f1 = a_coupling - 1.0

    # dot(phi)^2/(3 H0^2 Mpl^2); used only in positive q_c/A.
    phidot2_scaled = p.delta * xf / (1.0 + 2.0 * eta)
    qc_over_a = 1.0 + 2.0 * eta * phidot2_scaled / xchat
    qs_over_2mpl2 = np.full_like(xs, 1.0 + 2.0 * eta)
    chat_s2 = np.full_like(xs, 1.0 / (1.0 + 2.0 * eta))

    # Reconstruct combined scalar+momentum density and pressure.
    kinetic_total = 0.5 * (1.0 + 2.0 * eta) * phidot2_scaled
    potential = 0.5 * (2.0 - p.delta) * xf
    rho_reconstructed = kinetic_total + potential
    pressure_reconstructed = kinetic_total - potential
    target_pressure = (-1.0 + p.delta) * xf

    # Q/(H0 rho_crit0) identity in x-time.
    source_required = p.lam * xf
    source_reconstructed = e * xchat * dln_a_dx

    residuals = {
        "max_abs_rho_f_reconstruction": float(
            np.max(np.abs(rho_reconstructed - xf))
        ),
        "max_abs_pressure_f_reconstruction": float(
            np.max(np.abs(pressure_reconstructed - target_pressure))
        ),
        "max_abs_energy_transfer_reconstruction": float(
            np.max(np.abs(source_reconstructed - source_required))
        ),
    }
    checks = {
        "A_equals_1_plus_f1_positive": bool(np.all(a_coupling > 0.0)),
        "f_nn_zero_so_CDM_sound_speed_zero": True,
        "q_s_positive": bool(np.all(qs_over_2mpl2 > 0.0)),
        "q_c_positive": bool(np.all(qc_over_a > 0.0)),
        "scalar_gradient_coefficient_positive": bool(np.all(chat_s2 > 0.0)),
        "A1_density_pressure_reconstructed": bool(
            residuals["max_abs_rho_f_reconstruction"] < 1.0e-12
            and residuals["max_abs_pressure_f_reconstruction"] < 1.0e-12
        ),
        "A1_energy_transfer_reconstructed": bool(
            residuals["max_abs_energy_transfer_reconstruction"] < 1.0e-12
        ),
        "all_finite": bool(
            np.all(np.isfinite(varphi))
            and np.all(np.isfinite(a_coupling))
            and np.all(np.isfinite(qc_over_a))
        ),
    }
    return {
        "eta": eta,
        "step": step,
        "field_excursion_abs_Delta_varphi": float(-varphi[0]),
        "A_at_recombination": float(a_coupling[0]),
        "f1_at_recombination": float(f1[0]),
        "q_s_over_2Mpl2": float(qs_over_2mpl2[0]),
        "hat_c_s_squared": float(chat_s2[0]),
        "q_c_over_A_min": float(np.min(qc_over_a)),
        "q_c_over_A_today": float(qc_over_a[-1]),
        "residuals": residuals,
        "checks": checks,
        "passed": all(checks.values()),
    }


def main() -> int:
    eta_grid = [0.0, 0.1, 0.5, 1.0, 2.0, 5.0]
    coarse = [run_eta(eta, 5.0e-4) for eta in eta_grid]
    fine = [run_eta(eta, 2.5e-4) for eta in eta_grid]
    convergence = {}
    for c, f in zip(coarse, fine):
        label = f"eta={f['eta']:g}"
        convergence[label] = {
            key: abs(c[key] - f[key]) / max(abs(f[key]), 1.0e-300)
            for key in [
                "field_excursion_abs_Delta_varphi",
                "A_at_recombination",
                "q_c_over_A_today",
            ]
        }
    converged = all(
        value < 1.0e-5
        for item in convergence.values()
        for value in item.values()
    )
    all_pass = all(item["passed"] for item in fine)
    output = {
        "test": "A2-K5/K3a action, exact-background, and high-k stability gate",
        "action": (
            "Einstein gravity + G2=X-V(phi) + Schutz-Sorkin CDM + "
            "f=-f1(phi)rho_c+eta Z^2"
        ),
        "eta_grid_preregistered_for_first_gate": eta_grid,
        "fine_results": fine,
        "convergence_relative_differences": convergence,
        "checks": {
            "all_action_background_stability_tests_pass": all_pass,
            "step_converged": converged,
        },
        "status": (
            "PASS_K3a_ACTION_BACKGROUND_HIGH_K_STABILITY_GATE"
            if all_pass and converged
            else "FAIL_OR_REQUIRES_REVIEW"
        ),
        "mandatory_next_gate": (
            "Derive simultaneous-f1-plus-f2 full linear equations and G_eff,c; "
            "passing here does not prove weak gravity or acceptable S8."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if all_pass and converged else 1


if __name__ == "__main__":
    raise SystemExit(main())
