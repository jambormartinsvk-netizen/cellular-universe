# A2.2 — odvodenie a superhorizontové testy A2-K3 a A2-K4

**Dátum:** 2026-07-13  
**Výsledok A2-K3:** `MŔTVA — ARCHIVOVANÁ` (M-010)  
**Výsledok A2-K4:** `MŔTVA — ARCHIVOVANÁ` (M-011)  
**Nezmenený background:** A1-K1, `Gamma=lambda H0`, `lambda=0.15`, `delta=0.02297`

## 1. Spoločné konvencie

Používame Newtonovu gauge

```text
ds^2=a^2[-(1+2 Psi)d eta^2+(1-2 Phi)delta_ij dx^i dx^j],
theta_A=-k^2 v_A,
V_A=theta_A/k^2,
w_f=-1+delta,
c_s,f^2=1,
c_a,f^2=w_f.
```

Tok energie je v oboch koľajach palivo -> CDM:

```text
Q_f=-Gamma rho_f,
Q_c=+Gamma rho_f,
Gamma>0.
```

Primárny formalizmus Clemson et al. používa `Q_x=Gamma_ref rho_x`, kde `Gamma_ref>0` znamená CDM -> dark energy. Presné mapovanie je preto

```text
x -> f,
Gamma_ref=-Gamma,
1+w_f=delta>0.
```

## 2. Spoločné kontinuity

Smer prenosovej štvorrýchlosti nemení pri tomto skalári prvotné kontinuitné rovnice. Pre K3 aj K4 platí

```text
delta_c'+theta_c-3 Phi'
=a Gamma (rho_f/rho_c)(delta_f-delta_c+Psi),

delta_f'+3 mathcal H(1-w_f)delta_f+(1+w_f)theta_f
+9 mathcal H^2(1-w_f^2)theta_f/k^2-3(1+w_f)Phi'
=-a Gamma[Psi+3 mathcal H(1-w_f)theta_f/k^2].
```

Tlaková porucha zostáva

```text
delta p_f=delta rho_f
+(1-w_f)[3 mathcal H(1+w_f)+a Gamma]
 rho_f theta_f/k^2.
```

## 3. A2-K3 — prenos rovnobežný s palivom

### 3.1 Definícia

```text
Q_f^mu=-Gamma rho_f u_f^mu,
Q_c^mu=+Gamma rho_f u_f^mu.
```

Prenos hybnosti je nulový v rámci paliva, nie v rámci CDM.

### 3.2 Eulerove rovnice po mapovaní znamienka

Z rovníc (36)–(37) Clemson et al. vychádza

```text
theta_c'+mathcal H theta_c-k^2 Psi
=a Gamma(rho_f/rho_c)(theta_f-theta_c),

theta_f'-2 mathcal H theta_f-k^2 delta_f/(1+w_f)-k^2 Psi
=a Gamma theta_f/(1+w_f).
```

Skript 26 overil obe kontinuity, obe Eulerove rovnice, veľkoškálové znamienko, štyri nulové limity a backgroundovú bilanciu: `10/10 PASS`.

### 3.3 Gauge-invariantný superhorizontový mód

Relatívna rýchlosť `V_f-V_c` je gauge-invariantná. Vedúci homogénny palivový mód oproti `Gamma=0` spĺňa

```text
d ln R/dt=Gamma/(1+w_f)=Gamma/delta,
R_2/R_1=exp[Gamma Delta t/delta].
```

Na rovnakom A1-K1 backgrounde:

```text
lambda/delta=6.5302568568,
H0 Delta t(z_star->0)=0.9351169231,
N_K3=6.1065536987,
R_0/R_star=448.7893835.
```

Relatívny rozdiel exponentu medzi krokmi `5e-4` a `2.5e-4` je `9.1895e-9 < 1e-8`. Referenčná K3 stena `lambda/delta >~ 2` je prekročená.

### 3.4 Verdikt K3

**A2-K3 je MŔTVA — ARCHIVOVANÁ (M-010).**

Smer `u_f` znížil exponent oproti K1 na polovicu, ale neodstránil pól `Gamma/(1+w_f)` ani rastúci fyzikálny relatívny mód.

## 4. A2-K4 — prenos rovnobežný s celým tmavým sektorom

