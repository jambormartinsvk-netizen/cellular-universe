# KMPC-047 — GLOBAL_C1 NID primary/extended: predregistrácia a execution ledger

**Dátum predregistrácie:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / NID`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `TECHNICAL_PASS / AUTHORITATIVE_REVIEW_SUPPORT_EXTENSION_REQUIRED`  
**Identita:** `NID / k=0.05 Mpc^-1 / nominal`  
**K4:** `LIVE / 60/100`; **P5:** `3.5/6`; skóre a triggery `NONE`

## 1. Jediná otázka

Po uzavretí CDI a BI sa bez prenosu ich koeficientov alebo support verdictu
testuje iba:

> Prejde NID primary support `[0,3]` voči extended supportu `[0,5]` pri
> zmrazených rovniciach, prahoch a plochách?

Toto je prvý NID fail-fast atóm kontraktu 51. Nie je to test NIV, iných `k`,
nulových variantov, S-M, plnej hierarchie ani evolúcie.

## 2. Zmrazený kontrakt

| Veličina | Hodnota |
|---|---:|
| vedúci frakčný rád | `j=0` |
| primary support | `[0,3]` |
| extended support | `[0,5]` |
| F0 počty | `8 → 12` |
| M3 počty | `52 → 78` |
| common powers | `0,1,2,3` |
| čistý added tail | `4,5` |
| plochy | `z={1e-4,1e-2}` |
| common relative prah | `1e-8` |
| tail relative prah | `1e-6` |
| absolute fallback norm/tolerance | `1e-12 / 1e-12` |

Autoritatívny tail je `sum(abs(c_j) z^j)` iba cez `j=4,5`; signed tail je
diagnostický. Raw rozdiel dvoch solve zostáva zmiešanou diagnostikou a
nesmie prebiť čistý common/tail test.

## 3. NID-specific combined-R_fs guard

NID kompenzácia musí používať spoločnú collisionless váhu
`R_fs=R_nu+R_s`, nie samotné `R_nu`. V M1 seede sa priamo overia koeficienty

```text
delta_gamma[0] = -R_fs/R_gamma
delta_fs[0]    = 1
U_gamma[0]     = -R_fs/(4 R_gamma)
U_fs[0]        = 1/4
U_b[0]         = -R_fs/(4 R_gamma)
```

a presné kompenzačné rezíduá

```text
R_gamma delta_gamma[0] + R_fs delta_fs[0] = 0
R_gamma U_gamma[0] + R_fs U_fs[0] = 0.
```

Negatívny fixture musí odmietnuť kandidáta s `nid_compensation_weight=R_nu`.
Actual S-C0 coefficient lift/collapse guard sa opakuje na primary aj extended
M3 stave.

## 4. Povinné brány

1. exact source/prerequisite hash a immutable output guard;
2. frozen a nezávislá R-A state/driver/holdout parita;
3. B1 left-null/Bianchi a production-TCA0 bridge;
4. NID M1 anchor a combined-`R_fs` kompenzácia;
5. F0/M3 rank, driver rezíduá, nezávislé `00/0i` holdouty, forbidden-order,
   production, `U_c` regularita a konečnosť pre `[0,3]` aj `[0,5]`;
6. actual S-C0 lower-moment coefficient guard;
7. common coefficient bridge `0…3` a cancellation-safe tail `4,5`.

Immutable prerequisites:

- `RUN_KMPC_033_P5_3G7_S_C0_COEFFICIENT_PASSPORT_RERUN1.json`, SHA-256
  `4CED9D48FD9866113739580E20F69E8122D70204E37C055251C8A49B3E0CFE8C`;
- `RUN_KMPC_046_P5_3G7_BI_SUPPORT_STEP_3_OWNER_SUCCESSOR.json`, SHA-256
  `60EC5A801FDDBAFFBA6CE184EBB3BC154879928385E6E37FB118781118615FB1`,
  iba sekvenčný prerequisite bez prenosu numerického stavu.

## 5. Rozhodovací strom

1. parser/hash/runtime/JSON/publish chyba →
   `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT`;
2. contract, M1, combined-`R_fs`, core alebo S-C0 FAIL →
   `REVIEW_NID_C1_CORE_GATE_UNCLOSED`;
3. common powers `0…3` FAIL →
   `REVIEW_NID_C1_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED`;
4. tail `4,5` FAIL → `REVIEW_NID_C1_SUPPORT_EXTENSION_REQUIRED`;
5. všetko PASS → `PASS_NID_C1_PRIMARY_EXTENDED_ATOM_CANDIDATE_ONLY`.

Skript nevydáva autoritatívny PASS/REVIEW/STOP. Ak common alebo tail zlyhá,
ďalší support sa nespustí automaticky; najprv vznikne samostatná
predregistrácia. Invariantný nenulový holdout nie je STOP bez nezávislej
reprodukcie na úplnom potrebnom supporte.

## 6. Prevádzka a plánované artefakty

Poradie je: compile base, compile runner, `--help`, `--smoke`, kontrola
neexistencie outputov, presne jeden `--audit`, hash a nezávislé čítanie JSON.
Každý proces má vonkajší limit najviac `10 s`; vnútorný limit je presne
`4.8 s`. Smoke nesmie zapísať výsledok a musí pokryť zlý support,
`R_nu`-kompenzáciu, runtime, JSON a exclusive-publish negatívne fixtures.

- base: `scripts/baseScripts/p5_general_synchronous/nid_c1_coverage.py`;
- runner: `scripts/291_script_KMPC_047_P5_3g7_NID_C1_primary_extended_coverage.py`;
- output:
  `scripts/results/k_mpc_005/RUN_KMPC_047_P5_3G7_NID_C1_PRIMARY_EXTENDED_COVERAGE.json`.

## 7. Nonclaims

Bez NIV, ďalšieho supportu, iných `k`/variantov, S-M, full hierarchy,
finite opacity, ODE/P5.4, G8/G9, CLASS/CMB/BBN/S8/H0 a bez zmeny teórie.

## 8. Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | používateľ povolil pokračovanie a vyžiadal auditný balík po ucelenej časti | `AUTHORIZED` |
| 2026-07-18 | NID otázka, supporty, prahy, plochy, combined-`R_fs` guard a rozhodovací strom zmrazené pred Python procesom | `PREREGISTERED` |
| 2026-07-18 | base SHA `EEEE74848B6F4413914F0CC60230CC824982C7E485A38C77C4495F807975A2CD`; runner SHA `EF217D9AD729CFA0B112018B5D4C385E983564F185A1543F3BC245F812FEAF95` | `FROZEN_BEFORE_PYTHON` |
| 2026-07-18 | compile base, compile runner, `--help` a behaviorálny smoke | `PASS / PASS / PASS / PASS` |
| 2026-07-18 | jediný official audit, external exit `0`, internal `1.485 s`; immutable JSON SHA `EED63396DB99C0818306C581413572BE647630CFD0433A8F05A1DCE704DC696A` | `TECHNICAL_PASS` |
| 2026-07-18 | core/common/combined-`R_fs` PASS; tail `4,5` FAIL na `z=.01`, najhoršie `U_f` | `REVIEW_NID_C1_SUPPORT_EXTENSION_REQUIRED` |
