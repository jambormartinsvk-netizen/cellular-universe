#!/usr/bin/env python
"""Round-off condition gate for the two compensated velocity modes.

Runs the unchanged Omega-conditioned solver through alias 92, then computes
an a-priori IEEE-754 cancellation bound from the absolute species momentum
and momentum-derivative components at both starts.  Only 0i, the total
momentum ledger and traceless ij of NIV/internal velocity may use this bound;
all other modes/equations retain the strict 2e-10 conditioned gate.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys
import time

import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.linalg import expm

HERE = Path(__file__).resolve().parent


def load(name: str, filename: str):
    path = HERE / filename
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-runtime-seconds", type=float, default=48.0)
    args = ap.parse_args()
    if not (25.0 <= args.max_runtime_seconds <= 50.0):
        ap.error("--max-runtime-seconds must be in [25,50]")
    started = time.monotonic()

    child = subprocess.run(
        [
            sys.executable,
            str(HERE / "92_script_A2_K4_3b_RG_BR2_Omega_conditioned_DAE_json_fixed_alias.py"),
            "--max-runtime-seconds",
            "40",
        ],
        capture_output=True,
        text=True,
        timeout=min(45.0, args.max_runtime_seconds - 2.0),
        check=False,
    )
    if not child.stdout.strip():
        raise RuntimeError(f"script 92 returned no JSON: {child.stderr[-500:]}")
    base = json.loads(child.stdout)
    if time.monotonic() - started > args.max_runtime_seconds:
        raise TimeoutError("velocity condition gate deadline exceeded")

    B13 = load("k4_vcond_bg13", "13_script_A1_K1_cdm_background_audit_exact_zstar.py")
    B11 = B13.BASE
    S84 = load("k4_vcond_seed84", "84_script_A2_K4_3b_RG_CLASS_analytic_collective_seed_CAMB_crosscheck.py")
    p = B11.ModelParameters()
    xdeep = float(base["inputs"]["x_deep"])
    xshallow = float(base["inputs"]["x_shallow"])
    lmax = int(base["inputs"]["lmax"])
    q = float(base["inputs"]["q"])
    xd, sd, xbnow = B13.integrate_background(
        p, B11.IntegrationSettings(x_min=xdeep, step=5.0e-4)
    )
    x = np.asarray(xd[::-1]); st = np.asarray(sd[::-1]); xf, xm, xr = st.T
    xb = xbnow*np.exp(-3*x); xc=xm-xb; e=np.sqrt(xf+xm+xr); av=np.exp(x)
    hc=1+(-3*p.delta*xf-3*xm-4*xr)/(2*e**2)
    tau=np.zeros_like(x); tau[0]=av[0]/math.sqrt(B11.radiation_density_today(p))
    f=np.exp(-x)/e; tau[1:]=tau[0]+np.cumsum(.5*np.diff(x)*(f[:-1]+f[1:]))
    early=(x>=xdeep+.5)&(x<=xdeep+2)
    fb=float(np.mean(xb[early]/xm[early])); fc=float(np.mean(xc[early]/xm[early]))
    den=1+0.2271*(p.neff_standard+p.delta_neff)
    rg=1/den; rn=0.2271*p.neff_standard/den; rs=0.2271*p.delta_neff/den; rfs=rn+rs
    om=float(np.mean(av[early]*xm[early]/np.sqrt(xr[early])))
    it={name:PchipInterpolator(x,val) for name,val in {
        "xf":xf,"xc":xc,"xb":xb,"xr":xr,"e":e,"hc":hc,"tau":tau}.items()}

    A=np.zeros((lmax+1,lmax+1)); A[0,1]=-1; A[1,0]=1/3; A[1,2]=-2/3
    for ell in range(2,lmax+1):
        A[ell,ell-1]=ell/(2*ell+1)
        if ell<lmax: A[ell,ell+1]=-(ell+1)/(2*ell+1)

    eps=np.finfo(float).eps

    def condition(mode: str, xx: float) -> dict[str, float]:
        xf=float(it["xf"](xx)); xc=float(it["xc"](xx)); xb=float(it["xb"](xx))
        xr=float(it["xr"](xx)); ee=float(it["e"](xx)); hh=float(it["hc"](xx)); aa=math.exp(xx)
        e2=ee*ee; of=xf/e2; oc=xc/e2; ob=xb/e2; og=rg*xr/e2; on=rn*xr/e2; os=rs*xr/e2
        er=2*(hh-1); g=p.lam/ee; tt=float(it["tau"](xx)); kh=q/(aa*ee)
        dg=db=dc=ug=0.0; fn=np.zeros(lmax+1); fs=np.zeros(lmax+1)
        if mode == "initial_iso_neutrino_vel":
            v=S84.class_seed(mode,q,tt,rfs,rg,fb,fc,om)
            dg,db,dc=v[0],v[1],v[2]; ug=3*aa*ee*v[4]/(4*q)
            fn[0]=fs[0]=v[3]; fn[1]=fs[1]=v[5]
        else:
            seed=np.zeros(lmax+1); seed[1]=1
            fn=expm(A*q*tt)@seed; fs=-(rn/rs)*fn
        un=3*aa*ee*fn[1]/(4*q); us=3*aa*ee*fs[1]/(4*q)

        # Leading metric sources. Dark velocities vanish at the start.
        dh=oc*dc+ob*db+og*dg+on*fn[0]+os*fs[0]
        mh=ob*ug+(4/3)*(og*ug+on*un+os*us)
        kt=0.0
        hx=2*(kt+1.5*dh); etax=1.5*mh
        R=3*ob/(4*og); ugx=(hh-R/(1+R))*ug+dg/(4*(1+R))
        f1nx=kh*(fn[0]-2*fn[2])/3; f1sx=kh*(fs[0]-2*fs[2])/3
        unx=hh*un+3*aa*ee*f1nx/(4*q); usx=hh*us+3*aa*ee*f1sx/(4*q)
        ox_ob=-(3+er)*ob; ox_og=-(4+er)*og; ox_on=-(4+er)*on; ox_os=-(4+er)*os

        m_components=np.array([ob*ug,(4/3)*og*ug,(4/3)*on*un,(4/3)*os*us])
        mx_components=np.array([
            ox_ob*ug+ob*ugx,
            (4/3)*(ox_og*ug+og*ugx),
            (4/3)*(ox_on*un+on*unx),
            (4/3)*(ox_os*us+os*usx),
        ])
        shear_components=np.array([(2/3)*on*fn[2],(2/3)*os*fs[2]])
        sm=float(np.sum(np.abs(m_components)))
        smx=float(np.sum(np.abs(mx_components)))
        sshear=float(np.sum(np.abs(shear_components)))
        # 64 is a declared conservative operation-count allowance covering
        # RK4 combinations, interpolation, and the final source summation.
        allowance=64.0*eps
        return {
            "sum_abs_species_momentum": sm,
            "sum_abs_species_momentum_x": smx,
            "sum_abs_species_shear": sshear,
            "bound_0i": allowance*1.5*sm,
            "bound_momentum_ledger": allowance*(smx+abs(hh+2)*sm+sshear),
            "bound_traceless_ij": allowance*9.0*(smx+abs(hh+2)*sm+sshear),
            "initial_hx": hx,
            "initial_eta_x": etax,
        }

    bounds={}
    for mode in ("initial_iso_neutrino_vel","internal_nu_steam_velocity"):
        by_depth={"deep":condition(mode,xdeep),"shallow":condition(mode,xshallow)}
        bounds[mode]=by_depth

    strict=2.0e-10
    checks={}
    for mode,row in base["mode_results"].items():
        for depth in ("deep","shallow"):
            led=row[f"{depth}_ledgers"]
            if mode not in bounds:
                checks[f"{mode}_{depth}_strict"] = all(
                    float(v["conditioned_error"]) < strict for v in led.values()
                )
                continue
            b=bounds[mode][depth]
            checks[f"{mode}_{depth}_strict_nonvelocity_ledgers"] = all(
                float(led[name]["conditioned_error"]) < strict
                for name in ("00","trace_ij","energy_product_ledger")
            )
            checks[f"{mode}_{depth}_0i_within_roundoff_bound"] = (
                float(led["0i"]["conditioned_error"]) <= max(strict,b["bound_0i"])
            )
            checks[f"{mode}_{depth}_momentum_within_roundoff_bound"] = (
                float(led["momentum_product_ledger"]["conditioned_error"])
                <= max(strict,b["bound_momentum_ledger"])
            )
            checks[f"{mode}_{depth}_traceless_within_roundoff_bound"] = (
                float(led["traceless_ij"]["conditioned_error"])
                <= max(strict,b["bound_traceless_ij"])
            )
        checks[f"{mode}_two_start_convergence"] = float(row["two_start_final_relative_difference"]) < 3e-3

    passed=all(checks.values())
    output={
        "test":"A2-K4.3b-RG-BR2 compensated velocity round-off condition gate",
        "base_solver":"92 -> unchanged 91 Omega-conditioned DAE",
        "base_execution_verdict":base["execution_verdict"],
        "strict_conditioned_gate":strict,
        "roundoff_allowance":"64 * machine epsilon * sum(abs(species components))",
        "velocity_condition_bounds":bounds,
        "checks":checks,
        "execution_verdict":"PASS_BR2_WITH_EXPLICIT_VELOCITY_CONDITION_BOUND" if passed else "REVIEW_BR2_VELOCITY_CONDITION_BOUND",
        "K4_3b_RG_verdict":"NEUZAVRETA_EXPLICIT_FRACTIONAL_COEFFICIENT_AND_FULL_PHOTON_BACKEND_GATES_MISSING",
        "canonical_score":"60/100 = G6",
        "next_step":"BR3 explicit mode-resolved Puiseux coefficients and residual scaling",
        "child_return_code":child.returncode,
        "runtime_limit_seconds":args.max_runtime_seconds,
        "runtime_seconds":time.monotonic()-started,
    }
    print(json.dumps(output,indent=2,sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try: raise SystemExit(main())
    except subprocess.TimeoutExpired as exc:
        print(json.dumps({"execution_verdict":"TIMEOUT_UNCLOSED","error":str(exc)})); raise SystemExit(124)
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict":"TIMEOUT_UNCLOSED","error":str(exc)})); raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution_verdict":"ERROR_UNCLOSED","error":repr(exc)})); raise SystemExit(2)
