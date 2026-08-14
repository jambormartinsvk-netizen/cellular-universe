# A2-K4/P5.3g7-S-C0 — coefficient-level lift/collapse passport

**Dátum:** 2026-07-16  
**Stav pred behom:** `PREREGISTERED / NOT_RUN`  
**Run ID:** `KMPC-032`  
**Budúci runner:** `scripts/276_script_KMPC_032_P5_3g7_s_c_coefficient_passport.py`  
**Budúci výsledok:**
`scripts/results/k_mpc_005/RUN_KMPC_032_P5_3G7_S_C_COEFFICIENT_PASSPORT.json`  
**Vlastník:** `A1-K1 → A2-K4 → P5 → P5.3g7 → S-C0`  
**Skóre/hĺbka:** bez zmeny; K4 `LIVE / 60/100`, P5 `3.5/6`

## 1. Čo sa bude počítať ľudskou rečou

Súčasný M3 solver používa jeden spoločný collisionless druh `fs`. Passport
ho nerozšíri o nové neznáme a nebude riešiť ODE ani maticu seedu. Pre každý
použitý koeficient vytvorí iba explicitný pohľad

```text
fs → (nu, steam) → fs.
```

V podmienenej vetve S-C0 majú neutríno aj para rovnaký normalizovaný
koeficient. Ich vážený súčet musí presne vrátiť pôvodný spoločný
koeficient. Kontrola sa vykoná osobitne pre hustotu, rýchlosť v registrovanej
`U` konvencii a shear. Aktuálny M3 contract nemá päťmódové koeficienty
`F_l>=3`; preto sa pri nich overí iba všeobecná lineárna operatorová identita,
nie coefficient passport. Tým sa overí, že para nebola pridaná druhýkrát a
že lower-moment split nemení zdroje Einsteinových rovníc.

## 2. Zmrazené fyzikálne predpoklady

Tento beh smie používať iba už zvolenú conditional hypotézu:

- `P5-S1` je po produkcii decouplovaná bezhmotná collisionless para;
- `w_s=1/3`, `rho_s>=0`, po decouplingu `rho_s∝a^-4`;
- v S-C0 je `Q_s^mu=0` a nevzniká nový priamy K4 zdroj;
- interné `nu-steam` density/velocity módy sú podmienene nulové, nie
  fyzikálne zakázané;
- `Delta N_eff=0.0535` je vstupná okrajová hodnota, nie výsledok behu.

Presné racionálne váhy sa zostavia z

```text
alpha = 2271/10000,
N_nu  = 1523/500,
N_s   = 107/2000,
W     = 1 + alpha (N_nu+N_s),
R_gamma=1/W, R_nu=alpha N_nu/W, R_s=alpha N_s/W,
R_fs=R_nu+R_s.
```

Float reprezentácia sa smie exportovať iba ako pomocná informácia; PASS
rozhodujú presné SymPy rational nuly.

## 3. Nezávislý contract a explicitný view

Pred prvým Python procesom vzniknú dva oddelené base moduly:

1. `s1_collective_contract.py` — autoritatívne módy, primary/extended
   supporty, momenty, combined-state/driver/holdout contract a spoločný
   validator;
2. `s_c0_coefficient_passport.py` — implementácia lift/collapse a
   negatívnych fixtures, ktorá contract iba importuje.

Autoritatívny 13-state M3 solver sa nemení. Explicitný `nu+s` lower-moment
vektor je iba
auditný view; nesmie sa použiť ako nový independent solve, pretože bez
mikrofyziky S-M by obsahoval dve interné nulové smery.

Zmrazené support páry sú:

| mód | primary | extended | `leading_j` |
|---|---|---|---:|
| AD | `[0,2]` | `[0,4]` | 2 |
| CDI | `[0,1]` | `[0,3]` | 1 |
| BI | `[0,1]` | `[0,3]` | 1 |
| NID | `[0,3]` | `[0,5]` | 0 |
| NIV | `[-1,2]` | `[-1,4]` | -1 |

Tieto hodnoty sa načítajú z nezávislého contractu a fail-closed porovnajú s
`full_ra_m3_seed.py` a `mode_resolved_puiseux.py`. AD `J4` verdict sa
neprenesie na iný mód.

## 4. Presné identity

Pre každý mód sa načíta skutočný anchored M1 coefficient set pri
`k=0.05 Mpc^-1`, nominal. Pre každý jeho prítomný integer coefficient a
každý deklarovaný fractional slot extended supportu v momentoch
`delta`, `U`, `sigma` musí platiť

```text
Y_nu = Y_s = Y_fs,
R_nu Y_nu + R_s Y_s - R_fs Y_fs = 0,
Y_nu-Y_s = 0,
collapse(lift(Y_fs))-Y_fs = 0.
```

Osobitne sa overia názvové/normalizačné mosty:

```text
density source:   R_nu delta_nu + R_s delta_s = R_fs delta_fs,
momentum source:  R_nu U_nu     + R_s U_s     = R_fs U_fs,
shear source:     R_nu sigma_nu + R_s sigma_s = R_fs sigma_fs.
```

Rovnaká lineárna collisionless kontinuita, Euler a shear sa vyhodnotia aj
na skutočných M1 coefficient dictionaries a musia byť pre `nu`, `s` a `fs`
rovnaké po jednotlivých mocninách. Rekurencia pre `l=3,4` musí komutovať s
weighted collapse iba ako presná symbolická operatorová identita. Vyššie
multipóly nemajú v tomto chaine päťmódový coefficient source; výsledok musí
exportovať `HIGHER_MULTIPOLE_COEFFICIENTS_NOT_IN_SCOPE` a nejde o G8
`lmax` alebo closure test.

