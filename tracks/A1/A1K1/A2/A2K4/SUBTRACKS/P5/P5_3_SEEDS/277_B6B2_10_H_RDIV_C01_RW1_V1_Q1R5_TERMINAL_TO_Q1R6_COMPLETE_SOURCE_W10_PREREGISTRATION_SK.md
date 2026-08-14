# B6b-2.10 — Q1R5 terminál -> Q1R6 complete-source W10 preregistrácia

**Task:** `A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R5-TO-Q1R6-COMPLETE-SOURCE-W10-PREREG-20260727-242`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.10`  
**Autor teórie:** Martin Jambor  
**Formalizácia:** Codex, hlavný orchestrátor  
**Stav:** `DRAFT_ORDERED_TRANSITION_AND_ACQUISITION / NO_Q1R6_SOURCE_OPERATION_YET / NO_PYTHON`

## 1. Jediný cieľ a zachovanie poradia

Cieľom je získať jeden complete W10. Tento atóm preto otvorí iba prvý
nasledujúci neduplikovaný F-A raw rank a odstráni procesnú chybu, pre ktorú
riedke webové line windows nedokázali certifikovať úplnosť Q1R5.

```text
preserved Q1R3:
  arXiv 2301.12328
  NOT_ACCEPTED_NOT_EXCLUDED / 24/24_TERMINAL
  further operations and cap reset = FORBIDDEN

preserved Q1R5:
  arXiv 1405.4005
  ELIGIBLE_ACCESSIBLE_NOT_ACCEPTED_NOT_EXCLUDED / 15/15_TERMINAL
  authoritative gate map = S0-S12 NOT_ASSESSABLE_EVIDENCE_INCOMPLETE;
                           S13 PASS
  further operations and cap reset = FORBIDDEN

next immutable raw rank:
  global rank = 6
  family = F-A
  query = Q1
  query rank = 6
  transition label = Q1R6
  title = First principles determination of bubble wall velocity
  arXiv = 2204.13120
  canonical source archive URL = https://export.arxiv.org/e-print/2204.13120
```

Q1R6 sa nevyberá podľa výsledku, abstraktu ani podobnosti s W10. Poradie a
identita pochádzajú výlučne z immutable raw-v2 ledgera264. Q1R6 ešte nie je
eligible kandidát, reference model ani physical witness.

## 2. Immutable vstupy a stav

```text
parent source protocol261 SHA256:
  FB94A671AA861B5B9A18639AB9A4C565FC0F90A800723D232A0B073D3B877F5B
raw-v2 ordered source ledger264 SHA256:
  DA9F5FCACAD15FF8D00C6C582D05E05E47ED33F764FD05A0286D607E394F079A
Q1R5 prereg275 SHA256:
  4DB7C5B9E158A50AC47F233E0A775240BF12F65E0246A97A4CC3A9A6BDB685AE
Q1R5 result276 SHA256:
  44F50C417A8FFE47C8E3918C663D13CC40933517C613D22890192FE2A2327390
current plan after task240 SHA256:
  268E16A5233D13ABC5CD006CDC37EF0D651B388960CEC1332F4768A37BDE39A6
K4 plan after task240 SHA256:
  D58B0283D0D422B40A394C803D85E1004E74935CE0D771616B92584A3042C894
P5 plan after task240 SHA256:
  3A2DF2209D12EE633222AC1B5191849C8AE4994DC2842AC91CD933EF2CEE6BCA
event ledger through task240 SHA256:
  4071D609C6BFD8B12D34DF982CAEA16D098A708088FA1E5448269C6724E37AC6
progress review task241:
  BOUNDARY_OR_BLOCKER_PROGRESS / Q1R6 transition warranted only with
  coverage-complete acquisition contract
```

Stav ostáva K4 `60/100`, P5 `3.5/6`, P4 work atoms `2`, physical witness
attempts `0`, `RUN_AUTHORIZED=false` a blocker
`PHYSICAL_RW1_CARRIER_POWER_THRESHOLD_CONSERVATION_CELL_MEASURE_AND_RESET_NOT_DERIVED`.

## 3. Complete-source acquisition kontrakt

Po nezávislom auditnom PASS, out-of-file SHA freeze a absent-target
preflighte sa vykoná presne jedna Q1R6 internetová operácia:

```text
tool: C:\Windows\System32\curl.exe
method: GET
URL: https://export.arxiv.org/e-print/2204.13120
options: --fail --location --silent --show-error --proto =https
         --proto-redir =https --tlsv1.2 --connect-timeout 20
         --max-time 180 --max-redirs 5 --max-filesize 52428800
