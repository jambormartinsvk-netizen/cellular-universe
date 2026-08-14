#!/usr/bin/env python
"""BR3B-2f-3: bounded Frobenius recurrence for standard NID/NIV seeds.

Scripts 110 and 111 showed that double-precision subtraction cannot reliably
extract the high-order NID/NIV coefficients needed by the common fuel sector.
This independent route solves the regular synchronous-gauge radiation+matter
series coefficient-by-coefficient.  It includes tightly coupled baryons, CDM,
free-streaming shear and the first l=3 multipole.  The solved series is then
converted from y=k*tau to z proportional to the physical scale factor,

    z = y + (mu/4) y^2,  mu=omega_m/k,

before h_x, eta_x and U=Hconf*theta/k^2 ratios are read.

The finite series is validated against the published CLASS leading NID
coefficients and the CAMB-self-consistent NIV coefficients audited in script
106.  A numerical SVD solves the overdetermined linear coefficient ledger;
rank, condition and scaled residual are explicit.  Any numerical failure is
REVIEW_UNCLOSED, never a physical death verdict.
"""

from __future__ import annotations

import argparse
import json
import time

import numpy as np
import sympy as sp


VARIABLES = ("h", "eta", "dg", "dn", "db", "dc", "Vg", "Vn", "sig", "F3")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=25.0)
    parser.add_argument("--order", type=int, default=5)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 30.0:
        parser.error("runtime must be in (0, 30]")
    if not 5 <= args.order <= 6:
        parser.error("order must be 5 or 6")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("BR3B-2f-3 Frobenius deadline exceeded")

    order = args.order
    y, z = sp.symbols("y z")
    h0 = 0.6637
    omega_m0 = 0.3517
    ombh2 = 0.02237
    total_matter_h2 = omega_m0 * h0**2
    fb = ombh2 / total_matter_h2
    neff = 3.046 + 0.0535
    rnu = 0.2271 * neff / (1 + 0.2271 * neff)
    rg = 1 - rnu
    omega_gamma_h2 = 2.47282e-5
    omega_r0 = omega_gamma_h2 * (1 + 0.2271 * neff) / h0**2
    hubble0_mpc = 100 * h0 / 299792.458
    omega_parameter = hubble0_mpc * omega_m0 / np.sqrt(omega_r0)

    # Two k values verify that the final same-power ratios are independent of
    # the arbitrary y=k*tau parametrization after conversion to scale factor.
    k_values = (0.05, 0.025)
    modes = {"NID": 3, "NIV": 2}
    results: dict[str, object] = {}
    checks: dict[str, bool] = {}

    for k_mpc in k_values:
        mu = float(omega_parameter / k_mpc)
        u = mu * y
        # Exact radiation+matter solution used by CLASS:
        # a proportional to tau*(1+omega_m*tau/4).
        epsilon = u + u**2 / 4  # rho_m/rho_r
        hbar = (1 / y) * (1 + u / 2) / (1 + u / 4)  # Hconf/k
        omega_r = 1 / (1 + epsilon)
        omega_m = epsilon / (1 + epsilon)
        omega_g = rg * omega_r
        omega_n = rnu * omega_r
        omega_b = fb * omega_m
        omega_c = (1 - fb) * omega_m
        baryon_loading = sp.Rational(3, 4) * fb * epsilon / rg

        for mode, target_power in modes.items():
            coeff = {
                name: sp.symbols(f"{name}_{mode}_{str(k_mpc).replace('.', 'p')}_0:{order + 1}")
                for name in VARIABLES
            }
            series = {
                name: sum(coeff[name][power] * y**power for power in range(order + 1))
                for name in VARIABLES
            }
            h = series["h"]
            eta = series["eta"]
            dg, dn = series["dg"], series["dn"]
            db, dc = series["db"], series["dc"]
            vg, vn = series["Vg"], series["Vn"]
            sig, f3 = series["sig"], series["F3"]

            delta_total = omega_g * dg + omega_n * dn + omega_b * db + omega_c * dc
            momentum_total = (
                sp.Rational(4, 3) * omega_g * vg
                + sp.Rational(4, 3) * omega_n * vn
                + omega_b * vg
            )
            residuals = {
                "dg": sp.diff(dg, y) + sp.Rational(4, 3) * vg + sp.Rational(2, 3) * sp.diff(h, y),
                "dn": sp.diff(dn, y) + sp.Rational(4, 3) * vn + sp.Rational(2, 3) * sp.diff(h, y),
                "db": sp.diff(db, y) + vg + sp.diff(h, y) / 2,
                "dc": sp.diff(dc, y) + sp.diff(h, y) / 2,
                "Vg": (
                    sp.diff(vg, y)
                    - dg / (4 * (1 + baryon_loading))
                    + hbar * baryon_loading * vg / (1 + baryon_loading)
                ),
                "Vn": sp.diff(vn, y) - dn / 4 + sig,
                "sig": (
                    sp.diff(sig, y)
                    - sp.Rational(4, 15) * vn
                    - sp.Rational(2, 15) * (sp.diff(h, y) + 6 * sp.diff(eta, y))
                    + sp.Rational(3, 10) * f3
                ),
                "F3": sp.diff(f3, y) - sp.Rational(6, 7) * sig,
                "Einstein00": sp.diff(h, y) - 2 * eta / hbar - 3 * hbar * delta_total,
                "Einstein0i": sp.diff(eta, y) - sp.Rational(3, 2) * hbar**2 * momentum_total,
            }

            equations: list[sp.Expr] = []
            # Regular species/hierarchy rows.
            for name in ("dg", "dn", "db", "dc", "Vg", "Vn", "sig", "F3"):
                expanded = sp.series(residuals[name], y, 0, order).removeO().expand()
                equations.extend(expanded.coeff(y, power) for power in range(order))
            # Include the two regular-singular cancellation rows.  The upper
            # limits avoid coefficients that would require order+1 variables.
            e00 = sp.series(residuals["Einstein00"], y, 0, order).removeO().expand()
            equations.extend(e00.coeff(y, power) for power in range(-1, order))
            e0i = sp.series(residuals["Einstein0i"], y, 0, order - 1).removeO().expand()
            equations.extend(e0i.coeff(y, power) for power in range(-2, order - 1))

            initial = {name: 0.0 for name in VARIABLES}
            if mode == "NID":
                initial.update({"dg": -rnu / rg, "dn": 1.0})
            else:
                initial.update({"Vg": -3 * rnu / (4 * rg), "Vn": 0.75})
            equations.extend(coeff[name][0] - value for name, value in initial.items())
            unknowns = [coeff[name][power] for name in VARIABLES for power in range(order + 1)]
            matrix_sym, rhs_sym = sp.linear_eq_to_matrix(equations, unknowns)
            matrix = np.asarray(matrix_sym, dtype=float)
            rhs = np.asarray(rhs_sym, dtype=float).reshape(-1)
            deadline()

            solution, _, rank, singular = np.linalg.lstsq(matrix, rhs, rcond=None)
            raw_residual = matrix @ solution - rhs
            max_abs = float(np.max(np.abs(raw_residual)))
            scale = float(
                max(
                    np.max(np.abs(matrix) * np.maximum(np.abs(solution)[None, :], 1.0e-300)),
                    np.max(np.abs(rhs)),
                    1.0e-300,
                )
            )
            scaled_residual = max_abs / scale
            condition = float(singular[0] / singular[-1])
            solved = dict(zip(unknowns, solution))

            def value(name: str, power: int) -> float:
                return float(solved[coeff[name][power]])

            # Convert y to z proportional to physical a.  The overall omitted
            # constant cancels from ratios at a fixed power.
            y_of_z = 2 / mu * (sp.sqrt(1 + mu * z) - 1)
            substituted = {symbol: float(number) for symbol, number in solved.items()}

            def z_coefficient(expression: sp.Expr, power: int) -> float:
                numerical = expression.subs(substituted)
                converted = sp.series(numerical.subs(y, y_of_z), z, 0, order + 1).removeO().expand()
                return float(converted.coeff(z, power))

            hx = sp.diff(h, y) / hbar
            etax = sp.diff(eta, y) / hbar
            ug = hbar * vg
            un = hbar * vn
            hx_n = z_coefficient(hx, target_power)
            eta_n = z_coefficient(etax, target_power)
            ug_n = z_coefficient(ug, target_power)
            un_n = z_coefficient(un, target_power)
            ratios = {
                "eta_x_over_hx": eta_n / hx_n,
                "U_gamma_over_hx": ug_n / hx_n,
                "U_fs_over_hx": un_n / hx_n,
            }

            if mode == "NID":
                expected = {
                    "dg0": -rnu / rg,
                    "dn0": 1.0,
                    "dg2": rnu / (6 * rg),
                    "dn2": -1 / 6,
                    "Vg1": -rnu / (4 * rg),
                    "Vn1": 1 / 4,
                    "sig2": 1 / (2 * (4 * rnu + 15)),
                    "eta2": -rnu / (6 * (4 * rnu + 15)),
                    "dc3": -rnu * fb * mu / (80 * rg),
                }
            else:
                expected = {
                    "dg1": rnu / rg,
                    "dn1": -1.0,
                    "Vg0": -3 * rnu / (4 * rg),
                    "Vn0": 3 / 4,
                    "sig1": 1 / (4 * rnu + 5),
                    "eta1": -rnu / (4 * rnu + 5),
                    "dc2": -9 * rnu * fb * mu / (64 * rg),
                }
            measured = {
                label: value(label.rstrip("0123456789"), int(label[len(label.rstrip("0123456789")):]))
                for label in expected
            }
            leading_errors = {
                label: abs(measured[label] - wanted) / max(abs(wanted), 1.0e-12)
                for label, wanted in expected.items()
            }
            key = f"k={k_mpc:.3f}_{mode}"
            checks[f"{key}_full_column_rank"] = bool(rank == len(unknowns))
            checks[f"{key}_scaled_residual_below_1e-10"] = bool(scaled_residual < 1.0e-10)
            checks[f"{key}_leading_coefficients_below_2pct"] = bool(max(leading_errors.values()) < 0.02)
            checks[f"{key}_finite_target_ratios"] = bool(
                abs(hx_n) > 1.0e-14 and all(np.isfinite(v) for v in ratios.values())
            )
            results[key] = {
                "mode": mode,
                "k_mpc": k_mpc,
                "mu_omega_over_k": mu,
                "target_scale_factor_power": target_power,
                "matrix_shape": list(matrix.shape),
                "rank": int(rank),
                "unknown_count": len(unknowns),
                "condition_number": condition,
                "max_absolute_residual": max_abs,
                "scaled_absolute_residual": scaled_residual,
                "leading_expected": expected,
                "leading_measured": measured,
                "leading_relative_errors": leading_errors,
                "target_coefficients_in_z": {
                    "h_x": hx_n,
                    "eta_x": eta_n,
                    "U_gamma": ug_n,
                    "U_fs": un_n,
                },
                "target_ratios": ratios,
            }
            deadline()

    # The ratios in scale-factor power must not depend on which k was used to
    # parametrize the same Frobenius solution.
    for mode in modes:
        row_a = results[f"k={k_values[0]:.3f}_{mode}"]["target_ratios"]
        row_b = results[f"k={k_values[1]:.3f}_{mode}"]["target_ratios"]
        for ratio_name in row_a:
            relative = abs(row_a[ratio_name] - row_b[ratio_name]) / max(
                abs(row_a[ratio_name]), abs(row_b[ratio_name]), 1.0e-12
            )
            checks[f"{mode}_{ratio_name}_two_k_below_2pct"] = bool(relative < 0.02)

    passed = bool(checks) and all(checks.values())
    output = {
        "test": "A2-K4.3b-RG-BR3B-2f-3 exact-standard Frobenius NID/NIV",
        "supersedes_execution_only": (
            "scripts 110 and 111 unstable high-order numerical extraction; "
            "both REVIEW_UNCLOSED artifacts remain preserved"
        ),
        "background": {
            "Omega_r0": omega_r0,
            "omega_parameter_Mpc_inverse": omega_parameter,
            "baryon_fraction": fb,
            "R_gamma": rg,
            "R_fs": rnu,
        },
        "equations": (
            "synchronous 00+0i constraints; photon/neutrino/baryon/CDM "
            "continuities; tight-coupling photon-baryon Euler; neutrino "
            "Euler, shear and first l=3 recurrence"
        ),
        "mode_results": results,
        "checks": checks,
        "execution_verdict": (
            "PASS_STANDARD_NID_NIV_FROBENIUS_INPUTS"
            if passed
            else "REVIEW_STANDARD_NID_NIV_FROBENIUS_UNCLOSED"
        ),
        "K4_3b_RG_verdict": (
            "NEUZAVRETA_BR3B2F_INJECT_FROBENIUS_INPUTS_INTO_FUEL_SYSTEM"
            if passed
            else "NEUZAVRETA_BR3B2F_FROBENIUS_INPUT_AUDIT"
        ),
        "canonical_score": "60/100 = G6",
        "next_step": (
            "after PASS, inject the audited scale-factor ratios plus the earlier "
            "fractional-sector responses into the common p+n fuel matrix and "
            "verify all nine rows; otherwise audit the failed recurrence row"
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