NID a NIV dostanú aj presné ochrany proti starej skratke:

```text
NID: R_gamma delta_gamma + R_fs delta_fs = 0,
NIV: R_gamma U_gamma     + R_fs U_fs     = 0.
```

Variant s `R_nu` namiesto `R_fs` musí byť negatívnym fixture odmietnutý.

## 5. Povinné negatívne fixtures

Rovnaká produkčná validačná cesta musí odmietnuť najmenej:

1. chýbajúci mód;
2. univerzálny AD/J4 support vložený NID;
3. chýbajúci `sigma` moment;
4. `Einstein_00` vložený medzi drivers;
5. `Y_s != Y_nu` pri S-C0 lifte;
6. NID kompenzáciu s `R_nu` namiesto `R_fs`;
7. NIV kompenzáciu s `R_nu` namiesto `R_fs`;
8. nenulový direct `Q_s`;
9. float-only kontrolu samotného `R_nu+R_s=R_fs` bez coefficient liftu;
10. priamy prenos script-84 `q` do P5 `U` bez dokumentovaného konverzného
    mosta.

Fixture PASS znamená, že chybný kandidát bol odmietnutý. Žiadny fixture
nesmie používať inú validačnú funkciu než produkčný kandidát.

## 6. Predbehové očakávania

| Kontrola | Očakávanie | Ak neprejde |
|---|---|---|
| frozen source/hash/schema | presná zhoda | technický STOP balíka; opraviť bez fyzikálneho verdictu |
| exact radiation weights | kladné, súčet presne 1 | STOP S-C0 implementácie |
| coefficient lift/collapse | všetky exact residuals `0` | STOP S-C0 implementácie, nie K4/S-M |
| internal difference `D_l` | presne `0` | STOP S-C0 implementácie |
| density/momentum/shear | exact weighted residuals `0` | STOP S-C0 implementácie |
| M1 `fs` rows po lifte | coefficient dictionaries pre `nu,s,fs` zhodné | STOP lower-moment S-C0 implementácie |
| hierarchy operator commute | exact residuals `0`; coefficient scope explicitne NOT IN SCOPE | STOP operator mapy, nie full hierarchy verdict |
| collective `R_s→0` | presná obnova combined `fs` | STOP S-C0 implementácie |
| 10 negatívnych fixtures | všetky odmietnuté | technický/formulačný REVIEW; žiadny ďalší runner |
| runtime | interný `<=4.8 s`, každý proces external `<=10 s` | technická chyba; active counter +1 |

Očakávaný substantive výsledok je

```text
PASS_S_C0_LOWER_MOMENT_COEFFICIENT_LIFT_COLLAPSE_PASSPORT_ONLY
```

Jeho úspech vynuluje active technical counter na `0/10`, pretože prinesie
nový interpretovateľný čiastkový výsledok. Compile, `--help` a smoke ho
nevynulujú.

## 7. Nonclaims a ďalší postup

PASS nedokazuje fyzický vznik pary S-M, úplnú sedemmódovú bázu, amplitúdy
interných módov, päťmódové `F_l>=3` coefficients, finite opacity, ODE,
G8/G9, BBN/CMB, CLASS, S8/H0 ani release trigger. Nezvyšuje hĺbku ani P5
score.

- Pri PASS sa zapíše immutable JSON a výsledkový audit; potom sa predregistruje
  prvý CDI primary/extended coverage atóm s `leading_j=1`.
- Pri formulačnom zlyhaní sa zastaví iba S-C0 split. S-M a K4 neumierajú.
- Pri technickom zlyhaní sa zachová presná príčina, active counter sa zvýši
  o 1 a opraví sa rovnaký fyzický rozsah.

## 8. Prevádzkový sled

Každý Python proces bude samostatný a vopred uvedený v execution ledgeri:

1. `py_compile` contract modulu;
2. `py_compile` implementačného modulu;
3. `py_compile` runnera;
4. `--help`;
5. `--smoke` bez výsledkového JSON;
6. `--audit --output ...`.

Pred prvým procesom sa do tohto dokumentu doplnia SHA-256 oboch modulov a
runnera. Žiadny príkaz sa nebude spájať s ďalším Python procesom.

## 9. Zmrazené zdroje pred prvým Python procesom

| Súbor | SHA-256 |
|---|---|
| `s1_collective_contract.py` | `F535EE15137BBD6F9C0379821C9CC94DED8EC56037B6105B75BEF65A5884EE68` |
| `s_c0_coefficient_passport.py` | `C370B610815AFAC345C990E3CFE516D616873F39598F468A5ADBF2C65A2A6B95` |
| `276_script_KMPC_032_P5_3g7_s_c0_coefficient_passport.py` | `B6D108C2B2292E7D83B1C9251665C3C7B4C55D3C16C341D1545F946DC2FBC76E` |

Hashe boli získané iba read-only PowerShell príkazom. Runner navyše
fail-closed zmrazil priamo importované zdroje `full_ra_contract.py`,
`full_ra_m3_seed.py`, `mode_resolved_puiseux.py` a M1-anchored overlay.
Prvý `python` proces je týmto dokumentačne povolený.

## 10. Historický outcome

KMPC-032 skončil PF-069 technickou chybou pred prvou fyzikálnou identitou.
Failure JSON SHA je `51C7B32B...1EA03`. Predregistrácia sa spätne nemení;
autoritatívny úzky nástupca KMPC-033 a jeho scoped PASS sú v dokumentoch
54–56. Výsledok nemení skóre ani hĺbku.
