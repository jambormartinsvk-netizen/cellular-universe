#!/usr/bin/env python
"""Fine-grid alias of the A2-K4.3b-RG CAMB metric audit.

Script 81 reconstructed Phi/Psi correctly but its factor-two sampling made
the independent sigma-derivative check inaccurate for the tiny CDI/BI
potentials.  This script uses a pre-registered 1.25 depth ratio and judges the
same algebraic identity without loosening the absolute tolerance.
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


MODES = (
    "initial_adiabatic",
    "initial_iso_CDM",
    "initial_iso_baryon",
    "initial_iso_neutrino",
    "initial_iso_neutrino_vel",
)
VARS = ("a", "H", "etak", "Weyl", "v_newtonian_cdm")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=35.0)
    parser.add_argument("--k-mpc", type=float, default=0.05)
    parser.add_argument("--y-min", type=float, default=2.0e-4)
    parser.add_argument("--depths", type=int, default=32)
    parser.add_argument("--depth-ratio", type=float, default=1.25)
    args = parser.parse_args()
    if not (0.0 < args.max_runtime_seconds <= 50.0):
        parser.error("--max-runtime-seconds must be in (0, 50]")
    if not (1.0e-4 <= args.k_mpc <= 0.2):
        parser.error("--k-mpc must be in [1e-4, 0.2]")
    if not (1.0e-5 <= args.y_min <= 5.0e-4):
        parser.error("--y-min must be in [1e-5, 5e-4]")
    if not (24 <= args.depths <= 40):
        parser.error("--depths must be in [24, 40]")
    if not (1.15 <= args.depth_ratio <= 1.35):
        parser.error("--depth-ratio must be in [1.15, 1.35]")

    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("internal fine-grid CAMB metric deadline exceeded")

    y = args.y_min * args.depth_ratio ** np.arange(args.depths, dtype=float)
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

    checks: dict[str, bool] = {}
    rows: dict[str, object] = {}
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
        by_name = {name: values[:, i] for i, name in enumerate(VARS)}
        active = np.flatnonzero(np.max(np.abs(values[:, 2:]), axis=1) > 1.0e-30)
        if len(active) < 10:
            raise RuntimeError(f"too few active metric rows for {mode}")
        first = int(active[0])
        hconf = by_name["H"]
        sigma = -by_name["v_newtonian_cdm"] * hconf / args.k_mpc
        phi_n = (by_name["etak"] - hconf * sigma) / args.k_mpc
        weyl_phi = by_name["Weyl"] / args.k_mpc**2
        psi_n = 2.0 * weyl_phi - phi_n
        sigma_prime = np.gradient(sigma, eta, edge_order=2)
        psi_from_shear = (sigma_prime + hconf * sigma) / args.k_mpc

        # Avoid the backend activation edge and stop while k*tau<0.08.
        indices = np.flatnonzero((np.arange(args.depths) >= first + 3) & (y < 0.08))
        if len(indices) < 5:
            raise RuntimeError("insufficient fine-grid superhorizon audit window")
        absolute = np.abs(psi_from_shear[indices] - psi_n[indices])
        norm = np.maximum(
            np.maximum(np.abs(psi_from_shear[indices]), np.abs(psi_n[indices])),
            1.0e-12,
        )
        relative = absolute / norm
        max_abs = float(np.max(absolute))
        max_rel = float(np.max(relative))
        rms_abs = float(np.sqrt(np.mean(absolute**2)))

        checks[f"{mode}_finite"] = bool(
            np.all(np.isfinite(phi_n[first:])) and np.all(np.isfinite(psi_n[first:]))
        )
        checks[f"{mode}_Weyl_identity_exact"] = bool(
            np.max(np.abs((phi_n + psi_n) / 2.0 - weyl_phi)) < 1.0e-13
        )
        checks[f"{mode}_fine_grid_shear_route"] = bool(
            max_rel < 0.08 or max_abs < 2.0e-5
        )
        rows[mode] = {
            "first_active_k_tau": float(y[first]),
            "audit_window_k_tau": [float(y[indices[0]]), float(y[indices[-1]])],
            "Phi_N_first_active": float(phi_n[first]),
            "Psi_N_first_active": float(psi_n[first]),
            "Weyl_phi_first_active": float(weyl_phi[first]),
            "max_abs_Psi_shear_route_residual": max_abs,
            "rms_abs_Psi_shear_route_residual": rms_abs,
            "max_rel_Psi_shear_route_residual": max_rel,
        }

    passed = all(checks.values())
    output = {
        "test": "A2-K4.3b-RG fine-grid CAMB Newtonian metric reconstruction",
        "supersedes_for_derivative_sampling": "81_script_A2_K4_3b_RG_CAMB_Newtonian_metric_reconstruction_audit.py",
        "scope": "Gamma=0 metric interface only",
        "inputs": {
            "k_Mpc_inverse": args.k_mpc,
            "k_tau_min": args.y_min,
            "depth_ratio": args.depth_ratio,
            "depth_count": args.depths,
            "CAMB_version": camb.__version__,
        },
        "mode_results": rows,
        "checks": checks,
        "execution_verdict": "PASS_NULL_NEWTONIAN_METRIC_INTERFACE" if passed else "REVIEW_REQUIRED",
        "K4_3b_RG_verdict": "NEUZAVRETA_EXACT_K4_BACKGROUND_AND_FORCED_SERIES_MISSING",
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
