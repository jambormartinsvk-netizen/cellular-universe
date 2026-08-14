import numpy as np
from scipy.integrate import solve_ivp

km = 48*np.pi**2/35 + 2; C = 28; delta = 1/(km+C)
print("k_mean =", km, " delta =", delta, " w_f =", -1+delta)

h, lam, ob = 0.6637, 0.15, 0.02237

def bg(lam_, del_, h_, Om0):
    Or0 = 4.15e-5/h_**2; Ob0 = ob/h_**2
    y0 = [1-Om0-Or0, Om0-Ob0, Ob0, Or0]
    def r(x, y):
        A,B,Cc,D = y; E = np.sqrt(max(sum(y),1e-300)); s = lam_*A/E
        return [-3*del_*A-s, -3*B+s, -3*Cc, -4*D]
    xg = np.linspace(0,-9,200001)
    s = solve_ivp(r,[0,-9],y0,t_eval=xg,rtol=1e-13,atol=1e-18,method="DOP853")
    return s.t[::-1], s.y[:,::-1]

X, Y = bg(lam, delta, h, 0.3517)
E2 = Y.sum(axis=0)
tr = np.trapezoid(np.exp(3*X)*lam*Y[0]/np.sqrt(E2), X)
i = np.argmin(abs(np.exp(X)-1/1091))
om_rec = (Y[1]+Y[2])[i]*1091**3*h**2
print("ash from transfer =", tr)
print("omega_m(rec)      =", om_rec, " Planck 0.1431 +- 0.0012 -> sigma =", (om_rec-0.1431)/0.0012)
print("forced Om0        =", om_rec/h**2 + tr)

# lambda scan with self-consistent Om0
print()
print(" lam    Om0      S8(rel)   ")
for L in [0.0,0.05,0.10,0.15,0.20]:
    # iterate Om0 to self-consistency at fixed omega_m(rec)
    Om0 = 0.35
    for _ in range(60):
        X,Y = bg(L, delta, h, Om0)
        E2 = Y.sum(axis=0)
        tr = np.trapezoid(np.exp(3*X)*L*Y[0]/np.sqrt(E2), X)
        Om0 = 0.14299/h**2 + tr
    print(f" {L:.2f}  {Om0:.4f}   ash={tr:.5f}")
