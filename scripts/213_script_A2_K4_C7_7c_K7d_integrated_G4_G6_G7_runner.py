#!/usr/bin/env python3
"""Bounded prepare/case/aggregate runner for K7d C7-G4+G6+G7.

The physics is frozen to the audited projected K7 RHS.  A single invocation
does exactly one action.  Scientific cases write immutable JSON files.
"""

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
SOURCE178 = HERE / "178_script_A2_K4_C7_7c_K7c2_high_precision_seed_handoff.py"
SOURCE146 = HERE / "146_script_A2_K4_3b_RG_C7_7c_K4_analytic_reference_state.py"
SOURCE209 = HERE / "209_script_A2_K4_C7_7c_K7c_P4a_single_case_solver.py"
PREREG = ROOT / "Questions" / (
    "A2_K4_C7_7C_K7D_G4_G6_G7_INTEGRATED_PREREGISTRATION_2026-07-15.md"
)

NAMES = (
    "h", "eta", "delta_gamma", "D", "delta_b", "delta_c",
    "U_gamma", "M", "sigma_fs", "L3_fs", "L4_fs", "delta_f", "U_f",
)
SPECIES_NAMES = (
    "h", "eta", "delta_gamma", "delta_fs", "delta_b", "delta_c",
    "U_gamma", "U_fs", "sigma_fs", "L3_fs", "L4_fs", "delta_f", "U_f",
)
CASES = {
    "NID_DEEP": ("NID", "deep", -25.0),
    "NID_SHALLOW": ("NID", "shallow", -23.0),
    "NIV_DEEP": ("NIV", "deep", -25.0),
    "NIV_SHALLOW": ("NIV", "shallow", -23.0),
}
EXPECTED_SOURCE178_SHA256 = (
    "875ABF60DAE70D322CBFB5A9BC16361E2EF4861A0267E4555BCF6BD353DD6F55"
)
EXPECTED_SOURCE209_SHA256 = (
    "67E5B3C1B7C942242E4FEB4458A4CC81A52F6417E25D50A6E2009023F321A612"
)

DELTA = 0.02297
P_EXPONENT = 3.93109
H0 = 0.6637
OMEGA_M0 = 0.3517
OMBH2 = 0.02237
FB = OMBH2 / (OMEGA_M0 * H0**2)
FC = 1.0 - FB
NEFF = 3.046 + 0.0535
RN = 0.2271 * NEFF / (1.0 + 0.2271 * NEFF)
RG = 1.0 - RN
OMEGA_R0 = 2.47282e-5 * (1.0 + 0.2271 * NEFF) / H0**2
HUBBLE0_MPC = 100.0 * H0 / 299792.458
K_MPC = 0.05
MU = HUBBLE0_MPC * OMEGA_M0 / math.sqrt(OMEGA_R0) / K_MPC
G2 = 0.15 * (HUBBLE0_MPC / K_MPC) ** 2 * math.sqrt(OMEGA_R0)
TRANSFER_SHAPE = G2 * (1.0 / (P_EXPONENT + 1.0) - 0.5)

X_FINAL = -18.0
RTOL = 1e-11
ATOL = 1e-13
MAX_STEP = 0.05
RHS_CAP = 100000
SAFETY_CAP = 1e8
ACTIVITY_EXCURSION_MIN = 1e-10
ACTIVITY_RHS_MIN = 1e-11
PARITY_MAX = 1e-10
CONSTRAINT_ABS = 1e-12
CONSTRAINT_REL = 1e-8
ENDPOINT_L2_MAX = 3e-3
ENDPOINT_ENVELOPE_MAX = 1e-2
OVERLAP_ENVELOPE_MAX = 2e-2


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def parse_json(text: str) -> dict[str, object]:
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        raise RuntimeError("child returned no JSON object")
    return json.loads(text[start:end + 1])


