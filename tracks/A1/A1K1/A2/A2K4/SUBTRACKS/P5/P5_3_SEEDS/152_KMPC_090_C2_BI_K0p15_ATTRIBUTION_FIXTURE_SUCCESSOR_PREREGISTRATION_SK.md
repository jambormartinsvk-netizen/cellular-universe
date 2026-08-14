# KMPC-090 — attribution 80-dps fixture successor: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `2/10`

## PF-093

V2 `_serialized_two_ulp` vypočítal správny bound. Chybný bol iba smoke:
`bound` a `ulp` vznikli pri 80 dps, ale výraz `2*ulp` sa pri returne znovu
vyhodnotil už pri defaultnej mpmath presnosti. Preto dve matematicky rovnaké
hodnoty nemali rovnakú internú reprezentáciu.

## Jediná povolená zmena

- nový V3 owner overlay nahradí iba V2 `_fixture`;
- výpočet boundu, `2*ulp` aj ich porovnanie prebehne v jednom
  `mp.workdps(80)` bloku;
- fixture zároveň overí presných 50 významných číslic a rozdielne exponentové
  škály residual/norm;
- V1 ledger, V2 dynamic serialization formula, source vstupy, dva HP solve,
  rovnice, support, holdout non-fit a fyzikálne prahy ostávajú byteovo
  nezmenené;
- official sa smie spustiť iba po compile/help a úspešnom corrected smoke.

## Zmrazená implementácia pred prvým Python behom

- V3 fixture overlay:
  `62F049762892938867EE33C83F37DDE572431B31AF05837866E4F590D0A8B23E`;
- runner 334:
  `BACA676789BBF8E2713719505E03FEB44E12FB3F8E0387BEB3590D47C7AF5E8E`;
- atomický/high-precision harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`;
- statická kontrola: `37/37` source/prerequisite hashov sedelo; všetkých
  `40` dlhých hash literálov malo 64 hex znakov.

Po freeze sa V3 ani runner pred official behom nemenia.

## Výsledok

- všetky brány PASS: `REVIEW_C2_BI_K0p15_UPSTREAM_ATTRIBUTION_COMPLETE`;
- inak `TECHNICAL_ERROR / NO_PHYSICS_VERDICT` s presnými false checks.

Úspech resetuje aktívny counter na `0/10`, ale nemení C2 `5/10` ani K4
`60/100`.
