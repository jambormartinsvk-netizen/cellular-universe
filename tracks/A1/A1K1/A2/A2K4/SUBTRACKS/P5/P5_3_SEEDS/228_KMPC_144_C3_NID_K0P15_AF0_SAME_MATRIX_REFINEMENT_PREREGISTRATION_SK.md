# KMPC-144 — C3 NID/k=0.15 af0/audit-only same-matrix refinement

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → NID/k=0.15`  
**Stav:** `PREREGISTERED / SOURCE_HASHES_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Východisko:** `KMPC-131 / interný audit 227`; NID `8/9`, C3 `38/45`.

## 1. Jediný blocker a jediný cieľ

KMPC-131 NID/.15 je technicky úplný. `gamma0` je autoritatívne PASS a
`af0` má jedinú nepravdivú bránu: audit `[0,7]` rank-104 M3 driver
`4.1865589368e-10 > 1e-10`, worst row `gamma_Euler[7]`. Af0 audit holdout
`6.5627e-11 < 1e-9`, common, tail, background, null, bridge a accepted
solve sú PASS.

Immutable predchodca:
`RUN_KMPC_131_P5_3G7_C3_NID_K0p15_ZERO_VARIANT_PAIR.json`, SHA
`3850A3D951E5A8A3E21C93A6DAE7F1A08CBE6430E7100BD01B75F573F21AF71B`.

KMPC-144 smie refinovať výhradne shard `af0/audit`. Gamma0 accepted/audit
a af0 accepted sa nesmú refinovať.

## 2. Zmrazená náprava

- target iba `NID/k=.15/af0/audit`, `expected_rank=104`;
- presne `3` iteratívne korekcie;
- identická equilibrated matrix, constant/RHS, row labels, column scale a
  `rcond`;
- žiadne nové rows, unknowns, rovnice, supporty alebo prahy;
- support ostáva `[0,5]→[0,7]`, M1 depth `7`;
- refined stav sa vyberie iba ak je finite, relative residual sa zlepší a
  absolute-fallback residual sa nezhorší;
- gamma0 celý variant a af0 accepted solve musia byť exact paritné s
  immutable predchodcom;
- gamma0 audit nesmie obsahovať refinement provenance;
- worker `≤4.8 s`, parent wall `≤9 s`, external process `≤10 s`;
- parent vykoná `0` solverov a publikuje jeden pair receipt.

Použitý trojkorekčný mechanizmus je frozen modul úspešných KMPC-117/133/143.
Jeho použitie nemení fyzikálny model ani nefitne independent holdout.

## 3. Predregistrované rozhodnutia

- af0 refined driver `<1e-10`, selection/parity checks a všetky pôvodné
  brány PASS:
  `PASS_C3_NID_K0P15_AF0_AUDIT_SAME_MATRIX_REFINEMENT_CANDIDATE_ONLY`;
- selection alebo driver ostane false:
  `REVIEW_C3_NID_K0P15_NUMERICAL_BOUNDARY_UNCLOSED`;
- parity, holdout, common, tail, null, background alebo bridge fail sa
  nesmie skryť driver PASSom;
- syntax/import/hash/schema/runtime/child chyba je technical failure bez
  fyzikálneho verdiktu.

Pri internom prijatí PASS sa NID uzavrie `9/9` a globálne C3 `39/45`.
Skriptový candidate sám verdikt neprideľuje.

## 4. Predregistrovaný postup a output

`compile frozen+overlay+runner → help → NID/.15 targeted-refinement smoke →
NID/.15 official`.

Smoke musí overiť `4/4`, predecessor hash, exact target role, refinement
fixture, owner restoration a `physics_executed=false`. Official smie
vytvoriť iba:

`scripts/results/k_mpc_005/RUN_KMPC_144_P5_3G7_C3_NID_K0p15_AF0_AUDIT_SAME_MATRIX_REFINEMENT.json`

alebo príslušný `_TECHNICAL_FAILURE.json`. Ani jeden pred source freeze
neexistoval.

## 5. Source freeze pred prvým KMPC-144 Python behom

| artefakt | SHA-256 |
|---|---|
| frozen KMPC-131 four-shard base | `7FA292CF2910C5F2AEE5996DFC61498B688D2B8743615D7A0F3DFC3CA24E4C23` |
| frozen three-correction mechanism | `EA589E4CBAD3AD618DEBC41C81B271EAC23F229AEA82C80E962CD792091468F6` |
| nový af0/audit-only overlay | `B84A51D466ED4667A35653859B6E842C5529443A76EBF86BD22B1FDEA8272646` |
| nový runner `388/KMPC-144` | `A1E0B0F8BC1A26149308D86421E9F46E107EF8339A3E3453D676BFDEB50AA375` |

Žiadny `PENDING_BEFORE_FIRST_PYTHON` nezostal. Zdroje sa odteraz nemenia.
Po internom uzavretí alebo pomenovanom STOP sa vytvorí jeden externý auditný
balík za celý NID C3 mód.
