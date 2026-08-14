#!/usr/bin/env python
"""A2-K4.3b-RG CAMB five-mode audit using precompiled outputs only.

Script 78 correctly fixed CAMB's zero-placeholder start, but requesting the
symbolic pi_r source requires a local Fortran compiler that is unavailable.
This alias keeps the corrected active-start logic and asks only for variables
already exposed by the frozen CAMB binary.  It does not replace the exact
neutrino-hierarchy coefficient audit in scripts 76.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path
import sys
import time

import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
LOCAL_DEPS = ROOT / ".deps" / "python"
if LOCAL_DEPS.exists():
    sys.path.insert(0, str(LOCAL_DEPS))

import camb  # noqa: E402


def load_fixed_definitions():
    path = HERE / "78_script_A2_K4_3b_RG_collective_CAMB_regular_seed_active_start_fixed.py"
    spec = importlib.util.spec_from_file_location("k4_rg78_defs", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


D = load_fixed_definitions()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=45.0)
    parser.add_argument("--k-mpc", type=float, default=0.05)
    parser.add_argument("--y-min", type=float, default=2.0e-4)
    parser.add_argument("--depths", type=int, default=8)
    args = parser.parse_args()
    if not (0.0 < args.max_runtime_seconds <= 50.0):
        parser.error("--max-runtime-seconds must be in (0, 50]")
    if not (1.0e-4 <= args.k_mpc <= 0.2):
        parser.error("--k-mpc must be in [1e-4, 0.2] Mpc^-1")
    if not (1.0e-5 <= args.y_min <= 2.0e-3):
        parser.error("--y-min must be in [1e-5, 2e-3]")
    if not (6 <= args.depths <= 10):
        parser.error("--depths must be in [6, 10]")

    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("internal K4.3b-RG precompiled CAMB deadline exceeded")

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

    raw: dict[str, np.ndarray] = {}
    first_active: dict[str, int] = {}
    for mode in D.MODES:
        data.Params.scalar_initial_condition = mode
        values = np.asarray(
            data.get_time_evolution(
                args.k_mpc,
                eta,
                vars=list(D.BASE_VARS),
                lAccuracyBoost=4,
            ),
            dtype=float,
        )
        deadline()
        if values.shape != (args.depths, len(D.BASE_VARS)):
            raise RuntimeError(f"unexpected CAMB shape for {mode}: {values.shape}")
        active = np.flatnonzero(np.max(np.abs(values), axis=1) > 1.0e-30)
        if len(active) == 0:
            raise RuntimeError(f"CAMB returned no active row for {mode}")
        raw[mode] = values
        first_active[mode] = int(active[0])

    common_index = max(first_active.values())
    if common_index + 1 >= args.depths:
        raise RuntimeError("fewer than two common active depths")

    checks: dict[str, bool] = {}
    rows: dict[str, object] = {}
    descriptors: list[np.ndarray] = []
    descriptor_indices = {name: i for i, name in enumerate(D.DESCRIPTOR_NAMES)}
    for mode in D.MODES:
        values = raw[mode]
        by_name = {name: values[:, i] for i, name in enumerate(D.BASE_VARS)}
        s_cg = by_name["delta_cdm"] - 0.75 * by_name["delta_photon"]
        s_bg = by_name["delta_baryon"] - 0.75 * by_name["delta_photon"]
        s_rg = 0.75 * (by_name["delta_neutrino"] - by_name["delta_photon"])
        v_rg = by_name["v_neutrino"] - by_name["v_photon"]
        weyl = by_name["Weyl"]
        invariant = np.column_stack([s_cg, s_bg, s_rg, v_rg, weyl])

        prefix = values[: first_active[mode]]
        checks[f"{mode}_zero_placeholder_prefix_identified"] = bool(
            prefix.size == 0 or np.max(np.abs(prefix)) == 0.0
        )
        checks[f"{mode}_active_values_finite"] = bool(
            np.all(np.isfinite(values[first_active[mode] :]))
        )
        descriptor = invariant[common_index]
        norm = float(np.linalg.norm(descriptor))
        if norm <= 0.0 or not np.isfinite(norm):
            raise RuntimeError(f"zero/nonfinite descriptor for {mode}")
        normalized = descriptor / norm
        descriptors.append(normalized)
        dominant_index = int(np.argmax(np.abs(normalized)))
        expected_index = descriptor_indices[D.EXPECTED_DOMINANT[mode]]
        checks[f"{mode}_expected_invariant_signature"] = dominant_index == expected_index
        checks[f"{mode}_bounded_active_invariants"] = bool(
            np.max(np.abs(invariant[common_index:])) < 1.0e6
        )

        i0, i1 = common_index, common_index + 1
        slopes = {
            name: D.log_slope(
                float(series[i0]), float(series[i1]), float(y[i0]), float(y[i1])
            )
            for name, series in (
                ("S_c_gamma", s_cg),
                ("S_b_gamma", s_bg),
                ("S_nu_gamma", s_rg),
                ("V_nu_gamma", v_rg),
                ("Weyl", weyl),
                ("pi_photon", by_name["pi_photon"]),
            )
        }
        rows[mode] = {
            "first_active_index": first_active[mode],
            "first_active_k_tau": float(y[first_active[mode]]),
            "common_active_descriptor": descriptor.tolist(),
            "common_active_descriptor_normalized": normalized.tolist(),
            "dominant_invariant": D.DESCRIPTOR_NAMES[dominant_index],
            "two_common_depth_log_slopes": slopes,
        }

    matrix = np.column_stack(descriptors)
    singular_values = np.linalg.svd(matrix, compute_uv=False)
    rank = int(np.linalg.matrix_rank(matrix, tol=1.0e-7))
    checks["five_collective_seed_signatures_independent"] = rank == 5
    checks["common_active_depth_is_superhorizon"] = bool(y[common_index] < 1.0e-2)
    checks["zero_placeholders_not_used_as_physical_seeds"] = bool(common_index > 0)
    passed = all(checks.values())

    output = {
        "test": "A2-K4.3b-RG precompiled-only five-mode CAMB seed audit",
        "supersession_ledger": {
            "script_77": "active-start bug; preserved",
            "script_78": "active-start fixed but symbolic pi_r requires absent Fortran compiler; preserved",
            "script_79": "active-start fixed, precompiled CAMB variables only",
        },
        "scope": (
            "Gamma=0 collective seed reference. pi_neutrino is intentionally "
            "not fabricated; exact hierarchy coefficients remain in script 76."
        ),
        "CAMB_version": camb.__version__,
        "inputs": {
            "k_Mpc_inverse": args.k_mpc,
            "k_tau_depths": y.tolist(),
            "H0_km_s_Mpc": 100.0 * h,
            "Neff": 3.046 + 0.0535,
        },
        "first_active_index_by_mode": first_active,
        "common_active_index": common_index,
        "common_active_k_tau": float(y[common_index]),
        "descriptor_order": list(D.DESCRIPTOR_NAMES),
        "mode_results": rows,
        "descriptor_singular_values": singular_values.tolist(),
        "descriptor_numerical_rank": rank,
        "checks": checks,
        "execution_verdict": "PASS_NULL_COLLECTIVE_ACTIVE_SEEDS" if passed else "REVIEW_REQUIRED",
        "K4_3b_RG_verdict": "NEUZAVRETA_INTERNAL_MODES_AND_K4_CORRECTIONS_MISSING",
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
