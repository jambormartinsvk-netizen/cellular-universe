# KMPC-124 — C2 NIV/k=.15 `[-1,6]→[-1,8]` resume: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `TECHNICAL_FAILURE_NO_PHYSICS / DO_NOT_RUN`  
**Ordering prerequisite:** KMPC-122 SHA
`BAC68E1D85802852EEBF4B1AC2E277EC15FD32264E166F673D486FD747869419`  
**Checkpoint prerequisite:** KMPC-123 SHA
`D3B31093D84156D05BF4EE8EC707D53B5D653DE5700289E6EA68627674898DC8`

## Presná otázka

Obnoví KMPC-124 immutable NIV/.15 checkpoint accepted `[-1,6]`, zachová
presné 13-state poradie a dopočíta audit `[-1,8]` tak, aby M1, driver,
independent `00/0i` holdout, common, tail, S-C0 a background prešli pri
nezmenených prahoch?

## Zmrazený kontrakt

- support-generic successor SHA
  `70D8E55DD59FF7C1C23F9BD4C3615063C017D9639D497381AE803C4ED0EDBB0E`;
- `mode=NIV`, `k=.15`, accepted `[-1,6]`, audit `[-1,8]`, M1 depth `8`;
- KMPC-123 checkpoint musí mať exact hash, verdict-free status, source hash
  mapu a frozen ladder identitu;
- accepted stav sa obnoví z checkpointu; audit solve nesmie meniť accepted
  coefficients ani pridať independent holdout do driver fitu;
- prahy ostávajú driver `1e-10`, holdout `1e-9`, common `1e-8`, tail
  `1e-6`, absolute fallback/background `1e-12`;
- tail/background povrchy a equation builder ostávajú byteovo nezmenené.

## Predregistrované rozhodovanie

1. checkpoint/source/order/owner guard false → technický incident bez
   fyzikálneho verdiktu;
2. M1 alebo core false → príslušný `REVIEW_C2_*_BOUNDARY` podľa raw false
   množiny;
3. common false → `REVIEW_C2_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED`;
4. netail PASS a tail false →
   `REVIEW_C2_NIV_K0p15_SUPPORT_08_10_REQUIRED`;
5. background false → `STOP_C2_BACKGROUND_K_OR_MODE_LEAK_CANDIDATE_ONLY`;
6. všetko PASS →
   `PASS_C2_NIV_K0p15_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY`.

Skript vydáva iba candidate. Autoritatívny C2 `9/10→10/10`, uzavretie NIV
módu a ďalšiu route povoľuje až interný audit raw. K4 sa nemení iba na
základe candidate stringu.

## Scope a exekúcia

- compile → help → smoke → presne jeden resume atom;
- interný runtime `4.8 s`, vonkajší procesný limit `30 s`;
- S-M, ODE/P5.4, G8/G9 a dáta sú mimo scope;
- success/failure raw je immutable a nikdy sa neprepisuje.

## Zmrazená implementácia pred prvým Python behom

- runner 368:
  `scripts/368_script_KMPC_124_P5_3g7_C2_NIV_k0p15_support_06_08_checkpoint_resume.py`;
- runner SHA-256:
  `52ED054B687DC7C03E34879CCFE9D0CBA9AB4031E813180A5CE67BD71E4BA848`;
- source contract `20` položiek, prerequisite contract `7` položiek;
- stabilný harness SHA-256
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`;
- output:
  `scripts/results/k_mpc_005/RUN_KMPC_124_P5_3G7_C2_NIV_K0p15_SUPPORT_06_08_CHECKPOINT_RESUME.json`;
- output pred prvým behom neexistoval.

Pred vytvorením tejto predregistrácie nebol runner 368 spustený cez Python.
Od tohto bodu je immutable.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | compile/help exit 0; smoke exit 2 v checkpoint contract guard | `PF-114 / NO_PHYSICS` |
| 2026-07-19 | príčina: KMPC-123 `checkpoint_complete=false`; success raw KMPC-124 nevznikol | `FAIL_CLOSED_AS_DESIGNED` |
| 2026-07-19 | runner 368 sa nesmie opakovať; nový fyzikálny nástupca musí obísť neplatný checkpoint iba novou predregistráciou, nie guard bypassom | `DO_NOT_RUN_AUDIT_TECHNICAL` |
