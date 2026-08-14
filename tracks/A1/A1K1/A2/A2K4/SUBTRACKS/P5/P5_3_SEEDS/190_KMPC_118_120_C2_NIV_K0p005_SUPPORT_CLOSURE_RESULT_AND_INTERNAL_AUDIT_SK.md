# KMPC-118–120 — C2 NIV/k=.005 support closure: interný audit

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Interný auditor a autoritatívny zápis:** Codex (OpenAI)  
**Stav:** `INTERNAL_AUDIT_PASS / NIV_K0P005_CLOSED`  
**Autoritatívny verdict:**
`PASS_C2_NIV_K0p005_SUPPORT_06_ADEQUATE_CHECKPOINT_RESUME`  
**Dopad:** C2 `8/10→9/10 PASS`; K4 zostáva `LIVE / 60/100`; active
technical counter `0/10`

## Immutable evidence

| Beh | Rola | SHA-256 | Candidate/status |
|---|---|---|---|
| KMPC-118 | NIV/.005 nominal `[-1,4]→[-1,6]` | `FDB2DF9C0AA1620F2ABF76F1704735DD1848F8C8D861BD959B5F81EC6873B78F` | `REVIEW_C2_NIV_K0p005_SUPPORT_06_08_REQUIRED` |
| KMPC-119 | verdict-free accepted `[-1,6]` checkpoint | `0E87C19C706D2D8AE9FA1FF2771B46FEEF308327C5B459024175566BAF4ECEE9` | `TECHNICAL_CHECKPOINT_COMPLETE_NO_PHYSICS_VERDICT` |
| KMPC-120 | checkpoint resume, audit `[-1,8]` | `D6350636F9BA27C541EF8CDC2585ED370E2F1E2EB35495E01198A8BAA47AB136` | `PASS_C2_NIV_K0p005_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY` |

## Nominal výsledok a príčina rozšírenia

KMPC-118 prešiel M1, accepted/audit core, common, S-C0, independent
holdout, background a všetky rank/provenance brány. Jediný top-level false
check bol `tail_pass`. Na `z=.01` bol F0 worst `delta_f=1.54255e-5` a M3
worst `delta_f=2.18311e-5`, oba nad frozen `1e-6`. Na `z=.0001` oba tail
povrchy prešli. Ide o predregistrovanú support truncation vetvu, nie STOP.

## Checkpoint a successor audit

Pôvodná checkpoint vrstva obsahovala skrytý NID-only guard a labely. Nový
versioned successor SHA
`70D8E55DD59FF7C1C23F9BD4C3615063C017D9639D497381AE803C4ED0EDBB0E`
explicitne povoľuje iba frozen NIV ladder `[-1,6]→[-1,8]`, depth 8. Rovnice,
solver, prahy a equation builder nemení.

KMPC-119 má 9/9 checkpoint preconditions true, M1 PASS, verdict-free status,
exact support/depth identitu a obnovených ownerov. KMPC-120 overil exact
checkpoint SHA a všetkých osem checkpoint checks, 13-state order aj
successor owner restoration.

| Kontrola KMPC-120 | Hodnota | Prah/audit |
|---|---:|---|
| M1 driver | `9.94760e-14` | PASS |
| M1 holdout | `1.68532e-13` | PASS |
| F0 audit driver | `1.33925e-14` | `<1e-10`, PASS |
| M3 audit driver | `2.10479e-13` | `<1e-10`, PASS |
| M3 independent holdout | `4.77975e-14` | `<1e-9`, PASS |
| rank F0 / M3 | `20/20`, `130/130` | PASS |
| common F0 / M3 | `6.24347e-14`, `1.86511e-10` | `<1e-8`, PASS |
| tail F0 `.01` | `3.66649e-9` (`delta_f`) | `<1e-6`, PASS |
| tail M3 `.01` | `7.69530e-9` (`delta_f`) | `<1e-6`, PASS |
| background worst | `1.15195e-16` | `<1e-12`, PASS |

False-check množiny KMPC-120 sú prázdne. Absolute fallback residualy môžu
byť väčšie než driver threshold iba na riadkoch, ktoré majú samostatný
frozen absolute prah `1e-12`; observed maximum `1.433999e-13` ho spĺňa.

## Autoritatívne rozhodnutie

Interný audit prijíma scoped NIV/k=.005 PASS s accepted `[-1,6]`, audit
`[-1,8]`, M1 depth 8. C2 sa zvyšuje na `9/10`. K4 hĺbka sa nemení, pretože
NIV/k=.15 a nasledujúce P5 brány ešte nie sú uzavreté.

## Nonclaims a ďalší krok

Výsledok nepotvrdzuje NIV/k=.15, S-M, ODE/P5.4, G8/G9, dáta, A3 ani
release. Podľa package protokolu R4 nevzniká auditný balík po tomto
medzikroku; celý NIV mód sa zabalí spolu po druhom k-bode.

Ďalší frozen atóm je `NIV/k=.15/nominal`, accepted `[-1,4]`, audit
`[-1,6]`, M1 depth 6, ordering prerequisite KMPC-120 s exact SHA vyššie.
