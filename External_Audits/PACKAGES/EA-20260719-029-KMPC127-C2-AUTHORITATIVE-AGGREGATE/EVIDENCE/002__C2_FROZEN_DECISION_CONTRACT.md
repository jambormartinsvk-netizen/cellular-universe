# KMPC-057 — C2 Fourier coverage: predregistrácia a execution ledger

**Dátum:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → S-C0 / C2 Fourier gate`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**K4:** `LIVE / 60/100`; **P5:** `3.5/6`; triggery `NONE`

## 1. Otázka a počet atómov

Po C1 closure všetkých módov sa podľa frozen contractu 51 testuje presne
desať nových nominal atómov:

```text
mode = AD, CDI, BI, NID, NIV
k    = 0.005, 0.15 Mpc^-1
```

Jeden stabilný base a jeden runner obslúžia všetkých desať atómov; nevznikne
desať kópií skriptu. Každý atóm má vlastný immutable JSON a proces. Poradie
je mode-major, potom rastúce `k`; prvý neuzavretý core/common/tail výsledok
zastaví automatické pokračovanie a vyžiada autoritatívny audit.

## 2. Support a M1 depth mapa

| Mód | accepted support | audit support | M1 depth | leading `j` |
|---|---:|---:|---:|---:|
| AD | `[0,2]` | `[0,4]` | 5 | 2 |
| CDI | `[0,5]` | `[0,7]` | 7 | 1 |
| BI | `[0,5]` | `[0,7]` | 7 | 1 |
| NID | `[0,5]` | `[0,7]` | 7 | 0 |
| NIV | `[-1,4]` | `[-1,6]` | 6 | -1 |

M1 depth vždy pokrýva najvyšší auditovaný rád. Neprenáša sa žiadny
koeficient ani correction vector z `k=.05`; prenáša sa iba autoritatívne
uzavretá support veľkosť. Každý atóm zostaví nový M1/F0/M3 systém pre svoje
`mode×k`.

## 3. Brány atómu

1. exact C1 prerequisite hash pre všetkých päť módov;
2. frozen a nezávislý R-A contract, B1/Bianchi a production-TCA0;
3. M1 depth rank/anchor/driver/holdout a konečnosť;
4. NID/NIV combined-`R_fs` guard podľa módu;
5. accepted aj audit F0/M3 exact shape/rank, driver, nezávislý `00/0i`
   holdout, forbidden layers/stress, production a `U_c` regularita;
6. actual S-C0 lower-moment guard;
7. common koeficienty cez celý accepted support, prah `1e-8`;
8. cancellation-safe added tail dvoch nových rádov na `z=1e-4,1e-2`, prah
   `1e-6`, absolute fallback `1e-12`;
9. fyzický background na `a=1e-8,3e-8` proti lokálne prepočítanej
   `k=.05` baseline: `D,H,rho_f,rho_ash` relative `<=1e-12`.

Raw M1, ktorý zlyhá iba na numerickej hranici, nedostane automatickú
korekciu. Atóm skončí `REVIEW_C2_M1_NUMERICAL_BOUNDARY` a až samostatný
predregistrovaný same-matrix audit smie rozhodnúť o korekcii. Tým sa
correction precedens z `.05` neprenáša potichu na nové `k`.

## 4. Agregácia C2

Agregácia je dovolená iba po `10/10` technicky platných atómoch. Číta ich
immutable JSON, overí SHA a identitu, potom skontroluje:

- všetky atómové core/common/tail/background PASS;
- exact kartézsky register bez duplicity;
- cross-mode a cross-k spread `D,H,rho_f,rho_ash <=1e-12` na oboch `a`;
- žiadny output, ktorý bol technickým failure.

Agregát nič znovu nerieši a nemení skóre. C2 PASS iba odblokuje C3.

## 5. Rozhodovací strom

- technická chyba → `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT`;
- M1 boundary → `REVIEW_C2_M1_NUMERICAL_BOUNDARY`;
- accepted/audit core alebo S-C0 FAIL → `REVIEW_C2_CORE_GATE_UNCLOSED`;
- common FAIL → `REVIEW_C2_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED`;
- tail FAIL → `REVIEW_C2_SUPPORT_EXTENSION_REQUIRED`;
- background FAIL → `STOP_C2_BACKGROUND_K_OR_MODE_LEAK_CANDIDATE_ONLY`, ktorý
  vyžaduje nezávislú reprodukciu pred autoritatívnym STOP;
- všetko PASS → `PASS_C2_FOURIER_ATOM_CANDIDATE_ONLY`.

## 6. Artefakty

- base: `scripts/baseScripts/p5_general_synchronous/c2_fourier_coverage.py`;
- runner: `scripts/301_script_KMPC_057_P5_3g7_C2_Fourier_coverage.py`;
- atóm:
  `RUN_KMPC_057_P5_3G7_C2_{MODE}_K{TOKEN}_NOMINAL.json`;
- agregát:
  `RUN_KMPC_057_P5_3G7_C2_FOURIER_COVERAGE_AGGREGATE.json`.

Každý proces má interný limit presne `4.8 s` a vonkajší `10 s`. Pred prvým
atómom: compile base/runner, help, behaviorálny smoke a output guard. Runner
musí mať explicitné `--atom` a `--aggregate`; aggregate nebeží, kým chýba
hociktorý z desiatich atómov.

## 7. Immutable C1 prerequisites

- AD KMPC-031 SHA `C547F818E3918CD844CA06BEA32814279A9D4A20D662A9166114410645792FF6`;
- CDI KMPC-040 SHA `69C78F70ECD851D8B8A48E4E09445181C0D4559E9BD2E90A7BA19933351BD219`;
- BI KMPC-046 SHA `60EC5A801FDDBAFFBA6CE184EBB3BC154879928385E6E37FB118781118615FB1`;
- NID KMPC-053 SHA `625AC2FAF4BD114D4907ABF83BFF059B50741642E7FB198FA3D7FBCB1BF3B4BD`;
- NIV KMPC-056 SHA `9AF6410513C2B0A6142DA9B08E8A1D115670C644171B102683568E64D645C332`.

## 8. Nonclaims

Bez `gamma0/af0` C3, S-M, full hierarchy, finite opacity, ODE/P5.4, G8/G9,
CLASS/CMB/BBN/S8/H0 a bez zmeny teórie.

## 9. Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | C1 CDI/BI/NID/NIV a AD sentinel uzavreté iba `.05/nominal` | `C2_AUTHORIZED` |
| 2026-07-18 | 10-atómová matica, support/depth mapa, prahy, background a rozhodovací strom zmrazené pred Python procesom | `PREREGISTERED` |
| 2026-07-18 | base SHA `757F97E14657CC7046177C2D33115CA87639B9C92E89BDABE2BFF3B4380DF3FC`; runner SHA `5DAE00681E443F406A7CF3C2ABC65998794E35E43706F16E03BBB478634884C2`; žiadny KMPC-057 output neexistuje | `FROZEN_BEFORE_PYTHON` |
| 2026-07-18 | compile a help PASS; smoke exit `1`: chybný guard porovnal uzavretý C1 support so starou S1 extended mapou; PF-077; žiadny atóm ani JSON nevznikol | `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT` |
