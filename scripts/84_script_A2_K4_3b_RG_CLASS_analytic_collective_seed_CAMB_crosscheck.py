#!/usr/bin/env python
"""A2-K4.3b-RG analytic collective-seed cross-check: CLASS vs CAMB.

This script transcribes the leading synchronous-gauge AD/CDI/BI/NID/NIV
initial conditions from the public CLASS perturbations.c implementation
(Bucher--Moodley--Turok basis) and compares them with frozen CAMB 1.6.6
outputs.  Only regular synchronous/CDM-frame variables are compared; no
Newtonian potential is obtained by subtracting nearly cancelling terms.

Primary implementation reference:
https://raw.githubusercontent.com/lesgourg/class_public/master/source/perturbations.c
function perturbations_initial_conditions, current master lines 152--162 in
the web rendering audited on 2026-07-14.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
LOCAL_DEPS = ROOT / ".deps" / "python"
if LOCAL_DEPS.exists():
    sys.path.insert(0, str(LOCAL_DEPS))

import camb  # noqa: E402


C_KM_S = 299792.458
MODES = (
    "initial_adiabatic",
    "initial_iso_CDM",
    "initial_iso_baryon",
    "initial_iso_neutrino",
    "initial_iso_neutrino_vel",
)
VARS = (
    "delta_photon",
    "delta_baryon",
    "delta_cdm",
    "delta_neutrino",
    "v_photon",
    "v_neutrino",
    "etak",
)


def class_seed(
    mode: str,
    k: float,
    tau: float,
    fnu: float,
    fg: float,
    fb: float,
    fc: float,
    om: float,
) -> np.ndarray:
    """Return [dg,db,dc,dnu,qg,qnu,eta_s] with unit CLASS amplitude."""

    y = k * tau
    y2 = y * y
    y3 = y2 * y
    omt = om * tau
    dg = db = dc = dn = tg = tn = eta_s = 0.0

    if mode == "initial_adiabatic":
        dg = -y2 / 3.0 * (1.0 - omt / 5.0)
        tg = -k * y3 / 36.0 * (
            1.0 - 3.0 * (1.0 + 5.0 * fb - fnu) / (20.0 * (1.0 - fnu)) * omt
        )
        db = 0.75 * dg
        dc = 0.75 * dg
        dn = dg
        tn = -k * y3 / 36.0 / (4.0 * fnu + 15.0) * (
            4.0 * fnu
            + 23.0
            - 3.0
            * (8.0 * fnu * fnu + 50.0 * fnu + 275.0)
            / (20.0 * (2.0 * fnu + 15.0))
            * omt
        )
        eta_s = 1.0 - y2 / (12.0 * (15.0 + 4.0 * fnu)) * (
            5.0
            + 4.0 * fnu
            - (16.0 * fnu * fnu + 280.0 * fnu + 325.0)
            / (10.0 * (2.0 * fnu + 15.0))
            * omt
        )
    elif mode == "initial_iso_CDM":
        dg = fc * omt * (-2.0 / 3.0 + omt / 4.0)
        tg = -fc * om * y2 / 12.0
        db = 0.75 * dg
        dc = 1.0 + 0.75 * dg
        dn = dg
        tn = tg
        eta_s = -fc * omt * (1.0 / 6.0 - omt / 16.0)
    elif mode == "initial_iso_baryon":
        dg = fb * omt * (-2.0 / 3.0 + omt / 4.0)
        tg = -fb * om * y2 / 12.0
        db = 1.0 + 0.75 * dg
        dc = 0.75 * dg
        dn = dg
        tn = tg
        eta_s = -fb * omt * (1.0 / 6.0 - omt / 16.0)
    elif mode == "initial_iso_neutrino":
        dg = fnu / fg * (-1.0 + y2 / 6.0)
        tg = -fnu / fg * k * k * tau * (
            1.0 / 4.0 - fb / fg * 3.0 / 16.0 * omt
        )
        db = fnu / fg / 8.0 * y2
        dc = -fnu * fb / fg / 80.0 * y2 * omt
        dn = 1.0 - y2 / 6.0
        tn = k * k * tau / 4.0
        eta_s = -fnu / (4.0 * fnu + 15.0) / 6.0 * y2
    elif mode == "initial_iso_neutrino_vel":
        dg = k * tau * fnu / fg * (
            1.0 - 3.0 / 16.0 * fb * (2.0 + fg) / fg * omt
        )
        tg = fnu / fg * 0.75 * k * (
            -1.0
            + 0.75 * fb / fg * omt
            + 3.0 / 16.0 * omt * omt * fb / (fg * fg) * (fg - 3.0 * fb)
            + y2 / 6.0
        )
        db = 0.75 * dg
        dc = -9.0 / 64.0 * fnu * fb / fg * k * tau * omt
        dn = -k * tau * (1.0 + 3.0 / 16.0 * fb * fnu / fg * omt)
        tn = 0.75 * k * (1.0 - y2 / 6.0 * (4.0 * fnu + 9.0) / (4.0 * fnu + 5.0))
        eta_s = fnu * k * tau * (
            -1.0 / (4.0 * fnu + 5.0)
            + (
                -3.0 / 64.0 * fb / fg
                + 15.0 / 4.0 / (4.0 * fnu + 15.0) / (4.0 * fnu + 5.0)
            )
            * omt
        )
    else:
        raise ValueError(mode)

    # CAMB v_photon/v_neutrino are q_i=4 theta_i/(3 k).
    qg = 4.0 * tg / (3.0 * k)
    qn = 4.0 * tn / (3.0 * k)
    return np.array([dg, db, dc, dn, qg, qn, eta_s], dtype=float)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=35.0)
    parser.add_argument("--k-mpc", type=float, default=0.05)
    args = parser.parse_args()
    if not (0.0 < args.max_runtime_seconds <= 50.0):
        parser.error("--max-runtime-seconds must be in (0, 50]")
    if not (1.0e-4 <= args.k_mpc <= 0.2):
        parser.error("--k-mpc must be in [1e-4, 0.2]")

    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("internal CLASS/CAMB seed deadline exceeded")

    h = 0.6637
    omega_m0 = 0.3517
    ombh2 = 0.02237
    omch2 = omega_m0 * h**2 - ombh2
    neff = 3.046 + 0.0535
    omega_gamma0 = 2.469e-5 / h**2
    omega_r0 = omega_gamma0 * (1.0 + 0.2271 * neff)
    fnu = 0.2271 * neff / (1.0 + 0.2271 * neff)
    fg = 1.0 - fnu
    fb = (ombh2 / h**2) / omega_m0
    fc = 1.0 - fb
    h0_mpc = 100.0 * h / C_KM_S
    om = omega_m0 * h0_mpc / math.sqrt(omega_r0)

    pars = camb.CAMBparams()
    pars.set_cosmology(
        H0=100.0 * h,
        ombh2=ombh2,
        omch2=omch2,
        omk=0.0,
        mnu=0.0,
        nnu=neff,
        tau=0.054,
    )
    pars.set_dark_energy(w=-1.0 + 0.02297, wa=0.0, dark_energy_model="ppf")
    pars.WantTransfer = True
    data = camb.get_background(pars)
    deadline()

    y = np.array([0.0020, 0.0025, 0.003125, 0.00390625, 0.0048828125])
    eta = y / args.k_mpc
    checks: dict[str, bool] = {}
    results: dict[str, object] = {}
    for mode in MODES:
        data.Params.scalar_initial_condition = mode
        camb_values = np.asarray(
            data.get_time_evolution(
                args.k_mpc,
                eta,
                vars=list(VARS),
                lAccuracyBoost=4,
            ),
            dtype=float,
        )
        deadline()
        # etak = k*eta_s in CAMB's conventional synchronous variables.
        camb_vector = camb_values.copy()
        camb_vector[:, -1] /= args.k_mpc
        analytic = np.vstack(
            [class_seed(mode, args.k_mpc, tau, fnu, fg, fb, fc, om) for tau in eta]
        )

        # One amplitude per mode; CLASS and CAMB use opposite curvature sign
        # for AD, while all entropy modes have the same unit convention.
        flat_a = analytic.reshape(-1)
        flat_c = camb_vector.reshape(-1)
        amplitude = float(np.dot(flat_a, flat_c) / np.dot(flat_a, flat_a))
        residual = camb_vector - amplitude * analytic
        absolute = float(np.max(np.abs(residual)))
        relative_l2 = float(
            np.linalg.norm(residual) / max(np.linalg.norm(camb_vector), 1.0e-300)
        )
        expected_amplitude = -1.0 if mode == "initial_adiabatic" else 1.0
        checks[f"{mode}_amplitude_convention"] = abs(amplitude - expected_amplitude) < 2.0e-3
        # These are truncated leading series; NIV is documented by CLASS as
        # having small differences from CAMB, so use a declared 0.5% L2 gate.
        checks[f"{mode}_analytic_series_matches_CAMB"] = relative_l2 < 5.0e-3
        checks[f"{mode}_all_finite"] = bool(
            np.all(np.isfinite(camb_vector)) and np.all(np.isfinite(analytic))
        )
        results[mode] = {
            "best_fit_CAMB_over_CLASS_amplitude": amplitude,
            "expected_amplitude": expected_amplitude,
            "relative_L2_residual_all_depths_variables": relative_l2,
            "max_absolute_residual": absolute,
            "analytic_first_depth": analytic[0].tolist(),
            "CAMB_first_depth": camb_vector[0].tolist(),
        }

    passed = all(checks.values())
    output = {
        "test": "A2-K4.3b-RG CLASS analytic collective seeds vs CAMB",
        "primary_reference": (
            "CLASS perturbations.c perturbations_initial_conditions, "
            "Bucher-Moodley-Turok basis"
        ),
        "scope": "Gamma=0 regular synchronous/CDM-frame seed coefficients",
        "inputs": {
            "k_Mpc_inverse": args.k_mpc,
            "k_tau_depths": y.tolist(),
            "fraction_free_streaming_radiation": fnu,
            "fraction_photons": fg,
            "fraction_baryons_in_matter": fb,
            "fraction_cdm_in_matter": fc,
            "omega_parameter_Mpc_inverse": om,
            "CAMB_version": camb.__version__,
        },
        "vector_order": ["delta_g", "delta_b", "delta_c", "delta_nu", "q_g", "q_nu", "eta_s"],
        "mode_results": results,
        "checks": checks,
        "execution_verdict": "PASS_ANALYTIC_COLLECTIVE_SEEDS" if passed else "REVIEW_REQUIRED",
        "K4_3b_RG_verdict": "NEUZAVRETA_K4_PUISEUX_RESPONSE_AND_FULL_CONSTRAINTS_MISSING",
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
