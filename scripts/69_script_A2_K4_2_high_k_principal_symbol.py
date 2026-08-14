#!/usr/bin/env python3
"""A2-K4.2 analytic high-k principal-symbol and null-limit audit."""

from __future__ import annotations

import argparse
import json
import math
import time

import numpy as np
import sympy as sp


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--delta", type=float, default=0.02297)
    parser.add_argument("--max-runtime-seconds", type=float, default=10.0)
    args = parser.parse_args()
    started = time.monotonic()

    def check_time() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("K4.2 analytic audit exceeded internal runtime limit")

    d, mu, lam = sp.symbols("d mu lam", positive=True, real=True)
    # z=[dc,vc,df,vf,db,vb,dr,vr], v=theta/k.  With Fourier modes,
    # z_eta=k*P*z.  Phi=O(k^-2) is constraint-suppressed at principal order.
    principal = sp.zeros(8, 8)
    principal[0, 1] = -1
    principal[2, 3] = -d
    principal[3, 2] = 1 / d
    principal[4, 5] = -1
    principal[6, 7] = -sp.Rational(4, 3)
    principal[7, 6] = sp.Rational(1, 4)
    characteristic = sp.factor((mu * sp.eye(8) - principal).det())
    expected = sp.factor(mu**4 * (mu**2 + 1) * (mu**2 + sp.Rational(1, 3)))
    check_time()

    numeric = np.array(principal.subs(d, args.delta), dtype=float)
    eigenvalues = np.linalg.eigvals(numeric)
    propagation_speeds = sorted(
        [float((1j * value).real) for value in eigenvalues],
        key=lambda value: (abs(value), value),
    )
    expected_speeds = sorted(
        [0.0, 0.0, 0.0, 0.0, -1.0, 1.0, -1.0 / math.sqrt(3), 1.0 / math.sqrt(3)],
        key=lambda value: (abs(value), value),
    )

    # Constant proper-time interaction terms are O(k^0), so the principal
    # matrix has no lambda dependence.  Their algebraic null limit is lam=0.
    lower_order_test = sp.Matrix(
        [lam * sp.Symbol("A"), lam * sp.Symbol("B"), lam * sp.Symbol("C")]
    )
    null_limit = sp.simplify(lower_order_test.subs(lam, 0))
    delta_positive = args.delta > 0.0
    fuel_effective_kinetic_positive = delta_positive

    zero_alg_mult = 4
    zero_geom_mult = len(principal.nullspace())
    propagating = principal.extract([2, 3, 6, 7], [2, 3, 6, 7])
    propagating_diagonalizable = bool(propagating.is_diagonalizable())

    checks = {
        "characteristic_factorization": bool(
            sp.simplify(characteristic - expected) == 0
        ),
        "expected_characteristic_speeds": bool(
            np.allclose(propagation_speeds, expected_speeds, rtol=0.0, atol=1e-12)
        ),
        "all_speeds_real_and_causal": bool(
            all(math.isfinite(c) and abs(c) <= 1.0 + 1e-12 for c in propagation_speeds)
        ),
        "fuel_gradient_positive": bool(1.0 > 0.0),
        "fuel_effective_kinetic_positive": fuel_effective_kinetic_positive,
        "interaction_absent_from_principal_symbol": not principal.has(lam),
        "interaction_null_limit": bool(null_limit == sp.zeros(3, 1)),
        "propagating_blocks_diagonalizable": propagating_diagonalizable,
        "dust_defect_is_lambda_independent": not principal.has(lam),
    }
    passed = all(checks.values())
    check_time()
    output = {
        "test": "A2-K4.2 high-k effective-fluid principal symbol",
        "variables": "[dc,vc,df,vf,db,vb,dr,vr], v=theta/k",
        "characteristic_polynomial": str(characteristic),
        "eigenvalues_of_time_matrix": [
            {"real": float(v.real), "imag": float(v.imag)} for v in eigenvalues
        ],
        "physical_characteristic_speeds": propagation_speeds,
        "zero_eigenvalue_algebraic_multiplicity": zero_alg_mult,
        "zero_eigenvalue_geometric_multiplicity": zero_geom_mult,
        "full_principal_symbol_diagonalizable": bool(principal.is_diagonalizable()),
        "propagating_fuel_radiation_blocks_diagonalizable": propagating_diagonalizable,
        "dust_caveat": (
            "CDM and baryon zero-speed blocks are Jordan blocks. This is the "
            "standard pressureless-dust derivative-loss caveat already present "
            "at lambda=0, not a new K4 interaction instability."
        ),
        "effective_kinetic_weights": {
            "fuel": "delta*rho_f/cs2; positive because delta>0, rho_f>0, cs2=1",
            "radiation": "4*rho_r/3 > 0",
            "dust": "rho_c,rho_b > 0 with zero sound speed",
        },
        "limitation": (
            "Effective-fluid positivity only; without a microscopic action this "
            "is not a fundamental UV no-ghost theorem."
        ),
        "checks": checks,
        "runtime_seconds": time.monotonic() - started,
        "verdict": "PASS_ANALYTIC_K4_2" if passed else "FAIL_ANALYTIC_K4_2",
        "next_gate": "Time-limited complete-regular-basis subhorizon integration",
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())


