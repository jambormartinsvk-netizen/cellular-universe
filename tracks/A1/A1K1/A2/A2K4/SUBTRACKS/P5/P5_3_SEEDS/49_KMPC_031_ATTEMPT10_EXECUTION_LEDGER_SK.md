# KMPC-031 — procesový ledger pokusu 10/10

**Dátum:** 2026-07-16  
**Stav pred procesom 1:** `PREREGISTERED / HASH_FROZEN / NOT_RUN`  
**Fyzikálny stav:** `NONE_NOT_YET_AWARDED`  
**K4:** `LIVE / 60/100`  
**Technické počítadlo pred behom:** `9/10`

## Ľudský význam

Nevytvára sa nový seed a nerieši sa žiadna rovnica. Z nemenných J4, J6 a
refined-J8 koeficientov sa pre každý stav rozdelí starý rozdiel na drift už
spoločných koeficientov a na skutočný príspevok nových powers. Added tail sa
spočíta priamo, aby nevznikol odčítaním dvoch takmer rovnakých čísel.

Očakávame, že raw FAIL ostane reprodukovaný, common bridge ostane PASS a
explicitné tails prejdú pôvodným `1e-6/1e-12` pravidlom. Ak nie, ARCH-A sa
uzavrie REVIEW na 10/10; K4 tým nezomiera.

## Proces 1 — compile wrappera

**Stav:** `PASS / exit 0 / 1.0 s`  
**Očakávanie:** exit `0` bez výstupu do `10 s`.  
**PASS:** zapísať výsledok a otvoriť proces 2.  
**STOP:** syntax je technická chyba pokusu 10 a znamená
`ARCH_A_TECHNICAL_STOP_10_OF_10`, nie fyzikálny FAIL.

## Proces 2 — compile runnera

**Stav:** `PASS / exit 0 / 0.8 s`  
**Očakávanie:** exit `0` bez výstupu do `10 s`.

## Proces 3 — help runnera

**Stav:** `PASS / exit 0 / 0.9 s / canonical CLI confirmed`  
**Očakávanie:** exit `0` do `10 s`; iba `--max-runtime-seconds` a `--audit`,
bez `--output`.

## Proces 4 — no-solve audit

**Stav:** `TECHNICAL_COMPLETE / exit 0 / payload 0.016 s / process 2.3 s`  
**Interný limit:** `4.8 s`; **vonkajší limit:** `10 s`.  
**Očakávanie:** raw J4/J6 `1.2308e-5` a J6/J8 `3.3632e-6` zostanú FAIL
diagnostikou; direct added tails približne `4.67e-8` a `5.18e-14` na
`z=1e-2` a oveľa menšie na `z=1e-4`, všetky PASS a monotónne.

**PASS vetva:** iba kandidát
`CANDIDATE_SUPPORT_TRUNCATION_CLOSED_J4_SENTINEL_SCOPE`, následne audit JSON.  
**REVIEW vetva:** `REVIEW_SUPPORT_TAIL_UNCLOSED`; bez ďalšieho technického
pokus-u v ARCH-A.  
**Technický STOP:** exception/timeout/hash/storage/syntax s presným dôvodom;
K4 zostáva `REVIEW_TECHNICAL_UNRESOLVED`, nie mŕtva.

Úspešný immutable názov:
`RUN_KMPC_031_P5_3G7_M3_FULL_RA_DEEP_TAIL_BRANCH_PROVENANCE.json`.  
Failure názov:
`RUN_KMPC_031_P5_3G7_M3_FULL_RA_DEEP_TAIL_BRANCH_PROVENANCE_TECHNICAL_FAILURE.json`.
Runner nepovoľuje alternatívny output. Chyba ešte pred CLI parse alebo pred
zápisom môže zanechať iba procesový log bez failure JSON.

## Release

```text
NO_NEW_TRIGGER
EXISTING_PT1_REMAINS_OPEN
PT2_NOT_ESTABLISHED
```

## Frozen artefakty

| artefakt | SHA-256 |
|---|---|
| wrapper | `A7C06D4C16AF5429319DFF307ADB4A2FCF72542AA65E92B1D6EA1B229387CA55` |
| runner | `A222F96EEAF32042CCAE634FB71EE1794119704D83B26BC30D83B358568C15B2` |

## Výsledok pred autoritatívnym auditom

Výstup:
`RUN_KMPC_031_P5_3G7_M3_FULL_RA_DEEP_TAIL_BRANCH_PROVENANCE.json`  
SHA-256:
`C547F818E3918CD844CA06BEA32814279A9D4A20D662A9166114410645792FF6`

- všetky checks sú `true`; raw J4/J6 aj J6/J8 FAIL sa zachovali;
- J4→J6 explicitný tail: `4.66448e-14` pri `z=1e-4` a `4.66857e-8`
  pri `z=1e-2`, oba PASS;
- J6→J8 explicitný tail: `5.16515e-24` a `5.17916e-14`, oba PASS;
- J8 tail je na oboch plochách menší než J6 tail;
- forbidden maxima J4/J6/J8 sú `6.54e-16 / 7.62e-16 / 5.92e-16`,
  hlboko pod `1e-10`; stored forbidden a `U_c` regularity guards sú PASS;
- F0 aj M3 common bridges sú PASS a no-solve source checks sú PASS.

Automatický text je iba
`CANDIDATE_SUPPORT_TRUNCATION_CLOSED_J4_SENTINEL_SCOPE`. Hlavný orchestrátor
musí ešte auditovať JSON; nesmie sa z neho urobiť celý P5.3 alebo K4 PASS.

## Autoritatívny rozsudok hlavného orchestrátora

```text
PASS_SUPPORT_TRUNCATION_J4_SENTINEL_SCOPE
ARCH_A_COMPLETED_AT_10_OF_10
K4 = LIVE / 60/100
P5 = 3.5/6
SCORE_EFFECT = NONE
```

Rozsudok platí iba pre conditional `Phi1 M3-TCA0 AD/k=.05/nominal` a dve
predregistrované z-plochy. Raw full-state tail ostáva
`MIXED_COMMON_DRIFT_PLUS_ADDED_TAIL_DIAGNOSTIC`; nebol spätne premenovaný.
Celý P5.3, ostatné módy/k/varianty, S1, P5.4, G8, CMB a S8 zostávajú otvorené.