candidate-local source-operation budget: 1/1
```

Download smeruje do súboru s kryptograficky náhodným GUID názvom v novom
create-new dočasnom podadresári priamo v cieľovom `P5_3_SEEDS` adresári na
`D:`. Dočasný adresár aj názov sú pred curlom absent a vytvoria sa bez
prepisu. Až pri exit code `0`, nenulovej dĺžke, veľkosti najviac 50 MiB a
úspešnom archive safety preflighte sa temp súbor cez same-volume atomic
no-overwrite rename publikuje do absent cieľa:

`277A_B6B2_10_Q1R6_ARXIV_SOURCE.tar.gz`.

Cieľ nesmie byť prepísaný. Connect timeout 20 s, total timeout 180 s,
viac než 5 redirectov, redirect mimo HTTPS, payload nad 52 428 800 bytes,
HTTP chyba, prázdny payload, nečitateľný archive, kolízia cieľa alebo
neúspešný same-volume atomic move končia
`REVIEW_Q1R6_ACQUISITION_TECHNICAL_FAILURE_NO_PHYSICAL_INFERENCE`. Operácia
sa neopakuje; iný mirror, PDF, web window, search, click, retry alebo
companion nie sú povolené.

Táto `1/1` lineage je nová a candidate-local. Neresetuje Q1R3 ani Q1R5.

## 4. Bezpečné rozbalenie a complete-text receipt

Lokálne sa použije iba `C:\Windows\System32\tar.exe`; nejde o ďalšiu source
operáciu. Pred extrakciou sa musia úspešne a do 60 sekúnd získať oba výstupy
`tar -tf` (exact names v archive order) a `tar -tvf` (type/size rows v tom
istom order). Počty musia byť rovnaké. Type-aware parser musí jednoznačne
prečítať typ a uncompressed byte size každého riadku; nejednoznačný formát je
technical REVIEW. Povolené sú iba directory a regular-file entries. Symlink,
hardlink, block/character device, FIFO, socket alebo iný typ je zakázaný.

Pred extrakciou navyše platia guardy:

```text
maximum archive entries: 512
maximum one regular entry: 134217728 uncompressed bytes
maximum sum of regular entries: 268435456 uncompressed bytes
maximum list time: 60 seconds per tar listing
maximum extraction time: 120 seconds
```

Prekročenie limitu, timeout alebo nemožnosť ukončiť proces znamenajú
technical REVIEW a zákaz interpretácie. Celý manifest sa odmietne aj vtedy,
ak niektorý názov:

- je absolútna cesta, UNC alebo drive-qualified cesta;
- obsahuje spätnú lomku, dvojbodku/ADS, NUL alebo alternate separator;
- po rozdelení na `/` obsahuje prázdny segment alebo parent traversal `..`;
- obsahuje case-insensitive Windows device segment `CON`, `PRN`, `AUX`,
  `NUL`, `COM1..COM9` alebo `LPT1..LPT9`, aj s príponou;
- po resolved-path kontrole uniká z jedného nového OS temp adresára.

Každý regular archive entry sa po bezpečnej extrakcii zoradí podľa
forward-slash relative path a dostane byte length a SHA-256. Súčet regular
entries, dĺžok a hashov musí byť v receipte. Každý manifestový regular entry
musí mať práve jeden extrahovaný preobraz; navyše extrahovaný súbor znamená
technical REVIEW.

Readable-source allowlist je:

```text
.tex .ltx .bib .bbl .sty .cls .cfg .def .clo
.txt .md .rst .csv .tsv .dat
.m .wl .py .c .cc .cpp .h .hpp
.json .yaml .yml .xml
```

Known nonsemantic binary/figure allowlist je:

```text
.pdf .png .jpg .jpeg .gif .bmp .tif .tiff
.eps .ps .svg .ai
```

Každý readable entry sa vloží celý do jediného receipt súboru s exact
relative-path boundary, original byte length, original SHA-256 a deklarovaným
encoding výsledkom. UTF-8 sa dekóduje strict; pri zlyhaní sa skúsi Windows-1252
a dekódovanie sa označí. NUL byte, decode failure, neznáma prípona, chýbajúci
`\input`/`\include` cieľ alebo text iba v nepovolenom entry znamená:

`REVIEW_Q1R6_SOURCE_UNIVERSE_NOT_CERTIFIED_NO_PHYSICAL_INFERENCE`.

Binary/figure entries sa neinterpretujú ako text, ale ich path/length/SHA sú
povinne v manifeste. Fyzikálna absencia sa smie vyhlásiť iba nad úplným
readable source universe; obrázok nikdy nesmie niesť jedinú definíciu W10
objektu bez textového preobrazu v source.

Receipt sa publikuje presne raz cez create-new file handle do absent cieľa:

`277B_B6B2_10_Q1R6_COMPLETE_SOURCE_RECEIPT.txt`.

Obsahuje frozen URL a curl options, exit code, transport guards,
archive path/length/SHA, exact `tar -tf` aj `tar -tvf` manifest, type/size a
path bezpečnostné kontroly, archive limity/timing, complete entry accounting,
readable/binary klasifikáciu, decode status, include-closure kontrolu a celý
flattened readable source. Temp extrakcia a prázdny GUID podadresár sa po
úspešnom publikačnom close odstránia; immutable archive277A a receipt277B
zostanú.

`SOURCE_UNIVERSE_COMPLETE=PASS` platí iba pri splnení všetkých pravidiel
tejto sekcie. Nie je odvodené z počtu webových riadkov ani zo šírky okien.

## 5. Eligibility a W10 passport

Pri `SOURCE_UNIVERSE_COMPLETE=PASS` sa najprv overí, že source-native title,
authors a arXiv identity zodpovedajú Q1R6 a že ide o pôvodný research model.
F-A eligibility vyžaduje lokálny scalar/domain-wall interface model s
explicitným fluid/reservoir sektorom a relevantným barrier/interface-energy
preobrazom. Inak sa použije exact `PRIMARY_OUTSIDE_F_A...` alebo
`SECONDARY_EXCLUDED` vetva bez passport PASS.

Eligible zdroj musí v jednej koherentnej fyzike zmapovať:

```text
(Z_rec, P_rec, W_*, conservation, u_cell, congruence/dmu_cell,
 crossing, R_reset^Z, source-off, noncircularity).
