# A2-K4 / C7.7c / K7d — preregistrácia integrovanej brány C7-G4+G6+G7

**Dátum:** 2026-07-15  
**Stabilné ID:** `SCI-A2K4-C7G467-K7D-INTEGRATED`  
**Vstup:** C7-G5 PASS; P4a V0 prešla bez technickej opravy  
**Stav:** `PREREGISTERED / NOT RUN`  
**Celková váha:** `30/100` podľa C7-W1

## Ľudská otázka

K7 už ukázala, že jej krátka NID/deep trajektória nie je artefaktom jedného
kroku, solvera ani tolerancie. Teraz sa má jedným spoločným operátorom
rozhodnúť podstatnejšia otázka: prežije tá istá fyzika celý interval na NID
aj NIV, z hlbokého aj plytkého štartu, s rozlíšenou aktivitou všetkých 13
zložiek a s nezávislými Einsteinovými trace/traceless testami?

Očakávame konečné a vzájomne konzistentné riešenia. Neznámu veľkosť
jednotlivých módov nevymýšľame; predregistrujú sa invarianty, relatívne
rezíduá a rozdiel hlbokého/plytkého štartu.

## Zmrazená fyzika

Voči P4a/skriptu 209 sa nesmie zmeniť background, parametre, znamienka,
poradie 13 projektovaných premenných, high-precision seed handoff 178,
`physical_rhs`, kanonické dve presné nuly ani closure `L5=0`. Closure je
dočasná a znamená, že ani úplný PASS neudeľuje G8.

Plnointervalová mierka sa určí **pred evolúciou** ako maximum absolútnej
hodnoty príslušného deep seedu, shallow seedu a analytickej referencie 146 na
`x=-18`, po jej deterministickom prevode zo species bázy na `D,M`. Evolved
endpoint sa nesmie použiť na vytvorenie vlastnej tolerancie.

## Jedna konfiguračná matica

| Prípad | Štart | Koniec | Základná metóda |
|---|---:|---:|---|
| NID-deep | `-25` | `-18` | DOP853-tight |
| NID-shallow | `-23` | `-18` | DOP853-tight |
| NIV-deep | `-25` | `-18` | DOP853-tight |
| NIV-shallow | `-23` | `-18` | DOP853-tight |

Základné nastavenie: `rtol=1e-11`, normalizované `atol=1e-13`,
`max_step=0.05`, checkpoint každých `0.25` e-foldu, interný limit jedného
prípadu `25 s`, externý limit `30 s`, RHS cap `100000` a normalizovaný safety
cap `1e8`. Každý prípad zapisuje vlastný immutable JSON. Agregát fyziku
nespúšťa.

## Klasifikácia kontrol G4

### A. Nezávislé a skórujúce

1. **Einstein trace**

   `R_T = h_xx + (q+2)h_x - 2 s² eta + 9 P = 0`.

2. **Einstein traceless**

   `R_S = h_xx + 6 eta_xx + (q+2)(h_x+6 eta_x) - 2 s² eta + 9 S = 0`.

   Tu `h_xx` vznikne diferenciáciou `h_x=3D+2s²eta`, `eta_xx=M_x`,
   `P = Ω_f[df+(2-δ)(3δ+g)U_f] + (Ω_γ dγ+Ω_fs d_fs)/3` a
   `S=(2/3)Ω_fs sigma_fs`.

Tieto rovnice sa nepoužijú na definovanie `h_x`, `eta_x`, `D_x` ani `M_x`.
Na každom checkpointe musí platiť zmiešaná brána
`|R| <= 1e-12 + 1e-8 * sum(|term_j|)`. Zároveň sa exportuje čisté relatívne
rezíduum tam, kde norma členov nie je subnormálna.

3. **Aktivita 13 projektovaných zložiek.** Pre každú trajektóriu a zložku
   sa používa vopred určená obálková mierka `S_i`. Dynamický signál
   `max_x |y_i(x)-y_i(x_start)|/S_i` musí byť aspoň `1e-10`, teda aspoň
   `1000 × atol_norm`. Maximum normalizovanej RHS musí byť aspoň `1e-11`.
   Obe čísla sa exportujú; PASS vyžaduje aspoň jednu z dvoch dynamických
   ciest a konečný, numericky rozlíšený komponent. Všetkých 52 kombinácií
   mód/povrch/zložka musí mať explicitný výsledok; nič sa nesmie stratiť v
   priemere.

### B. Nezávislá implementačná parita bez bodov

