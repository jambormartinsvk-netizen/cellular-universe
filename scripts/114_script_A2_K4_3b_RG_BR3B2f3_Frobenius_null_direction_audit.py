#!/usr/bin/env python
"""Bounded coefficient-algebra clone of timed-out script 112.

Script 112 is preserved as EXTERNAL_TIMEOUT_UNCLOSED: SymPy series expansion
did not return before the 35 s outer limit.  This clone evaluates the same
linear synchronous-gauge Frobenius ledger with finite Laurent-series
convolutions.  The matrix is constructed by linear basis probing and solved
by SVD.  No symbolic call can block the internal deadline.
"""

from __future__ import annotations

import argparse
import json
import math
import time

import numpy as np


VARIABLES = ("h", "eta", "dg", "dn", "db", "dc", "Vg", "Vn", "sig", "F3")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=12.0)
    parser.add_argument("--order", type=int, default=5)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 15.0:
        parser.error("runtime must be in (0, 15]")
    if not 5 <= args.order <= 7:
        parser.error("order must be in [5,7]")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("BR3B-2f-3 bounded coefficient deadline exceeded")

    order = args.order
    lo, hi = -3, order + 3

    def tidy(series):
        return {power: float(value) for power, value in series.items()
                if lo <= power <= hi and abs(value) > 1.0e-300}

    def add(*items):
        out = {}
        for item in items:
            for power, value in item.items():
                if lo <= power <= hi:
                    out[power] = out.get(power, 0.0) + value
        return tidy(out)

    def scale(item, factor):
        return tidy({power: factor * value for power, value in item.items()})

    def mul(first, second):
        out = {}
        for pa, va in first.items():
            for pb, vb in second.items():
                power = pa + pb
                if lo <= power <= hi:
                    out[power] = out.get(power, 0.0) + va * vb
        return tidy(out)

    def derivative(item):
        return tidy({power - 1: power * value for power, value in item.items() if power != 0})

    def inverse(item):
        nonzero = [(power, value) for power, value in item.items() if abs(value) > 1.0e-15]
        if not nonzero:
            raise ZeroDivisionError("zero series")
        lead_power, lead = min(nonzero)
        result = {-lead_power: 1.0 / lead}
        max_index = hi + lead_power
        for index in range(1, max_index + 1):
            total = 0.0
            for step in range(1, index + 1):
                total += item.get(lead_power + step, 0.0) * result.get(-lead_power + index - step, 0.0)
            result[-lead_power + index] = -total / lead
        return tidy(result)

    def power(item, exponent):
        if exponent == 0:
            return {0: 1.0}
        if exponent < 0:
            return power(inverse(item), -exponent)
        result = {0: 1.0}
        base = item
        count = exponent
        while count:
            if count & 1:
                result = mul(result, base)
            base = mul(base, base)
            count //= 2
        return result

    def coefficient(item, exponent):
        return float(item.get(exponent, 0.0))

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
    omega_parameter = hubble0_mpc * omega_m0 / math.sqrt(omega_r0)

    unknown_count = len(VARIABLES) * (order + 1)
    index = {(name, power): i for i, (name, power) in enumerate(
        (pair for name in VARIABLES for pair in ((name, p) for p in range(order + 1)))
    )}

    def variable_series(vector, name):
        return {power: vector[index[(name, power)]] for power in range(order + 1)}

    k_values = (0.05, 0.025)
    modes = {"NID": 3, "NIV": 2}
    results = {}
    checks = {}

    for k_mpc in k_values:
        mu = omega_parameter / k_mpc
        eps = {1: mu, 2: mu**2 / 4}
        one = {0: 1.0}
        omega_r = inverse(add(one, eps))
        omega_m = mul(eps, omega_r)
        omega_g = scale(omega_r, rg)
        omega_n = scale(omega_r, rnu)
        omega_b = scale(omega_m, fb)
        omega_c = scale(omega_m, 1 - fb)
        numerator = {0: 1.0, 1: mu / 2}
        denominator = {0: 1.0, 1: mu / 4}
        hbar = mul({-1: 1.0}, mul(numerator, inverse(denominator)))
        inv_hbar = inverse(hbar)
        hbar2 = mul(hbar, hbar)
        loading = scale(eps, 3 * fb / (4 * rg))
        inv_one_loading = inverse(add(one, loading))

        for mode, target_power in modes.items():
            initial = {name: 0.0 for name in VARIABLES}
            if mode == "NID":
                initial.update({"dg": -rnu / rg, "dn": 1.0})
            else:
                initial.update({"Vg": -3 * rnu / (4 * rg), "Vn": 0.75})

            def ledger(vector):
                s = {name: variable_series(vector, name) for name in VARIABLES}
                dh, deta = derivative(s["h"]), derivative(s["eta"])
                delta_total = add(
                    mul(omega_g, s["dg"]), mul(omega_n, s["dn"]),
                    mul(omega_b, s["db"]), mul(omega_c, s["dc"]),
                )
                momentum_total = add(
                    scale(mul(omega_g, s["Vg"]), 4 / 3),
                    scale(mul(omega_n, s["Vn"]), 4 / 3),
                    mul(omega_b, s["Vg"]),
                )
                residual = {
                    "dg": add(derivative(s["dg"]), scale(s["Vg"], 4 / 3), scale(dh, 2 / 3)),
                    "dn": add(derivative(s["dn"]), scale(s["Vn"], 4 / 3), scale(dh, 2 / 3)),
                    "db": add(derivative(s["db"]), s["Vg"], scale(dh, 0.5)),
                    "dc": add(derivative(s["dc"]), scale(dh, 0.5)),
                    "Vg": add(
                        derivative(s["Vg"]),
                        scale(mul(s["dg"], inv_one_loading), -0.25),
                        mul(hbar, mul(loading, mul(s["Vg"], inv_one_loading))),
                    ),
                    "Vn": add(derivative(s["Vn"]), scale(s["dn"], -0.25), s["sig"]),
                    "sig": add(
                        derivative(s["sig"]), scale(s["Vn"], -4 / 15),
                        scale(add(dh, scale(deta, 6)), -2 / 15), scale(s["F3"], 3 / 10),
                    ),
                    "F3": add(derivative(s["F3"]), scale(s["sig"], -6 / 7)),
                    "Einstein00": add(dh, scale(mul(s["eta"], inv_hbar), -2),
                                       scale(mul(hbar, delta_total), -3)),
                    "Einstein0i": add(deta, scale(mul(hbar2, momentum_total), -1.5)),
                }
                values = []
                for name in ("dg", "dn", "db", "dc", "Vg", "Vn", "sig", "F3"):
                    values.extend(coefficient(residual[name], p) for p in range(order))
                values.extend(coefficient(residual["Einstein00"], p) for p in range(-1, order))
                values.extend(coefficient(residual["Einstein0i"], p) for p in range(-2, order - 1))
                values.extend(vector[index[(name, 0)]] - initial[name] for name in VARIABLES)
                return np.asarray(values, dtype=float)

            zero = np.zeros(unknown_count)
            constant = ledger(zero)
            matrix = np.empty((constant.size, unknown_count))
            for column in range(unknown_count):
                basis = np.zeros(unknown_count)
                basis[column] = 1.0
                matrix[:, column] = ledger(basis) - constant
            rhs = -constant
            deadline()

            solution, _, rank, singular = np.linalg.lstsq(matrix, rhs, rcond=None)
            residual = matrix @ solution - rhs
            max_abs = float(np.max(np.abs(residual)))
            row_scale = float(max(np.max(np.abs(matrix) * np.maximum(np.abs(solution)[None, :], 1e-300)),
                                  np.max(np.abs(rhs)), 1e-300))
            scaled_residual = max_abs / row_scale
            condition = float(singular[0] / singular[-1])
            solved = {name: variable_series(solution, name) for name in VARIABLES}

            # z is proportional to physical a and satisfies z=y+mu*y^2/4.
            # y(z)=2/mu*(sqrt(1+mu*z)-1).
            y_of_z = {}
            for n in range(1, hi + 1):
                binomial = 1.0
                for j in range(n):
                    binomial *= (0.5 - j) / (j + 1)
                y_of_z[n] = 2 * binomial * mu ** (n - 1)

            def compose_laurent(function):
                out = {}
                for exponent, value in function.items():
                    out = add(out, scale(power(y_of_z, exponent), value))
                return out

            hx_z = compose_laurent(mul(derivative(solved["h"]), inv_hbar))
            etax_z = compose_laurent(mul(derivative(solved["eta"]), inv_hbar))
            ug_z = compose_laurent(mul(hbar, solved["Vg"]))
            un_z = compose_laurent(mul(hbar, solved["Vn"]))
            hx_n = coefficient(hx_z, target_power)
            eta_n = coefficient(etax_z, target_power)
            ug_n = coefficient(ug_z, target_power)
            un_n = coefficient(un_z, target_power)
            ratios = {
                "eta_x_over_hx": eta_n / hx_n,
                "U_gamma_over_hx": ug_n / hx_n,
                "U_fs_over_hx": un_n / hx_n,
            }

            if mode == "NID":
                expected = {
                    ("dg", 0): -rnu / rg, ("dn", 0): 1.0,
                    ("dg", 2): rnu / (6 * rg), ("dn", 2): -1 / 6,
                    ("Vg", 1): -rnu / (4 * rg), ("Vn", 1): 1 / 4,
                    ("sig", 2): 1 / (2 * (4 * rnu + 15)),
                    ("eta", 2): -rnu / (6 * (4 * rnu + 15)),
                    ("dc", 3): -rnu * fb * mu / (80 * rg),
                }
            else:
                expected = {
                    ("dg", 1): rnu / rg, ("dn", 1): -1.0,
                    ("Vg", 0): -3 * rnu / (4 * rg), ("Vn", 0): 0.75,
                    ("sig", 1): 1 / (4 * rnu + 5),
                    ("eta", 1): -rnu / (4 * rnu + 5),
                    ("dc", 2): -9 * rnu * fb * mu / (64 * rg),
                }
            leading = {}
            errors = {}
            for (name, p), wanted in expected.items():
                label = f"{name}{p}"
                got = coefficient(solved[name], p)
                leading[label] = {"measured": got, "expected": wanted}
                errors[label] = abs(got - wanted) / max(abs(wanted), 1e-12)

            key = f"k={k_mpc:.3f}_{mode}"
            checks[f"{key}_full_column_rank"] = bool(rank == unknown_count)
            checks[f"{key}_scaled_residual_below_1e-10"] = bool(scaled_residual < 1e-10)
            checks[f"{key}_leading_coefficients_below_2pct"] = bool(max(errors.values()) < 0.02)
            checks[f"{key}_finite_target_ratios"] = bool(abs(hx_n) > 1e-14 and all(np.isfinite(v) for v in ratios.values()))
            results[key] = {
                "mode": mode, "k_mpc": k_mpc, "mu_omega_over_k": mu,
                "matrix_shape": list(matrix.shape), "rank": int(rank),
                "unknown_count": unknown_count, "condition_number": condition,
                "max_absolute_residual": max_abs, "scaled_absolute_residual": scaled_residual,
                "leading_coefficient_audit": leading, "leading_relative_errors": errors,
                "target_scale_factor_power": target_power,
                "target_coefficients_in_z": {"h_x": hx_n, "eta_x": eta_n,
                                               "U_gamma": ug_n, "U_fs": un_n},
                "target_ratios": ratios,
            }
            deadline()

    for mode in modes:
        first = results[f"k={k_values[0]:.3f}_{mode}"]["target_ratios"]
        second = results[f"k={k_values[1]:.3f}_{mode}"]["target_ratios"]
        for name in first:
            difference = abs(first[name] - second[name]) / max(abs(first[name]), abs(second[name]), 1e-12)
            checks[f"{mode}_{name}_two_k_below_2pct"] = bool(difference < 0.02)

    passed = bool(checks) and all(checks.values())
    output = {
        "test": "A2-K4.3b-RG-BR3B-2f-3 bounded Frobenius coefficients",
        "supersedes_execution_only": "script 112 EXTERNAL_TIMEOUT_UNCLOSED; physics equations unchanged",
        "background": {"Omega_r0": omega_r0, "omega_parameter_Mpc_inverse": omega_parameter,
                       "baryon_fraction": fb, "R_gamma": rg, "R_fs": rnu},
        "mode_results": results, "checks": checks,
        "execution_verdict": "PASS_STANDARD_NID_NIV_FROBENIUS_INPUTS" if passed else "REVIEW_STANDARD_NID_NIV_FROBENIUS_UNCLOSED",
        "K4_3b_RG_verdict": "NEUZAVRETA_BR3B2F_INJECT_FROBENIUS_INPUTS_INTO_FUEL_SYSTEM" if passed else "NEUZAVRETA_BR3B2F_FROBENIUS_INPUT_AUDIT",
        "canonical_score": "60/100 = G6",
        "next_step": "after PASS inject the scale-factor ratios and earlier fractional-sector responses into all nine common-fuel rows; otherwise audit the first failed recurrence check",
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

