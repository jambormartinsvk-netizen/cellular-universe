# B6b-2.10 — Q1R3 no-rerun evidence-binding/read-continuation preregistrácia

**Task:** `A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R3-BIND-CONT-PREREG-20260727-197`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.10`  
**Autor teórie:** Martin Jambor  
**Formalizácia:** Codex, hlavný orchestrátor  
**Stav:** `DRAFT_PREREGISTRATION / NO_RERUN / EXACT_Q1R3_ONLY / NO_PYTHON`

## 1. Jediný cieľ

Atóm má bez modifikácie evidence267A kryptograficky zviazať štyri zachované
raw telá B1–B4 a dokončiť chýbajúci full-text read set exact Q1R3 PDF. Až z
validného spojeného read setu sa smie vykonať nezmenený S0–S13 a W10 screen
z frozen dokumentov261 a 267.

Nie je to nový search, kandidát, companion ani nový fyzikálny ansatz. B1–B4
sa nikdy neopakujú.

## 2. Immutable rodičia a Q1R3 identita

```text
document261 = FB94A671AA861B5B9A18639AB9A4C565FC0F90A800723D232A0B073D3B877F5B
document267 = 3FDE90E9F5366E5688D958F5E803F9403EE4E6CF00B4983F4E5BF2773609BD04
evidence267A = 29868803DD2E23D2E40ACC36B0951D402463DCD32EB9E2BEE9ABA86B2A4792F0
result268 = D4A745AE703528094CDC9FE50063469D428AA21E93BA2A17F2E69327CAFAF59D
Q1R3 = Wang–Tian–Huang / arXiv 2301.12328 / JCAP07(2023)006
PDF provider ref = turn45view0
PDF = 30 pages / 2135 parsed lines
```

Screen, passport fields, provenance classes, evidence status, decision vetvy,
nonclaims a fyzikálne podmienky S0–S13 zostávajú byteovo odvodené z frozen
dokumentu267; tento successor ich nemení ani nezmäkčuje.

## 3. Frozen binding receipt 269A

Po auditnom PASS, out-of-file SHA freeze a absent-target preflighte sa bez web
operácie presne raz vytvorí absent cieľ
`269A_B6B2_10_Q1R3_EVIDENCE_BINDING_RECEIPT.txt`. Musí obsahovať:

```text
whole evidence267A SHA256:
  29868803DD2E23D2E40ACC36B0951D402463DCD32EB9E2BEE9ABA86B2A4792F0

physical file order: B1 -> B4 -> B3 -> B2
true call chronology: B1 -> B2 -> B3 -> B4
chronology evidence: task192 + monotone provider refs turn42 -> turn43 -> turn44 -> turn45

B1 raw span: after BEGIN line 6 through before END line 11;
  chars=186; lines=4;
  SHA256=59FE3AD890A7ED96B714EEABFA02454B4A2F4EBF4C79953E8E63CB5D82AACA46
B4 raw span: after BEGIN line 17 through before END line 500;
  chars=22117; lines=482;
  SHA256=B2226A9DC8E9EE51ADA2B1C71FAB96067A1242A719383AD3A2FD9EF6049CA963
B3 raw span: after BEGIN line 507 through before END line 512;
  chars=209; lines=4;
  SHA256=0136EDA19FB536D91DC2F65BD84404222CFEAEDC911DFABC74B85A51B6B1D912
B2 raw span: after BEGIN line 520 through before END line 525;
  chars=207; lines=4;
  SHA256=BBAB04E5688AEE60D566E4030EA559CEC2D49FC853DB1AA903E4030A19CC47CF

outer framing defect: B3/B4 headers plus-prefixed; standalone plus before B2;
  raw bodies are unique, nonoverlapping and delimiter-collision-free.
nonclaim: byte identity against transient original tool returns is not
  independently proven; only exact current spans are bound.
