# P5.3g3 — predregistrácia: regulárny neutrínový `l=2` seed

**Skript:** `scripts/251_script_KMPC_014_P5_3g3_standard_neutrino_l2_series.py`  
**Limit:** 5 s interný / 10 s vonkajší; bez ODE a bez skóre.

## Čo sa počíta ľudskou rečou

Po P5.3g2 vieme, že BR2 `F1` je CAMB `qnu`. BR2 má pre neutrínový šmyk
rovnicu (v `y=k tau`)

```text
dF2/dy = (2 F1 - 3 F3)/5 + 4 dh/(15 dy) + 8 deta/(5 dy).
```

Použijú sa už deklarované štandardné lower-moment seedy AD, CDI, BI, NID,
NIV zo skriptu 84 a CDM synchronná kontinuita `dh/dy=-2 d(delta_c)/dy`.
Najprv sa určí najnižší regulárny `F2`, potom prvý indukovaný `F3` a opravený
`F2`. Žiadna ODE sa nerieši.

## Očakávanie a hranice verdictu

- **DERIVATION PASS:** pre každý mód je `F2(0)=0`, `F3` začína o najmenej
  jeden kladný rád neskôr a dosadenie kandidátu dá nulové `l=2` rezíduum
  v deklarovanej truncácii.
- **REVIEW_BLOCKED:** nekladný exponent, nenulový konštantný šmyk alebo
  algebraické rezíduum.

PASS je len kandidát s formula-provenance stopou. Stále chýba nezávislý
Einsteinov constraint, fotónový quadrupól/TCA, vyššie multipóly a dvojštart;
P5.4 a G8 sa tým neotvoria.