V každom checkpointe sa z `D,M` rekonštruujú `delta_fs,U_fs`, samostatne sa
vyhodnotí species RHS podľa pôvodnej 13-zložkovej formulácie a jej derivácia
sa transformuje späť do projektovanej bázy. Max. škálovaný rozdiel oproti
K7 projected RHS musí byť `<=1e-10`. Táto kontrola chráni kód, ale nepridáva
druhý fyzikálny kredit za tú istú rovnicu.

### C. Iba monitory bez bodov

- `h_x == 3D+2s²eta` a `eta_x == M` sú konštrukčné identity;
- spätné zloženie density/momentum po rekonštrukcii species je cancellation
  monitor;
- samotná konečnosť, runtime a safety cap sú execution kontroly.

Žiadna položka C nesmie udeliť G4 PASS.

## Brána G6 — štyri plochy, váha 10

Každý zo štyroch prípadov musí samostatne:

- načítať správny mode/surface seed a jeho hash;
- zachovať presné mená a poradie 13 zložiek;
- dosiahnuť `x=-18` s konečným stavom aj RHS;
- zapísať všetky checkpointy a rešpektovať oba capy;
- mať vlastný PASS/REVIEW/STOP záznam.

Tri úspešné povrchy nezakryjú štvrtý timeout. Timeout je REVIEW, nie
fyzikálna smrť.

## Brána G7 — celý interval a deep/shallow agreement, váha 5

Pre NID aj NIV sa porovná deep trajektória s shallow trajektóriou na celom
spoločnom intervale `[-23,-18]`:

- primárny L2 relatívny rozdiel endpointu musí byť `<=3e-3`, čo zachováva
  starší predregistrovaný prah BR2;
- maximum obálkovo škálovaného komponentového rozdielu endpointu musí byť
  `<=1e-2`;
- maximum obálkovo škálovaného rozdielu na spoločných checkpointoch musí
  byť `<=2e-2`;
- všetky tri metriky sa vyhodnotia osobitne pre NID a NIV.

## Očakávaný výsledok a vzdialenosť od očakávania

| Veličina | Očakávanie | PASS hranica | Ak je mimo |
|---|---|---|---|
| štyri trajektórie | všetky konečné do `x=-18` | 4/4 | technický REVIEW alebo stabilitný kandidát podľa signálu |
| trace/traceless | Bianchi-konzistentné | mixed `1e-12 + 1e-8*norm` | cielené nezávislé potvrdenie |
| 13-zložková aktivita | rozlíšená v obálkových súradniciach | 52/52 explicitne uzavretých | audit presnej zložky, nie globálne uvoľnenie flooru |
| species/projected parita | iba roundoff | `<=1e-10` | technická chyba implementácie |
| deep/shallow endpoint | rovnaký fyzikálny mód | L2 `<=3e-3`, envelope `<=1e-2` | potvrdiť druhým solverom oba povrchy módu |

Po behu finálny audit uvedie pozorovanú hodnotu, rezervu alebo prekročenie
každého prahu a presnú zložku/checkpoint najhoršieho prípadu.

## Ohraničené rozhodovanie podľa AR66 a AR67

1. Základ V0: presne štyri prípady.
2. Celý balík má najviac **dve ďalšie cielené solverové spustenia** a
   najviac dve technické opravy. Nejde o dve opravy na každý povrch.
3. Formálna/provenance/parity chyba → `REVIEW`; opraví sa iba konkrétna
   technická príčina bez zmeny fyziky alebo prahov.
4. Jediný fyzikálny rozpor → zopakuje sa nezávislou metódou alebo
   toleranciou iba na rozhodujúcom povrchu. Pri endpoint konflikte sa
   potvrdia oba povrchy daného módu, čím sa spotrebujú obe spustenia.
5. Reprodukovateľný vysoko vážený rozpor s platnou numerikou → STOP K7 a
   architektonický audit A2-K4. Nezakladá sa automaticky K8.
6. Rozpor nepotvrdený ani neodstránený v rozpočte → `REVIEW_BLOCKED`.
7. G4, G6 aj G7 PASS → strict support `60 -> 90/100`; nasleduje G8.

## Čo ani úplný PASS nedokazuje

Balík nepoužíva plnú fotónovú/neutrínovú hierarchiu, recombination backend,
CMB likelihood ani neskorý rast `S8`. Closure `L5=0` ostáva explicitné
obmedzenie do G8. Jemná hĺbka `66.5/100` sa nemení bez samostatného depth
crosswalku.

## Plán artefaktov

- jeden verziovaný runner s režimami `prepare`, `case`, `aggregate`;
- jeden nezávislý fail-closed checker zdrojov a error-ledgeru;
- štyri immutable raw JSON a jeden offline agregát;
- finálny MD audit a SHA-256 manifest;
- žiadne nové K-ID ani písmenový P-suffix pre solver/toleranciu.

