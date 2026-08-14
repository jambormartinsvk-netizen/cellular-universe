# Externý audit — `EA-20260727-046-Q1R6-SUPPORTED-AUDITOR-CLOSURE`

## Povinné metadáta

- `TASK_ID`: `A2K4-Q1R6-EA046-EXTERNAL-AUDIT-20260727-280`
- Auditor/task identity: `/root/q1r6_ea046_external_auditor_v2`
- Rola: `external_auditor`
- Auditor/model/verzia: `OpenAI Codex / gpt-5.6-sol / high`
- Role config SHA-256: `26DEF062FB7D5034194CC6326D1E2D5128CB5E657328410DFA80781418A4A2F6`
- Dátum a časová zóna: `2026-07-28T09:44:46.5679007+02:00`, `Central Europe Standard Time` (`Europe/Bratislava`)
- Audit mode: `FORENSIC / PACKAGE-ONLY STATIC T1`
- Package revision: `SEALED_READY_FOR_AUDIT / NOT_SENT`
- Strojový manifest SHA-256: `35331C185E9FC398E5835939C937B6475C3D945ADF68D25E891F4E1B11C5A0C9`
- Ľudský manifest SHA-256: `3ABA970F2396FD0E19DFDFC1BA92564FB2BD15A51400C656BCE98177CF3CEF5C`
- Overenie manifestu/rulesetu: `PASS`
- Najvyššia dosiahnutá úroveň: `T1_PRIMARY_FORMULA / STATIC_REFERENCE_INTERFACE_SCOPE`
- Oficiálna vetva bez odchýlky: `NOT_RUN`
- Deklarované odchýlky: `NONE`
- Protokolová klasifikácia výsledku: `NONE_OF_FIVE_STATIC_REFERENCE_SCOPE`
- Neautoritatívne odporúčanie: `AGREE_WITH_LIMITATION`

`NONE_OF_FIVE_STATIC_REFERENCE_SCOPE` je správna klasifikácia, pretože tento
balík poskytuje iba statickú primárnu formula/reference kontrolu. Nevykonal
sa precheck vylučujúci kandidáta, úplný fyzikálny alebo observačný test,
benchmark mismatch ani technicky zlyhaný run. Preto nejde o
`PRECHECK_EXCLUDED_SCOPE`, `COMPUTED_STOP_SCOPE`,
`OBSERVATIONAL_STOP_SCOPE`, `REFERENCE_MISMATCH_ONLY` ani `TECHNICAL_STOP`.

## Ruleset, manifest a oddelenie povinností

Všetky charterové a manifestované copy hashe prešli. Package-local role
config má SHA-256
`26DEF062FB7D5034194CC6326D1E2D5128CB5E657328410DFA80781418A4A2F6`,
rovnaký hash je v charteri aj pribalenom rolovom manifeste a profil určuje
`gpt-5.6-sol / high`.

```text
ARTIFACT_AUTHOR_TASK_ID=/root
STATIC_AUDITOR_TASK_ID=/root/c01_q1r3_access_prereg_audit
INTERNAL_AUDITOR_TASK_ID=/root/c01_q1r3_access_result_audit
PACKAGE_CURATOR_TASK_ID=/root/q1r6_ea045_curator
EXTERNAL_AUDITOR_TASK_ID=/root/q1r6_ea046_external_auditor_v2
curator != external auditor: PASS
curator != author: PASS
author != static auditor: PASS
author != internal auditor: PASS
SEPARATION_OF_DUTIES_CHECK=PASS
```

Balík obsahuje 16 súborov: 7 controls a 9 evidence. Strojový manifest má
10 riadkov (package-generated scope + 9 evidence), všetky copy hashe sedia,
duplicitné hash skupiny sú 0, temp súbory 0, `REPRO=0`, runtime rows 0.
Response scaffold pred zápisom sedel s očakávaným SHA-256
`353311B34E90946F3CEDBA1AC4DFD70DD337B425742EBF43CC90FE2647808A1C`.

