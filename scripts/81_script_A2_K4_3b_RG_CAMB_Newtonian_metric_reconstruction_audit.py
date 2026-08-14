#!/usr/bin/env python
"""A2-K4.3b-RG reconstruction of Phi_N and Psi_N from CAMB outputs.

The frozen binary exposes the synchronous/CDM-frame curvature `etak`, the
scaled Newtonian CDM velocity, the conformal Hubble rate, and k^2 times the
Weyl potential.  CAMB's documented transfer conventions and its local
symbolic gauge map imply

  sigma_CDM = -v_newtonian_cdm * Hconf / k,
  Phi_N     = (etak - Hconf*sigma_CDM)/k,
  Weyl      = k^2 (Phi_N+Psi_N)/2.

This script reconstructs both Newtonian potentials for all five collective
regular modes and independently checks Psi_N=(sigma'+Hconf*sigma)/k on the
interior active grid.  It is still a Gamma=0 metric interface audit.
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
    parser.add_argument("--depths", type=int, default=12)
    args = parser.parse_args()
    if not (0.0 < args.max_runtime_seconds <= 50.0):
        parser.error("--max-runtime-seconds must be in (0, 50]")
    if not (1.0e-4 <= args.k_mpc <= 0.2):
        parser.error("--k-mpc must be in [1e-4, 0.2]")
    if not (1.0e-5 <= args.y_min <= 2.0e-3):
        parser.error("--y-min must be in [1e-5, 2e-3]")
    if not (10 <= args.depths <= 16):
        parser.error("--depths must be in [10, 16]")

    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("internal CAMB metric reconstruction deadline exceeded")

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
        # `a` and `H` are background outputs and nonzero even before the
        # perturbation start.  Detect the placeholder prefix using only the
        # three perturbation transfers.
        perturbation_block = values[:, 2:]
        active = np.flatnonzero(np.max(np.abs(perturbation_block), axis=1) > 1.0e-30)
        if len(active) < 5:
            raise RuntimeError(f"too few active metric rows for {mode}")
        first = int(active[0])

        hconf = by_name["H"]
        sigma = -by_name["v_newtonian_cdm"] * hconf / args.k_mpc
        phi_n = (by_name["etak"] - hconf * sigma) / args.k_mpc
        weyl_phi = by_name["Weyl"] / args.k_mpc**2
        psi_n = 2.0 * weyl_phi - phi_n

        sigma_prime = np.gradient(sigma, eta, edge_order=2)
        psi_from_shear = (sigma_prime + hconf * sigma) / args.k_mpc
        # Skip two points adjacent to the activation discontinuity and the
        # two last, least-superhorizon points.  Finite differences on a
        # factor-two grid are a consistency diagnostic, not a precision
        # Einstein solver.
        lo = first + 2
        hi = min(args.depths - 2, first + 7)
        if hi <= lo:
            raise RuntimeError("no interior metric reconstruction window")
        absolute_residual = np.abs(psi_from_shear[lo:hi] - psi_n[lo:hi])
        term_norm = np.maximum(
            np.maximum(np.abs(psi_from_shear[lo:hi]), np.abs(psi_n[lo:hi])),
            1.0e-12,
        )
        relative_residual = absolute_residual / term_norm
        max_rel = float(np.max(relative_residual))
        max_abs = float(np.max(absolute_residual))

        checks[f"{mode}_metric_arrays_finite"] = bool(
            np.all(np.isfinite(phi_n[first:]))
            and np.all(np.isfinite(psi_n[first:]))
            and np.all(np.isfinite(sigma[first:]))
        )
        checks[f"{mode}_Weyl_identity_exact"] = bool(
            np.max(np.abs((phi_n + psi_n) / 2.0 - weyl_phi)) < 1.0e-13
        )
        # Loose because the independent route differentiates sparse samples.
        checks[f"{mode}_shear_route_consistent_on_sparse_grid"] = bool(
            max_rel < 0.35 or max_abs < 2.0e-5
        )
        rows[mode] = {
            "first_active_index": first,
            "first_active_k_tau": float(y[first]),
            "audit_window_k_tau": [float(y[lo]), float(y[hi - 1])],
            "Phi_N_at_first_active": float(phi_n[first]),
            "Psi_N_at_first_active": float(psi_n[first]),
            "Weyl_phi_at_first_active": float(weyl_phi[first]),
            "slip_Phi_minus_Psi_at_first_active": float(phi_n[first] - psi_n[first]),
            "max_abs_Psi_shear_route_residual": max_abs,
            "max_rel_Psi_shear_route_residual": max_rel,
        }

    passed = all(checks.values())
    output = {
        "test": "A2-K4.3b-RG CAMB Newtonian metric reconstruction audit",
        "scope": "Gamma=0 five-mode metric interface; not exact K4 evolution",
        "frozen_conventions": {
            "CAMB_Weyl": "k^2(Phi_N+Psi_N)/2",
            "CAMB_v_newtonian_cdm": "-v_N,c k/Hconf",
            "local_symbolic_map": "v_N,c=sigma_CDM; Phi_N=(etak-Hconf*sigma)/k",
        },
        "inputs": {
            "k_Mpc_inverse": args.k_mpc,
            "k_tau_depths": y.tolist(),
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
