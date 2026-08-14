#!/usr/bin/env python
"""BR3B-2b: full source-vector Bianchi compatibility ledger.

The BR3B-2a algebraic witness dressed only the Einstein rows.  A physical
background expansion also drives the photon and free-streaming hierarchy.
This script derives, without choosing a seed amplitude, the two exact
compatibility identities for all nine row sources at once.

It is intentionally a formulation ledger.  BR3B-2c must populate every J
from the expanded background/base seed and pass the identities mode by mode.
"""

from __future__ import annotations

import argparse
import json
import time

import sympy as sp


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=10.0)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 15.0:
        parser.error("runtime must be in (0, 15]")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("BR3B-2b deadline exceeded")

    delta = sp.Rational(2297, 100000)
    p = 4 - 3 * delta
    neff = sp.Rational(3046, 1000) + sp.Rational(535, 10000)
    rg = sp.simplify(1 / (1 + sp.Rational(2271, 10000) * neff))
    rf = sp.simplify(1 - rg)

    # Additive right-hand-side sources in the five species/hierarchy rows.
    jgc, jge, jnc, jns, jne = sp.symbols("Jgc Jge Jnc Jns Jne")
    c00, c0i, ctr, ctl = sp.symbols("C00 C0i Ctr Ctl")
    generic_dressing = sp.Matrix([jgc, jge, jnc, jns, jne, c00, c0i, ctr, ctl])
    modes = {"AD": 2, "CDI": 1, "BI": 1, "NID": 3, "NIV": 2}

    rows: dict[str, object] = {}
    checks: dict[str, bool] = {}
    for mode, n_int in modes.items():
        n = sp.Integer(n_int)
        r = sp.simplify(p + n)
        den = sp.simplify((n - 1) * (n + 6 - 3 * delta) + 9 * (2 - delta))
        df = sp.simplify(-delta * (n - 1) / (2 * den))
        uf = sp.simplify(-1 / (2 * den))
        pf = sp.simplify(-delta * (n + 5 - 3 * delta) / (2 * den))
        mf = sp.simplify(delta * uf)

        matrix = sp.Matrix([
            [sp.Rational(2, 3), 0, r, 0, 0, 0, 0],
            [0, 0, -sp.Rational(1, 4), 0, r + 1, 0, 0],
            [sp.Rational(2, 3), 0, 0, r, 0, 0, 0],
            [-sp.Rational(4, 15), -sp.Rational(8, 5) * r, 0, 0, 0, 0, 2 * r],
            [0, 0, 0, -sp.Rational(1, 4), 0, r + 1, 1],
            [-sp.Rational(1, 2), 0, sp.Rational(3, 2) * rg,
             sp.Rational(3, 2) * rf, 0, 0, 0],
            [0, r, 0, 0, -2 * rg, -2 * rf, 0],
            [r + 1, 0, 3 * rg, 3 * rf, 0, 0, 0],
            [r + 1, 6 * r * (r + 1), 0, 0, 0, 0, 12 * rf],
        ])
        fuel = sp.Matrix([
            0, 0, 0, 0, 0,
            -sp.Rational(3, 2) * df,
            sp.Rational(3, 2) * mf,
            -9 * pf,
            0,
        ])
        left = matrix.T.nullspace()
        compatibility = [sp.factor((vector.T * (fuel + generic_dressing))[0])
                         for vector in left]
        completion = sp.solve(compatibility, (ctr, ctl), dict=True)
        unique = len(completion) == 1 and ctr in completion[0] and ctl in completion[0]
        checks[f"{mode}_two_total_Bianchi_conditions"] = len(compatibility) == 2
        checks[f"{mode}_Einstein_trace_sources_fixed_by_full_species_source"] = unique

        # Regression: setting all hierarchy sources to zero must reproduce
        # BR3B-2a exactly.  This detects sign drift between the two ledgers.
        if unique:
            reduced = {key: sp.factor(value.subs({jgc: 0, jge: 0, jnc: 0,
                                                  jns: 0, jne: 0}))
                       for key, value in completion[0].items()}
            expected_ctr = -(2 * (r - 1) * c00 + 3 * delta / 2)
            expected_ctl = -(2 * (r - 1) * c00 - 6 * (r + 1) * c0i
                             + 3 * delta / 2)
            checks[f"{mode}_zero_hierarchy_limit_matches_BR3B2a"] = (
                sp.simplify(reduced[ctr] - expected_ctr) == 0
                and sp.simplify(reduced[ctl] - expected_ctl) == 0
            )

        rows[mode] = {
            "n": n_int,
            "r": str(r),
            "compatibility_conditions_equal_zero": [str(value) for value in compatibility],
            "required_trace_sources": ({str(key): str(sp.factor(value))
                                        for key, value in completion[0].items()}
                                       if unique else None),
        }
        deadline()

    passed = bool(checks) and all(checks.values())
    output = {
        "test": "A2-K4.3b-RG-BR3B-2b full source-vector Bianchi ledger",
        "source_order": ["Jgc", "Jge", "Jnc", "Jns", "Jne",
                         "C00", "C0i", "Ctr", "Ctl"],
        "source_meaning": {
            "Jgc": "photon continuity RHS dressing",
            "Jge": "photon Euler RHS dressing",
            "Jnc": "free-streaming continuity RHS dressing",
            "Jns": "free-streaming shear RHS dressing",
            "Jne": "free-streaming Euler RHS dressing",
            "C00,C0i,Ctr,Ctl": "Einstein-row RHS dressing",
        },
        "mode_results": rows,
        "checks": checks,
        "execution_verdict": ("PASS_FULL_SOURCE_BIANCHI_IDENTITIES_DERIVED"
                              if passed else "REVIEW_BR3B2B"),
        "physical_verdict": "UNCLOSED: identities are exact, but their physical source coefficients are not yet populated",
        "K4_3b_RG_verdict": "NEUZAVRETA_BR3B2C_MODE_SOURCE_POPULATION_REQUIRED",
        "canonical_score": "60/100 = G6",
        "next_step": "BR3B-2c derive all nine dressing coefficients from the expanded background and each base seed, then test these identities without fitted terms",
        "runtime_limit_seconds": args.max_runtime_seconds,
        "runtime_seconds": time.monotonic() - started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict": "TIMEOUT_UNCLOSED", "error": str(exc)}))
        raise SystemExit(124)
    except Exception as exc:  # pragma: no cover
        print(json.dumps({"execution_verdict": "ERROR_UNCLOSED", "error": repr(exc)}))
        raise SystemExit(2)
