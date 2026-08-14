# B6b-2.10 / C01-RW1 / Q1R1-V3 — preregistrácia priameho source archívu cez kanonický host

**Stav:** `DRAFT_UNFROZEN / NO_NETWORK / NO_RUN`  
**Dátum:** 2026-07-28  
**Autor teórie:** Martin Jambor  
**Autor preregistrácie a budúci tvorca skriptu:** OpenAI Codex, hlavný orchestrátor  
**Route:** `A1_K1_A2_K4_P5.3g7_SM_v1_B6b-2.10_H_RDIV_C01_RW1_Q1R1_V3`

## 1. Účel a autoritatívny vstupný stav

Q1R1 naďalej potrebuje úplný same-paper zdroj, aby sa dali vykonať iba
eligibility brány `G0–G3`. V2 nezískala obsah: jej zmrazený priamy GET na
`export.arxiv.org` dostal HTTP `301`, redirect nesledoval a nevytvoril temp,
archív ani výsledok.

```text
AUTHORITATIVE_PARENT_STATE: REVIEW_TECHNICAL_UNRESOLVED_NO_PHYSICAL_INFERENCE
Q1R1_ELIGIBILITY: UNRESOLVED
V2_ARCHIVE_OPERATIONS: 1/1_TERMINAL
CUMULATIVE_SOURCE_OPERATIONS: 3
HISTORICAL_PACKAGES_TOTAL: 2
CONSECUTIVE_TECHNICAL_FAILURES: 2/10
K4_SCORE: 60/100_UNCHANGED
P5_SCORE: 3.5/6_UNCHANGED
A3_TRANSITION: NOT_AUTHORIZED
```

V3 nie je retry V2, nesleduje jej redirect a neodvodzuje jeho nezaznamenaný
`Location`. Je to nová transportná architektúra s vlastným preregistračným
hashom, implementačným auditom, offline SelfTestom a samostatnou autorizáciou.

## 2. Nezávislý pôvod exact URL

Exact V3 URL vzniká iba z dvoch už zmrazených lokálnych autorít:

1. dokument 264 viaže paper a arXiv ID na kanonický host
   `https://arxiv.org/abs/2307.12080`;
2. dokument 277 zachytáva už úspešne použitú oficiálnu source-path gramatiku
   `/e-print/<arXiv-ID>`; nejde o dôkaz obsahu Q1R1 ani o V2 redirect target;
3. verzia `v2` je zmrazená v Q1R1 dokumentoch 264/289 a nemení sa po výsledku.

```text
DOC264_SHA256: DA9F5FCACAD15FF8D00C6C582D05E05E47ED33F764FD05A0286D607E394F079A
DOC277_SHA256: C57404A73B558B4EF53D314EE9669347CBB94D35378CC2B67145864CFC5EBD56
V2_PREREG289_SHA256: F141E8781AE61E863D795224C00A8D0F0D6411DCEBF2239ED7750A46D9142225
V2_FROZEN_R2_SHA256: E958635FE621E8DF030E685197825BC5DD9E19CAAFCF8B46A8E546433BC94317
V2_TERMINAL_JOURNAL_SHA256: 7CBA9D46F2FC5A644FD79E26877DC1B7A69AFA020F1910CF68C112EA2FBEE2FA
V3_EXACT_URL: https://arxiv.org/e-print/2307.12080v2
URL_DERIVATION_USES_V2_LOCATION: false
```

Ak nezávislý audit neuzná toto zloženie hostu, cesty a version bindingu,
preregistrácia sa nezmrazí a sieť sa nepovolí.

## 3. Jediná povolená V3 sieťová operácia

```text
OPERATION_ID: V3-O1
METHOD: GET
URL: https://arxiv.org/e-print/2307.12080v2
REDIRECTS: forbidden
RETRIES: forbidden
FALLBACKS: forbidden
SEARCH_OR_OTHER_PAPER: forbidden
ACCEPT_ENCODING: identity
USER_AGENT: Teoria-Q1R1-V3-SourceAudit/1.0
INTERNAL_HTTP_TIMEOUT: 60_s
EXTERNAL_PROCESS_TIMEOUT: 120_s
HTTP_BODY_RANGE: 10000_to_8388608_bytes
```