## Prostredie

- OS: `Microsoft Windows 10.0.26200`
- OS architektúra / process architektúra: `X64 / X64`
- PowerShell: `7.6.3`
- Python: `NOT_RUN / NOT_PROBED`
- NumPy: `NOT_APPLICABLE`
- SciPy/SymPy: `NOT_APPLICABLE`
- BLAS/LAPACK: `NOT_APPLICABLE`
- Network: `0`
- Solver: `0`
- Generated JSON: `0`

## Procesný ledger

Všetky príkazy boli spustené iba nad sealed package; stdout sa nepoužil ako
nový vedecký artefakt a nevznikol generated output súbor.

| Fáza | Presný príkaz | Exit | Wall | Výstup/hash | Stav |
|---|---|---:|---:|---|---|
| archive hash | `Get-FileHash -Algorithm SHA256 -LiteralPath .\EVIDENCE\002__Q1R6_ARXIV_SOURCE.tar.gz` | 0 | 0.9 s | `5CE87BF1E5D9CF0D170439D14EA4F1A6898453799810F834E68E5A179C335416` | PASS |
| package inventory | `Get-ChildItem -LiteralPath . -Recurse -Force -File` | 0 | 1.0 s | 16 package files, 9 evidence | PASS |
| archive inventory | `tar -tzf .\EVIDENCE\002__Q1R6_ARXIV_SOURCE.tar.gz` | 0 | 0.9 s | 11 entries | PASS |
| primary stdout | `tar -xOf .\EVIDENCE\002__Q1R6_ARXIV_SOURCE.tar.gz main.tex` | 0 | 0.9 s | stdout only; independently recomputed `main.tex` SHA below | PASS |
| manifest/control/static inventory | package-local PowerShell `Get-FileHash`, `Import-Csv`, recursive file/hash grouping, temp and `REPRO` inventory | 0 | 1.1 s | all 10 manifest rows PASS; controls PASS; duplicates 0; temp 0; `REPRO=0` | PASS |
| archive-entry hash recomputation | package-local `.NET System.Formats.Tar.TarReader` + `SHA256.ComputeHash(entry.DataStream)` | 0 | 1.0 s | 11/11 lengths and SHA-256 equal receipt accounting | PASS |
| content classifier recomputation | package-local `TarReader`, PDF magic, strict UTF-8, raw-control, Unicode-control and byte-roundtrip checks | 0 | 2.1 s | 7 `BINARY_NON_TEXT`, 4 `READABLE_TEXT`, 0 ambiguous/fail | PASS |
| exact required-symbol search | `tar -xOf ... main.tex` + `Select-String` for `Z_rec`, `W_rec`, `P_rec`, `W_*`, `R_reset`, `dmu_cell`, `u_cell`, congruence/worldtube, source-off, reset, first-passage, stored/dissipated/ledger | 0 | 1.0 s | 0 matches for every searched W10 object/construct | PASS |
| include closure | `tar -xOf ... main.tex` + `Select-String` for `input/include/includegraphics/bibliography/bibliographystyle` | 0 | 1.0 s | all six graphics plus `ref.bib` and `utphys.bst` exist in the 11-entry archive; only `input` is commented | PASS |
| formula lines 80–170, 174–270, 350–480, 490–512, 695–725 | package-local `tar -xOf ... main.tex` followed by numbered bounded PowerShell ranges | 0 | 0.9 s | stdout only | PASS |
| formula lines 218–270 | package-local `tar -xOf ... main.tex` followed by numbered bounded PowerShell range | 0 | 0.9 s | stdout only | PASS |
| formula lines 350–450 | package-local `tar -xOf ... main.tex` followed by numbered bounded PowerShell range | 0 | 1.1 s | stdout only | PASS |
| title/author/ID search | package-local `tar -xOf` over text entries + `Select-String` | 0 | 1.2 s | title/authors found; literal `2204.13120` absent | LIMITATION F-001 |
| package-local documentary provenance search | `rg -n -i "2204\.13120|arxiv|source_id|download|url|provenance"` over charter, manifest and evidence 001/003/004 | 0 | 0.9 s | ID occurs only in charter; manifest labels archive by path/role | LIMITATION F-001 |
| environment | `[RuntimeInformation]::OSDescription/OSArchitecture/ProcessArchitecture; $PSVersionTable.PSVersion` | 0 | 0.9 s | Windows 10.0.26200, X64/X64, PS 7.6.3 | PASS |

