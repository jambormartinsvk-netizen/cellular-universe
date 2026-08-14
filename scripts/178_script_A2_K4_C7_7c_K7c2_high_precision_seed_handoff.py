#!/usr/bin/env python
"""Bounded K7c.2 construction of ODE-ready projected seeds.

D and M are injected from the high-precision K7b metric seeds before the
13 values are converted to float64. They are never recomputed from rounded
species. No ODE is run.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import subprocess
import sys
import time


HERE = Path(__file__).resolve().parent
PROJECTED_NAMES = (
    "h", "eta", "delta_gamma", "D", "delta_b", "delta_c",
    "U_gamma", "M", "sigma_fs", "L3_fs", "L4_fs", "delta_f", "U_f",
)


def parse_json(text: str) -> dict[str, object]:
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        raise RuntimeError("child returned no JSON object")
    return json.loads(text[start:end + 1])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, required=True)
    parser.add_argument("--child-runtime-seconds", type=float, default=8.0)
    args = parser.parse_args()
    if not 10 <= args.max_runtime_seconds <= 25:
        parser.error("max-runtime-seconds must be in [10,25]")
    if not 5 <= args.child_runtime_seconds <= 9:
        parser.error("child-runtime-seconds must be in [5,9]")
    started = time.monotonic()

    delta = 0.02297
    p = 3.93109
    h0 = 0.6637
    omega_m0 = 0.3517
    ombh2 = 0.02237
    fb = ombh2 / (omega_m0 * h0**2)
    fc = 1 - fb
    neff = 3.046 + 0.0535
    rn = 0.2271 * neff / (1 + 0.2271 * neff)
    rg = 1 - rn
    omega_r0 = 2.47282e-5 * (1 + 0.2271 * neff) / h0**2
    hubble0_mpc = 100 * h0 / 299792.458
    k_mpc = 0.05
    mu = hubble0_mpc * omega_m0 / math.sqrt(omega_r0) / k_mpc
    g2 = 0.15 * (hubble0_mpc / k_mpc)**2 * math.sqrt(omega_r0)
    transfer_shape = g2 * (1 / (p + 1) - 0.5)

    profiles = (
        ("NID", "deep", "175_script_A2_K4_C7_7c_K7b3b1_physical_mu_constraint_gate.py",
         "PASS_C7_7C_K7B3B1_PHYSICAL_MU_CONSTRAINT_GATE"),
        ("NID", "shallow", "175_script_A2_K4_C7_7c_K7b3b1_physical_mu_constraint_gate.py",
         "PASS_C7_7C_K7B3B1_PHYSICAL_MU_CONSTRAINT_GATE"),
        ("NIV", "deep", "166_script_A2_K4_C7_7c_K7b1_high_precision_coefficient_constraint_audit.py",
         "PASS_C7_7C_K7B1_COEFFICIENT_CONSTRAINT_AUDIT"),
        ("NIV", "shallow", "166_script_A2_K4_C7_7c_K7b1_high_precision_coefficient_constraint_audit.py",
         "PASS_C7_7C_K7B1_COEFFICIENT_CONSTRAINT_AUDIT"),
    )
    checks: dict[str, bool] = {
        "projected_names_exact_13_unique": len(PROJECTED_NAMES) == 13 and
            len(set(PROJECTED_NAMES)) == 13,
    }
    results: dict[str, object] = {}

    for mode, surface, script, expected in profiles:
        elapsed = time.monotonic() - started
        if elapsed >= args.max_runtime_seconds:
            raise TimeoutError("K7c.2 deadline exceeded before next child")
        command = [
            sys.executable, str(HERE / script),
            "--max-runtime-seconds", str(args.child_runtime_seconds),
            "--source-runtime-seconds", "5", "--mode", mode,
            "--surface", surface, "--dps", "80",
        ]
        child = subprocess.run(
            command, capture_output=True, text=True,
            timeout=min(args.child_runtime_seconds + 1,
                        args.max_runtime_seconds - elapsed), check=False,
        )
        payload = parse_json(child.stdout)
        key = f"{mode}_{surface}"
        child_checks = dict(payload.get("checks", {}))
        comparison = dict(payload.get("state_comparison", {}))
        projected_seeds = dict(payload.get("projected_seeds", {}))

        def hp(name: str) -> float:
            return float(dict(comparison[name])["high_precision"])

        D = float(projected_seeds["D_metric"])
        M = float(projected_seeds["M_metric"])
        seed = {
            "h": hp("h"), "eta": hp("eta"),
            "delta_gamma": hp("delta_gamma"), "D": D,
            "delta_b": hp("delta_b"), "delta_c": hp("delta_c"),
            "U_gamma": hp("U_gamma"), "M": M,
            "sigma_fs": hp("sigma_fs"), "L3_fs": hp("L3_fs"),
            "L4_fs": hp("L4_fs"), "delta_f": hp("delta_f"), "U_f": hp("U_f"),
        }
        target_delta_fs = hp("delta_fs")
        target_U_fs = hp("U_fs")
        h_x = hp("h_x")
        eta_x = hp("eta_x")

        x = -25.0 if surface == "deep" else -23.0
        z = k_mpc * math.exp(x) / (hubble0_mpc * math.sqrt(omega_r0))
        fuel_piece = z**p
        denominator = 1 + mu * z + fuel_piece * (1 + transfer_shape * z**2)
        s2 = z**2 / denominator
        Og, On = rg / denominator, rn / denominator
        Ob = fb * mu * z / denominator
        Oc = (fc * mu * z + g2 * z**(p + 2) / (p + 1)) / denominator
        Of = fuel_piece * (1 - g2 * z**2 / 2) / denominator
        Wg, Wf = 2 * Og + 1.5 * Ob, 1.5 * delta * Of
        recovered_delta_fs = (
            D - Og * seed["delta_gamma"] - Ob * seed["delta_b"]
            - Oc * seed["delta_c"] - Of * seed["delta_f"]
        ) / On
        recovered_U_fs = (
            M - Wg * seed["U_gamma"] - Wf * seed["U_f"]
        ) / (2 * On)
        delta_fs_error = abs(recovered_delta_fs - target_delta_fs) / max(
            1, abs(target_delta_fs)
        )
        U_fs_error = abs(recovered_U_fs - target_U_fs) / max(1, abs(target_U_fs))
        h_constraint = 3 * D + 2 * s2 * seed["eta"]
        h_allowance = 5e-14 + 5e-10 * max(abs(h_x), abs(h_constraint))
        eta_allowance = 5e-14 + 5e-10 * max(abs(eta_x), abs(M))
        naive_D = (
            Og * seed["delta_gamma"] + On * target_delta_fs
            + Ob * seed["delta_b"] + Oc * seed["delta_c"] + Of * seed["delta_f"]
        )
        naive_M = Wg * seed["U_gamma"] + 2 * On * target_U_fs + Wf * seed["U_f"]

        checks[f"{key}_child_exit_zero"] = child.returncode == 0
        checks[f"{key}_child_expected_pass"] = payload.get("execution_verdict") == expected
        checks[f"{key}_child_all_checks_true"] = bool(child_checks) and all(
            bool(value) for value in child_checks.values()
        )
        checks[f"{key}_seed_names_exact"] = tuple(seed) == PROJECTED_NAMES
        checks[f"{key}_seed_all_finite"] = all(math.isfinite(value) for value in seed.values())
        checks[f"{key}_D_seed_from_HP_metric"] = seed["D"] == D
        checks[f"{key}_M_seed_from_HP_metric"] = seed["M"] == M
        checks[f"{key}_delta_fs_inverse_below_5e-14"] = delta_fs_error < 5e-14
        checks[f"{key}_U_fs_inverse_below_5e-14"] = U_fs_error < 5e-14
        checks[f"{key}_h_constraint_within_allowance"] = abs(h_constraint - h_x) < h_allowance
        checks[f"{key}_eta_constraint_within_allowance"] = abs(M - eta_x) < eta_allowance
        results[key] = {
            "source_script": script, "projected_seed_float64": seed,
            "recovered_delta_fs": recovered_delta_fs,
            "target_delta_fs": target_delta_fs,
            "delta_fs_scaled_error": delta_fs_error,
            "recovered_U_fs": recovered_U_fs, "target_U_fs": target_U_fs,
            "U_fs_scaled_error": U_fs_error,
            "h_constraint_absolute_residual": abs(h_constraint - h_x),
            "eta_constraint_absolute_residual": abs(M - eta_x),
            "naive_D_from_double_species_non_authoritative": naive_D,
            "naive_D_minus_HP_seed": naive_D - D,
            "naive_M_from_double_species_non_authoritative": naive_M,
            "naive_M_minus_HP_seed": naive_M - M,
        }

    passed = bool(checks) and all(checks.values())
    output = {
        "test": "A2-K4 C7.7c-K7c.2 high-precision projected seed handoff",
        "projected_state_names": list(PROJECTED_NAMES),
        "seed_rule": "inject HP D,M before float64 conversion; never recompute from rounded species",
        "results": results, "checks": checks,
        "execution_verdict": (
            "PASS_C7_7C_K7C2_HIGH_PRECISION_SEED_HANDOFF"
            if passed else "REVIEW_C7_7C_K7C2_SEED_HANDOFF_UNCLOSED"
        ),
        "physical_verdict": (
            "four ODE-ready projected seeds certified; no evolution claim"
            if passed else "no death verdict; audit first failed seed"
        ),
        "fine_depth": "66.5/100",
        "runtime_limits_seconds": {
            "total": args.max_runtime_seconds,
            "per_child": args.child_runtime_seconds,
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
