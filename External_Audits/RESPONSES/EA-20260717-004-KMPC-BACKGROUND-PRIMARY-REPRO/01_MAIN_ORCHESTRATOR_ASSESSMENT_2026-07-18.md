# Hlavný posudok externého auditu EA-20260717-004

**Dátum:** 2026-07-18  
**Externá odpoveď:** `00_AUDITOR_AUDIT.md`  
**SHA-256 externej odpovede:**
`F5A8D1AB9BF1E9306C7786D39037D0A09BFCA0DBD5732C142869F9920987A487`  
**Autorita:** hlavný orchestrátor  
**Spracovanie:** `ACCEPTED_WITH_LIMITATIONS`

## Autoritatívny rozsudok

```text
PACKAGE_TIER = T2_REPRODUCIBLE_CALCULATION_WITH_ENVIRONMENT_GAP
EA001_EVIDENCE_UPGRADE = PASS_MAPY -> T2_FOR_THE_FOUR_SCOPED_QUESTIONS
PROJECT_VERDICT = UNCHANGED
ROUTE_SCORE_AND_DEPTH = UNCHANGED
```

Auditor overil manifest `26/26`, skontroloval primárne riadky a na nezávislej
platforme reprodukoval R1–R3. Fyzikálne polia zodpovedajú zapečateným raw
výsledkom bit po bite; odlišný je iba očakávaný `runtime_seconds`. Balík 004
preto dosiahol deklarovaný cieľ T2 a uzatvára dôkazovú medzeru E-1 balíka
001.

Tento T2 je PASS reprodukovateľnosti a formula lineage. Nie je to nový PASS
celej A2-K4, perturbácií, CLASS/CAMB, CMB/S8 ani mikrofyzického pôvodu
closure. A2-K4, jej skóre, hĺbka, release a Zenodo sa nemenia.

## Prijaté výsledky

1. Historický runner 213 skutočne preniesol fixed `K_MPC=0.05` cez `z^p`
   do denominatora. Starý `D(a,k)` preto nie je univerzálny FLRW background.
   Existujúci `STOP_BACKGROUND_K_DEPENDENCE_UNRESOLVED` zostáva správny a
   je ohraničený na historickú implementáciu.
2. Mapovanie
   `Phi(k)=A_f[H0 sqrt(Omega_r0)/k]^p` ruší módové `k` vo vedúcom ranom
   fuel člene. Auditor to potvrdil multi-`k` kontrolou aj negatívnou
   kontrolou. Výrok platí pre auditovaný raný rad; nie je dôkazom celého
   mikrofyzického mechanizmu.
3. `A_f=7809.270101963506` je výsledok konkrétneho FrozenA1 closure pri
   `lambda=0.15`, nie nový nezávislý fit ani konštanta prírody. RK4 výsledok
   bol reprodukovaný bitovo a nezávislá DOP853 kontrola súhlasí približne na
   `1e-12`.
4. Skrátený K7 rad nie je plný neskorý background. Nulový prechod blízko
   `a=0.70895788` a záporné `D_K7,trunc(1)` boli reprodukované; exact-A1
   background tým nie je zabitý.

## Nové nálezy a ich autoritatívne spracovanie

| ID | Spracovanie | Dopad |
|---|---|---|
| `A-1` | `ACCEPTED_PRIMARY_SOURCE_SEAM` | Runner 213 a FrozenA1 používajú odlišnú fotónovú konštantu (`2.47282e-5` verzus `2.469e-5`). Pred prenosom do CLASS/CAMB musí vzniknúť deklarácia záväznej `T_CMB/Omega_r0` konvencie a changelog historického švu. Zapečatený runner sa neprepisuje. |
| `A-2` | `ACCEPTED_LOW_SEVERITY` | `0.70895788` je gridovo lokalizovaná nula; presnejšia externá bisekcia nemení verdict. |
| `A-3` | `ACCEPTED_AS_EXTERNAL_DIAGNOSTIC` | Kvalitatívny záver je prijatý: nulový prechod je iba neskorý symptóm a skrátený rad stráca kvantitatívnu presnosť oveľa skôr. Čísla `a≈3.6e-6` pri 0.1 %, `a≈4.0e-5` pri 1 % a plateau približne 8.2 % zatiaľ nie sú kanonický projektový raw výsledok; na taký status potrebujú nový registrovaný runner, preregistráciu a raw JSON. |
| `A-4` | `ACCEPTED_PROVENANCE_DEBT` | Runner 235 nevynucuje SHA-256 vstupného `--af-json`. Každý nový nástupca musí hash vstupu kontrolovať; runner 235 sa spätne nemení. |
| `A-5` | `ACCEPTED_SCOPE_LIMIT` | Symbolický audit je viazaný na `lambda=3/20`. Budúci multi-`lambda` test musí použiť symbolické `lambda`; dnešný pracovný bod zostáva platný. |
| `A-6` | `ACCEPTED_LOW_SEVERITY` | Voľné `--x-min` nie je defenzívne zosúladené s fixnými checkpointmi. Opraviť iba v novom runneri, ak sa rozšíri jeho vstupný kontrakt. |

## Povinné následné kroky

1. Pred CLASS/CAMB uzavrieť `A-1`: zvoliť jednu záväznú fotónovú/
   `Omega_r0` konvenciu, uviesť jednotky a zaznamenať historickú odchýlku.
2. Každý nástupca runnera 235 musí hashovo viazať `A_f` JSON a uložiť úplný
   provenance tag (`lambda`, A1 vstupy, hash runu, jednotky a konvenciu
   `Omega_r0`).
3. Ak sa majú presné hranice z `A-3` používať v seede alebo v scope výroku,
   najprv ich reprodukovať projektovým predregistrovaným behom.
4. Pokračovať existujúcou P4 exact-background rederivation: `H(a)` a
   `d tau/da` z exact-A1, potom koeficienty bez skráteného denominatora,
   následne nulový limit a až potom CLASS/CAMB rozhranie.

## Čo sa nemení

- staré fixed-`K_MPC` a truncated-K7 STOP-y zostávajú ohraničené;
- exact-A1 zostáva jediným prípustným backgroundovým kandidátom tejto vetvy;
- mikropôvod A1 closure a parameter provenance zostávajú otvorené;
- nevzniká nový route PASS/REVIEW/STOP ani zmena skóre;
- nevzniká oprávnenie spustiť CMB/S8, likelihood alebo release.

Stav balíka: `ASSESSED_BY_MAIN_ORCHESTRATOR`.  
Stav projektu: nezmenený.
