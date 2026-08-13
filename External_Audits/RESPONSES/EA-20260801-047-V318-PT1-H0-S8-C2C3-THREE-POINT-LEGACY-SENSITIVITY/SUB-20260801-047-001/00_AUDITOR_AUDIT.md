# External audit response — EA-047 / SUB-20260801-047-001

## Identifikácia

```text
TASK_ID: V318-PT1-H0-S8-EA047-EXTERNAL-T2-20260801
AUDITOR_TASK_ID: /root/v318_pt1_h0_s8_external_auditor
ROLE: external_auditor
MODEL: gpt-5.6-sol
REASONING_EFFORT: high
AUDIT_MODE: blind_T2_package_only
TIMESTAMP: 2026-08-01T11:33:30.3853596+02:00
TIMEZONE: Central Europe Standard Time / UTC+02:00
PACKAGE_ID: EA-20260801-047-V318-PT1-H0-S8-C2C3-THREE-POINT-LEGACY-SENSITIVITY
CHECKPOINT_ID: CP-RELEASE-V318-PT1-H0-S8-C2C3-20260801-001
PARENT_CHECKPOINT_IDS: NONE_FIRST_RELEASE_DIAGNOSTIC_CHECKPOINT
AUDIT_SUBMISSION_ID: SUB-20260801-047-001
CANONICAL_PACKAGE_MANIFEST_SHA256: 646D81CE21B6CF5CCC3E3125B3DFC10DFF3E54ECE947272C3892997DD459F6B7
```

## Nezáväzné odporúčanie

```text
RECOMMENDATION: AGREE_WITH_LIMITATION
HIGHEST_ACTUAL_TIER: T2_REPRODUCIBLE_CALCULATION
PACKAGE_MANIFEST: PASS
PACKAGE_DECLARED_ALL_19_EXACT_PARITY: FAIL_P0_CONTROL_ONLY
RESULT_CLASSIFICATION: NONE_OF_FIVE_ACCEPTED_CONDITIONAL_DIAGNOSTIC
AUTHORITATIVE_STATE_CHANGE: none
```

`T2_REPRODUCIBLE_CALCULATION` bolo dosiahnuté pre deväť finálnych grid
buniek cez deklarovaný runner bez obídenia guardov. Prísnejšia požiadavka
balíka, aby sa aj deväť continuation rawov rovnalo prijatým kópiám po
odstránení iba top-level `runtime_seconds`, nie je splniteľná: čerstvé
runtime-dependent file hashe sa správne vkladajú downstream. Ide o finding
`EA047-EXT-P0-001` bez dosahu na vedecké tvrdenie.

## Package closure a oddelenie rolí

`[OBSERVED_IN_PRIMARY]`

- Všetky štyri bootstrap artefakty sedeli so sealed charterom:

```text
EVIDENCE/001__AGENTS.md = 472F31C5CAE790EFA16A815BE3183B7A2C1438E4961B2BE4A16AEAE0FF57BA72
EVIDENCE/002__PROJECT_OPERATING_SYSTEM.md = 45CDDF6CBD458CC8C18147C438557143E1EB962BB159058070A8CAA7E866921E
EVIDENCE/003__AUDITOR_PACKAGE_PROTOCOL_R8.md = F0F8DB2F7A63666709CCC77E92B80C95F895752E3A16DDF62AA77B0D1D96279C
EVIDENCE/004__EXTERNAL_AUDITOR_ROLE.toml = 98E55F94679F49D4DCE08E3281AE2A38F899B896E25726F9A3C2A85A9FC997E3
```

- Manifest prešiel `36/36`; package mal `39` súborov, `29` evidence,
  runtime mapu `2/2`, bez hash driftu, duplicít, temp súborov alebo
  nemapovaných REPRO dependencies.
- Curator/autor `/root` a auditor
  `/root/v318_pt1_h0_s8_external_auditor` sú odlišné identity.
- Package inventory SHA pred aj po audite bol
  `42909B0805B9EDDAAA4791FFE375A80A7846DE60606F1B67745EAB34D3DC1644`.
- Fresh-copy RC hashe ostali:
  runner `89C12064BA72ADB70C443DD14B0A64B5139314D8AB996A9FB2C63E7F6F4B6FF3`,
  base `74AE3B0BC31FA1AE4BB9FDB3339C84869DA38131440795BD0C7B2B82677F30D9`.

## Prostredie

```text
OS: Windows-10-10.0.26200-SP0
ARCHITECTURE: AMD64 / x86_64 little-endian
CPU: Intel64 Family 6 Model 141 Stepping 1
PYTHON: CPython 3.11.3, MSC v.1934, 64-bit
EXECUTABLE: C:\Python311\python.exe
NUMPY: 2.4.4
SCIPY: 1.17.1
BLAS/LAPACK: scipy-openblas 0.3.31.188.0
OPENBLAS: USE64BITINT, DYNAMIC_ARCH, Haswell, MAX_THREADS=24
```

