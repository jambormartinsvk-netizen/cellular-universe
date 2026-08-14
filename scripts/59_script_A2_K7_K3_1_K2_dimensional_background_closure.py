#!/usr/bin/env python3
"""A2-K7.1a-K3.1-K2.1 dimensional Onsager/background closure.

Use thermodynamic forces (dimensionless chemical affinity A, expansion
Theta) and fluxes (energy reaction Q, minus bulk pressure -Pi):

    Q       = ell A + alpha Theta,
    -Pi     = alpha A + zeta Theta,
    alpha   = epsilon (1-delta) rho_F.

The non-expansion part of the exact K7 source fixes

    ell A0 = (1-epsilon) Gamma rho_F.

Define ell_hat=ell/(H rho_F).  Positivity requires

    ell*zeta > alpha^2.

For a one-percent determinant margin, this script computes the required
affinity, minimum bulk-pressure correction, and compensated canonical-fuel
enthalpy on the validated A1 background.  The diagnostic ell_hat grid is
not a data fit.  A positive result proves only dimensional background
existence; it does not derive ell_hat, a bath temperature, or the noise
kernel from microphysics.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

import numpy as np


BASE_PATH = Path(__file__).with_name(
    "50_script_A2_K7_0_mediator_ledger_collision_gate.py"
)
SPEC = importlib.util.spec_from_file_location("k7_background_dimensional", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load {BASE_PATH}")
K70 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = K70
SPEC.loader.exec_module(K70)


ELL_HAT_GRID = (0.1, 1.0, 10.0, 100.0)
DETERMINANT_MARGIN = 0.01


def evaluate(base: dict, fraction: float, ell_hat: float) -> dict:
    p = base["p"]
    e = base["e"]
    epsilon = fraction * p.delta
    cross = epsilon * (1.0 - p.delta)

    # A0 follows from ell A0=(1-epsilon) Gamma rho_F.
    affinity = (1.0 - epsilon) * p.lam / (ell_hat * e)

    # zeta_hat = zeta*H/rho_F.  The determinant condition becomes
    # ell_hat*zeta_hat>(alpha/rho_F)^2=cross^2.
    zeta_hat = (1.0 + DETERMINANT_MARGIN) * cross * cross / ell_hat

    # -Pi/rho_F = alpha*A/rho_F + zeta*Theta/rho_F, Theta=3H.
    minus_bulk_pressure_ratio = cross * affinity + 3.0 * zeta_hat

    # Keep the registered total p_F fixed by shifting the equilibrium scalar
    # pressure: p_phi,eq = p_F-Pi.  Since Pi is negative here,
    # (rho_phi+p_phi,eq)/rho_F=delta-epsilon-Pi/rho_F.
    fuel_enthalpy_ratio = (
        p.delta - epsilon + minus_bulk_pressure_ratio
    )
    w_phi_equilibrium = (
        (-1.0 + p.delta) + minus_bulk_pressure_ratio
    ) / (1.0 - epsilon)

    determinant_hat = ell_hat * zeta_hat - cross * cross
    checks = {
        "onsager_determinant_positive": bool(determinant_hat > 0.0),
        "fuel_enthalpy_positive_all_times": bool(
            np.all(fuel_enthalpy_ratio > 0.0)
        ),
        "finite_affinity_and_pressure": bool(
            np.all(np.isfinite(affinity))
            and np.all(np.isfinite(minus_bulk_pressure_ratio))
        ),
        "near_equilibrium_affinity_abs_lt_1": bool(
            np.max(np.abs(affinity)) < 1.0
        ),
        "bulk_pressure_below_10_percent_rhoF": bool(
            np.max(minus_bulk_pressure_ratio) < 0.1
        ),
    }
    return {
        "epsilon_over_delta": fraction,
        "epsilon": epsilon,
        "ell_hat": ell_hat,
        "cross_alpha_over_rhoF": cross,
        "zeta_hat": zeta_hat,
        "determinant_hat": determinant_hat,
        "affinity_recombination": float(affinity[0]),
        "affinity_today": float(affinity[-1]),
        "max_abs_affinity": float(np.max(np.abs(affinity))),
        "minus_Pi_over_rhoF_recombination": float(
            minus_bulk_pressure_ratio[0]
        ),
        "minus_Pi_over_rhoF_today": float(minus_bulk_pressure_ratio[-1]),
        "min_fuel_enthalpy_over_rhoF": float(np.min(fuel_enthalpy_ratio)),
        "w_phi_equilibrium_today": float(w_phi_equilibrium[-1]),
        "normalised_reaction_noise_strength_per_2T": ell_hat,
        "checks": checks,
        "background_passed": all(checks.values()),
    }


def main() -> int:
    base = K70.background(2.5e-4)
    rows = [
        evaluate(base, fraction, ell_hat)
        for fraction in K70.EPSILON_OVER_DELTA_GRID
        for ell_hat in ELL_HAT_GRID
    ]

    viable = [row for row in rows if row["background_passed"]]
    viable_ell = sorted({row["ell_hat"] for row in viable})
    every_epsilon_has_viable = all(
        any(
            row["epsilon_over_delta"] == fraction
            and row["background_passed"]
            for row in rows
        )
        for fraction in K70.EPSILON_OVER_DELTA_GRID
    )

    output = {
        "test": "A2-K7 K3.1-K2.1 dimensional Onsager/background closure",
        "diagnostic_ell_hat_grid": ELL_HAT_GRID,
        "determinant_margin": DETERMINANT_MARGIN,
        "rows": rows,
        "summary": {
            "number_of_rows": len(rows),
            "number_background_passed": len(viable),
            "viable_ell_hat_values": viable_ell,
            "every_epsilon_has_a_viable_diagnostic_point": (
                every_epsilon_has_viable
            ),
            "bath_temperature_derived": False,
            "ell_hat_microphysically_derived": False,
            "noise_amplitude_physically_fixed": False,
        },
        "verdict": (
            "SURVIVES_DIMENSIONAL_BACKGROUND_EXISTENCE_ONLY"
            if every_epsilon_has_viable else "DEAD_M014c_BACKGROUND"
        ),
        "max_depth": "39/100",
        "parent_K7_accepted_score": "30/100",
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if every_epsilon_has_viable else 1


if __name__ == "__main__":
    raise SystemExit(main())
