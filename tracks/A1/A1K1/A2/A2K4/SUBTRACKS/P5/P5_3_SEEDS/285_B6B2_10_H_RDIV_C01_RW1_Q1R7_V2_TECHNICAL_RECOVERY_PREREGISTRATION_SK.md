# Q1R7-V2 — predregistrácia technickej obnovy od O2

**Stav:** `DRAFT_UNFROZEN / NO_SOURCE_OPERATION / NO_PYTHON`  
**Dátum:** 2026-07-28  
**Route:** `A1_K1_A2_K4 / P5.3 / B6b-2.10 / H_RDIV-MF1-v1 / C01-RW1 / Q1R7`  
**Autor teórie:** Martin Jambor  
**Autor procesného artefaktu:** Codex, task `/root`  
**Účel:** odstrániť iba technickú a provenance slepú vetvu Q1R7-V1 bez
zmeny kandidáta, fyziky, W10 passportu alebo source-operation capu.

## 1. Autoritatívny stav a immutable V1 transakcia

Q1R7 je stále ten istý ordered kandidát:

```text
FAMILY: F-A
QUERY: Q1
ORDERED_RANK: 7
TITLE: Hydrodynamics of ultra-relativistic bubble walls - ScienceDirect
WORK_TITLE: Hydrodynamics of ultra-relativistic bubble walls
PII: S0550321316000535
PUBLISHER_URL: https://www.sciencedirect.com/science/article/pii/S0550321316000535
ORDER_SOURCE_SHA256: DA9F5FCACAD15FF8D00C6C582D05E05E47ED33F764FD05A0286D607E394F079A
ORDER_SOURCE_ROW: 111
```

V1 transakcia sa nemení ani neopravuje:

```text
PREREG283_SHA256: E9F7AD9237BE24EB7CB4CF8EE80F58E1B1D38D6834D83FB442A5A909BD47B3B6
RUNNER_V1_SHA256: 1CBA6274580D5DF7CD88F24A5C42C50904DC8593192F644F353B49E27391BC2A
JOURNAL283C_SHA256: C104472F6079E5E5CE16680E4B2B3F8E704FF5E07ECB566B53BDC0250DD7BD2F
RESULT284_SHA256: 879AA3B9F9B5806E101DD1E1BAE4D5EC61ADD1B2711342FD3EC047099827F7FA
V1_TRANSACTION_STATUS: TECHNICAL_FAILURE_NO_PHYSICAL_INFERENCE
HISTORICAL_PACKAGES_TOTAL_BEFORE_V2: 1
CONSECUTIVE_TECHNICAL_FAILURES_BEFORE_V2: 1/10
CUMULATIVE_SOURCE_OPERATIONS_BEFORE_V2: 1/6
O1: CONSUMED_HTTP_403_BODY_READ_ADAPTER_FAILURE
O2_O6: NOT_CONSUMED
```

V2 nesmie meniť, mazať, dopĺňať ani znovu použiť 283A/283B/283C/284,
historický temp adresár alebo V1 runner. V1 `S13` ostáva FAIL; V2 je nová
transakcia toho istého kandidáta a tej istej technickej problémovej línie.

## 2. Read-only reachability rozhodnutie

### 2.1 Strict V1 O2 continuation — zamietnuté ako nedosiahnuteľné

V1 §3 vyžaduje, aby Crossref record bol eligible iba po neprázdnom author-sete
z O1. Frozen V1 runner navyše:

1. spracuje Crossref iba pri `o1Eligible=true`;
2. zneplatní každé neskoršie prijatie pri `o1Eligible=false`;
3. skutočný O1 skončil `HTTP 403`, nulovým body a bez bound author-setu.

Samotné spustenie pôvodného O2 by preto mohlo spotrebovať operáciu, ale podľa
V1 kontraktu nemôže založiť eligible DOI/author binding ani accepted source.
Taký krok by nemal rozumnú možnosť fyzikálneho informačného zisku.

### 2.2 O1 reacquisition — nezvolené

Opakovanie publisher requestu by bolo novou, kumulatívne druhou source
operáciou, nie resetom O1. Ani opravené čítanie 403 body však nemení V1
požiadavku na úspešný `2xx` O1 binding. Reacquisition preto neodstraňuje
identifikovanú provenance závislosť a zbytočne by spotrebovala zostávajúci
cap. O1 sa vo V2 nesmie spustiť.

### 2.3 Zvolený successor

```text
REACHABILITY_DECISION: V2_AMENDED_O2_CONTINUATION_NO_O1_REACQUISITION
PHYSICS_CHANGE: NONE
CANDIDATE_IDENTITY_CHANGE: NONE
SOURCE_QUERY_CHANGE: NONE_FOR_O2_AND_O3
PROVENANCE_CHANGE: O2_MAY_ESTABLISH_BOUND_AUTHOR_AND_DOI_SET_WITHOUT_O1
```

