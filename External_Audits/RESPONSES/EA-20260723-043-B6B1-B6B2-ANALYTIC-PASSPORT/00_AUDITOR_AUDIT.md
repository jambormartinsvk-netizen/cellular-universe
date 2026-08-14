# Externý audit EA-043 — B6b-1/B6b-2 analytický passport

## Identita, rozsah a autorita

```text
TASK_ID=A2K4-EA043-EXTERNAL-AUDIT-20260723-70
PACKAGE_ID=EA-20260723-043-B6B1-B6B2-ANALYTIC-PASSPORT
AUDITOR_TASK_ID=/root/ea043_external_auditor
ROLE=external_auditor
ROLE_CONFIG_SHA256=6B1AF6C55E725E7A2332F30F0337713F1A7E254402E7F8A5A64BB689569C9A14
MODEL=gpt-5.6
REASONING_EFFORT=high
DATE=2026-07-23
TIMEZONE=Europe/Bratislava
RECOMMENDATION=AGREE_WITH_LIMITATION
RUN_AUTHORIZED=false
```

Tento posudok je neautoritatívne T1 odporúčanie. Externý auditor nemení
projektové `PASS/REVIEW/STOP`, skóre, hĺbku, plán ani fyzikálny scope.
Hlavný orchestrátor je jediná autorita na prijatie, obmedzenie alebo
odmietnutie odporúčania.

## Bootstrap, identita a integrita

- `PACKAGE_CURATOR_TASK_ID=/root/ea043_package_curator` a
  `EXTERNAL_AUDITOR_TASK_ID=/root/ea043_external_auditor` sú rozdielne;
  oddelenie kurátora, autora, interného auditora a externého auditora je
  splnené. `[OBSERVED_IN_PRIMARY]`
- Všetkých päť package-contained ruleset/config hashov sa presne zhoduje s
  charterom. Packaged `external_auditor.toml`, capsule a packaged agent
  manifest viažu rovnaký SHA-256
  `6B1AF6C55E725E7A2332F30F0337713F1A7E254402E7F8A5A64BB689569C9A14`.
  `[OBSERVED_IN_PRIMARY]`
- Package-local manifest/inventory kontrola: `15/15` riadkov bez nezhody,
  `22` package súborov, `15` evidence súborov, `REPRO=0`, runtime rows `0`,
  duplicate-hash groups `0`, temp files `0`. `[OBSERVED_IN_PRIMARY]`
- Overené handoff hashe: scope
  `892B11BAAAE4B3F7B41C426CAB897D795FC872FCF878F4AA4B3EDB8C7B62D9A5`,
  manifest TSV
  `15256C1DC78E2CA414226E98DDB547F93439C91EA6653FB9B3A7179F789A2294`,
  history
  `F4390620C65E70A4B1434EA25CA38F675AC6CF2F0CBE81D94DFE3AAFD5F41AB3`,
  B6b-1
  `5E911971C2B7BAF2C2054228993766D753617D083F240A85FAAE75CF6C449223`
  a B6b-2
  `BEFF839636810D8AB83985DEE4CCF65892F15F670343AB6416450799131C895E`.
  `[OBSERVED_IN_PRIMARY]`

`MANIFEST=PASS` pre skutočné package kópie a deklarovanú source/copy hash
rovnosť. Živé source súbory sa podľa sealed-scope výnimky nečítali, takže
`15/15` live source/copy parity nebola externým auditorom nanovo overená proti
živému projektu; bola overená iba actual-copy verzus oba deklarované digesty
v sealed manifeste. `[OBSERVED_IN_PRIMARY]`

## Skutočná dôkazová úroveň

`ACTUAL_TIER=T1_PRIMARY_FORMULA`.

Balík obsahuje primárne analytické formula/passport dokumenty s presnou
source mapou a hashmi. Neobsahuje runner, runtime vstupy, raw computed
výsledok, DESI dátový vektor, likelihood ani druhú nezávislú implementáciu.
Nemôže dosiahnuť T2 alebo T3.

## Závery k auditným otázkam

