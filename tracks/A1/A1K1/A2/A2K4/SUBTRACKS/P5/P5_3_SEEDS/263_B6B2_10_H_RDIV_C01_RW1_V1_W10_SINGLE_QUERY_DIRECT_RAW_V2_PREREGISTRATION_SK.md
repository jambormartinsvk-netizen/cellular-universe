# B6b-2.10 — C01-RW1 W10 single-query direct-raw v2 preregistrácia

**Task:** `A2K4-B6B2-10-H-RDIV-C01-RW1-V1-W10-RAW-V2-PREREG-20260727-163`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.10`  
**Autor teórie:** Martin Jambor  
**Formalizácia:** Codex, hlavný orchestrátor  
**Stav:** `DRAFT_PREREGISTRATION / TECHNICAL_TRANSPORT_SUCCESSOR_ONLY / NO_SEARCH_YET / NO_RUN / NO_PYTHON`

## 1. Dôvod v2 a nemenný fyzikálny scope

Frozen v1 dokument 261 zostáva immutable. Dve v1 multi-query odpovede neboli
priamo uložené a provider neodovzdal auditovateľnú per-query provenance.
Dokument 262 preto nie je autoritatívny source ledger a hlavný posudok task161
uzavrel iba:

```text
REVIEW_EXACT_WEB_TOOL_TRANSCRIPT_NOT_IMMUTABLY_PERSISTED_NO_SCIENTIFIC_INFERENCE.
```

V2 nemení ani nerozširuje fyziku. Presne dedí z frozen dokumentu 261:

- Q1–Q4 texty bez jediného znaku zmeny;
- rodiny F-A, F-B a F-C aj ich poradie;
- primary-source eligibility, dedup a family cap päť;
- one-model/companion parity a zákaz splice;
- physical-precursor pravidlo `SOURCE_EXACT/DERIVED_SAME_MODEL`;
- on-shell `D_uW[Z_rec]=P_rec>=0`, covariance/stability, source-native
  worldtube/measure a dynamický reset;
- S0–S13, rozhodovacie vetvy, nonclaims a attempt accounting.

Jediná zmena je transport a immutable zachytenie query odpovedí.

## 2. Exact queries a single-query poradie

Volania sa vykonajú presne v poradí Q1, Q2, Q3, Q4:

```text
Q1: relativistic scalar field fluid first order phase transition stress energy conservation critical bubble energy primary paper
Q2: covariant critical bubble surface tension energy barrier scalar field fluid primary paper
Q3: relativistic irreversible phase field energy balance internal variable primary paper
Q4: covariant phase field fracture interface energy conservation reset primary paper
```

Každé volanie obsahuje práve jeden `search_query`,
`response_length="long"`, žiadny domain/recency filter, rewrite alebo
pagination. Q1 a Q2 patria F-A, Q3 patrí F-B, Q4 patrí F-C. Providerom
vrátené poradie v každom samostatnom receipte je query rank.

## 3. Predurčené immutable raw receipt paths

Pred prvým web volaním musí preflight potvrdiť neprítomnosť všetkých štyroch
cieľov:

```text
Q1 -> 263A_B6B2_10_W10_Q1_DIRECT_RAW_TOOL_RETURN.txt
Q2 -> 263B_B6B2_10_W10_Q2_DIRECT_RAW_TOOL_RETURN.txt
Q3 -> 263C_B6B2_10_W10_Q3_DIRECT_RAW_TOOL_RETURN.txt
Q4 -> 263D_B6B2_10_W10_Q4_DIRECT_RAW_TOOL_RETURN.txt
```

Všetky sú v rovnakom `P5_3_SEEDS` adresári ako tento dokument. Cieľ sa
publikuje presne raz. Kolízia znamená `REVIEW_RAW_RECEIPT_COLLISION / NO_WEB`.

## 4. Direct same-call persistence contract

Každé Q volanie prebehne v samostatnom `functions.exec`. V tom istom
orchestrated call sa sekvenčne vykoná:

1. jedno `web__run({search_query:[{q: exact_Q}], response_length:"long"})`;
2. bez manuálnej úpravy sa návrat skonvertuje iba deterministicky:
   string zostáva byte-for-byte textom; ne-string objekt sa uloží ako
   `JSON.stringify(result, null, 2)`;
3. k raw telu sa pridá iba vopred zmrazená hlavička s `TASK_ID`, Q ID, exact
   query, provider payload a delimiterom `BEGIN_EXACT_TOOL_RETURN`;
4. `apply_patch` vytvorí neprítomný Q receipt; každá raw línia sa prenesie
   mechanickým prefixom patchu, bez parafrázy, reordering-u alebo výberu;
5. call vráti receipt path a následne sa mimo neho vypočíta SHA-256.

`web__run` a `apply_patch` sa nevolajú paralelne. Ak web uspeje, ale receipt
publish zlyhá, query sa neopakuje: vznikne
`REVIEW_RAW_TOOL_RETURN_PERSISTENCE_FAILURE / NO_SOURCE_OPEN`, pretože nový
search by už nebol tým istým immutable návratom.

Manuálny prepis, screenshot, chatový súhrn, agentova pamäť ani dokument 262
nesmú nahradiť raw receipt.

## 5. Receipt integrity gate pred source open

Po štyroch volaniach a pred jediným `open/click` sa zastaví. Nezávislý
read-only auditor overí:

- presne štyri prítomné ciele a ich nonzero SHA;
- hlavičku, exact query a single-query payload každého receiptu;
- čitateľný `BEGIN_EXACT_TOOL_RETURN` blok;
- absenciu multi-query merge a jednoznačné Q/family mapovanie;
- neprítomnosť manuálne zostaveného document262 textu ako raw autority;
- Q1→Q4 poradie v event ledgeri a `web_calls=4`, `source_open_calls=0`.

Auditor nevykonáva nový web call. Ak receipt nie je čitateľný alebo dôveryhodne
oddelený, stav je `REVIEW_RAW_RECEIPT_INTEGRITY_BLOCKED / NO_SOURCE_OPEN`.

Až po prijatom integrity gate sa použije pôvodný dokument261 protocol:
eligibility, dedup, prvých päť eligible kandidátov v každej rodine, skorší
inaccessible blocker, prvý complete S0–S13 kandidát a independent source
physics audit.

## 6. Počítadlá a rozhodovacie vetvy

```text
Pred výsledkom:
  P4 work atoms = 2,
  physical witness attempts = 0.

