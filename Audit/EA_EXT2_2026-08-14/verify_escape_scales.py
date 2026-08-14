import numpy as np
# Audit III.5 result: 16 pi^2 (B-A) = 0.1026 ln(Lambda/m) + 0.294 ,  g = Lambda
def dc2(lnLm, gOverL=1.0):
    return (0.1026*lnLm + 0.294)/(16*np.pi**2) * gOverL**2
for lab,ln in [("electron",51.5),("proton",44.0),("Higgs",39.1)]:
    print(f"  {lab:9s} ln(L/m)={ln:5.1f}  dc2/c2 = {dc2(ln):.3e}")

print("\n  --- how much suppression is needed ---")
base=dc2(51.5)
for lim in [1e-16,1e-19,1e-23]:
    need=lim/base
    print(f"  limit {lim:.0e}: suppression {need:.2e} -> (M/Lambda) = {np.sqrt(need):.2e}"
          f"  i.e. EFT cutoff M = {np.sqrt(need)*1.22e19:.2e} GeV  (Lambda=M_Pl)")

print("\n  --- anomalous dimension route (audit III.6c) ---")
for lim in [1e-16,1e-19,1e-23]:
    need=lim/base
    print(f"  limit {lim:.0e}: Delta = {np.log(1/need)/51.5:.3f}")