Neexistoval `smoke`, `official audit`, Python, solver ani declared deviation.
Pre tieto fázy sú exit code, wall time a generated-output SHA-256
`NOT_RUN / NOT_APPLICABLE`.

Nezávisle prepočítané archive-entry SHA-256:

```text
Deltas.pdf=5492ADC2D56940E06472DE09132755D6782D5A22CE1673DD23BE180580DF3A86
error.pdf=60FE89778567AB8A649FC377F4A8BCCCF860F86B8B046F2DC980AF30A48B5811
fits.pdf=2E919564EF01836111C47C557D182D0D6BBDDA1FD0F4A26330D7EE74A2E6EB25
hist_alpha.pdf=BCC7CCABF9C6BBB472D5454E1984A281C56358E82C88617AD516421D9F4EDFD3
main.bbl=CA795F052AC4F5B1B112FC45AFD42858AC15DBA957FEEDF10B0C955E153DEEC6
main.tex=EB8E58F372E9EBCA6EF6AD8B26BB4EF80ED37A9BBB37D8AFB84C4671375AD791
pressure_defl.pdf=C754F73BD0E91F652C359D6A32E10553E2FBB5D2E81343B805E8727701FD6EC9
pressure_det.pdf=972E419424196EE40FFEBC5B901C5E82AF48DB5E30EFD0BE9A92DD70D49E19ED
ref.bib=25520A7602E18473A59BAC204B6B2CC114D1F82AD52D725D98EAB027C37C1432
scan.pdf=833021B950520B8ADE88DF215EEDFC140F9292FCAF2CB62FEB2B34B5E9044FA9
utphys.bst=58D9FCB341615E47A32B3E17A5F4C67DF3086867EA43EE7671147C3BEECEA78B
```

## Odpoveď na presnú otázku

Áno, s limitáciou F-001. Immutable archive, frozen preregistrácia, receipt a
result podporujú iba úzky záver, že ide o koherentný relativistický
scalar–plasma interface reference model. Primárny `main.tex` priamo obsahuje
Lorentz-invariantnú Boltzmannovu rovnicu a source term, scalar/plasma EMT,
total EMT conservation, scalar EOM, boundary conditions, nonlinear terminal
wall eigenvalue, benchmark scalar potential a pressure-balance klasifikáciu.
To je dostatočné pre reference-interface claim, nie pre W10 witness.

Complete W10 je správne odmietnutý. V primárnom zdroji nie sú `Z_rec`,
`W_rec`, nonnegative reservoir power `P_rec`, positive cycle-frozen `W_*`,
disjunktný conservation ledger, parent-cell `u_cell`/finite measure,
temporal first upward crossing, reset map ani source-off/event-off identita.
Existujúce EMT conservation, plasma flow, spatial wall profile, pressure
barrier a terminal condition `P_tot=0` nie sú týmito objektmi a ich
premapovanie by pridalo novú fyziku.

Mapovanie `S0/S10/S13=PASS` a `S1–S9/S11–S12=MISSING` je v tomto úzkom
scope správne. `S13` je process/mapping PASS: zdroj sám diskutuje numerické
fity, ale žiadny fit nebol použitý na vytvorenie W10 passportu.

## Overenie hlavných tvrdení