Povolený je iba exact HTTP `200`. Odlišný status je technické zlyhanie bez
čítania body a bez publikovania archívu. `HttpClientHandler` musí mať
`AllowAutoRedirect=false` a automatickú dekompresiu vypnutú.

Pred `SendAsync` sa cez `CreateNew + WriteThrough + Flush(true)` zapíše
jediný journal s `REQUEST_RESERVED`. Od tohto okamihu je V3-O1 spotrebovaná
aj pri timeoute, výnimke, páde alebo neúspešnom publishi. Retry nie je povolený.

## 4. Zlepšený terminálny dôkaz redirectu

V3 nesmie redirect nasledovať, ale pri non-200 odpovedi musí bezpečne
zachytiť, prečo transport skončil:

```text
HTTP_STATUS
LOCATION_VALUE_COUNT
LOCATION_PRESENT = LOCATION_VALUE_COUNT > 0
LOCATION_CLASS = ABSENT | SAME_ORIGIN_HTTPS | ALLOWED_ARXIV_HOST_HTTPS | OTHER_OR_INVALID
LOCATION_VALUES_SHA256 = SHA256 deterministicky rámcovaných UTF-8 bajtov
                         exact string hodnôt v poradí TryGetValues
LOCATION_NORMALIZED = exact kanonická serializácia jediného povoleného URI;
                      inak ABSENT
RESPONSE_BYTES = 0 pre non-200 vetvu
FAILURE_GUARD
```

`Location` sa číta iba cez `response.Headers.TryGetValues("Location", ...)`.
Digest nie je hash wire bytes, ku ktorým .NET API nedáva prístup. Je presne:

```text
SHA256(
  UTF8("LOCATION_VALUES_V1\0") ||
  UInt32BE(value_count) ||
  pre každú hodnotu v enumeration order:
    UInt32BE(UTF8_byte_count) || UTF8(exact_TryGetValues_string)
)
```

Nula hodnôt dá `ABSENT`. Viac než jedna hodnota dá `OTHER_OR_INVALID` a
`LOCATION_NORMALIZED=ABSENT`; digest zachová všetky hodnoty jednoznačne.
Presne jedna hodnota sa nesmie trimovať, nesmie mať leading/trailing
whitespace ani ASCII control `U+0000..U+001F`/`U+007F`. Relatívna hodnota sa
rieši cez `new Uri(exact_V3_request_uri, value)`; absolútna sa používa priamo.

Po resolve platí v tomto poradí:

1. parse failure, UTF-8 dĺžka nad `2048`, control znak, schéma iná než exact
   `https`, non-default port, userinfo, query alebo fragment →
   `OTHER_OR_INVALID`;
2. exact host `arxiv.org` a port `443` → `SAME_ORIGIN_HTTPS`;
3. exact host `export.arxiv.org` a port `443` →
   `ALLOWED_ARXIV_HOST_HTTPS`;
4. každý iný host → `OTHER_OR_INVALID`.

Pre dve povolené triedy je `LOCATION_NORMALIZED` presne výsledok
`resolved.GetComponents(UriComponents.SchemeAndServer | UriComponents.Path,
UriFormat.UriEscaped)`. Pred uložením musí aj táto serializácia prejsť rovnaký
control a `<=2048` UTF-8-byte guard. Pri inej triede sa raw ani normalizovaná
hodnota neukladá.

`LOCATION_NORMALIZED` je forenzný údaj, nie autorizácia, nový URL ani povolenie
na nasledovanie. Každý ďalší transportný krok by stále potreboval novú
preregistráciu. Neplatný alebo neprípustný Location sa neukladá raw; zostane
iba jeho SHA-256 a trieda.

Offline SelfTest musí mať exact fixtures pre nula/jedna/viac hodnôt, digest
framing a poradie, relatívny same-origin HTTPS cieľ, absolútny povolený arXiv
host, a osobitne zakázaný whitespace/control/overlength/non-HTTPS/non-default-
port/userinfo/query/fragment/other-host prípad. Žiadny fixture nesmie otvoriť
sieť.

## 5. Prenesený archive a source-closure kontrakt

V3 nemení vedecký ani archive parser kontrakt preregistrácie 289. Budúca
implementácia musí vzniknúť ako byte-identická kópia zmrazeného R2 pred
presne auditovanou deltou. Bez opätovného otvorenia rozhodnutí sa prenášajú:

