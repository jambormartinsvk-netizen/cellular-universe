#!/usr/bin/env python
"""Bounded, no-import L1 audit of formulation propagation in selected sources."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import time


ROOT = Path(__file__).resolve().parent.parent


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def write_once(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f"refusing to overwrite immutable output: {path}")
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def source_text(paths: tuple[str, ...], started: float, limit: float) -> str:
    chunks: list[str] = []
    for relative in paths:
        if time.monotonic() - started > limit:
            raise TimeoutError("L1 internal deadline exceeded")
        path = ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(path)
        chunks.append(path.read_text(encoding="utf-8").lower())
    return "\n".join(chunks)


def main() -> int:
    args = parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        raise ValueError("max-runtime-seconds must be in (0, 5]")
    started = time.monotonic()
    groups = {
        "K4_86_test_field": {
            "paths": ("scripts/86_script_A2_K4_3b_RG_general_synchronous_K4_test_field_response.py",),
            "required": ("uc", "ud", "g = lam / e_v", "s2 ="),
            "forbidden": ("k_mpc = 0.05",),
            "expected_status": "TEST_FIELD_PRESERVES_UC_NOT_FULL_CONSTRAINTS",
        },
        "K7_legacy": {
            "paths": (
                "scripts/197_script_A2_K4_C7_7c_K7c_P1_clean_standalone_RK4.py",
                "scripts/209_script_A2_K4_C7_7c_K7c_P4a_single_case_solver.py",
                "scripts/213_script_A2_K4_C7_7c_K7d_integrated_G4_G6_G7_runner.py",
            ),
            "required": ("k_mpc = 0.05", "k_mpc", "physical_rhs"),
            "forbidden": (),
            "forbidden_identifiers": ("uc",),
            "expected_status": "HISTORICAL_PHYSICALLY_LIMITED_MISSING_UC_AND_K_BACKGROUND",
        },
        "G8_screen": {
            "paths": (
                "scripts/221_script_A2_K4_C7_7c_K7_G8_S0_S1_structural_audit.py",
                "scripts/baseScripts/a2_k4_g8/structural.py",
            ),
            "required": ("u_b", "full_momentum", "k7_momentum"),
            "forbidden": ("oc * uc",),
            "expected_status": "SCREEN_ONLY_PHYSICALLY_LIMITED_MISSING_CDM_MOMENTUM",
        },
        "P5_preflight": {
            "paths": (
                "scripts/236_script_KMPC_003_P5_1_general_synchronous_static_ledger.py",
                "scripts/baseScripts/p5_general_synchronous/coefficient_identities.py",
            ),
            "required": ("uc", "ub", "m_full", "gamma", "beta_c"),
            "forbidden": ("k_mpc = 0.05",),
            "expected_status": "CURRENT_STATIC_PREFLIGHT_NOT_YET_CONSTRAINT_OR_ODE",
        },
    }
    rows: dict[str, object] = {}
    all_expected = True
    for name, item in groups.items():
        text = source_text(item["paths"], started, args.max_runtime_seconds)
        present = {token: token in text for token in item["required"]}
        absent = {token: token not in text for token in item["forbidden"]}
        absent.update({
            f"identifier:{token}": re.search(rf"(?<![A-Za-z0-9_]){re.escape(token)}(?![A-Za-z0-9_])", text) is None
            for token in item.get("forbidden_identifiers", ())
        })
        matched = all(present.values()) and all(absent.values())
        rows[name] = {
            "paths": list(item["paths"]),
            "required_present": present,
            "forbidden_absent": absent,
            "expected_status": item["expected_status"],
            "matches_preregistered_map": matched,
        }
        all_expected = all_expected and matched
    payload = {
        "test": "LINEAGE-L1 static formulation-to-source contract audit",
        "scope": "source text only; no imports, ODE, score, or historical rewrite",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "contract": "C1 energy-frame; C2 gamma; C3 exact background; C4 Uc/Ub; C5 k role",
        "groups": rows,
        "verdict": "PASS_L1_EXPECTED_LINEAGE_MAP" if all_expected else "STOP_L1_SOURCE_MAP_CHANGED",
    }
    write_once(args.output, payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if all_expected else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
