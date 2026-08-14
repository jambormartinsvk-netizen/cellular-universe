# P5.3g7-M3-FULL/R-A — pokus 9/10, J8 residual provenance a jedna korekcia

**Dátum:** 2026-07-16  
**Run ID:** `KMPC-030`  
**Stav:** `ATTEMPT_9_PREREGISTERED / NOT_RUN`  
**Scope:** `AD / k=0.05 / nominal / Phi1 M3-TCA0 / J8`  
**K4:** `LIVE / 60/100`

## 1. Otázka

Je jediný J8 driver residual `1.5577e-10` na `fuel_Euler[8]` numerická chyba
square solve/equilibrácie, alebo pretrvá aj po jednej vopred určenej residual
korekcii?

Immutable vstupy:

| stav | SHA-256 |
|---|---|
| J4 KMPC-028 | `2294E8623675B49F2D5A814005306D4E98E3CBDF4A1A66BD3AE1A9C0331EFC83` |
| J6 KMPC-029 | `658495A11A3C72262CDCBEC9B9515794E506A6C7F14F40865704AA26E6C4636A` |
| J8 KMPC-029 REVIEW | `1EE3FCDF3B77C6C7E4C26317A3F39AA45D4CFA5BA6B559E312E598BC3ED51AB8` |

## 2. Čo sa nesmie zmeniť

- physics base hash `070F217B45A385369ECAFAA3D409A1210BAE3C3AF8A600A9171225B258751BF2`;
- attempt-8 generalized-M1/shape wrapper hash
  `934AE0E9663A6D8CFD92DE2843E59D7A94065D277227EECC73F9B6646B6EE475`;
- M1 order 8, F0/M3 support `0..8`, 117 M3 unknowns/driver rows;
- rovnice, state/driver/holdout, pressure, B1, TCA0, gauge a scope;
- driver `1e-10`, holdout `1e-9`, absolute `1e-12`, coefficient drift
  `1e-8`, rcond/rank a tail `1e-6`;
- iba float64; žiadny nový fit, parameter alebo vyššia presnosť.

## 3. Povolená numerická operácia

Nový wrapper smie dočasne zachytiť iba technické funkcie `_affine_system`,
`_solve_equilibrated` a `_holdout_metrics` počas jedného M3 J8 solve. Tretí hook
zachytáva skutočné ordered holdout labels, nemení výpočet metriky. F0 zostane na
frozen solveri. Všetky funkcie a shape guards sa musia obnoviť v `finally`.

Frozen solver najprv vytvorí pôvodné riešenie. Z tej istej zachytenej
ekvilibrovanej matice sa potom vykoná **presne jedna** korekcia:

```text
r_y = b_eq - A_eq y_0
Delta y = solve(A_eq, r_y)
y_1 = y_0 + Delta y
x_1 = y_1 / column_scale
```

Žiadna druhá iterácia, zmena rcond, solver drivera alebo tolerancie nie je
dovolená.

## 4. Povinná residual provenance

Pre všetkých 117 driver rows sa exportuje signed residual, absolute residual,
term norm, ratio, row scale a branch relative/absolute. Pre najhorší pôvodný
row `fuel_Euler[8]` sa navyše exportuje constant a všetkých 117 affine
príspevkov s menom `state[power]`.

Rovnaký residual sa vyhodnotí dvoma cestami:

1. `matrix @ x + constant`;
2. priamym opätovným volaním zachyteného frozen ledgeru.

Ich maximum absolute difference musí byť `<=1e-12`. Obe priame residual cesty
navyše musia samostatne prejsť rovnakou relative/absolute branch metrikou ako
affine cesta. Tým sa oddelí chyba affine extraction od square solve.

## 5. Brány jednej korekcie

1. originálna reprodukcia koeficientov voči immutable J8: relative `<=1e-8`,
   absolute `<=1e-12`;
