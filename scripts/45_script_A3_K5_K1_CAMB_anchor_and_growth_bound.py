#!/usr/bin/env python3
"""A3 conservative CMB-normalized growth gate for A2-K5/K1.

This script deliberately separates two computations:

1. unmodified CAMB 1.6.6 supplies a reproducible CMB-normalized linear
   matter spectrum for two declared background surrogates;
2. the action-derived K5/K1 equations from script 33 supply the exact-A1
   late-time weighted matter-growth ratio.

The K5/K1 perturbations are NOT implemented inside the CAMB source.  The
combined result is therefore a conservative hybrid growth gate, not a
TT/TE/EE/lensing likelihood.  To bias the test in favour of K5/K1, the
growth correction is explicitly set to unity below k=0.01 h/Mpc.

All numerical assumptions, package versions, null tests, and the
predeclared one-dimensional KiDS-Legacy screening threshold are serialized
to stdout as JSON.  The physical interpretation belongs in the audit MD.
"""

from __future__ import annotations

import dataclasses
import importlib.util
import json
import math
from pathlib import Path
import platform
import sys


ROOT = Path(__file__).resolve().parents[1]
LOCAL_DEPS = ROOT / ".deps" / "python"
if LOCAL_DEPS.exists():
    sys.path.insert(0, str(LOCAL_DEPS))

import camb  # noqa: E402
from camb import model  # noqa: E402
import numpy as np  # noqa: E402


BASE_PATH = Path(__file__).with_name(
    "33_script_A2_K5_K1_quasistatic_growth_gate.py"
)
SPEC = importlib.util.spec_from_file_location("a3_k5_k1_growth", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load validated K5/K1 growth code: {BASE_PATH}")
BASE33 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE33
SPEC.loader.exec_module(BASE33)


C_KM_S = 299792.458
K_GATE_MIN_H_MPC = 0.01
KIDS_CENTRAL = 0.815
KIDS_PLUS = 0.016
KIDS_MINUS = 0.021
KIDS_SCREEN_SIGMA = 3.0
KIDS_SCREEN_HIGH = KIDS_CENTRAL + KIDS_SCREEN_SIGMA * KIDS_PLUS


def top_hat_window(x: np.ndarray) -> np.ndarray:
    out = np.ones_like(x)
    mask = np.abs(x) > 1.0e-4
    xm = x[mask]
    out[mask] = 3.0 * (np.sin(xm) - xm * np.cos(xm)) / xm**3
    if np.any(~mask):
        xs = x[~mask]
        out[~mask] = 1.0 - xs**2 / 10.0 + xs**4 / 280.0
    return out


def sigma_r_from_pk(kh: np.ndarray, pk: np.ndarray, radius_mpc_h: float) -> float:
    window = top_hat_window(kh * radius_mpc_h)
    integrand = kh**3 * pk * window**2 / (2.0 * math.pi**2)
    variance = float(np.trapezoid(integrand, x=np.log(kh)))
    if variance <= 0.0:
        raise FloatingPointError(f"Non-positive sigma_R variance: {variance}")
    return math.sqrt(variance)


def camb_spectrum(label: str, w0: float, wa: float, ns: float) -> dict:
    h = 0.6637
    omega_m0 = 0.3517
    ombh2 = 0.02237
    # The registered A1 background has massless radiation neutrinos and puts
    # all non-baryonic present matter into the CDM/ash variable.
    omch2 = omega_m0 * h**2 - ombh2

    pars = camb.CAMBparams()
    pars.set_cosmology(
        H0=100.0 * h,
        ombh2=ombh2,
        omch2=omch2,
        omk=0.0,
        mnu=0.0,
        nnu=3.046 + 0.0535,
        tau=0.054,
    )
    pars.InitPower.set_params(As=2.1e-9, ns=ns, r=0.0)
    pars.set_dark_energy(w=w0, wa=wa, dark_energy_model="ppf")
    pars.set_matter_power(redshifts=[0.0], kmax=8.0)
    pars.NonLinear = model.NonLinear_none
    results = camb.get_results(pars)
    kh, redshifts, pk = results.get_matter_power_spectrum(
        minkh=1.0e-4, maxkh=5.0, npoints=500
    )
    sigma8_camb = float(results.get_sigma8()[0])
    sigma8_integral = sigma_r_from_pk(kh, pk[0], 8.0)
    return {
        "label": label,
        "w0": w0,
        "wa": wa,
        "ns": ns,
        "kh_h_per_Mpc": kh,
        "pk_Mpc_over_h_cubed": pk[0],
        "sigma8_CAMB": sigma8_camb,
        "sigma8_independent_integral": sigma8_integral,
        "sigma8_integral_relative_error": abs(
            sigma8_integral / sigma8_camb - 1.0
        ),
        "S8_CAMB": sigma8_camb * math.sqrt(omega_m0 / 0.3),
        "inputs": {
            "H0_km_s_Mpc": 100.0 * h,
            "Omega_m0": omega_m0,
            "ombh2": ombh2,
            "omch2": omch2,
            "mnu_eV": 0.0,
            "Neff": 3.046 + 0.0535,
            "tau": 0.054,
            "As": 2.1e-9,
        },
    }


def weighted_growth_ratio(p, step: float, q: float) -> float:
    x_star = -math.log1p(p.z_star)
    settings = BASE33.BASE13.BASE.IntegrationSettings(x_min=x_star, step=step)
    xs_desc, states_desc, xb0 = BASE33.BASE13.integrate_background(p, settings)
    xs = xs_desc[::-1]
    states = states_desc[::-1]
    coeff = BASE33.coefficients(xs, states, xb0, p)
    full = BASE33.integrate_mode(xs, coeff, q, True, True)
    reference = BASE33.integrate_mode(xs, coeff, q, False, False)
    xc0 = p.omega_m0 - xb0
    xm0 = p.omega_m0
    delta_m_full = (
        xc0 * full["delta_c_today"] + xb0 * full["delta_b_today"]
    ) / xm0
    delta_m_reference = (
        xc0 * reference["delta_c_today"]
        + xb0 * reference["delta_b_today"]
    ) / xm0
    return float(delta_m_full / delta_m_reference)


def growth_grid(lam: float, step: float, npoints: int = 36) -> dict:
    p0 = BASE33.BASE13.BASE.ModelParameters()
    p = dataclasses.replace(p0, lam=lam)
    kh = np.geomspace(K_GATE_MIN_H_MPC, 5.0, npoints)
    # q = k/(H0/c).  With k in h/Mpc and H0=100h km/s/Mpc, h cancels.
    q = kh * C_KM_S / 100.0
    ratio = np.array([weighted_growth_ratio(p, step, float(qi)) for qi in q])
    return {
        "lambda": lam,
        "step_dln_a": step,
        "kh_h_per_Mpc": kh,
        "q_k_over_H0": q,
        "weighted_growth_ratio": ratio,
        "ratio_min": float(np.min(ratio)),
        "ratio_max": float(np.max(ratio)),
    }


def apply_conservative_growth(camb_run: dict, growth: dict) -> dict:
    kh = camb_run["kh_h_per_Mpc"]
    pk = camb_run["pk_Mpc_over_h_cubed"]
    ratio = np.ones_like(kh)
    mask = kh >= K_GATE_MIN_H_MPC
    ratio[mask] = np.interp(
        np.log(kh[mask]),
        np.log(growth["kh_h_per_Mpc"]),
        growth["weighted_growth_ratio"],
    )
    sigma8_modified = sigma_r_from_pk(kh, pk * ratio**2, 8.0)
    omega_m0 = camb_run["inputs"]["Omega_m0"]
    return {
        "sigma8_hybrid_K5_K1": sigma8_modified,
        "S8_hybrid_K5_K1": sigma8_modified * math.sqrt(omega_m0 / 0.3),
        "sigma8_ratio_to_CAMB_surrogate": (
            sigma8_modified / camb_run["sigma8_independent_integral"]
        ),
        "growth_forced_to_unity_below_k_h_Mpc": K_GATE_MIN_H_MPC,
    }


def serializable(value):
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, dict):
        return {key: serializable(item) for key, item in value.items()}
    if isinstance(value, list):
        return [serializable(item) for item in value]
    return value


