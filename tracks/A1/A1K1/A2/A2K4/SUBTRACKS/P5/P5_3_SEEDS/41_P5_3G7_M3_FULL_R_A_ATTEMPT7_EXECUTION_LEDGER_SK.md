# P5.3g7-M3-FULL/R-A — pokus 7/10, vykonávací ledger

**Dátum:** 2026-07-16  
**Run ID:** `KMPC-028`  
**Route:** `A1-K1 -> A2-K4 -> P5 -> P5.3g7-M3-FULL/R-A`  
**Stav:** `ATTEMPT_7_CLOSED / REVIEW_TRUNCATION_EXTENSION_REQUIRED`  
**Technický counter:** `7/10`  
**Fyzikálna hĺbka:** bez zmeny `60/100`

## 1. Čo sa ľudskou rečou počíta

Pokus 7 nemení fyziku pokusu 6. Rozdeľuje veľký výpočet na 45 malých,
samostatne auditovateľných atómov. Jeden atóm vezme jeden počiatočný mód,
jednu Fourierovu škálu `k` a jeden variant prenosu, vyrieši základný aj
rozšírený skorý rad a skontroluje nezávislé Einsteinove holdouty.

Atóm môže potvrdiť iba podmienenú `Phi1/M3-TCA0` konzistenciu. Nemôže potvrdiť
piatu silu, CDM recoil, finite opacity, plnú Boltzmannovu hierarchiu, CMB ani
`S8`. Ani úspešný agregátor si neudelí fyzikálny PASS; jeho čísla ešte osobitne
zaaudituje hlavný orchestrátor.

## 2. Zmrazené hashe

| artefakt | SHA-256 |
|---|---|
| physics base | `070F217B45A385369ECAFAA3D409A1210BAE3C3AF8A600A9171225B258751BF2` |
| atomic wrapper | `977082FF118645F8A7CD024EE6AE411D0F8995DA6F00552C0B53F19B520623F9` |
| runner 272 | `65AD56720AD06B32BE0EC54C2924491F1D8D9DB1C84E04015E56521B8FF8813D` |

## 3. Predbehové očakávania a rozhodovacie vetvy

### `py_compile`

- význam: iba syntax/import-independent byte-code kontrola wrappera a runnera;
- očakávanie: exit `0` do 10 s;
- PASS: pokračovať na `--help`;
- nonzero/timeout: technická chyba, zastaviť balík, fyzika `NOT_RUN`.

### `--help`

- význam: overiť spustiteľnosť CLI bez solve;
- očakávanie: exit `0`, voľby `--mode --k --variant --aggregate`;
- PASS: pokračovať na sentinel;
- nonzero/timeout: technická chyba, fyzika `NOT_RUN`.

### Sentinel `AD / k=0.05 / nominal`

- význam: prvý skutočný atóm; vyrieši primary aj `J+2` F0/M3 a holdouty;
- očakávanie: interný runtime `<4.8 s`, externý `<10 s`, všetky frozen checks
  true a atom status `PASS_M3_TCA0_SEED_CONDITIONAL_ATOM`;
- PASS: sentinel sa zachová ako 1/45 a pokračuje sa zvyšnými 44;
- exit `2`: numerický/formulačný REVIEW, zastaviť a auditovať čísla;
- exit `3`/timeout: technický pokus 7 zlyhal bez fyzikálneho verdiktu.

### Zvyšných 44 atómov

Po sentineli je deterministické poradie `mode = AD,CDI,BI,NID,NIV`, v každom
móde `k = 0.005,0.05,0.15`, v každom `variant = nominal,gamma0,af0`; už hotový
`AD/0.05/nominal` sa preskočí. Pred každým procesom sa v tejto evidencii
aktualizuje položka `NEXT_PROCESS`. Pri prvom nenulovom exit code sa ďalšie
atómy nespúšťajú.

### Agregátor

- očakávanie: nájde presne 45 immutable atómov, overí ich hashe, schémy,
  surfaces, prahy, štyri nominal-af0 bridge a 15 nominálnych backgroundov;
- technický úspech: `TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_NUMERICAL_AUDIT`;
- fyzikálny verdict zostáva `NONE_NOT_YET_AWARDED` až do hlavného auditu.

## 4. Procesný ledger

| fáza | stav | výsledok / dôkaz |
|---|---|---|
| static read-only physics audit | PASS_SCOPE_ONLY | rovnice nekopírované, frozen scope zachovaný |
| static read-only math/script audit | PASS_STATIC_ONLY | 45/45, four-bridge, JSON restore a fail-closed schéma overené |
| static documentation/release audit | PASS_AFTER_FIXES | release trigger žiadny; counter 6/10 |
| `py_compile` wrapper + runner | PASS | exit 0, wall 0.9 s; bez fyzikálneho významu |
| `--help` | PASS | exit 0, wall 1.0 s; frozen CLI potvrdené |
| sentinel AD/0.05/nominal | REVIEW | exit 2; technicky dobehol 2.047 s; iba J2/J4 tail FAIL |
| remaining atoms | `NOT_RUN_BY_PREREGISTERED_STOP` | 44 atómov sa úmyselne nespustilo |
| aggregate | `NOT_RUN_INCOMPLETE_SET` | 1/45, spustenie zakázané |
| orchestrator numerical audit | `REVIEW_TRUNCATION_EXTENSION_REQUIRED` | rovnice/ranky/holdouty PASS; support J2 príliš plytký |

`NEXT_PROCESS = NONE_IN_ATTEMPT_7`  
`RESULT = RUN_KMPC_028...AD_K0p05_NOMINAL.json`  
`RESULT_SHA256 = 2294E8623675B49F2D5A814005306D4E98E3CBDF4A1A66BD3AE1A9C0331EFC83`
`EXTERNAL_LIMIT = 10 s`

## 5. Release hranica

```text
NO_NEW_TRIGGER
EXISTING_PT1_REMAINS_OPEN
PT2_NOT_ESTABLISHED
```