```

Main orchestrator pred publikáciou mechanicky prepočíta whole-file a štyri
raw-span hashe read-only. Nesúlad, nejednoznačný boundary alebo existujúci
269A cieľ znamená
`REVIEW_Q1R3_BINDING_PRECHECK_FAILURE_NO_PHYSICAL_INFERENCE`; nič sa
neprepisuje a web sa nespustí.

## 4. Frozen B5 batched find a one-call receipt 269B

Po validnom binding receipte sa vykoná práve jeden `web__run` call s 14
vnútornými `find` operations na `turn45view0`, v tomto poradí:

```text
energy-momentum
friction term
energy conservation
critical bubble
nucleation
initial condition
source
reservoir
reset
daughter
worldtube
congruence
proper measure
residual
```

Raw návrat celého jediného batched callu sa v tom istom `functions.exec`
publikuje cez `apply_patch` presne raz do absent súboru
`269B_B6B2_10_Q1R3_BATCHED_FIND_RAW.txt`. Súbor obsahuje jeden header, exact
payload, `BEGIN_EXACT_BATCH_RETURN`, neupravený string alebo
`JSON.stringify(result,null,2)` a `END_EXACT_BATCH_RETURN`. Žiadny append sa
nepoužíva. Delimiter collision, call/publish exception, existing target alebo
neobnoviteľný raw return končí
`REVIEW_Q1R3_CONTINUATION_EVIDENCE_TECHNICAL_FAILURE_NO_PHYSICAL_INFERENCE`;
B5 sa neopakuje.

Existujúce B1–B4 spotrebovali 4 operations; B5 spotrebuje 14, teda po ňom je
stav `18/24`.

## 5. Frozen B6–B11 line-window selection a one-call receipt 269C

Z B5 sa vyberú iba pozitívne match locations. Neúspešný find sám nedokazuje
absenciu. Line-window priority je:

```text
1 energy-momentum
2 friction term
3 energy conservation
4 critical bubble
5 reset
6 daughter
7 worldtube
8 congruence
9 proper measure
10 residual
11 nucleation
12 initial condition
13 reservoir
14 source
```

Pre každý pattern sa použije prvý providerom vrátený match; locations vo
vzájomnej vzdialenosti najviac 20 parsed lines sa deduplikujú v prospech
vyššej priority. Vyberie sa najviac šesť zostávajúcich locations. Ak je
pozitívnych deduplikovaných locations menej, použije sa presne ich počet;
žiadny filler open nie je povolený.

Všetky zvolené locations sa otvoria v jednom batched `web__run/open` calle na
tom istom `turn45view0`. Každé vnútorné open je jedna operation. Raw návrat
celého callu sa same-call cez `apply_patch` publikuje presne raz do absent
`269C_B6B2_10_Q1R3_BATCHED_LINE_WINDOWS_RAW.txt`, s rovnakým single-block
framingom ako 269B a bez appendu. Celkový cap nesmie prekročiť `24/24`.

Ak B5 nevráti nijaký použiteľný positive match, 269C sa nevytvára a evidencia
je `NOT_ASSESSABLE_EVIDENCE_INCOMPLETE`, nie `MISSING`. Cache/transport/
publication/framing failure je technický fail-closed bez rerunu B6–B11.

## 6. Evidence-complete hranica a S0–S13

Fyzikálny screen sa smie vykonať iba ak sú naraz validné:

1. binding269A a jeho mechanická hash kontrola;
2. immutable B4 PDF raw span;
3. validný B5 find receipt269B;
4. ak existovali positive matches, validný B6–B11 receipt269C;
5. relevantné equation/section windows postačujú na odlíšenie source claimu,
   same-model derivácie, E3 mapovania a absencie.

Potom výsledok270 musí reprodukovať celú passport tabuľku a všetky S0–S13 z
dokumentu267. `MISSING` možno použiť iba pri evidence-complete full-text find
a section coverage. Inak je field/S-row
`NOT_ASSESSABLE_EVIDENCE_INCOMPLETE` a výsledok iba technical/evidence review.

Rozhodovacie vetvy zostávajú exact z dokumentu267:

- complete passport: `CANDIDATE_COMPLETE_W10_INTERFACE_ACTION_PASSPORT_FOUND / PENDING_INDEPENDENT_PHYSICS_AUDIT`;
- coherent reference-only s missing field:
  `PASS_Q1R3_REFERENCE_INTERFACE_MODEL_ONLY / REVIEW_Q1R3_NOT_A_COMPLETE_W10_WITNESS`;
- evidence-complete candidate conflict:
  `PRECHECK_Q1R3_EXCLUDED_SCOPE / CAUSE_Q1R3_CANDIDATE_ONLY_FORMULA_PHYSICAL_OR_SCOPE_CONFLICT / REVIEW_Q1R3_NOT_A_COMPLETE_W10_WITNESS`;
- incomplete/technical: `REVIEW_Q1R3_CONTINUATION_EVIDENCE_TECHNICAL_FAILURE_NO_PHYSICAL_INFERENCE` alebo `REVIEW_Q1R3_SCREEN_EVIDENCE_INCOMPLETE_NO_PHYSICAL_INFERENCE`.

Žiadna vetva nie je C01/global no-go ani dôkaz prázdnosti `A_RW1`.

## 7. Výstup a účtovanie

Výsledok sa presne raz publikuje do absent cieľa
`270_B6B2_10_H_RDIV_C01_RW1_V1_Q1R3_S0_S13_PHYSICS_SCREEN_RESULT_SK.md`.
Kolízia je fail-closed bez overwrite.

Iba prijatý complete-W10 výsledok ukončí frozen search a po nezávislom audite
mení `P4 work atoms 2->3` a witness attempts `0->1`. Iné vetvy ponechajú
počty `2` a `0`. Všetky vetvy zachovajú `K4=60/100`, `P5=3.5/6` a
`RUN_AUTHORIZED=false`, kým samostatný autoritatívny closure nerozhodne inak.

Live vedecký rozpočet atómu je presne najviac 5: document269, binding269A,
find269B, optional line-window269C a result270. Opening batch mení iba
document269 + event ledger; central closure batch až po audite výsledku.
Audit package copies `0`. Python, search, nový kandidát, companion, fit,
steam/completion, P5.4 a downstream sú zakázané.

## 8. Auditný handoff

```text
TASK_ID: A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R3-BIND-CONT-PREREG-AUDIT-20260727-198
ROLE: physics_track_auditor
ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
ASSIGNED_AGENT_TASK_ID: /root/c01_q1r3_access_prereg_audit
ARTIFACT_AUTHOR_TASK_ID: /root::task197
STATIC_AUDITOR_TASK_ID: /root/c01_q1r3_access_prereg_audit::task198
INTERNAL_AUDITOR_TASK_ID: RESERVED_DISTINCT_RESULT_AUDITOR_NOT_ACTIVE
PACKAGE_CURATOR_TASK_ID: RESERVED_EXTERNAL_PACKAGE_CURATOR_NOT_ACTIVE
EXTERNAL_AUDITOR_TASK_ID: RESERVED_EXTERNAL_AUDITOR_NOT_ACTIVE
SEPARATION_OF_DUTIES_CHECK: PASS_EXPECTED_ALL_DISTINCT
ROUTE: A1_K1_A2_K4_P5.3g7_SM_v1_B6b-2.10_H_RDIV_C01_RW1_v1_Q1R3_BIND_CONT
CURRENT_PHASE: DRAFT_NO_RERUN_BINDING_CONTINUATION_BEFORE_NEW_SOURCE_OPERATION
ALLOWED_NEXT_ACTION: independent read-only prereg audit; after PASS, out-of-file SHA freeze, absent-target preflight and binding269A creation
ALLOWED_READS: mandatory bootstrap; documents261,267-269; evidence267A; result268; relevant ledger tasks192-197; role config/manifest
ALLOWED_WRITES: none
FORBIDDEN_ACTIONS: edit; web/source operation; physics screen/verdict; rerun B1-B4; Python; score/depth/run/package change
IMMUTABLE_INPUT_PATHS_AND_SHA256: document261=FB94A671AA861B5B9A18639AB9A4C565FC0F90A800723D232A0B073D3B877F5B; document267=3FDE90E9F5366E5688D958F5E803F9403EE4E6CF00B4983F4E5BF2773609BD04; evidence267A=29868803DD2E23D2E40ACC36B0951D402463DCD32EB9E2BEE9ABA86B2A4792F0; result268=D4A745AE703528094CDC9FE50063469D428AA21E93BA2A17F2E69327CAFAF59D
PREREG_SHA256: PENDING_AFTER_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only audit; after freeze exact 269A/269B/optional269C/270 paths above
DONE_WHEN: immutable binding, no-rerun constraint, exact 14-pattern find, deterministic max-six line selection, 24-operation cap, one-call-one-file persistence, S0-S13 evidence boundary, result branches/accounting/nonclaims and five-file budget are fail-closed
NEXT_ROLE: main_orchestrator
```
