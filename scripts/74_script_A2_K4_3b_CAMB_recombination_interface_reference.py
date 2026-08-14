#!/usr/bin/env python
"""A2-K4.3b null recombination/tight-coupling interface reference.

Unmodified local CAMB supplies the frozen standard atomic history used by the
null reference.  This is not a K4 perturbation implementation and cannot close
K4.3b or K4.3c.  Every run has an internal wall-clock deadline.
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=50.0)
    parser.add_argument("--samples", type=int, default=1200)
    args = parser.parse_args()
    if not (0.0 < args.max_runtime_seconds <= 50.0):
        parser.error("--max-runtime-seconds must be in (0, 50]")
    if not (300 <= args.samples <= 4000):
        parser.error("--samples must be in [300, 4000]")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("internal CAMB recombination reference deadline exceeded")

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
    deadline()
    results = camb.get_background(pars)
    deadline()

    positive_z = np.geomspace(1.0e7, 1.0e-4, args.samples)
    redshift = np.concatenate([positive_z, np.array([0.0])])
    eta = np.asarray(results.conformal_time(redshift), dtype=float)
    thermal = results.get_background_redshift_evolution(
        redshift,
        vars=["x_e", "opacity", "visibility", "cs2b", "T_b"],
        format="dict",
    )
    deadline()

    x_e = np.asarray(thermal["x_e"], dtype=float)
    opacity = np.asarray(thermal["opacity"], dtype=float)
    visibility = np.asarray(thermal["visibility"], dtype=float)
    cs2b = np.asarray(thermal["cs2b"], dtype=float)
    t_b = np.asarray(thermal["T_b"], dtype=float)
    peak_index = int(np.argmax(visibility))
    z_peak = float(redshift[peak_index])
    visibility_integral = float(np.trapezoid(visibility, x=eta))

    hz = np.asarray(results.hubble_parameter(redshift), dtype=float)
    hconf = hz / (1.0 + redshift) / C_KM_S
    tau_c = np.full_like(opacity, np.inf)
    positive_opacity = opacity > 0.0
    tau_c[positive_opacity] = 1.0 / opacity[positive_opacity]
    k_reference = 0.2  # Mpc^-1, interface diagnostic only
    epsilon_tca = np.maximum(k_reference * tau_c, hconf * tau_c)
    early_index = int(np.argmin(np.abs(np.log1p(redshift) - math.log1p(1.0e6))))
    early_epsilon = float(epsilon_tca[early_index])
    switch_candidates = np.flatnonzero(epsilon_tca >= 0.1)
    switch_z = float(redshift[int(switch_candidates[0])]) if len(switch_candidates) else None

    arrays = [eta, x_e, opacity, visibility, cs2b, t_b, hz]
    checks = {
        "all_reference_arrays_finite": bool(all(np.all(np.isfinite(a)) for a in arrays)),
        "ionization_fraction_nonnegative_and_helium_bounded": bool(np.min(x_e) >= 0.0 and np.max(x_e) < 1.5),
        "opacity_and_visibility_nonnegative": bool(np.min(opacity) >= 0.0 and np.min(visibility) >= 0.0),
        "visibility_peak_in_recombination_window": bool(800.0 < z_peak < 1400.0),
        "visibility_normalization_controlled": bool(0.95 < visibility_integral < 1.05),
        "early_tight_coupling_for_k_0p2_Mpc": bool(early_epsilon < 1.0e-2),
        "finite_tight_coupling_switch_exists": bool(switch_z is not None and 100.0 < switch_z < 5000.0),
        "baryon_temperature_and_sound_speed_physical": bool(np.min(t_b) > 0.0 and np.min(cs2b) >= 0.0),
    }
    passed = all(checks.values())
    output = {
        "test": "A2-K4.3b unmodified CAMB recombination and tight-coupling interface reference",
        "scope": (
            "Null atomic/recombination reference only. The exact A1-K1/K4 "
            "background and perturbations are not implemented in CAMB here."
        ),
        "CAMB_version": camb.__version__,
        "inputs": {
            "H0_km_s_Mpc": 100.0 * h,
            "Omega_m0": omega_m0,
            "ombh2": ombh2,
            "omch2": omch2,
            "Neff": 3.046 + 0.0535,
            "w_constant_surrogate": -1.0 + 0.02297,
            "tau_reionization": 0.054,
            "samples": args.samples,
        },
        "diagnostics": {
            "z_visibility_peak": z_peak,
            "visibility_integral_deta": visibility_integral,
            "x_e_min": float(np.min(x_e)),
            "x_e_max": float(np.max(x_e)),
            "opacity_max_per_Mpc": float(np.max(opacity)),
            "early_z_for_epsilon": float(redshift[early_index]),
            "early_TCA_epsilon_k_0p2_Mpc": early_epsilon,
            "first_z_descending_with_epsilon_ge_0p1": switch_z,
        },
        "checks": checks,
        "execution_verdict": "PASS_NULL_RECOMBINATION_INTERFACE_REFERENCE" if passed else "REFERENCE_REQUIRES_REVIEW",
        "K4_3b_gate_verdict": "NEUZAVRETA_EXACT_K4_BACKGROUND_BACKEND_STILL_REQUIRED",
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