### 1. B6b-1 momentové obálky

`AGREE_IN_SCOPE` pre obsah tejto podotázky. Spoločný passport konzistentne
odvodzuje nezápornosť, rozklad `Q_D=Q_s+Q_M,birth`, Cauchyho momentovú
nerovnosť pri `R_D>0` a konečnom druhom momente, backlogový completion budget,
steam integračný faktor a conservation/noise null smery. Rodiny MF1–MF4 sú
porovnané na rovnakej analytickej hĺbke: rate/energy upper bounds sú vždy
podmienené existenciou príslušných konečných capov a pri chýbajúcich capoch
zostáva explicitný stav `*_MOMENT_UPPER_BOUND_OPEN`. Dokument nevydáva
životaschopnosť, prázdnosť ani výber rodiny. `[OBSERVED_IN_PRIMARY]`

Exact references: `EVIDENCE/001`, riadky 55–172, 175–309 a 328–331.

### 2. B6b-2 kovariantný P0–P8 passport

`AGREE_IN_SCOPE` na úrovni schémy. Pri signatúre `(-,+,+,+)` je rozklad
`Q_A^mu=Q_A u^mu+F_A^mu`, `Q_A=-u_mu Q_A^mu` a ortogonalita `F_A` znamienkovo
konzistentná. Background znamienka rozlišujú parent drain, steam birth,
bezsignový net `M` a completion gain; perturbované energy/momentum, pressure,
shear a cross-correlation položky správne nedostávajú univerzálne znamienko.
`P0–P8` pokrýva frame/gauge, energy a momentum transfer, pressure/entropy,
shear, covariance/noise, source-off, IR/UV/characteristics a initial
modes/correlations. Source-off rozlišuje zánik parent `M1–Mnoise` od
kauzálneho completion tailu. MF1–MF4 identity výslovne zahŕňajú perturbáciu
miery/Jacobiánu, `delta w`, endpoint responses a cross-channel covariance.
`[OBSERVED_IN_PRIMARY]`

Exact references: `EVIDENCE/002`, riadky 137–226. Ide iba o úplnosť
passportu; konkrétne `delta Q_A`, `delta F_A`, `delta p_A`, `P_AB(k)` a ich
product-rule rozvinutia musí dodať budúci jediný fyzikálny kernel.

### 3. Search, coverage, mutation a ranking guardy

`AGREE_IN_SCOPE` ako contract-level ochrana. Immutable candidate record
zmrazuje family/state, funkčnú a parameterovú dimenziu, basis/bounds,
dataset role, pipeline/verziu, nuisance/scale cuts, search coverage/stopping,
seeds, artifact SHA a prior data exposure. Po prvom výsledku je shape
mutation nový versioned candidate; uncertified coverage nemôže vydať empty
alebo observational STOP. Comparator a DESI quasi-holdout nesmú meniť
survivor set ani ranking; ranking dátami je povolený až po certifikácii
holdoutu a pre-open freeze jeho štatistiky. `[OBSERVED_IN_PRIMARY]`

Exact references: `EVIDENCE/002`, riadky 228–295. Posudok nepotvrdzuje, že
budúca implementácia tieto guardy vykoná; iba že ich schéma je dostatočne
explicitná na fail-closed preregistráciu.

### 4. E3/E2 a calibration/comparator/quasi-holdout split

`AGREE_IN_SCOPE` pre internú klasifikáciu. Outer envelope
`[0.777,0.831]` je správne vedený ako E3 model-dependent search envelope,
nie spoločný posterior alebo likelihood; mapovanie cez flat LambdaCDM je
oddelený E2 comparator. DES Y6 a KiDS sú calibration inputs, HSC je
nonselection comparator a DESI DR1 FS ostáva
`RESERVED_QUASI_HOLDOUT_PENDING_CROSS_COVARIANCE` bez ranking práva a bez
blindness claimu. Mismatch je iba `REFERENCE_MISMATCH_ONLY / REVIEW`, kým
neexistuje úplný model-to-data-vector likelihood reťazec. Táto klasifikácia
je konzistentná s package-contained FS-GATE dôkazovými triedami.
`[INFERRED_FROM_PROJECT_DOCS]`

