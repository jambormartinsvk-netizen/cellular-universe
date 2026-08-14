# KMPC-091 — attribution float-product bridge successor: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `3/10`

## PF-094

Frozen KMPC-087 holdout volá `pair.scale(..., 1.5 * inputs.delta)`. Python
najprv vytvorí binary64 produkt a `_mp` až potom presne prenesie jeho binárny
pomer. V1 ledger použil `mp(1.5) * mp(inputs.delta)`, teda zmenil poradie
zaokrúhlenia iba vo svojom diagnostickom fuel term-e.

## Jediná povolená zmena

- V4 overlay zachová V1 počet termov, powers, owners a všetky nefuel členy;
- každý fuel contribution preškáluje presným pomerom
  `mp(1.5*delta_float) / (mp(1.5)*mp(delta_float))`;
- `equation_factor_decimal`, signed/absolute contribution, subtotals,
  fingerprint, residual, norm a cancellation diagnostiku po tejto jedinej
  zmene znovu zostaví;
- exportuje oba faktory, ich rozdiel a počet zmenených fuel termov;
- V2 serialization-aware validácia a V3 corrected fixture ostávajú
  nezmenené;
- frozen driver/holdout výpočet, dva HP solve, rovnice, support, non-fit a
  fyzikálne prahy sa nemenia.

## Zmrazená implementácia pred prvým Python behom

- V4 float-product overlay:
  `C8372850F29B70ADA5640F51E9B2701EB83144AC295C2E1EFC3D7CABBE232C46`;
- runner 335:
  `D870F42347B9B3CD8C2739921C41D781A9F991F1B2F21DA642B99CCBD797935E`;
- atomický/high-precision harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`;
- statická kontrola: `39/39` source/prerequisite hashov sedelo; všetkých
  `42` dlhých hash literálov malo 64 hex znakov.

Po freeze sa V4 ani runner pred official behom nemenia.

## Brány a výsledok

- term count, powers a owner množina pred/po sú identické;
- menia sa iba fuel termy a aspoň jeden existuje;
- všetky V1/V2/V3 a reconstruction brány PASS:
  `REVIEW_C2_BI_K0p15_UPSTREAM_ATTRIBUTION_COMPLETE`;
- inak `TECHNICAL_ERROR / NO_PHYSICS_VERDICT` s presnými false checks.

Úspech resetuje counter na `0/10`, ale C2 zostane `5/10` a K4 `60/100`.
