#!/usr/bin/env python
"""A2-K4.3b-RG collective K4 dark-sector test-field response.

Five analytic CLASS regular seeds are evaluated on the exact A1-K1
background and transformed to finite-time Newtonian variables.  The audited
K4 fuel/ash continuity and Euler equations are then integrated while the
standard radiation/matter metric is held fixed.

This is a controlled test-field subgate only.  It is exact below the first
neglected fuel gravitational weight O(a^(4-3 delta)); it does not check the
full back-reacted Einstein constraints and therefore cannot close G7.
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
C_KM_S = 299792.458


def load(name: str, filename: str):
    path = HERE / filename
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


B13 = load("k4_rg85_bg13", "13_script_A1_K1_cdm_background_audit_exact_zstar.py")
B11 = B13.BASE
S84 = load("k4_rg85_seed84", "84_script_A2_K4_3b_RG_CLASS_analytic_collective_seed_CAMB_crosscheck.py")


def shear_nu(mode: str, k: float, tau: np.ndarray, fnu: float, fb: float, fc: float, om: float) -> np.ndarray:
    y = k * tau
    y2 = y * y
    omt = om * tau
    if mode == "initial_adiabatic":
        return (
            2.0
            * y2
            / (45.0 + 12.0 * fnu)
            * (1.0 + (4.0 * fnu - 5.0) / (4.0 * (2.0 * fnu + 15.0)) * omt)
        )
    if mode == "initial_iso_CDM":
        return -fc * y2 * tau * om / (6.0 * (2.0 * fnu + 15.0))
    if mode == "initial_iso_baryon":
        return -fb * y2 * tau * om / (6.0 * (2.0 * fnu + 15.0))
    if mode == "initial_iso_neutrino":
        return y2 / (2.0 * (4.0 * fnu + 15.0))
    if mode == "initial_iso_neutrino_vel":
        return y / (4.0 * fnu + 15.0) * (
            1.0 + 3.0 * omt * fnu / (4.0 * fnu + 15.0)
        )
    raise ValueError(mode)


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
            raise TimeoutError("internal K4 collective test-field deadline exceeded")

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
    h0_mpc = 100.0 * p.h / C_KM_S
    hconf = a * h0_mpc * e
    e2_x = -3.0 * p.delta * xf - 3.0 * xm - 4.0 * xr
    hc_x = 1.0 + e2_x / (2.0 * e * e)

    # Exact conformal map including the radiation tail below x_min.
    eta_h0 = np.zeros_like(x)
    eta_h0[0] = a[0] / math.sqrt(B11.radiation_density_today(p))
    integrand = np.exp(-x) / e
    for i in range(len(x) - 1):
        dx = x[i + 1] - x[i]
        eta_h0[i + 1] = eta_h0[i] + 0.5 * dx * (integrand[i] + integrand[i + 1])
    tau = eta_h0 / h0_mpc

    early_mask = (x >= args.x_min + 0.5) & (x <= args.x_min + 2.0)
    fb = float(np.mean(xb[early_mask] / xm[early_mask]))
    fc = float(np.mean(xc[early_mask] / xm[early_mask]))
    fnu = 0.2271 * (p.neff_standard + p.delta_neff) / (
        1.0 + 0.2271 * (p.neff_standard + p.delta_neff)
    )
    fg = 1.0 - fnu
    om_samples = h0_mpc * a[early_mask] * xm[early_mask] / np.sqrt(xr[early_mask])
    om = float(np.mean(om_samples))

    background_interp = {
        "xf": PchipInterpolator(x, xf),
        "xc": PchipInterpolator(x, xc),
        "e": PchipInterpolator(x, e),
        "hconf": PchipInterpolator(x, hconf),
        "hc_x": PchipInterpolator(x, hc_x),
    }

    metric_by_mode: dict[str, dict[str, np.ndarray | PchipInterpolator]] = {}
    for mode in S84.MODES:
        sync = np.vstack(
            [S84.class_seed(mode, args.k_mpc, tt, fnu, fg, fb, fc, om) for tt in tau]
        )
        dg, db, dc_sync, dn, qg, qn, eta_s = sync.T
        theta_g = 0.75 * args.k_mpc * qg
        theta_n = 0.75 * args.k_mpc * qn
        rm = xm / xr
        delta_r = fg * dg + fnu * dn
        delta_m = fb * db + fc * dc_sync
        velocity_total = (
            (4.0 / 3.0) * (fg * theta_g + fnu * theta_n)
            + rm * fb * theta_g
        ) / (1.0 + rm)
        delta_total = (delta_r + rm * delta_m) / (1.0 + rm)
        alpha = (
            eta_s
            + 1.5
            * hconf**2
            / args.k_mpc**2
            * (delta_total + 3.0 * hconf / args.k_mpc**2 * velocity_total)
        ) / hconf
        phi = eta_s - hconf * alpha
        snu = shear_nu(mode, args.k_mpc, tau, fnu, fb, fc, om)
        psi = phi - 6.0 * hconf**2 / args.k_mpc**2 * fnu * snu
        dc_newtonian = dc_sync - 3.0 * hconf * alpha
        uc_newtonian = hconf * alpha
        phi_x = np.gradient(phi, x, edge_order=2)
        metric_by_mode[mode] = {
            "phi": phi,
            "psi": psi,
            "dc": dc_newtonian,
            "uc": uc_newtonian,
            "phi_i": PchipInterpolator(x, phi),
            "psi_i": PchipInterpolator(x, psi),
            "phi_x_i": PchipInterpolator(x, phi_x),
            "dc_i": PchipInterpolator(x, dc_newtonian),
            "uc_i": PchipInterpolator(x, uc_newtonian),
        }
    deadline()

    def rhs(xx: float, z: np.ndarray, mode: str, lam: float) -> np.ndarray:
        dc, uc, df, uf = z
        xf_v = float(background_interp["xf"](xx))
        xc_v = float(background_interp["xc"](xx))
        e_v = float(background_interp["e"](xx))
        h_v = float(background_interp["hconf"](xx))
        hc_x_v = float(background_interp["hc_x"](xx))
        psi = float(metric_by_mode[mode]["psi_i"](xx))
        phi_x = float(metric_by_mode[mode]["phi_x_i"](xx))
        g = lam / e_v
        r = xf_v / xc_v
        beta = p.delta * r / (1.0 + p.delta * r)
        ud = (1.0 - beta) * uc + beta * uf
        s2 = (args.k_mpc / h_v) ** 2
        out = np.empty(4, dtype=float)
        out[0] = -s2 * uc + 3.0 * phi_x + g * r * (df - dc + psi)
        out[1] = -(1.0 - hc_x_v) * uc + psi + g * r * beta * (uf - uc)
        out[2] = (
            -3.0 * (2.0 - p.delta) * df
            - p.delta * s2 * uf
            - 9.0 * (2.0 * p.delta - p.delta**2) * uf
            + 3.0 * p.delta * phi_x
            - g * psi
            - 3.0 * g * (2.0 - p.delta) * uf
        )
        out[3] = (
            (hc_x_v + 2.0) * uf
            + df / p.delta
            + psi
            + g / p.delta * (2.0 * uf - ud)
        )
        return out

    def integrate(mode: str, lam: float, x_start: float) -> np.ndarray:
        intervals = int(math.ceil((args.x_final - x_start) / args.integration_step))
        grid = np.linspace(x_start, args.x_final, intervals + 1)
        z = np.array(
            [
                float(metric_by_mode[mode]["dc_i"](x_start)),
                float(metric_by_mode[mode]["uc_i"](x_start)),
                0.0,
                0.0,
            ],
            dtype=float,
        )
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
                raise FloatingPointError(f"nonfinite response for {mode}, lambda={lam}")
        return z

    start_deep = args.x_min
    start_shallow = args.x_min + 2.0
    checks: dict[str, bool] = {}
    mode_results: dict[str, object] = {}
    for mode in S84.MODES:
        runs: dict[tuple[float, str], np.ndarray] = {}
        for lam in (0.0, p.lam):
            runs[(lam, "deep")] = integrate(mode, lam, start_deep)
            runs[(lam, "shallow")] = integrate(mode, lam, start_shallow)
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
        external_dc = float(metric_by_mode[mode]["dc_i"](args.x_final))
        external_uc = float(metric_by_mode[mode]["uc_i"](args.x_final))
        null_ash_error = float(
            np.linalg.norm(null[:2] - np.array([external_dc, external_uc]))
            / max(np.linalg.norm([external_dc, external_uc]), 1.0e-30)
        )
        checks[f"{mode}_lambda_zero_ash_tracks_analytic_seed"] = null_ash_error < 3.0e-3
        checks[f"{mode}_finite_all_runs"] = bool(all(np.all(np.isfinite(v)) for v in runs.values()))
        mode_results[mode] = {
            "final_vector_order": ["delta_c", "U_c", "delta_f", "U_f"],
            "lambda_zero_final": null.tolist(),
            "lambda_0p15_final": coupled.tolist(),
            "K4_minus_null_final": (coupled - null).tolist(),
            "start_convergence_relative": convergence,
            "lambda_zero_ash_relative_error_vs_analytic_seed": null_ash_error,
            "metric_at_final": {
                "Phi": float(metric_by_mode[mode]["phi_i"](args.x_final)),
                "Psi": float(metric_by_mode[mode]["psi_i"](args.x_final)),
            },
        }

    passed = all(checks.values())
    output = {
        "test": "A2-K4.3b-RG collective K4 test-field Puiseux response",
        "scope": (
            "Exact A1-K1 background and audited K4 dark equations, but fixed "
            "standard metric; valid before omitted fuel backreaction O(a^(4-3delta))"
        ),
        "inputs": {
            "lambda": p.lam,
            "delta": p.delta,
            "k_Mpc_inverse": args.k_mpc,
            "x_start_deep": start_deep,
            "x_start_shallow": start_shallow,
            "x_final": args.x_final,
            "integration_step_max": args.integration_step,
            "early_baryon_fraction_in_matter": fb,
            "early_ash_fraction_in_matter": fc,
            "free_streaming_fraction_in_radiation": fnu,
            "CLASS_omega_Mpc_inverse_on_exact_background": om,
        },
        "neglected_first_orders": {
            "fuel_weight_in_Einstein_sources": 4.0 - 3.0 * p.delta,
            "interaction_backreaction_on_ash": 5.0 - 3.0 * p.delta,
        },
        "mode_results": mode_results,
        "checks": checks,
        "execution_verdict": "PASS_K4_TEST_FIELD_RESPONSE" if passed else "REVIEW_REQUIRED",
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
