# A2.1 — lineárne perturbácie, Einsteinove constrainty a prvý superhorizontový test

**Dátum:** 2026-07-13  
**Testovaná koľaj:** A2-K1  
**Výsledný stav:** **MŔTVA — ARCHIVOVANÁ**  
**Rozsah:** konštantné `Gamma>0`, `w_f=-1+delta>-1`, `c_s,f^2=1`, `Q_f^mu=-Gamma rho_f u_c^mu`

## 1. Konvencie

Používame konformný Newtonov gauge:

```text
ds^2 = a^2 [-(1+2 Psi)d eta^2 + (1-2 Phi) delta_ij dx^i dx^j].
```

- `eta` je konformný čas;
- čiarka znamená `d/d eta`;
- `mathcal H=a'/a`;
- Fourierova konvencia má priestorové derivácie `nabla^2 -> -k^2`;
- `delta_A=delta rho_A/bar rho_A`;
- `theta_A=-k^2 v_A` v Newtonovej gauge;
- `w_f=-1+delta`, `delta=0.02297`;
- fyzikálna pokojová zvuková rýchlosť aktívnej koľaje je `c_s,f^2=1`;
- adiabatic sound speed pri konštantnom `w_f` je `c_a,f^2=w_f`.

Potenciál `Psi` je časový/Newtonov potenciál a `Phi` priestorová krivostná perturbácia.

## 2. Mapovanie znamienka na primárny formalizmus

