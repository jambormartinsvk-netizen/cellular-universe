#!/usr/bin/env python
"""Locate the exact rows behind script 121 versus script 108 disagreement.

This bounded algebraic audit evaluates the script-108 rank-7 matrix on the
zero-matter shear-layer coefficients produced by script 121.  A nonzero
``A @ x_121 - b_108`` identifies a source ledger mismatch, not failure of the
new 11-row system.  Values are copied verbatim from the immutable JSON output
of script 121 and are labelled as such.
"""

from __future__ import annotations

import argparse
import json
import time

import numpy as np


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=5.0)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 10.0:
        parser.error("runtime must be in (0,10]")
    started = time.monotonic()

    delta = 0.02297
    p = 4 - 3 * delta
    neff = 3.046 + 0.0535
    rn = 0.2271 * neff / (1 + 0.2271 * neff)
    rg = 1 - rn
    vectors_121 = {
        "NID": np.array([
            1.7490961803923177e-16, 0.0011167485818317543,
            -0.023791103995262734, 0.033799153263612595,
            0.0019142817922588693, -0.004711417514867508,
            -0.005866431787257087,
        ]),
        "NIV": np.array([
            1.4114228015504883e-16, 0.008794109540570546,
            -0.07137331198578811, 0.10139745979083689,
            0.0261502001285532, -0.05982554640731107,
            -0.013244204325711093,
        ]),
    }
    rows = ("gamma_continuity", "gamma_Euler", "nu_continuity",
            "nu_shear", "nu_Euler", "Einstein_00", "Einstein_0i",
            "Einstein_trace", "Einstein_traceless")
    results = {}
    checks = {}
    for mode, m in (("NID", 2), ("NIV", 1)):
        r = p + m
        if mode == "NID":
            dg, dn = rn/(6*rg), -1/6
            ugl, unl = -rn/(4*rg), 1/4
            sig, eta = 1/(2*(4*rn+15)), -rn/(6*(4*rn+15))
        else:
            dg, dn = rn/rg, -1.0
            ugl, unl = -3*rn/(4*rg), 0.75
            sig, eta = 1/(4*rn+5), -rn/(4*rn+5)
        etax = m*eta
        ugm = dg/(4*(m+1))
        unm = (dn/4-sig)/(m+1)
        early = p+m-2
        factor = p/(2*(early+1))
        uge, une = factor*ugl, factor*unl
        b108 = np.array([
            4/3*(ugl-uge), p*ugm/2,
            4/3*(unl-une), 8/15*(uge-ugl), p*unm/2,
            0.0, -etax, 0.0, -3*p*etax+12*rn*sig,
        ])
        matrix = np.array([
          [2/3,0,r,0,0,0,0], [0,0,-1/4,0,r+1,0,0],
          [2/3,0,0,r,0,0,0], [-4/15,-8/5*r,0,0,0,0,2*r],
          [0,0,0,-1/4,0,r+1,1], [-1/2,0,1.5*rg,1.5*rn,0,0,0],
          [0,r,0,0,-2*rg,-2*rn,0], [r+1,0,3*rg,3*rn,0,0,0],
          [r+1,6*r*(r+1),0,0,0,0,12*rn],
        ], dtype=float)
        implied = matrix @ vectors_121[mode]
        difference = implied - b108
        row_difference = {row: float(value) for row, value in zip(rows, difference)}
        nonzero = {row: value for row, value in row_difference.items()
                   if abs(value) > 1e-11}
        checks[f"{mode}_only_neutrino_or_Einstein_source_rows_differ"] = all(
            row in {"nu_shear", "nu_Euler", "Einstein_0i", "Einstein_traceless"}
            for row in nonzero
        )
        checks[f"{mode}_source_difference_is_nonzero"] = bool(nonzero)
        results[mode] = {
            "row_order": list(rows),
            "A_times_script121_vector": implied.tolist(),
            "script108_source": b108.tolist(),
            "difference_by_row": row_difference,
            "nonzero_difference_above_1e-11": nonzero,
            "max_absolute_difference": float(np.max(np.abs(difference))),
        }

    passed = all(checks.values())
    output = {
        "test": "BR3B-2f-5 script-108 source-vector difference audit",
        "checks": checks,
        "mode_results": results,
        "execution_verdict": (
            "PASS_DIFFERENCE_LOCALIZED" if passed else "REVIEW_DIFFERENCE_UNCLOSED"
        ),
        "interpretation_limit": (
            "localization alone does not decide whether script 108 or script 121 "
            "has the correct source; derive the full source ledger independently"
        ),
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover
        print(json.dumps({"execution_verdict": "ERROR_UNCLOSED", "error": repr(exc)}))
        raise SystemExit(2)
