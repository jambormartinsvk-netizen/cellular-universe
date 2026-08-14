# B6b-2.10 — Q1R3 terminálna trojoknová section-coverage preregistrácia

**Task:** `A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R3-TERMINAL-3WINDOW-PREREG-20260727-211`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.10`  
**Autor teórie:** Martin Jambor  
**Formalizácia:** Codex, hlavný orchestrátor  
**Stav:** `DRAFT_PREREGISTRATION / TERMINAL_Q1R3_COVERAGE / NO_PYTHON`

## 1. Jediný cieľ a terminálnosť

Cieľom je minúť posledné tri internal operations kumulatívneho exact-Q1R3
capu na tri presne zmrazené PDF line windows. Atóm smie iba rozhodnúť, či
combined read set už postačuje na S1–S12; nesmie resetovať cap, meniť zdroj,
otvoriť companion ani hľadať ďalšieho kandidáta.

Ak tri okná coverage neuzavrú, Q1R3 sa terminálne ponechá
`EVIDENCE_INCOMPLETE` a nijaký ďalší Q1R3 source operation nie je povolený.

## 2. Immutable vstupy a zdedený stav

```text
document269 SHA256:
  1F236BCC08E83C0F7F316DF34ED1A7017CAFD301FA798C5C4933AB4D9E0203CD
binding269A SHA256:
  E7F51774A5139C3D16B21631A5094B245CBBA742E1EAD5F252D081C47C346D14
find269B SHA256:
  C0561EAF84B1C93690C28FA31B1CEE85D8D5096D401F2D4EF140062219D3F202
windows269C SHA256:
  456F3CD5C9EA80568DD1B8F500D3BF07A8DB5DEBE32059E8ECAE8D5858FCD4C5
immutable result270 SHA256:
  275DD1DC59DCAA4D49641AB69EE511E3E3D1407632F412690B1065DD42B32F61
authoritative interpretation:
  result270 + event-ledger task206 erratum
current accepted gate map:
  S0=PASS; S1-S12=NOT_ASSESSABLE_EVIDENCE_INCOMPLETE; S13=PASS
exact source/ref:
  Wang–Tian–Huang, arXiv 2301.12328, turn45view0
cumulative operations:
  21/24 consumed; exactly 3 remain; no reset
