import numpy as np
from scipy.integrate import quad

def F(k,m,W,Wp,Wpp):
    E2=W(k)+m*m; E=np.sqrt(E2)
    return k*k*( (3/16)*(1-Wp(k)/(3*k)-Wpp(k)/6)/E**5 + (5/96)*Wp(k)**2/E**7 - (1/8)/E**5 )

# --- Test 1: Lorentz-invariant dispersion W=k^2, cutoff -> infinity : must be EXACTLY zero
W=lambda k:k*k; Wp=lambda k:2*k; Wpp=lambda k:2.0
for m in [0.01,0.2,1.0,5.0]:
    val,err=quad(F,0,np.inf,args=(m,W,Wp,Wpp),limit=400)
    print(f"  LI, cutoff=inf, m={m:5.2f}:  integral = {val: .3e}  (quad err {err:.1e})   -> B-A = {val/(4*np.pi**2): .3e}")

# --- Test 2: LI dispersion, spatial cutoff k_max = (6 pi^2)^(1/3)
kmax=(6*np.pi**2)**(1/3)
print("\n  k_max =",round(kmax,4))
for m in [0.2,1.0]:
    val,_=quad(F,0,kmax,args=(m,W,Wp,Wpp),limit=400)
    BA=val/(4*np.pi**2)
    print(f"  LI + cutoff, m={m:4.2f}: B-A = {BA: .6e}   analytic -1/(96 pi^2 kmax^2) = {-1/(96*np.pi**2*kmax**2): .6e}")
print("  -> audit quotes -6.9468e-5 ; 16pi^2*(B-A) =",round(16*np.pi**2*(-1/(96*np.pi**2*kmax**2)),5))
