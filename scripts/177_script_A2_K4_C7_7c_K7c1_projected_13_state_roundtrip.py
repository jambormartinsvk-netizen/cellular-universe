#!/usr/bin/env python
"""Bounded K7c.1 certificate for the projected 13-component state.

The test uses the four authoritative physical states exported by script 174,
replaces delta_fs/U_fs by D/M, and verifies the inverse map. No ODE is run.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import time

import numpy as np


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "174_script_A2_K4_C7_7c_K7b3b1_slice_and_physical_mu_export.py"
SPECIES_NAMES = (
    "h", "eta", "delta_gamma", "delta_fs", "delta_b", "delta_c",
    "U_gamma", "U_fs", "sigma_fs", "L3_fs", "L4_fs", "delta_f", "U_f",
)
PROJECTED_NAMES = (
    "h", "eta", "delta_gamma", "D", "delta_b", "delta_c",
    "U_gamma", "M", "sigma_fs", "L3_fs", "L4_fs", "delta_f", "U_f",
)


def parse_json(text: str) -> dict[str, object]:
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        raise RuntimeError("source exporter returned no JSON")
    return json.loads(text[start:end + 1])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, required=True)
    parser.add_argument("--source-runtime-seconds", type=float, default=8.0)
    args = parser.parse_args()
    if not 4 <= args.max_runtime_seconds <= 15:
        parser.error("max-runtime-seconds must be in [4,15]")
    if not 2 <= args.source_runtime_seconds <= 8:
        parser.error("source-runtime-seconds must be in [2,8]")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("K7c.1 round-trip deadline exceeded")

    command = [
        sys.executable, str(SOURCE),
        "--max-runtime-seconds", str(args.source_runtime_seconds),
        "--standard-order", "6", "--x-deep", "-25", "--x-shallow", "-23",
        "--x-reference", "-18", "--k-mpc", "0.05",
        "--fuel-fraction-coefficient", "1", "--hp-mode", "NID",
    ]
    child = subprocess.run(command, capture_output=True, text=True,
                           timeout=args.source_runtime_seconds + 1, check=False)
    source = parse_json(child.stdout)
    deadline()

    checks: dict[str, bool] = {
        "source_exit_zero": child.returncode == 0,
        "source_export_pass": source.get("execution_verdict") ==
            "PASS_C7_7C_K4_ANALYTIC_REFERENCE_STATE",
        "source_all_checks_true": bool(source.get("checks")) and
            all(bool(value) for value in dict(source.get("checks", {})).values()),
        "species_names_exact_13_unique": len(SPECIES_NAMES) == 13 and
            len(set(SPECIES_NAMES)) == 13,
        "projected_names_exact_13_unique": len(PROJECTED_NAMES) == 13 and
            len(set(PROJECTED_NAMES)) == 13,
    }
    results: dict[str, object] = {}
    surfaces = dict(source.get("BR3C_state_surfaces", {}))
    delta = 0.02297

    for mode in ("NID", "NIV"):
        mode_surfaces = dict(dict(surfaces.get(mode, {})).get("surfaces", {}))
        for surface in ("deep", "shallow"):
            item = dict(mode_surfaces.get(surface, {}))
            state = dict(item.get("state", {}))
            omegas = dict(item.get("omegas", {}))
            key = f"{mode}_{surface}"
            y = np.asarray([float(state[name]) for name in SPECIES_NAMES], float)
            Og = float(omegas["Omega_gamma"])
            On = float(omegas["Omega_fs"])
            Ob = float(omegas["Omega_b"])
            Oc = float(omegas["Omega_c"])
            Of = float(omegas["Omega_f"])
            Wg = 2 * Og + 1.5 * Ob
            Wf = 1.5 * delta * Of

            transform = np.eye(13)
            transform[3, :] = 0
            transform[3, [2, 3, 4, 5, 11]] = [Og, On, Ob, Oc, Of]
            transform[7, :] = 0
            transform[7, [6, 7, 12]] = [Wg, 2 * On, Wf]
            projected = transform @ y
            recovered = np.linalg.solve(transform, projected)
            determinant = float(np.linalg.det(transform))
            expected_abs_determinant = 2 * On**2
            determinant_relative_error = abs(
                abs(determinant) - expected_abs_determinant
            ) / expected_abs_determinant
            component_scaled = np.abs(recovered - y) / np.maximum(1, np.abs(y))
            roundtrip = float(np.max(component_scaled))
            delta_fs_error = float(abs(recovered[3] - y[3]) / max(1, abs(y[3])))
            U_fs_error = float(abs(recovered[7] - y[7]) / max(1, abs(y[7])))
            rank = int(np.linalg.matrix_rank(transform))
            condition = float(np.linalg.cond(transform, 2))

            checks[f"{key}_Omega_fs_positive"] = On > 0
            checks[f"{key}_rank_13"] = rank == 13
            checks[f"{key}_determinant_formula_below_1e-13"] = (
                determinant_relative_error < 1e-13
            )
            checks[f"{key}_condition_below_10"] = condition < 10
            checks[f"{key}_roundtrip_below_5e-14"] = roundtrip < 5e-14
            checks[f"{key}_delta_fs_reconstruction_below_5e-14"] = (
                delta_fs_error < 5e-14
            )
            checks[f"{key}_U_fs_reconstruction_below_5e-14"] = U_fs_error < 5e-14
            results[key] = {
                "x": item.get("x"), "Omega_fs": On,
                "rank": rank, "determinant": determinant,
                "expected_abs_determinant": expected_abs_determinant,
                "determinant_relative_error": determinant_relative_error,
                "condition_2": condition,
                "max_component_scaled_roundtrip_error": roundtrip,
                "delta_fs_reconstruction_error": delta_fs_error,
                "U_fs_reconstruction_error": U_fs_error,
                "projected_D": float(projected[3]),
                "projected_M": float(projected[7]),
            }
            deadline()

    passed = bool(checks) and all(checks.values())
    output = {
        "test": "A2-K4 C7.7c-K7c.1 projected 13-state round-trip",
        "species_state_names": list(SPECIES_NAMES),
        "projected_state_names": list(PROJECTED_NAMES),
        "degree_of_freedom_statement":
            "D replaces delta_fs and M replaces U_fs; state dimension remains 13",
        "results": results, "checks": checks,
        "execution_verdict": (
            "PASS_C7_7C_K7C1_PROJECTED_13_STATE_ROUNDTRIP"
            if passed else "REVIEW_C7_7C_K7C1_REPRESENTATION_UNCLOSED"
        ),
        "physical_verdict": (
            "projected representation certified; no ODE claim"
            if passed else "no death verdict until first failed row is audited"
        ),
        "fine_depth": "66.5/100",
        "runtime_limits_seconds": {
            "total": args.max_runtime_seconds,
            "source": args.source_runtime_seconds,
        },
        "runtime_seconds": time.monotonic() - started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.TimeoutExpired as exc:
        print(json.dumps({"execution_verdict": "TIMEOUT_UNCLOSED",
                          "error": repr(exc)}, indent=2))
        raise SystemExit(124)
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict": "TIMEOUT_UNCLOSED",
                          "error": str(exc)}, indent=2))
        raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution_verdict": "ERROR_UNCLOSED",
                          "error": repr(exc)}, indent=2))
        raise SystemExit(1)
