# B6b-2.10 — Q1R3 exact-source accessibility-recovery preregistrácia

**Task:** `A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R3-ACCESS-PREREG-20260727-177`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.10`  
**Autor teórie:** Martin Jambor  
**Formalizácia:** Codex, hlavný orchestrátor  
**Stav:** `DRAFT_PREREGISTRATION / EXACT_Q1R3_ACCESS_RECOVERY_ONLY / NO_SEARCH_YET / NO_PHYSICS_SCREEN / NO_PYTHON`

## 1. Dôvod a jediný cieľ

Prijatý dokument 264 uzavrel iba
`REVIEW_SEARCH_COVERAGE_INCOMPLETE_NO_PHYSICAL_INFERENCE`. Prvý eligible F-A
zdroj v frozen poradí je:

```text
title: Model-dependent analysis method for energy budget of the cosmological
       first-order phase transition
authors: Xiao Wang; Chi Tian; Fa Peng Huang
journal identity: JCAP07(2023)006
DOI: 10.1088/1475-7516/2023/07/006
frozen rank: Q1R3; Q1R4 je duplicate
```

Jediným cieľom recovery atómu je získať verifikovateľný full text toho istého
článku s čitateľnými action/EOM/energy rovnicami, aby sa mohol obnoviť už
zmrazený S0–S13 screen. Tento atóm sám nevykonáva fyzikálnu klasifikáciu a
nesmie nájsť náhradného kandidáta.

## 2. Frozen identity a exact recovery query

Jediné povolené `search_query` volanie je:

```text
"Model-dependent analysis method for energy budget of the cosmological first-order phase transition" "Xiao Wang" "Chi Tian" "Fa Peng Huang"
```

Payload obsahuje práve tento jeden query, `response_length="long"`, bez
recency alebo domain filtra a bez pagination/rewrite. Query slúži iba na
nájdenie canonical publisher, arXiv/autorského preprintu alebo
author-controlled/inštitucionálneho full-text záznamu toho istého článku.

Hit je identity-eligible iba ak súčasne platí:

1. normalized exact title match;
2. autorstvo obsahuje Wang, Tian a Huang alebo DOI/journal metadata vytvárajú
   explicitnú exact väzbu na vyššie zmrazenú identitu;
3. nejde o iný článok, review, citáciu, index bez full-text cesty ani title
   collision.

Výsledky iných zdrojov sa zalogujú ako `IDENTITY_MISMATCH_OR_NAVIGATION_ONLY`
a nikdy sa nestanú novým kandidátom.

## 3. Frozen call a selection boundary

1. Pred callom musia byť neprítomné oba ciele:
   `265A_B6B2_10_Q1R3_ACCESS_RECOVERY_EVIDENCE.txt` a
   `266_B6B2_10_H_RDIV_C01_RW1_V1_Q1R3_ACCESSIBILITY_RECOVERY_RESULT_SK.md`.
2. Search evidence má jediné ID `A1_SEARCH_RETURN`. V tom istom
   `functions.exec` ako search sa návrat serializuje presne takto: string sa
   nemení; non-string sa uloží cez `JSON.stringify(result, null, 2)`. Header
   obsahuje `ACCESS_EVIDENCE_ID`, `CALL_TYPE=SEARCH_QUERY`, exact query a exact
   provider payload. Potom nasleduje samostatný riadok
   `BEGIN_EXACT_ACCESS_RETURN`, raw hodnota, samostatný riadok
   `END_EXACT_ACCESS_RETURN` a direct absent-target publication do 265A.
3. Recoverable raw body je presne reťazec po newline, ktorý ukončuje jediný
   BEGIN riadok, a pred jedným publication-added newline bezprostredne pred
   jediným END riadkom. Ak raw hodnota sama obsahuje celý delimiter na
   samostatnom riadku alebo framing nie je jednoznačný, výsledok je
   `REVIEW_Q1R3_ACCESS_EVIDENCE_TECHNICAL_FAILURE_NO_PHYSICAL_INFERENCE`.
4. Z provider poradia sa smie vybrať iba prvý identity-eligible záznam s
   publisher, arXiv/author-preprint alebo same-identity author-controlled či
   inštitucionálnou full-text cestou. Provider rank vlastní výber naprieč
   všetkými týmito route typmi; alternatívy ostávajú pripojené k tej istej
   bibliografickej identite.
5. Povolené sú najviac tri následné volania spolu, teda
   `count(open)+count(click)<=3`, iba v rámci toho istého bibliografického
   záznamu: landing metadata, full-text HTML/PDF/TeX a jedna canonical alebo
   same-identity alternatíva. Každé volanie má unikátne ID `A2`–`A4`, header
   s `CALL_TYPE`, exact target URL, provider ref/payload, rovnakú frozen
   serializáciu a BEGIN/END framing; exact návrat sa same-call appendne do
   265A.
6. Search transport exception, A1 publish failure, A2–A4 open/click transport
   exception pred appendom alebo akékoľvek A2–A4 append failure zakazuje
   rerun už spotrebovaného search/open/click callu, zachová čiastočnú
   evidenciu, zakazuje success/exhaustion claim a končí
   `REVIEW_Q1R3_ACCESS_EVIDENCE_TECHNICAL_FAILURE_NO_PHYSICAL_INFERENCE`.
7. Žiadny ďalší search query, nový titul, nový DOI, neskorší Q1 hit, Q2/F-B/F-C
   ani companion zdroj nie je povolený.

265A je append-only evidence ledger počas tasku; po poslednom povolenom calle
sa uzavrie finálnym SHA. Manuálny prepis alebo chatový súhrn nenahrádza raw
náv­rat.

## 4. Full-text success gate

`PASS_Q1R3_FULL_TEXT_RECOVERED_FOR_FROZEN_S0_SCREEN` vyžaduje naraz:

- exact bibliografickú identitu Q1R3;
- primary full text z publishera, arXiv/author preprintu alebo
  author-controlled/inštitucionálneho repozitára;
- čitateľné relevantné action/EOM/energy equations a ich section/equation
  identifiers, nie iba abstrakt, snippet alebo citačnú kartu;
- immutable URL/provider ref a exact raw access evidence v 265A;
- žiadne doplnenie chýbajúcej fyziky z iného modelu.

Úspech iba odomkne návrat do frozen S0–S13 screen-u dokumentu 261. Neznamená,
že Q1R3 prešiel S0–S13 alebo že vznikol W10.

Ak exact-title call nedá identity-eligible full-text cestu, ak sa spotrebuje
spoločný cap troch `open+click` volaní bez čitateľných rovníc alebo ak už
neexistuje ďalšia povolená same-record cesta aj pri menej než troch calloch:

```text
REVIEW_Q1R3_FULL_TEXT_ACCESSIBILITY_RECOVERY_EXHAUSTED_NO_PHYSICAL_INFERENCE
```

Stav sa vráti k coverage blockeru; Q1R3 sa nepreskočí.

## 5. Counts, nonclaims a scope

Recovery success/failure sám nemení:

```text
P4 work atoms = 2,
physical witness attempts = 0,
K4 = 60/100,
P5 = 3.5/6,
RUN_AUTHORIZED = false.
```

Python, P5.4, G8/G9, steam/completion, S8/H0 fit, nový ansatz, source splice,
fyzikálny verdict a package work sú zakázané.

## 6. Súborový rozpočet

Celý recovery atóm má najviac:

```text
1 preregistration document265
1 append-only exact access evidence ledger 265A
1 result document266 at exact path:
  tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/
  266_B6B2_10_H_RDIV_C01_RW1_V1_Q1R3_ACCESSIBILITY_RECOVERY_RESULT_SK.md
