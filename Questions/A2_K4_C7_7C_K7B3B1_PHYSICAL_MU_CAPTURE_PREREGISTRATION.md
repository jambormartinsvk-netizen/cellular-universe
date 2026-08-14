# A2-K4 / C7.7c / K7b.3b.1 — predregistrácia fyzikálneho mu registra

Dátum: 2026-07-15  
Rodič: K7b.3b / skripty 170–172

## Hypotéza

Zlyhanie skriptu 172 vzniklo prepísaním high-precision registra druhým solve pri `mu=0`, nie fyzikálnym rozporom tvrdo viazaného riešenia.

## Povolená zmena

V nemennom pokračovaní skriptu 171 sa HP register a audit smú uložiť iba vtedy, keď súčasne platí:

- mód sa rovná požadovanému `--hp-mode`;
- `mu` sa rovná `physical_mu` v numerickej tolerancii `1e-30`.

Žiadna rovnica, kotva, tolerancia, rád Puiseuxovej série ani fyzikálny parameter sa nesmie meniť.

## Poradie brán

1. Zdrojový export musí prejsť a register musí niesť fyzikálne `mu`.
2. NID/deep sa testuje ako prvý.
3. Všetky pôvodné brány skriptu 172 ostávajú bez zmeny vrátane `D_activity_relative_error < 0.1`.
4. NID/shallow sa spustí iba po úplnom PASS NID/deep.

## Rozsudky

- PASS deep a shallow: K7b.3b.1 prežila koeficientovú/constraint bránu; ODE stále netestované.
- FAIL po správnom fyzikálnom zachytení: K7b.3b.1 je mŕtva s dôvodom podľa prvého fyzikálneho rezídua.
- Timeout, parser alebo export chyba: REVIEW, nie fyzikálna smrť.

Každý beh musí mať vnútorný aj vonkajší časový limit.
