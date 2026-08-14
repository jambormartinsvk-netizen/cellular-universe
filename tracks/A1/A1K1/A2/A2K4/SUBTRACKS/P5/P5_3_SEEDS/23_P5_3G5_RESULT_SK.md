# A2-K4/P5.3g5 — výsledok: skorá opacity a nezávisle zostavený zdroj constraintov

**Dátum:** 2026-07-16  
**Verdikt:** `FORMULA_PASS_P5_3G5_EARLY_OPACITY_AND_INDEPENDENT_LEDGER_SCOPE`  
**Fyzikálna hĺbka A2-K4:** nezmenená, `60/100`.  
**Skóre:** bez zmeny.

## Čo prešlo

Pre plne ionizovaný skorý limit platí zo štandardnej Thomsonovej fyziky

```text
dot(kappa) = n_e0 sigma_T / a^2,
tau_c = a^2/(n_e0 sigma_T),
Hconf tau_c = H_r a/(n_e0 sigma_T),
k tau_c = k a^2/(n_e0 sigma_T).
```

Oba tesnoväzbové parametre preto pri `a -> 0` presne miznú. Tento limit
nepridáva voľný K4 parameter a je kompatibilný s presným, od Fourierovho
`k` nezávislým A1 backgroundom.

Oddelene zostavený zdroj pre synchronous `0i` constraint obsahuje

```text
Xc Uc + delta Xf Uf + Xb Ub
+ 4/3 (Xgamma Ugamma + Xnu Unu + Xsteam Usteam).
```

Teda sa nedá legálne zredukovať na starý K7 zdroj bez `U_c`; také vynechanie
by odstránilo nenulový povinný člen.

## Čo neprešlo a prečo to nie je smrť

Tento test nemeral dynamické Einsteinove rezíduum konkrétneho riešenia.
Tiež neodvodil úplnú ionizačnú históriu `x_e(a)` cez rekombináciu: tá vyžaduje
štandardný rekombinačný backend na exact-A1 backgrounde. Preto výsledok
neotvára P5.4 ani G8 a nie je testom CMB.

## Reprodukcia

- predregistrácia: `Questions/A2_K4_P5_3G5_EARLY_OPACITY_AND_INDEPENDENT_LEDGER_PREREGISTRATION_2026-07-16.md`;
- runner: `scripts/256_script_KMPC_019_P5_3g5_early_opacity_and_einstein_ledger.py`;
- zdieľaná algebra: `scripts/baseScripts/p5_general_synchronous/early_opacity_ledger.py`;
- immutable výstup: `scripts/results/k_mpc_005/RUN_KMPC_019_P5_3G5_EARLY_OPACITY_AND_EINSTEIN_LEDGER.json`.

Všetkých 12 kontrol prešlo za `0.187 s` pri vnútornom limite 5 s. SHA-256
viaže audit na P4 exact-background dokument a na zdrojový synchronous ledger.

## Ďalší krok

`P5.3g6` musí zložiť úplný fotónový + neutrínový + tmavosektorový regulárny
seed v tej istej báze a priamo dosadiť ho do `00`, `0i`, trace a traceless
Einsteinových rovníc na dvoch skorých plochách. Až taký reziduálny test môže
rozhodnúť, či sa otvorí P5.4.
