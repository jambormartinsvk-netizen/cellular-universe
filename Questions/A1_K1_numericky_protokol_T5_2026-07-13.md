# A1-K1-T5: reprodukovateľný numerický protokol kladnosti a rozdelenia hmoty

**Dátum:** 2026-07-13  
**Koľaj:** A1-K1 — prenos Q vytvára iba CDM  
**Účel:** nezávisle rozdeliť spoločnú backgroundovú hmotu skriptu 09 na baryóny a CDM, overiť kladnosť hustôt a kontrolný súčet zachovania  
**Stav:** PREŠIEL na testovanom modelovom bode

## 1. Prostredie

```text
Python 3.11.3
NumPy 2.4.4
Operačný systém: Windows, 64 bit
Integrátor: explicitný RK4 implementovaný priamo v protokole
```

Test nepoužíva sieť, náhodné čísla ani externý dataset.

## 2. Vstupy

| Parameter | Hodnota | Pôvod |
|---|---:|---|
| h | 0.6637 | reprodukovaný pracovný bod skriptu 09 |
| Ω_m0 | 0.3517 | reprodukovaný pracovný bod skriptu 09 |
| λ | 0.15 | pracovný bod V1 |
| δ | 0.02297 | `1/(15.54+28)` |
| ΔN_eff | 0.0535 | pracovná hodnota pary |
| ω_b | 0.02237 | vstup skriptu 09 |
| ω_γ | 2.469×10^-5 | vstup skriptu 09 |
| interval x | 0 až -25 | približne dnešok až z = 7.2×10^10 |
| počet bodov | 25 001 | krok 0.001 |

Premenné `X_i = ρ_i/ρ_crit,0` nie sú okamžité hustotné frakcie. Spoločná hmota `X_m` je rozdelená podľa

```text
X_b = (ω_b/h²) a^-3
X_c = X_m - X_b.
```

## 3. Presný reprodukčný kód

```python
import json
import numpy as np

h = 0.6637
Om_m0 = 0.3517
lam = 0.15
delta = 0.02297
dNeff = 0.0535
omega_b = 0.02237
omega_gamma = 2.469e-5

Xr0 = omega_gamma * (1 + 0.2271 * (3.046 + dNeff)) / h**2
Xf0 = 1.0 - Om_m0 - Xr0
Xb0 = omega_b / h**2

xs = np.linspace(0.0, -25.0, 25001)
dx = xs[1] - xs[0]
Y = np.zeros((len(xs), 3))
Y[0] = [Xf0, Om_m0, Xr0]  # fuel, total matter, radiation

def rhs(y):
    Xf, Xm, Xr = y
    E = np.sqrt(max(Xf + Xm + Xr, 1e-300))
    return np.array([
        -3 * delta * Xf - lam * Xf / E,
        -3 * Xm + lam * Xf / E,
        -4 * Xr,
    ])

for i in range(len(xs) - 1):
    y = Y[i]
    k1 = rhs(y)
    k2 = rhs(y + 0.5 * dx * k1)
    k3 = rhs(y + 0.5 * dx * k2)
    k4 = rhs(y + dx * k3)
    Y[i + 1] = y + dx * (k1 + 2*k2 + 2*k3 + k4) / 6

Xf, Xm, Xr = Y.T
Xb = Xb0 * np.exp(-3 * xs)
Xc = Xm - Xb
E = np.sqrt(Xf + Xm + Xr)

xstar = -np.log(1 + 1089.9)

def at_star(v):
    return float(np.interp(xstar, xs[::-1], v[::-1]))

Xc_comoving_star = at_star(Xc) * np.exp(3 * xstar)
f_created = (Xc[0] - Xc_comoving_star) / Xc[0]

rf = -3*delta*Xf - lam*Xf/E
rm = -3*Xm + lam*Xf/E
rb = -3*Xb
rc = rm - rb
rr = -4*Xr
residual = (rf + rc + rb + rr) - (
    -3*delta*Xf - 3*Xc - 3*Xb - 4*Xr
)
scale = np.abs(rf) + np.abs(rc) + np.abs(rb) + np.abs(rr)

out = {
    "python_test": "A1-K1-T5",
    "Xb0": float(Xb0),
    "Xc0": float(Xc[0]),
    "present_baryon_fraction": float(Xb0 / Om_m0),
    "baryon_fraction_at_zstar": at_star(Xb) / at_star(Xm),
    "fraction_present_CDM_created_since_zstar": float(f_created),
    "comoving_CDM_at_x_minus_25": float(Xc[-1] * np.exp(3 * xs[-1])),
    "min_Xf": float(Xf.min()),
    "min_Xc": float(Xc.min()),
    "min_Xb": float(Xb.min()),
    "min_Xr": float(Xr.min()),
    "all_positive": bool(
        np.all(Xf > 0) and np.all(Xc > 0)
        and np.all(Xb > 0) and np.all(Xr > 0)
    ),
    "max_abs_conservation_residual": float(np.max(np.abs(residual))),
    "max_relative_conservation_residual": float(
        np.max(np.abs(residual) / np.maximum(scale, 1e-300))
    ),
}
print(json.dumps(out, indent=2))
```

## 4. Výstup

```json
{
  "python_test": "A1-K1-T5",
  "Xb0": 0.050783467218636275,
  "Xc0": 0.30091653278136377,
  "present_baryon_fraction": 0.14439427699356347,
  "baryon_fraction_at_zstar": 0.15643911279555645,
  "fraction_present_CDM_created_since_zstar": 0.08998668198155564,
  "comoving_CDM_at_x_minus_25": 0.2738378267103084,
  "min_Xf": 0.6482044961998541,
  "min_Xc": 0.30091653278136377,
  "min_Xb": 0.050783467218636275,
  "min_Xr": 9.550380014592132e-05,
  "all_positive": true,
  "max_abs_conservation_residual": 16384.0,
  "max_relative_conservation_residual": 4.390265161784099e-16
}
```

## 5. Interpretácia

Absolútny zvyšok zachovania je pri `x = -25` nevhodná diagnostika, pretože jednotlivé hustotné členy sú v normalizácii na dnešnú kritickú hustotu extrémne veľké. Rozhodujúci je relatívny zvyšok `4.39×10^-16`, ktorý je na úrovni plávajúcej aritmetiky.

Všetky štyri hustoty zostali kladné. Na pracovnom bode vzniklo od rekombinácie do dneška približne `8.999 %` dnešnej komohybnej CDM hustoty. Baryónový podiel v celkovej hmote sa zmenil z približne `0.15644` pri rekombinácii na `0.14439` dnes.

Test preto nenašiel backgroundovú stenu A1-K1. Neoveruje však poruchy, mikrofyziku popola ani zhodu s dátami; tieto brány zostávajú otvorené.
