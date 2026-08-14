#!/usr/bin/env python3
"""Final offline V2: 80-dps D/M parity and K7 sigma convention."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

import mpmath as mp
import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
BASE_PATH = HERE / "213_script_A2_K4_C7_7c_K7d_integrated_G4_G6_G7_runner.py"
V1_PATH = HERE / "215_script_A2_K4_C7_7c_K7d_V1_offline_diagnostic_correction.py"
PREREG = ROOT / "Questions" / (
    "A2_K4_C7_7C_K7D_V2_HIGH_PRECISION_PARITY_AND_SHEAR_CONVENTION_PREREGISTRATION_2026-07-15.md"
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def m(value: float | str) -> mp.mpf:
    return mp.mpf(value if isinstance(value, str) else repr(float(value)))


def hp_background(x_value: float) -> dict[str, mp.mpf]:
    x = m(x_value)
    delta, p, h0, om0, obh2 = m("0.02297"), m("3.93109"), m("0.6637"), m("0.3517"), m("0.02237")
    fb = obh2 / (om0 * h0**2)
    fc = 1 - fb
    neff = m("3.046") + m("0.0535")
    rn = m("0.2271") * neff / (1 + m("0.2271") * neff)
    rg = 1 - rn
    or0 = m("2.47282e-5") * (1 + m("0.2271") * neff) / h0**2
    H0m = 100 * h0 / m("299792.458")
    k = m("0.05")
    mu = H0m * om0 / mp.sqrt(or0) / k
    g2 = m("0.15") * (H0m / k) ** 2 * mp.sqrt(or0)
    shape = g2 * (1 / (p + 1) - mp.mpf("0.5"))
    z = k * mp.exp(x) / (H0m * mp.sqrt(or0))
    fuel = z**p
    den = 1 + mu * z + fuel * (1 + shape * z**2)
    denx = mu * z + fuel * (p + (p + 2) * shape * z**2)
    ell = denx / den
    Og, On = rg / den, rn / den
    Ob = fb * mu * z / den
    Oc = (fc * mu * z + g2 * z ** (p + 2) / (p + 1)) / den
    Of = fuel * (1 - g2 * z**2 / 2) / den
    loading = 3 * fb * mu * z / (4 * rg)
    g = g2 * z**2
    gr = g2 / (fc * mu) * z ** (p + 1)
    cn = fc * mu * z + g2 * z ** (p + 2) / (p + 1)
    beta_c = (fc * mu * z + (p + 2) * g2 * z ** (p + 2) / (p + 1)) / cn
    beta_f = p - g / (1 - g / 2)
    return {
        "delta": delta, "ell": ell, "q": -1 + ell / 2, "s2": z**2 / den,
        "Og": Og, "On": On, "Ob": Ob, "Oc": Oc, "Of": Of,
        "load": loading / (1 + loading), "inv1r": 1 / (1 + loading),
        "g": g, "gr": gr, "beta_c": beta_c, "beta_f": beta_f,
    }


def hp_dm_and_ledgers(base, x: float, state: np.ndarray, scale: np.ndarray):
    b = hp_background(x)
    y = list(map(m, state))
    h, eta, dg, D, db, dc, Ug, M, sig, L3, L4, df, Uf = y
    d = b["delta"]
    Wg, Wf = 2 * b["Og"] + mp.mpf("1.5") * b["Ob"], mp.mpf("1.5") * d * b["Of"]
    dn = (D - b["Og"] * dg - b["Ob"] * db - b["Oc"] * dc - b["Of"] * df) / b["On"]
    Un = (M - Wg * Ug - Wf * Uf) / (2 * b["On"])
    hx = 3 * D + 2 * b["s2"] * eta
    srhs = [
        hx, M,
        -mp.mpf(4) / 3 * b["s2"] * Ug - mp.mpf(2) / 3 * hx,
        -mp.mpf(4) / 3 * b["s2"] * Un - mp.mpf(2) / 3 * hx,
        -b["s2"] * Ug - hx / 2,
        -hx / 2 + b["gr"] * (df - dc),
        b["q"] * Ug - b["load"] * Ug + b["inv1r"] * dg / 4,
        b["q"] * Un + dn / 4 - sig,
        mp.mpf(2) / 15 * hx + mp.mpf(4) / 5 * M + mp.mpf(4) / 15 * b["s2"] * Un - mp.mpf(3) / 10 * L3,
        -b["q"] * L3 + mp.mpf(6) / 7 * b["s2"] * sig - mp.mpf(4) / 7 * L4,
        -2 * b["q"] * L4 + mp.mpf(4) / 9 * b["s2"] * L3,
        -3 * (2 - d) * df - d * b["s2"] * Uf - d * hx / 2
            - 9 * d * (2 - d) * Uf - 3 * (2 - d) * b["g"] * Uf,
        (b["q"] + 2) * Uf + df / d + 2 * b["g"] * Uf / d,
    ]
    Ogx, Onx = -b["ell"] * b["Og"], -b["ell"] * b["On"]
    Obx, Ocx, Ofx = (1 - b["ell"]) * b["Ob"], (b["beta_c"] - b["ell"]) * b["Oc"], (b["beta_f"] - b["ell"]) * b["Of"]
    D_product = mp.fsum([
        Ogx * dg + b["Og"] * srhs[2], Onx * dn + b["On"] * srhs[3],
        Obx * db + b["Ob"] * srhs[4], Ocx * dc + b["Oc"] * srhs[5],
        Ofx * df + b["Of"] * srhs[11],
    ])
    Wgx, Wfx = 2 * Ogx + mp.mpf("1.5") * Obx, mp.mpf("1.5") * d * Ofx
    M_product = mp.fsum([
        Wgx * Ug + Wg * srhs[6], 2 * Onx * Un + 2 * b["On"] * srhs[7],
        Wfx * Uf + Wf * srhs[12],
    ])
    Ah = mp.mpf(2) / 3 * (b["Og"] + b["On"]) + (b["Ob"] + b["Oc"]) / 2 + d * b["Of"] / 2
    D_projected = (
        -b["ell"] * D + b["Ob"] * db + b["beta_c"] * b["Oc"] * dc
        + b["beta_f"] * b["Of"] * df - mp.mpf(2) / 3 * b["s2"] * M - Ah * hx
        + b["Oc"] * b["gr"] * (df - dc)
        + b["Of"] * (-3 * (2 - d) * df - 9 * d * (2 - d) * Uf - 3 * (2 - d) * b["g"] * Uf)
    )
    M_projected = (
        (-b["q"] - 2) * M + D / 2 - b["Ob"] * db / 2 - b["Oc"] * dc / 2
        + b["Of"] * df - 2 * b["On"] * sig
        + (mp.mpf("1.5") * d * b["Of"] * (b["beta_f"] + 2) + 3 * b["Of"] * b["g"]) * Uf
    )
    parity_D = abs(D_projected - D_product) / m(scale[3])
    parity_M = abs(M_projected - M_product) / m(scale[7])
    hx_x = 3 * D_projected - 4 * b["q"] * b["s2"] * eta + 2 * b["s2"] * M
    pressure = b["Of"] * (df + (2 - d) * (3 * d + b["g"]) * Uf) + (b["Og"] * dg + b["On"] * dn) / 3
    shear = mp.mpf(4) / 3 * b["On"] * sig
    trace_terms = [hx_x, (b["q"] + 2) * hx, -2 * b["s2"] * eta, 9 * pressure]
    traceless_terms = [hx_x, 6 * M_projected, (b["q"] + 2) * (hx + 6 * M), -2 * b["s2"] * eta, 9 * shear]
    return float(parity_D), float(parity_M), trace_terms, traceless_terms


def ledger(base, terms) -> dict[str, object]:
    residual = abs(mp.fsum(terms))
    norm = mp.fsum(abs(value) for value in terms)
    allowance = mp.mpf(repr(base.CONSTRAINT_ABS)) + mp.mpf(repr(base.CONSTRAINT_REL)) * norm
    return {
        "terms": [float(value) for value in terms],
        "absolute_residual": float(residual), "term_norm": float(norm),
        "relative_residual": float(residual / max(norm, mp.mpf("1e-300"))),
        "allowance": float(allowance), "pass": bool(residual <= allowance),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="K7d final offline V2 HP correction")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-runtime-seconds", type=float, required=True)
    args = parser.parse_args()
    if not 2 <= args.max_runtime_seconds <= 10:
        parser.error("max-runtime-seconds must be in [2,10]")
    started = time.monotonic()
    mp.mp.dps = 80
    base = load("k7d_base_213_v2", BASE_PATH)
    v1 = load("k7d_v1_215", V1_PATH)
    source = args.input.resolve()
    payload = json.loads(source.read_text(encoding="utf-8"))
    if payload.get("test") != "SCI-A2K4-C7G467-K7D-INTEGRATED-SINGLE-CASE":
        raise RuntimeError("input is not a K7d raw single case")
    if dict(payload.get("hashes", {})).get("runner_213_sha256") != sha256_file(BASE_PATH):
        raise RuntimeError("runner hash mismatch")
    scale = np.asarray([float(dict(payload["integration_scale"])[name]) for name in base.NAMES], float)
    rows = []
    max_parity = 0.0
    for raw_row in payload["checkpoints"]:
        row = dict(raw_row)
        x = float(row["x"])
        state = np.asarray([float(dict(row["state"])[name]) for name in base.NAMES], float)
        _, v1_projected = v1.corrected_species_projected(base, x, state)
        vector = (base.physical_rhs(x, state) - v1_projected) / scale
        pD, pM, trace_terms, traceless_terms = hp_dm_and_ledgers(base, x, state, scale)
        vector[3] = pD
        vector[7] = pM
        max_parity = max(max_parity, float(np.max(np.abs(vector))))
        row.update({
            "trace": ledger(base, trace_terms), "traceless": ledger(base, traceless_terms),
            "species_projected_parity_max_abs": float(np.max(np.abs(vector))),
            "species_projected_parity_vector": dict(zip(base.NAMES, map(float, vector))),
            "v2_diagnostic_source": "216 80-dps D/M parity; S=(4/3)Omega_fs sigma_fs",
        })
        rows.append(row)
    if time.monotonic() - started > args.max_runtime_seconds:
        raise TimeoutError("K7d V2 deadline exceeded")
    trace_pass = all(bool(dict(row["trace"])["pass"]) for row in rows)
    traceless_pass = all(bool(dict(row["traceless"])["pass"]) for row in rows)
    parity_pass = max_parity <= base.PARITY_MAX
    activity_pass = all(bool(item["pass"]) for item in dict(payload["activity"]).values())
    structural_pass = all(bool(value) for value in dict(payload["structural_checks"]).values())
    physical_checks = {
        "all_13_components_dynamically_resolved": activity_pass,
        "trace_all_checkpoints_within_mixed_allowance": trace_pass,
        "traceless_all_checkpoints_within_mixed_allowance": traceless_pass,
    }
    if not structural_pass or not parity_pass:
        verdict = "REVIEW_BLOCKED_K7D_V2_TECHNICAL_BUDGET_EXHAUSTED"
    elif all(physical_checks.values()):
        verdict = "PASS_K7D_SINGLE_CASE_G4_G6_LOCAL"
    else:
        verdict = "CANDIDATE_K7D_PHYSICAL_CONFLICT_CONFIRMATION_REQUIRED"
    corrected = dict(payload)
    corrected.update({
        "execution_verdict": verdict, "checkpoints": rows,
        "parity_checks": {"species_projected_parity_below_1e-10": parity_pass},
        "physical_checks": physical_checks, "max_species_projected_parity": max_parity,
        "v2_correction": {
            "raw_input_sha256": sha256_file(source), "corrector_216_sha256": sha256_file(Path(__file__)),
            "preregistration_sha256": sha256_file(PREREG), "mp_dps": 80,
            "physics_or_threshold_change": False, "ode_rerun": False,
            "reason": "FE-K7D-03 and FE-K7D-04", "technical_budget_exhausted_after_this": True,
        },
        "runtime_seconds_v2_offline": time.monotonic() - started,
    })
    hashes = dict(corrected.get("hashes", {}))
    hashes.update({"raw_213_sha256": sha256_file(source), "corrector_216_sha256": sha256_file(Path(__file__)), "v2_preregistration_sha256": sha256_file(PREREG)})
    corrected["hashes"] = hashes
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f"authoritative output overwrite refused: {output}")
    if not output.parent.is_dir():
        raise FileNotFoundError(f"output parent missing: {output.parent}")
    with output.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(corrected, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "case": payload["case"], "execution_verdict": verdict,
        "max_species_projected_parity": max_parity, "physical_checks": physical_checks,
        "corrector_216_sha256": sha256_file(Path(__file__)),
        "runtime_seconds": time.monotonic() - started,
    }, indent=2, sort_keys=True))
    return 0 if verdict.startswith("PASS_") else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}, indent=2))
        raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution_verdict": "ERROR_UNCLOSED", "error": repr(exc)}, indent=2))
        raise SystemExit(1)

