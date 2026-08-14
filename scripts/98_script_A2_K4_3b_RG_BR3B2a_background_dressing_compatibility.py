#!/usr/bin/env python
"""BR3B-2a: exact compatibility conditions for background dressing.

BR3B-1 proved that a fuel perturbation inserted as an isolated stress source
is not a conserved coefficient source.  Here four symbolic dressing terms are
added to the synchronous Einstein coefficient equations (00, 0i, trace and
traceless).  The left-null/Bianchi identities then determine the two exact
compatibility conditions which every physical radiation-background expansion
must satisfy.

This is a diagnostic gate, not a fit and not yet the complete BR3B solution.
The deliberately minimal trace/traceless completion is reported only as an
algebraic witness; BR3B-2b must derive the dressing from the expanded
background and base seed rather than choose it freely.
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
            raise TimeoutError("BR3B-2a deadline exceeded")

    delta = sp.Rational(2297, 100000)
    p = 4 - 3 * delta
    neff = sp.Rational(3046, 1000) + sp.Rational(535, 10000)
    rg = sp.simplify(1 / (1 + sp.Rational(2271, 10000) * neff))
    rf = sp.simplify(1 - rg)
    modes = {"AD": 2, "CDI": 1, "BI": 1, "NID": 3, "NIV": 2}
    c00, c0i, ctr, ctl = sp.symbols("C00 C0i Ctr Ctl")
    dressing = sp.Matrix([0, 0, 0, 0, 0, c00, c0i, ctr, ctl])

    results: dict[str, object] = {}
    checks: dict[str, bool] = {}

    for mode, n_int in modes.items():
        n = sp.Integer(n_int)
        r = sp.simplify(p + n)
        den = sp.simplify((n - 1) * (n + 6 - 3 * delta) + 9 * (2 - delta))
        df = sp.simplify(-delta * (n - 1) / (2 * den))
        uf = sp.simplify(-1 / (2 * den))
        pf = sp.simplify(-delta * (n + 5 - 3 * delta) / (2 * den))
        mf = sp.simplify(delta * uf)

        # Unknowns: h_x, eta, delta_gamma, delta_fs, U_gamma, U_fs, sigma_fs.
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
        fuel_rhs = sp.Matrix([
            0, 0, 0, 0, 0,
            -sp.Rational(3, 2) * df,
            sp.Rational(3, 2) * mf,
            -9 * pf,
            0,
        ])

        left_null = matrix.T.nullspace()
        compatibility = [sp.factor((vector.T * (fuel_rhs + dressing))[0])
                         for vector in left_null]
        solved = sp.solve(compatibility, (ctr, ctl), dict=True)
        unique_completion = len(solved) == 1 and ctr in solved[0] and ctl in solved[0]
        checks[f"{mode}_two_bianchi_compatibility_conditions"] = len(compatibility) == 2
        checks[f"{mode}_trace_completion_unique_given_C00_C0i"] = unique_completion

        if not unique_completion:
            witness = None
            augmented_rank = None
            response = None
        else:
            completion = solved[0]
            minimal = {c00: 0, c0i: 0,
                       ctr: completion[ctr].subs({c00: 0, c0i: 0}),
                       ctl: completion[ctl].subs({c00: 0, c0i: 0})}
            completed_rhs = sp.simplify((fuel_rhs + dressing).subs(minimal))
            augmented_rank = int(matrix.row_join(completed_rhs).rank())
            response_set = sp.linsolve((matrix, completed_rhs))
            response_tuple = list(response_set)[0]
            response = [str(sp.factor(value)) for value in response_tuple]
            witness = {
                "assumption": "C00=C0i=0; algebraic witness only",
                "Ctr": str(sp.factor(minimal[ctr])),
                "Ctl": str(sp.factor(minimal[ctl])),
            }
            checks[f"{mode}_minimal_witness_restores_rank_compatibility"] = (
                augmented_rank == int(matrix.rank())
            )

        results[mode] = {
            "n": n_int,
            "r": str(r),
            "compatibility_conditions_equal_zero": [str(item) for item in compatibility],
            "required_completion": ({str(key): str(sp.factor(value))
                                     for key, value in solved[0].items()}
                                    if unique_completion else None),
            "minimal_algebraic_witness": witness,
            "rank_A": int(matrix.rank()),
            "rank_augmented_after_minimal_witness": augmented_rank,
            "induced_response_for_minimal_witness": response,
        }
        deadline()

    passed = bool(checks) and all(checks.values())
    output = {
        "test": "A2-K4.3b-RG-BR3B-2a background-dressing compatibility",
        "delta": str(delta),
        "dressing_convention": "C00,C0i,Ctr,Ctl are additive RHS coefficients in the four Einstein equations",
        "mode_results": results,
        "checks": checks,
        "execution_verdict": ("PASS_EXACT_COMPATIBILITY_CONDITIONS_DERIVED"
                              if passed else "REVIEW_BR3B2A"),
        "physical_verdict": "UNCLOSED: algebra permits a completion, but BR3B-2b must derive it from the radiation-background/base-seed expansion",
        "K4_3b_RG_verdict": "NEUZAVRETA_BR3B2B_PHYSICAL_BACKGROUND_DRESSING_REQUIRED",
        "canonical_score": "60/100 = G6",
        "next_step": "BR3B-2b derive C00,C0i,Ctr,Ctl from Omega/background and base-seed cross coefficients, then compare with these exact identities",
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
    except Exception as exc:  # pragma: no cover - preserved audit failure record
        print(json.dumps({"execution_verdict": "ERROR_UNCLOSED", "error": repr(exc)}))
        raise SystemExit(2)