2. correction count presne `1`, všetko finite;
3. refined driver `<=1e-10` a absolute fallback `<=1e-12`;
4. refined nezávislý holdout `<=1e-9` a absolute fallback `<=1e-12`;
5. original-vs-refined coefficient drift `<=1e-8` / `<=1e-12`;
6. rank 117/117 a equilibrated singular ratio `>=1e-10`;
7. B1/TCA0/contract/forbidden/regularity a všetky temporary restorations PASS.
8. zachytené driver/holdout matice majú presné rozmery `117x117` a `18x117`,
   presné ordered labels a solver dostal identickú driver maticu;
9. pôvodný immutable incident sa musí reprodukovať ako `fuel_Euler[8]`,
   `pass_driver=false` a maximum sa musí zhodovať s immutable J8 s technickou
   reprodukčnou toleranciou `rtol=1e-12`, `atol=1e-18`;
10. opravený stav musí osobitne prejsť forbidden-layer `<=1e-10` a
    `U_c` lower-regularity `<=1e-12`.

## 6. Ladder closure bez ďalšieho solve

Wrapper načíta frozen J4/J6 a refined J8 a s pôvodnými prahmi vypočíta F0 aj
M3 common coefficient bridges, per-state J4/J6 a J6/J8 tail, exact added powers,
dominant-power membership a monotonicitu. Ak neprejde časť 5, tieto hodnoty sú
iba diagnostické a nesmú vytvoriť kandidáta. Kandidát po PASS časti 5 je:

- oba tails PASS: `CANDIDATE_J4_PRODUCTION_ADEQUATE`;
- iba J6/refined-J8 PASS: `CANDIDATE_J6_MINIMUM_PRODUCTION_SUPPORT`;
- inak: `REVIEW_LADDER_STILL_UNCLOSED`.

Tieto texty nie sú autoritatívny verdict. Ten udeľuje hlavný orchestrátor po
audite JSON.

## 7. Vopred zmrazené vetvy

### Numerický pôvod potvrdený

Jedna korekcia prejde driver/holdout/drift a direct-ledger kontrolu:

```text
TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT
PHYSICS_VERDICT=NONE_NOT_YET_AWARDED
```

### Neuzavreté

Ktorákoľvek brána neprejde:

```text
REVIEW_J8_RESIDUAL_PERSISTS_OR_PROVENANCE_UNCLOSED
```

Bez druhej korekcie a bez automatického fyzikálneho STOP.

### Technická chyba

Syntax, timeout, capture, restoration, serializácia alebo storage:

```text
ATTEMPT_9_TECHNICAL_FAILURE
PHYSICS_VERDICT=NONE
```

## 8. Proces a limity

```text
py_compile(wrapper) -> py_compile(runner) -> --help -> one audit process
```

Audit má interný limit `4.8 s`, každý Python proces externý `10 s`. Immutable
výsledok je
`RUN_KMPC_030_P5_3G7_M3_FULL_RA_J8_ONE_REFINEMENT_AUDIT.json`; presný failure
názov je
`RUN_KMPC_030_P5_3G7_M3_FULL_RA_J8_ONE_REFINEMENT_AUDIT_TECHNICAL_FAILURE.json`.
Runner nepovoľuje alternatívny output názov. Zlyhanie ešte pred načítaním alebo
zápisom môže zanechať iba procesový log bez JSON; nejde o fyzikálny výsledok.

## 9. Release

```text
NO_NEW_TRIGGER
EXISTING_PT1_REMAINS_OPEN
PT2_NOT_ESTABLISHED
```

## 10. Hash freeze po troch read-only auditoch

Statické posudky physics-track, math-script a documentation-release auditora
nenašli po oprave holdout proveniencie false-PASS blocker. Autoritatívny runtime
výsledok ešte nebol udelený.

| artefakt | SHA-256 |
|---|---|
| `full_ra_m3_seed_attempt9_refinement.py` | `A8E2EA26B6960F23298259EFBECFFC9806ECF10F0207AE4D2B2AD0C2713DA0AB` |
| `274_script_KMPC_030_P5_3g7_m3_full_ra_j8_refinement_attempt9.py` | `81D777534C552DC14E12807814FA63446807C1243B228EAFEE997F9D76B816FD` |

Wrapper je hash-frozen v runneri. Ďalšia zmena ktoréhokoľvek Python súboru ruší
túto preregistráciu a vyžaduje nový hash freeze pred spustením.
