"""Bounded audit of the provenance and gate claims around scripts 170--185.

This script performs source-level checks and four bounded child runs.  It does
not modify theory data.  A non-zero child exit is retained as evidence because
script 172 is expected to return REVIEW before the registry fix.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def source(number: int) -> str:
    matches = sorted(SCRIPTS.glob(f"{number}_script_*.py"))
    if len(matches) != 1:
        raise RuntimeError(f"expected one script {number}, found {len(matches)}")
    return matches[0].read_text(encoding="utf-8")


def run_json(number: int, arguments: list[str], timeout: float) -> dict:
    matches = sorted(SCRIPTS.glob(f"{number}_script_*.py"))
    if len(matches) != 1:
        raise RuntimeError(f"expected one script {number}, found {len(matches)}")
    completed = subprocess.run(
        [sys.executable, str(matches[0]), *arguments],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
    )
    if not completed.stdout.strip():
        raise RuntimeError(
            f"script {number} produced no JSON; exit={completed.returncode}; "
            f"stderr={completed.stderr[-1000:]}"
        )
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"script {number} emitted invalid JSON; exit={completed.returncode}; "
            f"stdout_tail={completed.stdout[-1000:]}"
        ) from exc
    return {"exit_code": completed.returncode, "payload": payload}


def nested(payload: dict, *keys: str):
    value = payload
    for key in keys:
        value = value[key]
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=35.0)
    parser.add_argument("--child-timeout-seconds", type=float, default=15.0)
    args = parser.parse_args()
    started = time.monotonic()

    texts = {number: source(number) for number in range(170, 186)}
    base119 = source(119)
    capture_marker = "if mode == args.hp_mode:"
    corrected_capture = (
        "if mode == args.hp_mode and abs(mu-physical_mu) < 1e-30:"
    )

    common_export = [
        "--max-runtime-seconds", "8", "--standard-order", "6",
        "--x-deep", "-25", "--x-shallow", "-23",
        "--x-reference", "-18", "--k-mpc", "0.05",
        "--fuel-fraction-coefficient", "1", "--hp-mode", "NID",
    ]
    common_gate = [
        "--max-runtime-seconds", "14", "--source-runtime-seconds", "8",
        "--mode", "NID", "--surface", "deep", "--dps", "80",
    ]

    runs: dict[str, dict] = {}
    for label, number, arguments in (
        ("export_171", 171, common_export),
        ("export_174", 174, common_export),
        ("gate_172", 172, common_gate),
        ("gate_175", 175, common_gate),
    ):
        remaining = args.max_runtime_seconds - (time.monotonic() - started)
        if remaining <= 1.0:
            raise TimeoutError("script 187 internal deadline exceeded")
        runs[label] = run_json(
            number, arguments, min(args.child_timeout_seconds, remaining)
        )

    pre = runs["gate_172"]["payload"]
    post = runs["gate_175"]["payload"]

    def difference(payload: dict, name: str) -> float:
        item = payload["state_comparison"][name]
        return abs(float(item["exported_float64"]) - float(item["high_precision"]))

    static = {
        "registry_capture_unqualified_in_170": capture_marker in texts[170],
        "physical_then_zero_mu_calls": (
            "solve_standard(mode, physical_mu)" in base119
            and "solve_standard(mode, 0.0)" in base119
            and base119.index("solve_standard(mode, physical_mu)")
            < base119.index("solve_standard(mode, 0.0)")
        ),
        "173_targets_marker_absent_from_171": (
            "171_script_" in texts[173]
            and texts[171].count(capture_marker) == 0
            and "source_text.count(old) != 1" in texts[173]
        ),
        "174_targets_170_and_filters_physical_mu": (
            "170_script_" in texts[174]
            and "abs(mu-physical_mu) < 1e-30" in texts[174]
        ),
        "condition_uses_original_singular_values": (
            "np.linalg.lstsq(matrix, rhs" in texts[170]
            and "condition_resolved" in texts[170]
            and "singular[0]" in texts[170]
        ),
        "179_tuple_order_check": "tuple(deep_seed) != NAMES" in texts[179],
        "180_set_check": "set(deep_seed) != set(NAMES)" in texts[180],
        "181_unscaled_unit_probe": "np.eye(13, dtype=float)[:, column]" in texts[181],
        "182_scaled_probe": (
            "np.eye(13, dtype=float)[:, column]*scale[column]" in texts[182]
            and "/scale[column]" in texts[182]
        ),
        "172_fail_open_rank_equality": (
            'hp_solver.get("reduced_rank") == hp_solver.get("free_count")'
            in texts[172]
        ),
        "178_seed_self_checks": (
            'seed["D"] == D' in texts[178] and 'seed["M"] == M' in texts[178]
        ),
        "185_ratio_exported_but_not_gated_8_to_32": (
            "previous_over_current_difference" in texts[185]
            and "8.0 < previous_over_current_difference < 32.0" not in texts[185]
            and "8 < previous_over_current_difference < 32" not in texts[185]
        ),
        "183_old_solver_left_after_early_return": (
            "solution = solve_ivp(" in texts[183]
            and "fixed_step + marker" in texts[183]
            and "return 0 if passed else 1" in texts[183]
        ),
    }

    solver = post["K7b3b_hard_constrained_standard_solver"]
    numeric = {
        "pre_172_exit": runs["gate_172"]["exit_code"],
        "pre_172_verdict": pre["execution_verdict"],
        "pre_U_fs_difference": difference(pre, "U_fs"),
        "pre_U_gamma_difference": difference(pre, "U_gamma"),
        "pre_D_activity_relative_error": pre["D_activity_relative_error"],
        "post_175_exit": runs["gate_175"]["exit_code"],
        "post_175_verdict": post["execution_verdict"],
        "post_U_fs_difference": difference(post, "U_fs"),
        "post_U_gamma_difference": difference(post, "U_gamma"),
        "post_D_activity_relative_error": post["D_activity_relative_error"],
        "post_rank_keys_present": all(k in solver for k in ("reduced_rank", "free_count")),
        "reported_condition": solver["condition_resolved"],
        "normal_equation_condition_estimate": solver["condition_resolved"] ** 2,
    }
    output = {
        "test": "A2-K4 K7b/K7c scripts 170-185 claim audit",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "static_evidence": static,
        "numerical_evidence": numeric,
        "scope": "provenance and bounded reproduction; no new ODE verdict or depth award",
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