def write_immutable(path: Path, payload: dict[str, object]) -> None:
    target = path.resolve()
    if target.exists():
        raise FileExistsError(f"authoritative output overwrite refused: {target}")
    if not target.parent.is_dir():
        raise FileNotFoundError(f"output parent missing: {target.parent}")
    with target.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def background(x: float) -> dict[str, float]:
    z = K_MPC * math.exp(x) / (HUBBLE0_MPC * math.sqrt(OMEGA_R0))
    fuel_piece = z**P_EXPONENT
    denominator = 1.0 + MU * z + fuel_piece * (1.0 + TRANSFER_SHAPE * z**2)
    denominator_x = MU * z + fuel_piece * (
        P_EXPONENT + (P_EXPONENT + 2.0) * TRANSFER_SHAPE * z**2
    )
    ell = denominator_x / denominator
    s2 = z**2 / denominator
    Og, On = RG / denominator, RN / denominator
    Ob = FB * MU * z / denominator
    Oc = (FC * MU * z + G2 * z ** (P_EXPONENT + 2.0) / (P_EXPONENT + 1.0)) / denominator
    Of = fuel_piece * (1.0 - G2 * z**2 / 2.0) / denominator
    loading = 3.0 * FB * MU * z / (4.0 * RG)
    inv1r = 1.0 / (1.0 + loading)
    g = G2 * z**2
    gr = G2 / (FC * MU) * z ** (P_EXPONENT + 1.0)
    c_numerator = FC * MU * z + G2 * z ** (P_EXPONENT + 2.0) / (P_EXPONENT + 1.0)
    beta_c = (
        FC * MU * z
        + (P_EXPONENT + 2.0) * G2 * z ** (P_EXPONENT + 2.0) / (P_EXPONENT + 1.0)
    ) / c_numerator
    beta_f = P_EXPONENT - g / (1.0 - g / 2.0)
    return {
        "z": z, "ell": ell, "q": -1.0 + ell / 2.0, "s2": s2,
        "Og": Og, "On": On, "Ob": Ob, "Oc": Oc, "Of": Of,
        "load_fraction": loading * inv1r, "inv1r": inv1r,
        "g": g, "gr": gr, "beta_c": beta_c, "beta_f": beta_f,
    }


def projected_from_species(x: float, species: dict[str, float]) -> np.ndarray:
    b = background(x)
    D = math.fsum((
        b["Og"] * species["delta_gamma"],
        b["On"] * species["delta_fs"],
        b["Ob"] * species["delta_b"],
        b["Oc"] * species["delta_c"],
        b["Of"] * species["delta_f"],
    ))
    M = math.fsum((
        (2.0 * b["Og"] + 1.5 * b["Ob"]) * species["U_gamma"],
        2.0 * b["On"] * species["U_fs"],
        1.5 * DELTA * b["Of"] * species["U_f"],
    ))
    return np.asarray([
        species["h"], species["eta"], species["delta_gamma"], D,
        species["delta_b"], species["delta_c"], species["U_gamma"], M,
        species["sigma_fs"], species["L3_fs"], species["L4_fs"],
        species["delta_f"], species["U_f"],
    ], dtype=float)


def projected_to_species(x: float, state: np.ndarray) -> np.ndarray:
    h, eta, dg, D, db, dc, Ug, M, sig, L3, L4, df, Uf = state
    b = background(x)
    Wg, Wf = 2.0 * b["Og"] + 1.5 * b["Ob"], 1.5 * DELTA * b["Of"]
    dn = (D - b["Og"] * dg - b["Ob"] * db - b["Oc"] * dc - b["Of"] * df) / b["On"]
    Un = (M - Wg * Ug - Wf * Uf) / (2.0 * b["On"])
    return np.asarray([h, eta, dg, dn, db, dc, Ug, Un, sig, L3, L4, df, Uf], float)


def physical_rhs(x: float, state: np.ndarray) -> np.ndarray:
    h, eta, dg, D, db, dc, Ug, M, sig, L3, L4, df, Uf = state
    b = background(x)
    Og, On, Ob, Oc, Of = b["Og"], b["On"], b["Ob"], b["Oc"], b["Of"]
    Wg, Wf = 2.0 * Og + 1.5 * Ob, 1.5 * DELTA * Of
    dn = (D - Og * dg - Ob * db - Oc * dc - Of * df) / On
    Un = (M - Wg * Ug - Wf * Uf) / (2.0 * On)
    hx = 3.0 * D + 2.0 * b["s2"] * eta
    Ah = 2.0 / 3.0 * (Og + On) + 0.5 * (Ob + Oc) + 0.5 * DELTA * Of
    return np.asarray([
        hx,
        M,
        -4.0 / 3.0 * b["s2"] * Ug - 2.0 / 3.0 * hx,
        -b["ell"] * D + Ob * db + b["beta_c"] * Oc * dc
            + b["beta_f"] * Of * df - 2.0 / 3.0 * b["s2"] * M - Ah * hx
            + Oc * b["gr"] * (df - dc)
            + Of * (-3.0 * (2.0 - DELTA) * df
                    - 9.0 * DELTA * (2.0 - DELTA) * Uf
                    - 3.0 * (2.0 - DELTA) * b["g"] * Uf),
        -b["s2"] * Ug - hx / 2.0,
        -hx / 2.0 + b["gr"] * (df - dc),
        b["q"] * Ug - b["load_fraction"] * Ug + 0.25 * b["inv1r"] * dg,
        (-b["q"] - 2.0) * M + D / 2.0
            - 0.5 * Ob * db - 0.5 * Oc * dc + Of * df - 2.0 * On * sig
            + (1.5 * DELTA * Of * (b["beta_f"] + 2.0) + 3.0 * Of * b["g"]) * Uf,
        2.0 / 15.0 * hx + 4.0 / 5.0 * M + 4.0 / 15.0 * b["s2"] * Un - 3.0 / 10.0 * L3,
        -b["q"] * L3 + 6.0 / 7.0 * b["s2"] * sig - 4.0 / 7.0 * L4,
        -2.0 * b["q"] * L4 + 4.0 / 9.0 * b["s2"] * L3,
        -3.0 * (2.0 - DELTA) * df - DELTA * b["s2"] * Uf - DELTA * hx / 2.0
            - 9.0 * DELTA * (2.0 - DELTA) * Uf
            - 3.0 * (2.0 - DELTA) * b["g"] * Uf,
        (b["q"] + 2.0) * Uf + df / DELTA + 2.0 * b["g"] * Uf / DELTA,
    ], float)


