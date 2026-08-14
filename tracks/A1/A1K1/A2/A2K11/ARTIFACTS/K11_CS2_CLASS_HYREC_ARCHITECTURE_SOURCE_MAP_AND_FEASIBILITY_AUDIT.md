# K11-CS2 — zdrojová mapa CLASS/HyRec a audit realizovateľnosti full v002

**Dátum:** 2026-07-16  
**Koľaj:** `A1-K1 -> A2-K11 -> K11-R -> K11-CS2`  
**Rozsah:** iba read-only architektúra zdrojov; bez Python behu a bez fyzikálneho skóre  
**Autoritatívny verdict:** `BACKEND_FEASIBLE_SOURCE_INJECTION_POINTS_FOUND / FULL_V002_NOT_IMPLEMENTED`  
**Fyzikálny stav:** naďalej `REVIEW_BLOCKED_IMPLEMENTATION`, hĺbka `10/100 = G1`  
**Release stav:** `LICENSE_PROVENANCE_UNRESOLVED_FOR_REDISTRIBUTION`

## 1. Ľudskou rečou

CLASS vie vypočítať rekombináciu aj fotónovo-baryónovú fyziku s naším
zmeneným rozpínaním, pretože HyRec dostáva aktuálne `H(z)` priamo z
backgroundu CLASS. Nemusíme teda meniť atómovú fyziku iba preto, že sa
zmení expanzia.

Nie je však správne iba zapnúť existujúci CLASS fluid a CDM. Štandardný
CLASS ich samostatne zachováva, kým A1 vyžaduje spoločný transfer
`fuel -> ash`. Aj ich poruchy a regulárne počiatočné módy preto potrebujú
nové rovnice. Navyše CLASS zapisuje polarizáciu v inom stave než náš
CAMB-E auditný register. Natívny počet stavov CLASS preto nesmie byť
porovnaný s číslom 41 bez presnej transformačnej mapy.

Výsledok tohto auditu je konštrukčný: našli sme konkrétne miesta, kde sa
dá full v002 implementovať. Nie je to dôkaz, že fyzický model prejde.

## 2. Pripnutý zdroj a reprodukovateľnosť

```text
repository: external/CLASS
origin: https://github.com/lesgourg/class_public.git
commit: e85808324f51fc694d12e3ed7439552a3c3f9540
source status: clean; jediný untracked artefakt je class.exe
HyRec declaration: HYREC_VERSION "2020"
```

| Súbor | SHA-256 |
|---|---|
| `external/CLASS/README.md` | `1CE30F841FD5CAFA284C62F1B4A6C83D9F5C629FBF175B70E2D5C407C5686A98` |
| `source/background.c` | `1F4B028671944487F0EC8956AAA1B4CA7F87190C2CF1B1A60943AB91CB0739F6` |
| `source/thermodynamics.c` | `320F93C39A6EE429ED42106CBC54E421EE23BB1D32F96F73DEA450A4A056169D` |
| `source/perturbations.c` | `17848792FB6AFE61D76C623513518536481AE139E1453DCAF82169EC20614E5B` |
| `include/background.h` | `11A00132957F2DBFA86FE69395C117246D334CCD0BD55E97230EB6FE16FC9A1F` |
| `include/perturbations.h` | `667082A54979270378354F44137846B81FEAAE34368763E525E9146A129D3975` |
| `external/HyRec2020/wrap_hyrec.c` | `A73F0076774AFD84A69CAE30DC60EA15E46FE2B369CC6D02EB1D4304F82B4D86` |
| `external/HyRec2020/history.h` | `C8EA3B70494A5E1E4556E1F8CD6E90D53A203D2DAB91F31B760FB8159DCA8657` |
| `external/HyRec2020/README.md` | `BE889220DC4065FEA86B454624D19E667C40869899E662A510B16ACE085A2C24` |
| lokálny `class.exe` | `BE62910540B57FE47C5964C6DF3EC73B79CE3164AAE354608DDD0BF095ECD7A3` |

V checkout-e nebol nájdený jednoznačný `LICENSE`, `COPYING` ani
`COPYRIGHT` súbor. Lokálne čítanie zdroja a audit tým nie sú fyzikálne
zablokované. Kopírovanie alebo zverejnenie upraveného zdrojového stromu je
však fail-closed, kým nebude licencia doložená z autoritatívneho zdroja.

## 3. Exact-A1 background — povinná zmena

Štandardný CDM je v `background_functions()` približne na riadkoch
`437–443` natvrdo analytický `a^-3`. Existujúci `fld` má v
`background_derivs()` približne na `2658–2660` samostatnú conservation
rovnicu bez transferu. Preto ich nemožno iba premenovať na popol a palivo.

