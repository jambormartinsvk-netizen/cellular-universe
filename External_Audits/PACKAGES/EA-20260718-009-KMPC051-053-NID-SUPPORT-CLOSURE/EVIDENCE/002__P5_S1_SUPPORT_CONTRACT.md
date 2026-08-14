# A2-K4/P5.3g7 — kontrakt vetvy S1 a prenosu supportu

**Dátum:** 2026-07-16  
**Stav:** `S_C0_LOWER_MOMENT_PASSPORT_PASS / S_M_AND_FULL_HIERARCHY_OPEN`  
**Cesta:** `A1-K1 → A2-K4 → P5 → P5.3g7`  
**K4:** `LIVE / 60/100`  
**P5:** `3.5/6`  
**Skóre a release:** bez zmeny; `NO_NEW_TRIGGER`  
**Účel:** zabrániť preneseniu úzkeho výsledku
`AD/k=0.05/nominal` na inú paru, mód alebo support bez vlastného dôkazu.

## 1. Čo je a nie je uzavreté

KMPC-031 uzavrel iba minimálny `J4` support pre podmienený
`Phi1 M3-TCA0 AD/k=0.05/nominal` sentinel na plochách `z=1e-4` a `z=1e-2`.
Neuzavrel fyzický pôvod pary, CDI/BI/NID/NIV, iné `k`, nulové varianty,
finite opacity, P5.4 ani G8. Raw full-state rozdiely z KMPC-030 zostávajú
zmiešanou diagnostikou spoločného driftu a pridaného tailu, nie čistým
support gate.

Z tohto dôvodu sa po úspešnom pokuse 10 **nevytvára pokus 11 ARCH-A**.
Ďalšie výpočty budú samostatné fyzikálne coverage atómy nad uzavretou
architektúrou. Ak by vyžadovali zmenu rovníc alebo architektúry solve, musí
pred nimi vzniknúť nový delta-audit; technická oprava sama osebe nevytvára
novú fyzikálnu koľaj.

## 2. Dve rozdielne vetvy S1

`P5-S1` v tomto dokumente znamená už vytvorenú, decouplovanú, bezhmotnú
voľne letiacu paru. Nie je to `G8 SCREEN-S1` ani rovnomenný Q22A
backgroundový budget. V conditional rozsahu je jej priamy zdroj nulový,
`w_s=1/3`, `rho_s>=0`, `rho_s∝a^-4` a nesie celú collisionless hierarchiu;
nesmie sa potichu zmeniť na perfektnú tekutinu so `sigma_s=0`.

### S-C0 — podmienené rozdelenie spoločného collisionless sektora

Táto vetva odpovedá iba na otázku: „Ak už para v skorom limite sleduje
rovnaký collisionless mód ako neutrína, dá sa spoločný sektor rozdeliť bez
zmeny metriky a constraintov?“ Nie je to odvodenie vzniku alebo korelácie
pary.

Nech `alpha=0.2271`, `N_nu=3.046`, `N_s=0.0535` a
`W=1+alpha(N_nu+N_s)`. Už zmrazené váhy sú

```text
R_gamma = 1/W                  = 0.5868901247...
R_nu    = alpha N_nu/W         = 0.4059792483...
R_s     = alpha N_s/W          = 0.0071306270...
R_fs    = R_nu+R_s             = 0.4131098753...
```

`Delta N_eff=0.0535` je tu prevzatá okrajová podmienka, nie nové odvodenie.
Pre každý normalizovaný moment spoločného sektora
`Y_fs` — hustotu, rýchlosť, shear a každý zahrnutý vyšší multipól — platí

```text
Y_nu = Y_s = Y_fs,
R_nu Y_nu + R_s Y_s = R_fs Y_fs.
```

Druhá rovnica musí vyjsť ako presná algebraická nula v konvencii konkrétnej
stavovej premennej. Para sa teda nepridáva na vrch pôvodného neutrínového
seedu. Pôvodný **celkový** collisionless sektor sa nahradí dvoma váženými
časťami. Pri NID/NIV sa kompenzácia a normalizácia musia formulovať s
`R_fs`, nie so samotným `R_nu`.

S-C0 zámerne nastavuje interné neutríno–para entropy a relative-velocity
módy na nulu. Ich nenulové hodnoty by boli nové primordiálne módy a potrebujú
samostatný fyzikálny pôvod; nesmú vzniknúť ako technická oprava seedu.
Plne species-resolved báza preto obsahuje aj interný hustotný a rýchlostný
`nu-s` mód; päť kolektívnych S-C0 módov sa nesmie označiť za úplnú
sedemmódovú bázu.

