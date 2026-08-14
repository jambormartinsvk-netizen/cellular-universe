#!/usr/bin/env python3
"""Offline, non-executing aggregate of three immutable P4a solver cases."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np


NAMES = (
    "h", "eta", "delta_gamma", "D", "delta_b", "delta_c",
    "U_gamma", "M", "sigma_fs", "L3_fs", "L4_fs", "delta_f", "U_f",
)
EXPECTED_REFERENCE_SHA256 = (
    "9E3C73D635924E829A5F57BA540EBB1F5861F67F21CFCE69BD93423D6FA8FC8D"
)
EXPECTED_BASE205_SHA256 = (
    "B7EC8BAD3BFB0D48EC91D6F1BB0A602FA1834A021BB94C92D6D1B398D5F3CDC2"
)
EXPECTED_RUNNER209_SHA256 = (
    "67E5B3C1B7C942242E4FEB4458A4CC81A52F6417E25D50A6E2009023F321A612"
)
LIMIT = 1e-8


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def load_case(path: Path, expected_case: str) -> tuple[dict[str, object], str]:
    resolved = path.resolve()
    payload = json.loads(resolved.read_text(encoding="utf-8"))
    if payload.get("case") != expected_case:
        raise RuntimeError(
            f"case mismatch for {resolved}: {payload.get('case')!r} != {expected_case!r}"
        )
    return payload, sha256_file(resolved)


def vector(payload: dict[str, object], key: str) -> np.ndarray:
    mapping = dict(payload.get(key, {}))
    if set(mapping) != set(NAMES):
        raise RuntimeError(f"{key} keys changed for case {payload.get('case')}")
    result = np.asarray([float(mapping[name]) for name in NAMES], dtype=float)
    if not np.all(np.isfinite(result)):
        raise FloatingPointError(f"non-finite {key} for case {payload.get('case')}")
    return result


def max_difference(left: np.ndarray, right: np.ndarray) -> float:
    value = float(np.max(np.abs(left - right)))
    if not math.isfinite(value) or value < 0:
        raise FloatingPointError("non-finite or negative comparison")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description="Offline P4a G5 aggregate")
    parser.add_argument("--medium", type=Path, required=True)
    parser.add_argument("--tight", type=Path, required=True)
    parser.add_argument("--radau", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    args = parser.parse_args()
    if not 0 < args.max_runtime_seconds <= 5:
        parser.error("max-runtime-seconds must be in (0,5]")
    output_path = args.output.resolve()
    if output_path.exists():
        raise FileExistsError(f"refusing to overwrite output: {output_path}")
    if not output_path.parent.is_dir():
        raise FileNotFoundError(f"output parent missing: {output_path.parent}")
    inputs = [args.medium.resolve(), args.tight.resolve(), args.radau.resolve()]
    if len(set(inputs)) != 3:
        raise RuntimeError("medium, tight, and Radau inputs must be distinct files")

    started = time.monotonic()
    medium, medium_hash = load_case(args.medium, "DOP853_MEDIUM")
    tight, tight_hash = load_case(args.tight, "DOP853_TIGHT")
    radau, radau_hash = load_case(args.radau, "RADAU_TIGHT")
    cases = (medium, tight, radau)

    structural_checks = {
        "all_case_execution_verdicts_pass": all(
            item.get("execution_verdict") == "PASS_P4A_SINGLE_CASE_EXECUTION"
            for item in cases
        ),
        "all_case_structural_pass": all(item.get("structural_pass") is True for item in cases),
        "all_state_names_exact_order": all(
            list(item.get("state_names", ())) == list(NAMES) for item in cases
        ),
        "all_reference_hashes_exact": all(
            dict(item.get("hashes", {})).get("reference_grid400_sha256")
            == EXPECTED_REFERENCE_SHA256 for item in cases
        ),
        "all_base205_hashes_exact": all(
            dict(item.get("hashes", {})).get("base205_sha256")
            == EXPECTED_BASE205_SHA256 for item in cases
        ),
        "all_runner209_hashes_exact": all(
            dict(item.get("hashes", {})).get("self_sha256")
            == EXPECTED_RUNNER209_SHA256 for item in cases
        ),
        "all_physics_executed": all(item.get("physics_executed") is True for item in cases),
    }
    structural_checks = {key: bool(value) for key, value in structural_checks.items()}
    structural_pass = all(structural_checks.values())

    medium_endpoint = vector(medium, "normalized_endpoint")
    tight_endpoint = vector(tight, "normalized_endpoint")
    radau_endpoint = vector(radau, "normalized_endpoint")
    medium_reference = vector(medium, "reference_grid400_normalized_endpoint")
    tight_reference = vector(tight, "reference_grid400_normalized_endpoint")
    radau_reference = vector(radau, "reference_grid400_normalized_endpoint")
    reference_identity = (
        np.array_equal(medium_reference, tight_reference)
        and np.array_equal(tight_reference, radau_reference)
    )

    comparisons = {
        "DOP853_TIGHT_vs_P3b_RK4_grid400": max_difference(
            tight_endpoint, tight_reference
        ),
        "DOP853_MEDIUM_vs_DOP853_TIGHT": max_difference(
            medium_endpoint, tight_endpoint
        ),
        "RADAU_TIGHT_vs_P3b_RK4_grid400": max_difference(
            radau_endpoint, radau_reference
        ),
        "RADAU_TIGHT_vs_DOP853_TIGHT": max_difference(
            radau_endpoint, tight_endpoint
        ),
    }
    comparison_checks = {
        name + "_le_1e-8": value <= LIMIT for name, value in comparisons.items()
    }
    comparison_checks["reference_vectors_bitwise_identical"] = bool(reference_identity)
    comparison_checks = {key: bool(value) for key, value in comparison_checks.items()}
    all_comparisons_pass = all(comparison_checks.values())

    methods_agree = comparisons["RADAU_TIGHT_vs_DOP853_TIGHT"] <= LIMIT
    both_disagree_with_reference = (
        comparisons["DOP853_TIGHT_vs_P3b_RK4_grid400"] > LIMIT
        and comparisons["RADAU_TIGHT_vs_P3b_RK4_grid400"] > LIMIT
    )
    if not structural_pass:
        verdict = "REVIEW_P4A_AGGREGATE_INPUT_OR_PROVENANCE"
        physical_verdict = "REVIEW: at least one immutable case failed structure/provenance"
        score_effect = "NONE"
        exit_code = 2
    elif all_comparisons_pass:
        verdict = "PASS_P4A_G5_METHOD_TOLERANCE_BREADTH"
        physical_verdict = "PASS: step, tolerance, and method convergence all closed"
        score_effect = "C7-G5 full PASS; strict support 40->60/100"
        exit_code = 0
    elif methods_agree and both_disagree_with_reference:
        verdict = "REVIEW_REFERENCE_CONFLICT"
        physical_verdict = "REVIEW: DOP853 and Radau agree with each other, not RK4"
        score_effect = "NONE"
        exit_code = 2
    else:
        verdict = "STOP_P4A_METHOD_BREADTH"
        physical_verdict = "STOP K7 at G5: valid alternative methods do not agree"
        score_effect = "C7-G5 blocker 20/100 for current K7"
        exit_code = 1

    if time.monotonic() - started > args.max_runtime_seconds:
        raise TimeoutError("P4a offline aggregate deadline exceeded")
    output = {
        "test": "SCI-A2K4-C7G5-K7C-P4A-METHOD-TOLERANCE",
        "execution_verdict": verdict,
        "physical_verdict": physical_verdict,
        "physics_executed_by_aggregate": False,
        "input_cases_executed_physics": True,
        "threshold": LIMIT,
        "comparisons": comparisons,
        "comparison_checks": comparison_checks,
        "structural_checks": structural_checks,
        "structural_pass": structural_pass,
        "all_comparisons_pass": all_comparisons_pass,
        "score_effect": score_effect,
        "fine_depth_before": "66.5/100",
        "input_files": {
            "DOP853_MEDIUM": str(args.medium.resolve()),
            "DOP853_TIGHT": str(args.tight.resolve()),
            "RADAU_TIGHT": str(args.radau.resolve()),
        },
        "input_sha256": {
            "DOP853_MEDIUM": medium_hash,
            "DOP853_TIGHT": tight_hash,
            "RADAU_TIGHT": radau_hash,
        },
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "scope_limit": (
            "P4a NID/deep 0.25-e-fold G5 method/tolerance only; no G4/G6/G7, "
            "full hierarchy, CMB, S8, H0, or likelihood claim"
        ),
    }
    encoded = json.dumps(output, indent=2, sort_keys=True)
    with output_path.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(encoded + "\n")
    print(encoded)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())

