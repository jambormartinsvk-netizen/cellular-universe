#!/usr/bin/env python3
"""A2-K7.1a-K2: open-system dissipation reconstruction gate.

For a canonical fuel scalar, a local dissipative mean equation has energy
transfer

    Q1 = Upsilon(phi, state) * dot(phi)^2,

and the K7 split gives

    dot(phi)^2 = (delta-epsilon) rho_F.

On the exact K7.0 background the required coefficient is therefore

    Upsilon/H0 = [(1-epsilon) lambda
                  + 3 E epsilon (1-delta)]/(delta-epsilon).

This script checks whether that required coefficient is positive, finite,
and single-valued as a function of the monotonic background scalar.  Such a
reconstruction is necessary but not sufficient: it does not derive Upsilon,
the memory kernel, or the noise correlator from the local phi-chi-psi action.
"""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path
import sys

import numpy as np
from scipy.integrate import cumulative_trapezoid


SOURCE = Path(__file__).with_name(
    "50_script_A2_K7_0_mediator_ledger_collision_gate.py"
)
SPEC = importlib.util.spec_from_file_location("k7_0_base_open", SOURCE)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load {SOURCE}")
K70 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = K70
SPEC.loader.exec_module(K70)


def run_fraction(base: dict, fraction: float) -> dict:
    p = base["p"]
    xs = base["xs"]
    xf = base["xf"]
    e = base["e"]
    epsilon = fraction * p.delta
    kinetic_fraction = p.delta - epsilon

    varphi_x = np.sqrt(3.0 * kinetic_fraction * xf) / e
    varphi = np.concatenate(
        ([0.0], cumulative_trapezoid(varphi_x, xs))
    )
    upsilon_h0 = (
        (1.0 - epsilon) * p.lam
        + 3.0 * e * epsilon * (1.0 - p.delta)
    ) / kinetic_fraction
    upsilon_h = upsilon_h0 / e

    q1_required_x = (
        (1.0 - epsilon) * p.lam * xf / e
        + 3.0 * epsilon * (1.0 - p.delta) * xf
    )
    q1_reconstructed_x = upsilon_h0 * kinetic_fraction * xf / e
    ledger_residual = float(
        np.max(np.abs(q1_reconstructed_x - q1_required_x))
    )

    dlnu_dx = np.gradient(np.log(upsilon_h0), xs)
    dphi_dx = np.gradient(varphi, xs)
    dlnu_dphi = np.divide(
        dlnu_dx,
        dphi_dx,
        out=np.full_like(dlnu_dx, np.nan),
        where=np.abs(dphi_dx) > 1.0e-14,
    )
    finite_slope = dlnu_dphi[np.isfinite(dlnu_dphi)]

    checks = {
        "positive_fuel_kinetic_term": kinetic_fraction > 0.0,
        "monotonic_scalar_clock": bool(np.all(varphi_x > 0.0)),
        "positive_finite_Upsilon": bool(
            np.all(upsilon_h0 > 0.0) and np.all(np.isfinite(upsilon_h0))
        ),
        "exact_background_source_reconstruction": ledger_residual < 1.0e-11,
    }
    return {
        "fraction": fraction,
        "epsilon": epsilon,
        "delta_minus_epsilon": kinetic_fraction,
        "Delta_varphi_recombination_to_today": float(varphi[-1] - varphi[0]),
        "Upsilon_over_H0_recombination": float(upsilon_h0[0]),
        "Upsilon_over_H0_today": float(upsilon_h0[-1]),
        "Upsilon_over_H_recombination": float(upsilon_h[0]),
        "Upsilon_over_H_today": float(upsilon_h[-1]),
        "Upsilon_max_to_min": float(np.max(upsilon_h0) / np.min(upsilon_h0)),
        "max_abs_dlnUpsilon_dvarphi": float(np.max(np.abs(finite_slope))),
        "source_ledger_residual": ledger_residual,
        "checks": checks,
        "reconstruction_passed": all(checks.values()),
        "microphysical_derivation_passed": False,
        "noise_and_memory_derived": False,
    }


def main() -> int:
    base = K70.background(2.5e-4)
    rows = [
        run_fraction(base, fraction)
        for fraction in K70.EPSILON_OVER_DELTA_GRID
    ]
    all_reconstructed = all(row["reconstruction_passed"] for row in rows)

    print("# A2-K7.1a-K2 — open-system dissipation reconstruction")
    print()
    print(
        "| eps/delta | epsilon | Delta varphi | Upsilon/H0 rec | "
        "Upsilon/H0 now | Upsilon/H rec | Upsilon/H now | max/min | "
        "ledger residual | reconstruction | microphysics |"
    )
    print("|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|:---:|")
    for row in rows:
        print(
            f"| {row['fraction']:.2f} | {row['epsilon']:.8f} | "
            f"{row['Delta_varphi_recombination_to_today']:.6f} | "
            f"{row['Upsilon_over_H0_recombination']:.6f} | "
            f"{row['Upsilon_over_H0_today']:.6f} | "
            f"{row['Upsilon_over_H_recombination']:.6f} | "
            f"{row['Upsilon_over_H_today']:.6f} | "
            f"{row['Upsilon_max_to_min']:.6f} | "
            f"{row['source_ledger_residual']:.3e} | "
            f"{'PASS' if row['reconstruction_passed'] else 'FAIL'} | "
            "NOT DERIVED |"
        )

    print()
    print("## Verdict")
    print()
    print(f"- positive single-valued background reconstruction: `{all_reconstructed}`;")
    print("- derivation from the phi-chi-psi action: `NOT PASSED`;")
    print("- memory kernel and noise correlator: `NOT DERIVED`;")
    print("- K7.1a-K2 status: `SURVIVES RECONSTRUCTION ONLY`; no physical")
    print("  K7.1 pass and no score increase until a spectral kernel is supplied.")
    return 0 if all_reconstructed else 1


if __name__ == "__main__":
    raise SystemExit(main())