| Tvrdenie | Tag dôkazu | Primárny zdroj | Metóda | Výsledok |
|---|---|---|---|---|
| Archive je complete local universe podľa frozen classifiera | `INDEPENDENTLY_RECOMPUTED` | `EVIDENCE/002`, `EVIDENCE/003:1–50` | TarReader hash/length/type + magic/UTF-8/control/roundtrip + include closure | PASS: 11 regular entries, 7 binary PDF, 4 strict readable text, 0 gap/fail |
| Primárna identita podľa obsahu | `OBSERVED_IN_PRIMARY` | `main.tex:83–91` | direct tar stdout | `First principles determination of bubble wall velocity`, Benoit Laurent, James M. Cline |
| Koherentný relativistický scalar–plasma interface model | `OBSERVED_IN_PRIMARY` | `main.tex:121–168,174–267,356–449` | formula-line audit | PASS v reference-interface scope |
| Lorentz-invariant Boltzmann + source | `OBSERVED_IN_PRIMARY` | `main.tex:125–168`, Eq. `BE`, `BESimplified`, `source` | equation/sign/symbol inspection | PASS |
| Scalar/plasma EMT, total conservation a EOM | `OBSERVED_IN_PRIMARY` | `main.tex:174–247`, Eq. `EMTcons`, `EOM`, `EMT`, `EMTsimplified` | equation lineage inspection | PASS ako total interface conservation; nie disjunktný W10 ledger |
| Static terminal boundary/eigenvalue, nie temporal W10 event | `OBSERVED_IN_PRIMARY` | `main.tex:249–267` | boundary/eigenvalue inspection | supports reference model and blocks first-passage reinterpretation |
| Benchmark nie je úplná one-source closure | `OBSERVED_IN_PRIMARY` | `main.tex:360–380` | potential/species-scope inspection | loop/thermal corrections point external; OOE includes only top, others future work |
| Pressure nie je nonnegative reservoir work | `OBSERVED_IN_PRIMARY` | `main.tex:417–449` | moment/pressure inspection | `P_i` may accelerate either way; terminal solution uses `P_tot=0`; not `D_uW=P_rec>=0` |
| Required W10 symbols/constructs absent | `INDEPENDENTLY_RECOMPUTED` | whole `main.tex` | exact case-insensitive symbol/construct search | all searched counts 0 |
| No downstream target drives passport | `OBSERVED_IN_PRIMARY` | `main.tex:98–118,358,371–449` | motivation-vs-equation inspection | GW/baryogenesis are motivation/application, not W10 inputs |
| No Python/solver/network in this audit; prior reprocess says Python 0 | `INFERRED_FROM_PROJECT_DOCS` | `EVIDENCE/003:1–16`, `EVIDENCE/004:14–34` plus current command ledger | receipt/result + audit ledger | PASS in process scope; no T2 claim |

## W10 passport — nezávislé posúdenie

| Pole | Tag | Posúdenie | Dôvod |
|---|---|---|---|
| `Z_rec` | `OBSERVED_IN_PRIMARY` | `MISSING` | Source state `{phi_i,T,u_plasma,delta f_i}` exists, but no cumulative `W_rec=W[Z_rec]`. |
| `P_rec` | `OBSERVED_IN_PRIMARY` | `MISSING` | EMT flux/net wall pressure is not pointwise nonnegative reservoir power; terminal condition is zero net pressure. |
| `W_*` | `OBSERVED_IN_PRIMARY` | `MISSING` | Jouguet pressure barrier/latent heat is not a positive cycle-frozen delivered-work threshold. |
| conservation | `OBSERVED_IN_PRIMARY` | `MISSING` | Only total EMT conservation is source-exact; stored/dissipated/export/loss partition and residual-interface flow are absent. |
| `u_cell` | `OBSERVED_IN_PRIMARY` | `MISSING` | Plasma/wall four-velocity has no parent-cell genealogy semantics. |
| congruence/`dmu_cell` | `OBSERVED_IN_PRIMARY` | `MISSING` | Planar coordinate/spherical profile is not once-only parent worldtube plus finite invariant cell measure. |
| crossing | `OBSERVED_IN_PRIMARY` | `MISSING` | Spatial false-to-true profile and terminal eigenvalue are not an absolutely continuous temporal first upward threshold crossing. |
| `R_reset^Z` | `INDEPENDENTLY_RECOMPUTED` | `MISSING` | No reset construct; vacuum boundary transition does not define zero daughter credit/residual-energy bookkeeping. |
| source-off | `OBSERVED_IN_PRIMARY` | `MISSING` | With `delta f=0`, LTE wall equations/solutions remain; friction-off is not event-off. |
| noncircularity | `OBSERVED_IN_PRIMARY` | `DERIVED_SAME_MODEL / PASS_SCOPE_LIMITED` | Equations use scalar/plasma inputs; GW/baryogenesis are downstream motivation/application. |