4 central registers in one state/closure batch: current, K4, P5, event ledger
0 audit package copies
```

Document266 sa publikuje presne raz iba do neprítomného cieľa po uzavretí
evidence ledgera 265A. Kolízia znamená
`REVIEW_Q1R3_RESULT_TARGET_COLLISION_NO_OVERWRITE`; existujúci cieľ sa nemení.

## 7. Auditný handoff

```text
TASK_ID: A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R3-ACCESS-PREREG-AUDIT-20260727-178
ROLE: physics_track_auditor
ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
ASSIGNED_AGENT_TASK_ID: /root/c01_q1r3_access_prereg_audit
ARTIFACT_AUTHOR_TASK_ID: /root task177
STATIC_AUDITOR_TASK_ID: /root/c01_q1r3_access_prereg_audit task178
INTERNAL_AUDITOR_TASK_ID: RESERVED_DISTINCT_RESULT_AUDITOR_NOT_ACTIVATED
PACKAGE_CURATOR_TASK_ID: RESERVED_EXTERNAL_PACKAGE_CURATOR_NOT_ACTIVATED
EXTERNAL_AUDITOR_TASK_ID: RESERVED_EXTERNAL_AUDITOR_NOT_ACTIVATED
SEPARATION_OF_DUTIES_CHECK: PASS_EXPECTED_ALL_DISTINCT
ROUTE: A1_K1_A2_K4_P5.3g7_SM_v1_B6b-2.10_H_RDIV_C01_RW1_v1_Q1R3_ACCESS
CURRENT_PHASE: DRAFT_PREREGISTRATION_BEFORE_ANY_RECOVERY_SEARCH
ALLOWED_NEXT_ACTION: independent read-only audit, then out-of-file SHA freeze and absent-target preflight
ALLOWED_READS: mandatory bootstrap; documents259-265; receipts263A-D; event ledger; role config/manifest
ALLOWED_WRITES: none
FORBIDDEN_ACTIONS: web/search/open/click; edit; new source/candidate; physics screen; Python; score/depth/run/package change
IMMUTABLE_INPUT_PATHS_AND_SHA256: document261=FB94A671AA861B5B9A18639AB9A4C565FC0F90A800723D232A0B073D3B877F5B; document263=8CC33C71C2C7479399741EF5F8B0019645210555F8AB59BE9AB468C75CC95AF3; accepted_document264=DA9F5FCACAD15FF8D00C6C582D05E05E47ED33F764FD05A0286D607E394F079A
PREREG_SHA256: PENDING_AFTER_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only prereg audit; after freeze tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/265A_B6B2_10_Q1R3_ACCESS_RECOVERY_EVIDENCE.txt and tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/266_B6B2_10_H_RDIV_C01_RW1_V1_Q1R3_ACCESSIBILITY_RECOVERY_RESULT_SK.md
DONE_WHEN: exact identity-only query, deterministic serialization/recoverable framing, direct raw persistence, total three open+click cap, full-text equation success gate, all technical/exhaustion/collision branches, counts/nonclaims and file budget are fail-closed
NEXT_ROLE: main_orchestrator
```
