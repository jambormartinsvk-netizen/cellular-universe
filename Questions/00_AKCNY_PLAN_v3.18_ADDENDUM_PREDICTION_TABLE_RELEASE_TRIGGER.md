# Akčný plán v3.18 — predikčná tabuľka ako release trigger

## Priorita

Riadkový audit publikovanej tabuľky v3.17 je povinná časť R3.18-DOC a predchádza jej automatickému kopírovaniu do novej verzie.

## Poradie

| Krok | Úloha | Výstup | Rozhodnutie |
|---:|---|---|---|
| PT-A0 | inventarizovať všetky publikované SK/EN/CSV/PDF tabuľky a ich verziové DOI | nemenný zoznam starých artefaktov | chýbajúca verzia/DOI blokuje audit riadku |
| PT-A1 | pre každý riadok identifikovať pôvodný mechanizmus, skript a dôkazovú úroveň | evidence map | bez dôkazu status najviac `HISTORICAL/RECALCULATION OPEN` |
| PT-A2 | priradiť jeden z piatich stavov aktuálnosti | row-by-row audit | `WITHDRAWN/SCOPE NARROWED` aktivuje PT1 |
| PT-A3 | pri PT1 vytvoriť úzky erratum balík bez čakania na náhradu | Git záznam do 3 pracovných dní; cieľ Zenodo do 14 dní | stará hodnota zostáva historická, nie aktuálna |
| PT-A4 | pre nové výpočty predregistrovať fyzikálnu a reprodukčnú bránu | replacement protocol | neauditovaná hodnota nesmie byť `PREDICTION` |
| PT-A5 | pri PT2 zmraziť novú tabuľku, audit a manifest | prediction-table RC | cieľ Zenodo do 30 dní |
| PT-A6 | zapracovať výsledok do R3.18 changelogu a README/BibTeX | citable mapping starý DOI -> nový DOI | žiadny starý riadok sa nemaže |

## Povinné prvé súbory na audit

- `theory/SK/03b_Predictions_Table_v3.17_SK.csv`;
- `theory/EN/03_Predictions_Table_v3.17_EN.csv`;
- príslušné publikované PDF a Zenodo balíky;
- všetky neskoršie audity, ktoré zmenili status alebo rozsah daného riadku.

## Stop pravidlo

Ak sa pri audite nájde stará hodnota, ktorá je už preukázateľne chybná, riadkový audit sa neodkladá do dokončenia všetkých ostatných riadkov. Pre danú hodnotu sa okamžite otvorí PT1 erratum vetva.

