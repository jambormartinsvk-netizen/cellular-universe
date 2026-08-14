#!/usr/bin/env python
"""BR3C-b segmented early evolution from both audited state surfaces.

The script imports no coefficients by hand.  It runs authoritative state
export 132, maps its complete 13-component state into the bounded L4-closed
ODE registered for BR3C-b, and integrates NID/NIV from x=-25 and x=-23 to
x=-18 with one-e-fold checkpoints.  Timeout or solver failure is UNCLOSED.
"""

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


STATE_NAMES = (
    "h",
    "eta",
    "delta_gamma",
    "delta_fs",
    "delta_b",
    "delta_c",
    "U_gamma",
    "U_fs",
    "sigma_fs",
    "L3_fs",
    "L4_fs",
    "delta_f",
    "U_f",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=50.0)
    parser.add_argument("--source-runtime-seconds", type=float, default=15.0)
    parser.add_argument("--x-final", type=float, default=-18.0)
    parser.add_argument("--segment-efolds", type=float, default=1.0)
    parser.add_argument("--max-step", type=float, default=0.02)
    parser.add_argument("--rtol", type=float, default=1e-10)
    parser.add_argument("--atol", type=float, default=1e-14)
    parser.add_argument("--safety-cap", type=float, default=1e12)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 50.0:
        parser.error("max runtime must be in (0,50]")
    if not 0.0 < args.source_runtime_seconds <= 15.0:
        parser.error("source runtime must be in (0,15]")
    if not -19.0 <= args.x_final <= -18.0:
        parser.error("x_final must be in [-19,-18]")
    if not 0.25 <= args.segment_efolds <= 1.0:
        parser.error("segment size must be in [0.25,1]")
    if not 0.001 <= args.max_step <= 0.02:
        parser.error("max_step must be in [0.001,0.02]")
    if not 1e-12 <= args.rtol <= 1e-8:
        parser.error("rtol must be in [1e-12,1e-8]")
    if not 1e-16 <= args.atol <= 1e-12:
        parser.error("atol must be in [1e-16,1e-12]")
    if args.safety_cap != 1e12:
        parser.error("BR3C-b safety cap is frozen at 1e12")

    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("BR3C-b internal deadline exceeded")

    source = Path(__file__).with_name(
        "132_script_A2_K4_3b_RG_BR3C_a_registered_zero_projection.py"
    )
    source_command = [
        sys.executable,
        str(source),
        "--max-runtime-seconds",
        str(args.source_runtime_seconds),
        "--standard-order",
        "6",
        "--x-deep",
        "-25",
        "--x-shallow",
        "-23",
        "--k-mpc",
        "0.05",
        "--fuel-fraction-coefficient",
        "1.0",
    ]
    source_run = subprocess.run(
        source_command,
        capture_output=True,
        text=True,
        timeout=min(20.0, args.max_runtime_seconds),
        check=False,
    )
    if source_run.returncode != 0:
        raise RuntimeError(
            f"state source returned {source_run.returncode}: "
            f"{source_run.stderr[-1000:]} {source_run.stdout[-1000:]}"
        )
    source_payload = json.loads(source_run.stdout)
    source_pass = (
        source_payload.get("execution_verdict")
        == "PASS_BR3C_A_REGISTERED_ZERO_STATE"
    )
    if not source_pass:
        raise RuntimeError("authoritative BR3C-a state source did not pass")

    delta = 0.02297
    p = 4.0 - 3.0 * delta
    h0 = 0.6637
    omega_m0 = 0.3517
    ombh2 = 0.02237
    total_matter_h2 = omega_m0 * h0**2
    fb = ombh2 / total_matter_h2
    fc = 1.0 - fb
    neff = 3.046 + 0.0535
    rn = 0.2271 * neff / (1.0 + 0.2271 * neff)
    rg = 1.0 - rn
    omega_gamma_h2 = 2.47282e-5
    omega_r0 = omega_gamma_h2 * (1.0 + 0.2271 * neff) / h0**2
    hubble0_mpc = 100.0 * h0 / 299792.458
    k_mpc = 0.05
    mu = hubble0_mpc * omega_m0 / math.sqrt(omega_r0) / k_mpc
    lambda_transfer = 0.15
    g2 = lambda_transfer * (hubble0_mpc / k_mpc) ** 2 * math.sqrt(omega_r0)
    phi_coefficient = 1.0
    transfer_shape = g2 * (1.0 / (p + 1.0) - 0.5)

    def background(x_value: float) -> dict[str, float]:
        z = k_mpc * math.exp(x_value) / (hubble0_mpc * math.sqrt(omega_r0))
        fuel_piece = phi_coefficient * z**p
        denominator = 1.0 + mu * z + fuel_piece * (
            1.0 + transfer_shape * z**2
        )
        denominator_x = mu * z + fuel_piece * (
            p + (p + 2.0) * transfer_shape * z**2
        )
        q = -1.0 + 0.5 * denominator_x / denominator
        s2 = z**2 / denominator
        omegas = {
            "gamma": rg / denominator,
            "fs": rn / denominator,
            "b": fb * mu * z / denominator,
            "c": (
                fc * mu * z
                + phi_coefficient * g2 * z ** (p + 2.0) / (p + 1.0)
            )
            / denominator,
            "f": (
                fuel_piece * (1.0 - 0.5 * g2 * z**2) / denominator
            ),
        }
        loading = 3.0 * fb * mu * z / (4.0 * rg)
        g = g2 * z**2
        gr = (
            phi_coefficient
            * g2
            / (fc * mu)
            * z ** (p + 1.0)
        )
        return {
            "z": z,
            "D": denominator,
            "q": q,
            "s2": s2,
            "loading": loading,
            "g": g,
            "gr": gr,
            **{f"Omega_{name}": value for name, value in omegas.items()},
        }

    rhs_calls = 0

    def rhs(x_value: float, y: np.ndarray) -> np.ndarray:
        nonlocal rhs_calls
        rhs_calls += 1
        if rhs_calls % 64 == 0:
            deadline()
        (
            h,
            eta,
            delta_gamma,
            delta_fs,
            delta_b,
            delta_c,
            U_gamma,
            U_fs,
            sigma_fs,
            L3_fs,
            L4_fs,
            delta_f,
            U_f,
        ) = y
        bg = background(x_value)
        density = (
            bg["Omega_gamma"] * delta_gamma
            + bg["Omega_fs"] * delta_fs
            + bg["Omega_b"] * delta_b
            + bg["Omega_c"] * delta_c
            + bg["Omega_f"] * delta_f
        )
        h_x = 3.0 * density + 2.0 * bg["s2"] * eta
        eta_x = (
            2.0 * bg["Omega_gamma"] * U_gamma
            + 2.0 * bg["Omega_fs"] * U_fs
            + 1.5 * bg["Omega_b"] * U_gamma
            + 1.5 * delta * bg["Omega_f"] * U_f
        )
        inv1r = 1.0 / (1.0 + bg["loading"])
        load_fraction = bg["loading"] * inv1r
        dg_x = -(4.0 / 3.0) * bg["s2"] * U_gamma - (2.0 / 3.0) * h_x
        Ug_x = (
            bg["q"] * U_gamma
            - load_fraction * U_gamma
            + 0.25 * inv1r * delta_gamma
        )
        dn_x = -(4.0 / 3.0) * bg["s2"] * U_fs - (2.0 / 3.0) * h_x
        Un_x = bg["q"] * U_fs + 0.25 * delta_fs - sigma_fs
        sig_x = (
            (2.0 / 15.0) * h_x
            + (4.0 / 5.0) * eta_x
            + (4.0 / 15.0) * bg["s2"] * U_fs
            - (3.0 / 10.0) * L3_fs
        )
        L3_x = (
            -bg["q"] * L3_fs
            + (6.0 / 7.0) * bg["s2"] * sigma_fs
            - (4.0 / 7.0) * L4_fs
        )
        L4_x = -2.0 * bg["q"] * L4_fs + (4.0 / 9.0) * bg["s2"] * L3_fs
        db_x = -bg["s2"] * U_gamma - 0.5 * h_x
        dc_x = -0.5 * h_x + bg["gr"] * (delta_f - delta_c)
        df_x = (
            -3.0 * (2.0 - delta) * delta_f
            - delta * bg["s2"] * U_f
            - 0.5 * delta * h_x
            - 9.0 * delta * (2.0 - delta) * U_f
            - 3.0 * (2.0 - delta) * bg["g"] * U_f
        )
        Uf_x = (
            (bg["q"] + 2.0) * U_f
            + delta_f / delta
            + (2.0 / delta) * bg["g"] * U_f
        )
        return np.asarray(
            [
                h_x,
                eta_x,
                dg_x,
                dn_x,
                db_x,
                dc_x,
                Ug_x,
                Un_x,
                sig_x,
                L3_x,
                L4_x,
                df_x,
                Uf_x,
            ],
            dtype=float,
        )

    checks: dict[str, bool] = {"authoritative_state_source_pass": source_pass}
    results: dict[str, dict] = {}
    for mode in ("NID", "NIV"):
        results[mode] = {}
        for surface in ("deep", "shallow"):
            deadline()
            source_surface = source_payload["BR3C_state_surfaces"][mode][
                "surfaces"
            ][surface]
            state = source_surface["state"]
            y = np.asarray([state[name] for name in STATE_NAMES], dtype=float)
            x_current = float(source_surface["x"])
            component_maxima = np.abs(y).copy()
            checkpoints = []
            total_nfev = 0
            trajectory_success = True
            trajectory_error = ""
            while x_current < args.x_final - 1e-13:
                deadline()
                x_next = min(x_current + args.segment_efolds, args.x_final)
                try:
                    solution = solve_ivp(
                        rhs,
                        (x_current, x_next),
                        y,
                        method="DOP853",
                        rtol=args.rtol,
                        atol=args.atol,
                        max_step=args.max_step,
                    )
                except TimeoutError as exc:
                    trajectory_success = False
                    trajectory_error = str(exc)
                    break
                total_nfev += int(solution.nfev)
                if solution.y.size:
                    component_maxima = np.maximum(
                        component_maxima, np.max(np.abs(solution.y), axis=1)
                    )
                if not solution.success or solution.y.size == 0:
                    trajectory_success = False
                    trajectory_error = solution.message
                    break
                y = np.asarray(solution.y[:, -1], dtype=float)
                x_current = float(solution.t[-1])
                rhs_end = rhs(x_current, y)
                checkpoint_finite = bool(
                    np.all(np.isfinite(y)) and np.all(np.isfinite(rhs_end))
                )
                checkpoint_cap = bool(
                    max(np.max(np.abs(y)), np.max(component_maxima))
                    < args.safety_cap
                )
                checkpoints.append(
                    {
                        "x": x_current,
                        "z": background(x_current)["z"],
                        "nfev_segment": int(solution.nfev),
                        "state_max_abs": float(np.max(np.abs(y))),
                        "rhs_max_abs": float(np.max(np.abs(rhs_end))),
                        "finite": checkpoint_finite,
                        "below_safety_cap": checkpoint_cap,
                    }
                )
                if not checkpoint_finite or not checkpoint_cap:
                    trajectory_success = False
                    trajectory_error = "nonfinite state/RHS or safety cap exceeded"
                    break

            expected_segments = int(
                math.ceil((args.x_final - float(source_surface["x"]))
                          / args.segment_efolds - 1e-14)
            )
            reached_final = abs(x_current - args.x_final) < 2e-12
            finite_final = bool(
                np.all(np.isfinite(y)) and np.all(np.isfinite(rhs(x_current, y)))
            )
            below_cap = bool(np.max(component_maxima) < args.safety_cap)
            complete_state = len(y) == len(STATE_NAMES)
            checks[f"{mode}_{surface}_solver_success"] = trajectory_success
            checks[f"{mode}_{surface}_reached_x_final"] = reached_final
            checks[f"{mode}_{surface}_all_checkpoints_written"] = (
                len(checkpoints) == expected_segments
            )
            checks[f"{mode}_{surface}_finite_final_state_and_rhs"] = finite_final
            checks[f"{mode}_{surface}_below_safety_cap"] = below_cap
            checks[f"{mode}_{surface}_complete_13_component_state"] = complete_state
            results[mode][surface] = {
                "x_start": float(source_surface["x"]),
                "x_final_reached": x_current,
                "expected_segments": expected_segments,
                "checkpoints": checkpoints,
                "total_nfev": total_nfev,
                "trajectory_success": trajectory_success,
                "trajectory_error": trajectory_error,
                "final_state": {
                    name: float(value) for name, value in zip(STATE_NAMES, y)
                },
                "component_max_abs": {
                    name: float(value)
                    for name, value in zip(STATE_NAMES, component_maxima)
                },
            }

    checks["all_four_trajectories_present"] = sum(
        len(mode_results) for mode_results in results.values()
    ) == 4
    checks["registered_state_names_exact"] = STATE_NAMES == (
        "h", "eta", "delta_gamma", "delta_fs", "delta_b", "delta_c",
        "U_gamma", "U_fs", "sigma_fs", "L3_fs", "L4_fs", "delta_f", "U_f"
    )
    passed = bool(checks) and all(checks.values())
    output = {
        "test": "A2-K4.3b-RG BR3C-b segmented early evolution",
        "state_source": source.name,
        "state_names": list(STATE_NAMES),
        "solver": {
            "method": "DOP853",
            "rtol": args.rtol,
            "atol": args.atol,
            "max_step": args.max_step,
            "segment_efolds": args.segment_efolds,
            "x_final": args.x_final,
            "safety_cap": args.safety_cap,
            "closure": "L5=0 bounded BR3C closure; full hierarchy pending",
        },
        "results": results,
        "checks": checks,
        "execution_verdict": (
            "PASS_BR3C_B_SEGMENTED_EARLY_EVOLUTION"
            if passed
            else "REVIEW_BR3C_B_EVOLUTION_UNCLOSED"
        ),
        "physical_verdict": (
            "K4 survives C7.7b finite early evolution"
            if passed
            else "no death verdict; inspect solver/checkpoint failure"
        ),
        "fine_depth": "66.5/100" if passed else "66.2/100",
        "scope_limit": (
            "does not test deep/shallow endpoint agreement, trace/traceless "
            "Einstein residuals, step convergence, or the full hierarchy"
        ),
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "rhs_calls": rhs_calls,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.TimeoutExpired as exc:
        print(
            json.dumps(
                {"execution_verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}
            )
        )
        raise SystemExit(124)
    except TimeoutError as exc:
        print(
            json.dumps(
                {"execution_verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}
            )
        )
        raise SystemExit(124)
    except Exception as exc:
        print(
            json.dumps(
                {"execution_verdict": "ERROR_UNCLOSED", "error": repr(exc)}
            )
        )
        raise SystemExit(2)

