# KMPC-096 — HP-M1 scale-fixture successor: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `3/10`

## Jediná povolená zmena

V4 nahradí iba syntetický V3 scale fixture. Nový fixture beží celý pri
`80 dps`, používa stĺpcový scale ratio `1e24`, absolútnu solution bránu
`1e-35`, residual bránu `1e-50` a ratio porovnáva numericky s relatívnou
toleranciou `1e-70`. Stále ide o 24-rádový test column equilibration, ale
nežiada 60 správnych miest po 40-rádovom zrušení.

V3 `_column_equilibrated_solve`, V1 M1 reassembly a V2 owner oprava ostávajú
byteovo nezmenené. Rovnako sa nemenia rovnice, support, vstupy, 80 dps,
background bridge, F0, fractional background, M3, prahy ani non-fit holdout.

## Zmrazená implementácia pred prvým Python behom

- V4 scale-fixture modul:
  `5C04E54C6AD89E936862A090AEC35F0A69F032B6350F4A59EA5A256BB3797240`;
- runner 340:
  `5A8C190E79FB1CA826C681D4A611E7A2042ED9CE64F60EFBCEBCC283B8A7B25F`;
- atomický/high-precision harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`;
- statická kontrola: `45/45` source/prerequisite hashov sedelo; všetkých
  `48` dlhých hash literálov malo presne 64 hex znakov.

## Výsledok

Po úspešnom compile/help/smoke sa official výsledok interpretuje podľa
predregistrácie 156. False fixture alebo implementačný pád je iba
`TECHNICAL_ERROR / NO_PHYSICS_VERDICT`. Úspešný vecný výpočet resetuje
counter na `0/10`; autoritatívny C2/K4 stav sa mení až po internom audite.
