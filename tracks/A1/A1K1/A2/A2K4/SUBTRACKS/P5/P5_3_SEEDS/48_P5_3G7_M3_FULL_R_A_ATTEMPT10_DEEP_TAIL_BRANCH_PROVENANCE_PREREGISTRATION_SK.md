# P5.3g7-M3-FULL/R-A — pokus 10/10, deep-tail branch provenance

**Dátum:** 2026-07-16  
**Run ID:** `KMPC-031`  
**Stav:** `ATTEMPT_10_PREREGISTERED / NOT_RUN`  
**Scope:** `AD / k=0.05 / nominal / Phi1 M3-TCA0 / no-solve support audit`  
**K4:** `LIVE / 60/100`

## 1. Prečo vzniká posledný balík

KMPC-030 technicky prešiel všetkých 22 numerických brán. Raw full-state tail
však pri `z=1e-4` neprešiel, hoci J6→J8 bol monotónne lepší. Audit ukázal:

```text
full independent-solve difference
= common-low-coefficient drift
+ explicit added-power tail
```

Pri `U_b` tvorí raw rozdiel takmer celý drift formálne nulového koeficienta
`U_b[0] ~ 1e-16`; skutočné nové powers sú J4→J6 približne `4.58e-25` a
J6→J8 približne `7.85e-35`. Immutable raw FAIL sa nesmie premenovať na PASS.
Treba iba zistiť, či explicitný support tail s pôvodným prahom konverguje.

## 2. Immutable vstupy

| vstup | SHA-256 |
|---|---|
| J4 KMPC-028 | `2294E8623675B49F2D5A814005306D4E98E3CBDF4A1A66BD3AE1A9C0331EFC83` |
| J6 KMPC-029 | `658495A11A3C72262CDCBEC9B9515794E506A6C7F14F40865704AA26E6C4636A` |
| J8 pôvodný KMPC-029 | `1EE3FCDF3B77C6C7E4C26317A3F39AA45D4CFA5BA6B559E312E598BC3ED51AB8` |
| refined J8 + ladder KMPC-030 | `8CB706223C43EB4E72F2B56BE266C73E07349F2E0D6B32212E280AB64F803C6F` |

Refined J8 sa číta výhradne z
`KMPC-030.one_refinement.fractional_state`. F0 a M3 common bridges sa berú z
toho istého hash-locknutého KMPC-030. Žiadny solve, ODE, fit alebo prepis
vstupného JSON nie je dovolený.

## 3. Presné rozdelenie pre každý stav a obe z-plochy

Pre bridge `N→M`, stav `i` a `z` sa vypočíta:

```text
C_i(z) = sum_{j=0..N} (c_i^M[j] - c_i^N[j]) z^j
T_i(z) = sum_{j=N+1..M} c_i^M[j] z^j
R_i(z) = (sum_{j=0..M} c_i^M[j] z^j)
       - (sum_{j=0..N} c_i^N[j] z^j)
```

Povinná identita je `R_i = C_i + T_i`. Počíta sa nezávisle cez
`Decimal(repr(float))` s precision najmenej 70 a cez float64. Decimal
reconstruction absolute residual musí byť `<=1e-50`; float/Decimal added-tail
crosscheck musí byť `rtol<=1e-12`, `atol<=1e-300`.

## 4. Formálny added-support tail gate

KMPC-030 už dokázal forbidden layers `j<2 <=1e-10`. Pre formálnu Puiseuxovu
sériu sa preto pri výpočte menovateľa support tailu tieto vrstvy projektujú na
presnú nulu. Ich neprojektovaný drift zostáva plne viditeľný v `C_i` a v raw
diagnostike; nesmie sa vymazať z coefficient bridge.

Z jedného vyššieho riešenia sa definuje:

```text
P_i^M,<=N(z) = sum_{j=2..N} c_i^M[j] z^j
P_i^M,<=M(z) = P_i^M,<=N(z) + T_i(z)
scale_i = max(abs(P_i^M,<=N), abs(P_i^M,<=M))
```

- ak `scale_i > 1e-12`, gate je `abs(T_i)/scale_i <= 1e-6`;
- inak gate je `abs(T_i) <= 1e-12`.

Prah sa nemení. Common coefficients majú naďalej samostatnú frozen gate
`relative<=1e-8` alebo `absolute<=1e-12`. F0 aj M3 bridges musia zostať PASS.

## 5. Povinné ochrany

1. exact source/result hashes a identity Run ID;
2. presná množina stavov z frozen contractu a explicitné kanonické premapovanie
   JSON kľúčov do authoritative poradia;
3. pre každý stav exact power sets J4 `0..4`, J6 `0..6`, J8 `0..8`;
   F0 musí mať presne stavy `{delta_f,U_f}` a rovnaké power rozsahy;