Full v002 potrebuje samostatné integrované stavy a indexy pre
`rho_fuel` a `rho_ash` s rovnicami

```text
d rho_fuel/d ln a = -3 delta rho_fuel -(Gamma/H) rho_fuel,
d rho_ash /d ln a = -3 rho_ash +(Gamma/H) rho_fuel.
```

Povinné zásahy sú:

- `background.h`: vstupné parametre, `index_bg_rho_fuel/ash` a
  `index_bi_rho_fuel/ash`;
- `background_indices()` (`background.c`, približne `963–1188`): presná
  parita registrovaných stavov a výstupov;
- `background_functions()` (`371–610`): tlak paliva, ash v hmote a obe
  zložky v celkovej energii;
- `background_initial_conditions()` (`2131–2257`): spätná integrácia alebo
  fail-closed shooting z dnešných `Omega_fuel0, Omega_ash0`; dve oddelené
  power-law počiatočné podmienky nie sú exact A1;
- `background_derivs()` (`2589–2670`): obe previazané rovnice a správny
  transferový člen v `p_tot_prime`;
- matter/growth a výstupné registre: popol musí byť v `Omega_m`, palivo nie.

Background nesmie prijať perturbatívne `k` ani historické `K_MPC`. Musí
prejsť nulovým limitom `lambda=0`, celkovou energy cancellation a
nezávislým A1 ODE cross-checkom.

## 4. HyRec a thermal history

`thermodynamics_derivs()` volá `background_at_z()` a na približne
`2585–2603` vytvára aktuálne `H(z)`. Na približne `2671–2684` sa toto `H`
odovzdáva priamo `hyrec_dx_H_dz()` a `hyrec_dx_He_dz()`. HyRec wrapper teda
nepoužíva skrytý samostatný Lambda-CDM Hubbleov zákon.

To umožňuje exact-A1 recombination adaptér bez zmeny atómovej mikrofyziky,
ak fuel/ash interakcia:

- neohrieva baryóny ani fotóny;
- nemení `T_gamma proportional a^-1` ani základné konštanty;
- nepridáva ionizačný zdroj.

Ak delenie buniek odovzdáva plazme teplo alebo vytvára interagujúcu paru,
štandardný HyRec už nie je úplný a full v002 zostane REVIEW.

Povinné thermal kontroly sú `x_e`, `T_b`, `c_b^2`, `dkappa`, visibility,
recombination a drag epoch. `FULL_K11` a `DRAG_NULL_K1` musia mať bitovo
rovnakú background/thermal tabuľku; `COMMON_NULL` ju musí prepočítať.
Reionizačné vstupy musia byť spoločné a explicitné. SWIFT/HyRec citlivosť
na zmenený background a `YHe` sa overí osobitným nulovým testom.

## 5. Stavový register: CAMB kontrakt nie je natívny CLASS vektor

Náš auditný stav pri `L=8` má presne `4L+9=41` zložiek a fotónovú
polarizáciu `E_gamma_2...E_gamma_L`. CLASS však v
`perturbations_vector_init()` (`3817–4032`, polarizácia približne
`3902–3909`) registruje `pol0_g, pol1_g, pol2_g, ...`. Analogický natívny
post-TCA CLASS vektor by preto mal 43 stavov, nie 41. Jeho veľkosť sa navyše
mení pri TCA/RSA/UFA prepínačoch.

Z toho vyplýva:

1. `CLASS pt_size == 41` je zakázaný gate;
2. `pol0_g/pol1_g` nie sú chybné CAMB `E_gamma_0/E_gamma_1` z PF-062;
3. 25/33/41 ostáva externý ordered CAMB-E auditný kontrakt;
4. backend potrebuje presnú dokumentovanú transformačnú mapu medzi vlastným
   stavom a týmto kontraktom na spoločných full-state checkpointoch;
5. TCA redukovaný stav potrebuje samostatný manifest a presný handoff.

Bez bijekcie/presnej projekcie, RHS parity a overlap testu CLASS nesmie
udeliť state-contract PASS.

## 6. Perturbačné rovnice a stress-energy ledger

Štandardné CDM a fluid riadky (`perturbations.c` približne `9219–9229` a
`9358–9389`) nemajú A1 transfer, K1 recoil ani K11-R reakciu. Full v002
musí pridať samostatné fuel/ash continuity a Euler rovnice, gauge mapu a
regular initial basis.

Povinné miesta:

- `perturbations_vector_init()` — natívna state/RHS parita;
- `perturbations_initial_conditions()` (`5269+`) — AD/CDI/BI/NID/NIV plus
  samostatné fuel/ash/steam regular modes podľa zmrazeného CS2 ranku;
