#!/usr/bin/env python
"""P5.3g6 RERUN1: exact photon gauge bridge with corrected audit-marker path."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import time

import sympy as sp


ROOT = Path(__file__).resolve().parent.parent
CAMB_SYMBOLIC = ROOT / ".deps" / "python" / "camb" / "symbolic.py"
AUDIT73 = ROOT / "Audit" / "A2_K4_3B_HIERARCHY_MODE_TAXONOMY_RECOMBINATION_AUDIT.md"
SOURCE84 = ROOT / "scripts" / "84_script_A2_K4_3b_RG_CLASS_analytic_collective_seed_CAMB_crosscheck.py"


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
    camb = CAMB_SYMBOLIC.read_text(encoding="utf-8")
    audit73 = AUDIT73.read_text(encoding="utf-8")
    source84 = SOURCE84.read_text(encoding="utf-8")
    ast.parse(camb, filename=CAMB_SYMBOLIC.name)
    ast.parse(source84, filename=SOURCE84.name)
    k, qg, hdot, etadot = sp.symbols("k q_gamma hdot eta_dot", nonzero=True)
    sigma_syn = (hdot + 6 * etadot) / (2 * k)
    metric_residual = sp.simplify(sp.Rational(8, 15) * k * sigma_syn - (sp.Rational(4, 15) * hdot + sp.Rational(8, 5) * etadot))
    theta_from_qg = sp.Rational(3, 4) * k * qg
    velocity_residual = sp.simplify(sp.Rational(2, 5) * k * qg - sp.Rational(8, 15) * theta_from_qg)
    checks = {
        "camb_declares_general_metric_shear": 'sigma = LinearPerturbation("sigma", description="shear"' in camb,
        "camb_declares_synchronous_shear_map": "Eq(sigma, (hdot_s + diff(6 * eta_s, t)) / 2 / k)" in camb,
        "camb_declares_photon_l2_metric_source": "eq = eq + 8 * k / 15 * sigma + opacity * polter" in camb,
        "seed84_declares_synchronous_CDM_frame": "leading synchronous-gauge" in source84,
        "seed84_declares_qg_theta_normalization": "qg = 4.0 * tg / (3.0 * k)" in source84,
        "audit73_contains_historical_photon_lower_equation": "F_{\\gamma2}'=\\frac8{15}\\theta_\\gamma" in audit73,
        "synchronous_metric_source_identity_is_exact": metric_residual == 0,
        "synchronous_velocity_source_identity_is_exact": velocity_residual == 0,
    }
    if time.monotonic() - started > args.max_runtime_seconds:
        raise TimeoutError("P5.3g6 RERUN1 gauge bridge exceeded internal deadline")
    passed = all(checks.values())
    payload = {
        "test": "KMPC-021 P5.3g6 RERUN1 synchronous photon l=2 gauge bridge",
        "scope": "corrected marker path plus source provenance/exact algebra; no full seed, physical residual, ODE, recombination, P5.4, G8, or score",
        "rerun_reason": "PF-054: historical photon equation lives in audit Markdown, not script 73",
        "synchronous_sigma": str(sigma_syn),
        "metric_identity_residual": str(metric_residual),
        "velocity_identity_residual": str(velocity_residual),
        "synchronous_photon_l2_drive": str(sp.Rational(2, 5) * k * qg + sp.Rational(8, 15) * k * sigma_syn),
        "checks": checks,
        "source_sha256": {
            CAMB_SYMBOLIC.name: hashlib.sha256(camb.encode("utf-8")).hexdigest(),
            AUDIT73.name: hashlib.sha256(audit73.encode("utf-8")).hexdigest(),
            SOURCE84.name: hashlib.sha256(source84.encode("utf-8")).hexdigest(),
        },
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
        "next_step": "P5.3g7: compose a full two-start seed and test actual Einstein residuals" if passed else "STOP: retain gauge-bridge review; do not compose a full seed",
        "verdict": "FORMULA_PASS_P5_3G6_RERUN1_SYNCHRONOUS_PHOTON_GAUGE_BRIDGE" if passed else "STOP_P5_3G6_RERUN1_SYNCHRONOUS_PHOTON_GAUGE_BRIDGE",
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
