# RUN-004 — G8 SCREEN-S3: zmrazený sweep multipólového chvosta

**Úloha:** overiť numerickú konvergenciu chvosta, nie vyhlásiť plný G8 backend.

Tri lineárne, škálované hierarchie `J`, `E`, `G` sa integrujú na K4
radiačnom intervale `x=-23 → -22` pre `lmax=8,12,16`. Nízke kvadrupóly sú
nenulovo, ale malou normovanou sondou budené; `J/E` majú deklarovanú
testovaciu kolíznu väzbu `chi=100`, `G` je bezkolízna. Vyššie multipóly
použijú **nenulový radiačne-asymptotický closure**

```text
X_L,x = -(L-2)q X_L + L/(2L+1) s2 X_(L-1) - (L+1) X_L,
```

plus kolízne tlmenie pre `J/E`. To je vedome iné od zakázaného `X_(L+1)=0`
closure. V skorom radiačnom limite používa `Hconf*eta≈1`; FULL musí neskôr
použiť autoritatívny backend closure a reálnu opacity.

## Kritériá

- každý `lmax` dosiahne endpoint, konečný stav a RHS sú konečné, cap
  `1e6`, `RHS_CAP=100000`, interný limit `45 s`, externý `55 s`;
- normovaný rozdiel nízkych momentov `lmax 12→16 <=1e-5`;
- rozdiel `8→12 <=5e-4` **alebo** aspoň štvornásobné zlepšenie oproti
  `12→16`;
- pomer posledného multipólu ku kvadrupólu `<=1e-6` pre každú rodinu;
- zmrazený SHA-256 K4 scriptu 213 musí sedieť.

PASS je iba `SCREEN-S3 PASS`, skóre 0. Neúspech konvergencie je
`STOP_G8_CLOSURE_CONVERGENCE_REVIEW`, nie fyzikálna smrť K7; technický
timeout/cap/import je REVIEW. S3 netestuje kompletný 32/44/56-stavový
Einstein-Boltzmann systém, rekombináciu ani CMB.