4. KMPC-030 má 22/22 numerical checks a všetky structural ladder checks PASS;
5. pôvodný raw FAIL sa reprodukuje: J4/J6 `1.2308231758e-5` a J6/J8
   `3.3632353574e-6` pri `z=1e-4`, oba worst `U_b`;
6. decomposition identity, finite Decimal/float hodnoty a crosscheck PASS;
7. common F0/M3 bridges ostávajú PASS bez zmeny prahov;
8. explicitný tail J6→J8 nesmie byť horší než J4→J6 na oboch z-plochách;
9. raw full-state metrika zostáva označená
   `MIXED_COMMON_DRIFT_PLUS_ADDED_TAIL_DIAGNOSTIC`, nikdy čistý tail PASS.
10. `leading_j=2` sa musí zhodovať s frozen AD mode a pred projekciou sa
    exportuje maximum všetkých J4/J6/refined-J8 koeficientov `j<2`; každé
    musí byť `<=1e-10` a uložené forbidden guards musia zostať PASS.
    J4/J6/refined-J8 `U_c` lower-regularity guards musia tiež zostať PASS.

## 6. Očakávania zmrazené pred kódom

Z read-only auditu immutable koeficientov očakávame:

| explicitný tail | z | max relative | worst | max absolute fallback |
|---|---:|---:|---|---:|
| J6 powers 5–6 nad J4 cut | `1e-4` | `4.66448e-14` | `U_f` | `4.75112e-38` |
| J6 powers 5–6 nad J4 cut | `1e-2` | `4.66857e-8` | `U_f` | `4.84565e-28` |
| J8 powers 7–8 nad J6 cut | `1e-4` | `5.16515e-24` | `U_f` | `3.28409e-46` |
| J8 powers 7–8 nad J6 cut | `1e-2` | `5.17916e-14` | `U_f` | `3.30475e-32` |

Priama float/Decimal kontrola added tailu zostáva `rtol=1e-12`,
`atol=1e-300`. Tabuľka je však zámerne zaokrúhlená na šesť platných číslic;
jej samostatná reprodukčná kontrola preto používa `rtol=2e-5`,
`atol=1e-300`. Táto pomocná tolerancia nemení fyzikálny tail gate. Očakávanie
sa po behu nemení bez samostatného zdôvodnenia.

## 7. Vopred zmrazené vetvy

### Oba explicitné tails PASS a monotónnosť PASS

```text
TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT
CANDIDATE_SUPPORT_TRUNCATION_CLOSED_J4_SENTINEL_SCOPE
```

To uzatvára iba support truncation pre conditional
`Phi1 M3-TCA0 AD/k=.05/nominal`. Nie je to celý P5.3, P5.4, G8, CMB, S8 ani
K4 PASS.

### Iba J6→J8 PASS

```text
CANDIDATE_J6_MINIMUM_SENTINEL_SUPPORT
```

### Decomposition, bridges alebo oba tails neprejdú

```text
REVIEW_SUPPORT_TAIL_UNCLOSED
ARCH_A_COUNTER_CLOSED_10_OF_10
```

K4 zostáva živá na `60/100`; nejde o fyzikálnu smrť.

### Technická chyba

```text
ATTEMPT_10_TECHNICAL_FAILURE
ARCH_A_TECHNICAL_STOP_10_OF_10
PHYSICS_VERDICT=NONE
```

Musí sa uviesť presný dôvod script/Python/sandbox/storage. Technická chyba sa
nesmie premenovať na fyzikálny FAIL.

## 8. Limity a proces

```text
py_compile(wrapper) -> py_compile(runner) -> --help -> one --audit process
```

Každý Python proces má externý limit `10 s`; audit má interný limit `4.8 s`.
Výstup je jediný immutable súbor
`RUN_KMPC_031_P5_3G7_M3_FULL_RA_DEEP_TAIL_BRANCH_PROVENANCE.json`; failure má
presný suffix `_TECHNICAL_FAILURE.json`. Runner nepovoľuje alternatívny output.

## 9. Release

```text
NO_NEW_TRIGGER
EXISTING_PT1_REMAINS_OPEN
PT2_NOT_ESTABLISHED
```

## 10. Hash freeze po troch read-only auditoch

Physics-track, math-script a documentation-release audítor nenašli po opravách
false-PASS ani dokumentačný blocker. Neudeľovali runtime ani fyzikálny verdict.

| artefakt | SHA-256 |
|---|---|
| `full_ra_m3_seed_attempt10_tail_provenance.py` | `A7C06D4C16AF5429319DFF307ADB4A2FCF72542AA65E92B1D6EA1B229387CA55` |
| `275_script_KMPC_031_P5_3g7_m3_full_ra_deep_tail_branch_provenance_attempt10.py` | `A222F96EEAF32042CCAE634FB71EE1794119704D83B26BC30D83B358568C15B2` |

Wrapper je hash-frozen v runneri. Ďalší edit Python súborov ruší freeze a
vyžaduje nový statický audit pred spustením.
