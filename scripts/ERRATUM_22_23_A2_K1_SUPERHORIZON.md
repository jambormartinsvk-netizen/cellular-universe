# Erratum skriptu 22 a nástupca 23

**Dátum:** 2026-07-13

## Čo sa stalo

Skript 22 porovnal kroky `1e-3` a `5e-4`. Fyzikálne testy nestability prešli, ale relatívny rozdiel exponentu bol `3.6758627e-8`, nad predregistrovaným prahom `1e-8`. Preto správne vrátil návratový kód 1 a verdikt `REQUIRES_FULL_REVIEW`.

## Čo sa nemení

- odvodená rovnica módu;
- parametre `lambda=0.15`, `delta=0.02297`;
- background skriptu 13;
- prah konvergencie `1e-8`;
- kill conditions.

## Oprava

Skript 23 opakuje ten istý výpočet s krokmi `5e-4` a `2.5e-4`. Skript 22 zostáva zachovaný a nesmie sa mazať ani prepisovať.

