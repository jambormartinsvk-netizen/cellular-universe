# KMPC-054 — GLOBAL_C1 NIV primary/extended: predregistrácia a execution ledger

**Dátum predregistrácie:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / NIV`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `TECHNICAL_PASS / AUTHORITATIVE_REVIEW_SUPPORT_EXTENSION_REQUIRED`  
**Identita:** `NIV / k=0.05 Mpc^-1 / nominal`  
**K4:** `LIVE / 60/100`; **P5:** `3.5/6`; skóre a triggery `NONE`

## 1. Jediná otázka

Po autoritatívnom uzavretí NID v KMPC-053 sa bez prenosu NID koeficientov,
korekčného vektora alebo support verdictu testuje iba:

> Prejde samostatný NIV primary support `[-1,2]` voči extended supportu
> `[-1,4]` pri zmrazených rovniciach, prahoch a plochách?

NIV má vedúci záporný rád a preto nejde o premenovaný NID test. M1 order 5
už pokrýva najvyšší extended rád `4`; tento prvý fail-fast atóm preto nemení
hĺbku M1. Ak core zlyhá, ďalší support sa automaticky nespustí.

## 2. Zmrazený kontrakt

| Veličina | Hodnota |
|---|---:|
| vedúci frakčný rád | `j=-1` |
| primary support | `[-1,2]` |
| extended support | `[-1,4]` |
| F0 počty | `8 → 12` |
| M3 počty | `52 → 78` |
| common powers | `-1,0,1,2` |
| čistý added tail | `3,4` |
| plochy | `z={1e-4,1e-2}` |
| common relative prah | `1e-8` |
| tail relative prah | `1e-6` |
| absolute fallback norm/tolerance | `1e-12 / 1e-12` |
| interný runtime | presne `4.8 s` |
| vonkajší limit jedného procesu | najviac `10 s` |

Autoritatívny tail je cancellation-safe obálka
`sum(abs(c_j) z^j)` iba cez `j=3,4`. Signed tail a raw rozdiel dvoch solve sú
iba diagnostiky.

## 3. NIV-specific combined-R_fs guard

NIV kompenzácia musí používať spoločnú collisionless váhu
`R_fs=R_nu+R_s`, nie samotné `R_nu`. Pri vedúcom ráde `j=-1` sa overí

```text
U_gamma[-1] = -3 R_fs/(4 R_gamma)
U_fs[-1]    = 3/4
U_b[-1]     = -3 R_fs/(4 R_gamma)
R_gamma U_gamma[-1] + R_fs U_fs[-1] = 0.
```

Zároveň sa vyžaduje nulový vedúci `j=-1` vo všetkých ostatných M1 stavoch,
nulové `j=0` pre `h, eta, delta_gamma, delta_fs, delta_b, delta_c,
sigma_fs, U_c`, presná identita `R_nu+R_steam=R_fs` a kolektívny kontrakt
`velocity_bridge=P5_U_REGISTERED_NOT_SCRIPT84_q`. Negatívny fixture musí
odmietnuť `niv_compensation_weight=R_nu`.

## 4. Povinné brány

1. exact source/prerequisite hash a immutable exclusive-output guard;
2. frozen a nezávislá R-A state/driver/holdout parita;
3. B1 left-null/Bianchi a production-TCA0 bridge;
4. NIV M1 order-5 anchor, záporný leading rád a combined-`R_fs` kompenzácia;
5. F0/M3 rank, driver rezíduá, nezávislé `00/0i` holdouty,
   forbidden-order/stress, production, `U_c` regularita a konečnosť pre oba
   supporty;
6. actual S-C0 lower-moment coefficient guard;
7. common bridge `-1…2` a čistý tail `3,4`.

Immutable prerequisites:

- `RUN_KMPC_033_P5_3G7_S_C0_COEFFICIENT_PASSPORT_RERUN1.json`, SHA-256
  `4CED9D48FD9866113739580E20F69E8122D70204E37C055251C8A49B3E0CFE8C`;
- `RUN_KMPC_053_P5_3G7_NID_SUPPORT_CLOSURE.json`, SHA-256
  `625AC2FAF4BD114D4907ABF83BFF059B50741642E7FB198FA3D7FBCB1BF3B4BD`,
  iba sekvenčný prerequisite bez prenosu numerického stavu.

## 5. Rozhodovací strom

1. parser/hash/runtime/JSON/publish chyba →
   `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT`;
2. contract, M1, combined-`R_fs`, core alebo S-C0 FAIL →
   `REVIEW_NIV_C1_CORE_GATE_UNCLOSED`;
3. common powers `-1…2` FAIL →
   `REVIEW_NIV_C1_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED`;
4. tail `3,4` FAIL → `REVIEW_NIV_C1_SUPPORT_EXTENSION_REQUIRED`;
5. všetko PASS → `PASS_NIV_C1_PRIMARY_EXTENDED_ATOM_CANDIDATE_ONLY`.

Skript nevydáva autoritatívny PASS/REVIEW/STOP. Ďalší support ani numerická
oprava sa nespustia post-hoc; vyžadujú nový predregistrovaný atóm.

## 6. Plánované artefakty a prevádzka

Poradie: compile base, compile runner, `--help`, behaviorálny `--smoke`,
kontrola neexistencie outputov, presne jeden `--audit`, SHA-256 a nezávislé
čítanie JSON. Smoke nesmie publikovať výsledok a musí pokryť zlý NIV
support, zlú `R_nu` kompenzáciu, runtime, non-finite JSON a kolíziu publish.

- base: `scripts/baseScripts/p5_general_synchronous/niv_c1_coverage.py`;
- runner: `scripts/298_script_KMPC_054_P5_3g7_NIV_C1_primary_extended_coverage.py`;
- output:
  `scripts/results/k_mpc_005/RUN_KMPC_054_P5_3G7_NIV_C1_PRIMARY_EXTENDED_COVERAGE.json`.

## 7. Nonclaims

Bez ďalšieho NIV supportu, iných `k`/variantov, S-M, full hierarchy,
finite opacity, ODE/P5.4, G8/G9, CLASS/CMB/BBN/S8/H0 a bez zmeny teórie.

## 8. Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | používateľ povolil pokračovanie, žiadal audit po ucelenej časti a minimálne zmeny zdrojových súborov | `AUTHORIZED` |
| 2026-07-18 | NIV otázka, supporty, prahy, plochy, M1 hĺbka, combined-`R_fs` guard a rozhodovací strom zmrazené pred Python procesom | `PREREGISTERED` |
| 2026-07-18 | base SHA `B222554E8F6E664DAC674E394FED02A02ECBEE432ADEDC9A9682DFA6BB746E9D`; runner SHA `75CDF108C4FA11A97E10F555FD47B0B5005551EC4513438A4B5C223985A0C66B` | `FROZEN_BEFORE_PYTHON` |
| 2026-07-18 | compile base, compile runner, `--help` a behaviorálny smoke | `PASS / PASS / PASS / PASS` |
| 2026-07-18 | jediný official audit, external exit `0`, internal `1.328 s`; immutable JSON SHA `0CF322A7BA5964B78BBF9180B29FA8BBBE43A646ECEB05D444B6250568ECFB1E` | `TECHNICAL_PASS` |
| 2026-07-18 | core/common/combined-`R_fs` PASS; tail `3,4` FAIL na oboch plochách, najhoršie `delta_f=8.23797e-2` pri `z=.01` | `REVIEW_NIV_C1_SUPPORT_EXTENSION_REQUIRED` |