Prostredie sa presne zhodovalo so zmrazenými verziami Python/NumPy/SciPy.

## Execution record

Každý Python proces mal vonkajší limit `60 s`; package vnútorné limity sa
nemenili.

| Príkaz/vetva | Exit | Wall s | Generated output SHA-256 |
|---|---:|---:|---|
| `py_compile` base + runner | 0 | 0.1223 | pyc `F492E050…E498`, `05584445…7968` |
| `runner --help` | 0 | 0.8218 | stdout `199C4FE5…7F0D` |
| `runner --self-test --max-runtime-seconds 45` | 0 | 0.8030 | stdout `74DE95F5…9A3`; `31/31` |
| direct `null-n2000` | 0 | 27.4207 | `72AEBE55…3A4D` |
| direct `null-n4000` | 0 | 41.0985 | `CE089342…BFAF` |
| direct `half-n2000` | 0 | 16.8330 | `DAC7F7F1…A248` |
| direct `half-n4000` | 0 | 33.4289 | `747E2D43…1279` |
| direct `full-n2000` | 0 | 17.4232 | `4FEB55CE…057A` |
| direct `full-n4000` | 0 | 41.9918 | `446BB8A5…C089` |
| n8000 reference | 0 | 12.1035 | `639017C3…DAFC` |
| null A / B / C | 0/0/0 | 24.1567 / 21.0659 / 18.4021 | `EE0C2766…D61C` / `5E315401…39DB` / `D4EA9406…B241` |
| null aggregate | 0 | 0.7684 | `0D0D9352…3850` |
| half A / B / C | 0/0/0 | 23.3583 / 20.2802 / 17.8513 | `C6D41341…CF8A` / `E5862C2B…338B` / `BAEF1649…D464` |
| half aggregate | 0 | 0.7582 | `67B1218B…66A` |
| full A / B / C | 0/0/0 | 22.4057 / 18.3088 / 17.5599 | `A02DC507…82F9` / `E191092D…477A` / `EF3ED25D…A123` |
| full aggregate | 0 | 0.7572 | `DE86BBD8…F06D` |

Presné fresh reference/predecessor hashe boli odovzdané nasledujúcim
príkazom; žiadny prijatý raw nebol vložený do fresh copy.

### Negatívny collision guard

`[INDEPENDENTLY_RECOMPUTED]` V oddelenej fresh copy bol na cieli
`null-n2000` prázdny sentinel. Exact official príkaz skončil pred výpočtom
s exit `1` za `0.9953 s`; sentinel SHA ostal
`E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855`
a temp files boli `0`. Guard prešiel.

## Reprodukcia a parita

`[INDEPENDENTLY_RECOMPUTED]` Po odstránení iba top-level
`runtime_seconds`:

- reference raw: exact recursive equality;
- všetkých 9 finálnych grid-cell rawov: exact recursive equality;
- 6 direct cells: exact equality;
- 3 n8000 aggregate rawy: byte-identické aj bez normalizácie;
- 9 continuation rawov: rozdiel iba vo fresh-chain provenance hashoch.

Každý A raw sa líšil iba v `reference_stage_sha256`; každý B a C raw iba v
`reference_stage_sha256` a `predecessor_segment_sha256`. Žiadne fyzikálne
číslo, bisection state, guard, iteration count, schema, frozen input,
identity, threshold alebo verdict sa nelíšili.

## Matematický a numerický audit

`[OBSERVED_IN_PRIMARY] [INDEPENDENTLY_RECOMPUTED]`

- Radiation/sound horizon používajú deklarované `omega_r`, baryon loading a
  kladné flat-reference `omega_L`.
- Fuel/matter transfer sa algebraicky ruší v `F′+M′+R′`.
- Distance používa `c/(100h) ∫e^-x/E dx`.
- Segmented bisection zachováva exact midpoint operation order.
- Growth používa `d ln E/dx=(-3δF-3M-4R)/(2E²)`.
- `sigma8=0.811 D_model/D_LCDM` a
  `S8=sigma8 sqrt(Omega_m0/0.3)`.
- Nezávislá binary64 kontrola dala nulový rozdiel pre `sigma8`, `S8` a
  angular residual vo všetkých 9 cells.
- Všetky segmented chains: `A=10`, `B=20`, `C=29`; fresh reference aj
  predecessor hash chain PASS; final width
  `4.656612873077393e-10 <= 5e-10`.

| Shard | `abs(H0_8000-H0_4000)` | `abs(S8_8000-S8_4000)` | Stav |
|---|---:|---:|---|
| null | `0.0003053806722164154` | `2.9953878236677056e-6` | PASS |
| half | `0.00030659139156341553` | `2.972272435952661e-6` | PASS |
| full | `0.00030780211091041565` | `2.949411137875835e-6` | PASS |

