#!/usr/bin/env python3
"""A2-K7 K3.1-K2.2-K1a: registered graviton-steam bath rate gate.

The registered theory describes the existing steam component as a thermal
graviton relic with T0=0.905 K and Delta N_eff=0.0535.  This test asks
whether that already-counted component, with gravity as its only coupling,
can provide the local dissipative rate required by the exact K7 source.

For low-energy gravitational 2->2 scattering, an intentionally optimistic
dimensional estimate is

    sigma_grav ~ T^2/Mbar_Pl^4,
    Gamma_grav ~ n sigma ~ T^5/Mbar_Pl^4,

with an order-one prefactor.  The exact K7 source per fuel density is

    Q1/(H rho_F) = (1-epsilon) lambda/E
                   + 3 epsilon (1-delta).

The estimate is not a precision cross section.  It is a robust hierarchy
test: an order-one uncertainty cannot repair a gap of many tens of orders
of magnitude.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np


BASE_PATH = Path(__file__).with_name(
    "50_script_A2_K7_0_mediator_ledger_collision_gate.py"
)
SPEC = importlib.util.spec_from_file_location("k7_background_steam", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load {BASE_PATH}")
K70 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = K70
SPEC.loader.exec_module(K70)


STEAM_T0_K = 0.905
DELTA_NEFF = 0.0535
KELVIN_TO_EV = 8.617333262e-5
HBAR_EV_S = 6.582119569e-16
MPC_M = 3.085677581491367e22
MPL_REDUCED_EV = 2.435e27
OPTIMISTIC_GRAVITY_PREFACTOR = 1.0


def main() -> int:
    base = K70.background(2.5e-4)
    p = base["p"]
    xs = base["xs"]
    e = base["e"]
    a = np.exp(xs)

    h0_s = 100.0 * p.h * 1000.0 / MPC_M
    h0_ev = h0_s * HBAR_EV_S
    h_ev = h0_ev * e
    temperature_ev = STEAM_T0_K * KELVIN_TO_EV / a

    gamma_grav_ev = (
        OPTIMISTIC_GRAVITY_PREFACTOR
        * temperature_ev**5
        / MPL_REDUCED_EV**4
    )
    gamma_grav_over_h = gamma_grav_ev / h_ev
    microscopic_frequency_over_h = temperature_ev / h_ev

    rows = []
    for fraction in K70.EPSILON_OVER_DELTA_GRID:
        epsilon = fraction * p.delta
        required_q1_over_h_rhof = (
            (1.0 - epsilon) * p.lam / e
            + 3.0 * epsilon * (1.0 - p.delta)
        )
        availability = gamma_grav_over_h / required_q1_over_h_rhof
        rows.append(
            {
                "epsilon_over_delta": fraction,
                "epsilon": epsilon,
                "required_Q1_over_HrhoF_recombination": float(
                    required_q1_over_h_rhof[0]
                ),
                "required_Q1_over_HrhoF_today": float(
                    required_q1_over_h_rhof[-1]
                ),
                "gravity_rate_over_H_recombination": float(
                    gamma_grav_over_h[0]
                ),
                "gravity_rate_over_H_today": float(
                    gamma_grav_over_h[-1]
                ),
                "maximum_available_to_required_rate_ratio": float(
                    np.max(availability)
                ),
                "minimum_orders_of_magnitude_rate_shortfall": float(
                    -math.log10(np.max(availability))
                ),
                "passes_required_rate": bool(np.all(availability >= 1.0)),
            }
        )

    checks = {
        "steam_background_already_registered": True,
        "steam_prediction_is_conditional_in_register_Q18_Q23": True,
        "microscopic_oscillation_scale_faster_than_H": bool(
            np.min(microscopic_frequency_over_h) > 1.0e6
        ),
        "gravity_only_rate_can_supply_K7_Q1": bool(
            all(row["passes_required_rate"] for row in rows)
        ),
    }
    dead = not checks["gravity_only_rate_can_supply_K7_Q1"]
    output = {
        "test": "A2-K7 K3.1-K2.2-K1a registered steam gravity-only rate",
        "inputs": {
            "steam_T0_K": STEAM_T0_K,
            "Delta_Neff": DELTA_NEFF,
            "reduced_Planck_mass_eV": MPL_REDUCED_EV,
            "gravity_prefactor": OPTIMISTIC_GRAVITY_PREFACTOR,
            "H0_eV": h0_ev,
            "z_start": float(np.exp(-xs[0]) - 1.0),
        },
        "kinematic_ratios": {
            "T_over_H_recombination": float(
                microscopic_frequency_over_h[0]
            ),
            "T_over_H_today": float(microscopic_frequency_over_h[-1]),
        },
        "rows": rows,
        "checks": checks,
        "verdict": (
            "DEAD_M014d1_REGISTERED_GRAVITON_STEAM_TOO_WEAK"
            if dead
            else "SURVIVES_GRAVITY_ONLY_RATE_GATE"
        ),
        "max_depth": "40/100",
        "parent_K7_accepted_score": "30/100",
        "next_if_dead": (
            "K3.1-K2.2-K1b: registered steam with a new non-gravitational "
            "coupling; it is a new hypothesis, not the gravity-only relic"
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 1 if dead else 0


if __name__ == "__main__":
    raise SystemExit(main())