```

Každý riadok musí uviesť exact source file + source line/equation/section,
`PROVENANCE_CLASS` (`SOURCE_EXACT`, `DERIVED_SAME_MODEL`, `E3_MAPPING` alebo
`MISSING`) a `EVIDENCE_STATUS`. `E3_MAPPING` nesmie tvoriť nový fyzický
objekt. Passport kontrakt je nezmenený:

```text
W_rec(tau_birth)=0,
D_u W_rec=P_rec>=0,
W_*>0 a D_u W_*=0 počas parent cyklu,
chi_div=W_rec/W_*, chi_c=1,
prvý jednoduchý transverzálny upward crossing.
```

Barrier/free energy nie je automaticky reálne dodaná kumulatívna work
energia. Nucleation, numerical initialization alebo premenovanie nie sú
automaticky regular crossing ani fyzická daughter reset mapa.

## 6. Zmrazený S0–S13 screen

| ID | PASS podmienka |
|---|---|
| S0 | original primary Q1R6 identity a `SOURCE_UNIVERSE_COMPLETE=PASS` |
| S1 | jedna action/EOM/state/`T^{mu nu}`/convention/dimension/boundary/regime closure bez splice |
| S2 | fyzický lokálny `Z_rec` a `W[Z_rec]` bez hidden history clocku |
| S3 | na tej istej on-shell pre-event ceste pointwise `D_uW=P_rec>=0`, odvodený zdroj aj reservoir |
| S4 | finite positive cycle-frozen `W_*` z tej istej fyziky |
| S5 | disjunktný local energy-momentum ledger, residual-interface tok a source-off identity |
| S6 | source-native future unit `u_cell`, once-only parent worldtube/congruence a finite invariant `dmu_cell` |
| S7 | dosiahnuteľná on-shell absolútne spojitá jednoduchá upward cesta; nie jump/interpolation/initialization |
| S8 | fyzická dynamická `R_reset^Z`, zero daughter credit a oddelená residual energy |
| S9 | kovariancia/gauge meaning, causal well-posed použitý režim, stabilita, jednotky a orientation |
| S10 | bez GW/S8/H0/division/biology/downstream targetu alebo fitu vo vstupe |
| S11 | všetky passport objekty v jednom provisional `Y_div` bez novej fyziky |
| S12 | bez fyzického vstupu/rezervoára nevzniká rast ani event |
| S13 | bez Pythonu, fitu, steam/completion, score/depth change alebo downstream runu |

Každý gate dostane `PASS`, `FAIL`, `MISSING` alebo exact evidence-incomplete
stav. `MISSING` je dovolené iba po `SOURCE_UNIVERSE_COMPLETE=PASS`. Pri
necertifikovanom universe sú S0–S12 `NOT_ASSESSABLE_EVIDENCE_INCOMPLETE` a
S13 sa vyhodnotí samostatne.

## 7. Rozhodovacie vetvy a účtovanie

```text
SOURCE_UNIVERSE_COMPLETE + eligible + S0-S13 PASS + všetky passport polia:
  CANDIDATE_COMPLETE_W10_INTERFACE_ACTION_PASSPORT_FOUND
  / PENDING_INDEPENDENT_PHYSICS_AUDIT.

Complete universe + koherentný interface reference, ale MISSING W10 polia:
  PASS_Q1R6_REFERENCE_INTERFACE_MODEL_ONLY
  / REVIEW_Q1R6_NOT_A_COMPLETE_W10_WITNESS.

