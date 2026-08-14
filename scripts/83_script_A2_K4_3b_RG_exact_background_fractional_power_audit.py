#!/usr/bin/env python
"""A2-K4.3b-RG early exact-background scaling/Puiseux audit.

The K4 background has w_f=-1+delta and Q=Gamma rho_f.  In radiation
domination lambda/E is O(a^2), while rho_f/rho_c is O(a^(3-3 delta)).
Consequently several first corrections have non-integer powers for the
registered delta=0.02297.  This script measures the powers on the exact A1-K1
background and compares them with the asymptotic derivation.  The result fixes
the power ledger for the later Frobenius/Puiseux perturbation solver.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path
import sys
import time

import numpy as np


HERE = Path(__file__).resolve().parent


def load(name: str, filename: str):
    path = HERE / filename
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


B13 = load("a2_k4_rg_bg13", "13_script_A1_K1_cdm_background_audit_exact_zstar.py")
B11 = B13.BASE


def fitted_power(x: np.ndarray, quantity: np.ndarray, mask: np.ndarray) -> tuple[float, float]:
    if np.any(quantity[mask] <= 0.0):
        raise ValueError("power fit requires positive quantity")
    coeff = np.polyfit(x[mask], np.log(quantity[mask]), 1)
    predicted = np.polyval(coeff, x[mask])
    max_residual = float(np.max(np.abs(np.log(quantity[mask]) - predicted)))
    return float(coeff[0]), max_residual


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=35.0)
    parser.add_argument("--x-min", type=float, default=-25.0)
    parser.add_argument("--step", type=float, default=5.0e-4)
    args = parser.parse_args()
    if not (0.0 < args.max_runtime_seconds <= 50.0):
        parser.error("--max-runtime-seconds must be in (0, 50]")
    if not (-30.0 <= args.x_min <= -22.0):
        parser.error("--x-min must be in [-30, -22]")
    if not (2.5e-4 <= args.step <= 1.0e-3):
        parser.error("--step must be in [2.5e-4, 1e-3]")

    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("internal exact-background power deadline exceeded")

    p = B11.ModelParameters()
    settings = B11.IntegrationSettings(x_min=args.x_min, step=args.step)
    xs_desc, states_desc, xb0 = B13.integrate_background(p, settings)
    deadline()
    x = np.asarray(xs_desc[::-1], dtype=float)
    states = np.asarray(states_desc[::-1], dtype=float)
    xf = states[:, 0]
    xm = states[:, 1]
    xr = states[:, 2]
    xb = xb0 * np.exp(-3.0 * x)
    xc = xm - xb
    e = np.sqrt(xf + xm + xr)
    a = np.exp(x)

    g = p.lam / e
    r = xf / xc
    gr = g * r
    fuel_over_radiation = xf / xr
    matter_over_radiation = xm / xr
    ash_over_radiation = xc / xr

    # Deep enough for asymptotics, but away from the first endpoint so the
    # fit is not controlled by a single backward-integration boundary value.
    mask = (x >= max(args.x_min + 1.0, -24.0)) & (x <= -18.0)
    if np.count_nonzero(mask) < 100:
        raise RuntimeError("insufficient early fit window")

    expected = {
        "lambda_over_E": 2.0,
        "rho_f_over_rho_c": 3.0 - 3.0 * p.delta,
        "lambda_over_E_times_rho_f_over_rho_c": 5.0 - 3.0 * p.delta,
        "rho_f_over_radiation": 4.0 - 3.0 * p.delta,
        "matter_over_radiation": 1.0,
        "ash_over_radiation": 1.0,
    }
    arrays = {
        "lambda_over_E": g,
        "rho_f_over_rho_c": r,
        "lambda_over_E_times_rho_f_over_rho_c": gr,
        "rho_f_over_radiation": fuel_over_radiation,
        "matter_over_radiation": matter_over_radiation,
        "ash_over_radiation": ash_over_radiation,
    }
    measured: dict[str, object] = {}
    checks: dict[str, bool] = {}
    for name, quantity in arrays.items():
        slope, log_residual = fitted_power(x, quantity, mask)
        error = abs(slope - expected[name])
        measured[name] = {
            "expected_power_of_a": expected[name],
            "measured_power_of_a": slope,
            "absolute_power_error": error,
            "max_log_fit_residual": log_residual,
        }
        checks[f"{name}_power_matches"] = error < 2.0e-5

    # Dimensionless conformal time H0*eta on the exact background.
    # The omitted a=0..a_min radiation tail is a_min/sqrt(Omega_r).
    integrand = np.exp(-x) / e
    eta_h0 = np.zeros_like(x)
    eta_h0[0] = math.exp(x[0]) / math.sqrt(B11.radiation_density_today(p))
    for i in range(len(x) - 1):
        dx = x[i + 1] - x[i]
        eta_h0[i + 1] = eta_h0[i] + 0.5 * dx * (integrand[i] + integrand[i + 1])
    radiation_identity = a * e * eta_h0
    identity_window = radiation_identity[mask]
    identity_error = float(np.max(np.abs(identity_window - 1.0)))
    checks["exact_background_conformal_map_radiation_limit"] = identity_error < 2.0e-3

    # Non-integer powers must not be silently rounded to ordinary Taylor
    # orders.  At registered delta they are far from numerical integers.
    fractional = {
        name: value for name, value in expected.items() if abs(value - round(value)) > 1.0e-6
    }
    checks["registered_delta_requires_fractional_power_ledger"] = len(fractional) == 3
    deadline()

    passed = all(checks.values())
    output = {
        "test": "A2-K4.3b-RG exact-background fractional-power audit",
        "inputs": {
            "lambda": p.lam,
            "delta": p.delta,
            "x_min": args.x_min,
            "background_step": args.step,
            "fit_window": [float(np.min(x[mask])), float(np.max(x[mask]))],
        },
        "power_ledger": measured,
        "fractional_expected_powers": fractional,
        "conformal_time_map": {
            "identity": "a E (H0 eta) -> 1 in radiation domination",
            "max_abs_error_in_fit_window": identity_error,
        },
        "interpretation": {
            "fuel_gravitational_weight_starts": "a^(4-3delta)",
            "ash_interaction_correction_starts": "a^(5-3delta)",
            "fuel_direct_interaction_coefficient_starts": "a^2",
            "required_series_type": "generalized Frobenius/Puiseux power ledger",
        },
        "checks": checks,
        "execution_verdict": "PASS_EARLY_K4_POWER_LEDGER" if passed else "REVIEW_REQUIRED",
        "K4_3b_RG_verdict": "NEUZAVRETA_COLLECTIVE_PUISEUX_COEFFICIENTS_MISSING",
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
    except Exception as exc:
        print(json.dumps({"execution_verdict": "ERROR_UNCLOSED", "error": repr(exc)}))
        raise SystemExit(2)
