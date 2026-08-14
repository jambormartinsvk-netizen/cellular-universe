"""Package-local KMPC-035 reproduction-closure runner.

This technical successor preserves the frozen KMPC-035 equations and decision
thresholds.  It repairs only the external-audit delivery contract: complete
runtime inputs, environment capture, collision-safe publication, explicit
cross-platform diagnostics, and absolute-branch diagnostics.
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.metadata
import io
import json
import math
import os
from pathlib import Path
import platform
import sys
import tempfile
import time
from typing import Any, Callable, Mapping

import numpy as np


PACKAGE_ID = "EA-20260717-005-KMPC035-CDI-SUPPORT-CLOSURE"
RUN_ID = "EA005_KMPC035_REPRODUCTION_CLOSURE"
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

BASE_DIR = ROOT / "scripts" / "baseScripts" / "p5_general_synchronous"
RESULT_DIR = ROOT / "scripts" / "results" / "k_mpc_005"
INPUT_DIR = ROOT / "inputs"
CANONICAL_OUTPUT = RESULT_DIR / "RUN_EA005_KMPC035_REPRODUCTION_CLOSURE.json"
FAILURE_OUTPUT = RESULT_DIR / "RUN_EA005_KMPC035_REPRODUCTION_CLOSURE_TECHNICAL_FAILURE.json"
REFERENCE_RESULT = INPUT_DIR / "RUN_KMPC_035_P5_3G7_CDI_C2_SUPPORT_03_05_LADDER.json"
KMPC034_INPUT = RESULT_DIR / "RUN_KMPC_034_P5_3G7_CDI_C1_PRIMARY_EXTENDED_COVERAGE.json"

EXPECTED_RUNTIME_INPUT_HASHES = {
    str(KMPC034_INPUT.relative_to(ROOT)): "37FB4453CBFF38710CF5694C21104689F1B070742FB02324011AA389508DCE20",
    str(REFERENCE_RESULT.relative_to(ROOT)): "A9BD519F9124B80E648EE327A3C2175A5E9DC3D65B02EB1CFD7F119333E42A01",
}

EXPECTED_SOURCE_HASHES = {
    "full_ra_b1_preflight.py": "62D6DEEFBDB81C0619FD58C668185FF9CA76926A90D00DCE9C092AD4797D6B5D",
    "full_ra_b1_preflight_v2.py": "27C0D6ADA828CA2F59C0D128EB6339074D5940F294272CDABE8127CB84867C7C",
    "full_ra_contract.py": "F3839DA931D24939FA9C5925FD29B1484E722D1A0F24117DC91EBE5F4436D464",
    "full_ra_m3_seed.py": "070F217B45A385369ECAFAA3D409A1210BAE3C3AF8A600A9171225B258751BF2",
    "mode_resolved_puiseux.py": "5A89CF82006CB5ECC1D8B4BE1FD56A463453EE3D6261968CB64DE8CCF2C8B7AE",
    "mode_resolved_puiseux_v2_m1_anchored.py": "5DE2C280B0E9DAF528A9E3011368361B37AE53DE38827FB6F6CE4AB2019A4455",
    "s1_collective_contract.py": "F535EE15137BBD6F9C0379821C9CC94DED8EC56037B6105B75BEF65A5884EE68",
    "s_c0_coefficient_passport.py": "C370B610815AFAC345C990E3CFE516D616873F39598F468A5ADBF2C65A2A6B95",
    "s_c0_coefficient_passport_v2_numpy_scalar.py": "06EE03C939FBCCFA6FA130421EEF98D0B8CC7571937EF02A7A46A57367534C11",
    "cdi_c1_coverage.py": "D57CA8CA5571A07440A987F4FB0DDA08A40DAF7EA8C95AF929FC5C936F2FCE0F",
    "cdi_support_ladder.py": "A8257E2195E2AB61B5C4195B80EA44EE7669B5A52F9C8440BA5F5244190E3068",
}

FROZEN_PHYSICS_THRESHOLDS = {
    "regression_relative": 1.0e-12,
    "regression_absolute": 1.0e-14,
    "common_relative": 1.0e-8,
    "common_absolute": 1.0e-12,
    "tail_relative": 1.0e-6,
    "tail_absolute_norm": 1.0e-12,
    "tail_absolute_tolerance": 1.0e-12,
}

# New in this follow-up package.  This diagnostic never changes the frozen
# KMPC-035 candidate interpretation or any project PASS/REVIEW/STOP.
CROSS_PLATFORM_DIAGNOSTIC = {
    "relative": 1.0e-9,
    "absolute": 1.0e-13,
    "verdict_effect": "NONE",
    "status": "PREREGISTERED_DIAGNOSTIC_ONLY_AFTER_EXTERNAL_FINDING_F2",
}

Z_SCAN_DIAGNOSTIC = (1.0e-4, 3.0e-4, 1.0e-3, 2.0e-3, 3.0e-3, 1.0e-2)


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def _json_safe(value: Any) -> Any:
    if isinstance(value, np.generic):
        return _json_safe(value.item())
    if isinstance(value, Mapping):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    if isinstance(value, float):
        if not math.isfinite(value):
            raise FloatingPointError("non-finite value rejected before JSON export")
        return value
    if isinstance(value, (str, int, bool)) or value is None:
        return value
    raise TypeError(f"unsupported JSON value type: {type(value).__name__}")


def _atomic_write_exclusive(
    path: Path,
    payload: Any,
    *,
    prelink_hook: Callable[[Path], None] | None = None,
) -> None:
    """Publish once and remove this process's temp file on every exit path."""
    if not path.parent.is_dir():
        raise FileNotFoundError(f"output directory missing: {path.parent}")
    if path.exists():
        raise FileExistsError(f"immutable output already exists: {path}")
    temporary = path.with_name(f"{path.name}.tmp-EA005-{os.getpid()}")
    try:
        with temporary.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(_json_safe(payload), handle, indent=2, sort_keys=True, allow_nan=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        if prelink_hook is not None:
            prelink_hook(path)
        os.link(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def _runtime_environment() -> dict[str, Any]:
    versions: dict[str, str] = {}
    for package_name in ("numpy", "scipy", "sympy"):
        try:
            versions[package_name] = importlib.metadata.version(package_name)
        except importlib.metadata.PackageNotFoundError:
            versions[package_name] = "NOT_INSTALLED"
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        np.show_config()
    config_text = buffer.getvalue()
    return {
        "python_version": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "packages": versions,
        "numpy_config_text": config_text,
        "numpy_config_sha256": hashlib.sha256(config_text.encode("utf-8")).hexdigest().upper(),
    }


def _verify_delivery_inputs() -> dict[str, Any]:
    observed_runtime = {
        relative: _sha256_file(ROOT / Path(relative))
        for relative in EXPECTED_RUNTIME_INPUT_HASHES
    }
    observed_sources = {
        name: _sha256_file(BASE_DIR / name)
        for name in EXPECTED_SOURCE_HASHES
    }
    return {
        "runtime_inputs_expected": EXPECTED_RUNTIME_INPUT_HASHES,
        "runtime_inputs_observed": observed_runtime,
        "runtime_inputs_pass": observed_runtime == EXPECTED_RUNTIME_INPUT_HASHES,
        "sources_expected": EXPECTED_SOURCE_HASHES,
        "sources_observed": observed_sources,
        "sources_pass": observed_sources == EXPECTED_SOURCE_HASHES,
    }


def _normalise_power_map(value: Mapping[Any, Any]) -> dict[str, float]:
    return {str(power): float(coefficient) for power, coefficient in value.items()}


def _coefficient_groups(payload: Mapping[str, Any]) -> dict[str, dict[str, dict[str, float]]]:
    groups: dict[str, dict[str, dict[str, float]]] = {}
    solved = payload["solved_supports"]
    for support in ("01", "03", "05"):
        groups[f"{support}/F0"] = {
            str(state): _normalise_power_map(powers)
            for state, powers in solved[support]["fuel"]["state"].items()
        }
        groups[f"{support}/M3"] = {
            str(state): _normalise_power_map(powers)
            for state, powers in solved[support]["m3"]["fractional_state"].items()
        }
    return groups


def _cross_platform_diagnostic(
    reference: Mapping[str, Any],
    observed: Mapping[str, Any],
) -> dict[str, Any]:
    expected_groups = _coefficient_groups(reference)
    observed_groups = _coefficient_groups(observed)
    rows: list[dict[str, Any]] = []
    exact_group_set = set(expected_groups) == set(observed_groups)
    exact_state_and_power_sets = exact_group_set
    if exact_group_set:
        for group in sorted(expected_groups):
            expected_states = expected_groups[group]
            observed_states = observed_groups[group]
            if set(expected_states) != set(observed_states):
                exact_state_and_power_sets = False
                continue
            for state in sorted(expected_states):
                expected_powers = expected_states[state]
                observed_powers = observed_states[state]
                if set(expected_powers) != set(observed_powers):
                    exact_state_and_power_sets = False
                    continue
                for power in sorted(expected_powers, key=int):
                    left = expected_powers[power]
                    right = observed_powers[power]
                    difference = abs(left - right)
                    scale = max(abs(left), abs(right))
                    relative = difference / scale if scale > 0.0 else 0.0
                    allowed = max(
                        CROSS_PLATFORM_DIAGNOSTIC["absolute"],
                        CROSS_PLATFORM_DIAGNOSTIC["relative"] * scale,
                    )
                    rows.append(
                        {
                            "path": f"{group}/{state}[{power}]",
                            "reference": left,
                            "observed": right,
                            "absolute_difference": difference,
                            "relative_difference": relative,
                            "allowed_diagnostic": allowed,
                            "bound_ratio": difference / allowed,
                        }
                    )
    worst_relative = max(rows, key=lambda row: row["relative_difference"], default=None)
    worst_bound = max(rows, key=lambda row: row["bound_ratio"], default=None)
    return {
        "status": CROSS_PLATFORM_DIAGNOSTIC["status"],
        "verdict_effect": CROSS_PLATFORM_DIAGNOSTIC["verdict_effect"],
        "thresholds": {
            "relative": CROSS_PLATFORM_DIAGNOSTIC["relative"],
            "absolute": CROSS_PLATFORM_DIAGNOSTIC["absolute"],
        },
        "exact_group_set": exact_group_set,
        "exact_state_and_power_sets": exact_state_and_power_sets,
        "coefficient_count": len(rows),
        "expected_coefficient_count": 180,
        "worst_relative": worst_relative,
        "worst_bound_ratio": worst_bound,
        "pass_diagnostic_only": bool(
            exact_state_and_power_sets
            and len(rows) == 180
            and worst_bound is not None
            and worst_bound["bound_ratio"] <= 1.0
        ),
    }


def _absolute_branch_diagnostics(payload: Mapping[str, Any]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    tails = payload["pure_added_tails_45"]
    for sector in ("F0", "M3"):
        for z_value, surface in tails[sector]["by_z"].items():
            for state, values in surface["states"].items():
                if values["branch"] != "absolute":
                    continue
                scale = max(
                    abs(float(values["base_candidate_03"])),
                    abs(float(values["full_audit_05"])),
                )
                envelope = float(values["absolute_term_envelope_45_authoritative"])
                rows.append(
                    {
                        "sector": sector,
                        "z": float(z_value),
                        "state": state,
                        "authoritative_branch": "absolute",
                        "authoritative_metric": float(values["metric"]),
                        "would_be_relative_metric_diagnostic": envelope / scale if scale > 0.0 else None,
                        "verdict_effect": "NONE",
                    }
                )
    return {
        "status": "DIAGNOSTIC_ONLY_AFTER_EXTERNAL_FINDING_F3",
        "rows": rows,
        "row_count": len(rows),
        "verdict_effect": "NONE",
    }


def _tail_scan_for_state(powers: Mapping[Any, Any], z_value: float) -> dict[str, Any]:
    coefficients = {int(power): float(value) for power, value in powers.items()}
    base = sum(coefficients.get(power, 0.0) * z_value**power for power in range(1, 4))
    signed_tail = sum(coefficients.get(power, 0.0) * z_value**power for power in (4, 5))
    envelope = sum(abs(coefficients.get(power, 0.0)) * z_value**power for power in (4, 5))
    full = base + signed_tail
    scale = max(abs(base), abs(full))
    branch = "relative" if scale > FROZEN_PHYSICS_THRESHOLDS["tail_absolute_norm"] else "absolute"
    metric = envelope / scale if branch == "relative" else envelope
    return {
        "base_1_3": base,
        "signed_tail_4_5": signed_tail,
        "envelope_4_5": envelope,
        "full_1_5": full,
        "branch_if_authoritative_surface": branch,
        "metric_if_authoritative_surface": metric,
    }


def _z_scan_diagnostic(payload: Mapping[str, Any]) -> dict[str, Any]:
    solved = payload["solved_supports"]["05"]
    sectors = {
        "F0": solved["fuel"]["state"],
        "M3": solved["m3"]["fractional_state"],
    }
    by_z: dict[str, Any] = {}
    for z_value in Z_SCAN_DIAGNOSTIC:
        by_z[str(z_value)] = {
            sector: {
                str(state): _tail_scan_for_state(powers, z_value)
                for state, powers in states.items()
            }
            for sector, states in sectors.items()
        }
    return {
        "status": "DIAGNOSTIC_ONLY_AFTER_EXTERNAL_FINDING_F4",
        "z_values": Z_SCAN_DIAGNOSTIC,
        "by_z": by_z,
        "verdict_effect": "NONE",
        "nonclaim": "This is a two-term local remainder diagnostic, not a bound on the infinite series.",
    }


def _atomic_collision_smoke() -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="ea005-atomic-", dir=RESULT_DIR) as directory:
        root = Path(directory)
        target = root / "collision.json"

        def create_collision(path: Path) -> None:
            path.write_text("{}\n", encoding="utf-8")

        collision_caught = False
        try:
            _atomic_write_exclusive(target, {"fixture": True}, prelink_hook=create_collision)
        except FileExistsError:
            collision_caught = True
        temp_files = list(root.glob("*.tmp-EA005-*"))
        target_unchanged = target.read_text(encoding="utf-8") == "{}\n"
        return {
            "collision_caught": collision_caught,
            "target_unchanged": target_unchanged,
            "temp_files_after_collision": [path.name for path in temp_files],
            "pass": collision_caught and target_unchanged and not temp_files,
        }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="EA-005 KMPC-035 external reproduction closure")
    parser.add_argument("--max-runtime-seconds", type=float, default=4.8)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--smoke", action="store_true")
    mode.add_argument("--audit", action="store_true")
    parser.add_argument("--output", type=Path)
    return parser


def main() -> int:
    args = _parser().parse_args()
    started = time.monotonic()
    progress = {"phase": "CLI_GUARDS"}
    try:
        if args.max_runtime_seconds != 4.8:
            raise ValueError("EA-005 preserves the exact KMPC-035 internal limit 4.8 s")
        if args.smoke and args.output is not None:
            raise ValueError("--output is forbidden in smoke mode")
        requested_output = CANONICAL_OUTPUT
        if args.output is not None:
            requested_output = args.output if args.output.is_absolute() else ROOT / args.output
        if requested_output.resolve() != CANONICAL_OUTPUT.resolve():
            raise ValueError("output must equal the EA-005 canonical reproduction path")
        if args.audit and CANONICAL_OUTPUT.exists():
            raise FileExistsError("canonical EA-005 output already exists before audit")

        progress["phase"] = "DELIVERY_INPUT_AND_SOURCE_GUARDS"
        delivery = _verify_delivery_inputs()
        if not delivery["runtime_inputs_pass"] or not delivery["sources_pass"]:
            raise RuntimeError("EA-005 delivery closure hash mismatch")

        progress["phase"] = "GUARDED_IMPORT"
        from scripts.baseScripts.p5_general_synchronous import cdi_support_ladder as audit

        if audit.REGRESSION_REL_TOL != FROZEN_PHYSICS_THRESHOLDS["regression_relative"]:
            raise RuntimeError("frozen regression relative threshold changed")
        if audit.REGRESSION_ABS_TOL != FROZEN_PHYSICS_THRESHOLDS["regression_absolute"]:
            raise RuntimeError("frozen regression absolute threshold changed")

        if args.smoke:
            progress["phase"] = "OFFICIAL_SMOKE"
            official_smoke = audit.run_smoke(args.max_runtime_seconds, RESULT_DIR)
            progress["phase"] = "ATOMIC_COLLISION_NEGATIVE_FIXTURE"
            atomic_fixture = _atomic_collision_smoke()
            passed = bool(official_smoke["passed"] and atomic_fixture["pass"])
            print(
                json.dumps(
                    {
                        "package_id": PACKAGE_ID,
                        "run_id": RUN_ID,
                        "smoke_pass": passed,
                        "official_smoke": official_smoke,
                        "atomic_collision_fixture": atomic_fixture,
                    },
                    sort_keys=True,
                ),
                flush=True,
            )
            return 0 if passed else 2

        progress["phase"] = "OFFICIAL_AUDIT_UNCHANGED_THRESHOLDS"
        official = audit.run_audit(args.max_runtime_seconds, RESULT_DIR)
        reference = json.loads(REFERENCE_RESULT.read_text(encoding="utf-8"))
        payload = {
            "package_id": PACKAGE_ID,
            "run_id": RUN_ID,
            "execution_status": "TECHNICAL_COMPLETE_EXTERNAL_REPRODUCTION_CANDIDATE",
            "delivery_closure": delivery,
            "runtime_environment": _runtime_environment(),
            "official_KMPC035_payload_unchanged": official,
            "frozen_physics_thresholds": FROZEN_PHYSICS_THRESHOLDS,
            "frozen_thresholds_changed": False,
            "cross_platform_reference_diagnostic": _cross_platform_diagnostic(reference, official),
            "absolute_branch_diagnostics": _absolute_branch_diagnostics(official),
            "z_scan_diagnostic": _z_scan_diagnostic(official),
            "process_wall_seconds": time.monotonic() - started,
            "score_effect": "NONE",
            "prediction_table_effect": "NONE",
            "release_trigger": "NONE",
            "zenodo_trigger": "NONE",
            "orchestrator_verdict": "NOT_ASSIGNED_BY_SCRIPT",
        }
        progress["phase"] = "IMMUTABLE_PUBLISH"
        _atomic_write_exclusive(CANONICAL_OUTPUT, payload)
        print(
            json.dumps(
                {
                    "package_id": PACKAGE_ID,
                    "candidate": official["candidate_interpretation_not_verdict"],
                    "official_regression_pass": official["regression_against_C1"]["pass"],
                    "cross_platform_diagnostic_pass": payload["cross_platform_reference_diagnostic"]["pass_diagnostic_only"],
                    "output": str(CANONICAL_OUTPUT.resolve()),
                },
                sort_keys=True,
            ),
            flush=True,
        )
        return 0
    except Exception as exc:
        failure = {
            "package_id": PACKAGE_ID,
            "run_id": RUN_ID,
            "execution_status": "TECHNICAL_FAILURE_NO_PHYSICS_VERDICT",
            "phase": progress["phase"],
            "exception_type": type(exc).__name__,
            "message": str(exc),
            "process_wall_seconds": time.monotonic() - started,
            "score_effect": "NONE",
            "prediction_table_effect": "NONE",
            "release_trigger": "NONE",
            "zenodo_trigger": "NONE",
        }
        try:
            _atomic_write_exclusive(FAILURE_OUTPUT, failure)
        except FileExistsError:
            failure["failure_write_status"] = "PRESERVED_EXISTING_FAILURE_FILE"
        print(json.dumps(_json_safe(failure), sort_keys=True), file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