Complete universe + formula/physical/scope konflikt:
  PRECHECK_Q1R6_EXCLUDED_SCOPE
  / exact candidate-local cause.

Acquisition alebo source-universe certification failure:
  REVIEW_Q1R6_*_NO_PHYSICAL_INFERENCE.
```

Po complete-universe výsledku a nezávislom audite/main acceptance sa P4 work
atoms zvýšia `2->3` pri complete-W10, reference-only alebo candidate-local
exclusion. Physical witness attempts sa zvýšia `0->1` iba pri prijatom
complete-W10. Evidence-incomplete/technical vetva zachová oba počty.

Žiadna vetva sama nedokazuje pravdu C01, `A_RW1` emptiness, P5.3 closure,
A3, score/depth zmenu ani run permission. Python, P5.4, fit,
steam/completion a druhý ansatz sú zakázané.

## 8. Výstup, procesy a súborový rozpočet

Výsledok sa po source acquisition a interpretácii publikuje presne raz do:

`278_B6B2_10_H_RDIV_C01_RW1_V1_Q1R6_S0_S13_PHYSICS_SCREEN_RESULT_SK.md`.

Celý atóm má najviac 4 live vedecké artefakty: document277, archive277A,
receipt277B a result278. Opening batch mení iba document277 a event ledger.
Central closure je najviac current/K4/P5 + ledger až po auditovanom výsledku.
Audit package copies `0`. Python processes `0`. Source operations `1/1`.

## 9. Auditný handoff

```text
TASK_ID: A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R5-TO-Q1R6-COMPLETE-SOURCE-W10-PREREG-AUDIT-20260727-243
ROLE: physics_track_auditor
ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
ASSIGNED_AGENT_TASK_ID: /root/c01_q1r3_access_prereg_audit
ARTIFACT_AUTHOR_TASK_ID: /root::task242
STATIC_AUDITOR_TASK_ID: /root/c01_q1r3_access_prereg_audit::task243
INTERNAL_AUDITOR_TASK_ID: /root/c01_q1r3_access_result_audit::RESERVED_DISTINCT_RESULT_AUDIT
PACKAGE_CURATOR_TASK_ID: RESERVED_EXTERNAL_PACKAGE_CURATOR_NOT_ACTIVE
EXTERNAL_AUDITOR_TASK_ID: RESERVED_EXTERNAL_AUDITOR_NOT_ACTIVE
SEPARATION_OF_DUTIES_CHECK: PASS_EXPECTED_AUTHOR_PREREG_RESULT_AUDITOR_DISTINCT
ROUTE: A1_K1_A2_K4_P5.3g7_SM_v1_B6b-2.10_H_RDIV_C01_RW1_v1_Q1R5_TO_Q1R6_COMPLETE_SOURCE
CURRENT_PHASE: DRAFT_BEFORE_ANY_Q1R6_SOURCE_OPERATION
ALLOWED_NEXT_ACTION: independent read-only prereg audit; after PASS, out-of-file SHA freeze and exact absent-target preflight
ALLOWED_READS: mandatory bootstrap; documents261,264,275-277; receipts275A/275B; result276 plus task238 erratum; ledger tasks237-242; current/K4/P5; role config/manifest
ALLOWED_WRITES: none
FORBIDDEN_ACTIONS: edit; internet/source operation; Python; Q1R3/Q1R5 operation or cap reset; later-rank selection; physics verdict; score/depth/run/package change
IMMUTABLE_INPUT_PATHS_AND_SHA256: document261=FB94A671AA861B5B9A18639AB9A4C565FC0F90A800723D232A0B073D3B877F5B; ledger264=DA9F5FCACAD15FF8D00C6C582D05E05E47ED33F764FD05A0286D607E394F079A; prereg275=4DB7C5B9E158A50AC47F233E0A775240BF12F65E0246A97A4CC3A9A6BDB685AE; result276=44F50C417A8FFE47C8E3918C663D13CC40933517C613D22890192FE2A2327390; current=268E16A5233D13ABC5CD006CDC37EF0D651B388960CEC1332F4768A37BDE39A6; K4=D58B0283D0D422B40A394C803D85E1004E74935CE0D771616B92584A3042C894; P5=3A2DF2209D12EE633222AC1B5191849C8AE4994DC2842AC91CD933EF2CEE6BCA; ledger_through_task240=4071D609C6BFD8B12D34DF982CAEA16D098A708088FA1E5448269C6724E37AC6
PREREG_SHA256: PENDING_AFTER_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only audit; after freeze exact archive277A, receipt277B and result278
DONE_WHEN: ordered Q1R6 identity, no-cap-reset preservation, one-operation archive acquisition, publish-once behavior, traversal/link safety, complete manifest/entry/hash/text/include accounting, eligibility, passport/S0-S13, accounting/nonclaims and four-artifact cap are fail-closed
NEXT_ROLE: main_orchestrator
```
