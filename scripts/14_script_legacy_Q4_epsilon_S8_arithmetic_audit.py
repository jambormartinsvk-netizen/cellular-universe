#!/usr/bin/env python3
"""Arithmetic audit of legacy Q4 epsilon and S8 tension statements.

This script checks numbers only. It does not derive the scar mechanism,
validate the V3 perturbation equation, or perform a cosmological likelihood.
The JSON output explicitly separates arithmetic from physical validation.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import sys


MPC_IN_KM = 3.085677581491367e19
PLANCK_TIME_S = 5.391247e-44


def h0_to_inverse_seconds(h0_km_s_mpc: float) -> float:
    return h0_km_s_mpc / MPC_IN_KM


def epsilon_audit(lam: float, h0_km_s_mpc: float) -> dict[str, float]:
    h0_s = h0_to_inverse_seconds(h0_km_s_mpc)
    epsilon_eff = lam * h0_s * PLANCK_TIME_S
    epsilon_squared = epsilon_eff**2
    target_yield = 1.0e-123
    return {
        "lambda": lam,
        "H0_km_s_Mpc": h0_km_s_mpc,
        "H0_s_inverse": h0_s,
        "Planck_time_s": PLANCK_TIME_S,
        "epsilon_eff": epsilon_eff,
        "epsilon_eff_log10": math.log10(epsilon_eff),
        "epsilon_eff_squared": epsilon_squared,
        "epsilon_squared_log10": math.log10(epsilon_squared),
        "epsilon_squared_over_1e_minus_123": epsilon_squared / target_yield,
        "factor_between_1e_minus_123_and_epsilon_squared": (
            target_yield / epsilon_squared
        ),
    }


def one_dimensional_residuals(
    prediction: float,
    observed: float,
    sigma_plus: float,
    sigma_minus: float,
) -> dict[str, float]:
    difference = prediction - observed
    symmetric_mean = 0.5 * (sigma_plus + sigma_minus)
    return {
        "prediction": prediction,
        "observed": observed,
        "difference": difference,
        "sigma_plus": sigma_plus,
        "sigma_minus": sigma_minus,
        "residual_using_upward_sigma": difference / sigma_plus,
        "residual_using_mean_symmetric_sigma": difference / symmetric_mean,
        "residual_using_legacy_0p018_sigma": difference / 0.018,
        "residual_using_pipeline_0p019_sigma": difference / 0.019,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--h0", type=float, default=66.37)
    parser.add_argument("--lambda-primary", type=float, default=0.15)
    parser.add_argument("--lambda-secondary", type=float, default=0.10)
    parser.add_argument("--s8-primary", type=float, default=0.874)
    parser.add_argument("--s8-secondary", type=float, default=0.859)
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    kids_legacy = {
        "label": "KiDS-Legacy cosmic shear",
        "S8": 0.815,
        "sigma_plus": 0.016,
        "sigma_minus": 0.021,
        "source": "arXiv:2503.19441",
    }
    kids_joint = {
        "label": "KiDS-Legacy + DES-Y3 shear + Pantheon+ + DESI-Y1 BAO",
        "S8": 0.814,
        "sigma_plus": 0.011,
        "sigma_minus": 0.012,
        "source": "arXiv:2503.19442",
    }
    kids_w0wa_all_probes = {
        "label": "KiDS-Legacy all probes, w0waCDM",
        "S8": 0.837,
        "sigma_plus": 0.008,
        "sigma_minus": 0.008,
        "source": "arXiv:2512.11041",
    }

    predictions = {
        "lambda_0p15_pipeline": args.s8_primary,
        "lambda_0p10_pipeline": args.s8_secondary,
    }

    s8_audit: dict[str, dict[str, dict[str, float]]] = {}
    for data in (kids_legacy, kids_joint, kids_w0wa_all_probes):
        comparisons = {}
        for label, prediction in predictions.items():
            comparisons[label] = one_dimensional_residuals(
                prediction,
                data["S8"],
                data["sigma_plus"],
                data["sigma_minus"],
            )
        s8_audit[data["label"]] = {
            "metadata": data,
            "comparisons": comparisons,
        }

    output = {
        "test": "legacy-Q4-epsilon-and-S8-arithmetic",
        "arithmetic_status": "PASS",
        "physical_status": "NOT_TESTED",
        "environment": {
            "python": sys.version.split()[0],
            "platform": platform.platform(),
        },
        "epsilon": {
            "lambda_primary": epsilon_audit(args.lambda_primary, args.h0),
            "lambda_secondary": epsilon_audit(args.lambda_secondary, args.h0),
            "interpretation_limit": (
                "lambda*H0*tP is a dimensionless conversion of the fitted rate; "
                "squaring it does not derive a failure×scar probability."
            ),
        },
        "S8": {
            "predictions_are_from_simplified_pipeline_09": predictions,
            "one_dimensional_residuals": s8_audit,
            "interpretation_limit": (
                "Residual/sigma values ignore model uncertainty, covariance, "
                "parameter refitting, and the missing interacting perturbations. "
                "They are not likelihood significances for the cellular model."
            ),
        },
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
