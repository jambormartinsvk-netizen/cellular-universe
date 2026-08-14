#!/usr/bin/env python3
"""Run one immutable P4a adaptive-solver case on the frozen P3b system."""

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
from scipy.integrate import solve_ivp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOURCE = HERE / "178_script_A2_K4_C7_7c_K7c2_high_precision_seed_handoff.py"
BASE205 = HERE / "205_script_A2_K4_C7_7c_K7c_P3b_zero_identity_RK4_audited.py"
REFERENCE = ROOT / "Audit" / "A2_K4_K7C_P3B_20260715_grid400.json"
NAMES = (
    "h", "eta", "delta_gamma", "D", "delta_b", "delta_c",
    "U_gamma", "M", "sigma_fs", "L3_fs", "L4_fs", "delta_f", "U_f",
)

EXPECTED_SOURCE_178_SHA256 = (
    "875ABF60DAE70D322CBFB5A9BC16361E2EF4861A0267E4555BCF6BD353DD6F55"
)
EXPECTED_BASE205_SHA256 = (
    "B7EC8BAD3BFB0D48EC91D6F1BB0A602FA1834A021BB94C92D6D1B398D5F3CDC2"
)
EXPECTED_REFERENCE_SHA256 = (
    "9E3C73D635924E829A5F57BA540EBB1F5861F67F21CFCE69BD93423D6FA8FC8D"
)

