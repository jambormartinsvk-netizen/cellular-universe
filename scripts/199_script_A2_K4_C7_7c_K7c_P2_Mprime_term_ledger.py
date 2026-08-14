#!/usr/bin/env python
"""Bounded, fail-closed M-prime term ledger for scientific K7c P2."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import time
from typing import Any

import mpmath as mp


HERE = Path(__file__).resolve().parent
SOURCE_185 = HERE / "185_script_A2_K4_C7_7c_K7c3c_second_fixed_RK4_refinement.py"
SOURCE_183 = HERE / "183_script_A2_K4_C7_7c_K7c3b_fixed_RK4_step_convergence.py"
SOURCE_179 = HERE / "179_script_A2_K4_C7_7c_K7c3_NID_deep_short_projected_ODE.py"
SOURCE_197 = HERE / "197_script_A2_K4_C7_7c_K7c_P1_clean_standalone_RK4.py"

EXPECTED_HASHES = {
    SOURCE_185: "CE75B6DB373F70701C7B35650CEB663C430197F2ED237A7346E7EBB666982686",
    SOURCE_183: "90F177DCD8AC612524AB9DD3DBA4516EC7A3805F4DE46682BEBE5F9D566EA7C8",
    SOURCE_179: "8F45DC698817992E4FB2B859A7CAFA49D225B4F7F5FD54B07F88CA99059BD441",
    SOURCE_197: "088B4CD58F57A30BD061D30042BA3E2CB5021DF9BF320003ED8291D86FB6C022",
}
EXPECTED_P1_RAW_SHA256 = (
    "A5A94550BB7542090D6244237326404A5A5CD2298D4D70A53C061B2A6B791BA5"
)
EXPECTED_CHILD_VERDICT = "REVIEW_C7_7C_K7C3C_SECOND_RK4_UNCLOSED"
EXPECTED_X = (-25.0, -24.875, -24.75)
NAMES = (
    "h", "eta", "delta_gamma", "D", "delta_b", "delta_c", "U_gamma",
    "M", "sigma_fs", "L3_fs", "L4_fs", "delta_f", "U_f",
)
TERM_NAMES = (
    "(-q-2)*M",
    "D/2",
    "(1.5*Ob-Wg*load_fraction)*U_gamma",
    "(0.25*Wg*inv1r-0.5*Og)*delta_gamma",
    "-0.5*Ob*delta_b",
    "-0.5*Oc*delta_c",
    "Of*delta_f",
    "-2*On*sigma_fs",
    "(1.5*delta*Of*(beta_f+2)+3*Of*g)*U_f",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def parse_json_blob(text: str) -> dict[str, Any]:
    start = text.find("{")
    end = text.rfind("}")
    if start < 0 or end < start:
        raise RuntimeError("child 185 returned no JSON object")
    value = json.loads(text[start:end + 1])
    if not isinstance(value, dict):
        raise TypeError("child 185 JSON root is not an object")
    return value


def left_associative_sum(values: list[float]) -> float:
    if not values:
        raise ValueError("empty term list")
    total = values[0]
    for value in values[1:]:
        total = total + value
    return total


def mp_from_float(value: float) -> mp.mpf:
    if not math.isfinite(value):
        raise FloatingPointError("non-finite float cannot enter HP reference")
    return mp.mpf(repr(float(value)))


def mp_record(value: mp.mpf) -> dict[str, object]:
    if mp.isnan(value):
        return {"decimal": "nan", "float": None}
    if mp.isinf(value):
        return {"decimal": "+inf" if value > 0 else "-inf", "float": None}
    as_float = float(value)
    return {
        "decimal": mp.nstr(value, 82),
        "float": as_float if math.isfinite(as_float) else None,
    }


def improvement_ratio(old_error: mp.mpf, new_error: mp.mpf) -> mp.mpf:
    if new_error == 0:
        return mp.inf if old_error > 0 else mp.mpf("1")
    return old_error / new_error


def background_float(x: float) -> dict[str, float]:
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
    z = k_mpc * math.exp(x) / (hubble0_mpc * math.sqrt(omega_r0))
    fuel_piece = z**p
    denominator = 1 + mu * z + fuel_piece * (1 + transfer_shape * z**2)
    denominator_x = mu * z + fuel_piece * (
        p + (p + 2) * transfer_shape * z**2
    )
    ell = denominator_x / denominator
    Og, On = rg / denominator, rn / denominator
    Ob = fb * mu * z / denominator
    Oc = (fc * mu * z + g2 * z**(p + 2) / (p + 1)) / denominator
    Of = fuel_piece * (1 - g2 * z**2 / 2) / denominator
    loading = 3 * fb * mu * z / (4 * rg)
    inv1r = 1 / (1 + loading)
    g = g2 * z**2
    beta_f = p - g / (1 - g / 2)
    return {
        "delta": delta,
        "q": -1 + ell / 2,
        "Og": Og,
        "On": On,
        "Ob": Ob,
        "Oc": Oc,
        "Of": Of,
        "load_fraction": loading * inv1r,
        "inv1r": inv1r,
        "g": g,
        "beta_f": beta_f,
    }


def background_mp(x: mp.mpf) -> dict[str, mp.mpf]:
    delta = mp.mpf("0.02297")
    p = mp.mpf("3.93109")
    h0 = mp.mpf("0.6637")
    omega_m0 = mp.mpf("0.3517")
    ombh2 = mp.mpf("0.02237")
    fb = ombh2 / (omega_m0 * h0**2)
    fc = 1 - fb
    neff = mp.mpf("3.046") + mp.mpf("0.0535")
    rn = mp.mpf("0.2271") * neff / (1 + mp.mpf("0.2271") * neff)
    rg = 1 - rn
    omega_r0 = (
        mp.mpf("2.47282e-5") * (1 + mp.mpf("0.2271") * neff) / h0**2
    )
    hubble0_mpc = 100 * h0 / mp.mpf("299792.458")
    k_mpc = mp.mpf("0.05")
    mu = hubble0_mpc * omega_m0 / mp.sqrt(omega_r0) / k_mpc
    g2 = mp.mpf("0.15") * (hubble0_mpc / k_mpc)**2 * mp.sqrt(omega_r0)
    transfer_shape = g2 * (1 / (p + 1) - mp.mpf("0.5"))
    z = k_mpc * mp.exp(x) / (hubble0_mpc * mp.sqrt(omega_r0))
    fuel_piece = z**p
    denominator = 1 + mu * z + fuel_piece * (1 + transfer_shape * z**2)
    denominator_x = mu * z + fuel_piece * (
        p + (p + 2) * transfer_shape * z**2
    )
    ell = denominator_x / denominator
    Og, On = rg / denominator, rn / denominator
    Ob = fb * mu * z / denominator
    Oc = (fc * mu * z + g2 * z**(p + 2) / (p + 1)) / denominator
    Of = fuel_piece * (1 - g2 * z**2 / 2) / denominator
    loading = 3 * fb * mu * z / (4 * rg)
    inv1r = 1 / (1 + loading)
    g = g2 * z**2
    beta_f = p - g / (1 - g / 2)
    return {
        "delta": delta,
        "q": -1 + ell / 2,
        "Og": Og,
        "On": On,
        "Ob": Ob,
        "Oc": Oc,
        "Of": Of,
        "load_fraction": loading * inv1r,
        "inv1r": inv1r,
        "g": g,
        "beta_f": beta_f,
    }


def terms_float(x: float, state: dict[str, float]) -> list[float]:
    b = background_float(x)
    Wg = 2 * b["Og"] + 1.5 * b["Ob"]
    return [
        (-b["q"] - 2) * state["M"],
        state["D"] / 2,
        (1.5 * b["Ob"] - Wg * b["load_fraction"]) * state["U_gamma"],
        (0.25 * Wg * b["inv1r"] - 0.5 * b["Og"])
        * state["delta_gamma"],
        -0.5 * b["Ob"] * state["delta_b"],
        -0.5 * b["Oc"] * state["delta_c"],
        b["Of"] * state["delta_f"],
        -2 * b["On"] * state["sigma_fs"],
        (
            1.5 * b["delta"] * b["Of"] * (b["beta_f"] + 2)
            + 3 * b["Of"] * b["g"]
        )
        * state["U_f"],
    ]


def terms_mp(x: float, state: dict[str, float]) -> list[mp.mpf]:
    b = background_mp(mp_from_float(x))
    s = {name: mp_from_float(value) for name, value in state.items()}
    Wg = 2 * b["Og"] + mp.mpf("1.5") * b["Ob"]
    return [
        (-b["q"] - 2) * s["M"],
        s["D"] / 2,
        (mp.mpf("1.5") * b["Ob"] - Wg * b["load_fraction"])
        * s["U_gamma"],
        (mp.mpf("0.25") * Wg * b["inv1r"] - mp.mpf("0.5") * b["Og"])
        * s["delta_gamma"],
        -mp.mpf("0.5") * b["Ob"] * s["delta_b"],
        -mp.mpf("0.5") * b["Oc"] * s["delta_c"],
        b["Of"] * s["delta_f"],
        -2 * b["On"] * s["sigma_fs"],
        (
            mp.mpf("1.5") * b["delta"] * b["Of"] * (b["beta_f"] + 2)
            + 3 * b["Of"] * b["g"]
        )
        * s["U_f"],
    ]


def exact_checkpoint_parity(
    child_checkpoints: list[dict[str, Any]],
    p1_checkpoints: list[dict[str, Any]],
) -> tuple[dict[str, bool], list[dict[str, object]]]:
    checks: dict[str, bool] = {
        "checkpoint_counts_exactly_three": (
            len(child_checkpoints) == 3 and len(p1_checkpoints) == 3
        )
    }
    details: list[dict[str, object]] = []
    if not checks["checkpoint_counts_exactly_three"]:
        return checks, details
    for index, expected_x in enumerate(EXPECTED_X):
        child = child_checkpoints[index]
        p1 = p1_checkpoints[index]
        child_state = dict(child.get("state", {}))
        p1_state = dict(p1.get("state", {}))
        child_rhs = dict(child.get("rhs", {}))
        p1_rhs = dict(p1.get("rhs", {}))
        x_ok = float(child.get("x")) == expected_x == float(p1.get("x"))
        names_ok = (
            set(child_state) == set(NAMES)
            and set(p1_state) == set(NAMES)
            and set(child_rhs) == set(NAMES)
            and set(p1_rhs) == set(NAMES)
        )
        state_mismatches = []
        rhs_mismatches = []
        if names_ok:
            for name in NAMES:
                if float(child_state[name]).hex() != float(p1_state[name]).hex():
                    state_mismatches.append(name)
                if float(child_rhs[name]).hex() != float(p1_rhs[name]).hex():
                    rhs_mismatches.append(name)
        checks[f"checkpoint_{index}_x_exact"] = x_ok
        checks[f"checkpoint_{index}_names_exact"] = names_ok
        checks[f"checkpoint_{index}_state_bitwise_parity"] = not state_mismatches
        checks[f"checkpoint_{index}_rhs_bitwise_parity"] = not rhs_mismatches
        details.append({
            "index": index,
            "x": expected_x,
            "state_mismatches": state_mismatches,
            "rhs_mismatches": rhs_mismatches,
        })
    return checks, details


def checkpoint_ledger(
    checkpoint: dict[str, Any], integration_scale_m: float
) -> tuple[dict[str, object], dict[str, bool], mp.mpf]:
    x = float(checkpoint["x"])
    state = {name: float(value) for name, value in dict(checkpoint["state"]).items()}
    if set(state) != set(NAMES):
        raise RuntimeError("checkpoint state names changed")
    float_terms = terms_float(x, state)
    if len(float_terms) != len(TERM_NAMES):
        raise RuntimeError("M-prime term count changed")
    if not all(math.isfinite(value) for value in float_terms):
        raise FloatingPointError("non-finite float64 M-prime term")
    plain_sum = left_associative_sum(float_terms)
    fsum_value = math.fsum(float_terms)
    rhs_m = float(dict(checkpoint["rhs"])["M"])
    rhs_bitwise_match = plain_sum.hex() == rhs_m.hex()

    same_float_hp_terms = [mp_from_float(value) for value in float_terms]
    same_float_hp_sum = mp.fsum(same_float_hp_terms)
    full_hp_terms = terms_mp(x, state)
    full_hp_sum = mp.fsum(full_hp_terms)
    sum_abs_full = mp.fsum([abs(value) for value in full_hp_terms])
    active = bool(sum_abs_full > 0 and abs(full_hp_sum) > 0)

    plain_mp = mp_from_float(plain_sum)
    fsum_mp = mp_from_float(fsum_value)
    plain_error_full = abs(plain_mp - full_hp_sum)
    fsum_error_full = abs(fsum_mp - full_hp_sum)
    improvement_full = improvement_ratio(plain_error_full, fsum_error_full)
    plain_error_same = abs(plain_mp - same_float_hp_sum)
    fsum_error_same = abs(fsum_mp - same_float_hp_sum)
    improvement_same = improvement_ratio(plain_error_same, fsum_error_same)
    cancellation = (
        sum_abs_full / abs(full_hp_sum) if full_hp_sum != 0 else mp.inf
    )
    scale_m = mp_from_float(abs(integration_scale_m))
    scaled_plain_error = plain_error_full / max(scale_m, mp.mpf("1e-300"))
    scaled_fsum_error = fsum_error_full / max(scale_m, mp.mpf("1e-300"))
    qualifies = bool(active and improvement_full >= 10)

    checks = {
        "term_count_exactly_nine": len(float_terms) == 9,
        "float_terms_finite": all(math.isfinite(value) for value in float_terms),
        "plain_sum_matches_child_rhs_M_bitwise": rhs_bitwise_match,
        "checkpoint_active": active,
        "full_hp_fsum_improvement_at_least_10": qualifies,
    }
    ledger = {
        "x": x,
        "active_checkpoint": active,
        "terms_float64": [
            {
                "name": name,
                "value": value,
                "hex": value.hex(),
                "sign": 0 if value == 0 else (1 if value > 0 else -1),
                "absolute_value": abs(value),
            }
            for name, value in zip(TERM_NAMES, float_terms)
        ],
        "terms_full_80dps": [
            {"name": name, "value": mp_record(value)}
            for name, value in zip(TERM_NAMES, full_hp_terms)
        ],
        "child_rhs_M": rhs_m,
        "plain_left_associative_sum": plain_sum,
        "math_fsum": fsum_value,
        "hp_sum_of_same_float64_terms": mp_record(same_float_hp_sum),
        "full_80dps_recomputed_sum": mp_record(full_hp_sum),
        "sum_abs_terms_over_abs_full_hp_sum": mp_record(cancellation),
        "plain_error_vs_full_hp": mp_record(plain_error_full),
        "fsum_error_vs_full_hp": mp_record(fsum_error_full),
        "fsum_improvement_vs_full_hp": mp_record(improvement_full),
        "plain_error_vs_same_float_terms_hp": mp_record(plain_error_same),
        "fsum_error_vs_same_float_terms_hp": mp_record(fsum_error_same),
        "fsum_improvement_vs_same_float_terms_hp": mp_record(improvement_same),
        "plain_error_scaled_by_M_integration_scale": mp_record(scaled_plain_error),
        "fsum_error_scaled_by_M_integration_scale": mp_record(scaled_fsum_error),
        "qualifies_for_separate_K7c3e_test": qualifies,
        "checks": checks,
    }
    return ledger, checks, improvement_full


def write_output(path: Path, payload: dict[str, object]) -> None:
    canonical = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), allow_nan=False
    )
    payload["payload_sha256_without_self"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True, allow_nan=False)
        handle.write("\n")
    print(json.dumps(payload, indent=2, sort_keys=True, allow_nan=False))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, required=True)
    parser.add_argument("--child-runtime-seconds", type=float, default=22.0)
    parser.add_argument("--p1-raw-json", type=Path)
    parser.add_argument("--output-json", type=Path)
    parser.add_argument("--smoke-test", action="store_true")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.smoke_test:
        if not 1 <= args.max_runtime_seconds <= 5:
            parser.error("smoke max-runtime-seconds must be in [1,5]")
        print(json.dumps({
            "test": "script 199 CLI and JSON smoke test",
            "term_count": len(TERM_NAMES),
            "execution_verdict": "PASS_SCRIPT199_SMOKE_NO_PHYSICS",
            "physics_executed": False,
        }, indent=2, sort_keys=True))
        return 0
    if args.max_runtime_seconds != 30:
        parser.error("scientific run requires max-runtime-seconds=30")
    if args.child_runtime_seconds != 22:
        parser.error("scientific run requires child-runtime-seconds=22")
    if args.p1_raw_json is None or args.output_json is None:
        parser.error("scientific run requires --p1-raw-json and --output-json")
    p1_raw_path = args.p1_raw_json.resolve()
    output_path = args.output_json.resolve()
    if not p1_raw_path.is_file():
        parser.error("p1-raw-json must exist")
    if not output_path.parent.is_dir():
        parser.error("output-json parent directory must exist")
    if output_path.exists():
        parser.error("output-json overwrite refused")

    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("script 199 internal deadline exceeded")

    try:
        actual_hashes = {
            str(path): sha256_file(path) for path in EXPECTED_HASHES
        }
        provenance_checks = {
            f"hash_{path.name}_matches": actual_hashes[str(path)] == expected
            for path, expected in EXPECTED_HASHES.items()
        }
        p1_hash = sha256_file(p1_raw_path)
        provenance_checks["p1_raw_hash_matches"] = (
            p1_hash == EXPECTED_P1_RAW_SHA256
        )
        if not all(provenance_checks.values()):
            payload: dict[str, object] = {
                "test": "SCI-A2K4-C7G5-K7C-P2-MLEDGER",
                "execution_verdict": "REVIEW_P2_HASH_PROVENANCE_UNCLOSED",
                "physics_executed": False,
                "provenance_checks": provenance_checks,
                "actual_hashes": actual_hashes,
                "p1_raw_sha256": p1_hash,
                "score_effect": "NONE",
                "runtime_seconds": time.monotonic() - started,
            }
            write_output(output_path, payload)
            return 1

        child = subprocess.run(
            [
                sys.executable,
                str(SOURCE_185),
                "--max-runtime-seconds", "20",
                "--source-runtime-seconds", "15",
                "--source-child-runtime-seconds", "6",
            ],
            capture_output=True,
            text=True,
            timeout=args.child_runtime_seconds,
            check=False,
        )
        deadline()
        child_payload = parse_json_blob(child.stdout)
        p1_payload = json.loads(p1_raw_path.read_text(encoding="utf-8"))
        if not isinstance(p1_payload, dict):
            raise TypeError("P1 raw JSON root is not an object")
        child_results = dict(child_payload.get("results", {}))
        p1_results = dict(p1_payload.get("results", {}))
        child_checkpoints = list(child_results.get("fine_checkpoints", []))
        p1_checkpoints = list(p1_results.get("finest_checkpoints", []))
        parity_checks, parity_details = exact_checkpoint_parity(
            child_checkpoints, p1_checkpoints
        )
        provenance_checks.update({
            "child_returncode_is_expected_review_1": child.returncode == 1,
            "child_execution_verdict_expected": (
                child_payload.get("execution_verdict") == EXPECTED_CHILD_VERDICT
            ),
            "child_state_names_exact": (
                tuple(child_payload.get("state_names", ())) == NAMES
            ),
            "p1_state_names_exact": tuple(p1_payload.get("state_names", ())) == NAMES,
            "p1_executed_path_exact": (
                p1_payload.get("executed_path_id")
                == "P1_CLEAN_STANDALONE_FIXED_CLASSICAL_RK4_ONLY"
            ),
        })
        provenance_checks.update(parity_checks)
        if not all(provenance_checks.values()):
            payload = {
                "test": "SCI-A2K4-C7G5-K7C-P2-MLEDGER",
                "execution_verdict": "REVIEW_P2_CHILD_P1_PARITY_UNCLOSED",
                "physics_executed": True,
                "term_ledger_executed": False,
                "child_returncode": child.returncode,
                "child_execution_verdict": child_payload.get("execution_verdict"),
                "provenance_checks": provenance_checks,
                "parity_details": parity_details,
                "score_effect": "NONE",
                "runtime_seconds": time.monotonic() - started,
            }
            write_output(output_path, payload)
            return 1

        mp.mp.dps = 80
        integration_scale = dict(child_payload.get("integration_scale", {}))
        integration_scale_m = float(integration_scale["M"])
        ledgers: list[dict[str, object]] = []
        checkpoint_checks: list[dict[str, bool]] = []
        improvement_values: list[mp.mpf] = []
        for checkpoint in child_checkpoints:
            deadline()
            ledger, checks, improvement = checkpoint_ledger(
                checkpoint, integration_scale_m
            )
            ledgers.append(ledger)
            checkpoint_checks.append(checks)
            improvement_values.append(improvement)

        all_formal_checks = all(
            checks["term_count_exactly_nine"]
            and checks["float_terms_finite"]
            and checks["plain_sum_matches_child_rhs_M_bitwise"]
            and checks["checkpoint_active"]
            for checks in checkpoint_checks
        )
        all_improve_10 = all(value >= 10 for value in improvement_values)
        if not all_formal_checks:
            execution_verdict = "REVIEW_P2_TERM_DECOMPOSITION_UNCLOSED"
            physical_verdict = (
                "no fsum decision; term decomposition or RHS parity failed"
            )
            return_code = 1
        elif all_improve_10:
            execution_verdict = "PASS_P2_FSUM_CANDIDATE_QUALIFIES_FOR_K7C3E"
            physical_verdict = (
                "fsum candidate qualifies for a separate evolution test; K7c remains REVIEW"
            )
            return_code = 0
        else:
            execution_verdict = "STOP_P2_SIMPLE_FSUM_EXPLANATION_IN_THIS_SCOPE"
            physical_verdict = (
                "simple fsum explanation is dead on at least one active checkpoint; "
                "A2-K4 remains alive and K7c remains REVIEW"
            )
            return_code = 0

        payload = {
            "test": "SCI-A2K4-C7G5-K7C-P2-MLEDGER",
            "execution_verdict": execution_verdict,
            "physical_verdict": physical_verdict,
            "physics_executed": True,
            "new_ODE_executed": False,
            "term_ledger_executed": True,
            "score_effect": "NONE",
            "fine_depth": "66.5/100",
            "C7_G5_weight": 20,
            "term_names": list(TERM_NAMES),
            "decision_threshold": {
                "full_hp_fsum_improvement_min_each_active_checkpoint": 10,
                "qualifying_result_only_allows_separate_K7c3e_test": True,
            },
            "source": {
                "child_script": str(SOURCE_185),
                "child_returncode": child.returncode,
                "child_execution_verdict": child_payload.get("execution_verdict"),
                "p1_raw_json": str(p1_raw_path),
                "actual_dependency_hashes": actual_hashes,
                "p1_raw_sha256": p1_hash,
            },
            "provenance_checks": provenance_checks,
            "parity_details": parity_details,
            "checkpoint_ledgers": ledgers,
            "aggregate_checks": {
                "all_provenance_checks_pass": all(provenance_checks.values()),
                "all_term_decomposition_checks_pass": all_formal_checks,
                "all_active_checkpoints_improve_at_least_10": all_improve_10,
                "checkpoint_count_exactly_three": len(ledgers) == 3,
            },
            "runtime_limits_seconds": {
                "total": args.max_runtime_seconds,
                "child_subprocess": args.child_runtime_seconds,
                "child_internal": 20,
                "child_seed_source": 15,
                "child_seed_child": 6,
            },
            "scope_limit": (
                "three stored-parity NID/deep checkpoints only; arithmetic M-prime "
                "diagnostic, no RHS replacement, no RK4 rerun, no CMB/S8 claim"
            ),
            "next_step": (
                "preregister separate K7c3e fsum evolution test"
                if all_formal_checks and all_improve_10
                else "close simple fsum explanation and audit algebraic conditioning, "
                "local stiffness/eigenmodes, or higher working precision"
            ),
            "runtime_seconds": time.monotonic() - started,
        }
        write_output(output_path, payload)
        return return_code
    except subprocess.TimeoutExpired as exc:
        payload = {
            "test": "SCI-A2K4-C7G5-K7C-P2-MLEDGER",
            "execution_verdict": "TIMEOUT_UNCLOSED",
            "physical_verdict": "no death verdict; child 185 timeout",
            "error": str(exc),
            "score_effect": "NONE",
            "runtime_seconds": time.monotonic() - started,
        }
        write_output(output_path, payload)
        return 1
    except TimeoutError as exc:
        payload = {
            "test": "SCI-A2K4-C7G5-K7C-P2-MLEDGER",
            "execution_verdict": "TIMEOUT_UNCLOSED",
            "physical_verdict": "no death verdict; script 199 internal timeout",
            "error": str(exc),
            "score_effect": "NONE",
            "runtime_seconds": time.monotonic() - started,
        }
        write_output(output_path, payload)
        return 1
    except Exception as exc:
        payload = {
            "test": "SCI-A2K4-C7G5-K7C-P2-MLEDGER",
            "execution_verdict": "ERROR_UNCLOSED",
            "physical_verdict": "no death verdict; audit formal/runtime error",
            "error_type": type(exc).__name__,
            "error": str(exc),
            "score_effect": "NONE",
            "runtime_seconds": time.monotonic() - started,
        }
        write_output(output_path, payload)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

