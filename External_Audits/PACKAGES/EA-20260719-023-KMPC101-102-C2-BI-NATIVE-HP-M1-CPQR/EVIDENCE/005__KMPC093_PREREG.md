# KMPC-093 — BI/k=.15 high-precision M1 reassembly: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `0/10`

## Zdrojový dôvod

Živá C2 funkcia `_standard_depth` volá priamo
`mode_resolved_puiseux_v2_m1_anchored.solve_standard_seed_anchored`. Táto
funkcia zostavuje M1 maticu a konštantu cez binary64 `Series` a rieši ich
`numpy.linalg.lstsq`. Modul KMPC-037 je iba oddelený numerical-boundary
audit; jeho refined ani 80-dps vektor sa do C2 pipeline nevkladá.

KMPC-092 lokalizoval dominantný `Einstein_0i[7]` upstream subtotal na
fractional background × M1 (`-7.04818880487719e-9`). Keďže tento owner je
bilineárny, najmenšia ďalšia hranica musí izolovať jednu jeho stranu. Ako
prvá sa testuje M1, lebo živá pipeline používa raw binary64 solve.

## Zmrazený rozsah

- iba `BI`, `k=0.15 Mpc^-1`, nominal, M1 order/depth `7`;
- tá istá M1 báza: 11 stavov × mocniny `-1…7`, plný systém `121×99`, po
  presnej eliminácii hard anchor `h[1]` reduced systém `121×98`;
- M1 driver aj initial riadky sa znovu zostavia pri `80 dps` a reduced
  overdetermined systém sa vyrieši jedným unweighted `mpmath.qr_solve`;
- matematické racionálne koeficienty M1 rovníc sa vyhodnotia natívne pri
  80 dps; nemení sa tým rovnica, iba sa odstráni binary64 assembly krok;
- štandardný background generátor sa **nemení**: jeho binary64 koeficienty
  sa prenesú presne cez `float.as_integer_ratio` bridge;
- hard anchor je presný bridge pôvodnej binary64 hodnoty
  `h[1]=0.007663658973679146`; initial hodnoty sa prenesú rovnakým spôsobom;
- nový M1 stav sa vloží iba do už zmrazeného 80-dps exact M3 driver/holdout
  a attribution pipeline KMPC-092;
- F0, fractional-background generátor, M3 rovnice, support `[0,5]→[0,7]`,
  vstupy a všetky prahy ostávajú nezmenené;
- `Einstein_00/0i` ostávajú non-fit holdouty; nepridá sa žiadny holdout riadok;
- počet HP solve je jeden nový M1 solve plus pôvodné dva M3 solve, spolu tri.

## Brány

1. exact source/prerequisite hashe, BI/k/order/shape identita a hard anchor;
2. M1 driver+initial residual aj oba M1 holdouty prejdú pôvodným `1e-10`
   hybridným prahom;
3. presne jeden nový M1 QR solve, tri HP solve celkom a nulový počet holdout
   riadkov vo všetkých solve;
4. pôvodné common, tail, background, S-C0 a exact M3 driver brány prejdú;
5. KMPC-092 attribution sa úplne zrekonštruuje nad novým M1 stavom;
6. owner lifecycle, compile, help, behaviorálny smoke, native JSON a
   immutable output prejdú.

## Predregistrované interpretácie

- M1 systém sa uzavrie a `Einstein_0i[7] <= 1e-9`:
  `PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_HP_M1_CANDIDATE_ONLY`;
- M1 systém sa uzavrie, ale C2 holdout ostane nad prahom:
  `REVIEW_C2_BI_K0p15_NON_M1_UPSTREAM_PRECISION_REQUIRED`;
- M1 driver/holdout sa pri natívnom 80-dps zostavení neuzavrie:
  `REVIEW_C2_BI_K0p15_HP_M1_SYSTEM_UNCLOSED`;
- implementačná alebo identity brána zlyhá:
  `TECHNICAL_ERROR / NO_PHYSICS_VERDICT`.

Ani candidate PASS nemení autoritatívny C2 stav pred interným auditom.
C2 ostáva `5/10`, P5 `3.5/6`, K4 `60/100`; release/Zenodo/prediction
trigger sú `NONE`.

## Zmrazená implementácia pred prvým Python behom

- HP M1 modul:
  `4509F89AB9987AF271DCC37F8D973672E647ABDBEBB8271D0B3B327A2F831065`;
- runner 337:
  `E4D97F39AD835F8D55AF72EE457B90BFDE9587F8A646A9B6DA1EF49D1BDF935D`;
- atomický/high-precision harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`;
- statická kontrola: `42/42` source/prerequisite hashov sedelo; všetkých
  `45` dlhých hash literálov malo presne 64 hex znakov.

Po tomto freeze sa modul ani runner pred official behom nemenia.
