# A2-K6 — MŔTVA M-013: presné Gij a spojitý eta no-go

**Dátum:** 2026-07-13  
**Kanonická koľaj:** A2-K6  
**Historický alias:** `K5/K3a`  
**Konečný stav:** `MŔTVA M-013`  
**Skóre pred smrťou:** K6.0 mala `40/100`; skóre sa po kill bráne
neaktualizuje na „nižšiu pravdepodobnosť“, ale nahrádza rozsudkom smrti

## 1. Auditovaná hypotéza

Koľaj používala jednu kovariantnú energy+momentum akciu v konvenciách
Kaseho a Tsujikawu:

```text
G2=X-V(phi),
f=-f1(phi) rho_c + eta Z^2,
Z=u_c^mu partial_mu phi,
A=1+f1,
rho_c_hat=A rho_c.
```

Člen `f1` mal presne reprodukovať už auditovaný A1 tok energie. Člen
`eta Z^2` mal pridať zdravý prenos hybnosti a oslabiť rast bez ručného
vymazania akciou vynútenej sily. Primárne všeobecné odvodenie je
[Kase & Tsujikawa, arXiv:2005.13809](https://arxiv.org/abs/2005.13809),
najmä rovnice (5.17)–(5.24).

## 2. Čo K6.0 skutočne dokázala

Predchádzajúci dokument
`Audit/A2_K5_K3a_0_akcna_backgroundova_stabilitna_brana.md` zostáva
historicky platný iba v tomto rozsahu:

- akcia presne reprodukuje A1 background;
- `f_,n_c n_c=0`, takže nevytvára tlakový mód popola;
- pre predregistrované `eta>=0` sú `q_s>0`, `q_c>0` a gradientový
  koeficient kladný.

Formulácia `PREŽÍVA K3a.0 — 40/100; G_eff otvorené` bola správna v čase
vzniku, ale rozsudok M-013 ju odteraz obmedzuje: backgroundová a high-k
kinetická stabilita neznamenala prijateľnú gravitačnú odozvu.

## 3. Nutné mapovanie hustotnej konvencie

V zdrojovom článku násobí publikované `G_cc` holú Schutzovu hustotu
`rho_c`. Background A1 však používa fyzickú hustotu
`rho_c_hat=A rho_c`. Preto sú fyzikálne väzby

```text
mu_cc = G_cc/(A G),
mu_cb = G_cb/G,
mu_bc = G_bc/(A G),
mu_bb = G_bb/G.
```

Pre auditovanú akciu potom

```text
mu_cc=(1+r1/A)/(1+r2),
mu_cb=1/(1+r2),
mu_bc=mu_bb=1.
```

Bez faktora `1/A` by sa miešala zmena definície zdrojovej hustoty so
zmenou gravitácie. Toto mapovanie je odteraz záväzná metodická kontrola.

## 4. Presné koeficienty perturbácií

Pre `x=ln(a)` a

```text
s=d ln A/dx,
t=1+2 eta,
r=t-1=2 eta,
d=delta rho_f/rho_c_hat,
P0=3 delta X_f/E^2,
B=1+eps_H+eps_Delta2-eps_Delta3
```

sa všeobecné výrazy redukujú bez numerického odčítania na

```text
q_c=A[1+(r/t)d],
beta_nc=1-A,
r2=r d,
r1/A=(2s/P0)[s(1+r)+r d(s+d ln(d)/dx-B)].
```

Gauge-ready CDM kontinuita a Eulerova rovnica použité ako zdroj redukcie sú

```text
dot(delta_cN)+3 dot(Phi)+(k^2/a^2)v_cN=0,

dot(v_cN)+H eps_qc v_cN
 -(1-beta_nc)Psi/q_c
 +(1-beta_nc-q_c)dot(delta_phi_N)/(q_c dotphi)
 -H[(1-beta_nc-q_c)eps_phi+q_c eps_qc]
    delta_phi_N/(q_c dotphi)=0.
```

Po Einsteinových constraintoch v presnom subhorizontovom QS limite vzniká

```text
ddot(delta_c)+c1 H dot(delta_c)
 -4 pi G[mu_cc rho_c_hat delta_c+mu_cb rho_b delta_b]=0,

ddot(delta_b)+2H dot(delta_b)
 -4 pi G[rho_c_hat delta_c+rho_b delta_b]=0.
```

Tieto rovnice zachovávajú povinnú piatu silu aj modifikované trenie. Úplný
Boltzmannov systém sa po zlyhaní nutnej high-k podmienky nespúšťal: nemôže
zmeniť asymptotickú QS vetu tej istej akcie na `mu_cc<=1`.

## 5. Dva nulové limity

### `eta->0`

```text
q_c=A,
mu_cc=1+2(d ln A/dvarphi)^2,
mu_cb=mu_bc=mu_bb=1.
```

Maximálne rezíduum nezávislých tvarov bolo `1.776e-15`. Limit presne
reprodukuje mŕtvu konformnú K5, ako musí.

### `f1->0`

```text
r1=0,
mu_cc=mu_cb=1/(1+r2),
mu_bc=mu_bb=1.
```

Maximálne rezíduum oproti čistému momentum modelu bolo `2.220e-16`.

## 6. Výsledok grida a spojitého intervalu

Na predregistrovanom gride `eta={0,0.1,0.5,1,2,5}` rástla dnešná
`mu_cc` takto:

```text
5.674662, 7.222625, 13.122551, 19.899770, 31.774623, 57.965432.
```

Nejde o prehliadnutý interval medzi bodmi. Pri `z=0` sa výraz dá zapísať

```text
mu_cc(r)=(n0+r n1)/(1+r d),  r=2 eta>=0.
```

Derivácia má konštantné kladné znamienko
`n1-d n0=7.816408230`, pričom

```text
mu_cc(0)=5.674661891,
lim_{eta->infinity} mu_cc=163.646709760.
```

Preto `mu_cc(z=0)>1` pre celý spojitý fyzikálny interval `eta>=0`.
Relatívna kroková chyba endpointu bola `1.552e-8`.

## 7. Fyzikálna príčina smrti

Momentum člen naozaj dá `mu_cb<1`. Súčasne však znižuje kinetickú rýchlosť
poľa podľa

```text
dotphi^2 proportional 1/(1+2 eta).
```

A1 tok `s=d ln A/dx` je pevný. Preto musí skalárny náboj

```text
d ln A/dphi = s/(d phi/dx)
```

rásť ako `sqrt(1+2 eta)`. Príťažlivá piata sila rastie rýchlejšie než
momentum faktor `1/(1+r2)` stíha tlmiť. Diagnostický rast od `z=100` sa pri
`eta=5` zvýšil na `2.160409` násobku K5 limitu namiesto požadovaného
poklesu.

## 8. Rozsudok a jeho presný rozsah

**A2-K6 je MŔTVA M-013.** Zlyhala predregistrovanú nutnú podmienku
`G_eff,c<=G` bez pólu, silnej väzby alebo dodatočného rušenia.

Rozsudok nezabíja všetok prenos hybnosti ani všetky piate sily. Zabíja
konkrétnu rodinu
`f=-f1(phi)rho_c+eta Z^2` s A1 tokom, kanonickým `G2=X-V` a `eta>=0`.
Zmena znamienka na `eta<0` nie je záchrana tej istej zdravej koľaje: smeruje
k `q_s=1+2eta<=0`, zhoršuje gradientové rezervy a nebola súčasťou
predregistrovaného zdravého intervalu.

## 9. Obmedzenie prvého numerického výstupu

`scripts/48_script_A2_K6_1_exact_Gij_and_growth_gate.py` v prvom behu
vytlačil pri nulových limitoch `FAIL`, hoci samotná odchýlka bola iba
`5.225e-7`. Príčinou bola numerická derivácia `eps_qc` na okraji a príliš
tvrdá hranica `2e-8`, nie fyzikálny nesúlad.

Následný skript 49 použil analytickú deriváciu a cancellation-free tvar;
oba limity prešli na `1.776e-15` a `2.220e-16`. Starý skript ani jeho
výstup sa nemažú. Jeho machine-label je týmto obmedzený; tabuľkové hodnoty
`mu_cc` sa zmenili iba na siedmom desatinnom mieste a rozsudok M-013 sa
zosilnil.

## 10. Zachované dôkazy

- `scripts/47_script_A2_K5_K3a_action_background_stability_gate.py` — K6.0;
- `scripts/48_script_A2_K6_1_exact_Gij_and_growth_gate.py` — prvý grid a
  rastový test;
- `scripts/49_script_A2_K6_1_continuous_eta_no_go.py` — analytické nulové
  limity, spojitá veta a konvergencia;
- `Audit/A2_K6_1_NUMERICAL_OUTPUT_M013.md` — rozhodujúci výstup v MD.

