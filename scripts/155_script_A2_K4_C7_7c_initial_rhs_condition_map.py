#!/usr/bin/env python
"""Bounded zero-integration RHS conditioning map for A2-K4 C7.7c.

The script evaluates the registered BR3C term decomposition at the four
authoritative initial surfaces.  It reports cancellation condition numbers
and a standard forward roundoff bound.  It performs no ODE evolution and
changes no score or physical verdict.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import subprocess
import sys
import time

import numpy as np


STATE_NAMES = (
    "h", "eta", "delta_gamma", "delta_fs", "delta_b", "delta_c",
    "U_gamma", "U_fs", "sigma_fs", "L3_fs", "L4_fs", "delta_f", "U_f",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--source-runtime-seconds", type=float, default=2.0)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        parser.error("max runtime must be in (0,5]")
    if not 0.0 < args.source_runtime_seconds <= 3.0:
        parser.error("source runtime must be in (0,3]")

    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("C7.7c condition-map deadline exceeded")

    source = Path(__file__).with_name(
        "146_script_A2_K4_3b_RG_C7_7c_K4_analytic_reference_state.py"
    )
    source_run = subprocess.run(
        [
            sys.executable,
            str(source),
            "--max-runtime-seconds",
            str(args.source_runtime_seconds),
        ],
        capture_output=True,
        text=True,
        timeout=args.source_runtime_seconds + 0.5,
        check=False,
    )
    if source_run.returncode != 0:
        raise RuntimeError(
            f"state source failed: {source_run.stderr[-500:]} "
            f"{source_run.stdout[-500:]}"
        )
    source_payload = json.loads(source_run.stdout)
    if (
        source_payload.get("execution_verdict")
        != "PASS_C7_7C_K4_ANALYTIC_REFERENCE_STATE"
    ):
        raise RuntimeError("authoritative analytic-reference source did not pass")

    delta = 0.02297
    p = 3.93109
    h0 = 0.6637
    omega_m0 = 0.3517
    ombh2 = 0.02237
    total_matter_h2 = omega_m0 * h0**2
    fb = ombh2 / total_matter_h2
    fc = 1.0 - fb
    neff = 3.046 + 0.0535
    rn = 0.2271 * neff / (1.0 + 0.2271 * neff)
    rg = 1.0 - rn
    omega_gamma_h2 = 2.47282e-5
    omega_r0 = omega_gamma_h2 * (1.0 + 0.2271 * neff) / h0**2
    hubble0_mpc = 100.0 * h0 / 299792.458
    k_mpc = 0.05
    mu = hubble0_mpc * omega_m0 / math.sqrt(omega_r0) / k_mpc
    lambda_transfer = 0.15
    g2 = lambda_transfer * (hubble0_mpc / k_mpc) ** 2 * math.sqrt(omega_r0)
    transfer_shape = g2 * (1.0 / (p + 1.0) - 0.5)

    def background(x_value: float) -> dict[str, float]:
        z = k_mpc * math.exp(x_value) / (hubble0_mpc * math.sqrt(omega_r0))
        fuel_piece = z**p
        denominator = 1.0 + mu * z + fuel_piece * (
            1.0 + transfer_shape * z**2
        )
        denominator_x = mu * z + fuel_piece * (
            p + (p + 2.0) * transfer_shape * z**2
        )
        q = -1.0 + 0.5 * denominator_x / denominator
        s2 = z**2 / denominator
        return {
            "q": q,
            "s2": s2,
            "loading": 3.0 * fb * mu * z / (4.0 * rg),
            "g": g2 * z**2,
            "gr": g2 / (fc * mu) * z ** (p + 1.0),
            "Omega_gamma": rg / denominator,
            "Omega_fs": rn / denominator,
            "Omega_b": fb * mu * z / denominator,
            "Omega_c": (
                fc * mu * z + g2 * z ** (p + 2.0) / (p + 1.0)
            ) / denominator,
            "Omega_f": fuel_piece * (1.0 - 0.5 * g2 * z**2) / denominator,
        }

    epsilon = float(np.finfo(float).eps)

    def report(named_terms: list[tuple[str, float]]) -> dict[str, object]:
        values = [float(value) for _, value in named_terms]
        exact_like_sum = float(math.fsum(values))
        sequential_sum = float(sum(values))
        sum_abs = float(math.fsum(abs(value) for value in values))
        n = len(values)
        gamma_n = n * epsilon / max(1.0 - n * epsilon, epsilon)
        forward_bound = float(gamma_n * sum_abs)
        return {
            "terms": {name: float(value) for name, value in named_terms},
            "fsum": exact_like_sum,
            "sequential_sum": sequential_sum,
            "sequential_minus_fsum": sequential_sum - exact_like_sum,
            "sum_abs_terms": sum_abs,
            "cancellation_condition": (
                sum_abs / abs(exact_like_sum)
                if exact_like_sum != 0.0 else None
            ),
            "standard_forward_roundoff_bound": forward_bound,
            "signal_to_roundoff_bound": (
                abs(exact_like_sum) / forward_bound
                if forward_bound > 0.0 else None
            ),
        }

    results: dict[str, dict[str, object]] = {}
    for mode in ("NID", "NIV"):
        results[mode] = {}
        for surface in ("deep", "shallow"):
            deadline()
            source_surface = source_payload["BR3C_state_surfaces"][mode][
                "surfaces"
            ][surface]
            state = source_surface["state"]
            (
                h, eta, dg, dn, db, dc, Ug, Un, sigma, L3, L4, df, Uf,
            ) = (float(state[name]) for name in STATE_NAMES)
            bg = background(float(source_surface["x"]))
            density_terms = [
                ("Omega_gamma*delta_gamma", bg["Omega_gamma"] * dg),
                ("Omega_fs*delta_fs", bg["Omega_fs"] * dn),
                ("Omega_b*delta_b", bg["Omega_b"] * db),
                ("Omega_c*delta_c", bg["Omega_c"] * dc),
                ("Omega_f*delta_f", bg["Omega_f"] * df),
            ]
            density = math.fsum(value for _, value in density_terms)
            h_terms = [
                ("3*Omega_gamma*delta_gamma", 3.0 * density_terms[0][1]),
                ("3*Omega_fs*delta_fs", 3.0 * density_terms[1][1]),
                ("3*Omega_b*delta_b", 3.0 * density_terms[2][1]),
                ("3*Omega_c*delta_c", 3.0 * density_terms[3][1]),
                ("3*Omega_f*delta_f", 3.0 * density_terms[4][1]),
                ("2*s2*eta", 2.0 * bg["s2"] * eta),
            ]
            h_x = math.fsum(value for _, value in h_terms)
            eta_terms = [
                ("2*Omega_gamma*U_gamma", 2.0 * bg["Omega_gamma"] * Ug),
                ("2*Omega_fs*U_fs", 2.0 * bg["Omega_fs"] * Un),
                ("1.5*Omega_b*U_gamma", 1.5 * bg["Omega_b"] * Ug),
                ("1.5*delta*Omega_f*U_f", 1.5 * delta * bg["Omega_f"] * Uf),
            ]
            eta_x = math.fsum(value for _, value in eta_terms)
            inv1r = 1.0 / (1.0 + bg["loading"])
            load_fraction = bg["loading"] * inv1r
            equation_terms = {
                "h": h_terms,
                "eta": eta_terms,
                "delta_gamma": [
                    ("-(4/3)*s2*U_gamma", -(4.0 / 3.0) * bg["s2"] * Ug),
                    ("-(2/3)*h_x", -(2.0 / 3.0) * h_x),
                ],
                "delta_fs": [
                    ("-(4/3)*s2*U_fs", -(4.0 / 3.0) * bg["s2"] * Un),
                    ("-(2/3)*h_x", -(2.0 / 3.0) * h_x),
                ],
                "delta_b": [
                    ("-s2*U_gamma", -bg["s2"] * Ug),
                    ("-0.5*h_x", -0.5 * h_x),
                ],
                "delta_c": [
                    ("-0.5*h_x", -0.5 * h_x),
                    ("gr*(delta_f-delta_c)", bg["gr"] * (df - dc)),
                ],
                "U_gamma": [
                    ("q*U_gamma", bg["q"] * Ug),
                    ("-load_fraction*U_gamma", -load_fraction * Ug),
                    ("0.25*inv1r*delta_gamma", 0.25 * inv1r * dg),
                ],
                "U_fs": [
                    ("q*U_fs", bg["q"] * Un),
                    ("0.25*delta_fs", 0.25 * dn),
                    ("-sigma_fs", -sigma),
                ],
                "sigma_fs": [
                    ("(2/15)*h_x", (2.0 / 15.0) * h_x),
                    ("(4/5)*eta_x", (4.0 / 5.0) * eta_x),
                    ("(4/15)*s2*U_fs", (4.0 / 15.0) * bg["s2"] * Un),
                    ("-(3/10)*L3", -(3.0 / 10.0) * L3),
                ],
                "L3_fs": [
                    ("-q*L3", -bg["q"] * L3),
                    ("(6/7)*s2*sigma", (6.0 / 7.0) * bg["s2"] * sigma),
                    ("-(4/7)*L4", -(4.0 / 7.0) * L4),
                ],
                "L4_fs": [
                    ("-2*q*L4", -2.0 * bg["q"] * L4),
                    ("(4/9)*s2*L3", (4.0 / 9.0) * bg["s2"] * L3),
                ],
                "delta_f": [
                    ("-3*(2-delta)*delta_f", -3.0 * (2.0 - delta) * df),
                    ("-delta*s2*U_f", -delta * bg["s2"] * Uf),
                    ("-0.5*delta*h_x", -0.5 * delta * h_x),
                    ("-9*delta*(2-delta)*U_f", -9.0 * delta * (2.0 - delta) * Uf),
                    ("-3*(2-delta)*g*U_f", -3.0 * (2.0 - delta) * bg["g"] * Uf),
                ],
                "U_f": [
                    ("(q+2)*U_f", (bg["q"] + 2.0) * Uf),
                    ("delta_f/delta", df / delta),
                    ("(2/delta)*g*U_f", (2.0 / delta) * bg["g"] * Uf),
                ],
            }
            results[mode][surface] = {
                "x": float(source_surface["x"]),
                "density_condition": report(density_terms),
                "rhs_conditions": {
                    name: report(terms) for name, terms in equation_terms.items()
                },
            }

    output = {
        "test": "A2-K4 C7.7c initial RHS cancellation-condition map",
        "state_source": source.name,
        "machine_epsilon": epsilon,
        "results": results,
        "execution_verdict": "CAPTURED_C7_7C_INITIAL_CONDITION_MAP",
        "physical_verdict": "diagnostic only; no K4 score or death verdict",
        "fine_depth": "66.5/100",
        "scope_limit": (
            "initial surfaces only; no ODE evolution and no replacement for "
            "the full C7.7c activity gate"
        ),
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.TimeoutExpired as exc:
        print(json.dumps({"execution_verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution_verdict": "ERROR_UNCLOSED", "error": repr(exc)}))
        raise SystemExit(2)