Raw receipt alebo integrity gate sám:
  nemení work atom ani witness attempt.

Úplne vykonaný a auditom prijatý source-physics screen:
  P4 work atoms 2 -> 3.

Prijatý explicitný complete-W10 kandidát:
  physical witness attempts 0 -> 1.

Collision, persistence failure, integrity blocker alebo source coverage
failure pred fyzikálnym candidate screenom:
  work atoms 2, witness attempts 0.
```

V2 nikdy samo nepotvrdí pravdu C01, physical `R_div`, P4/MF1/D03/P5.3
closure ani `A_RW1` no-go. `K4=60/100`, `P5=3.5/6`,
`RUN_AUTHORIZED=false`; Python, P5.4, G8, G9, steam/completion a S8/H0 fit sú
zakázané.

## 7. Súborový rozpočet a vopred zdôvodnená výnimka

Plánované live artefakty celého v2 atómu:

```text
1 preregistration document263
4 immutable per-query raw receipts 263A-263D
1 result document264
1 append-only event ledger
0 central plan updates pred vedeckou zmenou
0 audit package copies
```

Šesť vedeckých/raw artefaktov je vopred zdôvodnená výnimka z bežného limitu
päť: štyri oddelené Q receipts sú minimálny dôkaz per-query provenance a
nesmú sa zlúčiť, appendovať do už publikovaného cieľa ani nahradiť manuálnou
kópiou. Nevzniká samostatný súbor pre každý auditný komentár.

## 8. Auditný handoff

```text
TASK_ID: A2K4-B6B2-10-H-RDIV-C01-RW1-V1-W10-RAW-V2-PREREG-AUDIT-20260727-164
ROLE: physics_track_auditor
ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
ASSIGNED_AGENT_TASK_ID: /root/c01_w10_v2_prereg_audit
ARTIFACT_AUTHOR_TASK_ID: /root task163
STATIC_AUDITOR_TASK_ID: UNASSIGNED_STATIC_AUDITOR_NO_PYTHON
INTERNAL_AUDITOR_TASK_ID: /root/c01_w10_v2_prereg_audit task164
PACKAGE_CURATOR_TASK_ID: UNASSIGNED_PACKAGE_CURATOR
EXTERNAL_AUDITOR_TASK_ID: UNASSIGNED_EXTERNAL_AUDITOR
SEPARATION_OF_DUTIES_CHECK: PASS; /root task163 != /root/c01_w10_v2_prereg_audit task164; no script/package phase active
ROUTE: A1_K1_A2_K4_P5.3_B6b-2.10_H_RDIV_C01_RW1_v1_RAW_V2
CURRENT_PHASE: DRAFT_V2_PREREGISTRATION_BEFORE_ANY_NEW_SEARCH
ALLOWED_NEXT_ACTION: independent read-only audit of exact document263 transport delta against frozen documents261-262 and task162 review; after corrections/freeze only, preflight four absent receipt paths
ALLOWED_READS: mandatory bootstrap; documents259-263; event ledger through task163; task162 review; role config/manifest
ALLOWED_WRITES: none
FORBIDDEN_ACTIONS: web/search/open/click; edit; change Q1-Q4, families, physics, S0-S13 or counts; Python; score/depth/run change; package work
IMMUTABLE_INPUT_PATHS_AND_SHA256: document259=9766E5223C7AB95B8D3D3B9914BF8B02034F160F84EF0E47BEE8E4C14EB453E2; document260=91C25DD777FB9A10B1157F3CF729408B55A3CA264A03E29AA9C2F9E6747CA774; frozen_document261=FB94A671AA861B5B9A18639AB9A4C565FC0F90A800723D232A0B073D3B877F5B; historical_candidate_document262=D888FB5B8D5379B1ECC4F78E343317B2B0526F87CA226BCBC15F282E5BD53C9C; event_ledger_through_task161=332F9CB5DC7123E2FD55B88244C3BECCF84CDE753B5CC76F9902DABE20384174; current_plan=359022D0D50ADA0CAEE2815F2DAAFA40E033CAF912DF4EF09CC79B0E5381E2FD; K4_plan=515A35E454C6B82981B62E15C7F06E72AC448C82A8F830247FD34F6166C3CABC; P5_plan=160FDCF33F3C5FF0D1DE2B0137D5EE26052B283D6EE3B33EBEBA37C331E23FCC
PREREG_SHA256: PENDING_AFTER_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only prereg audit; after freeze exact receipt paths 263A-263D and result264
LIVE_FILE_BUDGET: pre-justified 6 scientific/raw artifacts + 1 ledger; central plans 0; package copies 0
DONE_WHEN: v2 changes only evidence transport; every Q is single-query; exact return is directly and exclusively persisted in the same call; failure cannot trigger a rerun; receipt integrity gate precedes source classification/open; counts and nonclaims remain exact
NEXT_ROLE: main_orchestrator
```
