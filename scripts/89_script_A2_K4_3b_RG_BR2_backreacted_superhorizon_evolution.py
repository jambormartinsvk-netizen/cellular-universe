#!/usr/bin/env python
"""A2-K4.3b-RG-BR2: back-reacted early synchronous evolution.

Evolves the K4 dark sector, baryons, a tightly-coupled photon--baryon fluid,
separate collisionless neutrino and steam hierarchies, and the synchronous
metric.  The 0i and trace equations drive eta and h_x; 00 and traceless ij
are monitored independently with finite-difference metric derivatives.

This is an early/superhorizon backreaction gate, not recombination.  Photons
are deliberately in the leading tight-coupling closure.  Consequently a PASS
does not close K4.3b/G7 and does not replace a modifiable Boltzmann backend.
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
from scipy.linalg import expm


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


B13 = load("k4_br2_bg13", "13_script_A1_K1_cdm_background_audit_exact_zstar.py")
B11 = B13.BASE
S84 = load("k4_br2_seed84", "84_script_A2_K4_3b_RG_CLASS_analytic_collective_seed_CAMB_crosscheck.py")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=45.0)
    parser.add_argument("--x-deep", type=float, default=-25.0)
    parser.add_argument("--x-shallow", type=float, default=-23.0)
    parser.add_argument("--x-final", type=float, default=-14.0)
    parser.add_argument("--integration-step", type=float, default=2.0e-3)
    parser.add_argument("--background-step", type=float, default=5.0e-4)
    parser.add_argument("--k-mpc", type=float, default=0.05)
    parser.add_argument("--lmax", type=int, default=8)
    args = parser.parse_args()
    if not (0.0 < args.max_runtime_seconds <= 50.0):
        parser.error("--max-runtime-seconds must be in (0,50]")
    if not (-27.0 <= args.x_deep <= -24.0):
        parser.error("--x-deep must be in [-27,-24]")
    if not (1.0 <= args.x_shallow - args.x_deep <= 3.0):
        parser.error("shallow-deep separation must be in [1,3] e-folds")
    if not (-16.0 <= args.x_final <= -13.0):
        parser.error("--x-final must be in [-16,-13]")
    if args.x_final <= args.x_shallow + 6.0:
        parser.error("need at least six e-folds after the shallow start")
    if not (5.0e-4 <= args.integration_step <= 5.0e-3):
        parser.error("--integration-step must be in [5e-4,5e-3]")
    if not (2.5e-4 <= args.background_step <= 1.0e-3):
        parser.error("--background-step must be in [2.5e-4,1e-3]")
    if not (6 <= args.lmax <= 12):
        parser.error("--lmax must be in [6,12]")

    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("BR2 numerical deadline exceeded")

    p = B11.ModelParameters()
    settings = B11.IntegrationSettings(x_min=args.x_deep, step=args.background_step)
    xd, sd, xb0 = B13.integrate_background(p, settings)
    deadline()
    xbg = np.asarray(xd[::-1], dtype=float)
    states = np.asarray(sd[::-1], dtype=float)
    xf_bg, xm_bg, xr_bg = states.T
    xb_bg = xb0 * np.exp(-3.0 * xbg)
    xc_bg = xm_bg - xb_bg
    e_bg = np.sqrt(xf_bg + xm_bg + xr_bg)
    a_bg = np.exp(xbg)
    e2_x = -3.0 * p.delta * xf_bg - 3.0 * xm_bg - 4.0 * xr_bg
    hc_bg = 1.0 + e2_x / (2.0 * e_bg * e_bg)

    # H0*tau, including the radiation-limit integral below x_deep.
    tau_h0 = np.zeros_like(xbg)
    tau_h0[0] = a_bg[0] / math.sqrt(B11.radiation_density_today(p))
    integrand = np.exp(-xbg) / e_bg
    tau_h0[1:] = tau_h0[0] + np.cumsum(
        0.5 * np.diff(xbg) * (integrand[:-1] + integrand[1:])
    )

    early = (xbg >= args.x_deep + 0.5) & (xbg <= args.x_deep + 2.0)
    fb = float(np.mean(xb_bg[early] / xm_bg[early]))
    fc = float(np.mean(xc_bg[early] / xm_bg[early]))
    denom = 1.0 + 0.2271 * (p.neff_standard + p.delta_neff)
    rg = 1.0 / denom
    rn = 0.2271 * p.neff_standard / denom
    rs = 0.2271 * p.delta_neff / denom
    rfs = rn + rs
    om_over_h0 = float(np.mean(a_bg[early] * xm_bg[early] / np.sqrt(xr_bg[early])))
    q = args.k_mpc / (100.0 * p.h / 299792.458)

    interpolators = {
        "xf": PchipInterpolator(xbg, xf_bg),
        "xc": PchipInterpolator(xbg, xc_bg),
        "xb": PchipInterpolator(xbg, xb_bg),
        "xr": PchipInterpolator(xbg, xr_bg),
        "e": PchipInterpolator(xbg, e_bg),
        "hc": PchipInterpolator(xbg, hc_bg),
        "tau": PchipInterpolator(xbg, tau_h0),
    }

    DC, UC, DF, UF, DB, DG, UG = range(7)
    N0 = 7
    S0 = N0 + args.lmax + 1
    ETA = S0 + args.lmax + 1
    HX = ETA + 1
    SIZE = HX + 1

    def bg(xx: float) -> tuple[float, ...]:
        xf = float(interpolators["xf"](xx))
        xc = float(interpolators["xc"](xx))
        xb = float(interpolators["xb"](xx))
        xr = float(interpolators["xr"](xx))
        e = float(interpolators["e"](xx))
        hc = float(interpolators["hc"](xx))
        a = math.exp(xx)
        return xf, xc, xb, rg * xr, rn * xr, rs * xr, e, hc, a

    def source(xx: float, z: np.ndarray) -> tuple[float, float, float, float]:
        xf, xc, xb, xg, xn, xs, e, _, a = bg(xx)
        fn = z[N0:S0]
        fs = z[S0:ETA]
        un = 3.0 * a * e * fn[1] / (4.0 * q)
        us = 3.0 * a * e * fs[1] / (4.0 * q)
        sig_n = 0.5 * fn[2]
        sig_s = 0.5 * fs[2]
        g = p.lam / e
        pf = xf * (z[DF] + (2.0 - p.delta) * (3.0 * p.delta + g) * z[UF])
        density = (
            xc * z[DC] + xf * z[DF] + xb * z[DB]
            + xg * z[DG] + xn * fn[0] + xs * fs[0]
        )
        pressure = pf + (xg * z[DG] + xn * fn[0] + xs * fs[0]) / 3.0
        momentum = (
            xc * z[UC] + p.delta * xf * z[UF] + xb * z[UG]
            + (4.0 / 3.0) * (xg * z[UG] + xn * un + xs * us)
        )
        shear = (4.0 / 3.0) * (xn * sig_n + xs * sig_s)
        return density, pressure, momentum, shear

    def rhs(xx: float, z: np.ndarray) -> np.ndarray:
        xf, xc, xb, xg, xn, xs, e, hc, a = bg(xx)
        g = p.lam / e
        r = xf / xc
        beta = p.delta * xf / (xc + p.delta * xf)
        ud = (1.0 - beta) * z[UC] + beta * z[UF]
        s2 = (q / (a * e)) ** 2
        _, pressure, momentum, _ = source(xx, z)
        eta_x = 1.5 * momentum / (e * e)

        out = np.zeros(SIZE, dtype=float)
        out[DC] = -s2 * z[UC] - 0.5 * z[HX] + g * r * (z[DF] - z[DC])
        out[UC] = (hc - 1.0) * z[UC] + g * r * beta * (z[UF] - z[UC])
        out[DF] = (
            -3.0 * (2.0 - p.delta) * z[DF]
            - p.delta * (s2 * z[UF] + 0.5 * z[HX])
            - 9.0 * p.delta * (2.0 - p.delta) * z[UF]
            - 3.0 * g * (2.0 - p.delta) * z[UF]
        )
        out[UF] = (hc + 2.0) * z[UF] + z[DF] / p.delta + g / p.delta * (2.0 * z[UF] - ud)

        # Leading tight-coupling photon--baryon closure.
        baryon_loading = 3.0 * xb / (4.0 * xg)
        out[DB] = -s2 * z[UG] - 0.5 * z[HX]
        out[DG] = -(4.0 / 3.0) * s2 * z[UG] - (2.0 / 3.0) * z[HX]
        out[UG] = (
            (hc - baryon_loading / (1.0 + baryon_loading)) * z[UG]
            + z[DG] / (4.0 * (1.0 + baryon_loading))
        )

        kh = q / (a * e)
        for start in (N0, S0):
            f = z[start:start + args.lmax + 1]
            out[start] = -kh * f[1] - (2.0 / 3.0) * z[HX]
            out[start + 1] = kh * (f[0] - 2.0 * f[2]) / 3.0
            out[start + 2] = (
                kh * (2.0 * f[1] - 3.0 * f[3]) / 5.0
                + (4.0 / 15.0) * z[HX]
                + (8.0 / 5.0) * eta_x
            )
            for ell in range(3, args.lmax + 1):
                following = f[ell + 1] if ell < args.lmax else 0.0
                out[start + ell] = kh * (
                    ell * f[ell - 1] - (ell + 1) * following
                ) / (2.0 * ell + 1.0)

        out[ETA] = eta_x
        out[HX] = 2.0 * q * q * z[ETA] / (a * e) ** 2 - (hc + 2.0) * z[HX] - 9.0 * pressure / (e * e)
        return out

    # Exact finite collisionless internal seeds exp(A k tau)e0/e1.
    hierarchy = np.zeros((args.lmax + 1, args.lmax + 1), dtype=float)
    hierarchy[0, 1] = -1.0
    hierarchy[1, 0] = 1.0 / 3.0
    hierarchy[1, 2] = -2.0 / 3.0
    for ell in range(2, args.lmax + 1):
        hierarchy[ell, ell - 1] = ell / (2.0 * ell + 1.0)
        if ell < args.lmax:
            hierarchy[ell, ell + 1] = -(ell + 1.0) / (2.0 * ell + 1.0)

    modes = list(S84.MODES) + ["internal_nu_steam_density", "internal_nu_steam_velocity"]

    def initial(mode: str, xx: float) -> np.ndarray:
        z = np.zeros(SIZE, dtype=float)
        xf, xc, xb, xg, xn, xs, e, _, a = bg(xx)
        tau = float(interpolators["tau"](xx))
        y = q * tau
        if mode in S84.MODES:
            seed = S84.class_seed(mode, q, tau, rfs, rg, fb, fc, om_over_h0)
            z[DG], z[DB], z[DC] = seed[0], seed[1], seed[2]
            z[N0] = seed[3]
            z[S0] = seed[3]
            z[UG] = 3.0 * a * e * seed[4] / (4.0 * q)
            z[N0 + 1] = seed[5]
            z[S0 + 1] = seed[5]
            z[ETA] = seed[6]
        else:
            basis = np.zeros(args.lmax + 1)
            basis[0 if mode.endswith("density") else 1] = 1.0
            internal_vec = expm(hierarchy * y) @ basis
            z[N0:S0] = internal_vec
            z[S0:ETA] = -(xn / xs) * internal_vec
            z[ETA] = 0.0

        density, _, _, _ = source(xx, z)
        z[HX] = 2.0 * (q * q * z[ETA] + 1.5 * a * a * density) / (a * e) ** 2
        return z

    def integrate(mode: str, x_start: float) -> tuple[np.ndarray, np.ndarray]:
        count = int(math.ceil((args.x_final - x_start) / args.integration_step))
        grid = np.linspace(x_start, args.x_final, count + 1)
        values = np.empty((count + 1, SIZE), dtype=float)
        values[0] = initial(mode, x_start)
        for i in range(count):
            xx = float(grid[i])
            step = float(grid[i + 1] - grid[i])
            z = values[i]
            k1 = rhs(xx, z)
            k2 = rhs(xx + step / 2.0, z + step * k1 / 2.0)
            k3 = rhs(xx + step / 2.0, z + step * k2 / 2.0)
            k4 = rhs(xx + step, z + step * k3)
            values[i + 1] = z + step * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
            if i % 500 == 0:
                deadline()
            if not np.all(np.isfinite(values[i + 1])):
                raise FloatingPointError(f"nonfinite state for {mode} at x={grid[i+1]}")
        return grid, values

    def residual_audit(grid: np.ndarray, values: np.ndarray) -> dict[str, object]:
        n = len(grid)
        density = np.empty(n)
        pressure = np.empty(n)
        momentum = np.empty(n)
        shear = np.empty(n)
        e = np.empty(n)
        hc = np.empty(n)
        a = np.exp(grid)
        for i, xx in enumerate(grid):
            density[i], pressure[i], momentum[i], shear[i] = source(float(xx), values[i])
            e[i] = float(interpolators["e"](xx))
            hc[i] = float(interpolators["hc"](xx))
        eta = values[:, ETA]
        hx = values[:, HX]
        eta_x_fd = np.gradient(eta, grid, edge_order=2)
        eta_xx_fd = np.gradient(eta_x_fd, grid, edge_order=2)
        hx_x_fd = np.gradient(hx, grid, edge_order=2)
        ae2 = (a * e) ** 2
        ledgers = {
            "00": np.vstack([q * q * eta, -0.5 * ae2 * hx, 1.5 * a * a * density]),
            "0i": np.vstack([eta_x_fd, -1.5 * momentum / (e * e)]),
            "trace_ij": np.vstack([
                ae2 * hx_x_fd,
                ae2 * (hc + 2.0) * hx,
                -2.0 * q * q * eta,
                9.0 * a * a * pressure,
            ]),
            "traceless_ij": np.vstack([
                ae2 * hx_x_fd,
                6.0 * ae2 * eta_xx_fd,
                ae2 * (hc + 2.0) * (hx + 6.0 * eta_x_fd),
                -2.0 * q * q * eta,
                9.0 * a * a * shear,
            ]),
        }
        use = slice(4, -4)
        result: dict[str, object] = {}
        for name, terms in ledgers.items():
            residual = np.sum(terms, axis=0)
            term_norm = np.sum(np.abs(terms), axis=0)
            global_norm = max(float(np.max(term_norm[use])), 1.0e-300)
            global_rel = float(np.max(np.abs(residual[use])) / global_norm)
            active = term_norm > 1.0e-8 * global_norm
            active[:4] = False
            active[-4:] = False
            point_rel = float(np.max(np.abs(residual[active]) / term_norm[active])) if np.any(active) else 0.0
            result[name] = {
                "max_absolute_residual": float(np.max(np.abs(residual[use]))),
                "global_relative_residual": global_rel,
                "max_active_pointwise_relative_residual": point_rel,
                "global_term_norm": global_norm,
            }
        result["all_four_global_relative_below_3e-3"] = all(
            float(result[name]["global_relative_residual"]) < 3.0e-3
            for name in ledgers
        )
        return result

    checks: dict[str, bool] = {}
    results: dict[str, object] = {}
    for mode in modes:
        gd, zd = integrate(mode, args.x_deep)
        gs, zs = integrate(mode, args.x_shallow)
        deadline()
        deep_audit = residual_audit(gd, zd)
        shallow_audit = residual_audit(gs, zs)
        scale = max(float(np.linalg.norm(zd[-1])), float(np.linalg.norm(zs[-1])), 1.0e-30)
        convergence = float(np.linalg.norm(zd[-1] - zs[-1]) / scale)
        checks[f"{mode}_deep_four_constraints"] = bool(deep_audit["all_four_global_relative_below_3e-3"])
        checks[f"{mode}_shallow_four_constraints"] = bool(shallow_audit["all_four_global_relative_below_3e-3"])
        checks[f"{mode}_two_start_convergence"] = convergence < 3.0e-3
        checks[f"{mode}_finite"] = bool(np.all(np.isfinite(zd)) and np.all(np.isfinite(zs)))
        dark_metric_norm = float(np.linalg.norm(zd[-1, [DC, UC, DF, UF, ETA, HX]]))
        if mode.startswith("internal_"):
            checks[f"{mode}_metric_dark_null"] = dark_metric_norm < 1.0e-10
        results[mode] = {
            "two_start_final_relative_difference": convergence,
            "deep_residuals": deep_audit,
            "shallow_residuals": shallow_audit,
            "deep_final_dark_metric_vector_dc_Uc_df_Uf_eta_hx": zd[-1, [DC, UC, DF, UF, ETA, HX]].tolist(),
            "deep_final_state_norm": float(np.linalg.norm(zd[-1])),
        }
        deadline()

    passed = all(checks.values())
    output = {
        "test": "A2-K4.3b-RG-BR2 back-reacted early synchronous evolution",
        "scope": "early superhorizon; leading photon-baryon tight coupling; separate nu and steam l<=lmax",
        "inputs": {
            "lambda": p.lam,
            "delta": p.delta,
            "q_k_over_H0": q,
            "x_deep": args.x_deep,
            "x_shallow": args.x_shallow,
            "x_final": args.x_final,
            "integration_step_max": args.integration_step,
            "lmax": args.lmax,
            "radiation_fractions": {"photon": rg, "nu": rn, "steam": rs},
        },
        "modes": modes,
        "mode_results": results,
        "checks": checks,
        "execution_verdict": "PASS_BR2_BACKREACTED_EARLY_SYSTEM" if passed else "REVIEW_BR2_BACKREACTED_EARLY_SYSTEM",
        "K4_3b_RG_verdict": "NEUZAVRETA_EXPLICIT_PUISEUX_COEFFICIENT_AND_FULL_PHOTON_BACKEND_GATES_MISSING",
        "canonical_score": "60/100 = G6",
        "next_step": "BR3 extract/residual-test fractional coefficients; then full photon hierarchy/recombination backend",
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
