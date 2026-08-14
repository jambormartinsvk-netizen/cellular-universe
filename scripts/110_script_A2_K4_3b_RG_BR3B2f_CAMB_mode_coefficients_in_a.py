#!/usr/bin/env python
"""BR3B-2f-1: extract standard seed coefficients at the fuel power.

Use precompiled CAMB 1.6.6 outputs as functions of the actual scale factor a.
For each AD/CDI/BI/NID/NIV mode, fit a declared Laurent/power basis in two
early windows and extract h_x, eta_x, U_gamma and U_nu at the leading h_x
power n.  Ratios are normalized to h_x=1.

This is an input gate.  Unstable coefficients are REVIEW_UNCLOSED and must not
be passed to the fractional fuel response.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import time

import numpy as np


ROOT=Path(__file__).resolve().parents[1]; LOCAL=ROOT/".deps"/"python"
if LOCAL.exists(): sys.path.insert(0,str(LOCAL))
import camb  # noqa: E402


MODES={
 "AD":("initial_adiabatic",2),"CDI":("initial_iso_CDM",1),
 "BI":("initial_iso_baryon",1),"NID":("initial_iso_neutrino",3),
 "NIV":("initial_iso_neutrino_vel",2)}


def fit_coeff(w,y,powers):
    A=np.column_stack([w**p for p in powers]); c=np.linalg.lstsq(A,y,rcond=None)[0]
    res=np.linalg.norm(A@c-y)/max(np.linalg.norm(y),1e-300)
    return {p:float(v) for p,v in zip(powers,c)},float(res),float(np.linalg.cond(A))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--max-runtime-seconds",type=float,default=40.)
    ap.add_argument("--k-mpc",type=float,default=.05); a=ap.parse_args()
    if not 0<a.max_runtime_seconds<=50: ap.error("runtime must be in (0,50]")
    if not 1e-4<=a.k_mpc<=.2: ap.error("k outside range")
    t0=time.monotonic()
    def deadline():
        if time.monotonic()-t0>a.max_runtime_seconds: raise TimeoutError("BR3B-2f-1 deadline")

    h=.6637; om0=.3517; obh2=.02237; och2=om0*h*h-obh2; neff=3.046+.0535
    rnu=.2271*neff/(1+.2271*neff); rg=1-rnu
    pars=camb.CAMBparams(); pars.set_cosmology(H0=100*h,ombh2=obh2,omch2=och2,omk=0,mnu=0,nnu=neff,tau=.054)
    pars.set_dark_energy(w=-1+.02297,wa=0,dark_energy_model="ppf"); pars.WantTransfer=True
    data=camb.get_background(pars); deadline()
    windows={"deep":np.geomspace(1.2e-3,4.0e-3,24),"shallow":np.geomspace(1.8e-3,6.0e-3,24)}
    # Explicit bases.  They include all lower terms that can contaminate n.
    bases={
      "AD":{"dc":[0,2,3,4],"eta":[0,2,3,4],"U":[2,3,4]},
      "CDI":{"dc":[0,1,2,3],"eta":[1,2,3,4],"U":[1,2,3,4]},
      "BI":{"dc":[1,2,3,4],"eta":[1,2,3,4],"U":[1,2,3,4]},
      "NID":{"dc":[3,4,5],"eta":[2,3,4,5],"U":[0,1,2,3,4,5]},
      "NIV":{"dc":[2,3,4],"eta":[1,2,3,4],"U":[-1,0,1,2,3,4]},}
    rows={}; checks={}
    for short,(mode,n) in MODES.items():
        data.Params.scalar_initial_condition=mode; wr={}
        for window,ykt in windows.items():
            tau=ykt/a.k_mpc
            v=np.asarray(data.get_time_evolution(a.k_mpc,tau,
              vars=["a","H","delta_cdm","v_photon","v_neutrino","etak"],lAccuracyBoost=4),float)
            aa,H,dc,qg,qn,etak=v.T; pivot=float(np.exp(np.mean(np.log(aa)))); w=aa/pivot
            Ug=3*H*qg/(4*a.k_mpc); Un=3*H*qn/(4*a.k_mpc); eta=etak/a.k_mpc
            cdc,rdc,kdc=fit_coeff(w,dc,bases[short]["dc"])
            ce,re,ke=fit_coeff(w,eta,bases[short]["eta"])
            cg,rgf,kg=fit_coeff(w,Ug,bases[short]["U"]); cn,rnf,kn=fit_coeff(w,Un,bases[short]["U"])
            hx=-2*n*cdc[n]; etax=n*ce[n]
            if abs(hx)<1e-30: raise FloatingPointError(f"{short} unresolved hx coefficient")
            out={"pivot_a":pivot,"h_x_coefficient":hx,"eta_x_over_hx":etax/hx,
              "U_gamma_over_hx":cg[n]/hx,"U_fs_over_hx":cn[n]/hx,
              "fit_relative_residuals":{"dc":rdc,"eta":re,"Ug":rgf,"Un":rnf},
              "basis_condition_numbers":{"dc":kdc,"eta":ke,"Ug":kg,"Un":kn}}
            out["0i_residual_normalized"]=out["eta_x_over_hx"]-2*(rg*out["U_gamma_over_hx"]+rnu*out["U_fs_over_hx"])
            wr[window]=out; deadline()
        d,s=wr["deep"],wr["shallow"]
        for key in ["eta_x_over_hx","U_gamma_over_hx","U_fs_over_hx"]:
            scale=max(abs(d[key]),abs(s[key]),1e-12); checks[f"{short}_{key}_two_window_10pct"]=abs(d[key]-s[key])/scale<.10
        checks[f"{short}_deep_0i_below_2pct"]=abs(d["0i_residual_normalized"])<.02
        checks[f"{short}_shallow_0i_below_2pct"]=abs(s["0i_residual_normalized"])<.02
        checks[f"{short}_all_fits_below_1e-7"]=max(d["fit_relative_residuals"].values())<1e-7 and max(s["fit_relative_residuals"].values())<1e-7
        rows[short]={"n":n,"windows":wr}
    expected={
      "AD":{"eta_x_over_hx":-(5+4*rnu)/(6*(15+4*rnu)),"U_gamma_over_hx":-1/36,
            "U_fs_over_hx":-(4*rnu+23)/(36*(4*rnu+15))},
      "CDI":{"eta_x_over_hx":-1/6,"U_gamma_over_hx":-1/12,"U_fs_over_hx":-1/12},
      "BI":{"eta_x_over_hx":-1/6,"U_gamma_over_hx":-1/12,"U_fs_over_hx":-1/12}}
    for mode,vals in expected.items():
        for key,want in vals.items():
            got=rows[mode]["windows"]["deep"][key]
            checks[f"{mode}_{key}_analytic_5pct"]=abs(got-want)<max(.05*abs(want),5e-4)
            rows[mode].setdefault("analytic_expected",{})[key]=want
    passed=all(checks.values())
    out={"test":"A2-K4.3b-RG-BR3B-2f-1 CAMB seed coefficients in a","CAMB_version":camb.__version__,
      "radiation_fractions":{"R_gamma":rg,"R_fs":rnu},"mode_results":rows,"checks":checks,
      "execution_verdict":"PASS_MODE_COEFFICIENT_EXTRACTION" if passed else "REVIEW_MODE_COEFFICIENT_EXTRACTION",
      "K4_3b_RG_verdict":"NEUZAVRETA_BR3B2F2_FUEL_RESPONSE_REQUIRED" if passed else "NEUZAVRETA_INPUT_COEFFICIENTS",
      "canonical_score":"60/100 = G6","next_step":"BR3B-2f-2 use only if this gate passes; solve ordered fuel plus decoupled F3 coefficient",
      "runtime_limit_seconds":a.max_runtime_seconds,"runtime_seconds":time.monotonic()-t0}
    print(json.dumps(out,indent=2,sort_keys=True)); return 0 if passed else 1


if __name__=="__main__":
    try: raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict":"TIMEOUT_UNCLOSED","error":str(exc)})); raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution_verdict":"ERROR_UNCLOSED","error":repr(exc)})); raise SystemExit(2)
