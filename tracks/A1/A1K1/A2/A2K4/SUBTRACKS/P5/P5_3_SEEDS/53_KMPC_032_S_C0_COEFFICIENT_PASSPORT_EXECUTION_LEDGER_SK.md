# KMPC-032 — S-C0 coefficient passport execution ledger

**Dátum:** 2026-07-16  
**Stav:** `TECHNICAL_FAILURE_PF069 / PHYSICS_NOT_REACHED`  
**Vstupná predregistrácia:** dokument 52  
**Interný limit:** najviac `4.8 s`  
**Vonkajší limit:** najviac `10 s` na každý samostatný proces

## Čo sa počíta ľudskou rečou

Existujúci solver má jeden spoločný voľne letiaci radiačný druh `fs`.
KMPC-032 ho nebude znovu riešiť ani rozširovať o nové fyzikálne stupne
voľnosti. Z každého už ukotveného koeficientu `delta_fs`, `U_fs` a
`sigma_fs` vytvorí dva rovnaké auditné pohľady `nu` a `steam`. Presnými
racionálnymi váhami overí, že ich súčet vráti pôvodný `fs` koeficient a že
sa nezmení zdroj energie, hybnosti ani anisotropného stresu.

Pri `l=3,4` sa overí iba všeobecná lineárna operatorová identita. Aktuálny
päťmódový M1/M3 zdroj tieto vyššie coefficient dictionaries neposkytuje,
preto sa z nich nesmie vyrobiť falošný coefficient PASS.

## Očakávaný výsledok a rozhodnutie

- Očakávame presné SymPy rezíduá `0` pre váhy, lift/collapse, tri Einsteinove
  zdrojové kombinácie, lower-moment riadky, nulový limit a operator commute.
- Očakávame skutočný ukotvený M1 state pre všetkých päť módov pri
  `k=0.05 Mpc^-1`, pričom existujúci M1 metadata guard musí prejsť.
- Očakávame odmietnutie všetkých 10 chybných fixtures rovnakým produkčným
  validatorom.
- Ak všetko prejde, kandidát výsledku bude
  `PASS_S_C0_LOWER_MOMENT_COEFFICIENT_LIFT_COLLAPSE_PASSPORT_ONLY`.
  Hlavný audítor ešte samostatne rozhodne; skóre a hĺbka sa nemenia.
- Ak presná formula neprejde, zastaví sa iba implementácia S-C0 splitu a
  prekontroluje sa formula/proveniencia. S-M a K4 neumierajú.
- Ak padne program, ide iba o technickú chybu. Zapíše sa dôvod a rovnaký
  rozsah sa opravuje do aktívneho limitu 10.

## Vopred zmrazený procesný sled

| Fáza | Proces | Očakávaný výsledok | PASS → | Odchýlka → | Stav |
|---:|---|---|---|---|---|
| 1 | `py_compile s1_collective_contract.py` | exit 0, bez výstupu | fáza 2 | technická chyba balíka | `PASS; exit 0; 0.5 s` |
| 2 | `py_compile s_c0_coefficient_passport.py` | exit 0, bez výstupu | fáza 3 | technická chyba balíka | `PASS; exit 0; 0.5 s` |
| 3 | `py_compile runner 276` | exit 0, bez výstupu | fáza 4 | technická chyba balíka | `PASS; exit 0; 0.5 s` |
| 4 | `runner --help` | usage, exit 0 | fáza 5 | technická chyba balíka | `PASS; exit 0; 0.5 s` |
| 5 | `runner --smoke --max-runtime-seconds 4.8` | contract/CLI/fixture-path smoke, bez výsledkového JSON | fáza 6 | technická chyba balíka | `PASS; smoke_pass=true; 1.0 s` |
| 6 | `runner --audit --max-runtime-seconds 4.8 --output ...` | immutable JSON a kandidát PASS/REVIEW | nezávislý audit | failure JSON, bez fyzikálneho verdiktu | `TECHNICAL_FAIL; TypeError np.float64; 1.2 s` |

Každá fáza je samostatný Python proces. Pred prvou fázou musia byť v
dokumente 52 zapísané SHA-256 všetkých troch nových Python zdrojov.

## Výsledky procesov

Táto sekcia sa aktualizuje po každej fáze. Predbehové očakávania vyššie sa
spätne nemenia; prípadná zmena interpretácie musí byť zdôvodnená v
samostatnom výsledkovom audite 54.

- Fáza 1 prešla presne podľa očakávania. Ide iba o syntax kontraktu; active
  technical counter sa nemení a fyzikálny výsledok nevznikol.
- Fáza 2 prešla presne podľa očakávania. Výpočtový modul je syntakticky
  platný, ale ešte nebol importovaný ani vykonaný; nejde o vecný výsledok.
- Fáza 3 prešla presne podľa očakávania. Runner je syntakticky platný;
  immutable write, hash guard a audit sa ešte nevykonali.
- Fáza 4 prešla. CLI výslovne ponúka vzájomne sa vylučujúce `--smoke` a
  `--audit`, runtime parameter a output; žiadna fyzika sa nespustila.
- Fáza 5 prešla: frozen hash guard, nezávislý contract, presné váhy a
  spoločná cesta desiatich negatívnych fixtures sú vykonateľné. Smoke
  nevytvoril výsledkový JSON a nevynuloval ani nezvýšil active counter.
- Fáza 6 zastala počas konverzie prvého skutočného M1 koeficientu. Hodnota
  `np.float64(6.5297...e-17)` bola poslaná do `SymPy Rational` cez text
  obsahujúci wrapper `np.float64(...)`; SymPy ho odmietol `TypeError`.
  Nevyhodnotila sa žiadna S-C0 fyzikálna identita a nevznikol výsledkový
  PASS/STOP JSON. Immutable failure dôkaz má SHA-256
  `51C7B32B84F498ACD9CEFD7BC72D546D87F1DDCBC4C2BC189A02E1036991EA03`.
  Úzky nástupca smie zmeniť iba bezpečnú konverziu každého konečného
  `numbers.Real` cez `float(value)`; rovnice, váhy, supporty a prahy ostávajú.
