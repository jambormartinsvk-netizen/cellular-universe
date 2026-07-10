import numpy as np
from scipy.integrate import quad
import json

# constants / Planck inputs (per V4 methodology)
c_km = 299792.458
om_b = 0.02237      # omega_b h^2
om_m = 0.1430       # omega_m h^2 (total matter)
om_c = om_m - om_b  # CDM part
om_gamma = 2.469e-5
Neff = 3.046
om_r0 = om_gamma * (1 + 0.2271 * Neff)   # = 4.18e-5 (V4 convention)
zstar = 1089.9
astar = 1 / (1 + zstar)

def Hconf(a, extra_r=0.0, f_late=0.0, a_c=None, h=0.70):
    """H(a) in km/s/Mpc. extra_r: additional omega_r (dark radiation).
    f_late: fraction of CDM created instantaneously at a_c (energy-conserving:
    before a_c that fraction sits as constant-density fuel)."""
    om_r = om_r0 + extra_r
    om_L = h**2 - om_m - om_r   # flatness
    if f_late > 0 and a < a_c:
        cdm = (1 - f_late) * om_c * a**-3 + f_late * om_c * a_c**-3
    else:
        cdm = om_c * a**-3
    mat = cdm + om_b * a**-3
    return 100.0 * np.sqrt(mat + om_r * a**-4 + om_L)

def r_s(extra_r=0.0, f_late=0.0, a_c=None, h=0.70):
    Rb = lambda a: (3 * om_b / (4 * om_gamma)) * a
    integ = lambda a: c_km / (np.sqrt(3 * (1 + Rb(a))) * a**2 * Hconf(a, extra_r, f_late, a_c, h))
    v, _ = quad(integ, 1e-9, astar, limit=400)
    return v  # Mpc

def D_M(h, extra_r=0.0):
    integ = lambda a: c_km / (a**2 * Hconf(a, extra_r, 0.0, None, h))
    v, _ = quad(integ, astar, 1.0, limit=400)
    return v

def solve_h(theta_target, extra_r=0.0, f_late=0.0, a_c=None):
    rs = r_s(extra_r, f_late, a_c)  # rs insensitive to h (Lambda negligible pre-z*)
    lo, hi = 0.55, 0.80
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        th = rs / D_M(mid, extra_r)
        if th < theta_target:  # need smaller D_M -> larger h
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi), rs

# ---- validation: LCDM must reproduce h = 0.673 (V4 rule P1) ----
h_ref = 0.673
rs_ref = r_s(h=h_ref)
DM_ref = D_M(h_ref)
theta = rs_ref / DM_ref
h_back, _ = solve_h(theta)
print(json.dumps({"validation": {"rs_LCDM_Mpc": round(rs_ref, 2),
    "DM_LCDM_Mpc": round(DM_ref, 1), "100theta*": round(100 * theta, 5),
    "h_inverted": round(h_back, 4), "target": h_ref}}))

# ---- branch A: bread fuel at recombination ----
# best CMB-anchored point: H0=65.6, Om=0.359 -> Of=0.641, delta=0.03
h_A = 0.656
om_f0 = (1 - 0.359) * h_A**2
delta = 0.03
om_f_star = om_f0 * (1 + zstar)**(3 * delta)
tot_star = om_m * (1 + zstar)**3 + om_r0 * (1 + zstar)**4
print(json.dumps({"branch_A_fuel_fraction_at_zstar": float(om_f_star / tot_star)}))

# ---- branch B: late DM creation (fraction f created at z_c > z*) ----
resB = []
for zc in [3000, 10000, 100000]:
    for f in [0.1, 0.3]:
        h_new, rs_new = solve_h(theta, f_late=f, a_c=1/(1+zc))
        resB.append({"z_c": zc, "f": f, "rs_Mpc": round(rs_new, 2),
                     "d_rs_percent": round(100*(rs_new-rs_ref)/rs_ref, 3),
                     "H0": round(100*h_new, 2), "dH0": round(100*(h_new-h_ref), 2)})
        print(json.dumps(resB[-1]))

# ---- branch C: dark radiation ("steam"), Delta N_eff ----
for dN in [0.2, 0.4]:
    extra = om_gamma * 0.2271 * dN
    h_new, rs_new = solve_h(theta, extra_r=extra)
    print(json.dumps({"dNeff": dN, "rs_Mpc": round(rs_new, 2),
        "d_rs_percent": round(100*(rs_new-rs_ref)/rs_ref, 3),
        "H0": round(100*h_new, 2), "dH0": round(100*(h_new-h_ref), 2)}))
