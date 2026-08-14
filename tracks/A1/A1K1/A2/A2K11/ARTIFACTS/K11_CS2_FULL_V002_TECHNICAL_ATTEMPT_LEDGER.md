# K11-CS2 full v002 — register technických pokusov

**Dátum založenia:** 2026-07-16  
**Fyzická koľaj:** `A1-K1 -> A2-K11 -> K11-R -> K11-CS2`  
**Technická vetva:** `K11-CS2-FULL-v002 / ARCH-A`  
**Stav vetvy:** `STRUCTURAL_SOURCE_AST_PASS / FULL_DAE_NOT_STARTED`  
**historical_packages_total:** `5`  
**consecutive_technical_failures:** `0/10` po vecne úspešnom pokuse 5  
**Fyzické pokusy:** `0`  
**Fyzikálna hĺbka:** bez zmeny, `10/100 = G1`

**Nasledujúci technický míľnik:** samostatne predregistrovaný full
thermal/TCA/DAE historický balík číslo 6 na prejdenom source-AST contracte.
Aktívny counter pred jeho spustením je `0/10`. Evolučný
`lmax`/closure sweep zostáva povinný pred fyzikálnym verdictom.

## Čo sa počíta ako jeden technický pokus

Jeden pokus je jeden vopred oznámený preflight alebo run balík, ktorý má
overiť konkrétny technický míľnik tejto architektúry. Môže obsahovať
samostatne timeoutovaný compile, import, help, smoke a run, ale celý balík
má jedno číslo pokusu. Zlyhanie ktorejkoľvek povinnej fázy znamená jeden
technický neúspech.

Read-only audit, Markdown zápis, kontrola hashov a úspešné čítanie zdroja sa
za technický pokus nepočítajú. Pokus sa nezapočíta ako fyzikálny, kým celý
technický a formula-provenance preflight neprejde a nevznikne úplný
interpretovateľný výsledok s povinnými holdoutmi.

## Povinný záznam neúspechu

Každý neúspech zachová:

- číslo pokusu, dátum a presný príkaz alebo manifest príkazov;
- cieľ a predbehové očakávanie;
- poslednú dokončenú fázu a exit/timeout;
- dotknuté súbory a ich hashe;
- presnú príčinu a jednu alebo viac kategórií;
- opravu alebo rozhodnutie zmeniť technickú architektúru.

Povolené hlavné kategórie:

```text
SCRIPT_IMPLEMENTATION_FAILURE
PYTHON_OR_DEPENDENCY_FAILURE
SANDBOX_OR_ENVIRONMENT_FAILURE
BUILD_OR_ADAPTER_FAILURE
```

## Tabuľka pokusov

| Pokus | Stav | Dôvod / výsledok |
|---:|---|---|
| 1 | `TECHNICAL_FAIL_EXTERNAL_TIMEOUT_124` | smoke PASS; full payload mal exact checks PASS a internal 3.25 s, ale celý proces s importom trval ~10.9 s; JSON diagnostický, nie autoritatívny |
| 2 | `TECHNICAL_FAIL_STALE_ATTEMPT_IDENTIFIER` | L4 exact checks a exit 0, ale JSON mal starý `ATTEMPT_1` verdict; L6/L8 nebežali |
| 3 | `TECHNICAL_FAIL_EXTERNAL_TIMEOUT_124` | L4 exact checks PASS a internal 0.687 s, ale import zvýšil wall na ~10.2 s; L6/L8 nebežali |
| 4 | `TECHNICAL_FAIL_EAGER_PACKAGE_IMPORT` | 55/55 PASS payload, internal 0.047 s; package init načítal CAMB/SymPy a wall skončil timeout 124 |
| 5 | `PASS_SOURCE_AST_STRUCTURAL_ONLY` | 55/55, counts 25/33/41, internal 0.032 s, wall ~1.5 s, exit 0; lazy package init; bez ODE/bodov |

Ďalší balík v ARCH-A má historické poradové číslo 6. Pokus 5 priniesol nový
interpretovateľný structural result, preto aktívny counter po sebe idúcich
technických zlyhaní vynuloval na `0/10`. Compile/help/smoke/hash-only by ho
nevynulovali. Historické poradové čísla sa nerecyklujú.

## Stav po limite

Ak desať balíkov tejto implementačnej línie **po sebe** technicky zlyhá,
`ARCH-A` dostane
`TECHNICAL_STOP` a posledný riadok musí ľudsky povedať, či sme nedokázali
napísať stabilný skript, zlyhal Python/dependency, sandbox/prostredie alebo
build/adapter. Tento stav nezabíja K11 ani K11-CS2. Rodič dostane
`REVIEW_TECHNICAL_UNRESOLVED`.

Vecný úspešný výpočet aktívny counter vynuluje, ale nemaže tabuľku. Iná
technická architektúra smie vzniknúť až po samostatnom Markdown
rozhodnutí, ktoré vysvetlí, čím odstráni príčinu smrti `ARCH-A`. Dostane
vlastný lineage ledger; aktívny counter sa nezačne nanovo iba premenovaním.
Fyzický suffix sa nemení, kým sa nemenia rovnice,
mechanizmus, prahy ani rozsah.
