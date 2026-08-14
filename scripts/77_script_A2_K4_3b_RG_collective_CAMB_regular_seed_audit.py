#!/usr/bin/env python
"""A2-K4.3b-RG: five collective regular-mode seeds from local CAMB.

This is a NULL (Gamma=0) Einstein--Boltzmann reference, not an exact K4
backend.  It samples the five standard scalar initial conditions at several
superhorizon depths, exports regular CDM-frame variables, and audits only
gauge-invariant entropy/relative-flow combinations plus the Weyl potential.

The script never promotes CAMB's geodesic-CDM evolution to the interacting K4
system.  Its role is to freeze independently reproducible leading seeds that
the later K4 Frobenius correction must match as lambda/E -> 0.
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


MODES = (
    "initial_adiabatic",
    "initial_iso_CDM",
    "initial_iso_baryon",
    "initial_iso_neutrino",
    "initial_iso_neutrino_vel",
)

# These are CAMB's documented time-evolution outputs.  Delta variables and
# etak are in the regular CDM frame.  Entropies formed below are invariant
# under a scalar time shift.  Velocity differences use like-normalized CAMB
# heat-flux outputs only within the two radiation species; baryon/CDM velocity
# comparisons are deliberately not inferred here.
VARS = (
    "delta_cdm",
    "delta_baryon",
    "delta_photon",
    "delta_neutrino",
    "Weyl",
    "etak",
    "v_photon",
    "pi_photon",
    "E_2",
    "v_neutrino",
)


def signed_log_slope(v0: float, v1: float, y0: float, y1: float) -> float | None:
    """Return a two-depth absolute-value power, or None below noise."""

    scale = max(abs(v0), abs(v1))
    if not np.isfinite(scale) or scale < 1.0e-28:
        return None
    if v0 == 0.0 or v1 == 0.0:
        return None
    return float(math.log(abs(v1 / v0)) / math.log(y1 / y0))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=45.0)
    parser.add_argument("--k-mpc", type=float, default=0.05)
    parser.add_argument("--y-min", type=float, default=2.0e-4)
    parser.add_argument("--depths", type=int, default=6)
    args = parser.parse_args()
    if not (0.0 < args.max_runtime_seconds <= 50.0):
        parser.error("--max-runtime-seconds must be in (0, 50]")
    if not (1.0e-4 <= args.k_mpc <= 0.2):
        parser.error("--k-mpc must be in [1e-4, 0.2] Mpc^-1")
    if not (1.0e-5 <= args.y_min <= 2.0e-3):
        parser.error("--y-min must be in [1e-5, 2e-3]")
    if not (4 <= args.depths <= 8):
        parser.error("--depths must be in [4, 8]")

    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("internal K4.3b-RG CAMB seed deadline exceeded")

    y = args.y_min * 2.0 ** np.arange(args.depths, dtype=float)
    eta = y / args.k_mpc

    h = 0.6637
    omega_m0 = 0.3517
    ombh2 = 0.02237
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
    pars.set_dark_energy(w=-1.0 + 0.02297, wa=0.0, dark_energy_model="ppf")
    pars.WantTransfer = True
    data = camb.get_background(pars)
    deadline()

    mode_rows: dict[str, object] = {}
    seed_descriptors: list[list[float]] = []
    checks: dict[str, bool] = {}
    for mode in MODES:
        data.Params.scalar_initial_condition = mode
        values = np.asarray(
            data.get_time_evolution(
                args.k_mpc,
                eta,
                vars=list(VARS),
                lAccuracyBoost=4,
            ),
            dtype=float,
        )
        deadline()
        if values.shape != (args.depths, len(VARS)):
            raise RuntimeError(f"unexpected CAMB output shape {values.shape}")
        by_name = {name: values[:, i] for i, name in enumerate(VARS)}

        # Gauge-invariant entropy combinations.  All density variables have
        # the same scalar time-shift contribution after dividing radiation
        # deltas by 4/3, so these differences are frame independent.
        s_cg = by_name["delta_cdm"] - 0.75 * by_name["delta_photon"]
        s_bg = by_name["delta_baryon"] - 0.75 * by_name["delta_photon"]
        s_rg = 0.75 * (
            by_name["delta_neutrino"] - by_name["delta_photon"]
        )
        # CAMB v_photon and v_neutrino are like-normalized radiation heat
        # flux variables, hence their difference is gauge invariant.
        v_rg = by_name["v_neutrino"] - by_name["v_photon"]
        weyl = by_name["Weyl"]

        invariant = np.column_stack([s_cg, s_bg, s_rg, v_rg, weyl])
        finite = bool(np.all(np.isfinite(values)) and np.all(np.isfinite(invariant)))
        checks[f"{mode}_finite"] = finite

        # Descriptor at the deepest available point, normalized per mode.
        # It is used only for a numerical rank/independence audit.
        descriptor = np.array(
            [s_cg[0], s_bg[0], s_rg[0], v_rg[0], weyl[0]], dtype=float
        )
        norm = float(np.linalg.norm(descriptor))
        if norm == 0.0 or not np.isfinite(norm):
            normalized = np.zeros_like(descriptor)
        else:
            normalized = descriptor / norm
        seed_descriptors.append(normalized.tolist())

        slopes: dict[str, float | None] = {}
        for name, series in (
            ("S_c_gamma", s_cg),
            ("S_b_gamma", s_bg),
            ("S_nu_gamma", s_rg),
            ("V_nu_gamma", v_rg),
            ("Weyl", weyl),
            ("pi_photon", by_name["pi_photon"]),
            ("pi_neutrino", np.zeros(args.depths)),
        ):
            slopes[name] = signed_log_slope(
                float(series[0]), float(series[1]), float(y[0]), float(y[1])
            )

        regular_norm = np.linalg.norm(invariant[:, :4], axis=1)
        checks[f"{mode}_no_nonfinite_or_gt_1e12_invariant"] = bool(
            finite and float(np.max(np.abs(invariant))) < 1.0e12
        )
        mode_rows[mode] = {
            "deepest_descriptor_normalized": normalized.tolist(),
            "deepest_values": {
                "S_c_gamma": float(s_cg[0]),
                "S_b_gamma": float(s_bg[0]),
                "S_nu_gamma": float(s_rg[0]),
                "V_nu_gamma": float(v_rg[0]),
                "Weyl": float(weyl[0]),
                "etak": float(by_name["etak"][0]),
                "pi_photon": float(by_name["pi_photon"][0]),
            },
            "two_deepest_log_slopes": slopes,
            "invariant_entropy_flow_norm_by_depth": regular_norm.tolist(),
        }

    descriptor_matrix = np.asarray(seed_descriptors, dtype=float).T
    singular_values = np.linalg.svd(descriptor_matrix, compute_uv=False)
    numerical_rank = int(np.linalg.matrix_rank(descriptor_matrix, tol=1.0e-7))
    checks["five_CAMB_initial_conditions_numerically_independent"] = numerical_rank == 5
    checks["all_requested_modes_returned"] = set(mode_rows) == set(MODES)
    passed = all(checks.values())

    output = {
        "test": "A2-K4.3b-RG five collective CAMB regular seed audit",
        "scope": (
            "Gamma=0 standard Einstein-Boltzmann seed reference only; "
            "not the interacting K4 equations or a G7 closure"
        ),
        "CAMB_version": camb.__version__,
        "inputs": {
            "k_Mpc_inverse": args.k_mpc,
            "k_tau_depths": y.tolist(),
            "conformal_times_Mpc": eta.tolist(),
            "H0_km_s_Mpc": 100.0 * h,
            "Omega_m0": omega_m0,
            "Neff": 3.046 + 0.0535,
            "w_constant_surrogate": -1.0 + 0.02297,
        },
        "invariant_descriptor_order": [
            "S_c_gamma",
            "S_b_gamma",
            "S_nu_gamma",
            "V_nu_gamma",
            "Weyl",
        ],
        "mode_results": mode_rows,
        "descriptor_singular_values": singular_values.tolist(),
        "descriptor_numerical_rank": numerical_rank,
        "checks": checks,
        "execution_verdict": "PASS_NULL_COLLECTIVE_SEEDS" if passed else "REVIEW_REQUIRED",
        "K4_3b_RG_verdict": "NEUZAVRETA_K4_FROBENIUS_CORRECTIONS_MISSING",
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
