#!/usr/bin/env python
"""A2-K4.3b-RG general-synchronous K4 test-field response.

Script 85 transformed truncated NID/NIV series to Newtonian gauge, where the
required cancellations need higher orders, and therefore failed its null and
start tests.  This corrected alias evolves the dark sector directly in a
regular synchronous gauge (zero lapse) and explicitly allows theta_c to become
nonzero after K4 is switched on.

The standard metric h' is held fixed, so this remains a test-field subgate;
full fuel backreaction and Einstein constraints are not claimed.
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
from scipy.interpolate import PchipInterpolator


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


B13 = load("k4_rg86_bg13", "13_script_A1_K1_cdm_background_audit_exact_zstar.py")
B11 = B13.BASE
S84 = load("k4_rg86_seed84", "84_script_A2_K4_3b_RG_CLASS_analytic_collective_seed_CAMB_crosscheck.py")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=45.0)
    parser.add_argument("--x-min", type=float, default=-25.0)
    parser.add_argument("--x-final", type=float, default=-14.0)
    parser.add_argument("--background-step", type=float, default=5.0e-4)
    parser.add_argument("--integration-step", type=float, default=2.0e-3)
    parser.add_argument("--k-mpc", type=float, default=0.05)
    args = parser.parse_args()
    if not (0.0 < args.max_runtime_seconds <= 50.0):
        parser.error("--max-runtime-seconds must be in (0, 50]")
    if not (-28.0 <= args.x_min <= -24.0):
        parser.error("--x-min must be in [-28,-24]")
    if not (-16.0 <= args.x_final <= -13.0):
        parser.error("--x-final must be in [-16,-13]")
    if args.x_final <= args.x_min + 7.0:
        parser.error("need at least seven e-folds for start convergence")
    if not (2.5e-4 <= args.background_step <= 1.0e-3):
        parser.error("--background-step must be in [2.5e-4,1e-3]")
    if not (5.0e-4 <= args.integration_step <= 5.0e-3):
        parser.error("--integration-step must be in [5e-4,5e-3]")

    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("internal synchronous K4 test-field deadline exceeded")

    p = B11.ModelParameters()
    settings = B11.IntegrationSettings(x_min=args.x_min, step=args.background_step)
    xd, sd, xb0 = B13.integrate_background(p, settings)
    deadline()
    x = np.asarray(xd[::-1], dtype=float)
    states = np.asarray(sd[::-1], dtype=float)
    xf, xm, xr = states.T
    xb = xb0 * np.exp(-3.0 * x)
    xc = xm - xb
    e = np.sqrt(xf + xm + xr)
    a = np.exp(x)
    e2_x = -3.0 * p.delta * xf - 3.0 * xm - 4.0 * xr
    hc_x = 1.0 + e2_x / (2.0 * e * e)

    # H0*eta, sufficient because k*tau is formed with q=k/H0 below.
    eta_h0 = np.zeros_like(x)
    eta_h0[0] = a[0] / math.sqrt(B11.radiation_density_today(p))
    integrand = np.exp(-x) / e
    for i in range(len(x) - 1):
        dx = x[i + 1] - x[i]
        eta_h0[i + 1] = eta_h0[i] + 0.5 * dx * (integrand[i] + integrand[i + 1])

    early_mask = (x >= args.x_min + 0.5) & (x <= args.x_min + 2.0)
    fb = float(np.mean(xb[early_mask] / xm[early_mask]))
    fc = float(np.mean(xc[early_mask] / xm[early_mask]))
    fnu = 0.2271 * (p.neff_standard + p.delta_neff) / (
        1.0 + 0.2271 * (p.neff_standard + p.delta_neff)
    )
    fg = 1.0 - fnu
    # CLASS om*tau is dimensionless. H0 factors cancel in om*tau.
    om_over_h0 = float(np.mean(a[early_mask] * xm[early_mask] / np.sqrt(xr[early_mask])))
    q = args.k_mpc / (100.0 * p.h / 299792.458)
    tau_h0 = eta_h0

    background = {
        "xf": PchipInterpolator(x, xf),
        "xc": PchipInterpolator(x, xc),
        "e": PchipInterpolator(x, e),
        "hc_x": PchipInterpolator(x, hc_x),
        "a": PchipInterpolator(x, a),
    }

    seeds: dict[str, dict[str, PchipInterpolator | np.ndarray]] = {}
    for mode in S84.MODES:
        # S84 expects k and tau in the same units. Use dimensionless q and
        # H0*tau; om is then om/H0.
        sync = np.vstack(
            [S84.class_seed(mode, q, tt, fnu, fg, fb, fc, om_over_h0) for tt in tau_h0]
        )
        dc_sync = sync[:, 2]
        dc_interp = PchipInterpolator(x, dc_sync)
        dc_x = dc_interp.derivative()(x)
        # In the null CDM-comoving synchronous seed, theta_c=0 and
        # delta_c,x=-h_x/2. This defines a regular metric source without any
        # Newtonian cancellation.
        h_x = -2.0 * dc_x
        seeds[mode] = {
            "dc": dc_sync,
            "h_x": h_x,
            "dc_i": dc_interp,
            "h_x_i": PchipInterpolator(x, h_x),
        }
    deadline()

    def rhs(xx: float, z: np.ndarray, mode: str, lam: float) -> np.ndarray:
        dc, uc, df, uf = z
        xf_v = float(background["xf"](xx))
        xc_v = float(background["xc"](xx))
        e_v = float(background["e"](xx))
        hc_x_v = float(background["hc_x"](xx))
        a_v = float(background["a"](xx))
        h_x = float(seeds[mode]["h_x_i"](xx))
        g = lam / e_v
        r = xf_v / xc_v
        beta = p.delta * r / (1.0 + p.delta * r)
        ud = (1.0 - beta) * uc + beta * uf
        s2 = (q / (a_v * e_v)) ** 2
        out = np.empty(4, dtype=float)
        out[0] = -s2 * uc - 0.5 * h_x + g * r * (df - dc)
        out[1] = -(1.0 - hc_x_v) * uc + g * r * beta * (uf - uc)
        out[2] = (
            -3.0 * (2.0 - p.delta) * df
            - p.delta * s2 * uf
            - 9.0 * (2.0 * p.delta - p.delta**2) * uf
            - 0.5 * p.delta * h_x
            - 3.0 * g * (2.0 - p.delta) * uf
        )
        out[3] = (
            (hc_x_v + 2.0) * uf
            + df / p.delta
            + g / p.delta * (2.0 * uf - ud)
        )
        return out

    def integrate(mode: str, lam: float, x_start: float) -> np.ndarray:
        intervals = int(math.ceil((args.x_final - x_start) / args.integration_step))
        grid = np.linspace(x_start, args.x_final, intervals + 1)
        z = np.array([float(seeds[mode]["dc_i"](x_start)), 0.0, 0.0, 0.0])
        for i in range(intervals):
            xx = float(grid[i])
            step = float(grid[i + 1] - grid[i])
            k1 = rhs(xx, z, mode, lam)
            k2 = rhs(xx + 0.5 * step, z + 0.5 * step * k1, mode, lam)
            k3 = rhs(xx + 0.5 * step, z + 0.5 * step * k2, mode, lam)
            k4 = rhs(xx + step, z + step * k3, mode, lam)
            z = z + step * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
            if i % 1000 == 0:
                deadline()
            if not np.all(np.isfinite(z)):
                raise FloatingPointError(f"nonfinite {mode}, lambda={lam}")
        return z

    deep = args.x_min
    shallow = args.x_min + 2.0
    checks: dict[str, bool] = {}
    rows: dict[str, object] = {}
    for mode in S84.MODES:
        runs: dict[tuple[float, str], np.ndarray] = {}
        for lam in (0.0, p.lam):
            runs[(lam, "deep")] = integrate(mode, lam, deep)
            runs[(lam, "shallow")] = integrate(mode, lam, shallow)
        deadline()
        convergence: dict[str, float] = {}
        for lam in (0.0, p.lam):
            zd = runs[(lam, "deep")]
            zs = runs[(lam, "shallow")]
            rel = float(np.linalg.norm(zd - zs) / max(np.linalg.norm(zd), np.linalg.norm(zs), 1.0e-30))
            convergence[str(lam)] = rel
            checks[f"{mode}_start_convergence_lambda_{lam}"] = rel < 2.0e-4

        null = runs[(0.0, "deep")]
        coupled = runs[(p.lam, "deep")]
        expected_dc = float(seeds[mode]["dc_i"](args.x_final))
        null_dc_abs = abs(float(null[0]) - expected_dc)
        null_uc_abs = abs(float(null[1]))
        checks[f"{mode}_lambda_zero_exact_CDM_seed"] = null_dc_abs < 2.0e-8 and null_uc_abs < 2.0e-10
        checks[f"{mode}_finite"] = bool(all(np.all(np.isfinite(v)) for v in runs.values()))
        rows[mode] = {
            "vector_order": ["delta_c_sync", "U_c_sync", "delta_f_sync", "U_f_sync"],
            "lambda_zero_final": null.tolist(),
            "lambda_0p15_final": coupled.tolist(),
            "K4_minus_null_final": (coupled - null).tolist(),
            "start_convergence_relative": convergence,
            "lambda_zero_CDM_absolute_residual": {
                "delta_c": null_dc_abs,
                "U_c": null_uc_abs,
            },
        }

    passed = all(checks.values())
    output = {
        "test": "A2-K4.3b-RG general-synchronous K4 test-field response",
        "supersedes_for_gauge_evolution": "85_script_A2_K4_3b_RG_collective_K4_test_field_Puiseux_response.py",
        "gauge": (
            "general synchronous, A=0; initialized in null CDM frame, but "
            "theta_c is dynamically evolved and not constrained to remain zero"
        ),
        "scope": "fixed standard metric h_x; no back-reacted Einstein constraints",
        "inputs": {
            "lambda": p.lam,
            "delta": p.delta,
            "q_k_over_H0": q,
            "x_start_deep": deep,
            "x_start_shallow": shallow,
            "x_final": args.x_final,
            "integration_step_max": args.integration_step,
            "early_baryon_fraction": fb,
            "early_ash_fraction": fc,
        },
        "first_omitted_power": 4.0 - 3.0 * p.delta,
        "mode_results": rows,
        "checks": checks,
        "execution_verdict": "PASS_GENERAL_SYNCHRONOUS_TEST_FIELD" if passed else "REVIEW_REQUIRED",
        "K4_3b_RG_verdict": "NEUZAVRETA_BACKREACTED_PUISEUX_CONSTRAINTS_MISSING",
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
