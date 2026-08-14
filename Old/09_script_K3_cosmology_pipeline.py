import numpy as np
from scipy.integrate import quad
import json

c_km=299792.458
om_b=0.02237; OM_M_STAR=0.1430   # Planck rho_m at z*
om_gamma=2.469e-5
zstar=1089.9; xstar=-np.log(1+zstar)
theta_target=None

def om_r_total(dNeff):
    return om_gamma*(1+0.2271*(3.046+dNeff))

# ---------- V1 background: integrate back from today ----------
def background(h, Om_m0, lam, delta, dNeff, xmin=-7.8, n=8000):
    om_r0=om_r_total(dNeff)
    Om_r0=om_r0/h**2
    Om_f0=1.0-Om_m0-Om_r0
    xs=np.linspace(0.0,xmin,n)
    dx=xs[1]-xs[0]
    Y=np.zeros((n,3)); Y[0]=[Om_f0,Om_m0,Om_r0]
    def f(y):
        Of,Om,Or=y
        E=np.sqrt(max(Of+Om+Or,1e-30))
        return np.array([-3*delta*Of - lam*Of/E,
                         -3*Om + lam*Of/E,
                         -4*Or])
    for i in range(n-1):
        y=Y[i]
        k1=f(y); k2=f(y+0.5*dx*k1); k3=f(y+0.5*dx*k2); k4=f(y+dx*k3)
        Y[i+1]=y+dx/6*(k1+2*k2+2*k3+k4)
    E=np.sqrt(Y.sum(axis=1))
    return xs,Y,E

def anchor(lam, delta, dNeff, DM_target):
    lo,hi=0.55,0.80
    for _ in range(25):
        h=0.5*(lo+hi)
        Om_m0=0.30
        for _ in range(6):   # inner self-consistency
            xs,Y,E=background(h,Om_m0,lam,delta,dNeff)
            Om_star=np.interp(xstar,xs[::-1],Y[::-1,1])
            target=OM_M_STAR*np.exp(-3*xstar)/h**2
            Om_m0*=target/Om_star
        # D_M
        m=xs>=xstar
        integ=np.exp(-xs[m])/E[m]
        DM=c_km/(100*h)*np.trapezoid(integ[::-1],xs[m][::-1])
        if DM>DM_target: lo=h
        else: hi=h
    return h,Om_m0,xs,Y,E

# ---------- r_s (pre-z* standard; fuel negligible there) ----------
def r_s(h,dNeff):
    om_r0=om_r_total(dNeff)
    def H(a):
        oL=h**2-OM_M_STAR-om_r0   # irrelevant pre-z*
        return 100*np.sqrt(OM_M_STAR*a**-3+om_r0*a**-4+max(oL,0))
    Rb=lambda a:(3*om_b/(4*om_gamma))*a
    f=lambda a:c_km/(np.sqrt(3*(1+Rb(a)))*a**2*H(a))
    return quad(f,1e-9,1/(1+zstar),limit=400)[0]

# ---------- V2 shadow + CPL ----------
def cpl(xs,Y,E,Om_m0,Om_r0_val):
    x=xs; rho=E**2-Om_m0*np.exp(-3*x)-Om_r0_val*np.exp(-4*x)
    z=np.exp(-x)-1
    m=(z>0.0)&(z<1.0)&(rho>1e-6)
    lnr=np.log(rho[m])
    w=-1-(1/3)*np.gradient(lnr,x[m])
    a=np.exp(x[m])
    W=rho[m]
    A=np.vstack([np.ones_like(a),(1-a)]).T
    WA=A*W[:,None]
    coef=np.linalg.lstsq(WA, w*W, rcond=None)[0]
    return coef  # w0, wa

# ---------- V3 growth ----------
def growth(xs,Y,E):
    x=xs[::-1]; Om=Y[::-1,1]; Ee=E[::-1]
    dlnE=np.gradient(np.log(Ee),x)
    x0=-np.log(1001.0)
    i0=np.searchsorted(x,x0)
    d=np.exp(x[i0]); Th=-d
    for i in range(i0,len(x)-1):
        dx=x[i+1]-x[i]
        def f(state,i):
            dd,tt=state
            return np.array([-tt, -(2+dlnE[i])*tt-1.5*(Om[i]/Ee[i]**2)*dd])
        s=np.array([d,Th])
        k1=f(s,i); k2=f(s+0.5*dx*k1,i); k3=f(s+0.5*dx*k2,i); k4=f(s+dx*k3,min(i+1,len(x)-1))
        s=s+dx/6*(k1+2*k2+2*k3+k4)
        d,Th=s
    return d

def run(label, lam, delta, dNeff, lcdm_D=None, lcdm_h=None):
    # anchor: DM target from r_s/theta
    global theta_target
    if theta_target is None:
        rs0=r_s(0.673,0.0); 
        # LCDM DM at h=0.673 for theta calibration
        h0=0.673; om_r0=om_r_total(0.0)
        def Hl(a): 
            oL=h0**2-OM_M_STAR-om_r0
            return 100*np.sqrt(OM_M_STAR*a**-3+om_r0*a**-4+oL)
        DM0=quad(lambda a:c_km/(a**2*Hl(a)),1/(1+zstar),1,limit=400)[0]
        theta_target=rs0/DM0
    rs=r_s(0.673,dNeff)
    DM_t=rs/theta_target
    h,Om_m0,xs,Y,E=anchor(lam,delta,dNeff,DM_t)
    om_r0=om_r_total(dNeff); Om_r0=om_r0/h**2
    w0,wa=cpl(xs,Y,E,Om_m0,Om_r0)
    D=growth(xs,Y,E)
    out={"label":label,"H0":round(100*h,2),"Om_m":round(Om_m0,4),
         "w0":round(w0,3),"wa":round(wa,3),"rs":round(rs,2)}
    if lcdm_D is not None:
        s8=0.811*D/lcdm_D
        S8=s8*np.sqrt(Om_m0/0.3)
        out["sigma8"]=round(s8,4); out["S8"]=round(S8,4)
        chi2=((w0+0.75)/0.06)**2+((wa+0.86)/0.25)**2+((S8-0.759)/0.024)**2
        out["chi2_3front"]=round(chi2,1)
    print(json.dumps(out)); return h,Om_m0,D

# 1) LCDM validation
h_l,Om_l,D_l=run("LCDM_validacia",0.0,0.0,0.0)
# LCDM chi2 for reference
w0l,wal,S8l=-1.0,0.0,None
# growth ref done inside; compute its S8/chi2:
s8_l=0.811; S8_l=0.811*np.sqrt(Om_l/0.3)
chi2_l=((-1+0.75)/0.06)**2+((0+0.86)/0.25)**2+((S8_l-0.759)/0.024)**2
print(json.dumps({"label":"LCDM_score","S8":round(S8_l,4),"chi2_3front":round(chi2_l,1)}))
# 2) model bez pary
run("model_bez_pary",0.15,0.03,0.0,lcdm_D=D_l)
# 3) model s parou
run("model_s_parou",0.15,0.03,0.0535,lcdm_D=D_l)
