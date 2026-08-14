"""
Demonstracia harnessu na uz overenom vypocte: null-kontroly smyckovej formuly
z externeho auditu 2, Dodatok A3.

Spustitelne samostatne:  python A0K5_demo_nullchecks.py
"""
import numpy as np
from scipy.integrate import quad
from qcts_check import Run

r = Run("A0K5_nullchecks",
        question="Q-A0-LORENTZ-RADIATIVE-STABILITY")

def F(k, m, W, Wp, Wpp):
    E2 = W(k) + m*m; E = np.sqrt(E2)
    return k*k*((3/16)*(1 - Wp(k)/(3*k) - Wpp(k)/6)/E**5
                + (5/96)*Wp(k)**2/E**7 - (1/8)/E**5)

W, Wp, Wpp = (lambda k: k*k), (lambda k: 2*k), (lambda k: 2.0)
kmax = (6*np.pi**2)**(1/3)

# --- POVINNA 1: Lorentzovsky invariantna disperzia, cutoff -> nekonecno
for m in (0.2, 1.0):
    val, _ = quad(F, 0, np.inf, args=(m, W, Wp, Wpp), limit=400)
    r.is_zero(f"LI disperzia, cutoff=inf, m={m}", val/(4*np.pi**2), tol=1e-12,
              why="LI disperzia nesmie generovat LV; nenulovy vysledok = chyba implementacie")

# --- POVINNA 2: analyticka kotva pri priestorovom cutoffe
val, _ = quad(F, 0, kmax, args=(1e-3, W, Wp, Wpp), limit=400)
r.check("LI + priestorovy cutoff vs -1/(96 pi^2 kmax^2)",
        val/(4*np.pi**2), -1/(96*np.pi**2*kmax**2), tol=2e-3, kind="ANCHOR",
        absolute=False,
        why="uzavrety tvar; overuje normalizaciu, prefaktor aj integracnu mez")

# --- CONVERGENCE: stabilita voci integracnej presnosti
ser = [quad(F, 0, kmax, args=(1e-3, W, Wp, Wpp), limit=L)[0]/(4*np.pi**2)
       for L in (50, 200, 800)]
r.converged("integracny limit", ser, rtol=1e-9)

r.note("cislo nizsie meria NEKOVARIANCIU REGULATORA, nie fyziku siete: "
       "disperzia je exaktne LI, jediny zdroj LV je priestorovy cutoff v jednom rame")
r.result("16 pi^2 (B-A) pri LI disperzii a cutoffe", 16*np.pi**2*ser[-1], unit="1")
r.finish()
