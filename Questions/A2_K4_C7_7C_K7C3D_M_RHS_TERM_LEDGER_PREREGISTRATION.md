# A2-K4 / C7.7c / K7c.3d — predregistrácia term ledgeru M-prime

Dátum: 2026-07-15  
Vstup: neasymptotická K7c.3b/c chyba dominantná v `M`

## Rozsah

Skript 185 sa spustí ako obmedzený child a jeho jemné NID/deep checkpointy `x=-25,-24.875,-24.75` sa iba diagnostikujú. Nová ODE sa nepridáva.

Pre každý checkpoint sa presne rovnaký zoznam členov `M'` vyhodnotí tromi cestami:

1. pôvodný ľavostranný float64 súčet;
2. `math.fsum` z tých istých float64 členov;
3. 80-dps `mpmath.fsum` s backgroundom z rovnakých registrovaných desatinných parametrov.

## Povinný výstup

- všetky jednotlivé členy `M'`;
- `sum_abs_terms/abs(high_precision_sum)` ako cancellation condition;
- absolútna chyba pôvodného súčtu a `math.fsum` voči 80-dps výsledku;
- pomer zlepšenia `old_error/fsum_error`;
- škálovaná chyba vzhľadom na integračnú škálu `M`;
- pevný child a celkový časový limit.

## Rozhodovanie

- Ak `math.fsum` zlepší chybu aspoň 10-násobne na každom aktívnom checkpointe, smie vzniknúť samostatná K7c.3e s jedinou zmenou: súčet už odvodených členov `M'` cez `math.fsum`.
- Ak zlepšenie nevznikne, fsum koľaj je mŕtva a musí sa hľadať algebraické preusporiadanie alebo vyššia pracovná presnosť.
- Diagnostika nemení skóre ani fyzikálne rovnice.
