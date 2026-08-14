# A2-K4 / C7.7c-K7a-J2 — predregistrácia 80-cifernej kontroly T'

**Dátum:** 2026-07-14  
**Dôvod:** double centrálna diferencia nedokáže relatívne overiť deriváciu `T'~10^-8` odčítaním matíc rádu `1`.  
**Skóre:** bez zmeny; žiadna ODE evolúcia.

## 1. Nemenné prvky

- rovnaké backgroundové vzorce a parametre ako skript 136;
- rovnaké analytické `Omega_A'`, `W_gamma'`, `W_f'` ako skript 159;
- rovnaké štyri povrchy NID/NIV × deep/shallow;
- rovnaký prah relatívnej chyby `<10^-8`;
- žiadna zmena `D',M'`, Jacobianu ani fyziky.

## 2. Nová numerická metóda

- `mpmath` s `mp.dps=80`;
- centrálne rozdiely pre kroky `10^-8`, `10^-12`, `10^-16` v premennej `x=ln a`;
- analytická aj FD `T'` sa zostavia v rovnakej 80-cifernej aritmetike;
- reportuje sa max. absolútna a relatívna Frobeniova chyba;
- výsledok sa až po porovnaní prevedie na JSON float/string výstup.

## 3. Acceptance

- všetky hodnoty konečné;
- aspoň dva po sebe idúce kroky majú relatívnu chybu `<10^-8`;
- najlepšia relatívna chyba `<10^-12`;
- analytická `T'` po konverzii súhlasí s double implementáciou skriptu 159 relatívne `<10^-14`;
- NID a NIV na rovnakom povrchu dávajú identický backgroundový výsledok.

## 4. Stop pravidlo

Ak J2 zlyhá, K7a sa nepresunie na ostatné Jacobianové povrchy ani k evolúcii. Prah sa neznižuje; treba auditovať analytické backgroundové derivácie.