CASES = {
    "DOP853_MEDIUM": {"method": "DOP853", "rtol": 1e-9, "atol": 1e-11},
    "DOP853_TIGHT": {"method": "DOP853", "rtol": 1e-11, "atol": 1e-13},
    "RADAU_TIGHT": {"method": "Radau", "rtol": 1e-10, "atol": 1e-12},
}


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
    parser = argparse.ArgumentParser(
        description="Run one frozen A2-K4 K7c P4a solver case"
    )
    parser.add_argument("--case", choices=tuple(CASES), required=True)
    parser.add_argument("--max-runtime-seconds", type=float, required=True)
    parser.add_argument("--source-runtime-seconds", type=float, default=12.0)
    parser.add_argument("--source-child-runtime-seconds", type=float, default=6.0)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 5 <= args.max_runtime_seconds <= 20:
        parser.error("max-runtime-seconds must be in [5,20]")
    if not 10 <= args.source_runtime_seconds <= 12:
        parser.error("source-runtime-seconds must be in [10,12]")
    if not 5 <= args.source_child_runtime_seconds <= 6:
        parser.error("source-child-runtime-seconds must be in [5,6]")

    output_path = args.output.resolve()
    if output_path.exists():
        raise FileExistsError(f"authoritative output overwrite refused: {output_path}")
    if not output_path.parent.is_dir():
        raise FileNotFoundError(f"output parent missing: {output_path.parent}")

    source_hash = sha256_file(SOURCE)
    base205_hash = sha256_file(BASE205)
    reference_hash = sha256_file(REFERENCE)
    if source_hash != EXPECTED_SOURCE_178_SHA256:
        raise RuntimeError("seed source 178 hash changed")
    if base205_hash != EXPECTED_BASE205_SHA256:
        raise RuntimeError("P3b base script 205 hash changed")
    if reference_hash != EXPECTED_REFERENCE_SHA256:
        raise RuntimeError("P3b grid400 reference hash changed")

    reference_payload = json.loads(REFERENCE.read_text(encoding="utf-8"))
    if list(reference_payload.get("state_names", ())) != list(NAMES):
        raise RuntimeError("P3b reference state names/order changed")
    if int(reference_payload.get("grid_steps", -1)) != 400:
        raise RuntimeError("P3b reference is not grid400")
    reference_map = dict(reference_payload.get("normalized_endpoint", {}))
    if set(reference_map) != set(NAMES):
        raise RuntimeError("P3b reference endpoint keys changed")
    reference_endpoint = np.asarray(
        [float(reference_map[name]) for name in NAMES], dtype=float
    )

    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("P4a single-case internal deadline exceeded")

    child = subprocess.run(
        [
            sys.executable,
            str(SOURCE),
            "--max-runtime-seconds",
            str(args.source_runtime_seconds),
            "--child-runtime-seconds",
            str(args.source_child_runtime_seconds),
        ],
        capture_output=True,
        text=True,
        timeout=args.source_runtime_seconds + 1,
        check=False,
    )
    source = parse_json(child.stdout)
    deadline()
    source_results = dict(source.get("results", {}))
    deep_seed = dict(dict(source_results["NID_deep"])["projected_seed_float64"])
    shallow_seed = dict(
        dict(source_results["NID_shallow"])["projected_seed_float64"]
    )
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
        denominator_x = mu * z + fuel_piece * (
            p + (p + 2) * transfer_shape * z**2
        )
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
        beta_c = (
            fc * mu * z + (p + 2) * g2 * z**(p + 2) / (p + 1)
        ) / c_numerator
        beta_f = p - g / (1 - g / 2)
        return {
            "z": z,
            "ell": ell,
            "q": -1 + ell / 2,
            "s2": s2,
            "Og": Og,
            "On": On,
            "Ob": Ob,
            "Oc": Oc,
            "Of": Of,
            "load_fraction": loading * inv1r,
            "inv1r": inv1r,
            "g": g,
            "gr": gr,
            "beta_c": beta_c,
            "beta_f": beta_f,
        }

    rhs_calls = 0
    maximum_normalized_abs = float(np.max(np.abs(w0)))

    def physical_rhs(x: float, state: np.ndarray) -> np.ndarray:
        nonlocal rhs_calls, maximum_normalized_abs
        rhs_calls += 1
        if rhs_calls > 100000:
            raise TimeoutError("P4a RHS call cap exceeded")
        if rhs_calls % 64 == 0:
            deadline()
        if not np.all(np.isfinite(state)):
            raise FloatingPointError("non-finite projected state")
        maximum_normalized_abs = max(
            maximum_normalized_abs, float(np.max(np.abs(state / scale)))
        )
        if maximum_normalized_abs > 1e8:
            raise FloatingPointError("P4a normalized safety cap exceeded")

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
    case = dict(CASES[args.case])
    solution = solve_ivp(
        scaled_rhs,
        (x_start, x_final),
        w0,
        method=str(case["method"]),
        rtol=float(case["rtol"]),
        atol=float(case["atol"]),
        t_eval=np.asarray([x_final]),
    )
    deadline()
    if solution.y.shape != (len(NAMES), 1):
        raise RuntimeError(f"unexpected solution shape: {solution.y.shape}")
    endpoint = np.asarray(solution.y[:, -1], dtype=float)
    final_rhs = scaled_rhs(x_final, endpoint)
    reference_difference = float(np.max(np.abs(endpoint - reference_endpoint)))
    endpoint_bytes = np.asarray(endpoint, dtype="<f8").tobytes()

    checks = {
        "seed_source_hash_exact": source_hash == EXPECTED_SOURCE_178_SHA256,
        "base205_hash_exact": base205_hash == EXPECTED_BASE205_SHA256,
        "reference_grid400_hash_exact": reference_hash == EXPECTED_REFERENCE_SHA256,
        "source_exit_zero": child.returncode == 0,
        "source_seed_handoff_pass": source.get("execution_verdict")
            == "PASS_C7_7C_K7C2_HIGH_PRECISION_SEED_HANDOFF",
        "source_names_exact_order": list(source.get("projected_state_names", ()))
            == list(NAMES),
        "reference_state_names_exact_order": list(
            reference_payload.get("state_names", ())
        ) == list(NAMES),
        "solver_success": bool(solution.success),
        "reached_exact_endpoint": bool(
            len(solution.t) == 1 and abs(float(solution.t[-1]) - x_final) <= 1e-13
        ),
        "finite_endpoint_and_rhs": bool(
            np.all(np.isfinite(endpoint)) and np.all(np.isfinite(final_rhs))
        ),
        "normalized_safety_cap_respected": maximum_normalized_abs <= 1e8,
        "rhs_call_cap_respected": rhs_calls <= 100000,
        "reference_difference_finite_nonnegative": bool(
            math.isfinite(reference_difference) and reference_difference >= 0
        ),
    }
    checks = {key: bool(value) for key, value in checks.items()}
    structural_pass = bool(checks) and all(checks.values())
    verdict = (
        "PASS_P4A_SINGLE_CASE_EXECUTION"
        if structural_pass else "REVIEW_P4A_SINGLE_CASE_STRUCTURE"
    )
    output = {
        "test": "SCI-A2K4-C7G5-K7C-P4A-METHOD-TOLERANCE-SINGLE-CASE",
        "case": args.case,
        "case_contract": case,
        "execution_verdict": verdict,
        "physical_verdict": "REVIEW: cross-case verdict belongs to offline aggregate 212",
        "physics_executed": True,
        "state_names": list(NAMES),
        "profile_request": {
            "mode": "NID", "surface": "deep",
            "x_start": x_start, "x_final": x_final,
        },
        "normalized_endpoint": dict(zip(NAMES, map(float, endpoint))),
        "physical_endpoint": dict(zip(NAMES, map(float, endpoint * scale))),
        "normalized_final_rhs": dict(zip(NAMES, map(float, final_rhs))),
        "integration_scale": dict(zip(NAMES, map(float, scale))),
        "reference_grid400_normalized_endpoint": dict(
            zip(NAMES, map(float, reference_endpoint))
        ),
        "reference_max_abs_difference": reference_difference,
        "normalized_endpoint_binary_sha256": hashlib.sha256(endpoint_bytes).hexdigest(),
        "solver": {
            "method": case["method"],
            "rtol": case["rtol"],
            "atol": case["atol"],
            "success": bool(solution.success),
            "message": str(solution.message),
            "nfev": int(solution.nfev),
            "njev": int(getattr(solution, "njev", 0)),
            "nlu": int(getattr(solution, "nlu", 0)),
            "endpoint": float(solution.t[-1]) if len(solution.t) else None,
        },
        "rhs_calls_including_final_audit": rhs_calls,
        "maximum_normalized_abs": maximum_normalized_abs,
        "checks": checks,
        "structural_pass": structural_pass,
        "hashes": {
            "self_sha256": sha256_file(Path(__file__)),
            "seed_source_178_sha256": source_hash,
            "base205_sha256": base205_hash,
            "reference_grid400_sha256": reference_hash,
        },
        "runtime_limits_seconds": {
            "total": args.max_runtime_seconds,
            "seed_source": args.source_runtime_seconds,
            "seed_source_children": args.source_child_runtime_seconds,
            "rhs_calls": 100000,
        },
        "runtime_seconds": time.monotonic() - started,
        "scope_limit": (
            "single NID/deep 0.25-e-fold P4a case; no G4/G6/G7, hierarchy, "
            "CMB, S8, H0, or likelihood claim"
        ),
    }
    encoded = json.dumps(output, indent=2, sort_keys=True)
    with output_path.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(encoded + "\n")
    print(encoded)
    return 0 if structural_pass else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.TimeoutExpired as exc:
        print(json.dumps({
            "execution_verdict": "TIMEOUT_UNCLOSED",
            "physics_executed": False,
            "error": repr(exc),
        }, indent=2))
        raise SystemExit(124)
    except TimeoutError as exc:
        print(json.dumps({
            "execution_verdict": "TIMEOUT_UNCLOSED",
            "error": str(exc),
        }, indent=2))
        raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({
            "execution_verdict": "ERROR_UNCLOSED",
            "error": repr(exc),
        }, indent=2))
        raise SystemExit(1)