### 4.1 Jednoznačná definícia `u_d`

„Celková rýchlosť tmavého sektora“ sa uzamyká ako energia-frame, teda entalpická rýchlosť:

```text
(rho_c+(1+w_f)rho_f) theta_d
=rho_c theta_c+(1+w_f)rho_f theta_f.
```

Definujeme

```text
r=rho_f/rho_c,
beta=(1+w_f)rho_f/[rho_c+(1+w_f)rho_f]
    =delta r/(1+delta r),
theta_d=(1-beta)theta_c+beta theta_f.
```

Hustotne vážený smer bez faktorov `rho+p` by nebol celkovým energy-frame štvorvektorom a predstavoval by inú koľaj.

### 4.2 Kovariantný prenos a Eulerove rovnice

```text
Q_f^mu=-Gamma rho_f u_d^mu,
Q_c^mu=+Gamma rho_f u_d^mu.
```

Z všeobecných rovníc (19)–(20) Clemson et al. sme odvodili

```text
theta_c'+mathcal H theta_c-k^2 Psi
=a Gamma(rho_f/rho_c)(theta_d-theta_c),

theta_f'-2 mathcal H theta_f-k^2 delta_f/(1+w_f)-k^2 Psi
=a Gamma/(1+w_f)(2theta_f-theta_d).
```

Toto K4 rozšírenie je naše odvodenie z primárnych všeobecných rovníc; zdroj ho netabuluje ako osobitný model.

### 4.3 Symbolická lokálna brána

V homogénnom veľkoškálovom rýchlostnom bloku platí

```text
d/dt [V_c,V_f]^T |_interaction
=Gamma M(r)[V_c,V_f]^T,

M=[[-r beta,             r beta],
   [-(1-beta)/delta, (2-beta)/delta]].
```

Skript 27 odvodil

```text
det M=-r^2/(1+delta r)<0
```

pre každé `r>0`, `delta>0`. Matica preto má jeden kladný a jeden záporný reálny eigenvalue. Spoločný vektor `[1,1]` nie je jej eigenvektor, takže kladný mód obsahuje nenulové `V_f-V_c` a nie je čistým gauge boostom. Všetkých 12 symbolických kontrol prešlo.

## 5. Plný prvý superhorizontový test K4

### 5.1 Premenné a Einsteinov constraint

Skript 30 integroval hustoty a rýchlosti CDM, paliva, baryónov a perfektnej radiácie spolu s `Phi`. Použil

```text
x=ln a,
q=k/H0,
u_A=H0 V_A,
E=H/H0,
Psi=Phi.
```

Z `0i` constraintu:

```text
d Phi/dx=-Phi+(3a/2E)
 [X_c u_c+delta X_f u_f+X_b u_b+(4/3)X_r u_r].
```

Kontrolovaný `00` constraint bol

```text
q^2 Phi+3(aE)^2(Phi_x+Phi)
+(3/2)a^2[X_c delta_c+X_f delta_f+X_b delta_b+X_r delta_r]=0.
```

### 5.2 Integrovaný systém K4

```text
delta_c,x=-q^2 u_c/(aE)+3 Phi_x
 +(lambda/E)r(delta_f-delta_c+Phi),

u_c,x=-u_c+Phi/(aE)
 +(lambda/E)r beta(u_f-u_c),

delta_f,x=-3(1-w_f)delta_f-delta q^2 u_f/(aE)
 -9aE(1-w_f^2)u_f+3delta Phi_x
 -(lambda/E)Phi-3a lambda(1-w_f)u_f,

u_f,x=2u_f+(delta_f/delta+Phi)/(aE)
 +(lambda/E delta)[(2-beta)u_f-(1-beta)u_c],

delta_b,x=-q^2 u_b/(aE)+3Phi_x,
u_b,x=-u_b+Phi/(aE),

delta_r,x=-(4/3)q^2u_r/(aE)+4Phi_x,
u_r,x=(delta_r/4+Phi)/(aE).
```

### 5.3 Fyzikálny počiatočný mód

Počiatočná podmienka pri `z_star=1089.9` bola velocity-isocurvature reprezentácia

