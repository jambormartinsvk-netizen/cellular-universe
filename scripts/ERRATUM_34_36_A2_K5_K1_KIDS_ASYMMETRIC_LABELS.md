# ERRATUM skriptov 34/36 — označenie asymetrických chýb KiDS-Legacy

**Dátum:** 2026-07-13  
**Rozsah opravy:** iba názvy dvoch výstupných položiek; fyzika a čísla sa nemenia

Skript 34 vypočítal pomery voči obom publikovaným šírkam
`S8 = 0.815 (+0.016/-0.021)`, ale hodnotu delenú `0.021` pomenoval ako
konzervatívny „high-side“ výsledok. Pri modelovej hodnote nad centrálnou
hodnotou je formálnou hornou asymetrickou šírkou `+0.016`.

Skript 36 preto zachováva oba výpočty a používa jednoznačné názvy:

- `formal_asymmetric_high_side_sigma_using_plus_0.016`;
- `conservative_wider_error_ratio_using_0.021`.

Žiadny z týchto pomerov sa nesmie interpretovať ako platná likelihoodová
signifikancia. Projekcia `S8` dedí neoverenú normalizáciu `0.8745` a nie je
výstupom CMB-normalizovaného Boltzmannovho riešiča.

Skript 34 sa nemaže: zostáva historickou stopou pôvodného výstupu. Na citovanie
sa používa skript 36.
