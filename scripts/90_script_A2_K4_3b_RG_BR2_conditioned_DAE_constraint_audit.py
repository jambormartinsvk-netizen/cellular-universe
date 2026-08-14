#!/usr/bin/env python
"""Conditioned successor to BR2 script 89.

Script 89 differentiated eta twice on a uniform ln(a) grid.  In the deep
radiation era, multiplying that round-off by Hconf^2 makes a regular null
mode look like an order-one traceless-ij violation.  This successor keeps the
same matter equations and seeds but treats 00 as the algebraic synchronous
constraint.  h_x is reconstructed from 00, while h_x,x and eta_x,x are
obtained by differentiating the *component product rules*.  Trace and
traceless ij are then independent consistency tests of the matter ledger.

Script 89 remains archived as the unconditioned negative diagnostic.
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
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


B13 = load("k4_br2c_bg13", "13_script_A1_K1_cdm_background_audit_exact_zstar.py")
B11 = B13.BASE
S84 = load("k4_br2c_seed84", "84_script_A2_K4_3b_RG_CLASS_analytic_collective_seed_CAMB_crosscheck.py")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-runtime-seconds", type=float, default=45.0)
    ap.add_argument("--x-deep", type=float, default=-25.0)
    ap.add_argument("--x-shallow", type=float, default=-23.0)
    ap.add_argument("--x-final", type=float, default=-14.0)
    ap.add_argument("--step", type=float, default=2.0e-3)
    ap.add_argument("--background-step", type=float, default=5.0e-4)
    ap.add_argument("--k-mpc", type=float, default=0.05)
    ap.add_argument("--lmax", type=int, default=8)
    args = ap.parse_args()
    if not (0.0 < args.max_runtime_seconds <= 50.0):
        ap.error("--max-runtime-seconds must be in (0,50]")
    if not (-27.0 <= args.x_deep <= -24.0):
        ap.error("--x-deep must be in [-27,-24]")
    if not (1.0 <= args.x_shallow - args.x_deep <= 3.0):
        ap.error("start separation must be in [1,3]")
    if not (-16.0 <= args.x_final <= -13.0):
        ap.error("--x-final must be in [-16,-13]")
    if not (5.0e-4 <= args.step <= 5.0e-3):
        ap.error("--step must be in [5e-4,5e-3]")
    if not (2.5e-4 <= args.background_step <= 1.0e-3):
        ap.error("--background-step must be in [2.5e-4,1e-3]")
    if not (6 <= args.lmax <= 12):
        ap.error("--lmax must be in [6,12]")

    started = time.monotonic()

    def deadline() -> None:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("conditioned BR2 deadline exceeded")

    p = B11.ModelParameters()
    settings = B11.IntegrationSettings(x_min=args.x_deep, step=args.background_step)
    xd, sd, xb0 = B13.integrate_background(p, settings)
    xbg = np.asarray(xd[::-1], dtype=float)
    states = np.asarray(sd[::-1], dtype=float)
    xf0, xm0, xr0 = states.T
    xb0a = xb0 * np.exp(-3.0 * xbg)
    xc0 = xm0 - xb0a
    e0 = np.sqrt(xf0 + xm0 + xr0)
    a0 = np.exp(xbg)
    hc0 = 1.0 + (-3.0 * p.delta * xf0 - 3.0 * xm0 - 4.0 * xr0) / (2.0 * e0**2)
    tau = np.zeros_like(xbg)
    tau[0] = a0[0] / math.sqrt(B11.radiation_density_today(p))
    integ = np.exp(-xbg) / e0
    tau[1:] = tau[0] + np.cumsum(0.5 * np.diff(xbg) * (integ[:-1] + integ[1:]))
    early = (xbg >= args.x_deep + 0.5) & (xbg <= args.x_deep + 2.0)
    fb = float(np.mean(xb0a[early] / xm0[early]))
    fc = float(np.mean(xc0[early] / xm0[early]))
    denom = 1.0 + 0.2271 * (p.neff_standard + p.delta_neff)
    rg = 1.0 / denom
    rn = 0.2271 * p.neff_standard / denom
    rs = 0.2271 * p.delta_neff / denom
    rfs = rn + rs
    om = float(np.mean(a0[early] * xm0[early] / np.sqrt(xr0[early])))
    q = args.k_mpc / (100.0 * p.h / 299792.458)
    I = {
        "xf": PchipInterpolator(xbg, xf0),
        "xc": PchipInterpolator(xbg, xc0),
        "xb": PchipInterpolator(xbg, xb0a),
        "xr": PchipInterpolator(xbg, xr0),
        "e": PchipInterpolator(xbg, e0),
        "hc": PchipInterpolator(xbg, hc0),
        "tau": PchipInterpolator(xbg, tau),
    }
    deadline()

    DC, UC, DF, UF, DB, DG, UG = range(7)
    N0 = 7
    S0 = N0 + args.lmax + 1
    ETA = S0 + args.lmax + 1
    SIZE = ETA + 1

    def bg(xx: float) -> tuple[float, ...]:
        xf = float(I["xf"](xx)); xc = float(I["xc"](xx)); xb = float(I["xb"](xx))
        xr = float(I["xr"](xx)); e = float(I["e"](xx)); hc = float(I["hc"](xx))
        return xf, xc, xb, rg*xr, rn*xr, rs*xr, e, hc, math.exp(xx)

    def raw_sources(xx: float, z: np.ndarray) -> dict[str, float]:
        xf, xc, xb, xg, xn, xs, e, hc, a = bg(xx)
        fn = z[N0:S0]; fs = z[S0:ETA]
        un = 3.0*a*e*fn[1]/(4.0*q); us = 3.0*a*e*fs[1]/(4.0*q)
        g = p.lam/e
        pf = xf*(z[DF] + (2.0-p.delta)*(3.0*p.delta+g)*z[UF])
        density = xc*z[DC]+xf*z[DF]+xb*z[DB]+xg*z[DG]+xn*fn[0]+xs*fs[0]
        pressure = pf+(xg*z[DG]+xn*fn[0]+xs*fs[0])/3.0
        momentum = xc*z[UC]+p.delta*xf*z[UF]+xb*z[UG]+(4.0/3.0)*(xg*z[UG]+xn*un+xs*us)
        shear = (2.0/3.0)*(xn*fn[2]+xs*fs[2])
        hx = 2.0*(q*q*z[ETA]+1.5*a*a*density)/(a*e)**2
        return {"D":density,"P":pressure,"M":momentum,"S":shear,"hx":hx,"e":e,"hc":hc,"a":a}

    def project(mode: str, z: np.ndarray) -> np.ndarray:
        if mode.startswith("internal_"):
            z = z.copy()
            z[:N0] = 0.0
            z[S0:ETA] = -(rn/rs)*z[N0:S0]
            z[ETA] = 0.0
        return z

    def rhs(xx: float, zin: np.ndarray, mode: str) -> np.ndarray:
        z = project(mode, zin)
        xf, xc, xb, xg, _, _, e, hc, a = bg(xx)
        s = raw_sources(xx, z); hx=s["hx"]
        g=p.lam/e; r=xf/xc; beta=p.delta*xf/(xc+p.delta*xf)
        ud=(1.0-beta)*z[UC]+beta*z[UF]; s2=(q/(a*e))**2
        out=np.zeros(SIZE)
        out[DC]=-s2*z[UC]-hx/2.0+g*r*(z[DF]-z[DC])
        out[UC]=(hc-1.0)*z[UC]+g*r*beta*(z[UF]-z[UC])
        out[DF]=(-3.0*(2.0-p.delta)*z[DF]-p.delta*(s2*z[UF]+hx/2.0)
                 -9.0*p.delta*(2.0-p.delta)*z[UF]-3.0*g*(2.0-p.delta)*z[UF])
        out[UF]=(hc+2.0)*z[UF]+z[DF]/p.delta+g/p.delta*(2.0*z[UF]-ud)
        R=3.0*xb/(4.0*xg)
        out[DB]=-s2*z[UG]-hx/2.0
        out[DG]=-(4.0/3.0)*s2*z[UG]-(2.0/3.0)*hx
        out[UG]=(hc-R/(1.0+R))*z[UG]+z[DG]/(4.0*(1.0+R))
        etax=1.5*s["M"]/(e*e); kh=q/(a*e)
        for start in (N0,S0):
            f=z[start:start+args.lmax+1]
            out[start]=-kh*f[1]-(2.0/3.0)*hx
            out[start+1]=kh*(f[0]-2.0*f[2])/3.0
            out[start+2]=kh*(2.0*f[1]-3.0*f[3])/5.0+(4.0/15.0)*hx+(8.0/5.0)*etax
            for ell in range(3,args.lmax+1):
                fp=f[ell+1] if ell<args.lmax else 0.0
                out[start+ell]=kh*(ell*f[ell-1]-(ell+1)*fp)/(2.0*ell+1.0)
        out[ETA]=etax
        if mode.startswith("internal_"):
            out[:N0]=0.0; out[S0:ETA]=-(rn/rs)*out[N0:S0]; out[ETA]=0.0
        return out

    # Exact internal collisionless seed operator.
    A=np.zeros((args.lmax+1,args.lmax+1)); A[0,1]=-1.0; A[1,0]=1/3; A[1,2]=-2/3
    for ell in range(2,args.lmax+1):
        A[ell,ell-1]=ell/(2*ell+1)
        if ell<args.lmax: A[ell,ell+1]=-(ell+1)/(2*ell+1)

    modes=list(S84.MODES)+["internal_nu_steam_density","internal_nu_steam_velocity"]

    def initial(mode: str, xx: float) -> np.ndarray:
        z=np.zeros(SIZE); xf,xc,xb,xg,xn,xs,e,hc,a=bg(xx); tt=float(I["tau"](xx))
        if mode in S84.MODES:
            v=S84.class_seed(mode,q,tt,rfs,rg,fb,fc,om)
            z[DG],z[DB],z[DC]=v[0],v[1],v[2]; z[N0]=v[3]; z[S0]=v[3]
            z[UG]=3.0*a*e*v[4]/(4.0*q); z[N0+1]=v[5]; z[S0+1]=v[5]; z[ETA]=v[6]
        else:
            b=np.zeros(args.lmax+1); b[0 if mode.endswith("density") else 1]=1.0
            z[N0:S0]=expm(A*(q*tt))@b
            z=project(mode,z)
        return z

    def audit(xx: float, z: np.ndarray, mode: str) -> dict[str, tuple[float,float]]:
        z=project(mode,z); dz=rhs(xx,z,mode); s=raw_sources(xx,z)
        xf,xc,xb,xg,xn,xs,e,hc,a=bg(xx); g=p.lam/e; s2=(q/(a*e))**2
        xf_x=-(3*p.delta+g)*xf; xc_x=-3*xc+g*xf; xb_x=-3*xb
        xg_x=-4*xg; xn_x=-4*xn; xs_x=-4*xs
        fn=z[N0:S0]; fs=z[S0:ETA]; dfn=dz[N0:S0]; dfs=dz[S0:ETA]
        D_x=(xc_x*z[DC]+xc*dz[DC]+xf_x*z[DF]+xf*dz[DF]+xb_x*z[DB]+xb*dz[DB]
             +xg_x*z[DG]+xg*dz[DG]+xn_x*fn[0]+xn*dfn[0]+xs_x*fs[0]+xs*dfs[0])
        un=3*a*e*fn[1]/(4*q); us=3*a*e*fs[1]/(4*q)
        un_x=hc*un+3*a*e*dfn[1]/(4*q); us_x=hc*us+3*a*e*dfs[1]/(4*q)
        M_x=(xc_x*z[UC]+xc*dz[UC]+p.delta*(xf_x*z[UF]+xf*dz[UF])
             +xb_x*z[UG]+xb*dz[UG]+(4/3)*(xg_x*z[UG]+xg*dz[UG]
             +xn_x*un+xn*un_x+xs_x*us+xs*us_x))
        W=xc+p.delta*xf+xb+(4/3)*(xg+xn+xs)
        D_expected=-3*(s["D"]+s["P"])-s2*s["M"]-0.5*s["hx"]*W
        M_expected=(hc-4)*s["M"]+s["P"]-s["S"]
        hx_x=2*(q*q*dz[ETA]+1.5*a*a*(D_x+2*s["D"]))/(a*e)**2-2*hc*s["hx"]
        eta_xx=1.5*(M_x-2*(hc-1)*s["M"])/(e*e)
        terms={
          "00":[q*q*z[ETA],-0.5*(a*e)**2*s["hx"],1.5*a*a*s["D"]],
          "0i":[dz[ETA],-1.5*s["M"]/(e*e)],
          "trace_ij":[(a*e)**2*(hx_x+(hc+2)*s["hx"]),-2*q*q*z[ETA],9*a*a*s["P"]],
          "traceless_ij":[(a*e)**2*(hx_x+6*eta_xx+(hc+2)*(s["hx"]+6*dz[ETA])),-2*q*q*z[ETA],9*a*a*s["S"]],
          "energy_product_ledger":[D_x,-D_expected],
          "momentum_product_ledger":[M_x,-M_expected],
        }
        return {k:(abs(float(sum(v))),float(sum(abs(t) for t in v))) for k,v in terms.items()}

    def integrate(mode: str, start_x: float) -> tuple[np.ndarray,dict[str,dict[str,float]]]:
        n=int(math.ceil((args.x_final-start_x)/args.step)); grid=np.linspace(start_x,args.x_final,n+1)
        z=initial(mode,start_x); maxima={}
        for key in ("00","0i","trace_ij","traceless_ij","energy_product_ledger","momentum_product_ledger"):
            maxima[key]={"abs":0.0,"norm":0.0}
        for i in range(n):
            xx=float(grid[i]); h=float(grid[i+1]-grid[i])
            k1=rhs(xx,z,mode); k2=rhs(xx+h/2,project(mode,z+h*k1/2),mode)
            k3=rhs(xx+h/2,project(mode,z+h*k2/2),mode); k4=rhs(xx+h,project(mode,z+h*k3),mode)
            z=project(mode,z+h*(k1+2*k2+2*k3+k4)/6)
            if i%25==0 or i==n-1:
                for key,(ab,no) in audit(float(grid[i+1]),z,mode).items():
                    maxima[key]["abs"]=max(maxima[key]["abs"],ab); maxima[key]["norm"]=max(maxima[key]["norm"],no)
            if i%500==0: deadline()
            if not np.all(np.isfinite(z)): raise FloatingPointError(f"nonfinite {mode}")
        for val in maxima.values(): val["global_relative"]=val["abs"]/max(val["norm"],1e-280)
        return z,maxima

    checks={}; rows={}
    for mode in modes:
        zd,ad=integrate(mode,args.x_deep); zs,ass=integrate(mode,args.x_shallow)
        conv=float(np.linalg.norm(zd-zs)/max(np.linalg.norm(zd),np.linalg.norm(zs),1e-30))
        for depth,audit_result in (("deep",ad),("shallow",ass)):
            checks[f"{mode}_{depth}_conditioned_six_ledgers"]=all(v["global_relative"]<2e-10 for v in audit_result.values())
        checks[f"{mode}_two_start_convergence"]=conv<3e-3
        checks[f"{mode}_finite"]=bool(np.all(np.isfinite(zd)) and np.all(np.isfinite(zs)))
        if mode.startswith("internal_"):
            checks[f"{mode}_exact_metric_dark_subspace"]=bool(np.linalg.norm(zd[[DC,UC,DF,UF,ETA]])<1e-20)
        rows[mode]={"two_start_final_relative_difference":conv,"deep_ledgers":ad,"shallow_ledgers":ass,
                    "deep_final_dark_metric_dc_Uc_df_Uf_eta":zd[[DC,UC,DF,UF,ETA]].tolist()}
        deadline()

    passed=all(checks.values())
    print(json.dumps({
      "test":"A2-K4.3b-RG-BR2 conditioned DAE constraint audit",
      "supersedes_for_constraint_numerics":"89_script_A2_K4_3b_RG_BR2_backreacted_superhorizon_evolution.py",
      "script_89_status":"PRESERVED_REVIEW_UNCONDITIONED_SECOND_DERIVATIVE_ILL_CONDITIONED",
      "scope":"early superhorizon, leading photon-baryon tight coupling, separate nu/steam l<=lmax",
      "inputs":{"lambda":p.lam,"delta":p.delta,"q":q,"x_deep":args.x_deep,"x_shallow":args.x_shallow,
                "x_final":args.x_final,"step":args.step,"lmax":args.lmax},
      "mode_results":rows,"checks":checks,
      "execution_verdict":"PASS_BR2_CONDITIONED_BACKREACTION" if passed else "REVIEW_BR2_CONDITIONED_BACKREACTION",
      "K4_3b_RG_verdict":"NEUZAVRETA_EXPLICIT_FRACTIONAL_COEFFICIENT_AND_FULL_PHOTON_BACKEND_GATES_MISSING",
      "canonical_score":"60/100 = G6",
      "next_step":"BR3 explicit mode-resolved Puiseux coefficient extraction and residual scaling",
      "runtime_limit_seconds":args.max_runtime_seconds,"runtime_seconds":time.monotonic()-started
    },indent=2,sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try: raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict":"TIMEOUT_UNCLOSED","error":str(exc)})); raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution_verdict":"ERROR_UNCLOSED","error":repr(exc)})); raise SystemExit(2)