Zmena je obmedzená na acquisition/provenance contract. Nepridáva nový web
search, mirror, identifikátor, fyzikálny objekt ani voľný fallback.

## 3. Kumulatívny schedule O2–O6

Jedna source operation zostáva jeden začatý top-level HTTP request. Skipped
krok nespotrebuje operáciu. Celoživotný Q1R7 cap zostáva `6`; V2 začína na
`1/6` a smie odoslať najviac ordinals `2..6`. Siedmy request je zakázaný.

1. **O2 / cumulative ordinal 2 — Crossref exact frozen query**

   ```text
   GET https://api.crossref.org/works?query=S0550321316000535&rows=3&select=DOI%2Ctitle%2Cauthor%2CURL
   ```

   Eligible je práve jeden record, ktorý má exact normalized work title,
   neprázdny normalized full-author set, práve jeden validný normalized DOI a
   `URL`, ktorého normalized DOI je ten istý DOI. Nula alebo viac eligible
   records je terminal evidence-incomplete, nie licencia meniť query.

2. **O3 / cumulative ordinal 3 — arXiv exact-title query**

   ```text
   GET https://export.arxiv.org/api/query?search_query=ti%3A%22Hydrodynamics%20of%20ultra-relativistic%20bubble%20walls%22&start=0&max_results=3&sortBy=relevance&sortOrder=descending
   ```

   Eligible je práve jeden entry s exact normalized title a presne rovnakým
   normalized full-author setom ako O2. Ak entry obsahuje DOI, musí byť exact
   rovnaký ako O2 DOI. Canonical arXiv ID musí prejsť V1 syntax guardom.

3. **O4 / cumulative ordinal 4 — canonical arXiv abstract**

   Vykoná sa iba pri jedinom eligible O2 a O3 recorde. URI je exact
   `https://arxiv.org/abs/<canonical-ID>`. Body musí zopakovať exact title,
   celý author-set a canonical ID; prítomný DOI musí súhlasiť s O2.

4. **O5 / cumulative ordinal 5 — canonical arXiv e-print**

   Vykoná sa iba po O4 PASS. URI je exact
   `https://export.arxiv.org/e-print/<canonical-ID>`. Source archive/PDF sa
   klasifikuje presne podľa immutable document283 §5. Aj úplný O5 zdroj je
   zatiaľ iba `PROVISIONAL_COMPLETE_SOURCE_PENDING_O6_PII_BINDING`.

5. **O6 / cumulative ordinal 6 — mandatory DOI→PII binding**

   Vykoná sa iba po jednom O2 DOI a provisional complete O5 source. Request
   je exact `https://doi.org/<segment-wise RFC3986 DOI>`. Redirect chain musí
   skončiť na HTTPS `sciencedirect.com` alebo jeho subdoméne a final path musí
   obsahovať exact segment `/pii/S0550321316000535`; explicitný non-443 port,
   userinfo, downgrade, loop alebo iný PII failne binding. HTTP 4xx na
   správnom final PII URL neznamená content PASS, ale môže potvrdiť iba
   DOI→PII redirect identity, pretože complete content už pochádza z O5.

Accepted source vznikne iba pri O2+O3+O4 identity PASS, O5 complete-source
PASS a O6 DOI→PII PASS. Po prvom nesplnenom precondition sa závislé kroky
zapíšu `SKIPPED_PRECONDITION`; nijaký slot sa nepresunie na iný request.

Normalizácia title, authors, DOI a URI, transportné hranice a complete-source
classifier sa preberajú byte-for-byte významom z immutable document283. Ak
V2 runner potrebuje text pravidla zmeniť, prereg sa pred freeze zastaví.

## 4. Povinné lokálne nonnetwork fixtures pred source operáciou

V2 runner musí mať explicitný `-SelfTest` mód, ktorý nemôže vytvoriť
285A/285B/285C/286, nemôže otvoriť socket ani zvýšiť source counter. Na
presne tom istom runner hashi musia pred nezávislým static auditom prejsť:

1. `F01_BYTE_ARRAY_READ_API`: PowerShell 7 načíta 0, 1, 65536 a 65537 bytes
   cez overload `ReadAsync(byte[], offset, count, CancellationToken)` alebo
   synchronný byte-array overload; žiadne volanie `byte[].AsMemory`;
2. `F02_HTTP403_EMPTY_BODY`: lokálne skonštruovaný 403 response s prázdnym
   streamom vráti `Body=[byte[]]@()`, status 403, nulový length a bez výnimky;
3. `F03_HTTP403_NONEMPTY_BODY`: lokálny 403 body sa prečíta a hashne celý bez
   toho, aby sa 403 zmenilo na eligible content;