Exact references: `EVIDENCE/002`, riadky 23–135; `EVIDENCE/009`, riadky
143–197. Hodnoty a citácie DES/KiDS/HSC ani survey likelihoody neboli
nezávisle overené.

### 5. Split stavu a successor D04+D08+D10

`AGREE_IN_SCOPE`. Rozdelenie
`PASS_B6B2_PASSPORT_SCHEMA / REVIEW_B6B2_PHYSICAL_CONTENT_BLOCKED_D03_D11`
je korektné: schéma je uzavretá, ale neexistuje vyplnený event-energy,
recoil/collision a statistical/noise kernel. `D04+D08+D10` je najmenší
koherentný coupled author-input subbalík pre energiu/produktový ledger,
recoil/collision moments a noise/correlations z toho istého operátora. Je
zámerne neexekvovateľný a nepredstiera closure závislostí: D03 rate/state,
D05 ordering, D06 constants/initial data, D07/D11 source-off a D09 thermal
state zostávajú otvorené. `[OBSERVED_IN_PRIMARY]`

Exact references: `EVIDENCE/002`, riadky 297–355;
`EVIDENCE/003`, riadky 87–105, 1331–1348 a 1538–1585;
`EVIDENCE/010`, riadky 195–204 a 481–542.

„Najmenší“ tu znamená najmenší koherentný spoločný author-input passport pre
P1/P2/P5 bez rozbitia same-kernel provenance, nie tvrdenie, že každý z troch
blokov samostatne nemá menší textový podkrok.

## Findings podľa závažnosti

### Material scientific findings

Žiadne.

### F-001 — LOW / package-process limitation

`EVIDENCE/02_AUDITOR_INSTRUCTIONS.md` (body 3–4) a
`03_REPRODUCTION_AND_EXPECTATIONS.md` prikazujú externému auditorovi spustiť
live `External_Audits/TOOLS/Test-ExternalAuditPackage.ps1`. Sealed handoff
však povoľuje čítať iba package path a tool nie je pribalený v balíku.
Presný `96/96` R6 preflight preto nebolo možné nezávisle zopakovať bez
porušenia izolácie. Auditor vykonal package-local ekvivalent hashov,
manifestu, countov, runtime mapy, duplicít a temp súborov; ten prešiel.

Package-tier impact: T1 ostáva dosiahnutý, ale nezávislý claim
`R6_PREFLIGHT_REEXECUTED_96_OF_96` sa nevydáva. Project-impact: žiadna zmena
fyzikálneho verdiktu, skóre alebo hĺbky. Toto je dôvod celkového enumu
`AGREE_WITH_LIMITATION` namiesto `AGREE_IN_SCOPE`.

### F-002 — LOW / editorial lifecycle inconsistency

`00_SCOPE_AND_READ_ORDER.md` hore deklaruje `SEALED_READY_FOR_AUDIT`, ale
posledný odsek ešte v prítomnom čase tvrdí, že balík zostáva
`DRAFT_NOT_DELIVERED`, kým sa neuskutoční review a seal. `05_PACKAGE_HISTORY.md`
už dokumentuje obidva vykonané kroky a seal. Ide o stale pred-seal vetu;
stav auditu bol určený explicitným sealed handoffom, horným markerom scope a
package history.

Package-tier impact: none. Project-impact: none. Sealed package sa nesmie
opravovať; prípadná oprava patrí do nového package ID alebo project response.

## Prostredie a execution ledger

```text
PowerShell=7.6.3 Core
OS=Microsoft Windows 10.0.26200
OS_ARCH=X64
PROCESS_ARCH=X64
.NET=10.0.9
Python=NOT_RUN
Python_libraries=NOT_LOADED
BLAS_LAPACK=NOT_APPLICABLE
generated JSON=NONE
smoke=NOT_APPLICABLE
official audit=NOT_APPLICABLE
solver/search/data_download=0
```

Deklarovaný R6 príkaz:

