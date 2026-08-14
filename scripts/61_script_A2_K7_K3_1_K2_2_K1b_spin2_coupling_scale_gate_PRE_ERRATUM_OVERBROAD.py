#!/usr/bin/env python3
"""A2-K7 K3.1-K2.2-K1b: massless-spin-2 coupling-scale gate.

K1a showed that the registered graviton steam is far too weak if it couples
at the observed Planck scale.  K1b asks whether a new coupling can keep the
bath quanta massless spin-2 gravitons and supply the exact K7 rate.

For a universal spin-2 coupling represented by an effective scale M_eff,

    Gamma ~ T^5/M_eff^4.

This script solves for the largest M_eff that could meet the K7 source.  It
also reports the corresponding enhancement relative to the measured
reduced Planck scale.  A species-dependent massless-spin-2 coupling is not
a numerical alternative under the standard local Lorentz-invariant
S-matrix assumptions: the soft-graviton Ward identity requires universal
coupling.  A scalar/vector rate Gamma~g^4 T is quoted only as a diagnostic
showing where a genuinely new non-spin-2 bath would begin (K1c).
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

import numpy as np


BASE_PATH = Path(__file__).with_name(
    "60_script_A2_K7_K3_1_K2_2_K1a_registered_steam_gravity_rate.py"
)
SPEC = importlib.util.spec_from_file_location("k7_steam_spin2_scale", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load {BASE_PATH}")
K1A = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = K1A
SPEC.loader.exec_module(K1A)


def main() -> int:
    base = K1A.K70.background(2.5e-4)
    p = base["p"]
    xs = base["xs"]
    e = base["e"]
    a = np.exp(xs)

    h0_s = 100.0 * p.h * 1000.0 / K1A.MPC_M
    h0_ev = h0_s * K1A.HBAR_EV_S
    h_ev = h0_ev * e
    temperature_ev = K1A.STEAM_T0_K * K1A.KELVIN_TO_EV / a
    gamma_planck_over_h = (
        temperature_ev**5 / K1A.MPL_REDUCED_EV**4 / h_ev
    )

    rows = []
    for fraction in K1A.K70.EPSILON_OVER_DELTA_GRID:
        epsilon = fraction * p.delta
        q_required = (
            (1.0 - epsilon) * p.lam / e
            + 3.0 * epsilon * (1.0 - p.delta)
        )
        availability = gamma_planck_over_h / q_required

        # Gamma scales as M_eff^-4.  This is the largest allowed universal
        # scale if the rate is to be at least the registered source.
        m_eff_max = K1A.MPL_REDUCED_EV * availability**0.25
        coupling_enhancement = K1A.MPL_REDUCED_EV / m_eff_max
        effective_G_ratio = coupling_enhancement**2

        # If the carrier were a new scalar/vector with Gamma~g^4 T, this is
        # the minimum dimensionless coupling.  It is not a graviton result.
        g_nonspin2_min = (q_required * h_ev / temperature_ev) ** 0.25

        rows.append(
            {
                "epsilon_over_delta": fraction,
                "M_eff_max_eV_recombination": float(m_eff_max[0]),
                "M_eff_max_eV_today": float(m_eff_max[-1]),
                "minimum_universal_coupling_enhancement": float(
                    np.max(coupling_enhancement)
                ),
                "minimum_effective_G_over_GN": float(
                    np.max(effective_G_ratio)
                ),
                "nonspin2_g_min_recombination": float(g_nonspin2_min[0]),
                "nonspin2_g_min_today": float(g_nonspin2_min[-1]),
            }
        )

    largest_today_scale = max(row["M_eff_max_eV_today"] for row in rows)
    checks = {
        "universal_scale_compatible_with_measured_Mpl": bool(
            largest_today_scale >= 0.1 * K1A.MPL_REDUCED_EV
        ),
        "species_dependent_massless_spin2_coupling_allowed_under_soft_theorem": False,
        "new_nonspin2_carrier_is_same_as_registered_graviton_steam": False,
    }
    dead = not any(checks.values())
    output = {
        "test": "A2-K7 K3.1-K2.2-K1b massless-spin-2 coupling scale",
        "assumptions": {
            "local_Lorentz_invariant_unitary_S_matrix": True,
            "massless_helicity_2_bath_quantum": True,
            "soft_graviton_universality_applies": True,
            "observed_reduced_Planck_mass_eV": K1A.MPL_REDUCED_EV,
        },
        "rows": rows,
        "checks": checks,
        "verdict": (
            "DEAD_M014d2_NONUNIVERSAL_MASSLESS_SPIN2_COUPLING_INCONSISTENT"
            if dead
            else "SURVIVES_SPIN2_COUPLING_GATE"
        ),
        "max_depth": "41/100",
        "parent_K7_accepted_score": "30/100",
        "next_if_dead": (
            "K3.1-K2.2-K1c: a genuinely new non-spin-2 light bath with "
            "its own action, Delta N_eff, pressure and coupling"
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 1 if dead else 0


if __name__ == "__main__":
    raise SystemExit(main())

