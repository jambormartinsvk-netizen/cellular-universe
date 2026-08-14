# A2-K5/K3a.0 — akčná, backgroundová a stabilitná brána

**Dátum:** 2026-07-13  
**Stav:** `PREŽÍVA K3a.0 — 40/100; G_eff A RAST EŠTE NEOVERENÉ`  
**Dôležité:** skóre je zrelosť dôkazového balíka, nie pravdepodobnosť pravdy

## 1. Kritérium piatej sily

Piata sila nie je vopred zakázaná. Ak ju tok energie a jedna lokálna akcia
vynútia, musí zostať v rovniciach. Nová koľaj však nesmie byť úplne závislá
od neodôvodnenej piatej sily ani ju rušiť nezávislým post-data členom.

K3a preto ponecháva energický člen, ktorý vyžaduje A1, a pridáva z tej istej
kovariantnej akcie samostatne auditovateľný prenos hybnosti.

## 2. Konkrétna akcia K3a

V konvenciách Kaseho a Tsujikawu volíme

```text
S = integral sqrt(-g) [Mpl^2 R/2 + G2(phi,X)] + S_Schutz-Sorkin + integral sqrt(-g) f,
G2 = X - V(phi),
f = -f1(phi) rho_c(n_c) + eta Z^2,
Z = u_c^mu partial_mu phi.
```

Efektívna hustota popola je

```text
rho_c_hat = (1+f1) rho_c.
```

Trieda `f=-f1 rho_c+f2` je dôležitá, pretože
`partial^2 f/partial n_c^2=0`, a teda nevytvára neprípustný tlakový mód CDM.
Primárne odvodenie všeobecnej triedy a stabilitných koeficientov je v
[Kase & Tsujikawa 2020](https://arxiv.org/abs/2005.13809). Práca zároveň
ukazuje, že `Z`-závislý momentum transfer môže v zdravých podtriedach viesť
k `G_eff,c<G`. Energy+momentum precedens je aj v
[Amendola & Tsujikawa 2020](https://arxiv.org/abs/2003.02686).

## 3. Presná reprodukcia A1 backgroundu

Pre `f2=eta Z^2` platí na homogénnom backgrounde

```text
rho_f = (1+2 eta) dot(phi)^2/2 + V,
P_f   = (1+2 eta) dot(phi)^2/2 - V.
```

Preto sa z registrovaného `w_f=-1+delta` rekonštruuje

```text
(1+2 eta) dot(phi)^2 = delta rho_f,
V = (1-w_f) rho_f/2,
d ln(1+f1)/dt = Gamma rho_f/rho_c_hat.
```

Posledná rovnica je presne A1 tok
`dot(rho_c_hat)+3H rho_c_hat=Gamma rho_f`. Momentum člen nemení túto
rovnicu, ale mení kinetiku a Eulerovu rovnicu.

Numerické maximálne absolútne rezíduá na jemnom kroku:

```text
rho_f reconstruction      = 2.22045e-16
P_f reconstruction        = 2.22045e-16
energy-transfer identity  = 2.77556e-17
```

## 4. Vysokofrekvenčná stabilita

Pre zvolenú akciu dávajú presné koeficienty

```text
q_s/(2 Mpl^2) = 1+2 eta,
hat(c_s)^2    = 1/(1+2 eta),
c_CDM^2       = 0,
q_c/A         = 1 + 2 eta dot(phi)^2/rho_c_hat.
```

Pre `eta>=0`, `A=1+f1>0` sú teda bez ducha skalár aj CDM, skalár nemá
gradientovú nestabilitu a CDM zostáva bez tlaku.

| `eta` | `Delta varphi` | `q_s/(2Mpl^2)` | `hat(c_s)^2` | `(q_c/A)_0` | stav |
|---:|---:|---:|---:|---:|---|
| 0.0 | 0.210335 | 1.0 | 1.000000 | 1.000000 | prešla; nulový limit K5/K1 |
| 0.1 | 0.192009 | 1.2 | 0.833333 | 1.008247 | prešla |
| 0.5 | 0.148730 | 2.0 | 0.500000 | 1.024740 | prešla |
| 1.0 | 0.121437 | 3.0 | 0.333333 | 1.032986 | prešla |
| 2.0 | 0.094065 | 5.0 | 0.200000 | 1.039584 | prešla |
| 5.0 | 0.063419 | 11.0 | 0.090909 | 1.044982 | prešla |

Najväčší relatívny rozdiel medzi krokmi `5e-4` a `2.5e-4` bol
`1.519e-8`. Pri rekombinácii vyšlo vo všetkých prípadoch
`A=0.9100125633>0`.

## 5. Čo táto brána nedokázala

Jednoduchý literárny vzťah

```text
G_cc = G/(1+r_f2) < G
```

platí pre čistý momentum model `f1=0`. K3a potrebuje súčasne `f1 != 0`, aby
reprodukovala A1. Preto by bolo chybou preniesť tento vzťah bez odvodenia.
K3a.0 nepotvrdzuje správne `S8`, plné perturbácie ani mikrofyzický pôvod
`eta`.

Navyše pomalšie pole pri rastúcom `eta` zväčšuje deriváciu
`d ln(1+f1)/d phi`. Momentum transfer teda musí prejsť skutočnou spoločnou
rastovou rovnicou; nestačí slovné tvrdenie, že „trenie vyhrá“.

## 6. Povinná nasledujúca brána K3a.1

1. odvodiť úplné lineárne rovnice pre súčasné `f1(phi)` a `eta Z^2`;
2. overiť dva nulové limity: `eta->0` dá K5/K1 a `f1->0` dá čistý momentum
   model z literatúry;
3. vypočítať `q_c`, `beta_nc`, ich časové derivácie a presné
   `G_cc`, `G_cb`, `G_bc`, `G_bb` na backgrounde A1;
4. použiť už zapísaný grid `eta={0,0.1,0.5,1,2,5}` bez výberu optima podľa
   pozorovaného `S8`;
5. zabiť koľaj, ak zdravý interval neobsahuje `G_eff,c<=G`, vznikne pól,
   silná väzba alebo je potrebné rušenie dvoch nezávisle doladených členov;
6. ak prežije, až potom implementovať úplný Boltzmannov systém.

Parameter `eta` je zatiaľ lešenie. Pred tvrdením o predikcii ho musí odvodiť
mikrofyzika bunkovej siete alebo musí byť verejne priznaný ako nový parameter.

## 7. Dôkaz

Výpočet a presné vstupy sú v
`scripts/47_script_A2_K5_K3a_action_background_stability_gate.py`.
