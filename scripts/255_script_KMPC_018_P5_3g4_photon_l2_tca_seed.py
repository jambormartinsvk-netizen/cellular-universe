#!/usr/bin/env python
"""Bounded P5.3g4 algebraic photon l=2 / polarization TCA seed audit.

No ODE is solved.  The result is a structural first-order seed only, not a
K4-opacity-normalized or two-start full-hierarchy result.
"""

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
SOURCE73 = ROOT / "scripts" / "73_script_A2_K4_3b_hierarchy_and_regular_mode_taxonomy_audit.py"
SOURCE76 = ROOT / "scripts" / "76_script_A2_K4_3b_exact_CAMB_hierarchy_coefficients_alias_fixed.py"
SOURCE84 = ROOT / "scripts" / "84_script_A2_K4_3b_RG_CLASS_analytic_collective_seed_CAMB_crosscheck.py"
sys.path.insert(0, str(BASE))
from photon_tca_first_order import collision_block, first_order_solution  # noqa: E402


def source_ok(source73: str, source76: str, source84: str) -> dict[str, bool]:
    return {
        "source73_declares_collision_block": "collision_block = sp.Matrix(" in source73,
        "source73_declares_audited_first_row": "[-sp.Rational(9, 10), sp.Rational(1, 10), sp.Rational(1, 10)]" in source73,
        "source76_declares_J2_metric_and_polarization_source": "rhs += sp.Rational(8, 15) * cs.k * cs.sigma + cs.opacity * cs.polter" in source76,
        "source76_declares_polarization_equation": "def e_expected(ell: int):" in source76,
        "source84_returns_photon_velocity_qg": "qg = 4.0 * tg / (3.0 * k)" in source84,
        "source84_returns_qg_in_seed_vector": "return np.array([dg, db, dc, dn, qg, qn, eta_s]" in source84,
    }


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
    sources = {path.name: path.read_text(encoding="utf-8") for path in (SOURCE73, SOURCE76, SOURCE84)}
    for path, text in ((SOURCE73, sources[SOURCE73.name]), (SOURCE76, sources[SOURCE76.name]), (SOURCE84, sources[SOURCE84.name])):
        ast.parse(text, filename=path.name)
    checks = source_ok(sources[SOURCE73.name], sources[SOURCE76.name], sources[SOURCE84.name])
    if time.monotonic() - started > args.max_runtime_seconds:
        raise TimeoutError("P5.3g4 source provenance exceeded internal deadline")
    matrix, drive, solution, symbols = first_order_solution()
    epsilon, k, q_gamma, shear = symbols
    residual = sp.simplify(matrix * solution + epsilon * drive)
    zero_limit = solution.subs(epsilon, 0)
    checks.update({
        "collision_matrix_matches_shared_module": matrix == collision_block(),
        "collision_matrix_full_rank": matrix.rank() == 3,
        "collision_matrix_has_no_equilibrium_nullspace": len(matrix.nullspace()) == 0,
        "first_order_collision_residual_is_exact_zero": residual == sp.zeros(3, 1),
        "zeroth_tca_limit_is_exact_zero": zero_limit == sp.zeros(3, 1),
        "all_first_order_components_are_proportional_to_epsilon": all(sp.simplify(component.subs(epsilon, 0)) == 0 for component in solution),
        "solution_contains_photon_velocity_or_metric_drive": all(component.has(k) and (component.has(q_gamma) or component.has(shear)) for component in solution),
    })
    if time.monotonic() - started > args.max_runtime_seconds:
        raise TimeoutError("P5.3g4 algebra exceeded internal deadline")
    passed = all(checks.values())
    payload = {
        "test": "KMPC-018 P5.3g4 first-order photon l=2/polarization TCA algebra",
        "scope": "exact collision-block algebra only; no K4 opacity history, time-power assignment, two-start test, ODE, P5.4, G8, or score",
        "basis": ["F_gamma2", "G_gamma0", "G_gamma2"],
        "tca_definition": "epsilon = 1/opacity; first nonzero multipoles solve C X + epsilon D = 0",
        "first_order_truncation": "D retains the audited l=2 q_gamma/metric drive. l=3 and higher hierarchy terms are deliberately deferred to the full-hierarchy gate.",
        "collision_matrix": [[str(value) for value in row] for row in matrix.tolist()],
        "collision_determinant": str(matrix.det()),
        "drive": [str(value) for value in drive],
        "solution": {name: str(value) for name, value in zip(("F_gamma2", "G_gamma0", "G_gamma2"), solution)},
        "collision_residual": [str(value) for value in residual],
        "checks": checks,
        "source_sha256": {name: hashlib.sha256(text.encode("utf-8")).hexdigest() for name, text in sources.items()},
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "next_step": "P5.3g5: bind a K4 opacity/time-power seed and an independent Einstein ledger; then test full photon+neutrino seed at two starts" if passed else "STOP: repair source provenance or first-order collision algebra before any P5.3g5/P5.4 work",
        "verdict": "DERIVATION_PASS_P5_3G4_PHOTON_TCA_FIRST_ORDER_OPACITY_UNCLOSED" if passed else "STOP_P5_3G4_PHOTON_TCA_FIRST_ORDER",
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