```

Všetky W10 passport polia, provenance tokeny, evidence statusy, S0–S13 PASS
podmienky, decision vetvy a nonclaims ostávajú exact z dokumentov267/269 a
task206 errata.

## 3. Frozen jediný web call

Po nezávislom auditnom PASS, out-of-file SHA freeze a absent-target
preflighte sa vykoná presne jeden batched `web__run/open` call:

```json
{"open":[
  {"ref_id":"turn45view0","lineno":900},
  {"ref_id":"turn45view0","lineno":1308},
  {"ref_id":"turn45view0","lineno":1950}
]}
```

Frozen význam anchors:

1. L900 — §3.3 model-dependent analysis;
2. L1308 — exact B5-captured §4 representative-model/nucleation location;
3. L1950 — late §5 smerom k §6 conclusion, zvolený z TOC p.25 a B5 §5
   location L1788.

Každý open je jedna internal operation. Po calle je cap presne `24/24`.
Žiadny find, search, click, iný line anchor, fallback, filler, retry alebo
pagination nie sú povolené.

## 4. One-call/one-file receipt

Exact raw návrat celého batched callu sa v tom istom `functions.exec` cez
`apply_patch` publikuje presne raz do absent cieľa:

`271A_B6B2_10_Q1R3_TERMINAL_THREE_WINDOW_RAW.txt`.

Súbor má jeden header s exact payloadom, internal count `3`,
`BEGIN_EXACT_BATCH_RETURN`, neupravený string alebo
`JSON.stringify(result,null,2)` a `END_EXACT_BATCH_RETURN`. Append sa
nepoužíva. Delimiter collision, existing target, call/publish exception,
cache miss ktoréhokoľvek okna alebo neobnoviteľný raw return končí
`REVIEW_Q1R3_TERMINAL_COVERAGE_TECHNICAL_FAILURE_NO_PHYSICAL_INFERENCE`.
Call sa neopakuje a cap sa neresetuje.

## 5. Result gate

Po validnom receipte sa combined set 267A + 269A-C + 271A zmapuje do celej
passport tabuľky a S0–S13. Každé pole musí mať exact equation/section,
`SOURCE_EXACT`, `DERIVED_SAME_MODEL`, `E3_MAPPING` alebo pri complete coverage
`MISSING`, plus evidence status.

Ak nové okná odstránia incomplete stav všetkých S1–S12, použije sa exact
frozen decision vetva dokumentu269: complete W10, reference-only, alebo
candidate-local `PRECHECK_Q1R3_EXCLUDED_SCOPE` podľa dôkazu.

Ak čo i len jeden S1–S12 ostane `NOT_ASSESSABLE_EVIDENCE_INCOMPLETE`, výsledok
je terminálne:

```text
REVIEW_Q1R3_TERMINAL_COVERAGE_EXHAUSTED_EVIDENCE_INCOMPLETE_NO_PHYSICAL_INFERENCE
```

Tento stav znamená iba vyčerpanie frozen Q1R3 evidence capu. Nie je Q1R3
physical FAIL, complete-W10 refutation, C01/global no-go ani dôkaz prázdnosti
`A_RW1`. Po ňom je každý ďalší Q1R3 source operation zakázaný; ďalší legálny
stav frozen source-search route určí až progress review a hlavný orchestrátor.

## 6. Výstup, účtovanie a rozpočet

Výsledok sa presne raz publikuje do absent cieľa:

`272_B6B2_10_H_RDIV_C01_RW1_V1_Q1R3_TERMINAL_COVERAGE_RESULT_SK.md`.

Kolízia je fail-closed bez overwrite. Tento atóm má najviac 3 live vedecké
artefakty: document271, receipt271A, result272. Opening batch mení iba
document271 + event ledger. Package copies `0`.

Iba auditovaný a hlavným orchestrátorom prijatý complete-W10 výsledok môže
meniť work atoms `2->3` a witness attempts `0->1`. Všetky ostatné vetvy
zachovajú P4 atoms `2`, attempts `0`, K4 `60/100`, P5 `3.5/6`,
`RUN_AUTHORIZED=false`. Python, fit, P5.4, steam/completion a downstream sú
zakázané.

## 7. Auditný handoff

```text
TASK_ID: A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R3-TERMINAL-3WINDOW-PREREG-AUDIT-20260727-212
ROLE: physics_track_auditor
ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
ASSIGNED_AGENT_TASK_ID: /root/c01_q1r3_access_prereg_audit
ARTIFACT_AUTHOR_TASK_ID: /root::task211
STATIC_AUDITOR_TASK_ID: /root/c01_q1r3_access_prereg_audit::task212
INTERNAL_AUDITOR_TASK_ID: RESERVED_DISTINCT_RESULT_AUDITOR_NOT_ACTIVE
PACKAGE_CURATOR_TASK_ID: RESERVED_EXTERNAL_PACKAGE_CURATOR_NOT_ACTIVE
EXTERNAL_AUDITOR_TASK_ID: RESERVED_EXTERNAL_AUDITOR_NOT_ACTIVE
SEPARATION_OF_DUTIES_CHECK: PASS_EXPECTED_ALL_DISTINCT
ROUTE: A1_K1_A2_K4_P5.3g7_SM_v1_B6b-2.10_H_RDIV_C01_RW1_v1_Q1R3_TERMINAL_COVERAGE
CURRENT_PHASE: DRAFT_BEFORE_TERMINAL_THREE_OPEN_CALL
ALLOWED_NEXT_ACTION: independent read-only prereg audit; after PASS, out-of-file SHA freeze and absent-target preflight
ALLOWED_READS: mandatory bootstrap; documents261,267,269-271; evidence267A; 269A-C; result270 + task206 erratum; relevant ledger tasks196-211; role config/manifest
ALLOWED_WRITES: none
FORBIDDEN_ACTIONS: edit; web/source operation; physics verdict; cap reset; new source/candidate/companion; Python; score/depth/run/package change
IMMUTABLE_INPUT_PATHS_AND_SHA256: document269=1F236BCC08E83C0F7F316DF34ED1A7017CAFD301FA798C5C4933AB4D9E0203CD; binding269A=E7F51774A5139C3D16B21631A5094B245CBBA742E1EAD5F252D081C47C346D14; find269B=C0561EAF84B1C93690C28FA31B1CEE85D8D5096D401F2D4EF140062219D3F202; windows269C=456F3CD5C9EA80568DD1B8F500D3BF07A8DB5DEBE32059E8ECAE8D5858FCD4C5; result270=275DD1DC59DCAA4D49641AB69EE511E3E3D1407632F412690B1065DD42B32F61
PREREG_SHA256: PENDING_AFTER_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only audit; after freeze exact receipt271A and result272 paths
DONE_WHEN: inherited 21/24, exact three anchors/payload, one-call one-file persistence, 24/24 terminal behavior, complete/incomplete result branches, nonclaims/accounting and three-file budget are fail-closed
NEXT_ROLE: main_orchestrator
```