```text
u_f-u_c=1,
X_c u_c+delta X_f u_f=0,
u_b=u_r=0,
delta_A=Phi=0.
```

Celková tmavosektorová hybnosť je nulová a `00` aj `0i` constraint sú splnené. Rozdiel `u_f-u_c` je gauge-invariantný. Jednotková amplitúda je iba normalizácia lineárneho módu; všetky perturbácie sa môžu lineárne preškálovať.

### 5.4 Výsledok

Jemný beh `q=1e-5`, krok `6.25e-5`:

```text
K4: |Delta u_0/Delta u_star|=1.5873084655,
Gamma=0: |Delta u_0/Delta u_star|=1.4693472258e-5,
K4/Gamma=0=108028.1391,
ln(K4/Gamma=0)=11.5901470.
```

Výsledok `delta_f=0.1149` pre jednotkovú počiatočnú rýchlosť nie je predikovaná kozmická amplitúda; dokumentuje prenos lineárne normalizovaného módu.

Numerické brány:

| Brána | Výsledok | Prah | Stav |
|---|---:|---:|---|
| kroková konvergencia log-rastu | `8.68094e-8` | `<1e-7` | PASS |
| zmena pri `q:1e-5 -> 5e-6` | `6.28286e-11` | `<1e-7` | PASS |
| globálne relatívne `00` rezíduum | `3.01385e-10` | `<1e-5` | PASS |
| interakčný rast | `11.5901` e-fold | `>1` e-fold = stena | KILL |

### 5.5 Prečo je to fyzikálna stena

Zdravý `Gamma=0` systém tento relatívny velocity-isocurvature mód potlačí približne o päť rádov. K4 ho namiesto toho zachová a zosilní voči zdravej limite faktorom `1.08028e5`. Bez mikrofyziky počiatočných podmienok by bolo nutné rastúci mód ručne potlačiť; to je predregistrovaná stena Q20.7.

### 5.6 Verdikt K4

**A2-K4 je MŔTVA — ARCHIVOVANÁ (M-011).**

## 6. Rozsah rozsudkov

K3 a K4 zomreli iba v kombinácii:

- constant-`w_f>-1` efektívna tekutina;
- `c_s,f^2=1`;
- `Gamma=lambda H0>0`, `lambda=0.15`;
- skalár prenosu `Gamma rho_f`;
- príslušný smer `u_f` alebo entalpický `u_d`;
- absencia mikrofyzikálneho zákona, ktorý by odstránil alebo zakázal rastúci mód.

Nezomreli:

- A1-K1 ako backgroundové účtovníctvo;
- A2-K5 s prenosom odvodeným z lokálnej akcie alebo mediátora;
- nová koľaj s časovo závislým `Gamma`, ak je fyzikálne odvodená a predregistrovaná;
- mikrofyzika, ktorá odstráni pól `1/(1+w_f)` a určí zdravé počiatočné módy.

## 7. Reprodukčné artefakty

- `scripts/25_script_A2_K3_superhorizon_velocity_instability.py`;
- `scripts/26_script_A2_K3_equation_sign_and_null_limit_audit.py`;
- `scripts/27_script_A2_K4_equation_sign_null_and_eigenvalue_audit.py`;
- `scripts/28_script_A2_K4_full_superhorizon_relative_mode.py` — zachovaný serializačný neúspech;
- `scripts/29_script_A2_K4_full_superhorizon_relative_mode_serialized.py` — zachovaný konvergenčne neuzavretý beh;
- `scripts/30_script_A2_K4_full_superhorizon_relative_mode_converged.py` — finálny beh;
- oba príslušné errata v adresári `scripts`.

## 8. Primárne zdroje

- [Clemson et al., Interacting Dark Energy — constraints and degeneracies](https://arxiv.org/abs/1109.6234): všeobecné rovnice (19)–(20), K3 rovnice (36)–(38) a referenčný prah (41).
- [Malik a Wands, Adiabatic and entropy perturbations with interacting fluids and fields](https://arxiv.org/abs/astro-ph/0411703): gauge-invariantné relatívne perturbácie interagujúcich tekutín.
- [Ma a Bertschinger, Cosmological Perturbation Theory](https://arxiv.org/abs/astro-ph/9506072): štandardné tekutiny a Einsteinove constrainty.

