# A2-K1 až A2-K5 — retrospektívny audit maximálnej hĺbky, rovníc, výpočtov a rozsudkov

**Dátum:** 2026-07-13  
**Rozsah:** iba A2-K1, A2-K2, A2-K3, A2-K4 a A2-K5  
**Zásada:** historické rozsudky, skripty a výstupy sa nemažú

## 1. Výsledok

| Koľaj | Max. hĺbka po audite | Rovnice/výpočet | Rozsudok po audite | Zastavenie pri prvom zlom výsledku |
|---|---:|---|---|---|
| A2-K1 | `45/100` | parita potvrdená | `MŔTVA M-009` v presnom fluidnom rozsahu | oprávnené; publikovaný modelový prah bol prekročený |
| A2-K2 | `25/100` | parita potvrdená | `MŔTVA M-008` v striktne barotropickom rozsahu | oprávnené; high-k hlavný symbol je fatálny |
| A2-K3 | `45/100` | parita potvrdená | `MŔTVA M-010` v presnom fluidnom rozsahu | oprávnené; publikovaný modelový prah bol prekročený |
| A2-K4 | `50/100` | rovnice a čísla platia | **`M-011 POZASTAVENÁ; K4 ZNOVU OTVORENÁ NA K4.1`** | **neoprávnené; porovnával sa absolútny mód s rýchlo zanikajúcou referenciou** |
| A2-K5 | `75/100` | parita potvrdená | `MŔTVA M-012` pre konkrétnu konformnú akciu | oprávnené; pokračovalo sa cez všetky A2 brány až po CMB-kotvený screen |

Maximálna hĺbka je najhlbší skutočne vykonaný test, nie pravdepodobnosť
pravdivosti ani odmena za priaznivý výsledok. Preto sa pri K4 nemení
`50/100`, hoci sa mení stav rozsudku.

## 2. Audit stupnice

Pre K1–K5 sa používa táto jemná interpretácia už existujúcej stupnice:

| Hĺbka | Dokázaný rozsah |
|---:|---|
| `25/100` | background/ledger alebo rozhodujúci lokálny hlavnosymbolový test |
| `45/100` | úplné fluidné rovnice, mapovanie znamienok, nulový limit a analytický vedúci mód; nie plná constraintová integrácia |
| `50/100` | integrovaný superhorizontový systém s Einsteinovými constraintmi |
| `60/100` | odvodený efektívny rast alebo úplné `G_ij` |
| `75/100` | CMB-normalizovaná rastová brána bez tvrdenia plnej vlastnej likelihood |
| `80+/100` | vlastný Boltzmannov systém a likelihood |

Tým je vysvetlené, prečo K1/K3 zostávajú na 45, K4 na 50 a K5 na 75.

## 3. A2-K1 — parita potvrdená

Presné mapovanie na Clemson et al. je

```text
Gamma_ref=-Gamma_cell,
1+w_f=delta>0,
Q_c^mu=+Gamma_cell rho_f u_c^mu.
```

Vedúci veľkoškálový pomer k nulovej väzbe je

```text
d ln R/dt=2 Gamma_cell/delta,
N_K1=2(lambda/delta) H0 Delta t=12.2131073973,
R=exp(N_K1)=201411.9108.
```

Skript 24 znovu prešiel `8/8` znamienkovými a nulovými kontrolami. Skript
23 reprodukoval čísla s krokovou odchýlkou `9.1895e-9 < 1e-8`.