```powershell
pwsh -NoProfile -File External_Audits\TOOLS\Test-ExternalAuditPackage.ps1 `
  -PackagePath External_Audits\PACKAGES\EA-20260723-043-B6B1-B6B2-ANALYTIC-PASSPORT
```

Stav: `NOT_RUN / DECLARED_PROCESS_DEVIATION`; exit code, wall time a
generated output SHA sú `N/A`, pretože tool je mimo sealed read allowlistu.

Package-local integrity príkaz bol PowerShell one-liner nad sealed package:
`Import-Csv` manifestu, `Get-FileHash -Algorithm SHA256` pre každý copy path
a povinné control/primary hashe, rekurzívny file count, duplicate-hash scan,
temp-name scan a načítanie header-only runtime mapy. Exit code `0`, interný
wall time `242 ms`, generated output file `NONE` a generated JSON `NONE`.

Environment probe: exit code `0`, interný wall time `13 ms`, generated file
`NONE`.

Celkový ledger po finálnej immutability kontrole: `33` PowerShell procesov,
z toho `32` úspešných a `1` úvodný nevedecký path-probe s exit code `1`
(`00_SCOPE.md` neexistoval; správny názov bol následne zistený iba v package
directory). Python procesy `0`; sieťové/download procesy `0`; fyzikálne
výpočty `0`; package preflight tool procesy `0`. Obsahové čítanie bolo iba v
sealed package. Zápis sa obmedzil na tento jediný response path.

## Odchýlky

1. R6 tool nebol spustený z dôvodu konfliktu package instruction s
   nadradeným sealed read allowlistom; náhradná package-local kontrola je
   opísaná vyššie.
2. Pred zistením exact názvu scope prebehol jeden neúspešný read pokus na
   neexistujúci súbor v tom istom sealed package path. Nečítal živý projekt
   a nemal vedecký efekt.
3. Žiadna formulačná, dátová, runtime alebo threshold odchýlka nebola
   vykonaná.

## Package tier verzus projektový dopad

| Vrstva | Záver |
|---|---|
| Package integrity | PASS pre package-local manifest/hash/inventory; exact R6 96/96 nebolo externým auditorom rerun |
| Najvyšší tier | `T1_PRIMARY_FORMULA` |
| B6b-1 obsah | súhlas v deklarovanom analytic-envelope scope |
| B6b-2 obsah | súhlas v schema/passport scope; fyzikálny kernel ostáva otvorený |
| Projektový verdict | bez zmeny; auditor nemá autoritu meniť `PASS/REVIEW/STOP` |
| Skóre/hĺbka/run | bez zmeny; `RUN_AUTHORIZED=false` |

## Explicitné nonclaims

- Nie je potvrdená existencia, neprázdnosť, životaschopnosť ani výber MF1–MF4.
- Nie je odvodený alebo overený fyzikálny kernel `D03–D11`, P5.4, G8 ani G9.
- Nebol vykonaný Python, solver, search, forward S8 prediction ani likelihood.
- Neboli nezávisle overené publikované DES/KiDS/HSC hodnoty, citácie,
  systematiky alebo likelihoody; tieto závery sú iba
  `INFERRED_FROM_PROJECT_DOCS`.
- DESI nebol otvorený ani certifikovaný ako nezávislý holdout.
- Nebol vydaný `COMPUTED_STOP_SCOPE`, `OBSERVATIONAL_STOP_SCOPE`, fyzikálny
  PASS/STOP, nový score ani nová hĺbka.
- T1 audit passportu nie je dôkaz pravdivosti bunkovej teórie.

## Handoff

`NEXT_ROLE=main_orchestrator`. Hlavný orchestrátor má posúdiť
`AGREE_WITH_LIMITATION`, oddeliť dve low findings od vedeckého obsahu a
rozhodnúť, či procesnú limitáciu prijme, alebo pripraví nový sealed package s
pribaleným/explicitne povoleným read-only preflight toolom. Response SHA-256
a post-write potvrdenie nemennosti balíka sa odovzdajú mimo tohto
self-referential response súboru.
