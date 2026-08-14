# A2-K4 / C7.7c — audit počiatočnej condition mapy RHS

**Dátum:** 2026-07-14  
**Skripty:** 155 a 156  
**Typ testu:** nulovo-integračný; štyri autoritatívne počiatočné povrchy  
**Skóre pred/po:** `66.5/100`  
**Rozsudok:** lokalizovaná aritmetická stena NID; A2-K4 ostáva **ŽIVÁ**.

## 1. Metóda

Pre každý RHS súčet sa vypočítalo:

- `sum_abs = sum(abs(term_j))`;
- kompenzovaný `math.fsum(term_j)`;
- condition číslo `sum_abs/abs(fsum)`;
- štandardná forward roundoff hranica `gamma_n × sum_abs`, kde `gamma_n=n eps/(1-n eps)`;
- pomer `abs(fsum)/roundoff_bound`.

Test nemení rovnice ani stav a nevykonáva ODE evolúciu.

## 2. Kľúčové výsledky

| Mód/povrch | Zdroj | Condition číslo | Signal / roundoff bound | Hodnotenie |
|---|---|---:|---:|---|
| NID/deep | celková hustota | `4.96×10^15` | `0.182` | pod double hranicou |
| NID/deep | `h_x` | `5.58×10^15` | `0.134` | pod double hranicou |
| NID/deep | `eta_x` | `5.93×10^14` | `1.90` | hraničné |
| NID/shallow | celková hustota | `7.44×10^15` | `0.121` | pod double hranicou |
| NID/shallow | `h_x` | `5.58×10^15` | `0.135` | pod double hranicou |
| NID/shallow | `eta_x` | `8.93×10^12` | `126` | rozlíšiteľné, ale podmienené |
| NIV/deep | celková hustota | `8.49×10^8` | `1.06×10^6` | rozlíšiteľné |
| NIV/deep | `h_x` | `8.49×10^8` | `8.84×10^5` | rozlíšiteľné |
| NIV/deep | `eta_x` | `2.02×10^14` | `5.58` | podmienené, nad hranicou |
| NIV/shallow | celková hustota | `1.15×10^8` | `7.84×10^6` | rozlíšiteľné |
| NIV/shallow | `h_x` | `1.15×10^8` | `6.53×10^6` | rozlíšiteľné |
| NIV/shallow | `eta_x` | `3.56×10^12` | `317` | rozlíšiteľné, podmienené |

NID/deep `h_x` má `fsum≈4.44×10^-16`, kým forward hranica je `≈3.30×10^-15`. NID/shallow dáva prakticky rovnaký pomer. Takýto zdroj nemožno v double precision čestne používať na integráciu komponentu s `atol_h≈1.76×10^-26`.

## 3. Čo nie je problém

Samotné vysoké multipóly nie sú aritmeticky zle podmienené:

- NID/deep `L3_fs` a `L4_fs` majú condition číslo prakticky `1`;
- NIV/deep aj NIV/shallow `L4_fs` majú condition číslo `1`;
- ich malá amplitúda je problém absolútnej škály, nie odčítania v ich vlastných RHS rovniciach.

K6 však integrovala celý coupled systém. NID gravitačný zdroj pod roundoff hranicou kontaminoval metrické a gravitačne viazané komponenty a znemožnil požadované extrémne `atol`.

## 4. Fyzikálny a numerický rozsudok

- K4 nie je fyzikálne mŕtva.
- K4/K5/K6 zlyhali ako numerické reprezentácie aktivity.
- Ďalšie predlžovanie runtime ani plošné uvoľnenie tolerancií nie je prípustné.
- Ďalšia podkoľaj musí odstrániť odčítanie NID species v celkovej hustote a momente algebraicky projektovanou kompenzovanou bázou alebo autoritatívnou vyššou presnosťou.

## 5. Obmedzenie

Mapa platí na počiatočných povrchoch `x=-25` a `x=-23`. Sama nepreukazuje evolučnú stabilitu, aktivitu všetkých komponentov ani plnú C7.7c. Je iba príčinným auditom smrti K6 a vstupom pre K7.

