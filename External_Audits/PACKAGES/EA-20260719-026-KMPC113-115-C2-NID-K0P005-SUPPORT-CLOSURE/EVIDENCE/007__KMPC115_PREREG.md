# KMPC-115 — C2 NID/k=.005 support `[0,7]→[0,9]`: predregistrácia resume

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE / PASS_CANDIDATE`  
**Fyzikálny prerequisite:** KMPC-113 SHA
`DD5B3075AB7581C4DC590CFE668952217B58C969B07FEC1CCDE5FA02C7B3B533`  
**Checkpoint prerequisite:** KMPC-114 SHA
`339FD13BE750060793FCE04698BA5726AFD58DCB08BBDD3DB7B1FDFE76B35195`

## Presná otázka

Prejde jediný fyzikálne interpretovateľný checkpoint-resumed atóm
`NID/k=.005`, accepted `[0,7]`, audit `[0,9]`, M1 depth 9 všetkými
zmrazenými M1, combined-`R_fs`, F0/M3 core, common, tail, S-C0 a background
bránami?

Resume smie hashovo načítať M1 a accepted blok z KMPC-114 a dopočítať iba
auditný chvost `[8,9]`. Musí overiť checkpoint SHA, rolu
`IMMUTABLE_INTERMEDIATE_NO_PHYSICS_VERDICT`, NID/k identitu, support,
hĺbku, prahy, source lineage, KMPC-113 kandidáta a autoritatívne poradie
13 stavov. Rovnice, matice, `rcond`, tolerancie a metriky sa nemenia.

## Zmrazené rozhodovanie

1. M1 false → `REVIEW_C2_M1_NUMERICAL_BOUNDARY`;
2. iný core false → `REVIEW_C2_CORE_GATE_UNCLOSED`;
3. common `[0,7]` false →
   `REVIEW_C2_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED`;
4. všetky netail brány PASS, ale tail `[8,9]` false →
   `REVIEW_C2_NID_K0p005_SUPPORT_09_11_REQUIRED`;
5. background false →
   `STOP_C2_BACKGROUND_K_OR_MODE_LEAK_CANDIDATE_ONLY`;
6. všetko PASS →
   `PASS_C2_NID_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY`.

Skript vydáva iba candidate. C2 sa môže zmeniť zo `6/10` na `7/10` až po
internom audite KMPC-113/114/115. K4 zostáva `LIVE / 60/100`; tento atóm
nie je P5.4, G8/G9, observačný fit ani release trigger.

## Prahy, rozsah a prevádzka

- driver `1e-10`, holdout `1e-9`, common `1e-8`, tail `1e-6`, absolute
  fallback a background `1e-12`;
- tail a background povrchy `z=1e-4,1e-2`;
- iba `NID/k=.005/[0,7]→[0,9]`; support `[0,11]`, iné módy/k a S-M sú
  mimo rozsahu;
- compile → help → smoke → presne jeden official resume;
- interný deadline `4.8 s`, každý proces má vonkajší limit `30 s`;
- success/failure raw je immutable a nikdy sa neprepisuje.

## Zmrazená implementácia pred prvým Python behom

- runner 359:
  `scripts/359_script_KMPC_115_P5_3g7_C2_NID_k0p005_support_07_09_checkpoint_resume.py`;
- runner SHA-256:
  `CE0EBDC90A22DD1180672450E4FA4FF28D14060CCF45DF64660A4F02851AF4CA`;
- configurable checkpoint SHA-256:
  `DEB7776EFE28D60978FA49ABB914B3718C7F31F111DDC4B4037DA73961798B9F`;
- harness SHA-256:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`;
- source contract `19` položiek, prerequisite contract `7` položiek;
- canonical output:
  `scripts/results/k_mpc_005/RUN_KMPC_115_P5_3G7_C2_NID_K0p005_SUPPORT_07_09_CHECKPOINT_RESUME.json`;
- canonical output pred prvým behom neexistoval.

Pred vytvorením tejto predregistrácie nebol runner 359 spustený cez Python.
Od tohto bodu je runner 359 immutable.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | checkpoint SHA, identita, support, hĺbka, prahy, kandidáty a nonclaims zmrazené | `PREREGISTERED / NOT_RUN` |
| 2026-07-19 | compile/help/smoke PASS; checkpoint SHA, 13-state order a owner restoration PASS | `PREFLIGHT_PASS` |
| 2026-07-19 | official resume exit 0 za `2.500 s`; M1/core/common/tail/background PASS | `IMMUTABLE / PASS_CANDIDATE` |
| 2026-07-19 | raw SHA `7D7B9BC1F2874A20E0CB8116D657F7C0419D03B284D0161CFFDF89112B4E0851` | `FROZEN_FOR_INTERNAL_AUDIT` |
