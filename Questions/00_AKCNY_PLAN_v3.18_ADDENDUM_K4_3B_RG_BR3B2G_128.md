# Akčný plán v3.18 — dodatok po BR3B-2g

Dátum: 2026-07-14  
A2-K4: **ŽIVÁ, 60/100 = G6**

| Poradie | Úloha | Brána | Stav |
|---:|---|---|---|
| 1 | BR3B-2g: `l=3`, transfer-corrected fuel, ash `delta_c` a prvý ash gravity | rank, všetky riadky, lambda-zero, presné poradie | **DONE — PASS** |
| 2 | BR3C-a: zostaviť počiatočný stav z koeficientov 127 pri dvoch skorých hĺbkach | všetky species, metric, `F3`; rovnaká normalizácia | **NEXT** |
| 3 | BR3C-b: spustiť úplnú skorú evolúciu s krátkym horizontom | žiadny timeout; konečné premenné | PENDING |
| 4 | BR3C-c: auditovať `00`, `0i`, trace a traceless Einsteinove rezíduá | absolútna aj škálovaná brána | PENDING |
| 5 | BR3C-d: zopakovať pri polovičnom kroku a prísnejšej tolerancii | stabilný transfer a rezíduá | PENDING |
| 6 | BR3C-e: zmeniť počiatočnú hĺbku a `lmax` | rovnaké neskoré riešenie v tolerancii | PENDING |
| 7 | Rozsudok celej G7 | všetky podbrány GO; žiadne priemerné či čiastočné skóre | PENDING |
| 8 | BR4: nezávislý plný backend/cross-check | až po uzavretí BR3C | PENDING |

## Povinné pravidlá BR3C

- Počiatočné vyššie multipóly musia rešpektovať gradientovú regularitu; nesmú
  sa fitovať ako nezávislé homogénne amplitúdy.
- Skript musí mať vnútorný limit najviac 50 s a vonkajší limit najviac 60 s.
- Relatívne rezíduum bez absolútnej brány nie je dôkaz pri noise/noise delení.
- Timeout, singularita alebo neuzavretý constraint znamenajú `UNCLOSED`, nie
  automatickú smrť K4.
- Kanonické skóre ostáva `60/100 = G6`, kým neprejde celá G7.

