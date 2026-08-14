# KMPC-059 — C2 Fourier exact-diff guard successor: predregistrácia

**Dátum:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → S-C0 / C2 Fourier gate`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Predchodcovia:** KMPC-057/PF-077 a KMPC-058/PF-078; oba bez atómu/JSON

## Zmrazená oprava

Detailný KMPC-058 smoke priamo vypísal staré false checks:
`BI_accepted_matches_closed_C1` a `CDI_accepted_matches_closed_C1`.
KMPC-059 preto mení iba exact očakávanie stale množiny zo štyroch módov na
`(CDI,BI)`. NID `[0,5]` a NIV `[-1,4]` sa nezmenili voči ich S1 extended
supportu; ich C1 autorita je napriek tomu naďalej viazaná na immutable
KMPC-053/056 hashe.

Všetkých desať C2 atómov, rovnice, support/depth mapa, prahy, poradie,
runtime a rozhodovací strom ostávajú presne podľa dokumentu 104. Žiadna
numerická korekcia ani prenos `.05` koeficientov nie je dovolený.

## Procesná náprava

Publikovanie, hash guard, CLI validácia a failure reporting sa presunú do
jedného stabilného pomocného modulu. Pokusový runner bude iba tenký manifest
identity, hashov a zvoleného auditného modulu. Ďalšie technické successor
pokusy tak nebudú kopírovať stovky riadkov runnera.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | observed exact diff `(CDI,BI)` zmrazený z detailného smoke výstupu KMPC-058 | `ROOT_CAUSE_CLOSED` |
| 2026-07-18 | fyzika a 10-atómová matica prevzaté bezo zmeny | `PREREGISTERED` |
| 2026-07-18 | overlay V3 SHA `6AB7097DE6774086D664ACDCA4BC3171824003F177C191E7F5A73422A83391C9`; stabilný harness SHA `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`; thin runner SHA `81EAB6F03CFD3B9F2CD58991C0DD1FA0181DBB51290129960B25A83DAFDBA283`; žiadny KMPC-059 output | `FROZEN_BEFORE_PYTHON` |
| 2026-07-18 | compile/help PASS; smoke exit `1`; exact diff a ownery PASS, corrected guard false bez vnútorného false mena; PF-079; bez atómu/JSON | `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT` |
