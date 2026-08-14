#!/usr/bin/env python
"""Audited P3a-B fixed-RK4 test with two exact-zero terms removed."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import time

import numpy as np


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "178_script_A2_K4_C7_7c_K7c2_high_precision_seed_handoff.py"
NAMES = (
    "h", "eta", "delta_gamma", "D", "delta_b", "delta_c",
    "U_gamma", "M", "sigma_fs", "L3_fs", "L4_fs", "delta_f", "U_f",
)

EXPECTED_SOURCE_178_SHA256 = (
    "875ABF60DAE70D322CBFB5A9BC16361E2EF4861A0267E4555BCF6BD353DD6F55"
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()



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
    parser.add_argument("--checkpoint-directory", type=Path, required=True)
    parser.add_argument("--checkpoint-prefix", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 12 <= args.max_runtime_seconds <= 25:
        parser.error("max-runtime-seconds must be in [12,25]")
    if not 10 <= args.source_runtime_seconds <= 18:
        parser.error("source-runtime-seconds must be in [10,18]")
    if not 5 <= args.source_child_runtime_seconds <= 8:
        parser.error("source-child-runtime-seconds must be in [5,8]")
    output_path = args.output.resolve()
    if output_path.exists():
        raise FileExistsError(f"authoritative output overwrite refused: {output_path}")
    actual_source_hash = sha256_file(SOURCE)
    if actual_source_hash != EXPECTED_SOURCE_178_SHA256:
        raise RuntimeError("seed source 178 hash changed")

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
    if set(deep_seed) != set(NAMES) or set(shallow_seed) != set(NAMES):
        raise RuntimeError("K7c.2 seed-name set changed")
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
                # P3a-A proved both omitted coefficients are identically zero.
                # No replacement force or fit term is introduced.
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
    executed_path_id = "P3B_ZERO_IDENTITY_FIXED_CLASSICAL_RK4_ONLY"
    checkpoint_directory = args.checkpoint_directory.resolve()
    if not checkpoint_directory.is_dir():
        parser.error("checkpoint-directory must already exist")
    if not args.checkpoint_prefix or len(args.checkpoint_prefix) > 80 or not all(
        char.isalnum() or char in "_-" for char in args.checkpoint_prefix
    ):
        parser.error("checkpoint-prefix must contain only letters, digits, _ or -")
    checkpoint_paths = {
        grid: checkpoint_directory / f"{args.checkpoint_prefix}_grid{grid}.json"
        for grid in (100, 200, 400)
    }
    existing = [str(path) for path in checkpoint_paths.values() if path.exists()]
    if existing:
        raise FileExistsError(f"checkpoint overwrite refused: {existing}")

    def write_checkpoint(grid: int, step: float, endpoint: np.ndarray) -> str:
        endpoint_native = np.asarray(endpoint, dtype=float)
        endpoint_bytes = np.asarray(endpoint_native, dtype="<f8").tobytes()
        payload = {
            "test": "A2-K4 K7c P3a-B exact-zero fixed-RK4 grid checkpoint",
            "executed_path_id": executed_path_id,
            "derived_from_script_179_sha256":
                "8f45dc698817992e4fb2b859a7cafa49d225b4f7f5fd54b07f88ca99059bd441",
            "grid_steps": grid,
            "step": step,
            "x_start": x_start,
            "x_final": x_final,
            "state_names": list(NAMES),
            "normalized_endpoint": dict(zip(NAMES, map(float, endpoint_native))),
            "physical_endpoint": dict(zip(NAMES, map(float, endpoint_native * scale))),
            "normalized_endpoint_binary_sha256": hashlib.sha256(endpoint_bytes).hexdigest(),
            "rhs_calls_cumulative": rhs_calls,
            "maximum_normalized_abs_cumulative": maximum_normalized_abs,
        }
        canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        payload["payload_sha256_without_self"] = hashlib.sha256(
            canonical.encode("utf-8")
        ).hexdigest()
        with checkpoint_paths[grid].open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")
        return payload["payload_sha256_without_self"]

    def integrate_fixed_rk4(step: float) -> tuple[int, list[tuple[float, np.ndarray]], np.ndarray]:
        interval = x_final - x_start
        step_count = int(round(interval / step))
        if abs(step_count * step - interval) > 1e-14 or step_count % 2:
            raise RuntimeError("RK4 grid does not close interval and midpoint")
        normalized = w0.copy()
        checkpoint_indices = {0, step_count // 2, step_count}
        trajectory = [(x_start, normalized.copy())]
        for index in range(step_count):
            if index % 25 == 0:
                deadline()
            x_now = x_start + index * step
            k1 = scaled_rhs(x_now, normalized)
            k2 = scaled_rhs(x_now + step / 2, normalized + step * k1 / 2)
            k3 = scaled_rhs(x_now + step / 2, normalized + step * k2 / 2)
            k4 = scaled_rhs(x_now + step, normalized + step * k3)
            normalized = normalized + step * (k1 + 2 * k2 + 2 * k3 + k4) / 6
            if not np.all(np.isfinite(normalized)):
                raise FloatingPointError("non-finite fixed-RK4 state")
            if index + 1 in checkpoint_indices:
                trajectory.append((x_start + (index + 1) * step, normalized.copy()))
        deadline()
        return step_count, trajectory, normalized

    grid100_steps, grid100_trajectory, endpoint100 = integrate_fixed_rk4(0.0025)
    checkpoint_hash100 = write_checkpoint(100, 0.0025, endpoint100)
    grid200_steps, grid200_trajectory, endpoint200 = integrate_fixed_rk4(0.00125)
    checkpoint_hash200 = write_checkpoint(200, 0.00125, endpoint200)
    grid400_steps, grid400_trajectory, endpoint400 = integrate_fixed_rk4(0.000625)
    checkpoint_hash400 = write_checkpoint(400, 0.000625, endpoint400)

    difference_100_200_by_component = np.abs(endpoint200 - endpoint100)
    difference_200_400_by_component = np.abs(endpoint400 - endpoint200)
    difference_100_200 = float(np.max(difference_100_200_by_component))
    difference_200_400 = float(np.max(difference_200_400_by_component))
    refinement_ratio = difference_100_200 / max(difference_200_400, 1e-300)
    dominant_index = int(np.argmax(difference_200_400_by_component))
    dominant_component = NAMES[dominant_index]
    normalized_change = float(np.max(np.abs(endpoint400 - w0)))

    checkpoint_output = []
    max_density_scaled = 0.0
    max_momentum_scaled = 0.0
    all_checkpoint_finite = True
    for x_value, normalized in grid400_trajectory:
        state = normalized * scale
        b = background(float(x_value))
        rhs = physical_rhs(float(x_value), state)
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
        finite = bool(
            np.all(np.isfinite(state)) and np.all(np.isfinite(rhs))
            and math.isfinite(dn) and math.isfinite(Un)
        )
        all_checkpoint_finite = all_checkpoint_finite and finite
        checkpoint_output.append({
            "x": float(x_value),
            "state": dict(zip(NAMES, map(float, state))),
            "rhs": dict(zip(NAMES, map(float, rhs))),
            "reconstructed_delta_fs": float(dn),
            "reconstructed_U_fs": float(Un),
            "density_constraint_scaled_residual": density_scaled,
            "momentum_constraint_scaled_residual": momentum_scaled,
            "finite": finite,
        })

    runtime_source_text = Path(__file__).read_text(encoding="utf-8")
    structural_checks = {
        "seed_source_hash_exact": actual_source_hash == EXPECTED_SOURCE_178_SHA256,
        "source_exit_zero": child.returncode == 0,
        "source_seed_handoff_pass": source.get("execution_verdict") ==
            "PASS_C7_7C_K7C2_HIGH_PRECISION_SEED_HANDOFF",
        "source_names_exact": set(source.get("projected_state_names", ())) == set(NAMES),
        "executed_path_id_exact": executed_path_id ==
            "P3B_ZERO_IDENTITY_FIXED_CLASSICAL_RK4_ONLY",
        "legacy_adaptive_solver_token_absent": ("solve" + "_ivp") not in runtime_source_text,
        "original_c_U_expression_absent":
            "(1.5 * Ob - Wg * b[\"load_fraction\"]) * Ug" not in runtime_source_text,
        "original_c_delta_expression_absent":
            "(0.25 * Wg * b[\"inv1r\"] - 0.5 * Og) * dg" not in runtime_source_text,
        "grid_steps_exact": (grid100_steps, grid200_steps, grid400_steps) ==
            (100, 200, 400),
        "each_grid_has_three_audit_surfaces": all(
            len(item) == 3 for item in
            (grid100_trajectory, grid200_trajectory, grid400_trajectory)
        ),
        "all_immutable_checkpoints_written": all(
            path.is_file() for path in checkpoint_paths.values()
        ),
        "checkpoint_hashes_unique_and_nonempty": len({
            checkpoint_hash100, checkpoint_hash200, checkpoint_hash400
        }) == 3 and all((checkpoint_hash100, checkpoint_hash200, checkpoint_hash400)),
        "finest_checkpoint_states_and_rhs_finite": all_checkpoint_finite,
        "differences_finite_nonnegative": (
            math.isfinite(difference_100_200)
            and math.isfinite(difference_200_400)
            and difference_100_200 >= 0
            and difference_200_400 >= 0
        ),
        "refinement_ratio_finite_nonnegative":
            math.isfinite(refinement_ratio) and refinement_ratio >= 0,
        "density_constraint_scaled_below_5e-12": max_density_scaled < 5e-12,
        "momentum_constraint_scaled_below_5e-12": max_momentum_scaled < 5e-12,
        "rhs_call_cap_respected": rhs_calls <= 200000,
        "normalized_safety_cap_respected": maximum_normalized_abs < 1e8,
    }
    structural_checks = {key: bool(value) for key, value in structural_checks.items()}
    physical_convergence_checks = {
        "difference_200_400_below_1e-6": difference_200_400 < 1e-6,
        "classical_RK4_ratio_between_8_and_32": 8 <= refinement_ratio <= 32,
    }
    physical_convergence_checks = {
        key: bool(value) for key, value in physical_convergence_checks.items()
    }
    structural_pass = bool(structural_checks) and all(structural_checks.values())
    convergence_pass = (
        bool(physical_convergence_checks)
        and all(physical_convergence_checks.values())
    )
    if not structural_pass:
        execution_verdict = "REVIEW_P3B_STRUCTURAL_OR_PROVENANCE_FAILURE"
        physical_verdict = "REVIEW: structural/provenance gate failed"
        next_step = "repair audit integrity before physical interpretation"
    elif convergence_pass:
        execution_verdict = "PASS_P3B_ZERO_IDENTITY_RK4_CONVERGENCE"
        physical_verdict = "PASS: both preregistered RK4 convergence gates passed"
        next_step = "open the separately preregistered wider G4/G6 audit"
    else:
        execution_verdict = "STOP_P3B_ZERO_IDENTITY_NOT_SUFFICIENT"
        physical_verdict = (
            "STOP: valid evolution failed at least one preregistered convergence gate"
        )
        next_step = "retain this dead track and open a separate stiffness/eigenmode audit"

    output = {
        "test": "SCI-A2K4-C7G5-K7C-P3B-ZERO-IDENTITY-RK4",
        "executed_path_id": executed_path_id,
        "derived_from_script_197_sha256":
            "088B4CD58F57A30BD061D30042BA3E2CB5021DF9BF320003ED8291D86FB6C022",
        "seed_source_178_sha256": actual_source_hash,
        "P3a_A_raw_sha256":
            "4C9747DEF1AB9662735E974B1A992C6FC12784F20F69EB4A73862A9E234C7E65",
        "profile_request": {"mode": "NID", "surface": "deep",
                            "x_start": x_start, "x_final": x_final},
        "state_names": list(NAMES),
        "integration_scale": dict(zip(NAMES, map(float, scale))),
        "solver": {
            "method": "fixed classical RK4",
            "steps": [0.0025, 0.00125, 0.000625],
            "grid_steps": [grid100_steps, grid200_steps, grid400_steps],
            "adaptive_error_control": False,
            "L5_closure": "L5=0 bounded closure",
        },
        "results": {
            "rhs_calls_including_audit": rhs_calls,
            "maximum_normalized_abs": maximum_normalized_abs,
            "difference_100_200": difference_100_200,
            "difference_200_400": difference_200_400,
            "previous_over_current_difference": refinement_ratio,
            "dominant_200_400_component": dominant_component,
            "difference_100_200_by_component": dict(zip(
                NAMES, map(float, difference_100_200_by_component)
            )),
            "difference_200_400_by_component": dict(zip(
                NAMES, map(float, difference_200_400_by_component)
            )),
            "max_normalized_finest_change": normalized_change,
            "max_density_constraint_scaled_residual": max_density_scaled,
            "max_momentum_constraint_scaled_residual": max_momentum_scaled,
            "grid100_endpoint_state": dict(zip(NAMES, map(float, endpoint100 * scale))),
            "grid200_endpoint_state": dict(zip(NAMES, map(float, endpoint200 * scale))),
            "grid400_endpoint_state": dict(zip(NAMES, map(float, endpoint400 * scale))),
            "finest_checkpoints": checkpoint_output,
            "checkpoint_files": {str(grid): str(path) for grid, path in checkpoint_paths.items()},
            "checkpoint_payload_hashes": {
                "100": checkpoint_hash100,
                "200": checkpoint_hash200,
                "400": checkpoint_hash400,
            },
        },
        "structural_checks": structural_checks,
        "physical_convergence_checks": physical_convergence_checks,
        "structural_pass": structural_pass,
        "convergence_pass": convergence_pass,
        "identity_terms_omitted": [
            "(1.5*Ob-Wg*load_fraction)*U_gamma",
            "(0.25*Wg*inv1r-0.5*Og)*delta_gamma",
        ],
        "execution_verdict": execution_verdict,
        "physical_verdict": physical_verdict,
        "fine_depth": "66.5/100",
        "score_effect": "NONE",
        "next_step": next_step,
        "scope_limit":
            "0.25 e-fold NID/deep P3a-B only; no four-surface, CMB/S8, or full-hierarchy claim",
        "runtime_limits_seconds": {
            "total": args.max_runtime_seconds,
            "seed_source": args.source_runtime_seconds,
            "seed_source_children": args.source_child_runtime_seconds,
            "rhs_calls": 200000,
        },
        "runtime_seconds": time.monotonic() - started,
    }
    encoded = json.dumps(output, indent=2, sort_keys=True)
    if not output_path.parent.is_dir():
        raise FileNotFoundError(f"output parent missing: {output_path.parent}")
    with output_path.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(encoded + "\n")
    print(encoded)
    if not structural_pass:
        return 2
    return 0 if convergence_pass else 1

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
