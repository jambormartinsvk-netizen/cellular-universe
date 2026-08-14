# Dodatok k 05 — očakávania a odchýlky pred numerickým behom (SK)

Dátum: 2026-07-15  
Stav: záväzný dodatok; staršie pravidlá sa nemenia

## Kontrola duplicity

AR13 vyžaduje rozlíšený, konvergentný a constraintový numerický PASS. AR36 povoľuje rozšíriť toleranciu iba vopred odvodenou condition hranicou. AR39 zakazuje uvoľniť prah po výsledku v cancellation audite a AR53 vyžaduje technické smoke-testy. Chýbalo všeobecné pravidlo, ktoré pred každým vedeckým behom vyžaduje číselné alebo kvalitatívne očakávanie, prípustnú odchýlku a následnú tabuľku vzdialenosti od očakávania. AR54 vypĺňa túto medzeru bez zmeny starších prahov.

## AR54 — Očakávaný výsledok a prípustná odchýlka sa zapisujú pred behom

Pred prvým fyzikálnym alebo numerickým behom nového skriptu musí existovať datovaný MD záznam podľa `Questions/00_SCRIPT_PRE_RUN_EXPECTATION_TEMPLATE.md`. Pre každú rozhodujúcu veličinu musí uviesť:

- či je očakávanie analytické, regresné alebo exploratívne;
- očakávanú hodnotu, interval, znamienko, rád alebo trend;
- zdroj očakávania a nezávislé invarianty;
- numerickú a fyzikálnu prípustnú odchýlku, ak sú odvoditeľné;
- presné PASS, acceptable, REVIEW a fyzikálne kill kritériá;
- interný aj externý časový limit podľa AR29.

Ak číselné očakávanie nie je poctivo odvoditeľné, zapíše sa `NEZNÁME/EXPLORATORY`; nesmie sa vymyslieť stredná hodnota. Stále sa však predregistrujú fyzikálne rozsahy, invarianty, bezpečnostné capy a rozhodovací postup.

Po behu sa povinne uvedie pozorovaná hodnota, absolútna a relatívna alebo normalizovaná odchýlka a informácia, či leží vo vopred povolenom intervale. Výsledok v tolerancii môže byť `ACCEPTABLE_WITHIN_TOLERANCE`, iba ak zároveň prešiel nezávislými fyzikálnymi bránami.

Pôvodné očakávanie ani tolerancia sa po výsledku neprepisujú. Zmena vyžaduje datovaný dodatok, nezávislé odôvodnenie a nový beh alebo novú podkoľaj. Pôvodný beh si zachová verdikt podľa pôvodnej brány. Post-hoc zmena bez dôkazu je zakázaná.

## Q79 — Aké očakávania platia pred najbližším pokračovaním K4/K7c?

Najbližší fail-closed nástupca 175/176 je regresný audit: fyzikálny payload sa nesmie zmeniť; zmeniť sa smie iba správanie pri chýbajúcich rankových kľúčoch. NID/NIV deep/shallow musia reprodukovať tabuľku K7b a synteticky chýbajúci kľúč musí zlyhať uzavreto.

Čistý samostatný RK4 prepis musí najprv reprodukovať REVIEW 184/185 vrátane pomeru približne `0.367`; refaktor sám nesmie zázračne vytvoriť konvergenciu. Až nový term ledger smie testovať hypotézu, že `math.fsum` zníži chybu `M'` najmenej desaťnásobne na každom aktívnom checkpointe.
