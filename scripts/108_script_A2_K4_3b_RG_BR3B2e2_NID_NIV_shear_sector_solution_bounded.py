#!/usr/bin/env python
"""Bounded clone of script 107 after its exact linsolve exceeded 15 s.

All physical source identities and Bianchi tests remain exact SymPy rational
equalities.  Only the overdetermined 9x7 response is solved with float64 SVD;
rank, condition number and scaled absolute residual are reported.  Script 107
is preserved as TIMEOUT_UNCLOSED.
"""

from __future__ import annotations

import argparse
import json
import time

import numpy as np
import sympy as sp


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-runtime-seconds", type=float, default=8.0)
    args = parser.parse_args()
    if not 0.0 < args.max_runtime_seconds <= 10.0:
        parser.error("runtime must be in (0, 10]")
    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("BR3B-2e-2 bounded deadline exceeded")

    delta = sp.Rational(2297, 100000)
    p = sp.simplify(4 - 3 * delta)
    neff = sp.Rational(3046, 1000) + sp.Rational(535, 10000)
    rg = sp.simplify(1 / (1 + sp.Rational(2271, 10000) * neff))
    rf = sp.simplify(1 - rg)
    base = {
        "NID": {"m": sp.Integer(2), "dg": rf/(6*rg), "dn": -sp.Rational(1,6),
                "ugl": -rf/(4*rg), "unl": sp.Rational(1,4),
                "sig": 1/(2*(4*rf+15)), "eta": -rf/(6*(4*rf+15)),
                "fuel": p+3},
        "NIV": {"m": sp.Integer(1), "dg": rf/rg, "dn": -sp.Integer(1),
                "ugl": -3*rf/(4*rg), "unl": sp.Rational(3,4),
                "sig": 1/(4*rf+5), "eta": -rf/(4*rf+5),
                "fuel": p+2},
    }

    checks: dict[str, bool] = {}
    rows: dict[str, object] = {}
    for mode, z in base.items():
        m, r = z["m"], sp.simplify(p+z["m"])
        dg, dn, ugl, unl = map(sp.simplify, (z["dg"],z["dn"],z["ugl"],z["unl"]))
        sig, eta = sp.simplify(z["sig"]), sp.simplify(z["eta"])
        etax = sp.simplify(m*eta)
        ugm = sp.simplify(dg/(4*(m+1)))
        unm = sp.simplify((dn/4-sig)/(m+1))
        early = sp.simplify(p+m-2)
        factor = sp.simplify(p/(2*(early+1)))
        uge, une = sp.simplify(factor*ugl), sp.simplify(factor*unl)

        jgc=sp.simplify(sp.Rational(4,3)*(ugl-uge)); jnc=sp.simplify(sp.Rational(4,3)*(unl-une))
        jge=sp.simplify(p*ugm/2); jne=sp.simplify(p*unm/2)
        jns=sp.simplify(sp.Rational(8,15)*(uge-ugl))
        c00=sp.Integer(0); c0i=-etax; ctr=sp.Integer(0)
        ctl=sp.simplify(-3*p*etax+12*rf*sig)

        checks[f"{mode}_base_density_compensation"] = bool(sp.simplify(rg*dg+rf*dn)==0)
        checks[f"{mode}_base_continuities"] = bool(sp.simplify(m*dg+sp.Rational(4,3)*ugl)==0 and sp.simplify(m*dn+sp.Rational(4,3)*unl)==0)
        checks[f"{mode}_base_Eulers"] = bool(sp.simplify((m+1)*ugm-dg/4)==0 and sp.simplify((m+1)*unm-dn/4+sig)==0)
        checks[f"{mode}_base_shear"] = bool(sp.simplify(2*m*sig-sp.Rational(8,5)*m*eta-sp.Rational(8,15)*unl)==0)
        checks[f"{mode}_base_0i"] = bool(sp.simplify(etax-2*(rg*ugm+rf*unm))==0)
        checks[f"{mode}_base_traceless"] = bool(sp.simplify(6*(m+1)*etax+12*rf*sig)==0)

        weighted_c=sp.simplify(rg*jgc+rf*jnc); weighted_e=sp.simplify(rg*jge+rf*jne)
        b1=sp.simplify(2*(r-1)*c00+ctr-3*weighted_c)
        b2=sp.simplify(2*(r-1)*c00-6*(r+1)*c0i+ctl-3*weighted_c-12*weighted_e)
        checks[f"{mode}_exact_Bianchi_pair"] = bool(b1==0 and b2==0)

        A=sp.Matrix([
          [sp.Rational(2,3),0,r,0,0,0,0], [0,0,-sp.Rational(1,4),0,r+1,0,0],
          [sp.Rational(2,3),0,0,r,0,0,0], [-sp.Rational(4,15),-sp.Rational(8,5)*r,0,0,0,0,2*r],
          [0,0,0,-sp.Rational(1,4),0,r+1,1],
          [-sp.Rational(1,2),0,sp.Rational(3,2)*rg,sp.Rational(3,2)*rf,0,0,0],
          [0,r,0,0,-2*rg,-2*rf,0], [r+1,0,3*rg,3*rf,0,0,0],
          [r+1,6*r*(r+1),0,0,0,0,12*rf]])
        b=sp.Matrix([jgc,jge,jnc,jns,jne,c00,c0i,ctr,ctl])
        af=np.asarray(A,float); bf=np.asarray(b,float).reshape(-1)
        solution,residuals,rank,svals=np.linalg.lstsq(af,bf,rcond=None)
        residual=af@solution-bf
        max_abs=float(np.max(np.abs(residual)))
        scale=float(max(np.max(np.abs(af)*np.maximum(np.abs(solution)[None,:],1e-300)),np.max(np.abs(bf)),1e-300))
        scaled=max_abs/scale
        condition=float(svals[0]/svals[-1])
        checks[f"{mode}_numeric_rank_7"] = bool(rank==7)
        checks[f"{mode}_finite_condition_number"] = bool(np.isfinite(condition))
        checks[f"{mode}_scaled_absolute_residual_below_1e-12"] = bool(scaled<1e-12)
        checks[f"{mode}_finite_response"] = bool(np.all(np.isfinite(solution)))
        l3=sp.simplify(p+m+2)
        checks[f"{mode}_l3_feedback_after_fuel"] = bool(l3>z["fuel"])
        rows[mode]={
          "base_power":str(m),"fractional_power":str(r),"earlier_velocity_power":str(early),
          "fixed_source":{"Jgc":str(jgc),"Jge":str(jge),"Jnc":str(jnc),"Jns":str(jns),"Jne":str(jne),"C00":str(c00),"C0i":str(c0i),"Ctr":str(ctr),"Ctl":str(ctl)},
          "exact_Bianchi_residuals":[str(b1),str(b2)],"numeric_rank":int(rank),
          "singular_values":svals.tolist(),"condition_number":condition,
          "solution_order":["h_x","eta","delta_gamma","delta_fs","U_gamma","U_fs","sigma_fs"],
          "numeric_solution":solution.tolist(),"max_absolute_residual":max_abs,
          "residual_scale":scale,"scaled_absolute_residual":scaled,
          "fuel_power":str(z["fuel"]),"first_l3_feedback_power":str(l3)}
        deadline()

    passed=all(checks.values())
    out={"test":"A2-K4.3b-RG-BR3B-2e-2 bounded NID/NIV shear sectors",
      "supersedes_execution_only":"script 107 exact linsolve TIMEOUT_UNCLOSED remains preserved",
      "NIV_shear":"sigma=(k tau)/(4Rnu+5), audited by script 106",
      "checks":checks,"mode_results":rows,
      "execution_verdict":"PASS_NID_NIV_FIRST_SHEAR_SECTORS_BOUNDED" if passed else "REVIEW_BR3B2E2_BOUNDED",
      "physical_verdict":"unique finite rank-7 responses with exact zero Bianchi pairs and <1e-12 scaled numerical residuals" if passed else "unclosed",
      "K4_3b_RG_verdict":"NEUZAVRETA_BR3B2F_ORDERED_COMMON_FUEL_AND_L3_RECURSION_REQUIRED",
      "canonical_score":"60/100 = G6","next_step":"BR3B-2f inject completed earlier sectors into common fuel response, then append later l3 recursion",
      "runtime_limit_seconds":args.max_runtime_seconds,"runtime_seconds":time.monotonic()-started}
    print(json.dumps(out,indent=2,sort_keys=True)); return 0 if passed else 1


if __name__=="__main__":
    try: raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict":"TIMEOUT_UNCLOSED","error":str(exc)})); raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution_verdict":"ERROR_UNCLOSED","error":repr(exc)})); raise SystemExit(2)
