# A2-K4 / C7.7c / K7c / P4a — preregistrácia metódovej a tolerančnej šírky C7-G5

**Dátum:** 2026-07-15  
**Stabilné ID:** `SCI-A2K4-C7G5-K7C-P4A-METHOD-TOLERANCE`  
**Vstupný stav:** P3b izolovaná kroková RK4 brána PASS; celý C7-G5 REVIEW  
**Typ očakávania:** `ANALYTIC + REGRESSION`

## Ľudská otázka

P3b ukázala, že po kanonizácii dvoch presných núl sa klasický RK4 správa ako
metóda štvrtého rádu. P4a má overiť, či ten istý koncový stav dostanú aj
adaptívny explicitný DOP853 a implicitný Radau a či výsledok DOP853 ostane
stabilný po sprísnení tolerancií. Ak áno, kroková, tolerančná aj metódová
časť C7-G5 budú uzavreté. Ak nie, P3b je iba lokálny RK4 výsledok a G5
zostane otvorená alebo dostane lokálny STOP.

## Zmrazený fyzikálny kontrakt

Voči skriptu 205 sa nesmie zmeniť:

- seed source 178 a jeho hash;
- NID/deep počiatočná plocha;
- interval `x=-25.0` až `x=-24.75`;
- poradie a význam 13 stavových zložiek;
- background, parametre, znamienka, closure `L5=0` a scale;
- `physical_rhs` vrátane kanonického vynechania iba dvoch presných núl;
- porovnávacia norma `max_i |w_i^A-w_i^B|` v identických normalizovaných
  súradniciach;
- referenčný endpoint P3b grid400 a jeho súborový SHA-256
  `9E3C73D635924E829A5F57BA540EBB1F5861F67F21CFCE69BD93423D6FA8FC8D`.

Nový source-delta audit musí pred prvým vedeckým prípadom dokázať zhodu
backgroundu, `physical_rhs`, scale, intervalu, seedu a mien stavov. Smie sa
líšiť iba solverový obal, CLI, fail-closed výstup a diagnostika metódy.

## Povinná architektúra behov

Jeden číslovaný runner vykoná vždy iba jeden prípad a zapíše jeden immutable
JSON. Každý prípad má samostatný interný aj externý timeout. Offline agregát
iba číta tri hotové JSON; nespúšťa deti ani fyziku.

| Prípad | Metóda | `rtol` | `atol` v normalizovanom stave | Interný limit | Vonkajší limit |
|---|---|---:|---:|---:|---:|
| `DOP853_MEDIUM` | DOP853 | `1e-9` | `1e-11` | 20 s | 25 s |
| `DOP853_TIGHT` | DOP853 | `1e-11` | `1e-13` | 20 s | 25 s |
| `RADAU_TIGHT` | Radau | `1e-10` | `1e-12` | 20 s | 25 s |

Seed source má limit najviac 12 s a jeho dieťa najviac 6 s. RHS call cap je
`100000` na prípad. Žiadny timeout sa automaticky neopakuje s dlhším limitom.

## Predbehové očakávania

Referenčná požiadavka C7-G5 bola `1e-6`. P4a používa prísnejší krížový limit
`1e-8`, teda stonásobnú rezervu voči bráne. Centrálne očakávanie nie je
konkrétne znamienko odchýlky, ale metódová zhoda v tomto intervale.

| Veličina | PASS hranica |
|---|---:|
| `DOP853_TIGHT` vs P3b RK4-grid400 | `<= 1e-8` |
| `DOP853_MEDIUM` vs `DOP853_TIGHT` | `<= 1e-8` |
| `RADAU_TIGHT` vs P3b RK4-grid400 | `<= 1e-8` |
| `RADAU_TIGHT` vs `DOP853_TIGHT` | `<= 1e-8` |

Každý prípad musí navyše:

- skončiť `solver_success=true` presne v `x=-24.75`;
- mať konečný stav aj RHS konečné;
- zachovať presné mená a poradie 13 zložiek;
- rešpektovať normalized safety cap `1e8` a RHS cap;
- uviesť `nfev`, runtime, solver message, endpoint a všetky zdrojové hashe;
- odmietnuť prepísanie existujúceho výstupu.

Constrainty v P4a sú iba monitory. Nezískavajú G4 váhu, pretože časť z nich
je v projektovanej sústave vynútená definíciou.

## Rozhodovací strom

1. Source-delta, syntax, CLI, SciPy import alebo provenance FAIL → `REVIEW`;
   vedecké prípady sa nespustia.
2. Timeout alebo technická chyba jedného prípadu → iba tento prípad REVIEW;
   hotové prípady sa zachovajú, agregát celý G5 neuzavrie.
3. Všetky štyri porovnania `<=1e-8` a všetky štrukturálne brány PASS →
   `PASS_P4A_G5_METHOD_TOLERANCE_BREADTH`; C7-G5 môže dostať plný PASS podľa
   C7-W1. Jemná hĺbka A2-K4 sa mení iba samostatným depth crosswalkom.
4. DOP853 tight a Radau sa zhodnú navzájom, ale nie s RK4 → P3b referencia
   sa znovu otvorí; `REVIEW_REFERENCE_CONFLICT`, nie okamžitá smrť K4.
5. Platné alternatívne metódy sa nezhodnú navzájom →
   `STOP_P4A_METHOD_BREADTH`; zachovať všetky výsledky a auditovať tuhosť,
   normu a solver assumptions pred G4/G6.

## Plánované číslovanie

- 209: jednopřípadový P4a runner;
- 210: source-delta a formálny audit 205 → 209;
- 211: versioned corpus checker pred fyzikou;
- 212: offline agregát troch immutable výsledkov.

Čísla sa nesmú znovu použiť, ani keď niektorý skript skončí technicky mŕtvy.

## Rozsah, ktorý ani PASS nepovoľuje preskočiť

P4a netestuje netautologickú G4, NID/NIV × deep/shallow G6, plný interval,
plnú Boltzmannovu hierarchiu, CMB, `S8`, `H0` ani likelihood. Po P4a PASS
nasleduje P4b-G4 a až potom P4c-G6.

