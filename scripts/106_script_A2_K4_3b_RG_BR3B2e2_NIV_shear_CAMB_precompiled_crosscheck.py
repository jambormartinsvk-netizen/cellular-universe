#!/usr/bin/env python
"""Precompiled CAMB clone replacing script 105 (which needs a compiler).

CAMB's built-in NIV outputs provide delta_nu and q_nu=4 theta_nu/(3k).
The massless-neutrino Euler equation gives

    sigma_nu = delta_nu/4 - (3/4) d q_nu / d(k tau).

This recovers the shear without custom symbolic compilation and tests the
leading synchronous traceless Einstein coefficient.  Script 105 remains an
ERROR_UNCLOSED artifact; it is not overwritten.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
LOCAL_DEPS = ROOT / ".deps" / "python"
if LOCAL_DEPS.exists():
    sys.path.insert(0, str(LOCAL_DEPS))

import camb  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=35.0)
    parser.add_argument("--k-mpc", type=float, default=0.05)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 50.0:
        parser.error("runtime must be in (0, 50]")
    if not 1.0e-4 <= args.k_mpc <= 0.2:
        parser.error("k outside [1e-4,0.2] Mpc^-1")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("precompiled CAMB NIV deadline exceeded")

    h = 0.6637
    omega_m0 = 0.3517
    ombh2 = 0.02237
    omch2 = omega_m0 * h**2 - ombh2
    neff = 3.046 + 0.0535
    rnu = 0.2271 * neff / (1 + 0.2271 * neff)

    pars = camb.CAMBparams()
    pars.set_cosmology(H0=100 * h, ombh2=ombh2, omch2=omch2, omk=0,
                       mnu=0, nnu=neff, tau=0.054)
    pars.set_dark_energy(w=-1 + 0.02297, wa=0, dark_energy_model="ppf")
    pars.WantTransfer = True
    pars.scalar_initial_condition = "initial_iso_neutrino_vel"
    data = camb.get_background(pars)
    deadline()

    y = np.array([0.0016, 0.0020, 0.0025, 0.003125, 0.00390625,
                  0.0048828125, 0.006103515625])
    tau = y / args.k_mpc
    values = np.asarray(data.get_time_evolution(
        args.k_mpc,
        tau,
        vars=["delta_neutrino", "v_neutrino", "etak", "delta_cdm"],
        lAccuracyBoost=4,
    ), dtype=float)
    deadline()

    delta_nu, q_nu, etak, delta_cdm = values.T
    # Fit the regular parity structure q=q0+q2*y^2+q4*y^4.  Using all depths
    # is less noisy than pointwise finite differences.
    design = np.column_stack([np.ones_like(y), y**2, y**4])
    q0, q2, q4 = np.linalg.lstsq(design, q_nu, rcond=None)[0]
    dq_dy = 2 * q2 * y + 4 * q4 * y**3
    sigma = delta_nu / 4 - 3 * dq_dy / 4
    eta_s = etak / args.k_mpc

    eta_coeff = eta_s / y
    sigma_coeff = sigma / y
    # CDM continuity in synchronous/CDM gauge: delta_c'=-h'/2.  A nonzero
    # leading h_x~y would imply delta_c~y; test its fitted linear coefficient.
    dc_design = np.column_stack([y, y**2, y**3])
    dc1, dc2, dc3 = np.linalg.lstsq(dc_design, delta_cdm, rcond=None)[0]
    hx_coeff = -2 * dc1
    traceless = 2 * hx_coeff + 12 * float(np.median(eta_coeff)) + 12 * rnu * float(np.median(sigma_coeff))

    expected_camb_consistent = {
        "eta_over_ktau": -rnu / (4 * rnu + 5),
        "sigma_over_ktau": 1 / (4 * rnu + 5),
        "hx_over_ktau": 0.0,
    }
    class_master_excerpt = {
        "eta_over_ktau": -rnu / (4 * rnu + 5),
        "sigma_over_ktau": 1 / (4 * rnu + 15),
        "note": "CLASS master marks surrounding NIV expressions as small differences versus CAMB",
    }
    measured = {
        "q_fit_coefficients_q0_q2_q4": [float(q0), float(q2), float(q4)],
        "eta_over_ktau": float(np.median(eta_coeff)),
        "sigma_over_ktau_from_Euler": float(np.median(sigma_coeff)),
        "hx_over_ktau_from_CDM_continuity": float(hx_coeff),
        "leading_traceless_residual": float(traceless),
    }
    norm = max(abs(12 * measured["eta_over_ktau"]),
               abs(12 * rnu * measured["sigma_over_ktau_from_Euler"]), 1e-300)
    relative = abs(traceless) / norm
    checks = {
        "all_precompiled_outputs_finite": bool(np.all(np.isfinite(values))),
        "q_even_polynomial_fit_relative_residual_below_1e-6": bool(
            np.linalg.norm(q_nu - design @ np.array([q0, q2, q4]))
            / max(np.linalg.norm(q_nu), 1e-300) < 1e-6
        ),
        "eta_matches_CAMB_consistent_coefficient": bool(
            abs(measured["eta_over_ktau"] - expected_camb_consistent["eta_over_ktau"]) < 5e-3
        ),
        "Euler_derived_shear_matches_4Rnu_plus_5": bool(
            abs(measured["sigma_over_ktau_from_Euler"] - expected_camb_consistent["sigma_over_ktau"]) < 5e-3
        ),
        "Euler_derived_shear_excludes_CLASS_4Rnu_plus_15_at_5e-3": bool(
            abs(measured["sigma_over_ktau_from_Euler"] - class_master_excerpt["sigma_over_ktau"]) > 5e-3
        ),
        "leading_hx_coefficient_is_small": bool(abs(hx_coeff) < 5e-3),
        "leading_traceless_relative_residual_below_2_percent": bool(relative < 2e-2),
    }
    passed = all(checks.values())
    output = {
        "test": "A2-K4.3b-RG-BR3B-2e-2 NIV precompiled CAMB shear cross-check",
        "supersedes_execution_only": "script 105; its compiler ERROR_UNCLOSED remains preserved",
        "CAMB_version": camb.__version__,
        "derivation": "sigma=delta_nu/4-(3/4)d q_nu/d(k tau), q_nu=4 theta_nu/(3k)",
        "measured": measured,
        "expected_CAMB_self_consistent": expected_camb_consistent,
        "CLASS_master_excerpt": class_master_excerpt,
        "leading_traceless_relative_residual": relative,
        "checks": checks,
        "execution_verdict": ("PASS_CAMB_SELF_CONSISTENT_NIV_SHEAR_MAPPING"
                              if passed else "REVIEW_NIV_PRECOMPILED_CROSSCHECK"),
        "physical_verdict": ("use sigma_NIV=ktau/(4Rnu+5) for the self-consistent recurrence; do not import the isolated CLASS 4Rnu+15 coefficient"
                             if passed else "NIV shear mapping remains unresolved"),
        "older_statement_limited": "script 84 validated a truncated CLASS seed vector that omitted shear; it did not validate the NIV shear coefficient",
        "K4_3b_RG_verdict": "NEUZAVRETA_BR3B2E2_FULL_SHEAR_SECTOR_STILL_REQUIRED",
        "canonical_score": "60/100 = G6",
        "next_step": "BR3B-2e-2 solve the NID p+2 and NIV p+1 shear sectors using the self-consistent hierarchy recurrence, then test all Einstein rows",
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