Rozsudok sa neopiera iba o nový interný pomer: rovnaká trieda
`Q proportional rho_x`, rovnaké dva transferové rámce a prah nestability sú
analyzované plnou Boltzmannovou implementáciou v
[Clemson et al.](https://arxiv.org/abs/1109.6234). Registrovaný pomer
`lambda/delta=6.5303` prekračuje ich rádový prah 1 pre tento rámec.

**Rozsah smrti:** iba constant-`Gamma`, constant-`w_f>-1`,
`c_s,f^2=1`, `Q^mu parallel u_c` efektívna fluidná uzávera. Nezabíja
background A1 ani inú akciu.

## 4. A2-K2 — parita potvrdená

Striktne barotropická definícia dáva

```text
c_s,f^2=dp_f/d rho_f=w_f=-0.97703<0,
delta_f''+c_s,f^2 k^2 delta_f approximately 0.
```

Rastová miera je `mu=|c_s|k` a rastie bez obmedzenia s `k` v deklarovanej
fluidnej teórii. Už pri `k=0.01 h/Mpc` skript 21 znovu dal
`mu/H0=29.6329`. Algebraický prenos bez kladného člena rádu `k^2` nemení
hlavný symbol.

Toto je skutočná gradientová nestabilita, nie iba nepriaznivý fit. Hlbšie
kozmologické fitovanie by fyzickú chybu neopravilo. Hĺbka `25/100` je preto
relevantná: koľaj zomrela na skorom, ale rozhodujúcom lokálnom teste.

**Rozsah smrti:** iba striktne barotropická uzávera. Skalárne pole s
`w<0`, ale `c_s^2>0`, nie je týmto výsledkom zabité.

## 5. A2-K3 — parita potvrdená

Po presnom mapovaní znamienka platí

```text
Q_c^mu=+Gamma rho_f u_f^mu,
d ln R/dt=Gamma/delta,
N_K3=(lambda/delta)H0 Delta t=6.1065536987,
R=448.7893835.
```

Skript 26 znovu prešiel `10/10` kontrolami a skript 25 reprodukoval krokovú
konvergenciu `9.1895e-9`. Pomer `lambda/delta=6.5303` prekračuje publikovaný
rádový prah 2 pre `Q parallel u_f` v tej istej fluidnej triede.

K3 sa nezastavila iba pre ľubovoľné interné skóre. Zastavila sa na známej
rýchlostnej nestabilite presne zvoleného fenomenologického modelu. Preto
zostáva `MŔTVA M-010`, ale iba v uvedenom rozsahu.

## 6. A2-K4 — rovnice platia, rozsudok bol príliš prísny

### 6.1 Čo zostáva správne

Entalpicky vážený energy-frame a odvodená interakčná matica sú konzistentné.
Skript 27 znovu prešiel `12/12` kontrolami a platí

```text
det M=-r^2/(1+delta r)<0.
```

Skript 30 je konvergentná a constraintovo kontrolovaná integrácia. Jeho
uložené čísla sú reprodukovateľné.

### 6.2 Kde vznikla interpretačná chyba

Skript 30 dal pre normalizovaný velocity-isocurvature mód

```text
T_K4=|Delta u_0/Delta u_star|=1.5873084655,
ln T_K4=0.4620397929,
T_0=1.4693472258e-5,
T_K4/T_0=108028.1391,
ln(T_K4/T_0)=11.5901470198.
```

Historický kill test použil posledné číslo ako „viac než jeden e-fold
nestability“. To je pomer k referenčnému módu, ktorý sám klesol približne o
päť rádov. Absolútny mód vzrástol iba faktorom 1.587, teda **menej než `e`**.

Kladný eigenvalue samotného interakčného podbloku tiež nie je automaticky
kladným globálnym Lyapunovovým exponentom celej časovo závislej sústavy s
Hubbleovými, hustotnými a Einsteinovými členmi.

### 6.3 Doplnený adiabatický test

Skript 63 pridal regular constrained common-clock/common-velocity mód s
`Delta u_star=0`. Skript 64 ho zjemnil bez zmeny rovníc alebo prahov.

Na jemnom behu:

```text
max |Delta u|/|u_common,star| = 1.43903e-6,
global relative 00 residual  = 5.42109e-12,
step difference              = 2.24352e-7  (PASS),
k difference                 = 1.13550e-6  (tesne FAIL pri prahu 1e-6).
```

Tento výsledok nie je zelený prechod, pretože `k` konvergencia tesne
neprešla. Zároveň neposkytuje dôkaz explózie: mód je o viac než šesť rádov
pod hranou `e`.

### 6.4 Opravený stav

`M-011` sa nemaže, ale **pozastavuje sa ako príliš široký rozsudok**.
A2-K4 sa znovu otvára iba na K4.1. Nevyhlasuje sa za životaschopnú.
Maximálna hĺbka zostáva `50/100`.

## 7. A2-K5 — hĺbka a rozsudok potvrdené

K5/K1 nezomrela pri prvom červenom náznaku. Prešla:

1. akčnou a backgroundovou rekonštrukciou;
2. ghostovou, gradientovou a backgroundovou hmotnostnou bránou;
3. rovnicami, znamienkami a nulovým limitom;
4. relatívnym aj regulárnym adiabatickým superhorizontovým testom;
5. kvázistatickým `G_eff` a rastom;
6. CMB-kotveným konzervatívnym rastovým screenom.

Reprodukcia dala

```text
weighted growth ratio=1.051963--1.053053,
S8_hybrid=0.983642--1.006266,
S8_screen=0.863.
```

Nezávislá aritmetická kontrola `A_s,req=A_s(0.863/S8)^2` znovu vyžaduje
pokles `A_s` o `23.0255--26.4477 %`. Skript 45 poctivo nie je plný vlastný
Boltzmann/likelihood systém; preto hĺbka nie je 80, ale 75. Veľkosť a povinné
kladné znamienko sily pri fixovaných parametroch však oprávňujú zachovať
predregistrovaný screeningový rozsudok M-012.

Neskoršie taxonomické erratum určuje, že historická `K5/K3a` je kanonicky
A2-K6, nie živá dcéra K5. A2-K5 preto označuje konkrétnu konformnú akciu a
M-012 sa na ňu môže vzťahovať bez zabitia všetkých možných akcií.

## 8. Odpoveď na otázku „nezastal si pri prvom zlom výsledku?“

- **K1:** áno, ďalšie interné stupne sa nevykonali, ale stena bola presným
  publikovaným no-go regiónom tej istej fluidnej triedy; zastavenie ostáva.
- **K2:** áno, ale high-k gradientová nestabilita je terminálna; zastavenie
  ostáva.
- **K3:** áno, ale presný publikovaný rýchlostný prah bol prekročený;
  zastavenie ostáva.
- **K4:** **áno a bolo to priskoro**; relatívny zisk voči zanikajúcej
  referencii bol zamenený za absolútnu explóziu.
- **K5:** nie; koľaj bola dotiahnutá až po CMB-normalizovanú rastovú bránu.

## 9. Povinná K4.1 brána pred návratom k ďalšej koľaji

1. začať hlboko v radiačnej ére, nie iba pri rekombinácii;
2. zostaviť úplnú bázu constraintovo prípustných adiabatických a
   izokurvatúrnych módov;
3. integrovať fundamentálnu maticu a určiť najväčší absolútny transfer alebo
   globálny rastový exponent celej sústavy;
4. osobitne hlásiť absolútny transfer, transfer nulovej referencie a ich
   pomer;
5. smrť vyhlásiť až pri divergencii, strate linearity alebo observačne
   neprípustnom transfere z regulárnych módov, nie iba preto, že nulová
   referencia silno zaniká;
6. ak K4.1 prejde, pokračovať high-k a plným Boltzmannovým testom; ak zlyhá,
   znovu potvrdiť M-011 s novým presným dôvodom.

## 10. Dôkazy

- `scripts/21_script_A2_barotropic_fuel_gradient_instability.py`
- `scripts/23_script_A2_K1_superhorizon_velocity_instability_converged.py`
- `scripts/24_script_A2_K1_equation_sign_and_null_limit_audit.py`
- `scripts/25_script_A2_K3_superhorizon_velocity_instability.py`
- `scripts/26_script_A2_K3_equation_sign_and_null_limit_audit.py`
- `scripts/27_script_A2_K4_equation_sign_null_and_eigenvalue_audit.py`
- `scripts/30_script_A2_K4_full_superhorizon_relative_mode_converged.py`
- `scripts/63_script_A2_K1_K5_retrospective_depth_equation_verdict_audit.py`
- `scripts/64_script_A2_K4_retrospective_adiabatic_convergence.py`
- `scripts/32--46` pre K5/K1 podľa manifestov K5.0, K5.1 a A3

Primárne metodické opory: [Clemson et al.](https://arxiv.org/abs/1109.6234),
[Malik a Wands](https://arxiv.org/abs/astro-ph/0411703) a
[Ma a Bertschinger](https://arxiv.org/abs/astro-ph/9506072).

