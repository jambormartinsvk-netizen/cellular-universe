# KMPC-052 — NID depth-7 numerical boundary: predregistrácia a execution ledger

**Dátum predregistrácie:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / NID / DEPTH7_BOUNDARY`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED`; score/triggery `NONE`

## 1. Jediná otázka

KMPC-051 ukázal, že M1 depth 7 odstránil veľký Einstein order-7 constraint
rozpor, ale pôvodný float64 M3 solve ostal na driver hranici
`fuel_Euler[7] = 1.3994e-10` oproti `1e-10`. Jedna diagnostická korekcia
`3.3227e-16` uzavrela driver aj holdout.

> Potvrdia jedna bounded float64 refinement a jeden nezávislý 80-dps
> same-matrix QR solve, že posledný depth-7 NID driver fail je solver/rounding
> floor bez zmeny rovníc, prahov alebo supportu?

Immutable prerequisite: KMPC-051 SHA
`AF088030BA709F08D40D825B9477C9A84BA330705CDDFB1C12C52B0DD3FC1E5E`.

## 2. Zmrazený kontrakt

- `NID/.05/nominal`, hard-anchored M1 depth `7`, M3 support `[0,7]`;
- M3 driver `104×104`, holdout `16×104`, rank `104/104`;
- V0 reprodukuje KMPC-051 matrix/constant hashe, `driver FAIL`, worst
  `fuel_Euler[7]`, `holdout PASS`;
- driver relative `1e-10`, holdout relative `1e-8`, absolute fallback
  `1e-12` bez zmeny;
- V1 normwise backward error a residual invarianty;
- V2 presne jedna equilibrated float64 correction rieši tú istú maticu,
  cap `max|delta| <= 1e-14`;
- V3 presne jeden 80-dps Householder QR solve tej istej float64 matice/RHS
  prenesenej cez `float.as_integer_ratio()`;
- V2, V3 aj V3→float64 projekcia musia prejsť všetky driver a holdout riadky,
  zachovať common M3 `0…5` v limite `1e-8` a correction/state difference cap
  `1e-14`;
- Householder používa auditovaný `mpmath.mp` context owner a `sign(0)→+1`
  tie; owner sa obnoví;
- native coefficient rebuild, druhá korekcia/HP solve, zmena poradia,
  normal equations, `[0,9]`, NIV a zmena publikovaného KMPC-051 sú zakázané.

## 3. Rozhodovací strom

1. prerequisite/source/V0 parity/owner/runtime/JSON fail → technický alebo
   `REVIEW_NID_DEPTH7_REFERENCE_UNCLOSED`;
2. V2 cap/common/rank fail → `REVIEW_NID_DEPTH7_REFINEMENT_OUT_OF_BOUNDS`;
3. V2 aj V3 vrátane projekcie uzavrú driver+holdout →
   `PASS_NID_DEPTH7_FLOAT64_SOLVER_FLOOR_CANDIDATE_ONLY`;
4. iba V3+projekcia prejdú →
   `PASS_NID_DEPTH7_FLOAT64_ROUNDING_FLOOR_CANDIDATE_ONLY`;
5. V3 same-matrix zlyhá → `REVIEW_NID_DEPTH7_SAME_MATRIX_BOUNDARY_UNCLOSED`.

Skript neprideľuje autoritatívny verdict ani support adequacy.

## 4. Runtime a prevádzka

Podľa PF-072/PF-073 a precedensu KMPC-044 smoke vykoná lifecycle na presnej
104×104 matici: interný limit `12 s`, externý `15 s`. Jediný audit má
interný `45 s`, externý `60 s`. Poradie: compile base, compile runner, help,
exact-matrix smoke, output guard, jediný audit, hash a nezávislé čítanie.

## 5. Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | KMPC-051 depth-7 constraint PASS a correction pattern uzavreté ako prerequisite | `PREREQUISITE_CLOSED` |
| 2026-07-18 | V0–V3, capy, runtime, operation limits a nonclaims zmrazené | `PREREGISTERED` |
| 2026-07-18 | base SHA `D5016BD007FD59D4BB715967366774478AFFD344C1B5CD95ACF6F5A9465DD7C8`; runner 296 SHA `A0CC1A5B6474AD627B105C990916DA40C8C455687521C6A3DB977AFBAE691B69`; output `RUN_KMPC_052_P5_3G7_NID_DEPTH7_NUMERICAL_BOUNDARY.json` | `FROZEN_BEFORE_PYTHON` |
| 2026-07-18 | compile base/runner a help PASS; exact 104×104 80-dps smoke PASS za internal `6.000 s`; output guard čistý | `PREFLIGHT_PASS` |
| 2026-07-18 | jediný audit exit `0`, internal `7.031 s`; V0/V2/V3 vrátane projekcie PASS | `TECHNICAL_COMPLETE` |
| 2026-07-18 | raw SHA `FDEE962EED16EDF459D7D8504833AB1206AEF1BFC8178A356A88A121CF196C4C` | `PASS_CANDIDATE_ONLY` |