## S0–S13

| Gate | Tag | Auditný výsledok | Scope dôvod |
|---|---|---|---|
| `S0` | `INDEPENDENTLY_RECOMPUTED` | `PASS_WITH_F001_ID_LIMITATION` | Complete 11-entry local universe, title/authors and primary formula source verified; remote numeric arXiv-ID binding is charter-only. |
| `S1` | `OBSERVED_IN_PRIMARY` | `MISSING` | External loop/thermal-potential reference and top-only OOE approximation prevent one-source complete closure. |
| `S2` | `OBSERVED_IN_PRIMARY` | `MISSING` | No local `Z_rec` carrying cumulative `W_rec`. |
| `S3` | `OBSERVED_IN_PRIMARY` | `MISSING` | No `D_uW=P_rec>=0` reservoir identity. |
| `S4` | `OBSERVED_IN_PRIMARY` | `MISSING` | No finite positive cycle-frozen delivered-work threshold. |
| `S5` | `OBSERVED_IN_PRIMARY` | `MISSING` | Total EMT conservation is not the required disjoint ledger/source-off identity. |
| `S6` | `OBSERVED_IN_PRIMARY` | `MISSING` | No parent-cell flow, once-only congruence/worldtube or finite invariant cell measure. |
| `S7` | `OBSERVED_IN_PRIMARY` | `MISSING` | Static spatial/terminal solution is not temporal first passage. |
| `S8` | `INDEPENDENTLY_RECOMPUTED` | `MISSING` | No physical reset map or daughter-credit rule. |
| `S9` | `OBSERVED_IN_PRIMARY` | `MISSING` | Lorentz covariance/conventions/convergence exist, but not full W10 causality, stability, orientation and units contract. |
| `S10` | `OBSERVED_IN_PRIMARY` | `PASS` | Downstream GW/baryogenesis are not passport inputs; no division/biology/H0/S8 target is imported. |
| `S11` | `INFERRED_FROM_PROJECT_DOCS` | `MISSING` | A single provisional `Y_div` would require adding the absent W10 objects/new physics. |
| `S12` | `OBSERVED_IN_PRIMARY` | `MISSING` | No W10 source-off/no-growth/no-event identity. |
| `S13` | `INFERRED_FROM_PROJECT_DOCS` | `PASS_SCOPE_LIMITED` | Reprocess/audit declare and exhibit no Python/network/solver/downstream run; no paper fit is imported into the W10 mapping; no score/depth/run change is claimed. |

## Nálezy

### F-001 — MINOR: remote arXiv-ID binding nie je package-lokálne preukázaný

- Typ: `DOCUMENTATION / PROVENANCE`
- Presný zdroj: `00_SCOPE_AND_READ_ORDER.md:40`, manifestový riadok
  `EVIDENCE/002`, `main.tex:83–85`.
