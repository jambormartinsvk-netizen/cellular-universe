#!/usr/bin/env python3
"""P3a-A exact-zero coefficient audit. No ODE is imported or executed."""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import time
from typing import Any

import mpmath as mp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOURCE_199 = HERE / "199_script_A2_K4_C7_7c_K7c_P2_Mprime_term_ledger.py"
P2_RAW = ROOT / "Audit" / "A2_K4_K7C_P2_MLEDGER_RAW_2026-07-15.json"
DEFAULT_OUTPUT = ROOT / "Audit" / "A2_K4_K7C_P3A_ZERO_IDENTITY_RAW_2026-07-15.json"

EXPECTED_SOURCE_199_SHA256 = (
    "911F7DDBDC6B41C019CD041FC024A2B8FAF9CF2A27A1F35686ECB6649BAD8DF9"
)
EXPECTED_P2_RAW_SHA256 = (
    "C268A63CE34888744E48A8BD784651C75B243B25705E74C301299DA69499FA5C"
)
EXPECTED_P2_VERDICT = "STOP_P2_SIMPLE_FSUM_EXPLANATION_IN_THIS_SCOPE"
EXPECTED_P2_TEST = "SCI-A2K4-C7G5-K7C-P2-MLEDGER"
TEST_ID = "SCI-A2K4-C7G5-K7C-P3A-ZERO-IDENTITY"
PASS_VERDICT = "PASS_P3A_EXACT_ZERO_IDENTITY"
FAIL_VERDICT = "STOP_P3A_EXACT_ZERO_IDENTITY_FAILED"
EXPECTED_X = (-25.0, -24.875, -24.75, -23.0)
HP_DPS = 80
HP_NORMALIZED_LIMIT = mp.mpf("1e-70")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def canonical_payload_sha256(payload: dict[str, Any]) -> str:
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest().upper()


def mp_record(value: mp.mpf) -> dict[str, object]:
    return {"decimal": mp.nstr(value, 82), "float": float(value)}


def normalized_residual(residual: mp.mpf, *terms: mp.mpf) -> mp.mpf:
    scale = max(*(abs(term) for term in terms), mp.mpf("1e-300"))
    return abs(residual) / scale


def exact_fraction_audit() -> dict[str, object]:
    # From R=(3/4)*(Omega_b/Omega_gamma):
    ratio_residual = Fraction(1, 1) - Fraction(4, 3) * Fraction(3, 4)

    # With Omega_b=(4/3) R Omega_gamma:
    w_constant_residual = Fraction(2, 1) - Fraction(2, 1)
    w_R_residual = Fraction(3, 2) * Fraction(4, 3) - Fraction(2, 1)

    # After cancelling the common nonzero (1+R) factor:
    c_u_R_residual = (
        Fraction(3, 2) * Fraction(4, 3) - Fraction(2, 1)
    )
    c_delta_residual = Fraction(1, 4) * Fraction(2, 1) - Fraction(1, 2)

    values = {
        "Omega_b_over_Omega_gamma_minus_4R_over_3": ratio_residual,
        "W_gamma_constant_coefficient_residual": w_constant_residual,
        "W_gamma_R_coefficient_residual": w_R_residual,
        "c_U_R_coefficient_residual": c_u_R_residual,
        "c_delta_coefficient_residual": c_delta_residual,
    }
    serialized = {
        name: {
            "numerator": value.numerator,
            "denominator": value.denominator,
            "is_exact_zero": value == 0,
        }
        for name, value in values.items()
    }
    return {
        "derivation": [
            "R=(3/4)*(Omega_b/Omega_gamma)",
            "Omega_b=(4/3)*R*Omega_gamma",
            "W_gamma=2*Omega_gamma+(3/2)*Omega_b=2*Omega_gamma*(1+R)",
            "c_U=(3/2)*Omega_b-W_gamma*R/(1+R)=0",
            "c_delta=W_gamma/[4*(1+R)]-Omega_gamma/2=0",
        ],
        "residuals": serialized,
        "all_exact_zero": all(value == 0 for value in values.values()),
    }


