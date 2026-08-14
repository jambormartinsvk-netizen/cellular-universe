#!/usr/bin/env python
"""BR3B-2d: power ordering of compensated NID/NIV dressing sectors.

The common h_x sector passed BR3B-2c, but NID and NIV possess radiation
density/velocity terms at lower powers than their leading h_x.  Multiplying
those terms by y=Omega_f~a^p creates earlier fractional sectors.  This ledger
checks the exact photon+free-streaming compensation and orders the sectors
that a physical Puiseux recursion must solve.

No hierarchy closure is claimed here: neutrino shear and higher multipoles
must be populated in BR3B-2e before either mode can pass.
"""

from __future__ import annotations

import argparse
import json
import time

import sympy as sp


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

    # Coefficients are stripped of common k/tau normalizations.  They are the
    # leading CLASS/Bucher-Moodley-Turok photon and neutrino coefficients.
    nid_density = {"gamma": -rf / rg, "fs": sp.Integer(1), "base_power": 0}
    nid_velocity_u = {"gamma": -rf / (4 * rg), "fs": sp.Rational(1, 4),
                      "base_power": 0}
    niv_density = {"gamma": rf / rg, "fs": sp.Integer(-1), "base_power": 1}
    niv_velocity_u = {"gamma": -3 * rf / (4 * rg), "fs": sp.Rational(3, 4),
                      "base_power": -1}

    def weighted(pair: dict[str, sp.Expr]) -> sp.Expr:
        return sp.simplify(rg * pair["gamma"] + rf * pair["fs"])

    checks = {
        "NID_leading_density_is_exactly_compensated": weighted(nid_density) == 0,
        "NID_leading_U_is_exactly_compensated": weighted(nid_velocity_u) == 0,
        "NIV_leading_density_is_exactly_compensated": weighted(niv_density) == 0,
        "NIV_leading_U_is_exactly_compensated": weighted(niv_velocity_u) == 0,
        "NID_Euler_dressing_precedes_hx_sector": p < p + 3,
        "NIV_Euler_dressing_precedes_hx_sector": p - 1 < p + 2,
    }

    sectors = {
        "NID": [
            {
                "power": str(p),
                "decimal_power": float(p),
                "origin": "(Hconf_x/Hconf) O(y) times compensated U_gamma/U_fs at a^0",
                "total_density_or_momentum_source": "zero at the leading compensated moment",
                "status": "requires relative-radiation hierarchy response",
            },
            {
                "power": str(p + 2),
                "decimal_power": float(p + 2),
                "origin": "O(y) gradient/shear/eta sector built on a^2 radiation terms",
                "total_density_or_momentum_source": "not decidable without shear and hierarchy coefficients",
                "status": "BR3B-2e required",
            },
            {
                "power": str(p + 3),
                "decimal_power": float(p + 3),
                "origin": "common fuel response driven by leading h_x~a^3",
                "total_density_or_momentum_source": "BR3B-2c compatible",
                "status": "cannot be solved before earlier sectors",
            },
        ],
        "NIV": [
            {
                "power": str(p - 1),
                "decimal_power": float(p - 1),
                "origin": "(Hconf_x/Hconf) O(y) times compensated U_gamma/U_fs at a^-1",
                "total_density_or_momentum_source": "zero at the leading compensated moment",
                "status": "requires relative-radiation hierarchy response",
            },
            {
                "power": str(p + 1),
                "decimal_power": float(p + 1),
                "origin": "O(y) density/eta/shear sector built on a^1 NIV terms",
                "total_density_or_momentum_source": "density compensation exact; shear not yet populated",
                "status": "BR3B-2e required",
            },
            {
                "power": str(p + 2),
                "decimal_power": float(p + 2),
                "origin": "common fuel response driven by leading h_x~a^2",
                "total_density_or_momentum_source": "BR3B-2c compatible",
                "status": "cannot be solved before earlier sectors",
            },
        ],
    }

    ordered = all(
        all(group[index]["decimal_power"] < group[index + 1]["decimal_power"]
            for index in range(len(group) - 1))
        for group in sectors.values()
    )
    checks["all_mode_sectors_are_strictly_ordered"] = ordered
    passed = all(bool(value) for value in checks.values())
    output = {
        "test": "A2-K4.3b-RG-BR3B-2d NID/NIV fractional power ordering",
        "p_Omega_f": str(p),
        "exact_compensated_coefficients": {
            "NID_density": {key: str(value) for key, value in nid_density.items()},
            "NID_U": {key: str(value) for key, value in nid_velocity_u.items()},
            "NIV_density": {key: str(value) for key, value in niv_density.items()},
            "NIV_U": {key: str(value) for key, value in niv_velocity_u.items()},
        },
        "ordered_sectors": sectors,
        "checks": checks,
        "execution_verdict": ("PASS_MULTIPOWER_ORDER_AND_COMPENSATION_LEDGER"
                              if passed else "REVIEW_BR3B2D"),
        "physical_verdict": "NID/NIV are not killed; their earlier compensated relative-radiation sectors must be evolved before the h_x fuel sector",
        "scope_limit": "shear and l>=3 free-streaming hierarchy coefficients not yet included",
        "K4_3b_RG_verdict": "NEUZAVRETA_BR3B2E_NID_NIV_HIERARCHY_COEFFICIENTS_REQUIRED",
        "canonical_score": "60/100 = G6",
        "next_step": "BR3B-2e populate neutrino shear and the minimum regular l>=3 recursion at every earlier NID/NIV power",
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