- Pozorované: charter označuje source ako `2204.13120` a manifest ho mapuje
  na live názov `277A_..._ARXIV_SOURCE.tar.gz`; samotný sealed evidence však
  neobsahuje remote acquisition receipt alebo primárne metadata s literal
  `2204.13120`. `main.tex` priamo potvrdzuje titul a autorov.
- Očakávané: pri tvrdení exact remote ID má package obsahovať immutable
  package-local provenance record viažuci `2204.13120` na exact archive SHA.
- Dopad na package tier: neznižuje formula-content audit pod T1; obmedzuje
  iba nezávislé potvrdenie bibliografického numeric ID.
- Dopad na fyzikálny scope/verdict: žiadny na reference-only verzus
  incomplete-W10 rozlíšenie; preto `AGREE_WITH_LIMITATION`, nie
  `CANNOT_AUDIT`.
- Minimálny reprodukčný test: v budúcom successor package overiť sealed
  acquisition metadata/receipt s ID, URL/source operation a archive SHA.
- Navrhovaná oprava: sealed EA-046 nemeniť; ak je exact arXiv-ID binding
  rozhodujúci, vytvoriť nový package/addendum podľa protokolu.

Iné `CRITICAL`, `MATERIAL`, `MINOR` alebo `EDITORIAL` nálezy: `0`.

## Tier verzus projektový dopad

- Package tier: T1 je dosiahnutý pre formula lineage, rozmerovo/symbolickú
  interpretáciu a statickú kontrolu reference-interface scope.
- T2/T3: nedosiahnuté a nepožadované; chýba runner/runtime closure a žiadny
  official výpočet ani nezávislá implementácia sa nespustili.
- Projektový fyzikálny dopad: audit podporuje iba scoped reference model a
  odmietnutie complete W10. Nie je to project `PASS/REVIEW/STOP`, no-go ani
  zmena skóre, hĺbky alebo route.

## Nonclaims, procesy a súborový rozpočet

Tento audit netvrdí complete W10, C01/global no-go, `A_RW1` emptiness,
P5.3 closure, A3, computed/observational STOP, benchmark mismatch, dynamic
current/K4/P5 stav, event-ledger stav, physical witness attempt, score,
depth, run permission ani release promotion. Nevykonal Python, solver,
network, fit, S8, smoke, official alebo generated JSON.

```text
READ_SET_CONFIRMED=sealed package + exact response scaffold only
FILES_CHANGED=1 (00_AUDITOR_AUDIT.md only)
PYTHON_PROCESSES=0
NETWORK=0
SOLVER=0
LIVE_SCIENTIFIC_ARTIFACTS=0
LIVE_CENTRAL_REGISTERS_UPDATED=0
LIVE_FILES_CHANGED_TOTAL=0
AUDIT_PACKAGE_COPIES_CREATED_BY_AUDITOR=0
RESPONSE_FILES_UPDATED=1
PACKAGE_FILES_CHANGED=0
RUN_AUTHORIZED=false
```

## Neautoritatívne odporúčanie

`AGREE_WITH_LIMITATION`

Main orchestrator môže prijať úzky výsledok
`PASS_Q1R6_REFERENCE_INTERFACE_MODEL_ONLY /
REVIEW_Q1R6_NOT_A_COMPLETE_W10_WITNESS` ako podporený T1 static scope,
pričom F-001 sa zachová ako bibliografická provenance limitácia. Odporúčaný
next role je hlavný orchestrátor; tento auditor neprideľuje projektový
verdikt.

## Vyhlásenie autority

Tento externý posudok nemení projektový `PASS/REVIEW/STOP`, skóre, hĺbku,
`RUN_AUTHORIZED`, route, registre ani release. Autoritatívne spracovanie
vykonáva iba hlavný orchestrátor v novom súbore odpovede. Final response
SHA-256 sa po uložení reportuje orchestrátorovi v task handoffe; nie je
samoreferenčne zapisovaný do auditovaného súboru.
