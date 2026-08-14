#!/usr/bin/env python
"""BR3B-2e-2a: CAMB cross-check of the leading NIV shear constraint.

The CLASS NIV initial-condition excerpt gives eta_s~k*tau and shear_ur~k*tau
with different denominators.  Before using these coefficients in K4, query
independent CAMB 1.6.6 symbolic variables hdot_s, eta_s and pi_r.  CAMB's
massless-neutrino pi_r equals 2*sigma in the Ma--Bertschinger convention.

This is a convention/series audit.  Any mismatch is REVIEW_UNCLOSED, never a
death of K4.
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
import camb.symbolic as cs  # noqa: E402


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
            raise TimeoutError("NIV CAMB cross-check deadline exceeded")

    hubble_h = 0.6637
    omega_m0 = 0.3517
    ombh2 = 0.02237
    omch2 = omega_m0 * hubble_h**2 - ombh2
    neff = 3.046 + 0.0535
    rnu = 0.2271 * neff / (1.0 + 0.2271 * neff)

    pars = camb.CAMBparams()
    pars.set_cosmology(H0=100 * hubble_h, ombh2=ombh2, omch2=omch2,
                       omk=0.0, mnu=0.0, nnu=neff, tau=0.054)
    pars.set_dark_energy(w=-1 + 0.02297, wa=0.0, dark_energy_model="ppf")
    pars.WantTransfer = True
    pars.scalar_initial_condition = "initial_iso_neutrino_vel"
    data = camb.get_background(pars)
    deadline()

    # k*tau values remain superhorizon and provide a scaling regression.
    ktau = np.array([2.0e-4, 2.5e-4, 3.125e-4, 3.90625e-4, 4.8828125e-4])
    tau = ktau / args.k_mpc
    values = np.asarray(data.get_time_evolution(
        args.k_mpc,
        tau,
        vars=[cs.eta_s, cs.hdot_s, cs.pi_r],
        lAccuracyBoost=4,
    ), dtype=float)
    deadline()

    eta = values[:, 0]
    hdot = values[:, 1]
    shear = values[:, 2] / 2.0
    eta_coeff = eta / ktau
    shear_coeff = shear / ktau
    # In radiation domination Hconf*tau -> 1, hence h_x/(k*tau)=hdot/k.
    hx_coeff = hdot / args.k_mpc
    leading_traceless = 2 * hx_coeff + 12 * eta_coeff + 12 * rnu * shear_coeff

    camb_coeff = {
        "eta_over_ktau": float(np.median(eta_coeff)),
        "sigma_over_ktau": float(np.median(shear_coeff)),
        "hx_over_ktau": float(np.median(hx_coeff)),
        "leading_traceless_combination": float(np.median(leading_traceless)),
    }
    class_expected = {
        "eta_over_ktau": -rnu / (4 * rnu + 5),
        "sigma_over_ktau": 1 / (4 * rnu + 15),
        "hx_over_ktau": 0.0,
    }
    scale = max(abs(camb_coeff["eta_over_ktau"]),
                abs(12 * rnu * camb_coeff["sigma_over_ktau"]), 1.0e-300)
    relative_constraint = abs(camb_coeff["leading_traceless_combination"]) / scale
    checks = {
        "CAMB_all_values_finite": bool(np.all(np.isfinite(values))),
        "CAMB_eta_scales_linearly": bool(np.std(eta_coeff) / max(abs(np.mean(eta_coeff)), 1e-300) < 5e-3),
        "CAMB_shear_scales_linearly": bool(np.std(shear_coeff) / max(abs(np.mean(shear_coeff)), 1e-300) < 5e-3),
        "CAMB_hx_scaling_is_resolved": bool(np.all(np.isfinite(hx_coeff))),
        "CAMB_matches_CLASS_eta_coefficient": bool(abs(camb_coeff["eta_over_ktau"] - class_expected["eta_over_ktau"]) < 5e-3),
        "CAMB_matches_CLASS_shear_coefficient": bool(abs(camb_coeff["sigma_over_ktau"] - class_expected["sigma_over_ktau"]) < 5e-3),
        "leading_traceless_constraint_relative_below_1e-2": bool(relative_constraint < 1e-2),
    }

    constraint_pass = checks["leading_traceless_constraint_relative_below_1e-2"]
    output = {
        "test": "A2-K4.3b-RG-BR3B-2e-2a NIV CAMB shear/constraint cross-check",
        "CAMB_version": camb.__version__,
        "variable_map": "CAMB pi_r=2*sigma_MB, h_x/(k tau)=hdot_s/k in the leading radiation limit",
        "ktau": ktau.tolist(),
        "raw_columns_eta_hdot_pi_r": values.tolist(),
        "CAMB_coefficients": camb_coeff,
        "CLASS_leading_coefficients": class_expected,
        "leading_constraint_relative_residual": relative_constraint,
        "checks": checks,
        "execution_verdict": ("PASS_NIV_LEADING_SHEAR_CONSTRAINT"
                              if all(checks.values()) else
                              "REVIEW_NIV_SHEAR_OR_TRUNCATION_CONVENTION"),
        "physical_verdict": ("leading CAMB NIV variables satisfy the audited traceless equation"
                             if constraint_pass else
                             "unresolved mismatch: do not populate BR3B-2e-2 coefficients yet"),
        "K4_3b_RG_verdict": "NEUZAVRETA_NIV_SHEAR_MAPPING_AUDIT_REQUIRED",
        "canonical_score": "60/100 = G6",
        "next_step": "audit exact CAMB/CLASS metric normalization or evaluate the full finite-time Einstein residual before BR3B-2e-2",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
    except Exception as exc:  # pragma: no cover
        print(json.dumps({"execution_verdict": "ERROR_UNCLOSED", "error": repr(exc)}))
        raise SystemExit(2)
