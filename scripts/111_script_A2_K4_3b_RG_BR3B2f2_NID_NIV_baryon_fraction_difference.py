#!/usr/bin/env python
"""BR3B-2f-2: isolate the late NID/NIV seed coefficient by composition differences.

Script 110 tried to recover a very small high-order CDM coefficient from one
CAMB run.  Lower powers then dominated the fit and the NID/NIV ratios were not
stable.  This bounded clone keeps the total physical matter density fixed and
changes only the baryon/CDM split.  A centred difference in f_b cancels the
pure-radiation lower-order seed and isolates the baryon-driven part that first
generates h_x for NID/NIV.

Two independent difference steps and two early-time windows are mandatory.
Failure is REVIEW_UNCLOSED: this is an input-extraction gate, not a physical
death test for K4.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
LOCAL = ROOT / ".deps" / "python"
if LOCAL.exists():
    sys.path.insert(0, str(LOCAL))

import camb  # noqa: E402


MODES = {
    "NID": ("initial_iso_neutrino", 3),
    "NIV": ("initial_iso_neutrino_vel", 2),
}


def fit_coeff(w: np.ndarray, values: np.ndarray, powers: list[int]):
    design = np.column_stack([w**power for power in powers])
    coeff = np.linalg.lstsq(design, values, rcond=None)[0]
    residual = np.linalg.norm(design @ coeff - values) / max(
        np.linalg.norm(values), 1.0e-300
    )
    return (
        {power: float(value) for power, value in zip(powers, coeff)},
        float(residual),
        float(np.linalg.cond(design)),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=45.0)
    parser.add_argument("--k-mpc", type=float, default=0.05)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 50.0:
        parser.error("runtime must be in (0, 50]")
    if not 1.0e-4 <= args.k_mpc <= 0.2:
        parser.error("k outside [1e-4, 0.2] Mpc^-1")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("BR3B-2f-2 deadline exceeded")

    h = 0.6637
    omega_m0 = 0.3517
    total_matter_h2 = omega_m0 * h**2
    base_ombh2 = 0.02237
    base_fb = base_ombh2 / total_matter_h2
    neff = 3.046 + 0.0535
    rnu = 0.2271 * neff / (1 + 0.2271 * neff)
    rgamma = 1 - rnu

    def make_background(fb: float):
        pars = camb.CAMBparams()
        pars.set_cosmology(
            H0=100 * h,
            ombh2=fb * total_matter_h2,
            omch2=(1 - fb) * total_matter_h2,
            omk=0,
            mnu=0,
            nnu=neff,
            tau=0.054,
        )
        pars.set_dark_energy(w=-1 + 0.02297, wa=0, dark_energy_model="ppf")
        pars.WantTransfer = True
        result = camb.get_background(pars)
        deadline()
        return result

    # Multiplicative half-widths around the physical baryon fraction.
    # They are far enough apart to beat float64 cancellation, while the
    # agreement test below rejects a nonlinear finite-difference artefact.
    difference_steps = {"small": 0.14, "large": 0.28}
    backgrounds: dict[str, dict[str, object]] = {}
    for label, relative_step in difference_steps.items():
        backgrounds[label] = {
            "minus": make_background(base_fb * (1 - relative_step)),
            "plus": make_background(base_fb * (1 + relative_step)),
        }

    windows = {
        "deep": np.geomspace(1.2e-3, 4.0e-3, 30),
        "shallow": np.geomspace(1.8e-3, 6.0e-3, 30),
    }
    # The difference cancels the dominant pure-radiation pieces, but the
    # explicit lower powers absorb finite precision and earlier matter terms.
    bases = {
        "NID": {
            "dc": [3, 4, 5, 6],
            "eta": [1, 2, 3, 4, 5, 6],
            "U": [0, 1, 2, 3, 4, 5, 6],
        },
        "NIV": {
            "dc": [2, 3, 4, 5],
            "eta": [0, 1, 2, 3, 4, 5],
            "U": [-1, 0, 1, 2, 3, 4, 5],
        },
    }

    results: dict[str, object] = {}
    checks: dict[str, bool] = {}
    for short, (camb_mode, target_power) in MODES.items():
        mode_rows: dict[str, object] = {}
        for step_label, relative_step in difference_steps.items():
            pair = backgrounds[step_label]
            fb_minus = base_fb * (1 - relative_step)
            fb_plus = base_fb * (1 + relative_step)
            step_rows: dict[str, object] = {}
            for window_label, ykt in windows.items():
                tau = ykt / args.k_mpc
                evolved: dict[str, np.ndarray] = {}
                for side in ("minus", "plus"):
                    data = pair[side]
                    data.Params.scalar_initial_condition = camb_mode
                    evolved[side] = np.asarray(
                        data.get_time_evolution(
                            args.k_mpc,
                            tau,
                            vars=[
                                "a",
                                "H",
                                "delta_cdm",
                                "v_photon",
                                "v_neutrino",
                                "etak",
                            ],
                            lAccuracyBoost=4,
                        ),
                        dtype=float,
                    )
                    deadline()

                minus = evolved["minus"]
                plus = evolved["plus"]
                same_a = np.max(
                    np.abs(plus[:, 0] - minus[:, 0])
                    / np.maximum(np.abs(plus[:, 0]), 1.0e-300)
                )
                same_hconf = np.max(
                    np.abs(plus[:, 1] - minus[:, 1])
                    / np.maximum(np.abs(plus[:, 1]), 1.0e-300)
                )
                # H is CAMB's conformal Hubble rate and q=4 theta/(3k), so
                # U=H theta/k^2=3 H q/(4 k).
                transformed = []
                for values in (minus, plus):
                    aa, hconf, dc, qg, qn, etak = values.T
                    transformed.append(
                        np.column_stack(
                            [
                                aa,
                                dc,
                                etak / args.k_mpc,
                                3 * hconf * qg / (4 * args.k_mpc),
                                3 * hconf * qn / (4 * args.k_mpc),
                            ]
                        )
                    )
                derivative = (transformed[1] - transformed[0]) / (fb_plus - fb_minus)
                aa = 0.5 * (transformed[1][:, 0] + transformed[0][:, 0])
                pivot = float(np.exp(np.mean(np.log(aa))))
                w = aa / pivot
                ddc = derivative[:, 1]
                deta = derivative[:, 2]
                dug = derivative[:, 3]
                dun = derivative[:, 4]

                cdc, rdc, kdc = fit_coeff(w, ddc, bases[short]["dc"])
                ceta, reta, keta = fit_coeff(w, deta, bases[short]["eta"])
                cug, rug, kug = fit_coeff(w, dug, bases[short]["U"])
                cun, run, kun = fit_coeff(w, dun, bases[short]["U"])
                hx = -2 * target_power * cdc[target_power]
                resolved_scale = max(np.max(np.abs(ddc)), 1.0e-300)
                resolved_ratio = abs(cdc[target_power]) / resolved_scale
                if abs(hx) < 1.0e-30:
                    ratios = {
                        "eta_x_over_hx": float("nan"),
                        "U_gamma_over_hx": float("nan"),
                        "U_fs_over_hx": float("nan"),
                    }
                else:
                    ratios = {
                        "eta_x_over_hx": target_power * ceta[target_power] / hx,
                        "U_gamma_over_hx": cug[target_power] / hx,
                        "U_fs_over_hx": cun[target_power] / hx,
                    }
                # This residual is a diagnostic only.  The differentiated
                # NID/NIV coefficient is baryon-driven, so the full 0i row can
                # also contain baryon momentum at the same order.
                radiation_only_0i = ratios["eta_x_over_hx"] - 2 * (
                    rgamma * ratios["U_gamma_over_hx"]
                    + rnu * ratios["U_fs_over_hx"]
                )
                step_rows[window_label] = {
                    "pivot_a": pivot,
                    "h_x_derivative_coefficient": hx,
                    "target_dc_coefficient_over_max_abs_ddc": resolved_ratio,
                    **ratios,
                    "radiation_only_0i_diagnostic_not_gate": radiation_only_0i,
                    "background_relative_mismatch": {
                        "a": float(same_a),
                        "Hconf": float(same_hconf),
                    },
                    "fit_relative_residuals": {
                        "dc": rdc,
                        "eta": reta,
                        "Ug": rug,
                        "Un": run,
                    },
                    "basis_condition_numbers": {
                        "dc": kdc,
                        "eta": keta,
                        "Ug": kug,
                        "Un": kun,
                    },
                }
            mode_rows[step_label] = step_rows

        # Gate the result on finite coefficients, two windows, two difference
        # steps and controlled fits.  No radiation-only 0i requirement is used.
        all_rows = [
            mode_rows[step][window]
            for step in difference_steps
            for window in windows
        ]
        checks[f"{short}_all_outputs_finite"] = bool(
            all(
                np.isfinite(row[key])
                for row in all_rows
                for key in (
                    "h_x_derivative_coefficient",
                    "eta_x_over_hx",
                    "U_gamma_over_hx",
                    "U_fs_over_hx",
                )
            )
        )
        checks[f"{short}_same_total_background_below_1e-10"] = bool(
            all(
                max(row["background_relative_mismatch"].values()) < 1.0e-10
                for row in all_rows
            )
        )
        checks[f"{short}_all_fits_below_2_percent"] = bool(
            all(
                max(row["fit_relative_residuals"].values()) < 2.0e-2
                for row in all_rows
            )
        )
        checks[f"{short}_target_dc_coefficient_resolved_above_1e-4"] = bool(
            all(row["target_dc_coefficient_over_max_abs_ddc"] > 1.0e-4 for row in all_rows)
        )
        for key in (
            "eta_x_over_hx",
            "U_gamma_over_hx",
            "U_fs_over_hx",
        ):
            deep = mode_rows["large"]["deep"][key]
            shallow = mode_rows["large"]["shallow"][key]
            scale = max(abs(deep), abs(shallow), 1.0e-10)
            checks[f"{short}_{key}_two_window_20pct"] = bool(
                abs(deep - shallow) / scale < 0.20
            )
            small = mode_rows["small"]["deep"][key]
            scale = max(abs(deep), abs(small), 1.0e-10)
            checks[f"{short}_{key}_two_step_20pct"] = bool(
                abs(deep - small) / scale < 0.20
            )
        results[short] = {
            "target_power": target_power,
            "difference_results": mode_rows,
        }
        deadline()

    passed = bool(checks) and all(checks.values())
    output = {
        "test": "A2-K4.3b-RG-BR3B-2f-2 NID/NIV baryon-fraction difference",
        "supersedes_execution_only": (
            "script 110 single-run high-order NID/NIV extraction; its "
            "REVIEW_UNCLOSED result remains preserved"
        ),
        "CAMB_version": camb.__version__,
        "fixed_total_background": {
            "Omega_m0": omega_m0,
            "total_matter_h2": total_matter_h2,
            "base_baryon_fraction": base_fb,
        },
        "radiation_fractions": {"R_gamma": rgamma, "R_fs": rnu},
        "mode_results": results,
        "checks": checks,
        "execution_verdict": (
            "PASS_DIFFERENTIAL_MODE_COEFFICIENT_EXTRACTION"
            if passed
            else "REVIEW_DIFFERENTIAL_MODE_COEFFICIENT_EXTRACTION_UNCLOSED"
        ),
        "scope_limit": (
            "radiation-only 0i is diagnostic because baryon momentum may enter "
            "the differentiated coefficient; a full composition-differenced "
            "0i ledger is still required before these inputs can close BR3B-2f"
        ),
        "K4_3b_RG_verdict": "NEUZAVRETA_BR3B2F_FULL_SOURCE_LEDGER_REQUIRED",
        "canonical_score": "60/100 = G6",
        "next_step": (
            "if stable, derive the full baryon-inclusive 0i source and combine "
            "it with the already solved fractional sectors; if unstable, replace "
            "numerical extraction by an exact Frobenius recurrence"
        ),
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
