# A2-K4 / C7.7c-K4 — audit analytického obálkového škálovania

## Rozsudok

**TIMEOUT_UNCLOSED; bez bodov; nie fyzikálna smrť K4.**

Tretia normalizačná podkoľaj úspešne vytvorila vopred registrovanú analytickú obálku všetkých zložiek, ale následná evolúcia sa neuzavrela v pevnom časovom limite.

## Čo prešlo

Skript 146 rozšíril už auditovaný koeficientový motor o tretiu referenčnú plochu `x_ref = -18`. Nezmenil rovnice ani koeficienty. Výsledok:

- `PASS_C7_7C_K4_ANALYTIC_REFERENCE_STATE`,
- 94/94 zdedených a nových kontrol PASS,
- všetky referenčné stavy a backgroundové veličiny konečné,
- obálka `L4_fs` pre hlboký NID: približne `1.8039092102682284e-24`,
- obálka `L4_fs` pre hlboký NIV: približne `5.135204691461256e-20`.

Tým sa odstránila chyba K2/K3, v ktorej sa vyššie multipóly škálovali iba extrémne malou počiatočnou hodnotou, miestami okolo `1e-42`.

## Čo sa neuzavrelo

Skript 148 spustil skript 147 s týmito zmrazenými limitmi:

- DOP853,
- `rtol = 1e-10`,
- normalizované `atol = 1e-12`,
- `max_step = 0.02`,
- interný limit evolúcie 45 s,
- obalový limit 50 s,
- externý limit 60 s.

Výsledok po približne 46,4 s:

`ERROR_UNCLOSED: script 147 returned 124; TIMEOUT_UNCLOSED; BR3C-b internal deadline exceeded`.

Keďže evolúcia nedodala úplný ledger štyroch trajektórií, nemožno vyhodnotiť 13-zložkovú bránu aktivity.

## Interpretácia

Analytické obálkové škálovanie odstránilo identifikovanú podmienkovú chybu počiatočných mierok, ale neodstránilo výpočtovú náročnosť NIV evolúcie. Tým sa zosilňuje evidencia, že ďalší pokrok vyžaduje profilovanie alebo formuláciu/solver prispôsobený stuhnutému systému, nie ďalšie svojvoľné menenie tolerancií.

Tri po sebe idúce ohraničené varianty narazili na tú istú praktickú stenu:

| Podkoľaj | Zmena | Výsledok |
|---|---|---|
| C7.7c-K2 | DOP853, mierka iba zo začiatku | timeout |
| C7.7c-K3 | Radau, mierka iba zo začiatku | timeout/chyba zle podmieneného Jacobianu |
| C7.7c-K4 | DOP853, analytická obálková mierka | timeout |

## Stav a ďalší postup

- K4 zostáva **živá, technicky pozastavená**, na **66,5/100**.
- Posledná úplná hlavná brána ostáva G6; G7 je otvorená.
- C7.7c ešte neprešla.
- Skripty 146–149 a tento audit sa uchovávajú; neúspešná podkoľaj sa nemaže.
- Pred ďalšou optimalizáciou K4 sa vykoná rýchly audit nezačatých koľají A2-K8 a A2-K9. Potom sa porovná počet živých kandidátov a cena ďalšieho kroku.

## Čo výsledok neznamená

Timeout nie je porušenie fyzikálneho zákona, divergencia riešenia ani nesplnenie observačného rozsahu. Nemožno ho použiť ako dôvod smrti K4.

