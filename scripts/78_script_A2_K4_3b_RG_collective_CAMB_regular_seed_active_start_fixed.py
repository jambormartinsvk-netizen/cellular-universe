#!/usr/bin/env python
"""A2-K4.3b-RG corrected CAMB five-mode seed audit.

Script 77 sampled rows before CAMB's internal perturbation start and therefore
treated zero placeholders as physical seeds.  This superseding audit detects
the contiguous zero-placeholder prefix, chooses one common active depth for
all five modes, and includes the collisionless-neutrino anisotropic stress via
CAMB's symbolic interface.

Scope remains the Gamma=0 reference.  Passing this script is necessary but
not sufficient for the interacting K4 G7 gate.
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
import camb.symbolic as cs  # noqa: E402


MODES = (
    "initial_adiabatic",
    "initial_iso_CDM",
    "initial_iso_baryon",
    "initial_iso_neutrino",
    "initial_iso_neutrino_vel",
)
BASE_VARS = (
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
DESCRIPTOR_NAMES = (
    "S_c_gamma",
    "S_b_gamma",
    "S_nu_gamma",
    "V_nu_gamma",
    "Weyl",
)
EXPECTED_DOMINANT = {
    "initial_adiabatic": "Weyl",
    "initial_iso_CDM": "S_c_gamma",
    "initial_iso_baryon": "S_b_gamma",
    "initial_iso_neutrino": "S_nu_gamma",
    "initial_iso_neutrino_vel": "V_nu_gamma",
}


def log_slope(v0: float, v1: float, y0: float, y1: float) -> float | None:
    if not np.isfinite(v0) or not np.isfinite(v1):
        return None
    if min(abs(v0), abs(v1)) < 1.0e-28:
        return None
    return float(math.log(abs(v1 / v0)) / math.log(y1 / y0))


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
            raise TimeoutError("internal K4.3b-RG corrected seed deadline exceeded")

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
    vars_requested = list(BASE_VARS) + [cs.pi_r]
    for mode in MODES:
        data.Params.scalar_initial_condition = mode
        values = np.asarray(
            data.get_time_evolution(
                args.k_mpc,
                eta,
                vars=vars_requested,
                lAccuracyBoost=4,
                frame="CDM",
            ),
            dtype=float,
        )
        deadline()
        if values.shape != (args.depths, len(vars_requested)):
            raise RuntimeError(f"unexpected CAMB shape for {mode}: {values.shape}")
        active = np.flatnonzero(np.max(np.abs(values), axis=1) > 1.0e-30)
        if len(active) == 0:
            raise RuntimeError(f"CAMB returned no active perturbation row for {mode}")
        raw[mode] = values
        first_active[mode] = int(active[0])

    common_index = max(first_active.values())
    if common_index + 1 >= args.depths:
        raise RuntimeError("fewer than two common active CAMB depths")

    checks: dict[str, bool] = {}
    rows: dict[str, object] = {}
    descriptors: list[np.ndarray] = []
    expected_indices = {name: i for i, name in enumerate(DESCRIPTOR_NAMES)}
    for mode in MODES:
        values = raw[mode]
        by_name = {name: values[:, i] for i, name in enumerate(BASE_VARS)}
        pi_neutrino = values[:, -1]
        s_cg = by_name["delta_cdm"] - 0.75 * by_name["delta_photon"]
        s_bg = by_name["delta_baryon"] - 0.75 * by_name["delta_photon"]
        s_rg = 0.75 * (by_name["delta_neutrino"] - by_name["delta_photon"])
        v_rg = by_name["v_neutrino"] - by_name["v_photon"]
        weyl = by_name["Weyl"]
        invariant = np.column_stack([s_cg, s_bg, s_rg, v_rg, weyl])

        prefix = values[: first_active[mode]]
        checks[f"{mode}_placeholder_prefix_exactly_zero"] = bool(
            prefix.size == 0 or np.max(np.abs(prefix)) == 0.0
        )
        checks[f"{mode}_all_active_values_finite"] = bool(
            np.all(np.isfinite(values[first_active[mode] :]))
        )
        descriptor = invariant[common_index]
        norm = float(np.linalg.norm(descriptor))
        if norm <= 0.0 or not np.isfinite(norm):
            raise RuntimeError(f"zero/nonfinite descriptor for {mode}")
        normalized = descriptor / norm
        descriptors.append(normalized)
        dominant_index = int(np.argmax(np.abs(normalized)))
        expected_index = expected_indices[EXPECTED_DOMINANT[mode]]
        checks[f"{mode}_expected_invariant_signature"] = dominant_index == expected_index

        active_norms = np.linalg.norm(invariant[common_index:, :4], axis=1)
        checks[f"{mode}_bounded_active_invariants"] = bool(
            np.all(np.isfinite(active_norms))
            and float(np.max(np.abs(invariant[common_index:]))) < 1.0e6
        )
        i0, i1 = common_index, common_index + 1
        slopes = {
            name: log_slope(
                float(series[i0]), float(series[i1]), float(y[i0]), float(y[i1])
            )
            for name, series in (
                ("S_c_gamma", s_cg),
                ("S_b_gamma", s_bg),
                ("S_nu_gamma", s_rg),
                ("V_nu_gamma", v_rg),
                ("Weyl", weyl),
                ("pi_photon", by_name["pi_photon"]),
                ("pi_neutrino", pi_neutrino),
            )
        }
        rows[mode] = {
            "first_active_index": first_active[mode],
            "first_active_k_tau": float(y[first_active[mode]]),
            "common_active_descriptor": descriptor.tolist(),
            "common_active_descriptor_normalized": normalized.tolist(),
            "dominant_invariant": DESCRIPTOR_NAMES[dominant_index],
            "two_common_depth_log_slopes": slopes,
            "active_invariant_norms": active_norms.tolist(),
            "pi_neutrino_at_common_depth": float(pi_neutrino[common_index]),
        }

    descriptor_matrix = np.column_stack(descriptors)
    singular_values = np.linalg.svd(descriptor_matrix, compute_uv=False)
    rank = int(np.linalg.matrix_rank(descriptor_matrix, tol=1.0e-7))
    checks["five_collective_seed_signatures_independent"] = rank == 5
    checks["common_active_depth_is_superhorizon"] = bool(y[common_index] < 1.0e-2)
    checks["zero_placeholders_were_not_used_as_physical_data"] = bool(common_index > 0)
    passed = all(checks.values())

    output = {
        "test": "A2-K4.3b-RG corrected active-start five-mode CAMB seed audit",
        "supersedes_for_active_start_logic": "77_script_A2_K4_3b_RG_collective_CAMB_regular_seed_audit.py",
        "scope": (
            "Gamma=0 collective regular-seed reference only; two internal "
            "nu-steam modes and the O(lambda/E) K4 corrections are separate"
        ),
        "CAMB_version": camb.__version__,
        "inputs": {
            "k_Mpc_inverse": args.k_mpc,
            "k_tau_depths": y.tolist(),
            "H0_km_s_Mpc": 100.0 * h,
            "Neff": 3.046 + 0.0535,
        },
        "CAMB_zero_placeholder_rows_by_mode": first_active,
        "common_active_index": common_index,
        "common_active_k_tau": float(y[common_index]),
        "descriptor_order": list(DESCRIPTOR_NAMES),
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
