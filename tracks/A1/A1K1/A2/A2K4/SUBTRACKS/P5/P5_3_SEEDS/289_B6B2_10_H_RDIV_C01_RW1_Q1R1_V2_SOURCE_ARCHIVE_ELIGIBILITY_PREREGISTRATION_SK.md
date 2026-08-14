# B6b-2.10 — Q1R1-V2 source-archive eligibility preregistrácia

**Task:** `A2K4-B6B2-10-H-RDIV-C01-RW1-Q1R1-V2-SOURCE-ARCHIVE-PREREG-20260728-327`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.10 -> Q1R1-V2`  
**Autor teórie a výberu Q1R1:** Martin Jambor  
**Formalizácia:** Codex, hlavný orchestrátor  
**Stav:** `DRAFT_UNFROZEN / AWAITING_INDEPENDENT_AUDIT / NO_NETWORK / NO_PYTHON`

## 1. Differential scope a zdedený stav

Q1R1-V1 dokumenty 287, 287A a 288 zostávajú immutable. V1 použila web-cache
provider na dve reprezentácie arXiv HTML/PDF; obe vrátili iba `Cache miss`.
Nezískala obsah paperu a skončila technicky:

```text
V1_ACCESS_OPERATIONS: 2/2_EXHAUSTED
HISTORICAL_PACKAGES_TOTAL: 1
CONSECUTIVE_TECHNICAL_FAILURES: 1/10
Q1R1_ELIGIBILITY: UNRESOLVED
```

V2 nie je retry O1/O2 ani reset počítadiel. Je to jedna nová technická
architektúra: priamy HTTP download oficiálneho source archívu toho istého
paperu, mimo zlyhaného web-cache provider path. Fyzický scope, G0–G3 a
rozhodovacie vetvy sa nemenia.

## 2. Jediná povolená network operácia a durable at-most-once journal

Povolený je presne jeden `HTTP GET`, at-most-once, bez retry, redirectu,
fallbacku, searchu alebo iného paperu:

```text
V2-O1 URL: https://export.arxiv.org/e-print/2307.12080v2
method: GET
redirects: forbidden
internal cancellation timeout: 60 s
external process timeout: 120 s
user-agent: Teoria-Q1R1-V2-SourceAudit/1.0
accept-encoding: identity
```

Pred vytvorením journalu musia byť neprítomné všetky štyri exact ciele:

```text
D:/Teoria/tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/289J_B6B2_10_Q1R1_V2_SOURCE_ARCHIVE_OPERATION_JOURNAL.txt
D:/Teoria/tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/.289A_B6B2_10_Q1R1_SOURCE_ARCHIVE.part
D:/Teoria/tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/289A_B6B2_10_Q1R1_ARXIV_2307_12080V2_SOURCE_ARCHIVE.tar.gz
D:/Teoria/tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/290_B6B2_10_H_RDIV_C01_RW1_Q1R1_V2_SOURCE_ARCHIVE_ELIGIBILITY_RESULT_SK.md
```

Proces najprv vytvorí 289J cez `FileMode.CreateNew`, `FileShare.None` a
`FileOptions.WriteThrough`. Pred prvým `SendAsync` zapíše a cez
`Flush(true)` trvalo uloží `V2-O1 REQUEST_RESERVED`, UTC čas, exact URL,
metódu a počiatočné počty. Od tejto durable značky je operácia spotrebovaná.
Po návrate alebo zachytenej chybe appendne a opäť `Flush(true)` presne jeden
terminálny záznam `REQUEST_COMPLETED` alebo `REQUEST_FAILED` s HTTP statusom,
počtom bytes, guardom a typom chyby. Pád procesu po `REQUEST_RESERVED` bez
terminálneho záznamu je `CONSUMED_PROCESS_INTERRUPTED`; nesmie vyvolať rerun.
Journal sa po prvom uzavretí nemení.

Exact transport je jeden nový PowerShell 7.6 proces s `.NET 10 HttpClient`:

```text
HttpClientHandler.AllowAutoRedirect = false
HttpClientHandler.AutomaticDecompression = None
HttpClientHandler.MaxResponseHeadersLength = 64  # KiB podľa .NET API
HttpRequestMessage = new GET exact V2-O1 URL
request.Headers.AcceptEncoding = identity
request.Headers.UserAgent = Teoria-Q1R1-V2-SourceAudit/1.0
HttpClient.SendAsync(request, ResponseHeadersRead, 60 s CancellationToken)
```

Prijateľný je iba status exact `200`; redirect alebo akýkoľvek iný status je
technická vetva. Ak `Content-Length` existuje, musí byť `10 000..8 MiB` ešte
pred čítaním body. Body sa streamuje po blokoch najviac `64 KiB` do exact
`.part` cez `FileMode.CreateNew`, `FileShare.None`, `FileOptions.WriteThrough`.
Hard cap je `8 MiB`; prekročenie sa odmietne bez dočítavania. Po body sa
vykoná `Flush(true)`. Zachytený failure odstráni procesom vlastnený `.part`;
pri neočakávanom páde sa zvyšok zachová ako forenzný temp, ale 289A nevznikne
a operácia ostáva spotrebovaná.

Až po všetkých guardoch sa response bytes publikujú jediným exclusive
`File.Move(temp, final, false)`. Kolízia alebo persistence failure nesmie
prepísať 289A a zakazuje retry.

## 3. Technické a archive-safety guardy pred publikovaním

Validácia má vlastný monotonic deadline `30 s` a pracuje iba nad bounded
bytes v `.part`; nič neextrahuje do filesystemu. Akýkoľvek neurčený formát,
exception alebo limit je fail-closed technická vetva. Povinné limity sú:

```text
compressed/http bytes: 10 000..8 MiB
decompressed TAR bytes: <=32 MiB
compression ratio: <=40
TAR entry count: 1..512
single regular-file payload: <=4 MiB
archive validation deadline: 30 s
```

Povolené sú iba dve reprezentácie: exact raw TAR alebo jeden RFC-1952 GZIP
member obsahujúci jeden TAR. GZIP parser musí overiť header a reserved flags,
ohraničiť všetky optional header polia spolu na `4 KiB`, dekódovať presne
jeden raw-DEFLATE stream cez no-overread wrapper, overiť jeho exact CRC32
(`0xEDB88320`) a ISIZE trailer a potom vyžadovať EOF. Druhý member,
concatenation alebo ľubovoľné trailing bytes sa odmietnu. Raw TAR aj
dekomprimovaný TAR musia končiť presne dvoma 512-byte nulovými blokmi bez
ďalších bytes.

TAR sa číta priamo cez `.NET System.Formats.Tar.TarReader`; externý `tar`
ani filesystem extraction sa nepoužijú. Povolené typy entry sú iba
`RegularFile`, `V7RegularFile` a `Directory`. Symlink, hardlink, device,
FIFO, socket, sparse, PAX/GNU metadata alebo iný typ sa odmietne. Každý entry
názov sa musí rovnať svojmu Unicode NFC tvaru a musí prejsť všetkými
kontrolami:

- iba relatívny slash-separated názov; žiadne `\\`, UNC, leading `/`, drive
  prefix, `:`, ADS, NUL alebo control znak;
- žiadny prázdny, `.` alebo `..` segment, leading `-`, trailing bod/medzera;
- žiadny Windows reserved basename `CON`, `PRN`, `AUX`, `NUL`, `COM1..9`
  alebo `LPT1..9`, ani s príponou;
- žiadna exact ani case-insensitive kolízia po NFC normalizácii;
- regular-file length musí byť deklarovaná, nezáporná, do `4 MiB` a súčet
  lengths do `32 MiB`.

Member obsah sa číta iba z `TarReader` po úspešnej validácii mena a typu.
Žiadne meno sa neposiela shellu. Ak by sa pri forenznom debugovaní niekedy
použil externý `tar`, povinný je option terminator `--` a exact už validovaný
member; taký debug nie je súčasťou V2 a nemôže vytvoriť výsledok.

Pred publish musia navyše prejsť:

1. HTTP status exact `200`, žiadny redirect, bounded headers/body;
2. prvé non-whitespace bytes nie sú HTML/XML/error page;
3. SHA-256 exact response bytes je konečný nonzero hash;
4. validný safe archive inventory obsahuje aspoň jeden `.tex`;
5. práve jeden main dependency root po nižšej closure procedúre obsahuje
   whitespace-normalized exact titul
   `General relativistic bubble growth in cosmological phase transitions`
   a identity `Giombi` aj `Hindmarsh`.

Ak ktorýkoľvek guard zlyhá, nejde o content/physics výsledok. 289A sa
nepublikuje, 289J uchová presný prvý failure guard a retry je zakázaný.

## 4. Source-archive completeness gate

Po immutable publish 289A sa už bez networku vykoná read-only source audit
cez rovnaký safe `TarReader` contract. Relevantné `.tex` a `.bib` entry sa
dekódujú strict UTF-8; encoding failure je `UNRESOLVED_ACCESS`.

Dependency closure sa zostaví rekurzívne z jediného main rootu. Najprv sa
odstránia iba neescaped `%` komentáre. Closed allowlist source-loading
direktív je presne:

```text
\input{file}  \include{file}  \subfile{file}
\import{dir}{file}  \subimport{dir}{file}
\inputfrom{dir}{file}  \subinputfrom{dir}{file}
\includefrom{dir}{file}  \subincludefrom{dir}{file}
\bibliography{comma-list}
\addbibresource[optional-literal-options]{file}
\documentclass[optional-literal-options]{file}
\usepackage[optional-literal-options]{comma-list}
\RequirePackage[optional-literal-options]{comma-list}
\lstinputlisting[optional-literal-options]{file}
\verbatiminput{file}
```

TeX source targety sa riešia relatívne voči includujúcemu memberu; pri
`input/include/subfile/import` rodine sa pri chýbajúcej prípone skúsi iba
`.tex`. Bibliografické targety sa rozdelia podľa literal commas a pri
chýbajúcej prípone dostanú iba `.bib`. Každý deklarovaný
`\bibliography`/`\addbibresource` target musí exact existovať a byť strict
UTF-8 čitateľný. Lokálne class/package targety dostanú iba `.cls`/`.sty`,
zaradia sa do closure a rekurzívne sa kontrolujú rovnakými pravidlami.

Ak class/package target v archíve nie je, zapíše sa ako
`EXTERNAL_TEX_DEPENDENCY`. Completeness smie pokračovať iba po manuálnom
zdôvodnení, že ide o štandardnú externú typesetting dependency a nenesie
modelovú definíciu, rovnicu ani loader potrebný pre G1–G3; inak je stav
`UNRESOLVED_SOURCE_CLOSURE`. `includegraphics` a iný asset reference sa
inventarizujú a každý chýbajúci alebo nečitateľný asset, ktorý môže niesť
definíciu/rovnicu pre G1–G3, takisto blokuje closure.

Každý source-loading príkaz mimo closed allowlistu, macro-generated alebo
dynamický path, `\csname`/`\endcsname` zostavenie loadera, catcode zmena,
alias loadera cez `\let`, loader vložený do `\def`/`\newcommand`/príbuznej
macro definície, unsafe path, missing/ambiguous target, dependency cycle
alebo unparseable balanced argument znamená
`UNRESOLVED_SOURCE_CLOSURE`. Automatický parser je iba nutná brána: pred
`ABSENT` hlavný obsahový audit manuálne prejde všetky regular textové
`.tex/.sty/.cls/.bib` entry v archíve, nie iba vypočítaný reachable graph,
a pre každé uvedie `REACHABLE`, `UNUSED_IRRELEVANT` alebo `UNRESOLVED`.
Ak nemožno vylúčiť ďalší loader alebo relevantný nepokrytý textový member,
completeness neprejde. Rovnakým spôsobom sa overia všetky deklarované
appendix zdroje.

`SOURCE_ARCHIVE_COMPLETE_FOR_ABSENCE=PASS` vyžaduje:

```text
exact Q1R1 title + Giombi/Hindmarsh identity
AND one main document with begin/end document
AND every local \input / \include TeX dependency present in inventory
AND searchable substantive model and equation source
AND boundary treatment source
AND energy/conservation treatment source
AND bibliography via present .bib or in-source thebibliography
AND every declared appendix source present
AND no unresolved source dependency needed to interpret G1-G3.
```

Figures a style files sa zapíšu do inventory, ale ich neprítomnosť blokuje
absence claim iba vtedy, ak nesú definíciu alebo rovnicu potrebnú pre G1–G3.
Neúplný dependency closure, nečitateľný TeX alebo chýbajúca relevantná časť
znamenajú `UNRESOLVED_ACCESS`, nikdy `ABSENT`.

Celý uzavretý source closure sa pre G1–G3 prehľadá podľa explicitného
synonymického registra zapísaného do resultu: interface/wall/boundary/shell,
finite width/thickness/profile/scalar field/action/equation of motion,
fluid/reservoir/stress-energy/energy-momentum/conservation/flux a
barrier/critical work/nucleation/action/surface energy. Automatický hit ani
no-hit nevydáva verdikt; result musí uviesť source-native kontext a rovnicu
alebo sekciu. `ABSENT` je dovolené iba po manuálnom posúdení celého closure.

### 4.1 Exact implementation freeze a nezávislý statický audit

Prose contract sám nepovoľuje network operáciu. Po zmrazení tejto
preregistrácie smie hlavný orchestrátor vytvoriť iba jeden exact executable
artefakt, bez jeho spustenia:

```text
D:/Teoria/tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/289S_B6B2_10_Q1R1_V2_SOURCE_ARCHIVE_ACQUISITION.ps1
```

Script musí mať default `NO_NETWORK`; režim `-SelfTest` nesmie konštruovať
HttpClient ani zapisovať live outputs. Režim `-Acquire` musí vyžadovať exact
frozen prereg SHA a exact authorization-event-ledger SHA ako povinné CLI
argumenty a odmietnuť všetko ostatné. Source SHA sa zmrazí mimo skriptu.
Autor skriptu ho nesmie byť jeho jediným auditorom.

Pred akýmkoľvek PowerShell procesom nad týmto skriptom musí distinct
`math_script_auditor` read-only overiť celý source, reachability skutočnej
executed cesty, fail-closed journal/order, HTTP a output guardy a embedded
non-network fixtures. Povinné fixture triedy sú:

- valid raw TAR a valid single-member GZIP(TAR);
- chybný CRC32, ISIZE a FHCRC, druhý GZIP member a trailing bytes;
- malformed TAR header checksum, non-512 framing, padding/trailing data a
  chýbajúce alebo nadbytočné terminálne nulové bloky;
- každý zakázaný TAR entry type, unsafe/reserved path, exact aj case-folded
  collision a všetky size/count/ratio/deadline hranice;
- missing/cyclic/ambiguous TeX dependency, každý podporovaný literal loader,
  unresolved bibliography target, local style/class recursion a
  unsupported/dynamic/macro/catcode loader.

Až po odporúčaní `STATIC_IMPLEMENTATION_AUDIT_PASS`, jeho prijatí hlavným
orchestrátorom a out-of-file source-SHA freeze sa smie presne raz spustiť
`-SelfTest`. Všetky fixtures musia prejsť a ich exact count/digest sa zapíše
do route event ledgera. SelfTest technický PASS nevynuluje Q1R1 counter.
Potom nasleduje mandatory progress review; až samostatný autorizačný append
smie povoliť jediný `-Acquire`. Neúspešný statický audit alebo SelfTest
znamená versioned implementation correction bez networku, nie fyzikálny
výsledok ani spotrebovanú V2-O1 operáciu.

## 5. Nemenné eligibility gate G0–G3

| ID | PASS podmienka |
|---|---|
| `G0` | exact primary/source identita Q1R1 |
| `G1` | source-native local finite-width interface pole/stav s explicitnou akciou alebo EOM; nie iba infinitesimal boundary/jump |
| `G2` | rovnaký model explicitne obsahuje coupled fluid/reservoir a local energy-momentum/conservation ledger |
| `G3` | rovnaká fyzika odvodzuje finite positive critical interface barrier/work použiteľnú ako pre-event threshold |

Result musí pre každý gate uviesť exact archive path, source line/rovnicu alebo
sekciu, stručnú parafrázu a `SOURCE_EXACT`, `DERIVED_SAME_MODEL`, `ABSENT`
alebo `UNRESOLVED_ACCESS`. `ABSENT` vyžaduje
`SOURCE_ARCHIVE_COMPLETE_FOR_ABSENCE=PASS` a celé relevantné synonymické
prehľadanie source closure.

## 6. Predregistrované vetvy a účtovanie

```text
IF TECHNICAL_NETWORK_GUARD_OR_PUBLISH_FAILURE:
  outcome = TECHNICAL_FAILURE_NO_PHYSICAL_INFERENCE
  V2_ARCHIVE_OPERATIONS = 1/1
  cumulative_source_operations = 3
  historical_packages_total = 2
  consecutive_technical_failures = 2/10
  289A = ABSENT

