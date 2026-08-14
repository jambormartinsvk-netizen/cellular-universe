# KMPC-094 — HP-M1 attribution-owner successor: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `1/10`

## Jediná povolená zmena

V2 počas KMPC-093 outer M1 overlayu nahradí iba vnorený V1
`_owners_restored` checker. Po ukončení V1 attribution overlayu musí overiť,
že driver `_exact_driver_boundary`, driver `source_hashes` a assembly
`_holdout_affine` boli obnovené na ich skutočných pôvodných ownerov, nie na
outer-dočasnú HP-M1 funkciu. Po ukončení celého V2 scope sa musí obnoviť aj
pôvodný V1 checker.

Frozen KMPC-093 modul s SHA
`4509F89AB9987AF271DCC37F8D973672E647ABDBEBB8271D0B3B327A2F831065`
sa nemení. Nemení sa M1 systém, 80 dps, QR solver, background bridge, F0,
fractional background, M3, support, prahy, term ledger ani non-fit holdout.

## Zmrazená implementácia pred prvým Python behom

- V2 attribution-owner modul:
  `C9E8691F7A9BA5BD055DCAC086DC2CC0E421E3D01278B2C59608D601FB49FC7B`;
- runner 338:
  `D3FF15EE2B10C879FC2AE9C920A2942285ABB8474EA37ADDB84F318C76E61D1F`;
- atomický/high-precision harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`;
- statická kontrola: `43/43` source/prerequisite hashov sedelo; všetkých
  `46` dlhých hash literálov malo presne 64 hex znakov.

Po freeze sa V1, V2 ani runner pred official behom nemenia.

## Výsledok

Po úspešnom compile/help/smoke sa official výsledok interpretuje presne podľa
predregistrácie 156. Ak owner lifecycle alebo iná implementačná brána zlyhá,
výsledok je iba `TECHNICAL_ERROR / NO_PHYSICS_VERDICT`. Úspech resetuje
counter na `0/10`; C2 ostáva do interného auditu `5/10`, K4 `60/100`.
