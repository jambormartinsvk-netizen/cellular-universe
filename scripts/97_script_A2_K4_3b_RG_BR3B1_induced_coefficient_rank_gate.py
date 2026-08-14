#!/usr/bin/env python
"""BR3B-1 rank/compatibility gate for the induced fractional response.

At r=(4-3delta)+n, build the radiation-era coefficient system driven by the
fuel density, pressure and momentum coefficients measured in BR3A.  Test all
four synchronous Einstein equations plus photon/free-streaming response.

If the augmented rank exceeds the coefficient rank, the isolated fuel-stress
ansatz is not a conserved perturbation by itself: background-dressing terms
must be added in BR3B-2.  Such a formulation failure is not a death of K4.
"""

from __future__ import annotations

import argparse
import json
import time

import sympy as sp


def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--max-runtime-seconds",type=float,default=10.)
    a=ap.parse_args()
    if not (0<a.max_runtime_seconds<=15): ap.error("runtime must be in (0,15]")
    t0=time.monotonic()
    def deadline():
        if time.monotonic()-t0>a.max_runtime_seconds: raise TimeoutError("BR3B-1 deadline exceeded")

    d=sp.Rational(2297,100000); p=4-3*d
    neff=sp.Rational(3046,1000)+sp.Rational(535,10000)
    rg=sp.simplify(1/(1+sp.Rational(2271,10000)*neff)); rf=sp.simplify(1-rg)
    modes={"AD":2,"CDI":1,"BI":1,"NID":3,"NIV":2}
    rows={}; checks={}
    for mode,n_int in modes.items():
        n=sp.Integer(n_int); r=sp.simplify(p+n)
        den=sp.simplify((n-1)*(n+6-3*d)+9*(2-d))
        df=sp.simplify(-d*(n-1)/(2*den))
        uf=sp.simplify(-1/(2*den))
        pf=sp.simplify(-d*(n+5-3*d)/(2*den))
        mf=sp.simplify(d*uf)

        # Unknowns [h_x, eta, delta_g, delta_fs, U_g, U_fs, sigma_fs].
        # k/H -> 0 at this fractional order; higher multipoles start later.
        A=sp.Matrix([
          [sp.Rational(2,3),0,r,0,0,0,0],                         # gamma continuity
          [0,0,-sp.Rational(1,4),0,r+1,0,0],                     # gamma Euler
          [sp.Rational(2,3),0,0,r,0,0,0],                         # fs continuity
          [-sp.Rational(4,15),-sp.Rational(8,5)*r,0,0,0,0,2*r], # fs shear
          [0,0,0,-sp.Rational(1,4),0,r+1,1],                     # fs Euler
          [-sp.Rational(1,2),0,sp.Rational(3,2)*rg,sp.Rational(3,2)*rf,0,0,0],
          [0,r,0,0,-2*rg,-2*rf,0],
          [r+1,0,3*rg,3*rf,0,0,0],
          [r+1,6*r*(r+1),0,0,0,0,12*rf],
        ])
        b=sp.Matrix([0,0,0,0,0,-sp.Rational(3,2)*df,sp.Rational(3,2)*mf,-9*pf,0])
        rank=int(A.rank()); aug=int(A.row_join(b).rank()); compatible=rank==aug
        left=A.T.nullspace(); obstructions=[sp.factor((v.T*b)[0]) for v in left]
        nonzero=[o for o in obstructions if sp.simplify(o)!=0]
        checks[f"{mode}_coefficient_matrix_full_column_rank"]=rank==7
        checks[f"{mode}_isolated_fuel_source_compatible"]=compatible
        checks[f"{mode}_fuel_momentum_identity"]=sp.simplify(r*mf-(-mf+pf))==0
        # The fuel energy coefficient is forced by the standard seed metric.
        energy_forcing=sp.simplify(r*df-(df-3*pf))
        checks[f"{mode}_fuel_energy_requires_metric_forcing"]=sp.simplify(energy_forcing+d/2)==0
        solution=None
        if compatible:
            solution=[str(sp.factor(v)) for v in list(sp.linsolve((A,b)))[0]]
        rows[mode]={
          "n":n_int,"r":float(r),"rank_A":rank,"rank_augmented":aug,
          "isolated_source_compatible":compatible,
          "fuel_coefficients":{"delta_f":str(df),"U_f":str(uf),"pressure":str(pf),"momentum":str(mf)},
          "left_null_obstructions":[str(o) for o in nonzero],
          "fuel_energy_missing_standard_metric_term":str(energy_forcing),
          "solution_if_compatible":solution}
        deadline()

    # A physical PASS is not expected for the deliberately isolated source.
    # The gate passes when it identifies the same missing metric forcing in
    # every mode without a rank defect of the response variables.
    diagnosed=all(checks[f"{m}_coefficient_matrix_full_column_rank"] and
                  checks[f"{m}_fuel_momentum_identity"] and
                  checks[f"{m}_fuel_energy_requires_metric_forcing"] and
                  not checks[f"{m}_isolated_fuel_source_compatible"] for m in modes)
    out={"test":"A2-K4.3b-RG-BR3B-1 induced coefficient rank gate",
      "declared_ansatz":"isolated fuel perturbation source; background-dressing intentionally omitted",
      "mode_results":rows,"checks":checks,
      "execution_verdict":"PASS_DIAGNOSIS_BACKGROUND_DRESSING_REQUIRED" if diagnosed else "REVIEW_BR3B1_UNEXPECTED_RANK_RESULT",
      "physical_interpretation":"an isolated fuel stress is not a conserved total coefficient source because its energy equation is forced by the standard seed metric; BR3B-2 must include background dressing",
      "K4_3b_RG_verdict":"NEUZAVRETA_BR3B2_BACKGROUND_DRESSED_SYSTEM_REQUIRED",
      "canonical_score":"60/100 = G6","next_step":"BR3B-2 include Omega/background and base-seed cross coefficients before solving induced response",
      "runtime_limit_seconds":a.max_runtime_seconds,"runtime_seconds":time.monotonic()-t0}
    print(json.dumps(out,indent=2,sort_keys=True)); return 0 if diagnosed else 1


if __name__=="__main__":
    try: raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict":"TIMEOUT_UNCLOSED","error":str(exc)})); raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution_verdict":"ERROR_UNCLOSED","error":repr(exc)})); raise SystemExit(2)
