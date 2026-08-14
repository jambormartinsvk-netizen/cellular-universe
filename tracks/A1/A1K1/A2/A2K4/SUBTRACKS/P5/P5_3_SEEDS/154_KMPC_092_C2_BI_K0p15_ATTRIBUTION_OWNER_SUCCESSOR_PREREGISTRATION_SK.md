# KMPC-092 — attribution nested-owner successor: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `4/10`

## Jediná povolená zmena

V5 nahradí iba V2 `_owners_restored` počas V4 outer overlayu. Po ukončení
V2 inner overlayu musí overiť:

- `v1._coefficient_attribution` je pôvodný V1 callable zachytený pred V4;
- `v1.source_hashes` a `v1.contract_guard` sú pôvodné V1 ownery;
- po ukončení celého V4/V5 scope sa obnoví aj pôvodný V2 checker.

V1 term ledger, V2 serialization bound, V3 fixture a V4 float-product
correction zostávajú byteovo nezmenené. Rovnako sa nemenia rovnice, support,
80 dps, dva solve, holdout non-fit ani fyzikálne prahy.

## Zmrazená implementácia pred prvým Python behom

- V5 nested-owner overlay:
  `DDBF6EB49DA5FC46CBDB82694AEBD19A9C43EF0233973525D8BEE4035EC662D8`;
- runner 336:
  `E67BD2D15FACD3F23D11F9CAA39D68FABBDEB7D95234F11895C8CE0A46647677`;
- atomický/high-precision harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`;
- statická kontrola: `40/40` source/prerequisite hashov sedelo; všetkých
  `43` dlhých hash literálov malo 64 hex znakov.

Po freeze sa V5 ani runner pred official behom nemenia.

## Výsledok

- compile/help/corrected smoke a official všetky PASS:
  `REVIEW_C2_BI_K0p15_UPSTREAM_ATTRIBUTION_COMPLETE`;
- inak `TECHNICAL_ERROR / NO_PHYSICS_VERDICT` s presnými false checks.

Úspech resetuje counter na `0/10`; C2 ostáva `5/10`, K4 `60/100`.
