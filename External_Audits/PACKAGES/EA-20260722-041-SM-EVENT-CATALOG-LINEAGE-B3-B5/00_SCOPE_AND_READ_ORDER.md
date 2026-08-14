# EA-041 — katalóg granularít, formula-lineage a definičná brána B3–B5

**Stav:** `SEALED_READY_FOR_AUDIT`  
**Target tier:** `T1_PRIMARY_FORMULA / DEFINITION_AND_LINEAGE_AUDIT_ONLY`  
**Autorita:** živý dokument 245; externý auditor iba odporúča  
**Autor teórie:** Martin Jambor  
**Formalizácia rovníc a procesný orchestrátor:** Codex (OpenAI)  
**PACKAGE_CURATOR_TASK_ID:** `/root`  
**EXTERNAL_AUDITOR_TASK_ID:** `/root/ea041_external_audit`  
**CURATION_REVIEWER_TASK_ID:** `/root/ea038_external_audit`  
**PHYSICS_REVIEWER_TASK_ID:** `/root/external_audit_ea036`  
**SEPARATION_OF_DUTIES_CHECK:** `PASS(curator != external auditor)`  
**AUDITOR_ROLE_CONFIG_SHA256:** `6B1AF6C55E725E7A2332F30F0337713F1A7E254402E7F8A5A64BB689569C9A14`  
**PACKAGE_CURATOR_ROLE_CONFIG_SHA256:** `26CAB7693DBB372C4FAEEFBACF9101CD2C1BA3F40E628CB20E6514EA8A906AE1`  
**PACKAGE_CURATOR_CONFIG_BINDING:** `REFERENCE_ONLY_MAIN_ORCHESTRATOR_CURATOR`  
**RUN_AUTHORIZED:** `false`  
**LIVE_SCIENTIFIC_ARTIFACTS:** `1`  
**LIVE_CENTRAL_REGISTERS_UPDATED:** `4`  
**LIVE_FILES_CHANGED_TOTAL:** `5`  
**AUDIT_PACKAGE_COPIES:** `15` manifestových kópií + `7` controls = `22`; response `1`; spolu `23 < 40`.

## AUDITOR_RULESET_PATHS_AND_SHA256

```text
EVIDENCE/011__AGENTS.md=BD64D6AC1C583194A67B3ABC5423467AF3F5F292F0293AF68F02AA3BBC503EE5
EVIDENCE/012__PROJECT_OPERATING_SYSTEM.md=F4F0C3610CBE5BDF05DEC7EE606534682222DBF959F439686CF89FA7B0F7E543
EVIDENCE/013__AUDITOR_PACKAGE_PROTOCOL_R6.md=4330FFD3D22C27CC60A3693E9B4694B601903FC6490A4DB7F56B56B1C4FD5272
EVIDENCE/014__EXTERNAL_AUDITOR_ROLE.toml=6B1AF6C55E725E7A2332F30F0337713F1A7E254402E7F8A5A64BB689569C9A14
EVIDENCE/015__AGENT_ROLE_MANIFEST.md=76921D8F2FA0FB02C70F511AFB4396C4148F052938DA21C33B91D1594C20061E
```

## Scope markery

```text
B3=FINITE_HYPOTHESIS_MAP / PASS_B3
B4=PASS_FORMULA_LINEAGE
F1_F2_F3_AS_A2_ENERGY_EVENTS=STOP_CURRENT_CORPUS_ONLY
B5=PASS_DEFINITION_INVENTORY
Q4_P0_COMPLETE=0/8
Q22A_G0=REVIEW_BLOCKED_BY_Q4_P0_DEFINITIONAL_INPUT
EARLY_EVENT_OPERATOR=NOT_DERIVABLE_FROM_CURRENT_CORPUS
D03=SOLE_ACTIVE_REVIEW_BLOCKED
D04_D11=BLOCKED
K4=60/100_UNCHANGED
P5=3.5/6_UNCHANGED
NO_RUNTIME
NO_PYTHON
NO_COMPUTED_VERDICT
```

## Presná otázka

1. Je B3 algebraická faktorizácia `j_D=nu_J epsilon_J` a trojica F1–F3
   korektná iba ako konečná mapa granularít toho istého hypotetického drainu,
   vrátane markovanej miery pri distribuovanej energii?
2. Podporuje primárna formula-lineage A2/A7/A12 záver B4, že `delta` je v
   aktuálnom korpuse efektívna tlaková/sieťová práca bez párového
   produktového zdroja, takže F1–F3 nemožno vyhlásiť za energiu réžie?
3. Je tento STOP správne obmedzený na danú interpretáciu a neznamená STOP
   udalostí, pary, S–M vetvy ani teórie?
4. Zodpovedá B5 inventár zdrojom: Q4-P0 je `0/8`, neskoré
   `epsilon_eff=lambda H0 t_P` sa neprenáša do skorého rezervoára a úplný
   Q22a-G0/AR46 operátor potrebuje aj štvorvektorové a vyššie momenty?
5. Je najmenší ďalší fyzikálny vstup úplný a zároveň stále jednoduchý:
   jedna lokálna udalosť s clockom, mierou, energiou, produktovým pravidlom,
   `M->C` dynamikou a jediným konzervačným/momentovým ledgerom?

## Poradie čítania

1. `EVIDENCE/001` — primárny dokument, najmä oddiely 8.10–8.12;
2. `EVIDENCE/002` a `003` — filozofia a primary A2/A7/A12 lineage;
3. `EVIDENCE/004` až `008` — Q4-P0, Q22a-G0 a momentové požiadavky;
4. `EVIDENCE/009` — aktuálny autoritatívny stav;
5. `EVIDENCE/010` — exact AR66.2 formula-provenance checklist;
6. manifest, prázdna runtime mapa a pravidlá `EVIDENCE/011` až `015`.

## Predregistrované hodnotenie externého posudku

- `AGREE_IN_SCOPE`: B3 algebra, B4 lineage, B5 inventár a scope sedia;
- `AGREE_WITH_LIMITATION`: jadro sedí, ale pred autorovým vstupom chýba
  presne pomenovaný invariant, moment alebo scope korekcia;
- `DISAGREE`: auditor nájde dvojité účtovanie, nepodporený formula-lineage
  prenos, nesprávny počet definícií alebo záver silnejší než zdroje;
- `CANNOT_AUDIT`: primárna formula alebo jej zdroje v balíku chýbajú.

## Nonclaims

Balík je statický T1 formula/definition audit. Neobsahuje skript, generated
JSON ani transitive runtime closure. B3 nevyberá fyzikálny event operator.
B4 nevylučuje existenciu produktových udalostí. B5 nie je dôkaz nepravdivosti
teórie alebo pary. Pozorovania nesmú určiť tvar, čas, amplitúdu, šírku,
pravdepodobnosť ani energiu chýbajúcej udalosti. K4 ostáva `60/100`, P5
`3.5/6`, P5.4 `NOT RUN`; D04–D11, G8/G9, fit, Python a prediction table sú
blokované.

## Autorita a oddelenie rolí

Kurátor, interní revieweri a fresh externý auditor sú oddelené identity.
Externý audit nemení projektový verdikt ani skóre; odpoveď spracuje hlavný
orchestrátor v samostatnom assessment súbore.