def species_rhs_and_projected_derivative(x: float, projected: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    species = projected_to_species(x, projected)
    h, eta, dg, dn, db, dc, Ug, Un, sig, L3, L4, df, Uf = species
    b = background(x)
    D_species = math.fsum((
        b["Og"] * dg, b["On"] * dn, b["Ob"] * db,
        b["Oc"] * dc, b["Of"] * df,
    ))
    M_species = math.fsum((
        (2.0 * b["Og"] + 1.5 * b["Ob"]) * Ug,
        2.0 * b["On"] * Un,
        1.5 * DELTA * b["Of"] * Uf,
    ))
    hx = 3.0 * D_species + 2.0 * b["s2"] * eta
    eta_x = M_species
    species_rhs = np.asarray([
        hx,
        eta_x,
        -4.0 / 3.0 * b["s2"] * Ug - 2.0 / 3.0 * hx,
        -4.0 / 3.0 * b["s2"] * Un - 2.0 / 3.0 * hx,
        -b["s2"] * Ug - hx / 2.0,
        -hx / 2.0 + b["gr"] * (df - dc),
        b["q"] * Ug - b["load_fraction"] * Ug + 0.25 * b["inv1r"] * dg,
        b["q"] * Un + 0.25 * dn - sig,
        2.0 / 15.0 * hx + 4.0 / 5.0 * eta_x + 4.0 / 15.0 * b["s2"] * Un - 3.0 / 10.0 * L3,
        -b["q"] * L3 + 6.0 / 7.0 * b["s2"] * sig - 4.0 / 7.0 * L4,
        -2.0 * b["q"] * L4 + 4.0 / 9.0 * b["s2"] * L3,
        -3.0 * (2.0 - DELTA) * df - DELTA * b["s2"] * Uf - DELTA * hx / 2.0
            - 9.0 * DELTA * (2.0 - DELTA) * Uf
            - 3.0 * (2.0 - DELTA) * b["g"] * Uf,
        (b["q"] + 2.0) * Uf + df / DELTA + 2.0 * b["g"] * Uf / DELTA,
    ], float)

    Ogx, Onx = -b["ell"] * b["Og"], -b["ell"] * b["On"]
    Obx = (1.0 - b["ell"]) * b["Ob"]
    Ocx = (b["beta_c"] - b["ell"]) * b["Oc"]
    Ofx = (b["beta_f"] - b["ell"]) * b["Of"]
    D_x = math.fsum((
        Ogx * dg + b["Og"] * species_rhs[2],
        Onx * dn + b["On"] * species_rhs[3],
        Obx * db + b["Ob"] * species_rhs[4],
        Ocx * dc + b["Oc"] * species_rhs[5],
        Ofx * df + b["Of"] * species_rhs[11],
    ))
    Wg = 2.0 * b["Og"] + 1.5 * b["Ob"]
    Wgx = 2.0 * Ogx + 1.5 * Obx
    Wf = 1.5 * DELTA * b["Of"]
    Wfx = 1.5 * DELTA * Ofx
    M_x = math.fsum((
        Wgx * Ug + Wg * species_rhs[6],
        2.0 * Onx * Un + 2.0 * b["On"] * species_rhs[7],
        Wfx * Uf + Wf * species_rhs[12],
    ))
    projected_derivative = np.asarray([
        species_rhs[0], species_rhs[1], species_rhs[2], D_x,
        species_rhs[4], species_rhs[5], species_rhs[6], M_x,
        species_rhs[8], species_rhs[9], species_rhs[10],
        species_rhs[11], species_rhs[12],
    ], float)
    return species_rhs, projected_derivative


def checkpoint_diagnostics(x: float, state: np.ndarray, scale: np.ndarray) -> dict[str, object]:
    rhs = physical_rhs(x, state)
    species, species_projected = species_rhs_and_projected_derivative(x, state)
    b = background(x)
    h, eta, dg, D, db, dc, Ug, M, sig, L3, L4, df, Uf = state
    dn, Un = species[3], species[7]
    hx, D_x, M_x = rhs[0], rhs[3], rhs[7]
    hx_x = 3.0 * D_x - 4.0 * b["q"] * b["s2"] * eta + 2.0 * b["s2"] * M
    pressure = (
        b["Of"] * (df + (2.0 - DELTA) * (3.0 * DELTA + b["g"]) * Uf)
        + (b["Og"] * dg + b["On"] * dn) / 3.0
    )
    shear = 2.0 / 3.0 * b["On"] * sig
    trace_terms = (
        hx_x, (b["q"] + 2.0) * hx, -2.0 * b["s2"] * eta, 9.0 * pressure,
    )
    traceless_terms = (
        hx_x, 6.0 * M_x, (b["q"] + 2.0) * (hx + 6.0 * M),
        -2.0 * b["s2"] * eta, 9.0 * shear,
    )

    def ledger(terms: tuple[float, ...]) -> dict[str, object]:
        residual = abs(math.fsum(terms))
        norm = math.fsum(abs(value) for value in terms)
        allowance = CONSTRAINT_ABS + CONSTRAINT_REL * norm
        return {
            "terms": list(map(float, terms)),
            "absolute_residual": float(residual),
            "term_norm": float(norm),
            "relative_residual": float(residual / max(norm, 1e-300)),
            "allowance": float(allowance),
            "pass": bool(residual <= allowance),
        }

    parity_vector = (rhs - species_projected) / scale
    return {
        "x": float(x),
        "state": dict(zip(NAMES, map(float, state))),
        "normalized_state": dict(zip(NAMES, map(float, state / scale))),
        "normalized_rhs": dict(zip(NAMES, map(float, rhs / scale))),
        "trace": ledger(trace_terms),
        "traceless": ledger(traceless_terms),
        "species_projected_parity_max_abs": float(np.max(np.abs(parity_vector))),
        "species_projected_parity_vector": dict(zip(NAMES, map(float, parity_vector))),
        "finite": bool(
            np.all(np.isfinite(state)) and np.all(np.isfinite(rhs))
            and np.all(np.isfinite(species_projected))
        ),
    }


def action_prepare(args: argparse.Namespace) -> int:
    started = time.monotonic()
    if sha256_file(SOURCE178) != EXPECTED_SOURCE178_SHA256:
        raise RuntimeError("seed source 178 hash changed")
    if sha256_file(SOURCE209) != EXPECTED_SOURCE209_SHA256:
        raise RuntimeError("audited P4a source 209 hash changed")

    seed_child = subprocess.run([
        sys.executable, str(SOURCE178), "--max-runtime-seconds", "12",
        "--child-runtime-seconds", "6",
    ], capture_output=True, text=True, timeout=14, check=False)
    seeds = parse_json(seed_child.stdout)
    if time.monotonic() - started > args.max_runtime_seconds:
        raise TimeoutError("K7d prepare deadline exceeded after seed source")
    reference_child = subprocess.run([
        sys.executable, str(SOURCE146), "--max-runtime-seconds", "8",
        "--x-deep", "-25", "--x-shallow", "-23", "--x-reference", "-18",
    ], capture_output=True, text=True, timeout=10, check=False)
    reference = parse_json(reference_child.stdout)

    checks: dict[str, bool] = {
        "seed_child_exit_zero": seed_child.returncode == 0,
        "seed_child_expected_pass": seeds.get("execution_verdict")
            == "PASS_C7_7C_K7C2_HIGH_PRECISION_SEED_HANDOFF",
        "seed_names_exact_order": list(seeds.get("projected_state_names", ())) == list(NAMES),
        "reference_child_exit_zero": reference_child.returncode == 0,
        "reference_child_expected_pass": reference.get("execution_verdict")
            == "PASS_C7_7C_K4_ANALYTIC_REFERENCE_STATE",
        "prereg_present": PREREG.is_file(),
    }
    source_results = dict(seeds.get("results", {}))
    reference_modes = dict(reference.get("BR3C_state_surfaces", {}))
    packed_modes: dict[str, object] = {}
    for mode in ("NID", "NIV"):
        projected_seeds: dict[str, dict[str, float]] = {}
        for surface in ("deep", "shallow"):
            raw = dict(dict(source_results[f"{mode}_{surface}"])["projected_seed_float64"])
            checks[f"{mode}_{surface}_seed_keys_exact"] = set(raw) == set(NAMES)
            projected_seeds[surface] = {name: float(raw[name]) for name in NAMES}
        reference_surface = dict(dict(dict(reference_modes[mode])["surfaces"])["reference"])
        reference_state_raw = dict(reference_surface["state"])
        species = {
            "h": float(reference_state_raw["h"]),
            "eta": float(reference_state_raw["eta"]),
            "delta_gamma": float(reference_state_raw["delta_gamma"]),
            "delta_fs": float(reference_state_raw["delta_fs"]),
            "delta_b": float(reference_state_raw["delta_b"]),
            "delta_c": float(reference_state_raw["delta_c"]),
            "U_gamma": float(reference_state_raw["U_gamma"]),
            "U_fs": float(reference_state_raw["U_fs"]),
            "sigma_fs": float(reference_state_raw["sigma_fs"]),
            "L3_fs": float(reference_state_raw["L3_fs"]),
            "L4_fs": float(reference_state_raw["L4_fs"]),
            "delta_f": float(reference_state_raw["delta_f"]),
            "U_f": float(reference_state_raw["U_f"]),
        }
        reference_projected = projected_from_species(X_FINAL, species)
        deep = np.asarray([projected_seeds["deep"][name] for name in NAMES], float)
        shallow = np.asarray([projected_seeds["shallow"][name] for name in NAMES], float)
        scale = np.maximum.reduce((np.abs(deep), np.abs(shallow), np.abs(reference_projected), np.full(13, 1e-300)))
        checks[f"{mode}_scale_finite_positive"] = bool(
            np.all(np.isfinite(scale)) and np.all(scale > 0.0)
        )
        checks[f"{mode}_reference_x_exact"] = abs(float(reference_surface["x"]) - X_FINAL) <= 1e-13
        packed_modes[mode] = {
            "seeds": projected_seeds,
            "analytic_reference_projected": dict(zip(NAMES, map(float, reference_projected))),
            "scale": dict(zip(NAMES, map(float, scale))),
        }
    passed = bool(checks) and all(checks.values())
    payload = {
        "test": "SCI-A2K4-C7G467-K7D-INTEGRATED-INPUT-PACK",
        "execution_verdict": "PASS_K7D_INPUT_PACK" if passed else "REVIEW_K7D_INPUT_PACK",
        "physics_executed": False,
        "state_names": list(NAMES),
        "modes": packed_modes,
        "checks": checks,
        "hashes": {
            "runner_213_sha256": sha256_file(Path(__file__)),
            "source_178_sha256": sha256_file(SOURCE178),
            "source_146_sha256": sha256_file(SOURCE146),
            "source_209_sha256": sha256_file(SOURCE209),
            "preregistration_sha256": sha256_file(PREREG),
        },
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
    write_immutable(args.output, payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if passed else 2


def checkpoint_grid(x_start: float) -> np.ndarray:
    count = int(round((X_FINAL - x_start) / 0.25))
    grid = x_start + 0.25 * np.arange(count + 1, dtype=float)
    grid[-1] = X_FINAL
    return grid


def action_case(args: argparse.Namespace) -> int:
    started = time.monotonic()
    pack_path = args.input.resolve()
    pack = json.loads(pack_path.read_text(encoding="utf-8"))
    if pack.get("execution_verdict") != "PASS_K7D_INPUT_PACK":
        raise RuntimeError("input pack is not PASS")
    if list(pack.get("state_names", ())) != list(NAMES):
        raise RuntimeError("input pack state names/order changed")
    pack_hashes = dict(pack.get("hashes", {}))
    if pack_hashes.get("runner_213_sha256") != sha256_file(Path(__file__)):
        raise RuntimeError("input pack was produced by a different runner 213 hash")
    mode, surface, x_start = CASES[args.case]
    mode_pack = dict(dict(pack["modes"])[mode])
    seed_map = dict(dict(mode_pack["seeds"])[surface])
    scale_map = dict(mode_pack["scale"])
    if set(seed_map) != set(NAMES) or set(scale_map) != set(NAMES):
        raise RuntimeError("seed/scale keys changed")
    y0 = np.asarray([float(seed_map[name]) for name in NAMES], float)
    scale = np.asarray([float(scale_map[name]) for name in NAMES], float)
    w0 = y0 / scale
    rhs_calls = 0
    maximum_normalized_abs = float(np.max(np.abs(w0)))

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("K7d single-case internal deadline exceeded")

    def scaled_rhs(x: float, normalized: np.ndarray) -> np.ndarray:
        nonlocal rhs_calls, maximum_normalized_abs
        rhs_calls += 1
        if rhs_calls > RHS_CAP:
            raise TimeoutError("K7d RHS call cap exceeded")
        if rhs_calls % 64 == 0:
            deadline()
        if not np.all(np.isfinite(normalized)):
            raise FloatingPointError("non-finite normalized state")
        maximum_normalized_abs = max(maximum_normalized_abs, float(np.max(np.abs(normalized))))
        if maximum_normalized_abs > SAFETY_CAP:
            raise FloatingPointError("K7d normalized safety cap exceeded")
        return physical_rhs(x, normalized * scale) / scale

    grid = checkpoint_grid(x_start)
    solution = solve_ivp(
        scaled_rhs, (x_start, X_FINAL), w0, method="DOP853",
        rtol=RTOL, atol=ATOL, max_step=MAX_STEP, t_eval=grid,
    )
    deadline()
    if solution.y.shape != (len(NAMES), len(grid)):
        raise RuntimeError(f"unexpected solution shape: {solution.y.shape}")
    physical = np.asarray(solution.y, float) * scale[:, None]
    diagnostics = [
        checkpoint_diagnostics(float(x), physical[:, index], scale)
        for index, x in enumerate(grid)
    ]
    normalized_rhs_matrix = np.asarray([
        [float(dict(row["normalized_rhs"])[name]) for name in NAMES]
        for row in diagnostics
    ], float).T
    excursion = np.max(np.abs(physical - physical[:, [0]]) / scale[:, None], axis=1)
    rhs_activity = np.max(np.abs(normalized_rhs_matrix), axis=1)
    activity_pass = np.logical_or(excursion >= ACTIVITY_EXCURSION_MIN, rhs_activity >= ACTIVITY_RHS_MIN)
    activity = {
        name: {
            "normalized_excursion": float(excursion[index]),
            "normalized_rhs_max_abs": float(rhs_activity[index]),
            "pass": bool(activity_pass[index]),
        }
        for index, name in enumerate(NAMES)
    }
    max_parity = max(float(row["species_projected_parity_max_abs"]) for row in diagnostics)
    trace_pass = all(bool(dict(row["trace"])["pass"]) for row in diagnostics)
    traceless_pass = all(bool(dict(row["traceless"])["pass"]) for row in diagnostics)
    structural_checks = {
        "solver_success": bool(solution.success),
        "reached_exact_endpoint": bool(
            len(solution.t) == len(grid) and abs(float(solution.t[-1]) - X_FINAL) <= 1e-13
        ),
        "all_checkpoints_written": len(diagnostics) == len(grid),
        "finite_state_rhs_diagnostics": bool(
            np.all(np.isfinite(physical)) and all(bool(row["finite"]) for row in diagnostics)
        ),
        "normalized_safety_cap_respected": maximum_normalized_abs <= SAFETY_CAP,
        "rhs_call_cap_respected": rhs_calls <= RHS_CAP,
        "exact_13_state_names": len(NAMES) == 13 and len(set(NAMES)) == 13,
    }
    parity_checks = {"species_projected_parity_below_1e-10": max_parity <= PARITY_MAX}
    physical_checks = {
        "all_13_components_dynamically_resolved": bool(np.all(activity_pass)),
        "trace_all_checkpoints_within_mixed_allowance": trace_pass,
        "traceless_all_checkpoints_within_mixed_allowance": traceless_pass,
    }
    structural_pass = all(structural_checks.values())
    parity_pass = all(parity_checks.values())
    local_g4_pass = all(physical_checks.values())
    if not structural_pass or not parity_pass:
        verdict = "REVIEW_K7D_SINGLE_CASE_TECHNICAL"
    elif local_g4_pass:
        verdict = "PASS_K7D_SINGLE_CASE_G4_G6_LOCAL"
    else:
        verdict = "CANDIDATE_K7D_PHYSICAL_CONFLICT_CONFIRMATION_REQUIRED"
    payload = {
        "test": "SCI-A2K4-C7G467-K7D-INTEGRATED-SINGLE-CASE",
        "case": args.case,
        "mode": mode,
        "surface": surface,
        "execution_verdict": verdict,
        "physics_executed": True,
        "profile": {"x_start": x_start, "x_final": X_FINAL, "checkpoint_step": 0.25},
        "state_names": list(NAMES),
        "integration_scale": dict(zip(NAMES, map(float, scale))),
        "activity": activity,
        "checkpoints": diagnostics,
        "structural_checks": structural_checks,
        "parity_checks": parity_checks,
        "physical_checks": physical_checks,
        "max_species_projected_parity": max_parity,
        "solver": {
            "method": "DOP853", "rtol": RTOL, "atol": ATOL,
            "max_step": MAX_STEP, "success": bool(solution.success),
            "message": str(solution.message), "nfev": int(solution.nfev),
            "njev": int(getattr(solution, "njev", 0)),
            "nlu": int(getattr(solution, "nlu", 0)),
        },
        "rhs_calls_including_audit": rhs_calls,
        "maximum_normalized_abs": maximum_normalized_abs,
        "thresholds": {
            "activity_excursion_min": ACTIVITY_EXCURSION_MIN,
            "activity_rhs_min": ACTIVITY_RHS_MIN,
            "parity_max": PARITY_MAX,
            "constraint_abs": CONSTRAINT_ABS,
            "constraint_rel": CONSTRAINT_REL,
        },
        "hashes": {
            "runner_213_sha256": sha256_file(Path(__file__)),
            "input_pack_sha256": sha256_file(pack_path),
            "preregistration_sha256": sha256_file(PREREG),
        },
        "runtime_limits": {
            "seconds": args.max_runtime_seconds, "rhs_calls": RHS_CAP,
            "normalized_safety_cap": SAFETY_CAP,
        },
        "runtime_seconds": time.monotonic() - started,
        "scope_limit": "L5=0 closure; no G8 hierarchy, CMB, S8, H0, or likelihood claim",
    }
    write_immutable(args.output, payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if verdict.startswith("PASS_") else 2


def action_aggregate(args: argparse.Namespace) -> int:
    started = time.monotonic()
    payloads: dict[str, dict[str, object]] = {}
    hashes: dict[str, str] = {}
    for path in args.inputs:
        resolved = path.resolve()
        payload = json.loads(resolved.read_text(encoding="utf-8"))
        case = str(payload.get("case", ""))
        if case not in CASES or case in payloads:
            raise RuntimeError(f"invalid or duplicate case: {case}")
        if payload.get("test") != "SCI-A2K4-C7G467-K7D-INTEGRATED-SINGLE-CASE":
            raise RuntimeError(f"wrong input test: {resolved}")
        payloads[case] = payload
        hashes[case] = sha256_file(resolved)
    if set(payloads) != set(CASES):
        raise RuntimeError("aggregate requires exactly four registered cases")
    runner_hashes = {dict(payload["hashes"])["runner_213_sha256"] for payload in payloads.values()}
    input_hashes = {dict(payload["hashes"])["input_pack_sha256"] for payload in payloads.values()}
    prereg_hashes = {dict(payload["hashes"])["preregistration_sha256"] for payload in payloads.values()}
    provenance_pass = len(runner_hashes) == len(input_hashes) == len(prereg_hashes) == 1
    structural_pass = all(all(dict(payload["structural_checks"]).values()) for payload in payloads.values())
    parity_pass = all(all(dict(payload["parity_checks"]).values()) for payload in payloads.values())
    g4_pass = all(all(dict(payload["physical_checks"]).values()) for payload in payloads.values())

    agreement: dict[str, object] = {}
    g7_pass = True
    for mode in ("NID", "NIV"):
        deep = payloads[f"{mode}_DEEP"]
        shallow = payloads[f"{mode}_SHALLOW"]
        deep_rows = {float(row["x"]): row for row in deep["checkpoints"]}
        shallow_rows = {float(row["x"]): row for row in shallow["checkpoints"]}
        common = sorted(set(deep_rows).intersection(shallow_rows))
        if not common or abs(common[0] + 23.0) > 1e-13 or abs(common[-1] - X_FINAL) > 1e-13:
            raise RuntimeError(f"{mode} common checkpoint interval changed")
        scale = np.asarray([float(dict(deep["integration_scale"])[name]) for name in NAMES], float)
        shallow_scale = np.asarray([float(dict(shallow["integration_scale"])[name]) for name in NAMES], float)
        if not np.array_equal(scale, shallow_scale):
            raise RuntimeError(f"{mode} deep/shallow scales differ")
        overlap_max = 0.0
        per_checkpoint: dict[str, float] = {}
        for x in common:
            yd = np.asarray([float(dict(deep_rows[x]["state"])[name]) for name in NAMES], float)
            ys = np.asarray([float(dict(shallow_rows[x]["state"])[name]) for name in NAMES], float)
            value = float(np.max(np.abs(yd - ys) / scale))
            per_checkpoint[f"{x:.2f}"] = value
            overlap_max = max(overlap_max, value)
        yd = np.asarray([float(dict(deep_rows[X_FINAL]["state"])[name]) for name in NAMES], float)
        ys = np.asarray([float(dict(shallow_rows[X_FINAL]["state"])[name]) for name in NAMES], float)
        endpoint_l2 = float(np.linalg.norm(yd - ys) / max(np.linalg.norm(yd), np.linalg.norm(ys), 1e-300))
        endpoint_envelope = float(np.max(np.abs(yd - ys) / scale))
        checks = {
            "endpoint_l2_below_3e-3": endpoint_l2 <= ENDPOINT_L2_MAX,
            "endpoint_envelope_below_1e-2": endpoint_envelope <= ENDPOINT_ENVELOPE_MAX,
            "overlap_envelope_below_2e-2": overlap_max <= OVERLAP_ENVELOPE_MAX,
        }
        g7_pass = g7_pass and all(checks.values())
        agreement[mode] = {
            "endpoint_l2_relative": endpoint_l2,
            "endpoint_envelope_scaled_max": endpoint_envelope,
            "overlap_envelope_scaled_max": overlap_max,
            "per_checkpoint_envelope_scaled_max": per_checkpoint,
            "checks": checks,
        }
    g6_pass = structural_pass and provenance_pass
    if not provenance_pass or not structural_pass or not parity_pass:
        verdict = "REVIEW_K7D_INTEGRATED_TECHNICAL"
    elif g4_pass and g6_pass and g7_pass:
        verdict = "PASS_K7D_C7_G4_G6_G7_INTEGRATED"
    else:
        verdict = "CANDIDATE_K7D_PHYSICAL_CONFLICT_CONFIRMATION_REQUIRED"
    result = {
        "test": "SCI-A2K4-C7G467-K7D-INTEGRATED-AGGREGATE",
        "execution_verdict": verdict,
        "gate_verdicts": {
            "C7-G4": "PASS" if g4_pass and parity_pass else ("REVIEW_TECHNICAL" if not parity_pass else "CONFIRMATION_REQUIRED"),
            "C7-G6": "PASS" if g6_pass else "REVIEW_TECHNICAL",
            "C7-G7": "PASS" if g7_pass else "CONFIRMATION_REQUIRED",
        },
        "checks": {
            "four_unique_registered_cases": set(payloads) == set(CASES),
            "common_provenance": provenance_pass,
            "all_structural": structural_pass,
            "all_species_projected_parity": parity_pass,
            "all_local_G4": g4_pass,
            "deep_shallow_G7": g7_pass,
        },
        "agreement": agreement,
        "case_verdicts": {case: payload["execution_verdict"] for case, payload in payloads.items()},
        "input_sha256": hashes,
        "hashes": {
            "runner_213_sha256": sha256_file(Path(__file__)),
            "preregistration_sha256": sha256_file(PREREG),
        },
        "runtime_seconds": time.monotonic() - started,
        "decision_rule": "a non-PASS physical metric is confirmation-required, never an immediate death verdict",
        "scope_limit": "L5=0 closure; no G8 hierarchy, CMB, S8, H0, or likelihood claim",
    }
    write_immutable(args.output, result)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if verdict.startswith("PASS_") else 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="A2-K4 K7d integrated G4/G6/G7 runner")
    sub = parser.add_subparsers(dest="action", required=True)
    prepare = sub.add_parser("prepare", help="create immutable seed/envelope input pack")
    prepare.add_argument("--max-runtime-seconds", type=float, required=True)
    prepare.add_argument("--output", type=Path, required=True)
    case = sub.add_parser("case", help="run exactly one registered trajectory")
    case.add_argument("--case", choices=tuple(CASES), required=True)
    case.add_argument("--input", type=Path, required=True)
    case.add_argument("--max-runtime-seconds", type=float, required=True)
    case.add_argument("--output", type=Path, required=True)
    aggregate = sub.add_parser("aggregate", help="offline aggregate four immutable cases")
    aggregate.add_argument("--inputs", type=Path, nargs=4, required=True)
    aggregate.add_argument("--output", type=Path, required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.action == "prepare":
        if not 15 <= args.max_runtime_seconds <= 20:
            raise ValueError("prepare max-runtime-seconds must be in [15,20]")
        return action_prepare(args)
    if args.action == "case":
        if not 10 <= args.max_runtime_seconds <= 25:
            raise ValueError("case max-runtime-seconds must be in [10,25]")
        return action_case(args)
    return action_aggregate(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.TimeoutExpired as exc:
        print(json.dumps({"execution_verdict": "TIMEOUT_UNCLOSED", "error": repr(exc)}, indent=2))
        raise SystemExit(124)
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}, indent=2))
        raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution_verdict": "ERROR_UNCLOSED", "error": repr(exc)}, indent=2))
        raise SystemExit(1)

