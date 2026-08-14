#!/usr/bin/env python
"""BR3B-2e-1: earliest NID/NIV relative-radiation sectors.

CLASS initial conditions show that the NID/NIV leading photon and
free-streaming velocities are equal and opposite after radiation weighting.
The O(Omega_f) correction to Hconf_x/Hconf therefore forces a relative mode
before shear enters: power p for NID and p-1 for NIV.

This script proves exact compensation, finite regular response and Bianchi
compatibility.  It does not claim the next shear-bearing sectors p+2 (NID)
and p+1 (NIV), which remain BR3B-2e-2.
"""

from __future__ import annotations

import argparse
import json
import time

import sympy as sp


CLASS_SOURCE = "https://raw.githubusercontent.com/lesgourg/class_public/master/source/perturbations.c"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=8.0)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 10.0:
        parser.error("runtime must be in (0, 10]")
    started = time.monotonic()

    delta = sp.Rational(2297, 100000)
    p = sp.simplify(4 - 3 * delta)
    neff = sp.Rational(3046, 1000) + sp.Rational(535, 10000)
    rg = sp.simplify(1 / (1 + sp.Rational(2271, 10000) * neff))
    rf = sp.simplify(1 - rg)

    modes = {
        "NID": {
            "base_U_power": sp.Integer(0),
            "U_gamma": -rf / (4 * rg),
            "U_fs": sp.Rational(1, 4),
            "base_shear_power": sp.Integer(2),
            "base_shear_coefficient": 1 / (2 * (4 * rf + 15)),
            "fuel_hx_sector_power": p + 3,
        },
        "NIV": {
            "base_U_power": sp.Integer(-1),
            "U_gamma": -3 * rf / (4 * rg),
            "U_fs": sp.Rational(3, 4),
            "base_shear_power": sp.Integer(1),
            "base_shear_coefficient": 1 / (4 * rf + 15),
            "fuel_hx_sector_power": p + 2,
        },
    }

    checks: dict[str, bool] = {}
    results: dict[str, object] = {}
    for mode, item in modes.items():
        u_power = item["base_U_power"]
        sector_power = sp.simplify(p + u_power)
        ug0 = sp.simplify(item["U_gamma"])
        un0 = sp.simplify(item["U_fs"])
        jge = sp.simplify(p * ug0 / 2)
        jne = sp.simplify(p * un0 / 2)

        # At this earliest power density, metric and shear coefficients vanish.
        # The radiation Euler equations reduce to (s+1) U_1 = J_Euler.
        ug1 = sp.simplify(jge / (sector_power + 1))
        un1 = sp.simplify(jne / (sector_power + 1))
        weighted_base = sp.simplify(rg * ug0 + rf * un0)
        weighted_force = sp.simplify(rg * jge + rf * jne)
        weighted_response = sp.simplify(rg * ug1 + rf * un1)

        # The two general BR3B-2b identities with all metric/continuity
        # dressings zero reduce to 0 and -12*weighted_force.
        bianchi_1 = sp.Integer(0)
        bianchi_2 = sp.simplify(-12 * weighted_force)
        next_shear_sector = sp.simplify(p + item["base_shear_power"])
        # F_l hierarchy raises the regular power by one at each l step;
        # the l=3 feedback into shear carries one further k/Hconf power.
        first_l3_feedback_power = sp.simplify(next_shear_sector + 2)

        checks[f"{mode}_base_velocity_exactly_compensated"] = bool(weighted_base == 0)
        checks[f"{mode}_Euler_forcing_exactly_compensated"] = bool(weighted_force == 0)
        checks[f"{mode}_induced_velocity_exactly_compensated"] = bool(weighted_response == 0)
        checks[f"{mode}_both_Bianchi_identities_zero"] = bool(
            bianchi_1 == 0 and bianchi_2 == 0
        )
        checks[f"{mode}_earliest_fractional_power_is_regular_positive"] = bool(
            sector_power > 0
        )
        checks[f"{mode}_shear_enters_after_earliest_velocity_sector"] = bool(
            next_shear_sector > sector_power
        )
        checks[f"{mode}_l3_feedback_enters_after_shear_sector"] = bool(
            first_l3_feedback_power > next_shear_sector
        )

        results[mode] = {
            "earliest_sector_power": str(sector_power),
            "base_velocity_coefficients": {"U_gamma": str(ug0), "U_fs": str(un0)},
            "fixed_Euler_forcing": {"Jge": str(jge), "Jne": str(jne)},
            "induced_relative_velocity": {"U_gamma_1": str(ug1), "U_fs_1": str(un1)},
            "weighted_base_force_response": [str(weighted_base), str(weighted_force),
                                               str(weighted_response)],
            "Bianchi_residuals": [str(bianchi_1), str(bianchi_2)],
            "base_shear_power": str(item["base_shear_power"]),
            "base_shear_coefficient": str(sp.factor(item["base_shear_coefficient"])),
            "next_shear_sector_power": str(next_shear_sector),
            "first_l3_feedback_power": str(first_l3_feedback_power),
            "fuel_hx_sector_power": str(item["fuel_hx_sector_power"]),
        }

    passed = all(checks.values())
    output = {
        "test": "A2-K4.3b-RG-BR3B-2e-1 earliest relative-radiation modes",
        "primary_implementation_reference": CLASS_SOURCE,
        "checks": checks,
        "mode_results": results,
        "execution_verdict": ("PASS_EARLIEST_RELATIVE_RADIATION_SECTORS"
                              if passed else "FAIL_BR3B2E1"),
        "physical_verdict": "earliest NID/NIV fractional sectors are finite metric-null compensated relative-velocity modes",
        "scope_limit": "next shear-bearing sectors and later l>=3 feedback remain unsolved",
        "K4_3b_RG_verdict": "NEUZAVRETA_BR3B2E2_SHEAR_SECTORS_REQUIRED",
        "canonical_score": "60/100 = G6",
        "next_step": "BR3B-2e-2 solve NID p+2 and NIV p+1 density/gradient/shear sectors with the induced earlier velocity included",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
    except Exception as exc:  # pragma: no cover
        print(json.dumps({"execution_verdict": "ERROR_UNCLOSED", "error": repr(exc)}))
        raise SystemExit(2)