IF ARCHIVE_PUBLISHED_BUT_SOURCE_CLOSURE_INCOMPLETE:
  outcome = REVIEW_Q1R1_SOURCE_ARCHIVE_ELIGIBILITY_UNRESOLVED
  V2_ARCHIVE_OPERATIONS = 1/1
  cumulative_source_operations = 3
  historical_packages_total = 2
  consecutive_technical_failures = 0/10
  no ABSENT gate

IF SOURCE_ARCHIVE_COMPLETE_FOR_ABSENCE PASS AND NO GATE ABSENT
AND NOT ALL G0-G3 PASS:
  outcome = REVIEW_Q1R1_SOURCE_ARCHIVE_ELIGIBILITY_AMBIGUOUS
  technical counter = 0/10
  no ABSENT gate; no S0-S13 successor authorization

IF SOURCE_ARCHIVE_COMPLETE_FOR_ABSENCE PASS AND ANY G1-G3 ABSENT:
  outcome = CONFIRM_Q1R1_PRIMARY_OUTSIDE_F_A_REQUIRED_INTERFACE_ACTION
  / NO_S0_S13_SCREEN
  technical counter = 0/10

IF SOURCE_ARCHIVE_COMPLETE_FOR_ABSENCE PASS AND G0-G3 ALL PASS:
  outcome = REVIEW_Q1R1_ELIGIBLE_FOR_SEPARATE_S0_S13_PREREGISTRATION
  technical counter = 0/10