Primárne rovnice [Clemson et al.](https://arxiv.org/abs/1109.6234) definujú

```text
Q_x = Gamma_ref rho_x,
Gamma_ref > 0: CDM -> dark energy.
```

Naša koľaj má opačný tok:

```text
palivo -> CDM,
Q_f = -Gamma rho_f,
Q_c = +Gamma rho_f,
Gamma > 0.
```

Presné mapovanie je preto

```text
x -> f,
Gamma_ref = -Gamma,
1+w_f = delta > 0.
```

Skript 24 symbolicky overil znamienka v rovniciach kontinuity CDM, kontinuity paliva, Eulerovej rovnici paliva, superhorizontovej miere, nulových limitách a backgroundovej bilancii.

## 3. Background v konformnom čase

```text
bar rho_f' + 3 mathcal H (1+w_f) bar rho_f = -a Gamma bar rho_f,
bar rho_c' + 3 mathcal H bar rho_c = +a Gamma bar rho_f.
```

Baryóny nemajú bunkový zdroj. Súčet paliva a CDM má nulový interakčný zdroj.

## 4. Úplné nové lineárne rovnice A2-K1

### 4.1 CDM/popol

Kontinuita:

```text
delta_c' + theta_c - 3 Phi'
= a Gamma (bar rho_f/bar rho_c) (delta_f - delta_c + Psi).
```

Euler:

```text
theta_c' + mathcal H theta_c - k^2 Psi = 0.
```

Eulerova rovnica má štandardný tvar, pretože `Q^mu` je rovnobežné s `u_c^mu`. Kontinuita štandardná nie je.

### 4.2 Palivo

Kontinuita:

```text
delta_f'
+ 3 mathcal H (1-w_f) delta_f
+ (1+w_f) theta_f
+ 9 mathcal H^2 (1-w_f^2) theta_f/k^2
- 3(1+w_f) Phi'
= -a Gamma [Psi + 3 mathcal H (1-w_f) theta_f/k^2].
```

Euler:

```text
theta_f'
- 2 mathcal H theta_f
- k^2 delta_f/(1+w_f)
- k^2 Psi
= a Gamma/(1+w_f) (2 theta_f - theta_c).
```

Nebezpečný faktor `Gamma/(1+w_f)=Gamma/delta` nie je numerická voľba. Vyplýva z hybnostnej rovnice tekutiny, ktorej inerciálna hustota je `rho_f+p_f=delta rho_f`.

### 4.3 Palivová tlaková porucha

Všeobecný prevod z pokojového rámca pri `c_s,f^2=1`, `c_a,f^2=w_f` dáva

```text
delta p_f
= delta rho_f
+ (1-w_f)[3 mathcal H(1+w_f)+a Gamma]
  bar rho_f theta_f/k^2.
```

Tento neadiabatický člen je už zahrnutý v rovniciach vyššie. Zápis `delta p_f=delta rho_f` mimo pokojového rámca by bol nesprávny.

## 5. Neinteragujúce a štandardné sektory

Nový bunkový prenos nemení štandardné rovnice baryónov, fotónov a neutrín. Pre baryóny a prvé fotónové momenty:

```text
delta_b' = -theta_b + 3 Phi',

theta_b' = -mathcal H theta_b + c_s,b^2 k^2 delta_b + k^2 Psi
           + (4 bar rho_gamma/3 bar rho_b) a n_e sigma_T
             (theta_gamma-theta_b),

delta_gamma' = -(4/3)theta_gamma + 4 Phi',

theta_gamma' = k^2(delta_gamma/4 - sigma_gamma) + k^2 Psi
               + a n_e sigma_T(theta_b-theta_gamma).
```

Pre voľne prúdiacu bezhmotnú zložku `X` (štandardné neutrína alebo už vytvorená decouplovaná para):

```text
delta_X' = -(4/3)theta_X + 4 Phi',
theta_X' = k^2(delta_X/4 - sigma_X) + k^2 Psi.
```

Vyššie multipóly `sigma_X, F_X,ell` a fotónová polarizácia pokračujú štandardnou Boltzmannovou hierarchiou Ma–Bertschinger. A2.1 úplne špecifikuje **všetky nové interakčné členy**; nekopíruje celú štandardnú nekonečnú hierarchiu, ktorá sa musí prevziať bez zmeny v A3.

## 6. Einsteinove constrainty

Celkové zdroje:

```text
delta rho = sum_A bar rho_A delta_A,
delta p = sum_A delta p_A,
(bar rho+bar p) theta = sum_A (bar rho_A+bar p_A) theta_A,
(bar rho+bar p) sigma = sum_A (bar rho_A+bar p_A) sigma_A.
```

Rovnice v našej konvencii sú:

### 00 constraint

```text
k^2 Phi + 3 mathcal H(Phi' + mathcal H Psi)
= -4 pi G a^2 delta rho.
```

### 0i constraint

```text
k^2(Phi' + mathcal H Psi)
= 4 pi G a^2 (bar rho+bar p) theta.
```

### stopová priestorová rovnica

```text
Phi'' + mathcal H(Psi' + 2 Phi')
+ (2 mathcal H' + mathcal H^2)Psi
+ (k^2/3)(Phi-Psi)
= 4 pi G a^2 delta p.
```

### bezstopová priestorová rovnica

```text
k^2(Phi-Psi)
= 12 pi G a^2 (bar rho+bar p) sigma.
```

Znamienka boli skontrolované proti primárnym rovniciam 23a–23d v [Ma a Bertschinger](https://arxiv.org/abs/astro-ph/9506072).

## 7. Nulový limit

Pri `Gamma->0`:

- pravá strana kontinuity CDM zmizne;
- obe interakčné pravé strany paliva zmiznú;
- zostane štandardná constant-`w`, `c_s^2=1` tekutina;
- Eulerova rovnica CDM zostane štandardná;
- Einsteinove constrainty sa nemenia.

Skript 24 overil algebraický nulový limit pre všetky nové interakčné členy.

## 8. Prvý superhorizontový test

Definujeme konečný veľkoškálový rýchlostný potenciál

`V_A=theta_A/k^2`.

Eulerove rovnice v limite `k->0` obsahujú:

```text
V_c' + mathcal H V_c - Psi = 0,

V_f' - 2 mathcal H V_f - delta_f/(1+w_f) - Psi
= a Gamma/(1+w_f)(2V_f-V_c).
```

Relatívna rýchlosť `V_f-V_c` je gauge-invariantná. Vedúci homogénny rýchlostný mód A2-K1 má voči neinteragujúcej tekutine pomer `R`, pre ktorý

```text
d ln R/dt = 2 Gamma/(1+w_f) = 2 Gamma/delta,

R(t_2)/R(t_1) = exp[2 Gamma(t_2-t_1)/delta].
```

Keďže `Gamma>0` a `delta>0`, mód rastie dopredu v čase. Primárna analýza rovnakého efektívneho modelu potvrdila tento rýchlostný mód aj plnou perturbačnou integráciou; v jej znamienkach ide o nestabilný kvadrant `Gamma_ref<0`, `w>-1`.

### 8.1 Bezrozmerná miera

```text
Gamma/[H0(1+w_f)] = lambda/delta
= 0.15/0.02297
= 6.5302568568.
```

Referenčná podmienka, pri ktorej sa nestabilita stane kozmologicky významnou pre `Q^mu parallel u_c^mu`, je rádovo väčšia než 1. Model ju prekračuje faktorom približne 6.53.

## 9. Numerický výpočet na A1-K1 backgrounde

Skript 23 použil presne background skriptu 13 a spočítal

```text
H0 Delta t(z_star -> 0) = 0.9351169231,
N_inst = 2(lambda/delta) H0 Delta t = 12.2131073973,
R(z=0)/R(z_star) = exp(N_inst) = 201411.91.
```

Konvergenčná kontrola:

| Krok | Exponent |
|---:|---:|
| `5e-4` | `12.2131075096` |
| `2.5e-4` | `12.2131073973` |

Relatívny rozdiel `9.1895e-9` prešiel prahom `1e-8`.

Skript 22 s hrubšími krokmi zostáva zachovaný: fyzikálne kontroly prešli, ale konvergenčný rozdiel `3.6759e-8` nesplnil prah. Skript 23 je jeho zdokumentovaný nástupca.

## 10. Verdikt

A2-K1 narazila na predregistrovanú stenu:

> nekontrolovaný rastúci superhorizontový relatívny rýchlostný mód v oblasti parametrov vyžadovanej teóriou.

Stav je preto:

**A2-K1 MŔTVA — ARCHIVOVANÁ.**

Smrť je spôsobená kombináciou:

- smeru energie palivo -> CDM;
- `Q^mu parallel u_c^mu`;
- konštantného `Gamma>0`;
- `w_f>-1` veľmi blízkeho `-1`;
- efektívnej fluidnej uzávery `c_s,f^2=1`.

## 11. Čo verdikt nezabíja

- A1-K1 ako matematicky konzistentné backgroundové účtovníctvo;
- A2-K3 s prenosom rovnobežným s `u_f^mu`, kým neprejde vlastným testom;
- A2-K4 so smerom celkovej tmavosektorovej rýchlosti;
- A2-K5 s prenosom odvodeným z akcie/mediátora;
- inú časovú závislosť `Gamma`, ak ide o novú koľaj a nie post-data úpravu;
- inú mikrofyziku, ktorá odstráni nebezpečný pól `1/(1+w_f)` a má zdravú kinetickú maticu.

## 12. Podmienka novej koľaje

A2-K1 sa nesmie oživiť menším krokom, inou gauge alebo zmenou počiatočnej amplitúdy. Nová koľaj musí zmeniť konkrétnu fyziku, ktorá vytvorila rastový mód, a obsahovať sekciu `Rozdiel oproti A2-K1`.

## 13. Reprodukčné artefakty

- `scripts/22_script_A2_K1_superhorizon_velocity_instability.py` — prvý, konvergenčne neuzavretý beh;
- `scripts/23_script_A2_K1_superhorizon_velocity_instability_converged.py` — finálny konvergentný beh;
- `scripts/24_script_A2_K1_equation_sign_and_null_limit_audit.py` — symbolická kontrola znamienok;
- `scripts/ERRATUM_22_23_A2_K1_SUPERHORIZON.md`;
- `scripts/README_AUDIT_SCRIPTS_22-24.md`.

## 14. Primárne zdroje

- [Clemson et al., Interacting Dark Energy — constraints and degeneracies](https://arxiv.org/abs/1109.6234): rovnaká trieda `Q proportional rho_x`, oba smery štvorvektora, úplné lineárne rovnice a rýchlostná nestabilita.
- [Malik a Wands, Adiabatic and entropy perturbations with interacting fluids and fields](https://arxiv.org/abs/astro-ph/0411703): gauge-invariantný viac-tekutinový formalizmus.
- [Ma a Bertschinger, Cosmological Perturbation Theory](https://arxiv.org/abs/astro-ph/9506072): Einsteinove constrainty a štandardné druhy častíc.
- [Valiviita, Majerotto a Maartens](https://arxiv.org/abs/0804.0232): nezávislé varovanie, že jednoduchý constant-`w` interagujúci background môže mať fatálne poruchy. Ich konkrétny skalár prenosu nie je použitý ako dôkaz znamienka A2-K1.