- `perturbations_derivs()` (`8722+`) — exact finite-`k` A1/K11 rovnice;
- `perturbations_total_stress_energy()` (`6752+`) — nezávislý príspevok
  hustoty, hybnosti, palivového tlaku a shear;
- gauge/output/source bloky — obe dark zložky a steam bez pozičného kopírovania.

CLASS Einsteinove metric rovnice môžu zostať nezmenené iba po úplnej
stress-energy parite. Interné `0i`/slip riadky však nie sú nezávislé
holdouty. `00`, trace, total energy, total momentum a Bianchi sa musia
zostaviť druhou cestou z exportovaných stavov a analytických RHS.

Steam nemožno potichu zlúčiť s agregovaným `ur`. Mapovanie na collisionless
`idr` je prípustné iba po audite jeho backgroundu, normalizácie, closure a
vypnutí interakcií; inak potrebuje vlastnú hierarchiu.

## 7. Closure, TCA a počiatočné módy

CLASS má explicitné nenulové horné closure riadky pre fotóny, polarizáciu,
`idr` a `ur` približne na `9157–9161`, `9188–9193`, `9277–9281` a
`9452–9455`. Sú zdrojovo auditovateľnou referenciou, nie automatickým
dôkazom nášho CAMB/Frobeniovho closure.

Povinné je vybrať jednu konzistentnú architektúru:

- zachovať natívnu CLASS bázu a exaktne dokázať mapu na CAMB-E auditné
  checkpointy; alebo
- implementovať zmrazený v002 CAMB-E systém samostatne.

Miešať `E_2...E_L` s CLASS `pol0...polL`, pozične kopírovať TCA seed alebo
aplikovať generic rekurenciu aj na `ell=L` je fail-closed.

CLASS built-in počiatočné podmienky nemajú samostatné fuel entropy,
fuel-ash velocity ani steam density/velocity módy. Pri niektorých
interacting-radiation konfiguráciách dokonca odmietajú neadiabatické módy.
Úplná CS2 regular basis preto musí byť nová, nie iba premenovaný vstup.

## 8. Povinné testy pred fyzickým verdictom

1. upstream pinovaný CLASS reprodukuje referenčný background/thermal výstup;
2. `lambda=0` dá paritu custom fuel+ash s neinteragujúcim fluid+CDM;
3. exact-A1 background prejde nezávislým ODE a je identický pre dummy `k`;
4. rovnaké `H` dá HyRec null paritu `x_e/T_b/dkappa/visibility`;
5. zmena A1 parametrov vynúti prepočet thermal tabuľky;
6. FULL a DRAG_NULL majú identický background/thermal hash;
7. COMMON_NULL odstráni `lambda/Gamma/Upsilon`, ale zachová registrovaný
   radiation content vrátane pary; osobitný `STEAM_NULL` je iba diagnostika;
8. presne sa zruší dark energy/momentum aj Thomson momentum transfer;
9. steam-null odstráni iba samostatnú steam hierarchy;
10. polarization/state mapa a TCA/full overlap prejdú podľa mien;
11. nezávislé `00`, trace, conservation a Bianchi holdouty prejdú;
12. sign-flip fixture v dark alebo Thomson riadku musí holdout zabiť;
13. `L=4,6,8`, štart, časový krok, amplitúda a nezávislá metóda konvergujú.

## 9. Rozsudok a ohraničený ďalší krok

Zdrojové injection points existujú, exact-A1 `H(z)` sa dá viesť až do
HyRec a CLASS poskytuje použiteľné TCA/closure referencie. Preto backend
nie je fyzikálne ani technicky nemožný.

Full v002 však dnes neexistuje a nejde o úzky patch. Chýbajú:

- coupled present-day-normalized fuel/ash background;
- presný palivový tlak a `p_tot_prime` s transferom;
- custom dark perturbácie, stress ledger a gauge mapa;
- úplná regulárna mode basis a nezávislá steam hierarchy;
- CAMB-E/CLASS polarization a TCA handoff mapa;
- netautologické holdouty a konvergenčný harness.

Autoritatívny stav preto je

```text
BACKEND_FEASIBLE_SOURCE_INJECTION_POINTS_FOUND
FULL_V002_NOT_IMPLEMENTED
REVIEW_BLOCKED_IMPLEMENTATION
```

Tento audit nepridáva skóre, G-bránu, koľaj, opravný suffix ani release
trigger. V002 ostáva rovnakým fyzickým suffixom. Neskorší pokyn používateľa
zaviedol ledger `0/10` na jednu technickú architektúru; jej prípadný
`TECHNICAL_STOP` nie je fyzikálny STOP. V003 ani CS3 nevzniknú, pokiaľ sa
nemení fyzika.