```

Každá technicky dokončená committed source-content vetva vynuluje counter,
aj keď potvrdí source-local exclusion. Nikdy nevzniká complete W10, C01
PASS/STOP, physical witness attempt, `A_RW1` verdict, score/depth/A3 zmena,
Q1R8, Python, solver, downstream fit, steam/completion alebo biologická
validácia.

```text
P4_WORK_ATOMS: 3_UNCHANGED
PHYSICAL_WITNESS_ATTEMPTS: 0_UNCHANGED
K4: 60/100_UNCHANGED
P5: 3.5/6_UNCHANGED
```

## 7. Výstupy a rozpočet

Celý V2 atóm:

```text
LIVE_SCIENTIFIC_ARTIFACTS:
  1 preregistration 289
  1 exact audited PowerShell implementation 289S
  1 immutable operation journal 289J
  1 immutable raw source archive 289A on success only
  1 result 290
LIVE_CENTRAL_REGISTERS_UPDATED:
  route event ledger; current/K4/P5 only after a real blocker/state closure
AUDIT_PACKAGE_COPIES: 0
PYTHON_PROCESSES: 0
```

289J je durable at-most-once dôkaz a po prvom uzavretí sa nemení. 289A je
externý primary-source raw, nie projektová rovnica. Jeho exact response-byte
SHA, zistená reprezentácia a veľkosť sa vykážu oddelene. Po publish sa
nemení. Result 290 vznikne až z exact 289J a 289A SHA/inventory alebo z
fail-closed technického journalu; event ledger nie je náhradou raw journalu.

## 8. Auditný handoff kapsul

```text
TASK_ID: A2K4-B6B2-10-H-RDIV-C01-RW1-Q1R1-V2-SOURCE-ARCHIVE-PREREG-FINAL-DELTA-REAUDIT-20260728-328R2
ROLE: physics_track_auditor
ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
ASSIGNED_AGENT_TASK_ID: /root/c01_q1r3_access_prereg_audit
ARTIFACT_AUTHOR_TASK_ID: /root
STATIC_AUDITOR_TASK_ID: /root/c01_q1r1_v2_source_impl_audit
INTERNAL_AUDITOR_TASK_ID: /root/c01_q1r3_access_prereg_audit
PACKAGE_CURATOR_TASK_ID: NOT_ASSIGNED_Q1R1_V2_PACKAGE_CURATOR
EXTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED_Q1R1_V2_EXTERNAL_AUDITOR
SEPARATION_OF_DUTIES_CHECK: author(/root)!=internal(/root/c01_q1r3_access_prereg_audit):PASS; author(/root)!=static(/root/c01_q1r1_v2_source_impl_audit):PASS; curator(NOT_ASSIGNED_Q1R1_V2_PACKAGE_CURATOR)!=external(NOT_ASSIGNED_Q1R1_V2_EXTERNAL_AUDITOR):PASS
ROUTE: A1_K1_A2_K4_P5.3g7_SM_v1_B6b-2.10_H_RDIV_C01_RW1_Q1R1_V2
CURRENT_PHASE: DRAFT_UNFROZEN_BEFORE_DIRECT_HTTP_SOURCE_ARCHIVE_ACCESS
PARENT_DECISION: Q1R1_V1_technical_cache_failure_2_of_2_packages1_failures1_of_10; progress_task326_recommends_one_different_source_archive_architecture; task328_initial_corrections_closed; task328R_requires_closed_TeX_loader_set_and_distinct_static_implementation_audit
CLAIM: one official same-paper source archive can resolve the full-text eligibility evidence boundary
NONCLAIMS: no source content yet; no S0-S13/W10/C01/score/depth/A3/witness change
ALLOWED_NEXT_ACTION: independent read-only preregistration audit only
ALLOWED_READS: exact fully-qualified inputs and mandatory ruleset; no network
ALLOWED_WRITES: none
FORBIDDEN_ACTIONS: network/source/search/open/download; edit; Python; infer source content; authorize run; score/depth/package change
IMMUTABLE_INPUT_PATHS_AND_SHA256: prereg287=EFB73C7203251362AD95E0E97D43252CD5ACBFE1D532F77F5E37FA05E09DFFF9; receipt287A=6DC658EF0276EFE35C3C98091290B0FD280DF2CB40017CC093F261EB392A52CA; result288=4717E2D6E773C1E58A493DA32B61521C81489E492B7E5A0FAA595E5A7DF1E994; D:/Teoria/tracks/A1/A1K1/A2/A2K4/HISTORY/00_EVENT_LEDGER.md=41CA8CBB6893A2CA9906FF505904E82783BB208F8196ACED20A83BC31900DE2D; historical_doc264=DA9F5FCACAD15FF8D00C6C582D05E05E47ED33F764FD05A0286D607E394F079A
FROZEN_EQUATIONS_AND_THRESHOLDS: one_at_most_once_GET_after_durable_REQUEST_RESERVED; HTTP200_no_redirect; body_10000_to_8MiB; raw_tar_or_exactly_one_gzip_member_to_tar; decompressed_32MiB_entry512_per_entry4MiB_ratio40_validation30s; strict_entry_types_paths_collisions; closed_loader_allowlist_plus_recursive_TeX_bibliography_style_closure_and_manual_all_text_member_inventory; absence_only_after_complete_source_archive_gate; G0_G3_all_PASS_for_eligibility
PREREG_SHA256: PENDING_AFTER_AUDIT
RULESET_PATHS_AND_SHA256: D:/Teoria/AGENTS.md=226710D6467FE923D6F2CBAFF02CE9235F1B48C07C4A9DACD95C6B06486B2B29; D:/Teoria/tracks/00_PROJECT_OPERATING_SYSTEM.md=519BDCBAE2CD9BF62351586E357DE3C9A28E60AD79CDB653661DD2821D65B6E7; D:/Teoria/tracks/00_READ_FIRST.md=3BE1654E58D51F0C7B2322B4C8D0CE3E7554A8599F479788B9F781244D930411; D:/Teoria/tracks/METHODOLOGY/05_WORKING_Methodology_Rules_and_Question_Register_SK.md=AB29543ACD4F132276DF59E1020EEA6FB3A042C78FAAA1B7DDD448F5479D0FF1
AUDITOR_RULESET_PATHS_AND_SHA256: same_live_internal_ruleset
AUDITOR_ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
RUN_AUTHORIZED: false
SOURCE_ACCESS_AUTHORIZED: false
TIMEOUT_AND_OUTPUT_GUARDS: exact_four_network_output_target_absence; prereg_then_exact_289S_source_freeze_distinct_static_audit_then_one_nonnetwork_SelfTest_then_progress_review_then_separate_authorization; journal_CreateNew_WriteThrough_FlushTrue_REQUEST_RESERVED_before_SendAsync; HttpClient_ResponseHeadersRead_identity_no_decompression_headers64KiB_internal60s_external120s; bounded_CreateNew_part; raw_tar_or_strict_single_gzip_member; archive_limits_and_path_type_collision_guards; no_filesystem_extraction; closed_loader_TeX_bibliography_style_closure_and_manual_all_text_inventory; exclusive_publish; caught_failure_temp_cleanup; crash_preserves_consumption
OUTPUT_PATHS: D:/Teoria/tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/289S_B6B2_10_Q1R1_V2_SOURCE_ARCHIVE_ACQUISITION.ps1; D:/Teoria/tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/289J_B6B2_10_Q1R1_V2_SOURCE_ARCHIVE_OPERATION_JOURNAL.txt; D:/Teoria/tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/289A_B6B2_10_Q1R1_ARXIV_2307_12080V2_SOURCE_ARCHIVE.tar.gz; D:/Teoria/tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/290_B6B2_10_H_RDIV_C01_RW1_Q1R1_V2_SOURCE_ARCHIVE_ELIGIBILITY_RESULT_SK.md
LIVE_FILE_BUDGET: max5_scientific_V2_including_prereg_implementation_journal_archive_success_only_result; one_route_event_ledger_batched; package_copies0
DONE_WHEN: auditor verifies corrected task326 ledger binding, durable at-most-once journal, exact HttpClient/temp/publish contract, strict bounded raw-tar-or-single-gzip archive validation, safe member paths/types/collisions, closed loader/bibliography/local-style TeX closure with manual all-text inventory, distinct exact implementation static-audit and fixture lifecycle, G0-G3 branches, inherited accounting and nonclaims
NEXT_ROLE: main_orchestrator
```