Povinný S-C0 vektor pre každý z `AD, CDI, BI, NID, NIV` obsahuje najmenej

```text
(delta_s, U_s, sigma_s, F_s,3 ... F_s,lmax)
```

v presne rovnakej normalizácii ako neutrínový vektor. Nestačí kontrola
`R_nu+R_s=R_fs`; musí sa overiť vážená kancelácia každého použitého momentu,
celkovej energie, hybnosti a anisotropného stresu.

**Dovolený výsledok S-C0:** iba `PASS_CONDITIONAL_EMBEDDING` alebo
`REVIEW/STOP_IMPLEMENTATION`. S-C0 nikdy nezvyšuje fyzikálne skóre a
nepotvrdzuje, že bunková para naozaj vzniká s touto koreláciou.

### S-M — mikrofyzikálne odvodená para

S-M je fyzická vetva. Musí vychádzať z jedného lokálneho zdroja alebo
produkčného/collision kernelu pre delenie buniek. Nestačí zvoliť hotový seed
podľa želaného CMB výsledku.

Pred fyzikálnym P5.3 PASS musí S-M určiť alebo odvodiť:

1. nultý moment zdroja: produkciu energie pary a jej párovanie s palivom a
   popolom;
2. prvý moment: prenos hybnosti a znamienka v Eulerových rovniciach;
3. druhý a vyššie momenty: tlak, shear, disperziu/šum a po decouplingu
   hierarchiu;
4. čas produkcie, thermalizácie a decouplingu;
5. koreláciu s AD/CDI/BI/NID/NIV alebo dôvod vzniku nového módu;
6. presné total-energy a total-momentum identity vrátane nulového limitu;
7. nezápornú hustotu, regulárny superhorizontový limit, kauzalitu a
   kompatibilitu s už zmrazeným `Delta N_eff=0.0535` bez nového tichého fitu.

Súčasný A1 ledger nepovoľuje významný perzistentný neskorý priamy parný
kanál: už auditovaný budget prežije iba pri zanedbateľnom
`f_R,direct<~3.2e-5`. S-M preto nesmie potichu doplniť neskorú produkciu do
P5-S1. Aktuálne nevyvrátený koridor je skorý ukončený relikt a neskorý
takmer čistý `F→C`; jeho mikrofyzika však stále nie je odvodená.

Q18/Q22 preto zostávajú otvoreným rodičom S-M. Kým tieto body nie sú
uzavreté, S-C0 smie preverovať matematickú existenciu seedu, ale nie fyzickú
predikciu pary.

## 3. Passport prenosu supportu

Výsledok `J4` z AD sa nesmie kopírovať na ostatné módy. Každý mód má vlastný
vedúci rád a vlastné coefficient okno z dokumentov 27 a 32.

| mód | vedúci `h_x` rád | primary → extended support | fractional `leading_j` | background `m_max` | stav |
|---|---:|---|---:|---:|---|
| AD | 2 | `[0,2] → [0,4]` | 2 | 2 | `J4 PASS`, iba sentinel scope |
| CDI | 1 | `[0,1] → [0,3]` | 1 | 1 | NOT RUN |
| BI | 1 | `[0,1] → [0,3]` | 1 | 1 | NOT RUN |
| NID | 3 | `[0,3] → [0,5]` | 0 | 3 | NOT RUN |
| NIV | 2 | `[-1,2] → [-1,4]` | -1 | 3 | NOT RUN |

Tieto páry sú už zmrazené v `full_ra_m3_seed.py` a
`mode_resolved_puiseux.py`; nový runner ich nesmie znovu vyberať. Z AD sa
prenáša iba metóda porovnania primary/extended supportu, nie koeficienty,
`J4` ani jeho PASS verdict. Najmä NID sa nesmie nahradiť univerzálnym J4
testom.

Čistý added-tail gate musí porovnávať výlučne nové powers nad spoločným
supportom. Raw rozdiel dvoch nezávislých solve sa zachová ako diagnostika,
ale nesmie prebiť čistý tail ani byť spätne premenovaný na PASS. Každý atóm
musí navyše prejsť vlastnou hodnosťou, driver rezíduami, nezávislými `00/0i`
holdoutmi, forbidden-order guardom, `U_c` regularitou a S-C0 momentovou
kanceláciou.

## 4. Konečný coverage plán

### C1 — fail-fast módová brána pri `k=0.05`, nominal

Poradie zostáva podľa už zmrazeného registra:

```text
CDI → BI → NID → NIV
```

