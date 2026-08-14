"""Thin bounded runner for preregistered KMPC-027 attempt 6."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
import time
import traceback


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


RESULT_DIR = ROOT / "scripts" / "results" / "k_mpc_005"
SHARD_PATTERN = "RUN_KMPC_027_P5_3G7_M3_FULL_RA_SEED_{mode}.json"
AGGREGATE_NAME = "RUN_KMPC_027_P5_3G7_M3_FULL_RA_SEED_ATTEMPT6.json"
FAILURE_PATTERN = "RUN_KMPC_027_P5_3G7_M3_FULL_RA_SEED_{label}_TECHNICAL_FAILURE.json"
EXPECTED_SOURCE_HASHES = {
    "full_ra_contract.py": "F3839DA931D24939FA9C5925FD29B1484E722D1A0F24117DC91EBE5F4436D464",
    "full_ra_b1_preflight.py": "62D6DEEFBDB81C0619FD58C668185FF9CA76926A90D00DCE9C092AD4797D6B5D",
    "full_ra_b1_preflight_v2.py": "27C0D6ADA828CA2F59C0D128EB6339074D5940F294272CDABE8127CB84867C7C",
    "mode_resolved_puiseux.py": "5A89CF82006CB5ECC1D8B4BE1FD56A463453EE3D6261968CB64DE8CCF2C8B7AE",
    "mode_resolved_puiseux_v2_m1_anchored.py": "5DE2C280B0E9DAF528A9E3011368361B37AE53DE38827FB6F6CE4AB2019A4455",
    "full_ra_m3_seed.py": "070F217B45A385369ECAFAA3D409A1210BAE3C3AF8A600A9171225B258751BF2",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-runtime-seconds", type=float, default=4.5)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--smoke", action="store_true")
    group.add_argument("--mode", choices=("AD", "CDI", "BI", "NID", "NIV"))
    group.add_argument("--aggregate", action="store_true")
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def _hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def _json_safe(value: object) -> object:
    if isinstance(value, float) and not math.isfinite(value):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    return value


def _write_new(path: Path, payload: dict[str, object]) -> None:
    path = path.resolve()
    result_root = RESULT_DIR.resolve()
    if result_root not in path.parents:
        raise ValueError("output must stay inside scripts/results/k_mpc_005")
    if path.exists():
        raise FileExistsError(f"immutable result already exists: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(_json_safe(payload), indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def _aggregate(base: object, max_runtime_seconds: float) -> dict[str, object]:
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > max_runtime_seconds:
            raise TimeoutError("KMPC-027 aggregate internal deadline exceeded")

    modes = ("AD", "CDI", "BI", "NID", "NIV")
    shards: dict[str, object] = {}
    hashes: dict[str, str] = {}
    checks: dict[str, bool] = {}
    expected_hashes = base.source_hashes()
    expected_thresholds = {
        "rcond": base.RCOND,
        "pass_singular_ratio": base.PASS_SINGULAR_RATIO,
        "driver": base.DRIVER_TOL,
        "holdout": base.HOLDOUT_TOL,
        "absolute_fallback_norm": base.ABS_FALLBACK_NORM,
        "absolute_fallback": base.ABS_FALLBACK_TOL,
        "low_coefficient": base.LOW_COEFFICIENT_TOL,
        "tail": base.TAIL_TOL,
        "background_k": base.BACKGROUND_K_TOL,
    }
    physical_backgrounds: dict[str, dict[str, list[float]]] = {
        str(a): {name: [] for name in ("D", "H_Mpc_inverse", "rho_f_over_rho_r", "rho_ash_over_rho_r")}
        for a in base.A_VALUES_BACKGROUND
    }
    for mode in modes:
        path = RESULT_DIR / SHARD_PATTERN.format(mode=mode)
        if not path.exists():
            raise FileNotFoundError(path)
        data = json.loads(path.read_text(encoding="utf-8"))
        deadline()
        shards[mode] = {
            "path": str(path.relative_to(ROOT)),
            "sha256": _hash(path),
            "verdict": data.get("verdict"),
            "runtime_seconds": data.get("runtime_seconds"),
        }
        hashes[mode] = _hash(path)
        checks[f"{mode}_present"] = data.get("mode") == mode
        checks[f"{mode}_run_id"] = data.get("run_id") == "KMPC-027"
        checks[f"{mode}_k_set"] = data.get("k_Mpc_inverse") == list(base.K_VALUES)
        checks[f"{mode}_z_surfaces"] = data.get("z_surfaces") == list(base.Z_SURFACES)
        checks[f"{mode}_thresholds"] = data.get("thresholds") == expected_thresholds
        checks[f"{mode}_source_hashes"] = data.get("source_hashes") == expected_hashes
        checks[f"{mode}_all_checks_true"] = bool(data.get("checks")) and all(
            bool(value) for value in data.get("checks", {}).values()
        )
        result_map = data.get("results", {})
        checks[f"{mode}_all_k_results"] = set(result_map) == {
            str(value) for value in base.K_VALUES
        }
        variants_complete = True
        for k_mpc in base.K_VALUES:
            entry = result_map.get(str(k_mpc), {})
            variants = entry.get("variants", {})
            variants_complete = variants_complete and set(variants) == {
                "nominal", "gamma0", "af0"
            }
            for variant in variants.values():
                variants_complete = variants_complete and all(
                    key in variant
                    for key in ("fuel_primary", "fuel_extended", "m3_primary", "m3_extended", "truncation", "null_limit", "pass")
                )
        checks[f"{mode}_variants_and_primary_extended_complete"] = variants_complete
        for a, by_quantity in data.get("background_physical_values_by_a", {}).items():
            if a not in physical_backgrounds:
                continue
            for name, values in by_quantity.items():
                if name in physical_backgrounds[a]:
                    physical_backgrounds[a][name].extend(float(value) for value in values)
        checks[f"{mode}_pass"] = data.get("verdict") == "PASS_M3_TCA0_SEED_CONDITIONAL_SHARD"
    cross_mode_spreads: dict[str, dict[str, float]] = {}
    for a, by_quantity in physical_backgrounds.items():
        cross_mode_spreads[a] = {}
        for name, values in by_quantity.items():
            spread = (
                (max(values) - min(values))
                / max(max(abs(value) for value in values), 1.0e-300)
                if values
                else math.inf
            )
            cross_mode_spreads[a][name] = spread
            checks[f"cross_mode_background:a={a}:{name}"] = bool(
                len(values) == len(modes) * len(base.K_VALUES)
                and spread <= base.BACKGROUND_K_TOL
            )
    deadline()
    passed = bool(checks) and all(checks.values())
    return {
        "test": "KMPC-027 P5.3g7 M3 FULL/R-A attempt-6 aggregate",
        "run_id": "KMPC-027",
        "scope": "conditional M3-TCA0 seed only; aggregate of five immutable mode shards",
        "shards": shards,
        "shard_hashes": hashes,
        "checks": checks,
        "cross_mode_background_relative_spreads": cross_mode_spreads,
        "verdict": (
            "PASS_M3_TCA0_SEED_CONDITIONAL"
            if passed
            else "REVIEW_M3_TCA0_SEED_UNCLOSED"
        ),
        "P5_3g7_verdict": (
            "REVIEW_BLOCKED_S1_FINITE_OPACITY_AND_P5_4"
            if passed
            else "REVIEW_BLOCKED_M3"
        ),
        "canonical_depth": "60/100",
        "score_effect": "NONE_UNTIL_WHOLE_G7_CLOSES",
        "release_trigger": "NONE",
        "runtime_limit_seconds": max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }


def main() -> int:
    args = parse_args()
    if not 0.05 <= args.max_runtime_seconds <= 5.0:
        raise ValueError("internal runtime must be in [0.05, 5.0] seconds")
    from scripts.baseScripts.p5_general_synchronous import full_ra_m3_seed as base
    observed_hashes = base.source_hashes()
    if observed_hashes != EXPECTED_SOURCE_HASHES:
        raise RuntimeError(
            f"frozen source hash mismatch: expected={EXPECTED_SOURCE_HASHES}, observed={observed_hashes}"
        )

    try:
        if args.smoke:
            payload = base.run_smoke(args.max_runtime_seconds)
            print(json.dumps(_json_safe(payload), indent=2, sort_keys=True, allow_nan=False))
            return 0 if payload["passed"] else 2
        if args.aggregate:
            payload = _aggregate(base, args.max_runtime_seconds)
            output = args.output or (RESULT_DIR / AGGREGATE_NAME)
        else:
            payload = base.run_mode_shard(args.mode, args.max_runtime_seconds)
            output = args.output or (RESULT_DIR / SHARD_PATTERN.format(mode=args.mode))
        _write_new(output, payload)
        print(json.dumps({"output": str(output), "verdict": payload["verdict"]}, sort_keys=True))
        return 0 if payload["verdict"].startswith("PASS_") else 2
    except Exception as error:
        label = "AGGREGATE" if args.aggregate else (args.mode or "SMOKE")
        failure_path = RESULT_DIR / FAILURE_PATTERN.format(label=label)
        failure = {
            "test": "KMPC-027 attempt-6 technical failure evidence",
            "run_id": "KMPC-027",
            "phase": label,
            "error_type": type(error).__name__,
            "error_message": str(error),
            "traceback": traceback.format_exc(limit=12),
            "physics_verdict": "NONE_TECHNICAL_FAILURE",
        }
        if not args.smoke and not failure_path.exists():
            _write_new(failure_path, failure)
        print(json.dumps(_json_safe(failure), indent=2, sort_keys=True, allow_nan=False))
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