- raw TAR alebo presne jeden GZIP member → TAR;
- CRC/ISIZE/FHCRC/EOF a little-endian guardy;
- decompressed limit `32 MiB`, najviac `512` entries, `4 MiB` na entry,
  compression ratio `40`, validation deadline `30 s`;
- strict TAR path/type/padding/collision kontrakt bez filesystem extraction;
- strict UTF-8 a uzavretý TeX loader allowlist;
- recursive same-archive dependency closure, exact ordinal paths, lokálne
  `.cls/.sty/.bib` pravidlá a manuálny all-text inventory;
- presne jeden main root s názvom paperu a identitami `Giombi`, `Hindmarsh`;
- eligibility brány `G0–G3` a všetky nonclaims preregistrácie 289.

Ak statický audit nájde inú zmenu parsera, limitu, closure alebo G0–G3
vetvenia, výsledok je `STATIC_AUDIT_BLOCKED / NO_RUN`.

## 6. Povolená implementačná delta

Budúci script `291S` smie voči frozen R2 meniť iba:

1. identity tasku, exact názov a V3 output cesty;
2. expected hash tejto preregistrácie po freeze;
3. URL, user-agent a authorization marker na V3;
4. jednorazový journal `291J`, temp `.291A`, archive `291A` a result `292`;
5. bezpečné Location evidence z oddielu 4 a jeho offline fixtures;
6. V3 účtovanie z oddielu 9.

Povinné zamýšľané cesty:

```text
291S_B6B2_10_Q1R1_V3_CANONICAL_HOST_SOURCE_ARCHIVE_ACQUISITION.ps1
291J_B6B2_10_Q1R1_V3_SOURCE_ARCHIVE_OPERATION_JOURNAL.txt
.291A_B6B2_10_Q1R1_V3_SOURCE_ARCHIVE.part
291A_B6B2_10_Q1R1_ARXIV_2307_12080V2_SOURCE_ARCHIVE.tar.gz
292_B6B2_10_H_RDIV_C01_RW1_Q1R1_V3_SOURCE_ARCHIVE_ELIGIBILITY_RESULT_SK.md
```

Všetky štyri operation output targety musia pred autorizáciou neexistovať.
Official publish používa `CreateNew`/exclusive move a cieľ sa nikdy neprepisuje.

## 7. Povinný statický audit, freeze a SelfTest

Poradie je fail-closed:

1. nezávislý audit a obsahové uzavretie tejto preregistrácie;
2. SHA freeze preregistrácie mimo nej v append-only route ledgeri;
3. autor vytvorí jediný `291S` successor v povolenej delte;
4. iný agent vykoná full static audit a exact R2→291S delta audit;
5. orchestrátor zmrazí SHA `291S`;
6. presne jeden offline `-SelfTest`; všetky fixtures musia PASS;
7. mandatory progress review;
8. až samostatný ledger append smie povoliť jediný `-Acquire` s exact hashom
   autorizačného ledgera.

Neúspešný audit alebo SelfTest nepoužije sieť. Versioned correction je možná
iba pre presný auditovaný implementačný defect; frozen skript sa neupravuje
ani nespúšťa druhý raz. Python nie je povolený.

## 8. Eligibility vetvenie a nonclaims

Po úspešnom immutable archive publishi sa bez ďalšej siete vykoná exact
G0–G3 source audit z preregistrácie 289; definície sa prenášajú doslovne:

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

Absencia sa smie tvrdiť iba po complete source closure a manuálnom all-text
inventory. Rovnaké PASS/REVIEW vetvy ako v 289 zostávajú zmrazené.

V3 nikdy sama nepotvrdí W10, C01, fyzický witness, `A_RW1`, D03–D11, P5.4,
G8/G9, S8/H0 fit, biologickú analógiu, score, hĺbku ani A3. Technický status,
redirect alebo source-local absencia nie sú smrť teórie.

## 9. Zmrazené účtovanie

```text
IF NO REQUEST_RESERVED:
  V3_OPERATIONS = 0/1
  cumulative_source_operations = 3
  historical_packages_total = 2
  consecutive_technical_failures = 2/10

IF REQUEST_RESERVED AND TECHNICAL_FAILURE:
  V3_OPERATIONS = 1/1_TERMINAL
  cumulative_source_operations = 4
  historical_packages_total = 3
  consecutive_technical_failures = 3/10
  outcome = TECHNICAL_FAILURE_NO_PHYSICAL_INFERENCE

IF ARCHIVE_PUBLISHED_AND_SOURCE_AUDIT_TERMINATES:
  V3_OPERATIONS = 1/1_TERMINAL
  cumulative_source_operations = 4
  historical_packages_total = 3
  consecutive_technical_failures = 0/10
  outcome = exact_G0_G3_branch_from_prereg289
```

