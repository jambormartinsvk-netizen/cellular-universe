# Dodatok k 05 — A2-K4.3b-BR, podmienenie rezíduí a módové Puiseuxove rády (SK)

**Dátum:** 2026-07-14  
**Stav:** záväzný dodatok; staršie pravidlá sa nemenia

## Kontrola duplicity

AR32 rieši nulový prefix backendu a AR33 dostatočný rád gauge mapy. Neurčujú
numerické podmienenie Einsteinových derivácií, škálu kompenzovaných species
zdrojov ani podmienky pre uvoľnenie tolerancie. AR34–AR36 vypĺňajú tieto tri
odlišné medzery bez duplikácie.

## AR34 — Constraintový rozsudok musí rešpektovať podmienenie derivácie

Hlbokoradiačný test nesmie vyhlásiť fyzikálny `FAIL` iba zo surovej konečnej
druhej derivácie metriky násobenej veľkým faktorom `Hconf^2`. Musí použiť
aspoň jednu stabilnú alternatívu: constraintovú DAE formuláciu, analytickú
Bianchi deriváciu product ledgeru alebo preukázanú konvergentnú vyššiu
presnosť. Nevhodná derivácia zostáva archivovaná ako numerický REVIEW.

## AR35 — Kompenzované zdroje sa tvoria na prirodzenej škále

Pri NID, NIV a interných species módoch sa celkové `delta rho`, momentum a
shear nesmú tvoriť odčítaním surových `X_A ~ a^-4`, ak tým zaniknú platné
cifry. Použije sa `Omega_A=X_A/E^2`, vyššia presnosť alebo algebraicky
projektovaná kompenzovaná báza. Fyzikálny výsledok sa nesmie opierať o
catastrophic cancellation.

## AR36 — Tolerancia sa smie rozšíriť iba vopred odvodenou condition hranicou

Pevná tolerancia sa pre konkrétny kompenzovaný ledger môže nahradiť iba
hranicou odvodenou zo `sum(abs(species components))`, machine epsilon a
deklarovaného počtu operácií. Hranica musí byť vypočítaná pred interpretáciou
rezídua, musí platiť iba pre pomenované rovnice a nesmie plošne uvoľniť ostatné
brány.

## Q61a — Aktuálny stav K4.3b po BR3A

**Stav:** `BR1 PASS; BR2 PASS; BR3A PASS; K4.3b NEUZAVRETÁ.`

Sedem skorých módov prešlo dve hĺbky, štyri Einsteinove rovnice a dva
conservation ledgery. Päť kolektívnych módov prešlo módovo závislé
Puiseuxove zdroje. Chýba indukovaný frakčný metric/species koeficient a plná
photon/polarization/recombination implementácia.

## Q62 — Ako neskorší audit obmedzil staré exponenty 3.93109 a 4.93109?

Tieto čísla zostávajú správne pre backgroundové prefaktory `Omega_f` a
`(Gamma/H)(rho_f/rho_c)`. Nie sú univerzálnymi konečnými exponentmi poruchy.
Úplný zdroj pridáva vedúcu mocninu konkrétneho seedu. Overené tlakové rády sú
pre AD/CDI/BI/NID/NIV postupne `5.93109`, `4.93109`, `4.93109`, `6.93109`,
`5.93109`; ash-transfer rády sú `6.93109`, `4.93109`, `5.93109`, `7.93109`,
`6.93109`.

## Q63 — Čo je ďalší rozhodovací krok?

`BR3B`: vyriešiť indukované frakčné koeficienty metriky a všetkých
gravitačne viazaných species a koeficientovo overiť štyri Einsteinove rovnice.
Bez BR3B a plnej photon backendovej brány sa G7 ani skóre nad `60/100`
nesmú priznať.

