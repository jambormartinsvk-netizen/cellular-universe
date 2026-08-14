# KMPC-117 — C2 NID/k=.15 same-matrix refinement: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE / PASS_CANDIDATE`  
**Prerequisite:** KMPC-116 SHA
`0965E3D1F7726CC851B3D1B6043468169ADEBED44096B010565F768DBD8E25AB`

## Dôvod a jediná otázka

KMPC-116 prešiel M1, accepted solve, common, tail, S-C0, background a
nezávislý audit holdout. Audit `[0,7]` zlyhal iba na `M3_driver`:
`gamma_Euler[7]=4.1865589368e-10 > 1e-10`; rank je `104/104` a holdout
maximum `6.5626998417e-11 < 1e-9`.

KMPC-117 testuje, či tri predregistrované residual corrections na presne
tej istej 104×104 matici a pravej strane znížia driver pod `1e-10` bez
zmeny rovnice, supportu, `rcond`, prahu alebo holdout definície.

## Zmrazený kontrakt

- byteovo sa znovupoužije existujúci auditovaný modul
  `c2_cdi_k0p15_same_matrix_refinement.py`; napriek historickému názvu je
  už použitý aj pre BI a je konfigurovateľný pre frozen NID atóm;
- `mode=NID`, `k=.15`, accepted `[0,5]`, audit `[0,7]`, M1 depth 7;
- presne tri corrections; selection rule musí zlepšiť relative residual a
  nesmie zhoršiť absolute-fallback residual;
- matrix/constant identita musí byť `EXACT_SAME_MATRIX_AND_CONSTANT`;
- deterministic single-thread prostredie je povinné;
- driver `1e-10`, holdout `1e-9`, common `1e-8`, tail `1e-6`, absolute
  fallback/background `1e-12`; nič sa neuvoľňuje;
- žiadny holdout riadok sa nepridáva do driver solve.

## Predregistrované rozhodovanie

1. source/prerequisite/fixture/owner/provenance fail → technický incident,
   bez fyzikálneho verdiktu;
2. driver ostane false →
   `REVIEW_C2_NID_K0p15_SAME_MATRIX_NUMERICAL_BOUNDARY` a ďalší krok musí
   byť osobitne predregistrovaný precision/provenance audit, nie štvrtá
   correction;
3. driver prejde, ale independent holdout zlyhá →
   `REVIEW_C2_NID_K0p15_INDEPENDENT_HOLDOUT_BOUNDARY`;
4. vznikne iná false brána → `REVIEW_C2_CORE_GATE_UNCLOSED` podľa presnej
   false množiny;
5. všetky frozen brány a refinement provenance prejdú →
   `PASS_C2_NID_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY`.

Skript vydáva iba candidate. C2 `7/10→8/10` povoľuje až interný audit.
K4 zostáva `60/100`; P5.4, G8/G9, dáta a release sú mimo scope.

## Implementácia zmrazená pred prvým Python behom

- runner 361:
  `scripts/361_script_KMPC_117_P5_3g7_C2_NID_k0p15_same_matrix_refinement.py`;
- runner SHA-256:
  `6B7E8596638ECD7BD68380F6D36F5C902258536D63CCB34A005E986AD79A577B`;
- same-matrix base SHA-256:
  `EA589E4CBAD3AD618DEBC41C81B271EAC23F229AEA82C80E962CD792091468F6`;
- source contract `18` položiek, prerequisite contract `6` položiek;
- harness SHA-256:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`;
- output:
  `scripts/results/k_mpc_005/RUN_KMPC_117_P5_3G7_C2_NID_K0p15_SAME_MATRIX_REFINEMENT.json`;
- output pred prvým behom neexistoval.

Pred vytvorením tejto predregistrácie nebol runner 361 spustený cez Python.
Od tohto bodu je runner 361 immutable.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | compile/help/smoke PASS; matrix identity, 3 corrections, fixture a owners PASS | `PREFLIGHT_PASS` |
| 2026-07-19 | official exit 0 za `4.125 s`; driver `4.18656e-10→1.35140e-16`, holdout `1.43732e-11` | `IMMUTABLE / PASS_CANDIDATE` |
| 2026-07-19 | raw SHA `F9BE1AC95575B0A71E73596384360ADC382C651EE4C8BA067DD4313C4BE6C7C4` | `FROZEN_FOR_INTERNAL_AUDIT` |