def background_float(x: float) -> dict[str, float]:
    p = 3.93109
    h0 = 0.6637
    omega_m0 = 0.3517
    ombh2 = 0.02237
    fb = ombh2 / (omega_m0 * h0**2)
    neff = 3.046 + 0.0535
    rn = 0.2271 * neff / (1 + 0.2271 * neff)
    rg = 1 - rn
    omega_r0 = 2.47282e-5 * (1 + 0.2271 * neff) / h0**2
    hubble0_mpc = 100 * h0 / 299792.458
    k_mpc = 0.05
    mu = hubble0_mpc * omega_m0 / math.sqrt(omega_r0) / k_mpc
    g2 = 0.15 * (hubble0_mpc / k_mpc) ** 2 * math.sqrt(omega_r0)
    transfer_shape = g2 * (1 / (p + 1) - 0.5)
    z = k_mpc * math.exp(x) / (hubble0_mpc * math.sqrt(omega_r0))
    fuel_piece = z**p
    denominator = 1 + mu * z + fuel_piece * (1 + transfer_shape * z**2)
    Og = rg / denominator
    Ob = fb * mu * z / denominator
    R = 3 * fb * mu * z / (4 * rg)
    Wg = 2 * Og + 1.5 * Ob
    return {"Og": Og, "Ob": Ob, "R": R, "Wg": Wg}


def background_mp(x: mp.mpf) -> dict[str, mp.mpf]:
    p = mp.mpf("3.93109")
    h0 = mp.mpf("0.6637")
    omega_m0 = mp.mpf("0.3517")
    ombh2 = mp.mpf("0.02237")
    fb = ombh2 / (omega_m0 * h0**2)
    neff = mp.mpf("3.046") + mp.mpf("0.0535")
    rn = mp.mpf("0.2271") * neff / (1 + mp.mpf("0.2271") * neff)
    rg = 1 - rn
    omega_r0 = (
        mp.mpf("2.47282e-5") * (1 + mp.mpf("0.2271") * neff) / h0**2
    )
    hubble0_mpc = 100 * h0 / mp.mpf("299792.458")
    k_mpc = mp.mpf("0.05")
    mu = hubble0_mpc * omega_m0 / mp.sqrt(omega_r0) / k_mpc
    g2 = mp.mpf("0.15") * (hubble0_mpc / k_mpc) ** 2 * mp.sqrt(omega_r0)
    transfer_shape = g2 * (1 / (p + 1) - mp.mpf("0.5"))
    z = k_mpc * mp.exp(x) / (hubble0_mpc * mp.sqrt(omega_r0))
    fuel_piece = z**p
    denominator = 1 + mu * z + fuel_piece * (1 + transfer_shape * z**2)
    Og = rg / denominator
    Ob = fb * mu * z / denominator
    R = 3 * fb * mu * z / (4 * rg)
    Wg = 2 * Og + mp.mpf("1.5") * Ob
    return {"Og": Og, "Ob": Ob, "R": R, "Wg": Wg}


