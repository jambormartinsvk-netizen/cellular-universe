"""Bounded S3 multipole-tail convergence screen on frozen K4 background."""

from __future__ import annotations

import math
import time

import numpy as np
from scipy.integrate import solve_ivp

from .s2_tca_direct import (EXPECTED_SOURCE_213_SHA256, SAFETY_CAP, SOURCE_213,
                             background_k4, sha256_file)


X_START, X_FINAL, CHI, RHS_CAP = -23.0, -22.0, 100.0, 100_000
FAMILIES = ("J", "E", "G")


def names(lmax: int) -> tuple[str, ...]:
    if lmax < 3:
        raise ValueError("lmax must be >=3")
    return tuple(f"{family}_{ell}" for family in FAMILIES for ell in range(2, lmax + 1))


def run_sweep(max_runtime_seconds: float) -> dict[str, object]:
    if not (0.0 < max_runtime_seconds <= 45.0):
        raise ValueError("max_runtime_seconds must be in (0,45]")
    started = time.monotonic()
    source_hash = sha256_file(SOURCE_213)
    if source_hash != EXPECTED_SOURCE_213_SHA256:
        raise RuntimeError("frozen K7d script 213 hash mismatch")

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError("G8 S3 hierarchy sweep internal deadline exceeded")

    results: dict[str, dict[str, object]] = {}
    for lmax in (8, 12, 16):
        rhs_calls = 0
        state_names = names(lmax)
        index = {name: i for i, name in enumerate(state_names)}
        grid = np.linspace(X_START, X_FINAL, 41)

        def value(y: np.ndarray, family: str, ell: int) -> float:
            return float(y[index[f"{family}_{ell}"]])

        def rhs(x: float, y: np.ndarray) -> np.ndarray:
            nonlocal rhs_calls
            rhs_calls += 1
            deadline()
            if rhs_calls > RHS_CAP:
                raise RuntimeError(f"S3 RHS cap exceeded at lmax={lmax}")
            if not (np.all(np.isfinite(y)) and np.max(np.abs(y)) <= SAFETY_CAP):
                raise FloatingPointError(f"S3 state unsafe at lmax={lmax}")
            b = background_k4(x)
            out = np.zeros_like(y)
            # The l=2 drives are normalized linear probes. They make tail
            # convergence measurable without claiming a full metric source.
            for family, drive in (("J", 2.0e-7), ("E", 0.0), ("G", 3.0e-7)):
                current = value(y, family, 2)
                following = value(y, family, 3)
                collision = -CHI * current if family in ("J", "E") else 0.0
                if family == "J":
                    polter = (2.0 / 15.0) * (0.75 * current + 4.5 * value(y, "E", 2))
                    collision += CHI * polter
                if family == "E":
                    polter = (2.0 / 15.0) * (0.75 * value(y, "J", 2) + 4.5 * current)
                    collision += CHI * polter
                out[index[f"{family}_2"]] = drive + collision - 3.0 / 5.0 * following
                for ell in range(3, lmax):
                    previous = value(y, family, ell - 1)
                    current_h = value(y, family, ell)
                    following_h = value(y, family, ell + 1)
                    coll = -CHI * current_h if family in ("J", "E") else 0.0
                    out[index[f"{family}_{ell}"]] = (-(ell - 2) * b["q"] * current_h
                        + ell / (2 * ell + 1) * b["z"] ** 2 * previous
                        - (ell + 1) / (2 * ell + 1) * following_h + coll)
                ell = lmax
                previous = value(y, family, ell - 1)
                current_h = value(y, family, ell)
                coll = -CHI * current_h if family in ("J", "E") else 0.0
                out[index[f"{family}_{ell}"]] = (-(ell - 2) * b["q"] * current_h
                    + ell / (2 * ell + 1) * b["z"] ** 2 * previous - (ell + 1) * current_h + coll)
            return out

        solution = solve_ivp(rhs, (X_START, X_FINAL), np.zeros(len(state_names)), method="Radau",
                             t_eval=grid, rtol=1e-10, atol=1e-16, max_step=0.02)
        deadline()
        if solution.y.shape != (len(state_names), len(grid)):
            raise RuntimeError(f"S3 unexpected shape at lmax={lmax}")
        final = {name: float(solution.y[i, -1]) for i, name in enumerate(state_names)}
        tail_ratios = {
            family: abs(final[f"{family}_{lmax}"]) / max(abs(final[f"{family}_2"]), 1e-300)
            for family in FAMILIES
        }
        results[str(lmax)] = {
            "dynamic_state_count": len(state_names), "state_names": list(state_names),
            "solver_success": bool(solution.success), "endpoint": float(solution.t[-1]),
            "nfev": int(solution.nfev), "rhs_calls": rhs_calls, "final_low_moments":
            {name: final[name] for name in ("J_2", "E_2", "G_2")},
            "tail_ratios": tail_ratios,
            "finite_under_cap": bool(np.all(np.isfinite(solution.y)) and np.max(np.abs(solution.y)) <= SAFETY_CAP),
        }

    def low_difference(left: str, right: str) -> float:
        values = []
        for name in ("J_2", "E_2", "G_2"):
            a = float(results[left]["final_low_moments"][name])
            b = float(results[right]["final_low_moments"][name])
            values.append(abs(a - b) / max(abs(b), 1e-300))
        return max(values)

    diff_8_12, diff_12_16 = low_difference("8", "12"), low_difference("12", "16")
    checks = {"frozen_K7d_source_hash_exact": source_hash == EXPECTED_SOURCE_213_SHA256,
              "all_lmax_solver_endpoint_success": all(bool(results[l]["solver_success"]) and abs(float(results[l]["endpoint"]) - X_FINAL) < 1e-14 for l in results),
              "all_lmax_finite_under_cap": all(bool(results[l]["finite_under_cap"]) for l in results),
              "all_lmax_rhs_under_cap": all(int(results[l]["rhs_calls"]) <= RHS_CAP for l in results),
              "tail_ratios_all_le_1e6_inverse": all(float(ratio) <= 1e-6 for l in results for ratio in results[l]["tail_ratios"].values()),
              "lmax_12_to_16_low_moment_diff_le_1e5_inverse": diff_12_16 <= 1e-5,
              "lmax_8_to_12_converges_or_improves_x4": diff_8_12 <= 5e-4 or (diff_12_16 > 0 and diff_8_12 / diff_12_16 >= 4.0)}
    passed = all(checks.values())
    return {"test": "A2-K4 C7.7c K7 G8 SCREEN-S3 frozen hierarchy tail/closure sweep",
            "scope": "three-family hierarchy-tail screen; not full Einstein-Boltzmann/recombination backend",
            "ode_executed": True, "score_effect": 0, "source_213_sha256": source_hash,
            "configuration": {"lmax": [8, 12, 16], "x_start": X_START, "x_final": X_FINAL,
                              "chi_test": CHI, "closure": "radiation_asymptotic_nonzero_damping", "rhs_cap_each": RHS_CAP},
            "results": results, "diagnostics": {"low_moment_diff_8_to_12": diff_8_12, "low_moment_diff_12_to_16": diff_12_16},
            "checks": checks, "verdict": "PASS_G8_SCREEN_S3_HIERARCHY_CONVERGENCE" if passed else "STOP_G8_CLOSURE_CONVERGENCE_REVIEW",
            "runtime_limit_seconds": max_runtime_seconds, "runtime_seconds": time.monotonic()-started}
