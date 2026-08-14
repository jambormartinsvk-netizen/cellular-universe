# EA-033 — C3 BI/.15 exact-runtime blocker

**Stav:** `SEALED_READY_FOR_EXTERNAL_AUDIT`  
**Target tier:** `T1_PRIMARY_FORMULA_AND_RUNTIME_CONTRACT`  
**Theory author:** Martin Jambor  
**Script creator/internal auditor:** Codex (OpenAI)  
**LIVE_FILES_CHANGED_THIS_CONTINUATION:** `16` — dvanásť atomických
artefaktov KMPC-135 až 137 a štyri centrálne/closure aktualizácie  
**PREEXISTING_INTERRUPTED_KMPC134_ARTIFACTS:** `4`  
**AUDIT_PACKAGE_COPIES:** `27` evidence kópií + `7` controls; response
šablóna je osobitný `1` súbor; spolu `35 < 40`.

## Presná otázka

Potvrdzuje primárny kód, immutable receipts a autoritatívny KMPC-112 raw, že
C3 BI/.15 je zablokovaný konfliktom medzi nezmeneným 80-dps exact solverom
(`34.86 s` pri historickom limite `45 s`) a novým C3 contractom
(`4.8 s/worker`, `9 s/parent`), nie fyzikálnym STOP? Ktorá z troch ciest je
metodicky najmenšia a auditovateľná: osobitná exact-runtime výnimka, nový
rýchly solver alebo checkpointovaný exact rozklad?

## Poradie čítania

1. `EVIDENCE/001__C3_BI_RUNTIME_BLOCKER_INTERNAL_AUDIT.md`;
2. BI rawy `010` až `012`;
3. technické receipts `013` až `016` a historical authority `017`;
4. predregistrácie `004` až `007`;
5. primary exact a C3 source `018` až `027`;
6. error/DO-NOT-RUN ledgers `008` a `009`;
7. metodika, aktuálny plán, manifest a pokyny.

## Tier hranica

Balík je zámerne T1. Obsahuje primárny source a hash-bound rawy, ale nie
úplný transitive import/runtime closure a nežiada opakovať official vetvu,
ktorá je predmetom runtime blockera. Auditor smie staticky overiť vzťah
solver–limit–receipt a odporučiť procesnú cestu. Nesmie tvrdiť T2
reprodukciu KMPC-137 ani nový computed fyzikálny verdikt.

## Predregistrované hodnotenie externého posudku

- `CONFIRM_TECHNICAL_RUNTIME_BLOCKER`: dôkazy stačia na oddelenie technického
  blockera od fyzikálneho STOP a auditor zoradí tri riešenia;
- `REVIEW_EVIDENCE_GAP`: chýba primárny dôkaz pre runtime alebo solver
  identitu; auditor presne vypíše potrebný súbor;
- `REJECT_BLOCKER_ATTRIBUTION`: receipt alebo source ukáže inú príčinu;
  projektový verdikt sa nemení bez následného interného posúdenia.

## Nonclaims

Balík neuzatvára BI `9/9`, nemení C3 `27/45`, nemení K4 `60/100`, netvrdí
STOP K4, nereprodukuje KMPC-112/137 ako T2, neschvaľuje nový solver,
nepovoľuje automatický KMPC-138 a neotvára P5.4, G8/G9 ani likelihood.

## Autorita

Externý audit je read-only odporúčanie. Runtime výnimku, novú numerickú
metódu alebo checkpointovaný proces môže predregistrovať iba hlavný
orchestrátor po explicitnom projektovom rozhodnutí.
