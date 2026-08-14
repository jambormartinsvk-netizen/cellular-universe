#!/usr/bin/env python
"""Bounded first projected ODE smoke test for K7c.3 NID/deep."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import subprocess
import sys
import time

import numpy as np
from scipy.integrate import solve_ivp


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "178_script_A2_K4_C7_7c_K7c2_high_precision_seed_handoff.py"
NAMES = (
    "h", "eta", "delta_gamma", "D", "delta_b", "delta_c",
    "U_gamma", "M", "sigma_fs", "L3_fs", "L4_fs", "delta_f", "U_f",
)


def parse_json(text: str) -> dict[str, object]:
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        raise RuntimeError("seed source returned no JSON")
    return json.loads(text[start:end + 1])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, required=True)
    parser.add_argument("--source-runtime-seconds", type=float, default=15.0)
    parser.add_argument("--source-child-runtime-seconds", type=float, default=6.0)
    args = parser.parse_args()
    if not 12 <= args.max_runtime_seconds <= 25:
        parser.error("max-runtime-seconds must be in [12,25]")
    if not 10 <= args.source_runtime_seconds <= 18:
        parser.error("source-runtime-seconds must be in [10,18]")
    if not 5 <= args.source_child_runtime_seconds <= 8:
        parser.error("source-child-runtime-seconds must be in [5,8]")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("K7c.3 total deadline exceeded")

    child = subprocess.run(
        [sys.executable, str(SOURCE),
         "--max-runtime-seconds", str(args.source_runtime_seconds),
         "--child-runtime-seconds", str(args.source_child_runtime_seconds)],
        capture_output=True, text=True,
        timeout=args.source_runtime_seconds + 1, check=False,
    )
    source = parse_json(child.stdout)
    deadline()
    source_results = dict(source.get("results", {}))
    deep_seed = dict(dict(source_results["NID_deep"])["projected_seed_float64"])
    shallow_seed = dict(dict(source_results["NID_shallow"])["projected_seed_float64"])
    if tuple(deep_seed) != NAMES or tuple(shallow_seed) != NAMES:
        raise RuntimeError("K7c.2 seed names changed")
    y0 = np.asarray([float(deep_seed[name]) for name in NAMES], float)
    envelope = np.asarray([float(shallow_seed[name]) for name in NAMES], float)
    scale = np.maximum(np.maximum(np.abs(y0), np.abs(envelope)), 1e-300)
    w0 = y0 / scale

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

    def background(x: float) -> dict[str, float]:
        z = k_mpc * math.exp(x) / (hubble0_mpc * math.sqrt(omega_r0))
        fuel_piece = z**p
        denominator = 1 + mu * z + fuel_piece * (1 + transfer_shape * z**2)
        denominator_x = mu * z + fuel_piece * (p + (p + 2) * transfer_shape * z**2)
        ell = denominator_x / denominator
        s2 = z**2 / denominator
        Og, On = rg / denominator, rn / denominator
        Ob = fb * mu * z / denominator
        Oc = (fc * mu * z + g2 * z**(p + 2) / (p + 1)) / denominator
        Of = fuel_piece * (1 - g2 * z**2 / 2) / denominator
        loading = 3 * fb * mu * z / (4 * rg)
        inv1r = 1 / (1 + loading)
        g = g2 * z**2
        gr = g2 / (fc * mu) * z**(p + 1)
        c_numerator = fc * mu * z + g2 * z**(p + 2) / (p + 1)
        beta_c = (fc * mu * z + (p + 2) * g2 * z**(p + 2) / (p + 1)) / c_numerator
        beta_f = p - g / (1 - g / 2)
        return {
            "z": z, "ell": ell, "q": -1 + ell / 2, "s2": s2,
            "Og": Og, "On": On, "Ob": Ob, "Oc": Oc, "Of": Of,
            "load_fraction": loading * inv1r, "inv1r": inv1r,
            "g": g, "gr": gr, "beta_c": beta_c, "beta_f": beta_f,
        }

    rhs_calls = 0
    maximum_normalized_abs = float(np.max(np.abs(w0)))

    def physical_rhs(x: float, state: np.ndarray) -> np.ndarray:
        nonlocal rhs_calls, maximum_normalized_abs
        rhs_calls += 1
        if rhs_calls > 200000:
            raise TimeoutError("K7c.3 RHS call cap exceeded")
        if rhs_calls % 64 == 0:
            deadline()
        if not np.all(np.isfinite(state)):
            raise FloatingPointError("non-finite projected state")
        maximum_normalized_abs = max(
            maximum_normalized_abs, float(np.max(np.abs(state / scale)))
        )
        if maximum_normalized_abs > 1e8:
            raise FloatingPointError("K7c.3 normalized safety cap exceeded")

        h, eta, dg, D, db, dc, Ug, M, sig, L3, L4, df, Uf = state
        b = background(x)
        Og, On, Ob, Oc, Of = b["Og"], b["On"], b["Ob"], b["Oc"], b["Of"]
        Wg, Wf = 2 * Og + 1.5 * Ob, 1.5 * delta * Of
        dn = (D - Og * dg - Ob * db - Oc * dc - Of * df) / On
        Un = (M - Wg * Ug - Wf * Uf) / (2 * On)
        hx = 3 * D + 2 * b["s2"] * eta
        Ah = 2 / 3 * (Og + On) + 0.5 * (Ob + Oc) + 0.5 * delta * Of
        return np.asarray([
            hx,
            M,
            -4 / 3 * b["s2"] * Ug - 2 / 3 * hx,
            -b["ell"] * D + Ob * db + b["beta_c"] * Oc * dc
                + b["beta_f"] * Of * df - 2 / 3 * b["s2"] * M - Ah * hx
                + Oc * b["gr"] * (df - dc)
                + Of * (-3 * (2 - delta) * df - 9 * delta * (2 - delta) * Uf
                        - 3 * (2 - delta) * b["g"] * Uf),
            -b["s2"] * Ug - hx / 2,
            -hx / 2 + b["gr"] * (df - dc),
            b["q"] * Ug - b["load_fraction"] * Ug + 0.25 * b["inv1r"] * dg,
            (-b["q"] - 2) * M + D / 2
                + (1.5 * Ob - Wg * b["load_fraction"]) * Ug
                + (0.25 * Wg * b["inv1r"] - 0.5 * Og) * dg
                - 0.5 * Ob * db - 0.5 * Oc * dc + Of * df - 2 * On * sig
                + (1.5 * delta * Of * (b["beta_f"] + 2) + 3 * Of * b["g"]) * Uf,
            2 / 15 * hx + 4 / 5 * M + 4 / 15 * b["s2"] * Un - 3 / 10 * L3,
            -b["q"] * L3 + 6 / 7 * b["s2"] * sig - 4 / 7 * L4,
            -2 * b["q"] * L4 + 4 / 9 * b["s2"] * L3,
            -3 * (2 - delta) * df - delta * b["s2"] * Uf - delta * hx / 2
                - 9 * delta * (2 - delta) * Uf - 3 * (2 - delta) * b["g"] * Uf,
            (b["q"] + 2) * Uf + df / delta + 2 * b["g"] * Uf / delta,
        ], float)

    def scaled_rhs(x: float, normalized: np.ndarray) -> np.ndarray:
        return physical_rhs(x, normalized * scale) / scale

    x_start, x_final = -25.0, -24.75
    checkpoints_x = np.asarray([x_start, (x_start + x_final) / 2, x_final])
    solution = solve_ivp(
        scaled_rhs, (x_start, x_final), w0, method="DOP853",
        t_eval=checkpoints_x, rtol=1e-10, atol=1e-12, max_step=0.02,
    )
    deadline()
    physical_checkpoints = solution.y.T * scale if solution.y.size else np.empty((0, 13))
    checkpoint_output = []
    max_density_scaled = 0.0
    max_momentum_scaled = 0.0
    all_checkpoint_finite = True
    for x, state in zip(solution.t, physical_checkpoints):
        b = background(float(x))
        rhs = physical_rhs(float(x), state)
        h, eta, dg, D, db, dc, Ug, M, sig, L3, L4, df, Uf = state
        Og, On, Ob, Oc, Of = b["Og"], b["On"], b["Ob"], b["Oc"], b["Of"]
        Wg, Wf = 2 * Og + 1.5 * Ob, 1.5 * delta * Of
        dn = (D - Og * dg - Ob * db - Oc * dc - Of * df) / On
        Un = (M - Wg * Ug - Wf * Uf) / (2 * On)
        density_terms = np.asarray([Og * dg, On * dn, Ob * db, Oc * dc, Of * df])
        momentum_terms = np.asarray([Wg * Ug, 2 * On * Un, Wf * Uf])
        density_scaled = abs(float(np.sum(density_terms)) - D) / max(
            float(np.sum(np.abs(density_terms))), abs(D), 1e-300
        )
        momentum_scaled = abs(float(np.sum(momentum_terms)) - M) / max(
            float(np.sum(np.abs(momentum_terms))), abs(M), 1e-300
        )
        max_density_scaled = max(max_density_scaled, density_scaled)
        max_momentum_scaled = max(max_momentum_scaled, momentum_scaled)
        finite = bool(np.all(np.isfinite(state)) and np.all(np.isfinite(rhs))
                      and math.isfinite(dn) and math.isfinite(Un))
        all_checkpoint_finite = all_checkpoint_finite and finite
        checkpoint_output.append({
            "x": float(x), "state": dict(zip(NAMES, map(float, state))),
            "rhs": dict(zip(NAMES, map(float, rhs))),
            "reconstructed_delta_fs": float(dn), "reconstructed_U_fs": float(Un),
            "Omega_fs": On, "density_constraint_scaled_residual": density_scaled,
            "momentum_constraint_scaled_residual": momentum_scaled,
            "metric_h_identity_residual": abs(rhs[0] - (3 * D + 2 * b["s2"] * eta)),
            "metric_eta_identity_residual": abs(rhs[1] - M), "finite": finite,
        })

    reached_final = bool(solution.t.size and abs(solution.t[-1] - x_final) < 1e-10)
    normalized_change = (
        float(np.max(np.abs(solution.y[:, -1] - w0))) if solution.y.size else math.inf
    )
    checks = {
        "source_exit_zero": child.returncode == 0,
        "source_seed_handoff_pass": source.get("execution_verdict") ==
            "PASS_C7_7C_K7C2_HIGH_PRECISION_SEED_HANDOFF",
        "source_names_exact": tuple(source.get("projected_state_names", ())) == NAMES,
        "solver_success": bool(solution.success),
        "reached_x_final": reached_final,
        "all_three_checkpoints_written": len(checkpoint_output) == 3,
        "checkpoint_states_rhs_and_reconstruction_finite": all_checkpoint_finite,
        "rhs_call_cap_respected": rhs_calls <= 200000,
        "normalized_safety_cap_respected": maximum_normalized_abs < 1e8,
        "nontrivial_normalized_change_above_1e-12": normalized_change > 1e-12,
        "density_constraint_scaled_below_5e-12": max_density_scaled < 5e-12,
        "momentum_constraint_scaled_below_5e-12": max_momentum_scaled < 5e-12,
        "nfev_consistent_with_rhs_counter": rhs_calls >= int(solution.nfev),
    }
    passed = bool(checks) and all(checks.values())
    output = {
        "test": "A2-K4 C7.7c-K7c.3 NID/deep short projected ODE smoke test",
        "profile_request": {"mode": "NID", "surface": "deep",
                            "x_start": x_start, "x_final": x_final},
        "state_names": list(NAMES), "integration_scale": dict(zip(NAMES, map(float, scale))),
        "solver": {"method": "DOP853", "rtol": 1e-10, "normalized_atol": 1e-12,
                   "max_step": 0.02, "L5_closure": "L5=0 bounded closure"},
        "results": {"solver_message": solution.message, "nfev": int(solution.nfev),
                    "rhs_calls_including_audit": rhs_calls,
                    "maximum_normalized_abs": maximum_normalized_abs,
                    "max_normalized_checkpoint_change": normalized_change,
                    "max_density_constraint_scaled_residual": max_density_scaled,
                    "max_momentum_constraint_scaled_residual": max_momentum_scaled,
                    "checkpoints": checkpoint_output},
        "checks": checks,
        "execution_verdict": (
            "PASS_C7_7C_K7C3_NID_DEEP_SHORT_PROJECTED_ODE"
            if passed else "REVIEW_C7_7C_K7C3_NID_DEEP_ODE_UNCLOSED"
        ),
        "physical_verdict": (
            "first short projected ODE segment passed; no four-surface or hierarchy claim"
            if passed else "no death verdict; audit first failed numerical/constraint gate"
        ),
        "fine_depth": "66.5/100",
        "scope_limit": "0.25 e-fold NID/deep smoke test; no convergence, endpoint agreement, or full hierarchy",
        "runtime_limits_seconds": {"total": args.max_runtime_seconds,
                                   "seed_source": args.source_runtime_seconds,
                                   "seed_source_children": args.source_child_runtime_seconds,
                                   "rhs_calls": 200000},
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
