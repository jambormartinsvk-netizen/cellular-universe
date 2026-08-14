#!/usr/bin/env python
"""BR3B-2c: physical background dressing of the common h_x sector.

For h_x = a^n (unit coefficient), expand the radiation-dominated background
with y=Omega_f proportional to a^p, p=4-3*delta.  The expansion fixes, rather
than fits, the Einstein dressing and the photon/free-streaming Euler forcing.
The two Bianchi compatibility conditions are tested exactly.

NID and NIV also contain lower-power compensated radiation sectors.  Passing
this script proves the common h_x-driven sector only; it deliberately leaves
those additional sectors to BR3B-2d.
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
            raise TimeoutError("BR3B-2c deadline exceeded")

    delta = sp.Rational(2297, 100000)
    p = 4 - 3 * delta
    neff = sp.Rational(3046, 1000) + sp.Rational(535, 10000)
    rg = sp.simplify(1 / (1 + sp.Rational(2271, 10000) * neff))
    rf = sp.simplify(1 - rg)
    modes = {"AD": 2, "CDI": 1, "BI": 1, "NID": 3, "NIV": 2}
    eta_x, photon_u = sp.symbols("eta_x U_gamma")
    # Standard 0i constraint at the base coefficient:
    # eta_x = 2 (R_gamma U_gamma + R_fs U_fs).
    fs_u = sp.simplify((eta_x / 2 - rg * photon_u) / rf)

    checks: dict[str, bool] = {}
    results: dict[str, object] = {}
    for mode, n_int in modes.items():
        n = sp.Integer(n_int)
        r = sp.simplify(n + p)

        # Fuel coefficients per unit h_x, established in BR3A.
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

        # Exact O(y) dressing.  h_x has unit coefficient.  The trace terms
        # use the base Einstein equations; no observational number is fitted.
        jge = sp.simplify(p * photon_u / 2)
        jne = sp.simplify(p * fs_u / 2)
        c00 = sp.Rational(1, 2)
        c0i = -eta_x
        ctr = -sp.simplify(n + 1 + p / 2)
        ctl = -sp.simplify((n + 1 + p / 2) * (1 + 6 * eta_x))
        physical_dressing = sp.Matrix([
            0, jge, 0, 0, jne, c00, c0i, ctr, ctl
        ])

        compatibility = [sp.factor((vector.T * (fuel + physical_dressing))[0])
                         for vector in matrix.T.nullspace()]
        compatible = all(sp.simplify(value) == 0 for value in compatibility)
        augmented_rank = int(matrix.row_join(fuel + physical_dressing).rank())
        checks[f"{mode}_physical_hx_dressing_satisfies_both_Bianchi_identities"] = compatible
        checks[f"{mode}_physical_hx_dressing_restores_rank_compatibility"] = (
            augmented_rank == int(matrix.rank()) == 7
        )
        checks[f"{mode}_Euler_weight_is_fixed_by_standard_0i"] = (
            sp.simplify(rg * jge + rf * jne - p * eta_x / 4) == 0
        )
        results[mode] = {
            "n": n_int,
            "r": str(r),
            "Bianchi_residuals": [str(value) for value in compatibility],
            "fixed_dressing": {
                "Jgc": "0",
                "Jge": str(jge),
                "Jnc": "0",
                "Jns": "0 at this common sector; hierarchy-specific terms are BR3B-2d",
                "Jne": str(jne),
                "C00": str(c00),
                "C0i": str(c0i),
                "Ctr": str(ctr),
                "Ctl": str(ctl),
            },
            "rank_A": int(matrix.rank()),
            "rank_augmented": augmented_rank,
        }
        deadline()

    passed = bool(checks) and all(checks.values())
    output = {
        "test": "A2-K4.3b-RG-BR3B-2c physical common h_x sector",
        "background_expansion": "Omega_f=y~a^(4-3delta), Hconf_x/Hconf=-1+(4-3delta)y/2+O(y^2)",
        "normalization": "unit leading coefficient of h_x=a^n; eta_x and U_gamma remain symbolic",
        "mode_results": results,
        "checks": checks,
        "execution_verdict": ("PASS_PHYSICAL_HX_SECTOR_BIANCHI_COMPATIBILITY"
                              if passed else "FAIL_PHYSICAL_HX_SECTOR"),
        "physical_verdict": "the BR3B-1 obstruction is removed by mandatory background/Euler terms without a fitted coefficient",
        "scope_limit": "does not yet solve the extra lower-power compensated-radiation sectors of NID/NIV or the full hierarchy",
        "K4_3b_RG_verdict": "NEUZAVRETA_BR3B2D_NID_NIV_MULTIPOWER_SECTORS_REQUIRED",
        "canonical_score": "60/100 = G6",
        "next_step": "BR3B-2d enumerate and solve NID/NIV lower-power fractional sectors before the common h_x sector",
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