def main() -> int:
    # Both were stated before this run: constant w_f is a transparent bracket;
    # the CPL pair is the pre-existing background summary used in v3.18 notes.
    camb_runs = [
        camb_spectrum("constant_w_f_surrogate", -1.0 + 0.02297, 0.0, 0.96432),
        camb_spectrum("registered_CPL_surrogate", -0.919, -0.612, 0.96432),
    ]

    growth = growth_grid(lam=0.15, step=5.0e-4)
    null_growth = growth_grid(lam=0.0, step=5.0e-4, npoints=8)
    hybrids = [
        {
            "label": run["label"],
            **apply_conservative_growth(run, growth),
        }
        for run in camb_runs
    ]

    integral_ok = all(
        run["sigma8_integral_relative_error"] < 5.0e-3 for run in camb_runs
    )
    null_error = float(
        np.max(np.abs(null_growth["weighted_growth_ratio"] - 1.0))
    )
    null_ok = null_error < 1.0e-12
    all_above_screen = all(
        item["S8_hybrid_K5_K1"] > KIDS_SCREEN_HIGH for item in hybrids
    )

    output = {
        "test": "A3-K5/K1 conservative CAMB-normalized hybrid growth gate",
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "camb": camb.__version__,
            "numpy": np.__version__,
            "local_dependency_directory": str(LOCAL_DEPS),
        },
        "observational_screen": {
            "KiDS_Legacy_S8": KIDS_CENTRAL,
            "plus_68_percent": KIDS_PLUS,
            "minus_68_percent": KIDS_MINUS,
            "predeclared_screen_sigma": KIDS_SCREEN_SIGMA,
            "one_dimensional_high_threshold": KIDS_SCREEN_HIGH,
            "warning": (
                "This is a screening threshold, not a reanalysis of the "
                "KiDS shear likelihood under modified gravity."
            ),
        },
        "CAMB_surrogates": camb_runs,
        "exact_A1_K5_K1_growth": growth,
        "lambda_zero_growth_null_test": {
            "grid": null_growth,
            "max_abs_ratio_minus_one": null_error,
            "passed": null_ok,
        },
        "hybrid_results": hybrids,
        "checks": {
            "independent_sigma8_integral_matches_CAMB": integral_ok,
            "lambda_zero_growth_ratio_is_unity": null_ok,
            "all_conservative_hybrids_above_3sigma_KiDS_screen": (
                all_above_screen
            ),
        },
        "status": (
            "FAIL_A3_CONSERVATIVE_GROWTH_GATE"
            if integral_ok and null_ok and all_above_screen
            else "A3_CONSERVATIVE_GATE_INCONCLUSIVE_OR_NUMERICAL_FAIL"
        ),
        "scope": (
            "CAMB-normalized linear P(k) plus exact-background K5/K1 "
            "late-time growth ratio. Not a custom K5/K1 Boltzmann solver and "
            "not a TT/TE/EE/lensing or KiDS likelihood."
        ),
    }
    print(json.dumps(serializable(output), indent=2, ensure_ascii=False))
    return 0 if integral_ok and null_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
