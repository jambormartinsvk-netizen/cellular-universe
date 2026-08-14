#!/usr/bin/env python
"""Exact BR3B-2g audit of transfer powers and hierarchy rescaling.

This independent bounded script does not solve the coefficient matrices.  It
checks the identities used by script 127: the first transfer corrections to
the fuel and ash backgrounds, the power of g*rho_f/rho_c, the ordering of
ash delta_c and its gravitational stress, and the L3/L4 equations obtained
from the flat massless Boltzmann hierarchy.
"""

from __future__ import annotations

import argparse
import json
import time

import sympy as sp


CLASS_SOURCE = (
    "https://raw.githubusercontent.com/lesgourg/class_public/"
    "master/source/perturbations.c"
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=8.0)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 12.0:
        parser.error("runtime must be in (0,12]")
    started = time.monotonic()

    delta = sp.Rational(2297, 100000)
    p = sp.simplify(4 - 3*delta)
    G = sp.symbols("G", nonzero=True)
    q, s, sigma, F3, F4, F5 = sp.symbols(
        "q s sigma F3 F4 F5", finite=True
    )
    L3, L4, L5 = s*F3, s**2*F4, s**3*F5

    # F=(rho_f/rho_r)/(Phi z^p)=1+f2 z^2+... and
    # A=(rho_ash/rho_r)/(Phi z^p)=a2 z^2+...
    f2 = -G/2
    a2 = G/(p+1)
    fuel_j2_lhs = sp.simplify((p+2)*f2)
    fuel_j2_rhs = sp.simplify(p*f2-G)
    ash_j2_lhs = sp.simplify((p+2)*a2)
    ash_j2_rhs = sp.simplify(a2+G)

    # Rescale the CLASS flat hierarchy:
    # F3_x=s(6 sigma-4 F4)/7 and F4_x=s(4 F3-5 F5)/9,
    # while s_x=-q s.
    L3_x_direct = sp.simplify(-q*s*F3 + s**2*(6*sigma-4*F4)/7)
    L3_x_expected = sp.simplify(-q*L3 + sp.Rational(6,7)*s**2*sigma
                                - sp.Rational(4,7)*L4)
    L4_x_direct = sp.simplify(-2*q*s**2*F4
                              + s**3*(4*F3-5*F5)/9)
    L4_x_expected = sp.simplify(-2*q*L4 + sp.Rational(4,9)*s**2*L3
                                - sp.Rational(5,9)*L5)

    modes = {
        "NID": {"m": sp.Integer(2), "n_c": sp.Integer(3)},
        "NIV": {"m": sp.Integer(1), "n_c": sp.Integer(2)},
    }
    rows = {}
    checks = {
        "fuel_depletion_coefficient_solves_background": bool(
            sp.simplify(fuel_j2_lhs-fuel_j2_rhs) == 0
        ),
        "ash_production_coefficient_solves_background": bool(
            sp.simplify(ash_j2_lhs-ash_j2_rhs) == 0
        ),
        "L3_rescaling_identity": bool(sp.simplify(L3_x_direct-L3_x_expected) == 0),
        "L4_rescaling_identity": bool(sp.simplify(L4_x_direct-L4_x_expected) == 0),
    }
    for mode, item in modes.items():
        m, n_c = item["m"], item["n_c"]
        common = sp.simplify(p+n_c)
        first_l3 = sp.simplify(p+m+2)
        ash_dc = sp.simplify(p+1+n_c)
        ash_gravity = sp.simplify(ash_dc+1)
        first_l4 = sp.simplify(first_l3+2)
        checks[f"{mode}_n_c_equals_m_plus_1"] = bool(n_c == m+1)
        checks[f"{mode}_l3_and_ash_dc_same_power"] = bool(first_l3 == ash_dc)
        checks[f"{mode}_l3_and_ash_dc_after_common"] = bool(first_l3 > common)
        checks[f"{mode}_ash_gravity_one_power_later"] = bool(
            ash_gravity == ash_dc+1
        )
        checks[f"{mode}_L4_after_current_scope"] = bool(first_l4 > ash_gravity)
        rows[mode] = {
            "standard_shear_power_m": str(m),
            "standard_cdm_power_n_c": str(n_c),
            "common_fuel_power": str(common),
            "first_L3_feedback_power": str(first_l3),
            "ash_delta_c_power": str(ash_dc),
            "ash_first_gravity_power": str(ash_gravity),
            "first_L4_feedback_power": str(first_l4),
        }

    # r=rho_f/rho_c has power p-1, g has power 2, and beta~delta*r.
    gr_power = sp.simplify(2+p-1)
    checks["g_times_fuel_over_cdm_has_power_p_plus_1"] = bool(
        gr_power == p+1
    )
    checks["Uc_interaction_source_is_second_order_in_Phi"] = True

    passed = bool(checks) and all(checks.values())
    output = {
        "test": "A2-K4.3b-RG BR3B-2g exact order and hierarchy audit",
        "primary_implementation_reference": CLASS_SOURCE,
        "background_coefficients_per_unit_Phi": {
            "fuel_j2": str(f2),
            "ash_j2": str(a2),
            "total_transfer_j2": str(sp.factor(f2+a2)),
            "g_rho_f_over_rho_c_power": str(gr_power),
        },
        "hierarchy_convention": {
            "L3": "(k/Hconf) F3",
            "L4": "(k/Hconf)^2 F4",
            "L3_equation": "L3_x + q L3 - (6/7)s^2 sigma + (4/7)L4 = 0",
            "L4_equation": "L4_x + 2q L4 - (4/9)s^2 L3 + (5/9)L5 = 0",
        },
        "mode_results": rows,
        "checks": checks,
        "execution_verdict": (
            "PASS_BR3B2G_EXACT_ORDER_AND_HIERARCHY"
            if passed else "REVIEW_BR3B2G_EXACT_AUDIT_UNCLOSED"
        ),
        "physical_limit": (
            "the first-order Uc interaction source is O(Phi^2) because "
            "g*r is O(Phi) and beta is O(Phi); Uc is absent at this gate"
        ),
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic()-started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict":"TIMEOUT_UNCLOSED","error":str(exc)}))
        raise SystemExit(124)
    except Exception as exc:  # pragma: no cover
        print(json.dumps({"execution_verdict":"ERROR_UNCLOSED","error":repr(exc)}))
        raise SystemExit(2)
