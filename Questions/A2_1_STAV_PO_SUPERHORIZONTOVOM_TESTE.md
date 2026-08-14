# A2.1 — stav po prvom superhorizontovom teste

**Dátum:** 2026-07-13

## Rozhodnutie

- A2-K1: **MŔTVA — ARCHIVOVANÁ**.
- A2-K2: **MŔTVA — ARCHIVOVANÁ** už z gradientového testu.
- A1-K1: backgroundový ledger zostáva prežívajúcim účtovníctvom, ale zatiaľ nemá živú potvrdenú perturbačnú uzáveru.

## Aktuálne koľaje Q20

| Poradie | Koľaj | Stav | Ďalší test |
|---:|---|---|---|
| 1 | A2-K1: `Q^mu parallel u_c`, `c_s^2=1` | **MŔTVA M-009** | archivovaná |
| 2 | A2-K2: barotropické `c_s^2=w_f` | **MŔTVA M-008** | archivovaná |
| 3 | **A2-K3: `Q^mu parallel u_f`, `c_s^2=1`** | **NASLEDUJE** | vlastná Eulerova rovnica a superhorizontový mód |
| 4 | A2-K4: smer celkovej tmavosektorovej rýchlosti | `ČAKÁ` | až po K3 |
| 5 | A2-K5: akcia/mediátor | `ČAKÁ`; možná v4 | až po jednoduchších efektívnych koľajach |

## Varovanie pre A2-K3

Primárna literatúra naznačuje, že pri rovnakom smere energie a `w_f>-1` môže mať aj prenos rovnobežný s `u_f` rýchlostnú nestabilitu, hoci s iným koeficientom. Toto je iba predbežné riziko, nie verdikt. A2-K3 dostane samostatné odvodenie, skript a archívny záznam.

## Nasledujúci konkrétny krok

Odvodiť A2-K3 s presným mapovaním znamienok, otestovať nulový limit a spočítať jeho gauge-invariantný relatívny rýchlostný mód na rovnakom backgrounde. Ak zomrie, pokračovať A2-K4.

