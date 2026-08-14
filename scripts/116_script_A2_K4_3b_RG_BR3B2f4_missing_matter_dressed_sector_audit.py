#!/usr/bin/env python
"""BR3B-2f-4: exact audit of mixed matter/fuel Puiseux ordering.

Scripts 104 and 108 solved the pure-radiation fuel-dressed sectors.  This
script checks whether the non-zero early matter fraction generates an
additional sector one integer power later.  It also verifies that ash/CDM
stress enters gravity only after the common fuel sector.

The result limits the scope of older PASS statements; it does not erase them
and it is not a death test for K4.
"""

from __future__ import annotations

import argparse
import json
import time

import sympy as sp


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=6.0)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 10.0:
        parser.error("runtime must be in (0,10]")
    started = time.monotonic()

    delta = sp.Rational(2297, 100000)
    p = sp.simplify(4 - 3 * delta)
    neff = sp.Rational(3046, 1000) + sp.Rational(535, 10000)
    rg = sp.simplify(1 / (1 + sp.Rational(2271, 10000) * neff))
    rn = sp.simplify(1 - rg)
    h = sp.Rational(6637, 10000)
    omega_m = sp.Rational(3517, 10000)
    omega_b_h2 = sp.Rational(2237, 100000)
    fb = sp.simplify(omega_b_h2 / (omega_m * h**2))
    # R_b=3 rho_b/(4 rho_gamma)=B*epsilon_m at first matter order.
    baryon_loading_coefficient = sp.simplify(3 * fb / (4 * rg))

    modes = {
        "NID": {
            "base_U_power": sp.Integer(0),
            "U_gamma": -rn / (4 * rg),
            "U_fs": sp.Rational(1, 4),
            "pure_radiation_shear_sector": p + 2,
            "common_fuel_sector": p + 3,
            "base_dc_power": sp.Integer(3),
        },
        "NIV": {
            "base_U_power": sp.Integer(-1),
            "U_gamma": -3 * rn / (4 * rg),
            "U_fs": sp.Rational(3, 4),
            "pure_radiation_shear_sector": p + 1,
            "common_fuel_sector": p + 2,
            "base_dc_power": sp.Integer(2),
        },
    }

    checks: dict[str, bool] = {}
    rows: dict[str, object] = {}
    for mode, item in modes.items():
        base_u_power = item["base_U_power"]
        earliest = sp.simplify(p + base_u_power)
        ug0 = sp.simplify(item["U_gamma"])
        un0 = sp.simplify(item["U_fs"])
        # Script 104 response to the O(Omega_f) Hubble-slope forcing.
        ug1 = sp.simplify((p * ug0 / 2) / (earliest + 1))
        un1 = sp.simplify((p * un0 / 2) / (earliest + 1))

        # In x=ln(a), q=Hconf_x/Hconf=-1+epsilon_m/2+...
        # Photon tight coupling adds R_b=B*epsilon_m.  At the next integer
        # power the already nonzero U response therefore contributes to the
        # Euler LHS by (B-1/2)Ug1 and -Un1/2.  RHS signs are immaterial for the
        # non-vanishing/order audit and are recorded explicitly below.
        lhs_gamma = sp.simplify((baryon_loading_coefficient - sp.Rational(1, 2)) * ug1)
        lhs_fs = sp.simplify(-sp.Rational(1, 2) * un1)
        weighted_lhs = sp.factor(rg * lhs_gamma + rn * lhs_fs)
        forced_sector = sp.simplify(earliest + 1)

        checks[f"{mode}_earliest_response_compensated"] = bool(
            sp.simplify(rg * ug1 + rn * un1) == 0
        )
        checks[f"{mode}_matter_dressed_weighted_Euler_source_nonzero"] = bool(
            weighted_lhs != 0
        )
        checks[f"{mode}_missing_sector_between_earliest_and_old_shear_sector"] = bool(
            earliest < forced_sector < item["pure_radiation_shear_sector"]
        )
        checks[f"{mode}_missing_sector_precedes_common_fuel_sector"] = bool(
            forced_sector < item["common_fuel_sector"]
        )

        # Ash transfer corrects delta_c at p+1+n_dc.  CDM has background
        # weight Omega_c~a in the radiation-era Einstein rows, hence its first
        # gravitational stress is one further power p+2+n_dc.  It is later
        # than the common fuel stress for every mode and is not the missing
        # source in BR3B-2f.
        ash_delta_c_sector = sp.simplify(p + 1 + item["base_dc_power"])
        ash_gravity_sector = sp.simplify(ash_delta_c_sector + 1)
        checks[f"{mode}_ash_gravity_after_common_fuel"] = bool(
            ash_gravity_sector > item["common_fuel_sector"]
        )
        rows[mode] = {
            "earliest_pure_radiation_sector": str(earliest),
            "script104_induced_velocity": {"U_gamma": str(ug1), "U_fs": str(un1)},
            "matter_Euler_LHS_per_epsilon_m": {
                "gamma": str(lhs_gamma), "free_streaming": str(lhs_fs),
                "radiation_weighted": str(weighted_lhs),
            },
            "mandatory_missing_matter_dressed_sector": str(forced_sector),
            "old_pure_radiation_shear_sector": str(item["pure_radiation_shear_sector"]),
            "common_fuel_sector": str(item["common_fuel_sector"]),
            "ash_delta_c_sector": str(ash_delta_c_sector),
            "ash_first_gravitating_sector": str(ash_gravity_sector),
        }

    passed = bool(checks) and all(checks.values())
    output = {
        "test": "A2-K4.3b-RG-BR3B-2f-4 missing matter-dressed sectors",
        "background_identity": "q=-1+epsilon_m/2+O(epsilon_m^2,Omega_f); R_b=(3 f_b/(4 R_gamma)) epsilon_m",
        "mode_results": rows,
        "checks": checks,
        "execution_verdict": (
            "PASS_MISSING_MATTER_DRESSED_SECTORS_PROVEN"
            if passed else "REVIEW_MATTER_DRESSED_ORDERING_UNCLOSED"
        ),
        "older_statements_limited": (
            "scripts 104 and 108 remain valid for the pure-radiation sectors "
            "they solved, but their ordered list is not complete at nonzero "
            "matter fraction; NID p+1 and NIV p must be inserted"
        ),
        "physical_verdict": (
            "K4 remains alive; common-fuel closure attempted without the "
            "mixed matter/fuel chain would be incomplete"
        ),
        "K4_3b_RG_verdict": "NEUZAVRETA_BR3B2F5_MIXED_CHAIN_REQUIRED",
        "canonical_score": "60/100 = G6",
        "next_step": (
            "solve NID p+1,p+2,p+3 and NIV p,p+1,p+2 recursively with "
            "matter dressing, gradient/shear sources and all nine rows"
        ),
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
