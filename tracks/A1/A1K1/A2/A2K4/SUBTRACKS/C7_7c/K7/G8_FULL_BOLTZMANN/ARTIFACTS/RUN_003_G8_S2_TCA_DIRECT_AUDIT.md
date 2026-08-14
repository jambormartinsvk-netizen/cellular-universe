# RUN-003 — audit G8 SCREEN-S2: direct/TCA overlap

**Verdikt:** `PASS_G8_SCREEN_S2_TCA_DIRECT`  
**Skóre:** `0`; support/WBS ostáva `90/100`  
**Autoritatívny artefakt:** `RUN_003_G8_S2_TCA_DIRECT_RESULT.json`

**SHA-256 JSON:** `8ADAF71C7E36A80306DC69CC75D2F4F46283C007BB4E60E5F56772C743C627A1`

## Čo prešlo

Na `x=-23 → -22` bol explicitný tuhý fotónovo-baryónový blok integrovaný
Radau metódou a porovnaný s kombinovaným K7 tight-coupling limitom riešeným
DOP853. Zdrojový K4 background skript 213 mal presný zmrazený SHA-256.

| Veličina | Výsledok | Hranica | Stav |
|---|---:|---:|---|
| direct–TCA overlap | `7.057×10^-11` | `<=1×10^-4` | PASS |
| fotón–baryón slip | `4.887×10^-9` | `<=1×10^-6` | PASS |
| max TCA parameter | `1.893×10^-9` | `<=1×10^-6` | PASS |
| direct RHS volania | `532` | `<=100000` | PASS |
| TCA RHS volania | `761` | `<=100000` | PASS |

Oba integrátory dosiahli endpoint, všetky hodnoty boli konečné a pod
safety cap. Vnútorný čas bol `0.047 s`; celý proces skončil za `1.9 s`,
pod limitmi 45 s/55 s.

## Správna interpretácia

S2 potvrdzuje, že nová oddelená formulácia neporušila už overený K7
fotónovo-baryónový limit v hlbokom tight-coupling režime. Nie je to test
plnej fotónovej teplotnej/polarizačnej ani neutrínovej hierarchie. `chi=100`
je deklarovaná bezrozmerná testovacia väzba, nie odvodená fyzikálna opacity;
preto výsledok nedokazuje rekombináciu, posledný rozptyl, CMB spektrum ani
G8/FULL PASS.

## Ďalší krok

Povolený je SCREEN-S3: jeden zmrazený `lmax=8,12,16` sweep s
asymptotickým closure, rovnakým K4 backgroundom a konvergenciou nízkych
momentov. S3 musí pred behom explicitne pridať fotónový šmyk, polarizáciu a
free-streaming chvost; nesmie preberať S2 syntetickú `chi` ako fyzikálnu
rekombináciu.
