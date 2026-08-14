#!/usr/bin/env python
"""BR3A mode-resolved Puiseux source coefficient extraction.

On the exact A1-K1 background, evolve the K4 dark test field in the regular
synchronous metric of each CLASS collective seed.  Extract the leading fuel
pressure coefficient and the ash-transfer exponent.  The analytic radiation
era response to h_x=H a^n is

  U_f/h_x = -1/(2 D_n),
  delta_f/h_x = -delta (n-1)/(2 D_n),
  delta p_f/(rho_f h_x) = -delta(n+5-3delta)/(2 D_n),
  D_n=(n-1)(n+6-3delta)+9(2-delta).

This resolves the fractional *sources*. It does not yet solve the induced
fractional metric/species coefficient and therefore cannot close K4.3b/G7.
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

HERE=Path(__file__).resolve().parent


def load(name,filename):
    path=HERE/filename; spec=importlib.util.spec_from_file_location(name,path)
    if spec is None or spec.loader is None: raise ImportError(path)
    mod=importlib.util.module_from_spec(spec); sys.modules[name]=mod; spec.loader.exec_module(mod); return mod


B13=load("k4_br3a_bg13","13_script_A1_K1_cdm_background_audit_exact_zstar.py")
B11=B13.BASE
S84=load("k4_br3a_seed84","84_script_A2_K4_3b_RG_CLASS_analytic_collective_seed_CAMB_crosscheck.py")


def slope(x,y):
    mask=np.isfinite(y)&(np.abs(y)>1e-280)
    if np.count_nonzero(mask)<20: return float("nan")
    return float(np.polyfit(x[mask],np.log(np.abs(y[mask])),1)[0])


def median_ratio(num,den):
    mask=np.isfinite(num)&np.isfinite(den)&(np.abs(den)>1e-280)
    if np.count_nonzero(mask)<20: return float("nan")
    return float(np.median(num[mask]/den[mask]))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--max-runtime-seconds",type=float,default=40.0)
    ap.add_argument("--x-deep",type=float,default=-25.0)
    ap.add_argument("--x-shallow",type=float,default=-23.0)
    ap.add_argument("--x-final",type=float,default=-14.0)
    ap.add_argument("--step",type=float,default=2e-3)
    ap.add_argument("--background-step",type=float,default=5e-4)
    ap.add_argument("--k-mpc",type=float,default=.05)
    args=ap.parse_args()
    if not (0<args.max_runtime_seconds<=50): ap.error("runtime outside (0,50]")
    if not (-27<=args.x_deep<=-24): ap.error("deep start outside range")
    if not (1<=args.x_shallow-args.x_deep<=3): ap.error("start separation outside range")
    if not (-16<=args.x_final<=-13): ap.error("final outside range")
    if not (5e-4<=args.step<=5e-3): ap.error("step outside range")
    t0=time.monotonic()
    def deadline():
        if time.monotonic()-t0>args.max_runtime_seconds: raise TimeoutError("BR3A deadline exceeded")

    p=B11.ModelParameters(); xd,sd,xbnow=B13.integrate_background(
        p,B11.IntegrationSettings(x_min=args.x_deep,step=args.background_step))
    xbg=np.asarray(xd[::-1]); st=np.asarray(sd[::-1]); xf,xm,xr=st.T
    xb=xbnow*np.exp(-3*xbg); xc=xm-xb; e=np.sqrt(xf+xm+xr); aa=np.exp(xbg)
    hc=1+(-3*p.delta*xf-3*xm-4*xr)/(2*e**2)
    tau=np.zeros_like(xbg); tau[0]=aa[0]/math.sqrt(B11.radiation_density_today(p))
    integ=np.exp(-xbg)/e; tau[1:]=tau[0]+np.cumsum(.5*np.diff(xbg)*(integ[:-1]+integ[1:]))
    early=(xbg>=args.x_deep+.5)&(xbg<=args.x_deep+2)
    fb=float(np.mean(xb[early]/xm[early])); fc=float(np.mean(xc[early]/xm[early]))
    den=1+.2271*(p.neff_standard+p.delta_neff); rg=1/den; rfs=1-rg
    om=float(np.mean(aa[early]*xm[early]/np.sqrt(xr[early])))
    q=args.k_mpc/(100*p.h/299792.458)
    I={name:PchipInterpolator(xbg,val) for name,val in {
       "xf":xf,"xc":xc,"e":e,"hc":hc,"tau":tau}.items()}

    # Exact expected leading synchronous powers read from the CLASS series.
    leading_hx={
      "initial_adiabatic":2.0,"initial_iso_CDM":1.0,"initial_iso_baryon":1.0,
      "initial_iso_neutrino":3.0,"initial_iso_neutrino_vel":2.0}
    leading_dc={
      "initial_adiabatic":2.0,"initial_iso_CDM":0.0,"initial_iso_baryon":1.0,
      "initial_iso_neutrino":3.0,"initial_iso_neutrino_vel":2.0}

    # Build analytic standard h_x=-2 delta_c,x over the whole background grid.
    seeds={}
    for mode in S84.MODES:
        vals=np.vstack([S84.class_seed(mode,q,float(tt),rfs,rg,fb,fc,om) for tt in tau])
        dc_i=PchipInterpolator(xbg,vals[:,2]); hx_i=PchipInterpolator(xbg,-2*dc_i.derivative()(xbg))
        seeds[mode]={"dc":dc_i,"hx":hx_i}

    def b(xx):
        xf=float(I["xf"](xx)); xc=float(I["xc"](xx)); ee=float(I["e"](xx))
        return xf,xc,ee,float(I["hc"](xx)),math.exp(xx)

    def rhs(xx,z,mode):
        dc,uc,df,uf=z; xf,xc,ee,hcv,av=b(xx); g=p.lam/ee; r=xf/xc
        beta=p.delta*xf/(xc+p.delta*xf); ud=(1-beta)*uc+beta*uf
        s2=(q/(av*ee))**2; hxv=float(seeds[mode]["hx"](xx))
        return np.array([
          -s2*uc-hxv/2+g*r*(df-dc),
          (hcv-1)*uc+g*r*beta*(uf-uc),
          -3*(2-p.delta)*df-p.delta*(s2*uf+hxv/2)-9*p.delta*(2-p.delta)*uf-3*g*(2-p.delta)*uf,
          (hcv+2)*uf+df/p.delta+g/p.delta*(2*uf-ud)])

    def integrate(mode,start):
        n=math.ceil((args.x_final-start)/args.step); grid=np.linspace(start,args.x_final,n+1)
        z=np.zeros((n+1,4)); z[0,0]=float(seeds[mode]["dc"](start))
        for i in range(n):
            xx=float(grid[i]); h=float(grid[i+1]-grid[i]); y=z[i]
            k1=rhs(xx,y,mode); k2=rhs(xx+h/2,y+h*k1/2,mode); k3=rhs(xx+h/2,y+h*k2/2,mode); k4=rhs(xx+h,y+h*k3,mode)
            z[i+1]=y+h*(k1+2*k2+2*k3+k4)/6
            if i%500==0: deadline()
            if not np.all(np.isfinite(z[i+1])): raise FloatingPointError(mode)
        return grid,z

    def extract(mode,grid,z):
        # Last 2.5 e-folds are common to both starts and still deeply early.
        mask=(grid>=args.x_final-2.5)&(grid<=args.x_final-.25)
        xx=grid[mask]; zz=z[mask]; hxv=np.asarray(seeds[mode]["hx"](xx),float)
        xfv=np.asarray(I["xf"](xx),float); xcv=np.asarray(I["xc"](xx),float); ev=np.asarray(I["e"](xx),float)
        of=xfv/(ev*ev); g=p.lam/ev; r=xfv/xcv
        pfhat=of*(zz[:,2]+(2-p.delta)*(3*p.delta+g)*zz[:,3])
        ash=g*r*(zz[:,2]-zz[:,0])
        return {
          "hx_exponent":slope(xx,hxv),"Omega_f_exponent":slope(xx,of),
          "fuel_pressure_source_exponent":slope(xx,pfhat),"ash_transfer_exponent":slope(xx,ash),
          "Uf_over_hx":median_ratio(zz[:,3],hxv),
          "fuel_pressure_over_Omegaf_hx":median_ratio(pfhat,of*hxv),
          "fit_window":[float(xx[0]),float(xx[-1])],
          "max_abs_fuel_pressure_source":float(np.max(np.abs(pfhat))),
          "max_abs_ash_fractional_source":float(np.max(np.abs(ash)))}

    checks={}; rows={}; p_f=4-3*p.delta; p_c=5-3*p.delta
    for mode in S84.MODES:
        gd,zd=integrate(mode,args.x_deep); gs,zs=integrate(mode,args.x_shallow)
        rd=extract(mode,gd,zd); rslt=extract(mode,gs,zs); n=leading_hx[mode]
        D=(n-1)*(n+6-3*p.delta)+9*(2-p.delta)
        ufcoef=-1/(2*D); pcoef=-p.delta*(n+5-3*p.delta)/(2*D)
        expected_pressure_power=p_f+n; expected_ash_power=p_c+leading_dc[mode]
        checks[f"{mode}_hx_leading_power"]=abs(rd["hx_exponent"]-n)<.03
        checks[f"{mode}_Omega_f_fractional_power"]=abs(rd["Omega_f_exponent"]-p_f)<.003
        checks[f"{mode}_fuel_pressure_fractional_power"]=abs(rd["fuel_pressure_source_exponent"]-expected_pressure_power)<.08
        checks[f"{mode}_ash_transfer_fractional_power"]=abs(rd["ash_transfer_exponent"]-expected_ash_power)<.10
        checks[f"{mode}_Uf_coefficient"]=abs(rd["Uf_over_hx"]-ufcoef)<max(2e-4,.05*abs(ufcoef))
        checks[f"{mode}_pressure_coefficient"]=abs(rd["fuel_pressure_over_Omegaf_hx"]-pcoef)<max(2e-5,.06*abs(pcoef))
        checks[f"{mode}_two_start_Uf_coefficient"]=abs(rd["Uf_over_hx"]-rslt["Uf_over_hx"])<max(1e-5,.01*abs(rd["Uf_over_hx"]))
        checks[f"{mode}_two_start_pressure_coefficient"]=abs(rd["fuel_pressure_over_Omegaf_hx"]-rslt["fuel_pressure_over_Omegaf_hx"])<max(1e-6,.01*abs(rd["fuel_pressure_over_Omegaf_hx"]))
        rows[mode]={"leading_hx_power_declared":n,"leading_dc_power_declared":leading_dc[mode],
          "analytic_Uf_over_hx":ufcoef,"analytic_pressure_over_Omegaf_hx":pcoef,
          "expected_fuel_pressure_source_power":expected_pressure_power,"expected_ash_transfer_power":expected_ash_power,
          "deep":rd,"shallow":rslt}
        deadline()
    passed=all(checks.values())
    out={"test":"A2-K4.3b-RG-BR3A mode-resolved Puiseux sources",
      "scope":"fixed regular synchronous standard metric; extracts fractional sources, not induced metric coefficient",
      "background_fractional_powers":{"Omega_f":p_f,"g_r":p_c},"mode_results":rows,"checks":checks,
      "execution_verdict":"PASS_BR3A_PUISEUX_SOURCE_COEFFICIENTS" if passed else "REVIEW_BR3A_PUISEUX_SOURCE_COEFFICIENTS",
      "K4_3b_RG_verdict":"NEUZAVRETA_INDUCED_FRACTIONAL_METRIC_SPECIES_COEFFICIENT_AND_FULL_BACKEND_MISSING",
      "canonical_score":"60/100 = G6","next_step":"BR3B solve the induced fractional metric/species coefficient system",
      "runtime_limit_seconds":args.max_runtime_seconds,"runtime_seconds":time.monotonic()-t0}
    print(json.dumps(out,indent=2,sort_keys=True)); return 0 if passed else 1


if __name__=="__main__":
    try: raise SystemExit(main())
    except TimeoutError as exc:
        print(json.dumps({"execution_verdict":"TIMEOUT_UNCLOSED","error":str(exc)})); raise SystemExit(124)
    except Exception as exc:
        print(json.dumps({"execution_verdict":"ERROR_UNCLOSED","error":repr(exc)})); raise SystemExit(2)
