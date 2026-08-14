#!/usr/bin/env python3
"""A2-K7 K3.1-K2.2-K1a2a incoherent KMS graviton-transition gate.

Erratum scope:
The T^5/M_Pl^4 estimate in script 60 tests a relativistic gravitational
2->2 / graviton-bath scattering channel.  It is not a universal bound on
emission from a massive or coherent fuel/mediator transition.

This script tests the distinct *incoherent single-transition* possibility.
It deliberately uses the optimistic dimensional envelope

    Gamma_1 <= C * omega^3/Mbar_Pl^2,  C=1,

which is less suppressive than a quadrupole transition with additional
selection-rule or form-factor powers.  For a local thermal/KMS bath, an
unsuppressed reverse absorption channel requires omega/T not to be large.
The pre-registered thermal window is omega<=T.  The script compares the
maximum rate in that window with the exact K7 Q1 source, and separately
solves for the omega that would be required if spontaneous emission were
allowed to leave the KMS window.

Collective/coherent enhancement is NOT excluded here; it is K1a2b.
High-frequency spontaneous emission with omega>>T belongs to the vacuum or
coloured non-equilibrium branch K2, not to this local thermal K1 branch.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np


BASE_PATH = Path(__file__).with_name(
    "60_script_A2_K7_K3_1_K2_2_K1a_registered_steam_gravity_rate.py"
)
SPEC = importlib.util.spec_from_file_location("k7_steam_transition", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load {BASE_PATH}")
K1A = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = K1A
SPEC.loader.exec_module(K1A)


OPTIMISTIC_MATRIX_ELEMENT = 1.0
KMS_MAX_OMEGA_OVER_T = 1.0


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

    gamma_thermal_max_over_h = (
        OPTIMISTIC_MATRIX_ELEMENT
        * (KMS_MAX_OMEGA_OVER_T * temperature_ev) ** 3
        / K1A.MPL_REDUCED_EV**2
        / h_ev
    )

    rows = []
    for fraction in K1A.K70.EPSILON_OVER_DELTA_GRID:
        epsilon = fraction * p.delta
        q_required = (
            (1.0 - epsilon) * p.lam / e
            + 3.0 * epsilon * (1.0 - p.delta)
        )
        enhancement_needed = q_required / gamma_thermal_max_over_h
        omega_required_ev = (
            q_required * h_ev * K1A.MPL_REDUCED_EV**2
            / OPTIMISTIC_MATRIX_ELEMENT
        ) ** (1.0 / 3.0)
        omega_over_t = omega_required_ev / temperature_ev
        log10_kms_absorption = -omega_over_t / math.log(10.0)

        rows.append(
            {
                "epsilon_over_delta": fraction,
                "required_Q1_over_HrhoF_recombination": float(q_required[0]),
                "required_Q1_over_HrhoF_today": float(q_required[-1]),
                "max_incoherent_KMS_rate_over_H_recombination": float(
                    gamma_thermal_max_over_h[0]
                ),
                "max_incoherent_KMS_rate_over_H_today": float(
                    gamma_thermal_max_over_h[-1]
                ),
                "minimum_collective_or_matrix_enhancement_recombination": float(
                    enhancement_needed[0]
                ),
                "minimum_collective_or_matrix_enhancement_today": float(
                    enhancement_needed[-1]
                ),
                "omega_required_eV_recombination": float(omega_required_ev[0]),
                "omega_required_eV_today": float(omega_required_ev[-1]),
                "omega_required_over_T_recombination": float(omega_over_t[0]),
                "omega_required_over_T_today": float(omega_over_t[-1]),
                "log10_reverse_absorption_factor_recombination": float(
                    log10_kms_absorption[0]
                ),
                "log10_reverse_absorption_factor_today": float(
                    log10_kms_absorption[-1]
                ),
                "incoherent_KMS_rate_passed": bool(
                    np.all(gamma_thermal_max_over_h >= q_required)
                ),
            }
        )

    checks = {
        "optimistic_incoherent_rate_meets_K7_with_omega_le_T": bool(
            all(row["incoherent_KMS_rate_passed"] for row in rows)
        ),
        "required_high_frequency_transition_has_unsuppressed_reverse_absorption": bool(
            all(
                row["omega_required_over_T_recombination"] <= 1.0
                and row["omega_required_over_T_today"] <= 1.0
                for row in rows
            )
        ),
        "collective_coherent_channel_tested": False,
        "fuel_mediator_transition_spectrum_derived": False,
    }
    dead_leaf = (
        not checks["optimistic_incoherent_rate_meets_K7_with_omega_le_T"]
        and not checks[
            "required_high_frequency_transition_has_unsuppressed_reverse_absorption"
        ]
    )
    output = {
        "test": "A2-K7 K3.1-K2.2-K1a2a incoherent KMS graviton transition",
        "scope": {
            "single_incoherent_transition": True,
            "optimistic_width_envelope": "Gamma=omega^3/Mbar_Pl^2",
            "KMS_thermal_window": "omega/T<=1",
            "collective_enhancement_excluded_by_test": False,
            "high_frequency_vacuum_emission_excluded_by_test": False,
        },
        "rows": rows,
        "checks": checks,
        "verdict": (
            "DEAD_M014d1b_INCOHERENT_KMS_GRAVITON_TRANSITION"
            if dead_leaf
            else "SURVIVES_INCOHERENT_KMS_TRANSITION_GATE"
        ),
        "max_depth": "42/100",
        "parent_K7_accepted_score": "30/100",
        "next_if_dead": (
            "K3.1-K2.2-K1a2b coherent collective graviton emission/absorption; "
            "omega>>T spontaneous emission is reclassified to coloured K2"
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 1 if dead_leaf else 0


if __name__ == "__main__":
    raise SystemExit(main())

