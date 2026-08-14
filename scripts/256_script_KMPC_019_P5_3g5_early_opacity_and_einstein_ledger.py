#!/usr/bin/env python
"""Bounded P5.3g5 early-opacity and independent source-ledger screen."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys
import time

import sympy as sp


ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "scripts" / "baseScripts" / "p5_general_synchronous"
SOURCE88 = ROOT / "scripts" / "88_script_A2_K4_3b_RG_BR1_synchronous_Einstein_and_transfer_ledger.py"
SOURCE09 = ROOT / "Independent_Audits" / "K_MPC_0_05" / "09_P4_EXACT_A1_BACKGROUND_REDERIVATION_PLAN_AND_SOURCE_AUDIT_SK.md"
sys.path.insert(0, str(BASE))
from early_opacity_ledger import early_opacity_identities, synchronous_constraint_sources  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 5.0:
        raise ValueError("max-runtime-seconds must be in (0,5]")
    started = time.monotonic()
    if args.output.exists():
        raise FileExistsError(args.output)
    source88 = SOURCE88.read_text(encoding="utf-8")
    source09 = SOURCE09.read_text(encoding="utf-8")
    ast.parse(source88, filename=SOURCE88.name)
    early = early_opacity_identities()
    ledger = synchronous_constraint_sources()
    a = early["a"]
    checks = {
        "source88_declares_synchronous_00_constraint": "C00 = q**2 * eta" in source88,
        "source88_declares_synchronous_0i_constraint": "C0i = etax" in source88,
        "source09_declares_exact_k_independent_Hconf": "Hconf(a)" in source09 and "nezávislé od Fourierovho módu" in source09,
        "fully_ionized_opacity_times_a_squared_is_constant": sp.simplify(early["opacity_times_a_squared"] - sp.Symbol("n_e0", positive=True) * sp.Symbol("sigma_T", positive=True)) == 0,
        "collision_time_scales_as_a_squared": sp.simplify(sp.diff(early["tau_c"], a) * a - 2 * early["tau_c"]) == 0,
        "radiation_era_Hconf_tau_c_scales_as_a": sp.simplify(sp.diff(early["hconf_tau_c"], a) * a - early["hconf_tau_c"]) == 0,
        "radiation_era_k_tau_c_scales_as_a_squared": sp.simplify(sp.diff(early["k_tau_c"], a) * a - 2 * early["k_tau_c"]) == 0,
        "early_tca_limits_are_zero": sp.limit(early["hconf_tau_c"], a, 0, dir="+") == 0 and sp.limit(early["k_tau_c"], a, 0, dir="+") == 0,
        "C00_contains_total_density_source": ledger["C00"].has(ledger["drho"]),
        "C0i_contains_Uc_with_nonzero_weight": sp.simplify(sp.diff(ledger["C0i"], ledger["Uc"])) == -sp.Rational(3, 2) * ledger["Xc"] / sp.Symbol("E", positive=True)**2,
        "C0i_contains_Ub_with_nonzero_weight": sp.simplify(sp.diff(ledger["C0i"], ledger["Ub"])) == -sp.Rational(3, 2) * ledger["Xb"] / sp.Symbol("E", positive=True)**2,
        "C0i_contains_Uf_with_enthalpy_weight": sp.simplify(sp.diff(ledger["C0i"], ledger["Uf"])) == -sp.Rational(3, 2) * ledger["delta"] * ledger["Xf"] / sp.Symbol("E", positive=True)**2,
    }
    if time.monotonic() - started > args.max_runtime_seconds:
        raise TimeoutError("P5.3g5 symbolic audit exceeded internal deadline")
    passed = all(checks.values())
    payload = {
        "test": "KMPC-019 P5.3g5 early fully-ionized opacity and independent synchronous source ledger",
        "scope": "fully-ionized radiation-era power counting and independently assembled 00/0i source content; no recombination x_e(a), seed residual, ODE, P5.4, G8, or score",
        "early_opacity": {key: str(value) for key, value in early.items() if key != "a"},
        "momentum_source": str(ledger["momentum"]),
        "checks": checks,
        "source_sha256": {SOURCE88.name: hashlib.sha256(source88.encode("utf-8")).hexdigest(), SOURCE09.name: hashlib.sha256(source09.encode("utf-8")).hexdigest()},
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "next_step": "P5.3g6: construct full photon+neutrino regular seed and check its actual Einstein residual at two starts" if passed else "STOP: repair early-opacity scaling or missing species momentum before full seed work",
        "verdict": "FORMULA_PASS_P5_3G5_EARLY_OPACITY_AND_INDEPENDENT_LEDGER_SCOPE" if passed else "STOP_P5_3G5_EARLY_OPACITY_AND_INDEPENDENT_LEDGER",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if passed else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as error:
        print(json.dumps({"verdict": "TIMEOUT_UNCLOSED", "error": str(error)}))
        raise SystemExit(124)