Každý mód je samostatne auditovateľný atóm. Technická chyba atóm nezabíja a
započíta sa do technického limitu iba v príslušnej implementačnej vetve.
Fyzikálny STOP môže vzniknúť iba z reprodukovaného invariantného rozporu,
nie zo syntaxe, timeoutu, serializácie alebo zlej tolerancie.

### C2 — Fourierova brána

Iba ak C1 prejde, preveria sa pre všetkých päť módov

```text
k = 0.005 a 0.15 Mpc^-1, nominal.
```

Na rovnakých fyzických `a` plochách musia `D,H,rho_f,rho_ash` zostať medzi
módmi a `k` rovnaké do relatívne `1e-12`. Tým sa testuje, že perturbatívny
mód znovu nepresiakol do backgroundu.

### C3 — nulové varianty

Posledná seedová coverage vrstva je kartézsky súčin piatich módov, troch `k`
a variantov `nominal,gamma0,af0`, spolu 45 atómov vrátane už existujúceho
sentinelu. Každý nominal atóm musí mať vlastný `gamma→0` a `A_f→0` bridge.
Agregovaný conditional verdikt je dovolený až pri `45/45`; partial výsledky
sa zachovajú, ale neextrapolujú.

## 5. Rozhodovacie mantinely

| Nález | Autoritatívny význam |
|---|---|
| S-C0 vážené momenty nie sú nulové | STOP implementácie splitu; nie smrť fyzickej S-M pary |
| mód potrebuje väčší support | REVIEW; pred behom zapísať odvodený `J_min`, potom prepočítať |
| invariantný nenulový `00/0i` holdout po úplnom supporte | kandidát na fyzikálny STOP daného M3 módu, vyžaduje nezávislú reprodukciu |
| background závisí od `k` alebo módu | fyzikálny STOP použitej background mapy |
| syntax, timeout, hash, CLI alebo serializácia | iba technická chyba; zachovať dôvod a pokračovať do limitu 10 |
| C1/C2/C3 prejdú iba so S-C0 | conditional matematický PASS bez skóre |
| S-M odvodí iný seed než S-C0 | nová fyzická vstupná vetva; conditional výsledky sa na ňu nekopírujú |

## 6. Bezprostredný ďalší krok

Pred ďalším Python procesom vznikne samostatná predregistrácia prvého C1
atómu. Musí obsahovať:

- presný CDI vektor vrátane S-C0 váženého rozdelenia;
- algebraicky odvodený `J_min(CDI)` a porovnanie s `J_min+2`;
- nemenné prahy z dokumentu 27;
- očakávaný rozsah, PASS/REVIEW/STOP a ďalší krok ľudskou rečou;
- vnútorný limit najviac `5 s` a vonkajší limit najviac `10 s` pre každý
  samostatný Python proces.

Kým táto CDI predregistrácia a coefficient-level S-C0 lift/collapse passport
neprejdú formula-provenance kontrolou, stav je
`S_C_FORMULA_FROZEN / COEFFICIENT_PASSPORT_NOT_RUN`. P5.4, G8, G9 a CLASS
adapter zostávajú blokované.

## 7. Neskorší autoritatívny výsledok

KMPC-032 zastal technicky na PF-069 bez fyzikálneho výsledku. Úzky
KMPC-033 RERUN1 prešiel a hlavný audítor udelil iba
`PASS_S_C0_LOWER_MOMENT_COEFFICIENT_LIFT_COLLAPSE_PASSPORT_ONLY` v
dokumente 56. Tento výsledok nemení S-M, full hierarchy ani blokovanie
P5.4/G8/G9/CLASS.

## 8. Neskorší coverage stav

KMPC-040 neskôr uzavrel CDI support `[0,5]` voči `[0,7]` iba pre
`.05/nominal`. KMPC-041 dokázal nedostatočnosť BI `[0,1]`; KMPC-042 potom
dokázal nedostatočnosť BI `[0,3]`, pričom core/common ostali stabilné.
KMPC-043 uzavrel BI order-7 lower/structural provenance, ale 5 driver a jeden
holdout zostali na precision boundary. KMPC-044 túto hranicu na tej istej
BI matici uzavrel jedinou korekciou aj 80-dps QR. KMPC-045 skončil PF-074
bez fyzikálneho payloadu; owner-only KMPC-046 následne uzavrel BI support
`[0,5]` voči `[0,7]` iba `.05/nominal`. Najbližší krok je NID primary
`[0,3]` voči extended `[0,5]`, leading `j=0`; NIV, C2/C3, S-M a full
hierarchy ostávajú NOT_RUN/open.
