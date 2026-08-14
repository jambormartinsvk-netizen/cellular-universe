# KMPC-053 — NID support closure: predregistrácia a execution ledger

**Dátum predregistrácie:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / NID / SUPPORT_CLOSURE`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED`; score/triggery `NONE`

## Jediná otázka

Je NID candidate support `[0,5]` dostatočný pri konzistentnom hard-anchored
M1 depth `7`, ak audit support `[0,7]` používa jedinú same-matrix refinement
už nezávisle uzavretú KMPC-052?

Immutable prerequisites:

- KMPC-052 SHA `FDEE962EED16EDF459D7D8504833AB1206AEF1BFC8178A356A88A121CF196C4C`;
- KMPC-048 SHA `B4F320F5D850DCF78FD9EC2A5BDDEBDA87D590DA2988CF505FA7D5B25B49BF32`
  iba pre regresiu supportov `[0,3]` a `[0,5]`.

## Zmrazený rozsah a brány

- `NID/.05/nominal`, M1 depth `7`; supporty presne `[0,3]`, `[0,5]`,
  `[0,7]`; leading `j=0`;
- rovnaké rovnice, registre, prahy a hard anchor;
- support `[0,7]` smie dostať presne jednu KMPC-052 equilibrated correction,
  cap `1e-14`; žiadny ďalší HP solve v tomto atóme;
- regresia `[0,3]/[0,5]` proti KMPC-048 musí prejsť pôvodným regression
  kontraktom;
- core: F0 aj M3 shapes/rank/driver/holdout/forbidden/contract, combined
  `R_fs`, S-C0 a finite;
- common powers iba `0…5` s pôvodným `1e-8`;
- tail iba powers `6,7`, cancellation-safe envelope
  `sum(abs(c_j)z^j)` na `z=1e-4,1e-2`, frozen `1e-6`, absolute fallback
  `1e-12`;
- `[0,9]`, NIV, iné `k`/varianty, S-M, ODE, P5.4 a G8/G9 sú zakázané.

## Rozhodovací strom

1. source/prerequisite/runtime/JSON/publish chyba → technický FAIL;
2. regression alebo KMPC-052 parity fail →
   `REVIEW_NID_SUPPORT_CLOSURE_REFERENCE_UNCLOSED`;
3. core fail → `REVIEW_NID_SUPPORT_CLOSURE_CORE_UNCLOSED`;
4. common fail → `REVIEW_NID_SUPPORT_CLOSURE_COMMON_UNCLOSED`;
5. tail fail → `REVIEW_NID_SUPPORT_05_REMAINDER_UNCLOSED`;
6. všetko PASS → `PASS_NID_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY`.

PASS uzavrie iba NID `.05/nominal` support. Nepridáva bod ani neotvára P5.4;
ďalší mód je NIV.

## Prevádzka a ledger

Compile base, compile runner, help, smoke, output guard a jediný audit;
interný `4.8 s`, externý `10 s`.

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | KMPC-052 same-matrix boundary autoritatívne uzavretá | `PREREQUISITE_CLOSED` |
| 2026-07-18 | supporty, regression/core/common/tail brány a zákazy zmrazené | `PREREGISTERED` |
| 2026-07-18 | base SHA `0B9DA3BBF95FE14878DBD2604C7B8E9619BE9F94A4C147C4FAA79299DC165F5A`; runner 297 SHA `B9B89D725F881067755E92D49C102D986C75D07A0EAE5B6DBD5DD620983DCCA1`; output `RUN_KMPC_053_P5_3G7_NID_SUPPORT_CLOSURE.json` | `FROZEN_BEFORE_PYTHON` |
| 2026-07-18 | compile base/runner, help, smoke a output guard PASS; jediný audit exit `0`, internal `3.125 s` | `TECHNICAL_COMPLETE` |
| 2026-07-18 | raw SHA `625AC2FAF4BD114D4907ABF83BFF059B50741642E7FB198FA3D7FBCB1BF3B4BD`; reference/core/common/tail PASS | `PASS_CANDIDATE_ONLY` |
