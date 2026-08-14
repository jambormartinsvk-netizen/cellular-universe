import numpy as np
# --- fix of audit Appendix A1 typo: /1091**3 not *1091**3 ---
from scipy.integrate import solve_ivp
km=48*np.pi**2/35+2; delta=1/(km+28); h,lam,ob=0.6637,0.15,0.02237
def bg(lam_,del_,h_,Om0):
    Or0=4.15e-5/h_**2; Ob0=ob/h_**2
    y0=[1-Om0-Or0,Om0-Ob0,Ob0,Or0]
    def r(x,y):
        A,B,Cc,D=y; E=np.sqrt(max(sum(y),1e-300)); s=lam_*A/E
        return [-3*del_*A-s,-3*B+s,-3*Cc,-4*D]
    xg=np.linspace(0,-9,200001)
    s=solve_ivp(r,[0,-9],y0,t_eval=xg,rtol=1e-13,atol=1e-18,method="DOP853")
    return s.t[::-1],s.y[:,::-1]
X,Y=bg(lam,delta,h,0.3517); i=np.argmin(abs(np.exp(X)-1/1091))
om_rec=(Y[1]+Y[2])[i]/1091**3*h**2
print("CORRECTED omega_m(rec) =",round(om_rec,5)," (audit says 0.14299)")
print("  sigma vs Planck 0.1431+-0.0012:",round((om_rec-0.1431)/0.0012,2))

# --- II.6 : relation (28) inferred as n_s = 1 - (3/2)delta ---
print()
def ns_of_C(Cv,alpha=1.5): return 1-alpha/(km+Cv)
def C_of_ns(ns,alpha=1.5): return alpha/(1-ns)-km
print("n_s(C=28) =",round(ns_of_C(28),6))
for lab,ns in [("best",0.9649),("1s-",0.9649-0.0042),("1s+",0.9649+0.0042),
               ("2s-",0.9649-0.0084),("2s+",0.9649+0.0084),
               ("3s-",0.9649-0.0126),("3s+",0.9649+0.0126)]:
    print(f"  {lab}: n_s={ns:.4f} -> C={C_of_ns(ns):.2f}")
for Cv in [28,56,118]:
    print(f"  C={Cv}: n_s={ns_of_C(Cv):.4f}, sigma={(ns_of_C(Cv)-0.9649)/0.0042:.2f}")

# --- II.7 : steam vs CMB Planck spectra ---
print()
h_p=6.62607015e-34; kB=1.380649e-23; c=2.99792458e8
def Bnu(nu,T): return 2*h_p*nu**3/c**2/np.expm1(h_p*nu/(kB*T))
T_s,T_c=0.905074,2.72548
for f in [30e9,53.21e9,100e9,217e9]:
    print(f"  {f/1e9:6.2f} GHz : steam/CMB = {100*Bnu(f,T_s)/Bnu(f,T_c):.2f} %")
print("  rho_steam/rho_CMB =",round(100*(T_s/T_c)**4,3),"%   (2 dof vs 2 dof)")
print("  Wien freq peak of 0.905K:",round(2.821439*kB*T_s/h_p/1e9,2),"GHz")

# --- II.4 : is S8*H0 an identity? ---
print()
S8=[0.885610,0.880025,0.874500]; H0=[65.79214,66.08320,66.37433]
pr=[a*b for a,b in zip(S8,H0)]
print("  S8*H0 =",[round(p,3) for p in pr],"spread =",round(100*(max(pr)-min(pr))/np.mean(pr),3),"%")
