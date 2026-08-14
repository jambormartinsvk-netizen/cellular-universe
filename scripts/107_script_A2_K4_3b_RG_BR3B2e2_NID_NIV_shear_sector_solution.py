#!/usr/bin/env python
"""BR3B-2e-2: solve the first NID/NIV density-gradient-shear sectors.

Uses the exact standard hierarchy recurrence.  For NIV the self-consistent
CAMB-audited coefficient sigma=t/(4 R_nu+5) is used; the isolated CLASS-master
4 R_nu+15 coefficient is excluded by script 106.  The earlier induced
relative-velocity modes from script 104 are included in the gradient source.

This closes the sectors p+2 (NID) and p+1 (NIV), not the later common fuel
sector or l>=3 feedback.
"""

from __future__ import annotations

import argparse
import json
import time

import sympy as sp


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=10.0)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 15.0:
        parser.error("runtime must be in (0, 15]")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("BR3B-2e-2 deadline exceeded")

    delta = sp.Rational(2297, 100000)
    p = sp.simplify(4 - 3 * delta)
    neff = sp.Rational(3046, 1000) + sp.Rational(535, 10000)
    rg = sp.simplify(1 / (1 + sp.Rational(2271, 10000) * neff))
    rf = sp.simplify(1 - rg)

    # Coefficients of the standard base sector, stripped of the common
    # (k tau)^m factor. U_low occurs two powers earlier because s^2~(k tau)^2.
    base = {
        "NID": {
            "m": sp.Integer(2),
            "dg": rf / (6 * rg),
            "dn": -sp.Rational(1, 6),
            "ug_low": -rf / (4 * rg),
            "un_low": sp.Rational(1, 4),
            "sigma": 1 / (2 * (4 * rf + 15)),
            "eta": -rf / (6 * (4 * rf + 15)),
            "fuel_power": p + 3,
        },
        "NIV": {
            "m": sp.Integer(1),
            "dg": rf / rg,
            "dn": -sp.Integer(1),
            "ug_low": -3 * rf / (4 * rg),
            "un_low": sp.Rational(3, 4),
            "sigma": 1 / (4 * rf + 5),
            "eta": -rf / (4 * rf + 5),
            "fuel_power": p + 2,
        },
    }

    checks: dict[str, bool] = {}
    results: dict[str, object] = {}
    for mode, item in base.items():
        m = item["m"]
        r = sp.simplify(p + m)
        dg0, dn0 = sp.simplify(item["dg"]), sp.simplify(item["dn"])
        ugl, unl = sp.simplify(item["ug_low"]), sp.simplify(item["un_low"])
        sig0, eta0 = sp.simplify(item["sigma"]), sp.simplify(item["eta"])
        etax0 = sp.simplify(m * eta0)
        ug0 = sp.simplify(dg0 / (4 * (m + 1)))
        un0 = sp.simplify((dn0 / 4 - sig0) / (m + 1))

        early_power = sp.simplify(p + m - 2)
        early_factor = sp.simplify(p / (2 * (early_power + 1)))
        uge = sp.simplify(early_factor * ugl)
        une = sp.simplify(early_factor * unl)

        # Full fixed O(y) source at power r=p+m.
        jgc = sp.simplify(sp.Rational(4, 3) * (ugl - uge))
        jnc = sp.simplify(sp.Rational(4, 3) * (unl - une))
        jge = sp.simplify(p * ug0 / 2)
        jne = sp.simplify(p * un0 / 2)
        jns = sp.simplify(sp.Rational(8, 15) * (uge - ugl))
        c00 = sp.Integer(0)
        c0i = sp.simplify(-etax0)
        ctr = sp.Integer(0)
        ctl = sp.simplify(-3 * p * etax0 + 12 * rf * sig0)
        source = sp.Matrix([jgc, jge, jnc, jns, jne, c00, c0i, ctr, ctl])

        matrix = sp.Matrix([
            [sp.Rational(2, 3), 0, r, 0, 0, 0, 0],
            [0, 0, -sp.Rational(1, 4), 0, r + 1, 0, 0],
            [sp.Rational(2, 3), 0, 0, r, 0, 0, 0],
            [-sp.Rational(4, 15), -sp.Rational(8, 5) * r, 0, 0, 0, 0, 2 * r],
            [0, 0, 0, -sp.Rational(1, 4), 0, r + 1, 1],
            [-sp.Rational(1, 2), 0, sp.Rational(3, 2) * rg,
             sp.Rational(3, 2) * rf, 0, 0, 0],
            [0, r, 0, 0, -2 * rg, -2 * rf, 0],
            [r + 1, 0, 3 * rg, 3 * rf, 0, 0, 0],
            [r + 1, 6 * r * (r + 1), 0, 0, 0, 0, 12 * rf],
        ])

        # Audit the standard coefficient sector before using it as a source.
        checks[f"{mode}_base_density_compensation"] = bool(sp.simplify(rg * dg0 + rf * dn0) == 0)
        checks[f"{mode}_base_continuities"] = bool(
            sp.simplify(m * dg0 + sp.Rational(4, 3) * ugl) == 0
            and sp.simplify(m * dn0 + sp.Rational(4, 3) * unl) == 0
        )
        checks[f"{mode}_base_Euler_equations"] = bool(
            sp.simplify((m + 1) * ug0 - dg0 / 4) == 0
            and sp.simplify((m + 1) * un0 - dn0 / 4 + sig0) == 0
        )
        checks[f"{mode}_base_shear_equation"] = bool(
            sp.simplify(2 * m * sig0 - sp.Rational(8, 5) * m * eta0
                        - sp.Rational(8, 15) * unl) == 0
        )
        checks[f"{mode}_base_0i_constraint"] = bool(
            sp.simplify(etax0 - 2 * (rg * ug0 + rf * un0)) == 0
        )
        checks[f"{mode}_base_traceless_constraint"] = bool(
            sp.simplify(6 * (m + 1) * etax0 + 12 * rf * sig0) == 0
        )

        bianchi = [sp.factor((vector.T * source)[0]) for vector in matrix.T.nullspace()]
        rank_a = int(matrix.rank())
        rank_aug = int(matrix.row_join(source).rank())
        solution_set = sp.linsolve((matrix, source)) if rank_a == rank_aug else sp.EmptySet
        solution = list(solution_set)[0] if solution_set != sp.EmptySet else None
        checks[f"{mode}_both_fractional_Bianchi_residuals_zero"] = bool(
            len(bianchi) == 2 and all(sp.simplify(value) == 0 for value in bianchi)
        )
        checks[f"{mode}_fractional_response_rank_compatible"] = bool(rank_a == rank_aug == 7)
        checks[f"{mode}_fractional_solution_finite"] = bool(
            solution is not None and all(value.is_finite is not False for value in solution)
        )
        l3_feedback_power = sp.simplify(p + m + 2)
        checks[f"{mode}_l3_feedback_follows_common_fuel_sector"] = bool(
            l3_feedback_power > item["fuel_power"]
        )

        results[mode] = {
            "base_power_m": str(m),
            "fractional_sector_power": str(r),
            "earlier_velocity_power": str(early_power),
            "base_coefficients": {
                "delta_gamma": str(dg0), "delta_fs": str(dn0),
                "U_gamma_low": str(ugl), "U_fs_low": str(unl),
                "U_gamma_m": str(ug0), "U_fs_m": str(un0),
                "sigma_fs": str(sig0), "eta": str(eta0),
            },
            "earlier_induced_velocity": {"U_gamma": str(uge), "U_fs": str(une)},
            "fixed_source": {
                "Jgc": str(jgc), "Jge": str(jge), "Jnc": str(jnc),
                "Jns": str(jns), "Jne": str(jne), "C00": str(c00),
                "C0i": str(c0i), "Ctr": str(ctr), "Ctl": str(ctl),
            },
            "Bianchi_residuals": [str(value) for value in bianchi],
            "rank_A": rank_a,
            "rank_augmented": rank_aug,
            "solution_order": ["h_x", "eta", "delta_gamma", "delta_fs",
                               "U_gamma", "U_fs", "sigma_fs"],
            "fractional_solution": ([str(sp.factor(value)) for value in solution]
                                    if solution is not None else None),
            "common_fuel_sector_power": str(item["fuel_power"]),
            "first_l3_feedback_power": str(l3_feedback_power),
        }
        deadline()

    passed = all(checks.values())
    output = {
        "test": "A2-K4.3b-RG-BR3B-2e-2 NID/NIV shear-sector solution",
        "NIV_shear_convention": "sigma_NIV=(k tau)/(4Rnu+5), fixed by Euler+CAMB script 106",
        "checks": checks,
        "mode_results": results,
        "execution_verdict": ("PASS_NID_NIV_FIRST_SHEAR_SECTORS"
                              if passed else "FAIL_OR_REVIEW_BR3B2E2"),
        "physical_verdict": "the first shear-bearing NID/NIV fractional sectors have unique finite rank-compatible responses",
        "scope_limit": "common fuel sectors and later l>=3 feedback are not yet jointly solved",
        "K4_3b_RG_verdict": "NEUZAVRETA_BR3B2F_ORDERED_COMMON_FUEL_AND_L3_RECURSION_REQUIRED",
        "canonical_score": "60/100 = G6",
        "next_step": "BR3B-2f solve the common fuel sector after injecting the completed earlier sectors; then append later l3 recursion",
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