Reprodukované n8000 body:

```text
DeltaNeff=0       H0=65.79213819466531  S8=0.8856095825403126
DeltaNeff=0.02675 H0=66.08320294879377  S8=0.8800254370658636
DeltaNeff=0.0535  H0=66.37433224357665  S8=0.874499891729803
```

Endpoint binary64:

```text
Delta H0 = 0.5821940489113331; declared display = 0.582194048911333
Delta S8 = -0.01110969081050961; declared display = -0.0111096908105096
```

Oba prahy tabuľkovej materiality prešli. Nejde o štatistickú významnosť.

## Material finding EA047-EXT-P0-001

```text
FINDING_CLASS: P0_PACKAGE_PROCESS_ONLY
CLAIM_REACH: NONE
EARLIEST_POSSIBLY_INVALID_CHECKPOINT_ID: NONE
EARLIEST_AFFECTED_ARTIFACT: package controls 02/03
KNOWN_DOWNSTREAM_CLAIMS: unqualified EA-047 all-19 exact-parity acceptance only
SMALLEST_WORKFLOW_RETURN_POINT: PACKAGE_CONTROL_REPAIR_REVISION
TRACK_IDENTITY_IMPLICATION: NONE
```

Fresh reference sa od accepted líši iba v povolenom `runtime_seconds`, tým
sa však zmení whole-file SHA, ktorý runner správne vloží do A/B/C. Preto
continuation rawy nemôžu byť exact rovnaké s historickými rawmi a zároveň
použiť skutočne fresh súbory, zachovať exact SHA chain a normalizovať iba
top-level runtime.

- Matematický/logický dopad: žiadny na rovnice alebo čísla; nesprávne je iba
  package tvrdenie o exact parite provenance polí.
- Fyzikálny dopad: žiadny; 9 final cells, guardy, konvergencia, comparators
  a endpoint sa reprodukovali.
- Identita koľaje: bez dopadu.

Najmenšia oprava je control-only package revision: fresh continuation chain
sa má kontrolovať interne voči fresh hashom; accepted-copy exact parita sa
má požadovať iba pre stabilné vedecké/final polia. DEV, RC, project official
ani internal-science rerun netreba. Nový submission má auditovať iba túto
control opravu.

## Odchýlky a auditor harness

```text
DECLARED_DEVIATIONS_FROM_SEALED_REPRODUCTION: NONE
NETWORK: not used
LIVE_PROJECT_READS: none
SIBLING_RESPONSES_READ: none
PACKAGE_EDITS: none
PROJECT_FILES_CHANGED: 0
```

Dve nemateriálne read-only chyby auditorovho harnessu boli opravené:
PowerShell recursive-diff parser error pred porovnaním a použitie
rezervovaného `$null` v prvom endpoint summary. Obe vetvy boli zahodené a
znovu spočítané; nedosiahli package, RC, rawy, guardy ani claim.

## Physical scope a nonclaims

`[OBSERVED_IN_PRIMARY] [INDEPENDENTLY_RECOMPUTED]`

- Presne tri diskrétne conditional legacy-anchor sensitivity body.
- Nie likelihood, posterior, fit, interval ani continuous envelope.
- Nie aktuálne tvrdé v3.18 predikcie `H0` alebo `S8`.
- `H0` je podmienené syntetickou kotvou `h_ref=0.673`.
- `S8` používa simplified growth a `sigma8_LCDM=0.811`; nejde o G9.
- `Delta N_eff=0` vypína iba legacy steam; nie je ΛCDM ani mechanism-off.
- Žiadne P5.4, G8, G9, covariance, gauge, causality, stability, A2-K4, A1,
  score, depth alebo release closure.

Externý auditor je iba poradný a nemení autoritatívny projektový stav.

## Signed identity addendum

```text
ADDENDUM_CLASS: P0_RESPONSE_IDENTITY_CORRECTION_ONLY
INCORRECT_TASK_ID: V318-PT1-H0-S8-C1-20260730
CORRECT_TASK_ID: V318-PT1-H0-S8-EA047-EXTERNAL-T2-20260801
AUDITOR_TASK_ID: /root/v318_pt1_h0_s8_external_auditor
SIGNED_BY: external_auditor / gpt-5.6-sol
NEW_READS: 0
NEW_RUNS: 0
FILES_CHANGED: 0
```

Nesprávny task ID bol zdedený typografický prepis z package V1 contractu.
Nemal vplyv na autorizáciu, scope, izoláciu, príkazy, evidence, hashe,
finding, tier ani odporúčanie. Ostatné identity a výsledky ostávajú
nezmenené.