4. `F04_ARRAY_SHAPE_0_1_MANY`: PDF-link, title, author, DOI, Crossref item a
   arXiv match kolekcie sú vždy materializované ako arrays; `.Count` sa nikdy
   nevolá nad `$null` ani scalarom;
5. `F05_PRIOR_JOURNAL_BINDING`: read-only načítanie 283C potvrdí exact SHA,
   V1 prereg/runner hash, ordinal 1 a absenciu ordinalov 2..6;
6. `F06_CUMULATIVE_CAP`: state machine začína `consumed=1`, povoľuje iba
   ordinals 2..6, odmietne duplicate/out-of-order/ordinal 7 a skipped slot
   nezvýši request count;
7. `F07_FRESH_TARGET_COLLISION`: prítomnosť ktoréhokoľvek 285A/285B/285C/286
   alebo V2 temp cieľa skončí fail-closed pred networkingom;
8. `F08_TRANSACTION_SUCCESS_FAILURE`: lokálna simulácia overí journal-first,
   source-first, receipt-last commit order, cleanup iba V2 tempu a zachovanie
   V1 forenzných artefaktov pri úspechu aj chybe;
9. `F09_NETWORK_DISABLE_GUARD`: `-SelfTest` vyhodí FAIL, ak sa dosiahne
   request dispatcher; fixture úspech musí mať `NETWORK_REQUESTS=0`.

Každý fixture vypíše deterministické `PASS/FAIL`, runner skončí nonzero pri
jedinom FAIL a súhrn musí obsahovať `9/9 PASS`, `NETWORK_REQUESTS=0`,
`PYTHON_PROCESSES=0`. Fixture úspech nie je source operácia, nevynuluje
`1/10` counter a nepridáva vedecký výsledok.

## 5. Fresh transakčné cesty a publikácia

Povolené live artefakty celej V2 línie sú najviac tieto:

```text
285  tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/285_B6B2_10_H_RDIV_C01_RW1_Q1R7_V2_TECHNICAL_RECOVERY_PREREGISTRATION_SK.md
285A tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/285A_B6B2_10_Q1R7_V2_PRIMARY_SOURCE_BLOB.bin
285B tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/285B_B6B2_10_Q1R7_V2_COMPLETE_SOURCE_RECEIPT.txt
285C tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/285C_B6B2_10_Q1R7_V2_SOURCE_OPERATION_JOURNAL.txt
286  tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/286_B6B2_10_H_RDIV_C01_RW1_Q1R7_V2_S0_S13_RESULT_SK.md
```

Transient implementation je iba `.q1r7_v2_acquire.ps1`; nie je vedeckým
výstupom. V2 používa nový temp názov a nesmie čistiť V1 temp. Pred source
operation musia 285A/285B/285C/286 aj V2 temp absent. 285C vznikne prvý cez
exclusive `CreateNew` a musí obsahovať prereg hash, V2 runner hash, všetky
štyri V1 immutable hashe, `STARTING_CUMULATIVE_SOURCE_OPERATIONS=1` a
`STARTING_CONSECUTIVE_TECHNICAL_FAILURES=1`.

Každý skutočný request dostane `REQUEST_RESERVED` + `Flush(true)` pred
odoslaním a `REQUEST_COMPLETED` + `Flush(true)` po návrate. Commit order ostáva
source temp→285A, finálny journal hash a receipt temp→285B posledný. Pri clean
evidence-incomplete výsledku 285A nevznikne, ale 285B je stále commit marker
platnej dokončenej transakcie. Kolízia, orphan alebo abnormal exit je iba
technický incident V2.

## 6. Výsledok, počítadlá a nonclaims

S0–S13, outcome precedence a zákaz cross-source fyzikálneho skladania sa
preberajú z document283 §7–§8. Navyše:

```text
IF V2_TECHNICAL_FAILURE:
  historical_packages_total = 2
  consecutive_technical_failures = 2/10
  physical_witness_attempts = 0

IF V2_COMPLETES_WITH_VALID_COMMIT_RECEIPT_AND_INTERPRETABLE_SOURCE_COVERAGE_RESULT:
  historical_packages_total = 2
  consecutive_technical_failures = 0/10
  physical_witness_attempts = 0 unless complete W10 survives independent audit
```

Clean `SOURCE_UNIVERSE_NOT_CERTIFIED` je source-coverage REVIEW, nie technická
chyba a nie fyzikálna refutácia. P4 work atom sa môže zmeniť `3→4` iba podľa
document283 complete-source + independent result audit podmienky. Physical
witness attempt sa môže zmeniť `0→1` iba pri kompletnom W10 kandidátovi po
nezávislom audite a prijatí hlavným orchestrátorom.

Táto preregistrácia:

- nemení `K4=60/100`, `P5=3.5/6`, P5.4, A3 ani teóriu;
- netvrdí, že Q1R7 obsahuje W10 alebo že je fyzikálne relevantný;
- nepovoľuje Python, solver, steam/completion ansatz, S8/H0 fit, P5.4/G8/G9;
- nepovoľuje source operation, kým prereg, runner a fixtures nemajú oddelený
  nezávislý audit, exact hashe a main freeze/authorization.

## 7. Handoff capsule pre prereg audit

```text
TASK_ID: A2K4-B6B2-10-H-RDIV-C01-RW1-Q1R7-V2-RECOVERY-PREREG-AUDIT-20260728-298
ROLE: physics_track_auditor
ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
ASSIGNED_AGENT_TASK_ID: /root/c01_q1r3_access_prereg_audit
ARTIFACT_AUTHOR_TASK_ID: /root
STATIC_AUDITOR_TASK_ID: /root/c01_q1r3_access_prereg_audit
INTERNAL_AUDITOR_TASK_ID: /root/c01_q1r3_access_result_audit
PACKAGE_CURATOR_TASK_ID: NOT_ASSIGNED_Q1R7_V2_PACKAGE_CURATOR
EXTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED_Q1R7_V2_EXTERNAL_AUDITOR
SEPARATION_OF_DUTIES_CHECK: /root != /root/c01_q1r3_access_prereg_audit; /root != /root/c01_q1r3_access_result_audit; NOT_ASSIGNED_Q1R7_V2_PACKAGE_CURATOR != NOT_ASSIGNED_Q1R7_V2_EXTERNAL_AUDITOR
ROUTE: A1_K1_A2_K4/P5.3/B6b-2.10/H_RDIV-MF1-v1/C01-RW1/Q1R7
CURRENT_PHASE: V2_DRAFT_UNFROZEN_PREREGISTRATION
ALLOWED_NEXT_ACTION: independent read-only prereg audit only
ALLOWED_READS: mandatory bootstrap; document285; immutable 264/283/283C/284; V1 runner; PF-130; current/K4/P5 plans; event ledger through task297
ALLOWED_WRITES: NONE_FOR_AUDITOR
FORBIDDEN_ACTIONS: edit; network; source operation; Python; runner execution; physics verdict; score/depth/run change
IMMUTABLE_INPUT_PATHS_AND_SHA256: doc264=DA9F5FCACAD15FF8D00C6C582D05E05E47ED33F764FD05A0286D607E394F079A; doc283=E9F7AD9237BE24EB7CB4CF8EE80F58E1B1D38D6834D83FB442A5A909BD47B3B6; journal283C=C104472F6079E5E5CE16680E4B2B3F8E704FF5E07ECB566B53BDC0250DD7BD2F; result284=879AA3B9F9B5806E101DD1E1BAE4D5EC61ADD1B2711342FD3EC047099827F7FA; runnerV1=1CBA6274580D5DF7CD88F24A5C42C50904DC8593192F644F353B49E27391BC2A; PFledger=EDCE33641F6D78D8C49B0967BCD45025583BF7785E31161928FE054A88677515; current=D4CEE4C96F8872B9C988C4E87505F40282FAC6BEE5F87F61CE8C9D83DDFC38E0; K4=6016E7A2C92B792B8408DACF1685683E5F2937688408D6623A11E1E3F31F6A5B; P5=83BF4C2F4EA50ED9EC39DD9F7D86CDD044748013759B5B2A3E1F226ACE720121; event_through297=14194508DD4EC2DC716A5921C128B4C8F6506D0F4FA022BACDB0A3421748064C
PREREG_SHA256: PENDING_AFTER_INDEPENDENT_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: auditor chat response only; future 285A/285B/285C/286 exact paths in section5
DONE_WHEN: auditor verifies inherited 1/6 and 1/10 counters; reachability reasoning; no O1 retry; deterministic O2-O6 identity binding; cumulative cap; nonnetwork fixtures; fresh transaction paths; accounting; nonclaims; returns PASS or exact corrections
NEXT_ROLE: main_orchestrator correction/freeze; then runner authoring and separate static audit; still no source operation
```

## 8. Stav pred auditom

```text
Q1R7_ROUTE_STATUS: REVIEW_TECHNICAL_UNRESOLVED
Q1R7_V2_STATUS: DRAFT_UNFROZEN
CUMULATIVE_SOURCE_OPERATIONS: 1/6
CONSECUTIVE_TECHNICAL_FAILURES: 1/10
HISTORICAL_PACKAGES_TOTAL: 1
Q1R8_AUTHORIZED: false
P4_WORK_ATOMS: 3
PHYSICAL_WITNESS_ATTEMPTS: 0
K4: 60/100
P5: 3.5/6
RUN_AUTHORIZED: false
SOURCE_ACQUISITION_AUTHORIZED: false
PYTHON_PROCESSES: 0
```