def surface_audit(x: float) -> dict[str, object]:
    bf = background_float(x)
    inv1r_f = 1.0 / (1.0 + bf["R"])
    c_u_f = 1.5 * bf["Ob"] - bf["Wg"] * bf["R"] * inv1r_f
    c_delta_f = 0.25 * bf["Wg"] * inv1r_f - 0.5 * bf["Og"]

    bm = background_mp(mp.mpf(repr(x)))
    inv1r_m = 1 / (1 + bm["R"])
    ratio_left = bm["Ob"] / bm["Og"]
    ratio_right = mp.mpf(4) * bm["R"] / 3
    w_right = 2 * bm["Og"] * (1 + bm["R"])
    c_u_left = mp.mpf("1.5") * bm["Ob"]
    c_u_right = bm["Wg"] * bm["R"] * inv1r_m
    c_delta_left = mp.mpf("0.25") * bm["Wg"] * inv1r_m
    c_delta_right = mp.mpf("0.5") * bm["Og"]

    residuals = {
        "ratio": normalized_residual(
            ratio_left - ratio_right, ratio_left, ratio_right
        ),
        "W_gamma": normalized_residual(
            bm["Wg"] - w_right, bm["Wg"], w_right
        ),
        "c_U": normalized_residual(
            c_u_left - c_u_right, c_u_left, c_u_right
        ),
        "c_delta": normalized_residual(
            c_delta_left - c_delta_right, c_delta_left, c_delta_right
        ),
    }
    finite = all(mp.isfinite(value) for value in bm.values())
    checks = {
        "background_finite": bool(finite),
        "all_hp_normalized_residuals_le_1e_minus_70": all(
            value <= HP_NORMALIZED_LIMIT for value in residuals.values()
        ),
    }
    return {
        "x": x,
        "float64": {
            "Omega_gamma": bf["Og"],
            "Omega_b": bf["Ob"],
            "R": bf["R"],
            "W_gamma": bf["Wg"],
            "c_U_original_form": c_u_f,
            "c_delta_original_form": c_delta_f,
            "c_U_exact_identity_form": 0.0,
            "c_delta_exact_identity_form": 0.0,
        },
        "hp_80dps_normalized_residuals": {
            name: mp_record(value) for name, value in residuals.items()
        },
        "checks": checks,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="P3a-A exact-zero coefficient audit; no ODE"
    )
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument(
        "--smoke",
        action="store_true",
        help="parse and report metadata only; execute no physics",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.smoke:
        print(
            json.dumps(
                {
                    "test": TEST_ID,
                    "smoke": True,
                    "physics_executed": False,
                    "new_ODE_executed": False,
                    "expected_surface_count": len(EXPECTED_X),
                },
                sort_keys=True,
            )
        )
        return 0

    if not (0 < args.max_runtime_seconds <= 5.0):
        raise ValueError("--max-runtime-seconds must be in (0, 5]")
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing output: {output}")

    started = time.monotonic()
    actual_source_hash = sha256_file(SOURCE_199)
    actual_raw_hash = sha256_file(P2_RAW)
    with P2_RAW.open("r", encoding="utf-8") as handle:
        p2 = json.load(handle)

    provenance_checks = {
        "script_199_hash_exact": actual_source_hash
        == EXPECTED_SOURCE_199_SHA256,
        "P2_raw_hash_exact": actual_raw_hash == EXPECTED_P2_RAW_SHA256,
        "P2_test_exact": p2.get("test") == EXPECTED_P2_TEST,
        "P2_verdict_exact": p2.get("execution_verdict")
        == EXPECTED_P2_VERDICT,
        "P2_new_ODE_false": p2.get("new_ODE_executed") is False,
    }
    mp.mp.dps = HP_DPS
    exact = exact_fraction_audit()
    surfaces = []
    for x in EXPECTED_X:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("P3a-A internal deadline exceeded")
        surfaces.append(surface_audit(x))

    checks = {
        "all_provenance_checks_pass": all(provenance_checks.values()),
        "all_exact_fraction_residuals_zero": bool(exact["all_exact_zero"]),
        "surface_set_exact": tuple(item["x"] for item in surfaces) == EXPECTED_X,
        "all_surfaces_finite": all(
            item["checks"]["background_finite"] for item in surfaces
        ),
        "all_hp_residuals_within_preregistered_limit": all(
            item["checks"]["all_hp_normalized_residuals_le_1e_minus_70"]
            for item in surfaces
        ),
        "no_ODE_executed": True,
    }
    passed = all(checks.values())
    runtime = time.monotonic() - started
    if runtime > args.max_runtime_seconds:
        raise TimeoutError("P3a-A internal deadline exceeded after audit")

    payload: dict[str, Any] = {
        "test": TEST_ID,
        "execution_verdict": PASS_VERDICT if passed else FAIL_VERDICT,
        "physical_verdict": (
            "exact-zero coefficient identity verified; P3a-B may be prepared"
            if passed
            else "exact-zero coefficient identity failed; algebraic P3a track stops"
        ),
        "fine_depth": "66.5/100",
        "score_effect": "NONE",
        "physics_executed": True,
        "new_ODE_executed": False,
        "hp_dps": HP_DPS,
        "hp_normalized_limit": "1e-70",
        "expected_x": list(EXPECTED_X),
        "provenance": {
            "script_199": str(SOURCE_199),
            "script_199_sha256": actual_source_hash,
            "P2_raw": str(P2_RAW),
            "P2_raw_sha256": actual_raw_hash,
        },
        "provenance_checks": provenance_checks,
        "exact_fraction_audit": exact,
        "surface_audits": surfaces,
        "checks": checks,
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": runtime,
        "scope_limit": (
            "registered background identities at four surfaces only; "
            "no ODE, no RK4 rerun, no CMB/S8 claim"
        ),
        "next_step": (
            "prepare separately preregistered P3a-B RK4 rerun"
            if passed
            else "close P3a algebraic track and retain evidence"
        ),
    }
    payload["payload_sha256_without_self"] = canonical_payload_sha256(payload)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True, ensure_ascii=False)
        handle.write("\n")
    print(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