SelfTest, static audit a compile/help nepočítajú source operáciu a nevynulujú
counter. Úspešný committed source-content výsledok counter vynuluje aj v
prípade source-local REVIEW alebo exclusion.

## 10. Súborový rozpočet a externý audit

```text
LIVE_SCIENTIFIC_ARTIFACTS_V3_MAX: 5
  prereg291
  implementation291S
  terminal_journal291J_after_request_only
  archive291A_on_success_only
  result292_on_success_only
LIVE_CENTRAL_REGISTERS_UPDATED_AT_COHERENT_CLOSURE_MAX: 4
AUDIT_PACKAGE_COPIES_NOW: 0
```

V2 technické zlyhanie nedostane samostatný externý balík. Podľa R6.1 sa
priloží k najbližšiemu ucelenému Q1R1 výsledku alebo významnému route blockeru.

## 11. Handoff kapsul pre audit preregistrácie

```text
TASK_ID: A2K4-B6B2-10-H-RDIV-C01-RW1-Q1R1-V3-TRANSPORT-PREREG-AUDIT-20260728-361
ROLE: math_script_auditor
ROLE_CONFIG_SHA256: 028FD63B14B9C39AD896A62CBC5EBFB5EBD76BE95144B21B8C79D9D8334F89A4
ASSIGNED_AGENT_TASK_ID: /root/c01_q1r1_v2_access_failure_audit
ARTIFACT_AUTHOR_TASK_ID: /root
STATIC_AUDITOR_TASK_ID: /root/c01_q1r1_v2_source_impl_audit_r1
INTERNAL_AUDITOR_TASK_ID: /root/c01_q1r1_v2_access_failure_audit
PACKAGE_CURATOR_TASK_ID: NOT_ASSIGNED_Q1R1_V3_PACKAGE_CURATOR
EXTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED_Q1R1_V3_EXTERNAL_AUDITOR
SEPARATION_OF_DUTIES_CHECK: author_root_neq_prereg_auditor_PASS; author_root_neq_future_static_auditor_PASS; no_package_roles_active
ROUTE: A1_K1_A2_K4_P5.3g7_SM_v1_B6b-2.10_H_RDIV_C01_RW1_Q1R1_V3
CURRENT_PHASE: DRAFT_UNFROZEN_TRANSPORT_PREREGISTRATION
ALLOWED_NEXT_ACTION: independent_read-only_preregistration_audit_only
ALLOWED_READS: mandatory_role_bootstrap; exact_doc264_doc277_prereg289_R2_journal289J; exact_prereg291; route_ledger_tasks357R_359_360
ALLOWED_WRITES: none
FORBIDDEN_ACTIONS: network_source_search_open_download; execute_or_parse_scripts; SelfTest; Acquire; Python; edit; freeze; infer_V2_Location_or_paper_content; change_verdict_score_depth_counter_or_A3
IMMUTABLE_INPUT_PATHS_AND_SHA256: doc264=DA9F5FCACAD15FF8D00C6C582D05E05E47ED33F764FD05A0286D607E394F079A; doc277=C57404A73B558B4EF53D314EE9669347CBB94D35378CC2B67145864CFC5EBD56; prereg289=F141E8781AE61E863D795224C00A8D0F0D6411DCEBF2239ED7750A46D9142225; frozen_R2=E958635FE621E8DF030E685197825BC5DD9E19CAAFCF8B46A8E546433BC94317; terminal_289J=7CBA9D46F2FC5A644FD79E26877DC1B7A69AFA020F1910CF68C112EA2FBEE2FA
PREREG_SHA256: PENDING_AFTER_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: advisory_response_only
DONE_WHEN: auditor verifies independent URL derivation; no V2 redirect inference; at-most-once lifecycle; safe Location evidence; exact inherited archive/TeX/G0-G3 contract; implementation delta; counters; output guards and nonclaims; returns PASS or exact correction list
NEXT_ROLE: main_orchestrator
```
