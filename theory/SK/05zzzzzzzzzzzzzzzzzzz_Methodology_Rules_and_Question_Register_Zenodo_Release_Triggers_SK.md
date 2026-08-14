# Dodatok k 05 — kritériá publikovania verzií na Zenodo (SK)

## Kontrola duplicity

AR5 chráni nemennosť už publikovanej verzie. AR9 vyžaduje Git commit/tag a technický release reťazec. AR48 pridáva doteraz chýbajúce rozhodnutie, **kedy** novú verziu vydať, kedy ju nevydávať a ako rozlíšiť patch, novú `3.x` a `4.0`. Pravidlá sa neduplikujú.

## AR48 — Zenodo vydanie vyžaduje materiálny spúšťač a úplnú release bránu

Nová Zenodo verzia smie vzniknúť iba pri materiálnom spúšťači: kritická oprava publikovaného tvrdenia, uzavretý vedecký míľnik, koherentný auditný snapshot, predregistračné zmrazenie pred externými dátami alebo reprodukčná zmena meniaca vedecký výsledok.

Jednotlivý pracovný podtest, timeout, otvorená otázka, nová hypotéza, desatinný posun hĺbky alebo refaktor bez zmeny výsledku novú verziu nespúšťajú. Zmeny sa zhromažďujú v Git histórii a pracovnom changelogu.

Zmena publikovaného súboru vždy vytvára novú verziu, aj keď Zenodo technicky povoľuje krátke opravné okno. Bez novej verzie sa smú meniť iba nesémantické metadáta a každá zmena musí mať metadata changelog.

Patch `3.x.y` nesmie meniť rovnice, čísla, verdikty, rozsah ani záver. Materiálna zmena tej istej teórie dostane novú verziu `3.x`. Zmena fundamentálnych postulátov, jadrovej dynamiky, ontológie alebo kauzálnej štruktúry vyžaduje `4.0`.

Release je `GO` iba po úplnom checkliste, zhode s Git tagom, changelogu, manifeste/SHA-256 a audite zmrazeného kandidáta. Každá zmena po manifeste resetuje release candidate.

## Q74 — kedy je v3.18 pripravená na Zenodo?

**Stav:** `OTVORENÁ RELEASE BRÁNA; AKTUÁLNE NO-GO.`

`R3.18-DOC` môže byť vydaná aj s otvorenou K4/G7, ak presne prizná otvorené brány a nepublikuje nové predikčné nároky. Musí však dokončiť upratanie dokumentácie, jediný kanonický stav, changelog v3.17 -> v3.18, SK/EN cross-check, celobalíkový manifest, Git commit/tag a nezávislý release audit.

`R3.18-PHYS/PREDICTION` zostáva NO-GO bez príslušných A2/G7, A3/G8 a pri dátovom fite G9 brán.

## Obmedzenie staršej formulácie A0

„A0 je vybavené“ znamená, že bolo prijaté pravidlo nemennosti, changelogu a kontrolných súčtov. Neznamená to, že každý aktuálny workspace alebo v3.18 kandidát automaticky prešiel publikačnou bránou.

