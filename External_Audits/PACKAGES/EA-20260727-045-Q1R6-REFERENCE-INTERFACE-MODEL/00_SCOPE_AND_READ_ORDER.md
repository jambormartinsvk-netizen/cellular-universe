# EA-045 — Q1R6 reference interface model

**Stav:** `SEALED_READY_FOR_AUDIT / NOT_SENT`  
**Target tier:** `T1_PRIMARY_FORMULA / STATIC_REFERENCE_INTERFACE_SCOPE`  
**Autorita:** zmrazené artefakty Q1R6; externý auditor iba odporúča  
**Autor teórie:** Martin Jambor  
**Vykonanie a procesný orchestrátor:** Codex / `/root`  
**TASK_ID:** `A2K4-Q1R6-EA045-PACKAGE-CURATOR-DRAFT-20260727-268`  
**PACKAGE_ID:** `EA-20260727-045-Q1R6-REFERENCE-INTERFACE-MODEL`  
**PACKAGE_CURATOR_TASK_ID:** `/root/q1r6_ea045_curator`  
**ARTIFACT_AUTHOR_TASK_ID:** `/root`  
**STATIC_AUDITOR_TASK_ID:** `/root/c01_q1r3_access_prereg_audit`  
**INTERNAL_AUDITOR_TASK_ID:** `/root/c01_q1r3_access_result_audit`  
**EXTERNAL_AUDITOR_TASK_ID:** `/root/q1r6_ea045_external_auditor`  
**SEPARATION_OF_DUTIES_CHECK:** `PASS(curator=/root/q1r6_ea045_curator != external auditor=/root/q1r6_ea045_external_auditor; curator != author=/root; author != internal auditor=/root/c01_q1r3_access_result_audit)`  
**AUDITOR_ROLE_CONFIG_SHA256:** `6B1AF6C55E725E7A2332F30F0337713F1A7E254402E7F8A5A64BB689569C9A14`  
**PACKAGE_CURATOR_ROLE_CONFIG_SHA256:** `26CAB7693DBB372C4FAEEFBACF9101CD2C1BA3F40E628CB20E6514EA8A906AE1`  
**PREREG_SHA256:** `266BCABBF7C7AEA87E9E01BC1120FDF3E44CE7841FC892AF391CD11B060C1228`  
**RUN_AUTHORIZED:** `false`

## R6 súborové počítadlá

```text
LIVE_SCIENTIFIC_ARTIFACTS=0
LIVE_CENTRAL_REGISTERS_UPDATED=1
LIVE_FILES_CHANGED_TOTAL=1
AUDIT_PACKAGE_COPIES=20 (13 evidence + 7 controls)
RESPONSE_TEMPLATE_FILES=1
NEW_PACKAGE_AND_RESPONSE_FILES_TOTAL=21
REPRO=0
RUNTIME_ROWS=0
PYTHON_PROCESSES=0
```

Podkladový Q1R6 local-reprocess atóm mal tri live vedecké artefakty
(`document279`, `receipt279A`, `result280`) a balík ich nemení.

## AUDITOR_RULESET_PATHS_AND_SHA256

```text
EVIDENCE/009__AGENTS.md=226710D6467FE923D6F2CBAFF02CE9235F1B48C07C4A9DACD95C6B06486B2B29
EVIDENCE/010__PROJECT_OPERATING_SYSTEM.md=519BDCBAE2CD9BF62351586E357DE3C9A28E60AD79CDB653661DD2821D65B6E7
EVIDENCE/011__AUDITOR_PACKAGE_PROTOCOL_R6_1.md=E22381E0463196384EC126C23E7C62E6AF1BA1EAFC98FB85FECC6444E6CBBD01
EVIDENCE/012__EXTERNAL_AUDITOR_ROLE.toml=6B1AF6C55E725E7A2332F30F0337713F1A7E254402E7F8A5A64BB689569C9A14
EVIDENCE/013__AGENT_ROLE_MANIFEST.md=EA48FEF9348EFEA1F681EF8A3D35F69038FABE57B07D9F8BC70CB3D670F3FE91
```

## Presná otázka

Podporuje jediný immutable primárny arXiv source `2204.13120`, spolu so
zmrazenou preregistráciou, complete-local receiptom a výsledkom, iba úzky
claim `PASS_Q1R6_REFERENCE_INTERFACE_MODEL_ONLY`; a je odmietnutie complete
W10 witness správne ohraničené absenciou `Z_rec`, nonnegative `P_rec`,
cycle-frozen `W_*`, disjunktného RW1 conservation ledgeru, parent-cell
`u_cell`/measure, temporal crossing, reset mapy a event-off identity?

Skontrolujte tiež, či S0, S10 a S13 sú jedinými `PASS` a S1–S9, S11, S12 sú
správne `MISSING`, bez premeny analógie na novú fyziku.

## Poradie čítania

1. `01_MANIFEST_SHA256.tsv`, potom `EVIDENCE/009` až `013`; overte exact
   ruleset/profile/manifest hashes a identity separation.
2. Tento scope, `02`, `03`, `04` a `05`.
3. `EVIDENCE/001` až `004`: frozen local procedure, jediný source archive,
   complete-universe receipt a výsledkový passport.
4. `EVIDENCE/005` až `008`: iba route/state/provenance context.
5. Pre primary-source kontrolu iba package-local čítanie archívu `002`.

Externý auditor po odovzdaní nečíta live projekt mimo tohto balíka.

## Predregistrované hodnotenie externého posudku

- `AGREE_IN_SCOPE` — source podporuje interface reference scope a výsledok
  nepreceňuje chýbajúce W10 objekty;
- `AGREE_WITH_LIMITATION` — jadro sedí, ale konkrétny line reference,
  passport field alebo S-gate potrebuje zúženie;
- `DISAGREE` — source/result materiálne preceňuje interface analógiu alebo
  nesprávne označuje W10 field/gate;
- `CANNOT_AUDIT` — chýba archive, receipt, result alebo isolated ruleset.

## Povinná protokolová klasifikácia výsledku

```text
REQUIRED_PROTOCOL_RESULT_CLASSIFICATION=NONE_OF_FIVE_STATIC_REFERENCE_SCOPE
```

Tento T1 static reference-interface audit netvrdí ani jednu z piatich
protokolových výsledkových tried: `PRECHECK_EXCLUDED_SCOPE`,
`COMPUTED_STOP_SCOPE`, `OBSERVATIONAL_STOP_SCOPE`,
`REFERENCE_MISMATCH_ONLY` ani `TECHNICAL_STOP`. Auditor musí zvoliť jednu
z piatich tried alebo `NONE_OF_FIVE_STATIC_REFERENCE_SCOPE` a uviesť stručné
odôvodnenie. Táto povinnosť nemení ani nepredurčuje jeho auditný názor.

## Nonclaims

Balík nedokazuje kompletný W10 witness, nevyvracia C01/RW1 ani A2-K4,
nevymýšľa missing objects, nevyberá mikrofyziku, nevykonáva Python,
numerický solver, download, fit alebo downstream S8 výpočet. Nemení
projektový `PASS/REVIEW/STOP`, K4 `60/100`, P5 `3.5/6`, skóre, hĺbku ani
`RUN_AUTHORIZED=false`.

## Autorita a lifecycle

Externý posudok je neautoritatívne odporúčanie. Balík je zapečatený po
nezávislom pre-seal review a čaká iba na package-only externý audit.
