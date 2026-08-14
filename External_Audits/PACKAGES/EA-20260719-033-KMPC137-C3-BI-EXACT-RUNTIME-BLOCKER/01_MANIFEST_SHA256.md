# SHA-256 manifest EA-033

Zdrojom pravdy pre strojovú kontrolu je `01_MANIFEST_SHA256.tsv`.
Balík obsahuje 27 jedinečných evidence kópií. Každá má zhodný source a copy
SHA-256; žiadny súbor nie je duplicitne v `REPRO/`.

| Rozsah | Súbory | Úloha |
|---|---:|---|
| autoritatívny audit/plán/metodika | 3 | stav a rozhodovacie pravidlá |
| predregistrácie | 4 | zmrazený scope KMPC-134 až 137 |
| technické registre | 2 | PF a zákaz opakovania |
| raw výsledky/receipts | 8 | BI stav, štyri failure a KMPC-112 authority |
| primárny kód | 10 | exact formula/runtime lineage a C3 process |

Najdôležitejšie raw hashe:

- KMPC-131 BI/.15: `F04725F06B29AB596518CA9A9A2C34C6349D82AC17B743E007FB5D81B67E3A10`;
- KMPC-137 failure: `213F2B2E2516BBD4FC5A14C52D5750FD32DDECC727578DFDE04F0FD58A42E72A`;
- KMPC-112 success: `FAF52256489BA7C105F9125C1ED9A68358C0187E5F7B8B1164E1BA036A6507A1`.

