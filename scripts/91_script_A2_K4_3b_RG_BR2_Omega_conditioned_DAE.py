#!/usr/bin/env python
"""Omega-conditioned successor to BR2 scripts 89 and 90.

Script 89 exposed an ill-conditioned second metric derivative. Script 90
removed that derivative but still formed compensated NID/internal sources
from raw X_A~a^-4 densities. This script performs the identical DAE system in
Omega_A=X_A/E^2 variables. All Einstein and conservation ledgers are thereby
dimensionless and compensated sums involve O(1) numbers.

The scope remains the early superhorizon/tight-coupling subgate. A PASS is not
the full photon/recombination backend and cannot promote K4 above G6.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path
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


B13 = load("k4_br2o_bg13", "13_script_A1_K1_cdm_background_audit_exact_zstar.py")
B11 = B13.BASE
S84 = load("k4_br2o_seed84", "84_script_A2_K4_3b_RG_CLASS_analytic_collective_seed_CAMB_crosscheck.py")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-runtime-seconds", type=float, default=45.0)
    ap.add_argument("--x-deep", type=float, default=-25.0)
    ap.add_argument("--x-shallow", type=float, default=-23.0)
    ap.add_argument("--x-final", type=float, default=-14.0)
    ap.add_argument("--step", type=float, default=2e-3)
    ap.add_argument("--background-step", type=float, default=5e-4)
    ap.add_argument("--k-mpc", type=float, default=0.05)
    ap.add_argument("--lmax", type=int, default=8)
    a = ap.parse_args()
    if not (0 < a.max_runtime_seconds <= 50): ap.error("runtime must be in (0,50]")
    if not (-27 <= a.x_deep <= -24): ap.error("x-deep outside [-27,-24]")
    if not (1 <= a.x_shallow-a.x_deep <= 3): ap.error("start separation outside [1,3]")
    if not (-16 <= a.x_final <= -13): ap.error("x-final outside [-16,-13]")
    if not (5e-4 <= a.step <= 5e-3): ap.error("step outside [5e-4,5e-3]")
    if not (2.5e-4 <= a.background_step <= 1e-3): ap.error("background-step outside range")
    if not (6 <= a.lmax <= 12): ap.error("lmax outside [6,12]")
    t0 = time.monotonic()

    def deadline():
        if time.monotonic()-t0 > a.max_runtime_seconds:
            raise TimeoutError("Omega-conditioned BR2 deadline exceeded")

    p = B11.ModelParameters()
    xd, sd, xbnow = B13.integrate_background(
        p, B11.IntegrationSettings(x_min=a.x_deep, step=a.background_step)
    )
    x = np.asarray(xd[::-1]); st = np.asarray(sd[::-1]); xf,xm,xr = st.T
    xb = xbnow*np.exp(-3*x); xc=xm-xb; e=np.sqrt(xf+xm+xr); aa=np.exp(x)
    hc=1+(-3*p.delta*xf-3*xm-4*xr)/(2*e**2)
    tau=np.zeros_like(x); tau[0]=aa[0]/math.sqrt(B11.radiation_density_today(p))
    f=np.exp(-x)/e; tau[1:]=tau[0]+np.cumsum(.5*np.diff(x)*(f[:-1]+f[1:]))
    early=(x>=a.x_deep+.5)&(x<=a.x_deep+2)
    fb=float(np.mean(xb[early]/xm[early])); fc=float(np.mean(xc[early]/xm[early]))
    den=1+0.2271*(p.neff_standard+p.delta_neff)
    rg=1/den; rn=0.2271*p.neff_standard/den; rs=0.2271*p.delta_neff/den; rfs=rn+rs
    om=float(np.mean(aa[early]*xm[early]/np.sqrt(xr[early])))
    q=a.k_mpc/(100*p.h/299792.458)
    it={name:PchipInterpolator(x,val) for name,val in {
        "xf":xf,"xc":xc,"xb":xb,"xr":xr,"e":e,"hc":hc,"tau":tau}.items()}
    deadline()

    DC,UC,DF,UF,DB,DG,UG=range(7); N0=7; S0=N0+a.lmax+1; ETA=S0+a.lmax+1; SIZE=ETA+1

    def back(xx):
        xf=float(it["xf"](xx)); xc=float(it["xc"](xx)); xb=float(it["xb"](xx))
        xr=float(it["xr"](xx)); e=float(it["e"](xx)); hc=float(it["hc"](xx)); av=math.exp(xx)
        e2=e*e
        return {"xf":xf,"xc":xc,"xb":xb,"xg":rg*xr,"xn":rn*xr,"xs":rs*xr,
                "of":xf/e2,"oc":xc/e2,"ob":xb/e2,"og":rg*xr/e2,"on":rn*xr/e2,
                "os":rs*xr/e2,"e":e,"hc":hc,"a":av,"g":p.lam/e}

    def project(mode,z):
        if mode.startswith("internal_"):
            z=z.copy(); z[:N0]=0; z[S0:ETA]=-(rn/rs)*z[N0:S0]; z[ETA]=0
        return z

    def src(xx,z):
        b=back(xx); fn=z[N0:S0]; fs=z[S0:ETA]
        un=3*b["a"]*b["e"]*fn[1]/(4*q); us=3*b["a"]*b["e"]*fs[1]/(4*q)
        pf=b["of"]*(z[DF]+(2-p.delta)*(3*p.delta+b["g"])*z[UF])
        dh=b["oc"]*z[DC]+b["of"]*z[DF]+b["ob"]*z[DB]+b["og"]*z[DG]+b["on"]*fn[0]+b["os"]*fs[0]
        ph=pf+(b["og"]*z[DG]+b["on"]*fn[0]+b["os"]*fs[0])/3
        mh=b["oc"]*z[UC]+p.delta*b["of"]*z[UF]+b["ob"]*z[UG]+(4/3)*(b["og"]*z[UG]+b["on"]*un+b["os"]*us)
        sh=(2/3)*(b["on"]*fn[2]+b["os"]*fs[2])
        kt=q*q*z[ETA]/(b["a"]*b["e"])**2
        hx=2*(kt+1.5*dh)
        return b,{"D":dh,"P":ph,"M":mh,"S":sh,"hx":hx,"un":un,"us":us}

    def rhs(xx,zin,mode):
        z=project(mode,zin); b,s=src(xx,z); out=np.zeros(SIZE)
        r=b["of"]/b["oc"]; beta=p.delta*b["of"]/(b["oc"]+p.delta*b["of"])
        ud=(1-beta)*z[UC]+beta*z[UF]; s2=(q/(b["a"]*b["e"]))**2
        out[DC]=-s2*z[UC]-s["hx"]/2+b["g"]*r*(z[DF]-z[DC])
        out[UC]=(b["hc"]-1)*z[UC]+b["g"]*r*beta*(z[UF]-z[UC])
        out[DF]=-3*(2-p.delta)*z[DF]-p.delta*(s2*z[UF]+s["hx"]/2)-9*p.delta*(2-p.delta)*z[UF]-3*b["g"]*(2-p.delta)*z[UF]
        out[UF]=(b["hc"]+2)*z[UF]+z[DF]/p.delta+b["g"]/p.delta*(2*z[UF]-ud)
        R=3*b["ob"]/(4*b["og"])
        out[DB]=-s2*z[UG]-s["hx"]/2; out[DG]=-(4/3)*s2*z[UG]-(2/3)*s["hx"]
        out[UG]=(b["hc"]-R/(1+R))*z[UG]+z[DG]/(4*(1+R))
        etax=1.5*s["M"]; kh=q/(b["a"]*b["e"])
        for start in (N0,S0):
            h=z[start:start+a.lmax+1]
            out[start]=-kh*h[1]-(2/3)*s["hx"]
            out[start+1]=kh*(h[0]-2*h[2])/3
            out[start+2]=kh*(2*h[1]-3*h[3])/5+(4/15)*s["hx"]+(8/5)*etax
            for ell in range(3,a.lmax+1):
                nxt=h[ell+1] if ell<a.lmax else 0
                out[start+ell]=kh*(ell*h[ell-1]-(ell+1)*nxt)/(2*ell+1)
        out[ETA]=etax
        if mode.startswith("internal_"):
            out[:N0]=0; out[S0:ETA]=-(rn/rs)*out[N0:S0]; out[ETA]=0
        return out

    A=np.zeros((a.lmax+1,a.lmax+1)); A[0,1]=-1; A[1,0]=1/3; A[1,2]=-2/3
    for ell in range(2,a.lmax+1):
        A[ell,ell-1]=ell/(2*ell+1)
        if ell<a.lmax: A[ell,ell+1]=-(ell+1)/(2*ell+1)
    modes=list(S84.MODES)+["internal_nu_steam_density","internal_nu_steam_velocity"]

    def initial(mode,xx):
        z=np.zeros(SIZE); b=back(xx); tt=float(it["tau"](xx))
        if mode in S84.MODES:
            v=S84.class_seed(mode,q,tt,rfs,rg,fb,fc,om)
            z[DG],z[DB],z[DC]=v[0],v[1],v[2]; z[N0]=v[3]; z[S0]=v[3]
            z[UG]=3*b["a"]*b["e"]*v[4]/(4*q); z[N0+1]=v[5]; z[S0+1]=v[5]; z[ETA]=v[6]
        else:
            v=np.zeros(a.lmax+1); v[0 if mode.endswith("density") else 1]=1
            z[N0:S0]=expm(A*q*tt)@v; z=project(mode,z)
        return z

    def audit(xx,z,mode):
        z=project(mode,z); dz=rhs(xx,z,mode); b,s=src(xx,z); fn=z[N0:S0]; fs=z[S0:ETA]
        dfn=dz[N0:S0]; dfs=dz[S0:ETA]; er=2*(b["hc"]-1)
        # Omega derivatives follow from exact background product rules.
        ox={
          "of":-(3*p.delta+b["g"]+er)*b["of"],
          "oc":-3*b["oc"]+b["g"]*b["of"]-er*b["oc"],
          "ob":-(3+er)*b["ob"],"og":-(4+er)*b["og"],
          "on":-(4+er)*b["on"],"os":-(4+er)*b["os"]}
        dhx=ox["oc"]*z[DC]+b["oc"]*dz[DC]+ox["of"]*z[DF]+b["of"]*dz[DF]+ox["ob"]*z[DB]+b["ob"]*dz[DB]+ox["og"]*z[DG]+b["og"]*dz[DG]+ox["on"]*fn[0]+b["on"]*dfn[0]+ox["os"]*fs[0]+b["os"]*dfs[0]
        unx=b["hc"]*s["un"]+3*b["a"]*b["e"]*dfn[1]/(4*q)
        usx=b["hc"]*s["us"]+3*b["a"]*b["e"]*dfs[1]/(4*q)
        mhx=ox["oc"]*z[UC]+b["oc"]*dz[UC]+p.delta*(ox["of"]*z[UF]+b["of"]*dz[UF])+ox["ob"]*z[UG]+b["ob"]*dz[UG]+(4/3)*(ox["og"]*z[UG]+b["og"]*dz[UG]+ox["on"]*s["un"]+b["on"]*unx+ox["os"]*s["us"]+b["os"]*usx)
        wh=b["oc"]+p.delta*b["of"]+b["ob"]+(4/3)*(b["og"]+b["on"]+b["os"])
        dexp=-3*(s["D"]+s["P"])-(q/(b["a"]*b["e"]))**2*s["M"]-.5*s["hx"]*wh-er*s["D"]
        mexp=-(b["hc"]+2)*s["M"]+s["P"]-s["S"]
        kt=q*q*z[ETA]/(b["a"]*b["e"])**2
        hxx=2*(q*q*(dz[ETA]-2*b["hc"]*z[ETA])/(b["a"]*b["e"])**2+1.5*dhx)
        etaxx=1.5*mhx
        terms={
          "00":[kt,-s["hx"]/2,1.5*s["D"]],"0i":[dz[ETA],-1.5*s["M"]],
          "trace_ij":[hxx+(b["hc"]+2)*s["hx"],-2*kt,9*s["P"]],
          "traceless_ij":[hxx+6*etaxx+(b["hc"]+2)*(s["hx"]+6*dz[ETA]),-2*kt,9*s["S"]],
          "energy_product_ledger":[dhx,-dexp],"momentum_product_ledger":[mhx,-mexp]}
        return {k:(abs(float(sum(v))),float(sum(abs(t) for t in v))) for k,v in terms.items()}

    keys=("00","0i","trace_ij","traceless_ij","energy_product_ledger","momentum_product_ledger")
    def integrate(mode,start):
        n=math.ceil((a.x_final-start)/a.step); grid=np.linspace(start,a.x_final,n+1); z=initial(mode,start)
        mx={k:{"abs":0.,"norm":0.} for k in keys}
        for i in range(n):
            xx=float(grid[i]); h=float(grid[i+1]-grid[i]); k1=rhs(xx,z,mode)
            k2=rhs(xx+h/2,project(mode,z+h*k1/2),mode); k3=rhs(xx+h/2,project(mode,z+h*k2/2),mode)
            k4=rhs(xx+h,project(mode,z+h*k3),mode); z=project(mode,z+h*(k1+2*k2+2*k3+k4)/6)
            if i%25==0 or i==n-1:
                for k,(ab,no) in audit(float(grid[i+1]),z,mode).items():
                    mx[k]["abs"]=max(mx[k]["abs"],ab); mx[k]["norm"]=max(mx[k]["norm"],no)
            if i%500==0: deadline()
            if not np.all(np.isfinite(z)): raise FloatingPointError(mode)
        for v in mx.values():
            v["conditioned_error"]=v["abs"]/max(v["norm"],1.0)
            v["raw_relative"]=v["abs"]/max(v["norm"],1e-280)
        return z,mx

    checks={}; rows={}
    for mode in modes:
        zd,ad=integrate(mode,a.x_deep); zs,ass=integrate(mode,a.x_shallow)
        conv=float(np.linalg.norm(zd-zs)/max(np.linalg.norm(zd),np.linalg.norm(zs),1e-30))
        checks[f"{mode}_deep_six_conditioned_ledgers"]=all(v["conditioned_error"]<2e-10 for v in ad.values())
        checks[f"{mode}_shallow_six_conditioned_ledgers"]=all(v["conditioned_error"]<2e-10 for v in ass.values())
        checks[f"{mode}_two_start_convergence"]=conv<3e-3; checks[f"{mode}_finite"]=bool(np.all(np.isfinite(zd)) and np.all(np.isfinite(zs)))
        if mode.startswith("internal_"): checks[f"{mode}_exact_metric_dark_subspace"]=np.linalg.norm(zd[[DC,UC,DF,UF,ETA]])<1e-20
        rows[mode]={"two_start_final_relative_difference":conv,"deep_ledgers":ad,"shallow_ledgers":ass,
                    "deep_final_dark_metric_dc_Uc_df_Uf_eta":zd[[DC,UC,DF,UF,ETA]].tolist()}
        deadline()
    passed=all(checks.values())
    out={"test":"A2-K4.3b-RG-BR2 Omega-conditioned DAE","supersedes_for_numerics":[
        "89_script_A2_K4_3b_RG_BR2_backreacted_superhorizon_evolution.py",
        "90_script_A2_K4_3b_RG_BR2_conditioned_DAE_constraint_audit.py"],
      "older_run_status":"both preserved as REVIEW diagnostics: raw second derivative; raw-X cancellation",
      "scope":"early superhorizon, leading photon-baryon tight coupling, separate nu/steam hierarchy",
      "inputs":{"lambda":p.lam,"delta":p.delta,"q":q,"x_deep":a.x_deep,"x_shallow":a.x_shallow,"x_final":a.x_final,"step":a.step,"lmax":a.lmax},
      "mode_results":rows,"checks":checks,"execution_verdict":"PASS_BR2_OMEGA_CONDITIONED" if passed else "REVIEW_BR2_OMEGA_CONDITIONED",
      "K4_3b_RG_verdict":"NEUZAVRETA_EXPLICIT_FRACTIONAL_COEFFICIENT_AND_FULL_PHOTON_BACKEND_GATES_MISSING",
      "canonical_score":"60/100 = G6","next_step":"BR3 explicit mode-resolved Puiseux coefficients and residual scaling",
      "runtime_limit_seconds":a.max_runtime_seconds,"runtime_seconds":time.monotonic()-t0}
    print(json.dumps(out,indent=2,sort_keys=True)); return 0 if passed else 1


if __name__ == "__main__":
    try: raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict":"TIMEOUT_UNCLOSED","error":str(exc)})); raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution_verdict":"ERROR_UNCLOSED","error":repr(exc)})); raise SystemExit(2)
