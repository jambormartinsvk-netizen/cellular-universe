# A2-K4 BR3C-b — konečný audit segmentovanej skorej evolúcie

**Dátum:** 2026-07-14  
**Rozsudok:** `C7.7b PASS`  
**Nová jemná hĺbka:** `66.5/100`  
**K4:** živá; `G6 PASS`, `G7 OTVORENÁ`

## Záver

NID a NIV boli z oboch auditovaných povrchov evolvované spoločnou
13-zložkovou ODE sústavou do `x=-18`. Všetky štyri trajektórie prešli všetky
segmenty, mali konečný stav aj RHS a neprekročili safety cap.

Pred numerickým behom skript 137 overil 13 rearrangement identít a osem
kritických znamienok proti zdrojovému kódu 136. Skript 136 potom prešiel
`27/27` kontrol za približne `6.39 s`.

## Prečo je výsledok iba C7.7b

Metrické derivácie boli počas integrácie definované z `00` a `0i`:

```text
h_x   = 3 delta_rho_total + 2 s^2 eta
eta_x = total momentum source.
```

Tieto dve rovnice preto nemôžu dostať druhý nezávislý PASS iba preto, že ich
integrátor používal. C7.8 musí zostaviť nezávislé propagované alebo redundantné
rezíduá; trace a traceless rovnice ešte neboli testované počas trajektórie.

Rovnako sa v C7.7b nehodnotí zhoda deep/shallow endpointov. Tá patrí do
C7.7d a môže odhaliť chybu truncation alebo počiatočnej asymptotiky aj po
úspešnom dobehnutí oboch solverov.

## Numerické riziko

Hlboký NIV beh potreboval `312842` RHS vyhodnotení, zatiaľ čo NID behy boli
rádu tisícov. Stav neexplodoval, ale rozdiel je varovným signálom pre
conditioning/stiffness. K4 kvôli nemu neumiera; povinne sa preverí pri
krokovej, tolerančnej a solverovej konvergencii.

## Skóre

```text
pred BR3C-b: 66.2/100
C7.7b PASS: +0.3
aktuálne:    66.5/100
```

Ďalší checkpoint C7.7c je samostatný audit, že žiadny species/mode komponent
nebol počas evolúcie iba formálne prítomný, zamrznutý alebo ticho nulovaný.

Výstup a kontrolné súčty sú v
`scripts/OUTPUT_A2_K4_3B_RG_BR3C_B_136_138.md`.

