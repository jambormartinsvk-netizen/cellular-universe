#!/usr/bin/env python3
"""Offline V1 correction of K7d species/projected and Einstein diagnostics."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time

import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
BASE = HERE / "213_script_A2_K4_C7_7c_K7d_integrated_G4_G6_G7_runner.py"
PREREG = ROOT / "Questions" / (
    "A2_K4_C7_7C_K7D_V1_DIAGNOSTIC_CORRECTION_PREREGISTRATION_2026-07-15.md"
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def load_base():
    spec = importlib.util.spec_from_file_location("k7d_base_213", BASE)
    if spec is None or spec.loader is None:
        raise ImportError(BASE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def corrected_species_projected(base, x: float, state: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    species = base.projected_to_species(x, state)
    h, eta, dg, dn, db, dc, Ug, Un, sig, L3, L4, df, Uf = species
    D, M = float(state[3]), float(state[7])
    b = base.background(x)
    hx = 3.0 * D + 2.0 * b["s2"] * eta
    eta_x = M
    d = base.DELTA
    srhs = np.asarray([
        hx,
        eta_x,
        -4.0 / 3.0 * b["s2"] * Ug - 2.0 / 3.0 * hx,
        -4.0 / 3.0 * b["s2"] * Un - 2.0 / 3.0 * hx,
        -b["s2"] * Ug - hx / 2.0,
        -hx / 2.0 + b["gr"] * (df - dc),
        b["q"] * Ug - b["load_fraction"] * Ug + 0.25 * b["inv1r"] * dg,
        b["q"] * Un + 0.25 * dn - sig,
        2.0 / 15.0 * hx + 4.0 / 5.0 * eta_x
            + 4.0 / 15.0 * b["s2"] * Un - 3.0 / 10.0 * L3,
        -b["q"] * L3 + 6.0 / 7.0 * b["s2"] * sig - 4.0 / 7.0 * L4,
        -2.0 * b["q"] * L4 + 4.0 / 9.0 * b["s2"] * L3,
        -3.0 * (2.0 - d) * df - d * b["s2"] * Uf - d * hx / 2.0
            - 9.0 * d * (2.0 - d) * Uf - 3.0 * (2.0 - d) * b["g"] * Uf,
        (b["q"] + 2.0) * Uf + df / d + 2.0 * b["g"] * Uf / d,
    ], float)
    Ogx, Onx = -b["ell"] * b["Og"], -b["ell"] * b["On"]
    Obx = (1.0 - b["ell"]) * b["Ob"]
    Ocx = (b["beta_c"] - b["ell"]) * b["Oc"]
    Ofx = (b["beta_f"] - b["ell"]) * b["Of"]
    D_x = math.fsum((
        Ogx * dg + b["Og"] * srhs[2],
        Onx * dn + b["On"] * srhs[3],
        Obx * db + b["Ob"] * srhs[4],
        Ocx * dc + b["Oc"] * srhs[5],
        Ofx * df + b["Of"] * srhs[11],
    ))
    Wg, Wgx = 2.0 * b["Og"] + 1.5 * b["Ob"], 2.0 * Ogx + 1.5 * Obx
    Wf, Wfx = 1.5 * d * b["Of"], 1.5 * d * Ofx
    M_x = math.fsum((
        Wgx * Ug + Wg * srhs[6],
        2.0 * Onx * Un + 2.0 * b["On"] * srhs[7],
        Wfx * Uf + Wf * srhs[12],
    ))
    projected = np.asarray([
        srhs[0], srhs[1], srhs[2], D_x, srhs[4], srhs[5], srhs[6], M_x,
        srhs[8], srhs[9], srhs[10], srhs[11], srhs[12],
    ], float)
    return species, projected


def ledger(base, terms: tuple[float, ...]) -> dict[str, object]:
    residual = abs(math.fsum(terms))
    norm = math.fsum(abs(value) for value in terms)
    allowance = base.CONSTRAINT_ABS + base.CONSTRAINT_REL * norm
    return {
        "terms": list(map(float, terms)),
        "absolute_residual": float(residual),
        "term_norm": float(norm),
        "relative_residual": float(residual / max(norm, 1e-300)),
        "allowance": float(allowance),
        "pass": bool(residual <= allowance),
    }


def corrected_checkpoint(base, row: dict[str, object], scale: np.ndarray) -> dict[str, object]:
    x = float(row["x"])
    state = np.asarray([float(dict(row["state"])[name]) for name in base.NAMES], float)
    rhs = base.physical_rhs(x, state)
    species, species_projected = corrected_species_projected(base, x, state)
    b = base.background(x)
    h, eta, dg, D, db, dc, Ug, M, sig, L3, L4, df, Uf = state
    dn, Un = float(species[3]), float(species[7])
    hx, D_x, M_x = float(rhs[0]), float(rhs[3]), float(rhs[7])
    hx_x = 3.0 * D_x - 4.0 * b["q"] * b["s2"] * eta + 2.0 * b["s2"] * M
    pressure = (
        b["Of"] * (df + (2.0 - base.DELTA) * (3.0 * base.DELTA + b["g"]) * Uf)
        + (b["Og"] * dg + b["On"] * dn) / 3.0
    )
    shear = 2.0 / 3.0 * b["On"] * sig
    trace = ledger(base, (
        hx_x, (b["q"] + 2.0) * hx, -2.0 * b["s2"] * eta, 9.0 * pressure,
    ))
    traceless = ledger(base, (
        hx_x, 6.0 * M_x, (b["q"] + 2.0) * (hx + 6.0 * M),
        -2.0 * b["s2"] * eta, 9.0 * shear,
    ))
    parity = (rhs - species_projected) / scale
    corrected = dict(row)
    corrected.update({
        "trace": trace,
        "traceless": traceless,
        "species_projected_parity_max_abs": float(np.max(np.abs(parity))),
        "species_projected_parity_vector": dict(zip(base.NAMES, map(float, parity))),
        "v1_diagnostic_source": "215 corrected state/RHS typing and authoritative projected D,M",
    })
    return corrected


def main() -> int:
    parser = argparse.ArgumentParser(description="Offline K7d V1 diagnostic correction")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-runtime-seconds", type=float, required=True)
    args = parser.parse_args()
    if not 2 <= args.max_runtime_seconds <= 10:
        parser.error("max-runtime-seconds must be in [2,10]")
    started = time.monotonic()
    base = load_base()
    source_path = args.input.resolve()
    payload = json.loads(source_path.read_text(encoding="utf-8"))
    if payload.get("test") != "SCI-A2K4-C7G467-K7D-INTEGRATED-SINGLE-CASE":
        raise RuntimeError("input is not a K7d single-case raw JSON")
    if list(payload.get("state_names", ())) != list(base.NAMES):
        raise RuntimeError("state names/order changed")
    if dict(payload.get("hashes", {})).get("runner_213_sha256") != sha256_file(BASE):
        raise RuntimeError("raw JSON runner hash does not match current 213")
    scale = np.asarray([
        float(dict(payload["integration_scale"])[name]) for name in base.NAMES
    ], float)
    rows = [corrected_checkpoint(base, dict(row), scale) for row in payload["checkpoints"]]
    if time.monotonic() - started > args.max_runtime_seconds:
        raise TimeoutError("K7d V1 offline correction deadline exceeded")
    max_parity = max(float(row["species_projected_parity_max_abs"]) for row in rows)
    trace_pass = all(bool(dict(row["trace"])["pass"]) for row in rows)
    traceless_pass = all(bool(dict(row["traceless"])["pass"]) for row in rows)
    activity_pass = all(bool(item["pass"]) for item in dict(payload["activity"]).values())
    structural_pass = all(bool(value) for value in dict(payload["structural_checks"]).values())
    parity_pass = max_parity <= base.PARITY_MAX
    physical_checks = {
        "all_13_components_dynamically_resolved": activity_pass,
        "trace_all_checkpoints_within_mixed_allowance": trace_pass,
        "traceless_all_checkpoints_within_mixed_allowance": traceless_pass,
    }
    if not structural_pass or not parity_pass:
        verdict = "REVIEW_K7D_SINGLE_CASE_TECHNICAL"
    elif all(physical_checks.values()):
        verdict = "PASS_K7D_SINGLE_CASE_G4_G6_LOCAL"
    else:
        verdict = "CANDIDATE_K7D_PHYSICAL_CONFLICT_CONFIRMATION_REQUIRED"
    corrected = dict(payload)
    corrected.update({
        "execution_verdict": verdict,
        "checkpoints": rows,
        "parity_checks": {"species_projected_parity_below_1e-10": parity_pass},
        "physical_checks": physical_checks,
        "max_species_projected_parity": max_parity,
        "v1_correction": {
            "raw_input_sha256": sha256_file(source_path),
            "corrector_215_sha256": sha256_file(Path(__file__)),
            "preregistration_sha256": sha256_file(PREREG),
            "physics_or_threshold_change": False,
            "ode_rerun": False,
            "reason": "FE-K7D-01 and FE-K7D-02",
        },
        "runtime_seconds_v1_offline": time.monotonic() - started,
    })
    corrected_hashes = dict(corrected.get("hashes", {}))
    corrected_hashes.update({
        "raw_213_sha256": sha256_file(source_path),
        "corrector_215_sha256": sha256_file(Path(__file__)),
        "v1_preregistration_sha256": sha256_file(PREREG),
    })
    corrected["hashes"] = corrected_hashes
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f"authoritative output overwrite refused: {output}")
    if not output.parent.is_dir():
        raise FileNotFoundError(f"output parent missing: {output.parent}")
    with output.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(corrected, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "execution_verdict": verdict,
        "case": payload["case"],
        "max_species_projected_parity": max_parity,
        "physical_checks": physical_checks,
        "raw_input_sha256": sha256_file(source_path),
        "corrector_215_sha256": sha256_file(Path(__file__)),
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

