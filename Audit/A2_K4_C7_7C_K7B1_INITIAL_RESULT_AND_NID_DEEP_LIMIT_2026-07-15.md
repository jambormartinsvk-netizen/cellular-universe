# A2-K4 / C7.7c / K7b.1 — výsledok a limit NID/deep

**Dátum zápisu:** 2026-07-15  
**K7b.1 podľa preregistrovaných zmiešaných tolerancií:** PASS na štyroch povrchoch  
**Celá K7b:** **zostáva otvorená**  
**A2-K4:** živá, `66.5/100`

## Čo prešlo

- Koeficienty po exact-zero projekcii boli exportované priamo z autoritatívneho reťazca.
- NID/NIV deep/shallow boli vyhodnotené pri 80 dps.
- Rekonštrukcia stavov, `delta_fs,U_fs`, metrické `00/0i` identity a všetkých 13 RHS komponentov prešli vopred zapísanými zmiešanými toleranciami.
- NIV nemá významný problém v `D'`: relatívny rozdiel RHS a série je približne `2.84e-7` na deep a `3.85e-8` na shallow.
- Metrické seedy `D=(h_x-2s^2 eta)/3` a `M=eta_x` odstraňujú priame double odčítanie.

## Prečo K7b ešte nie je uzavretá

Na NID/deep:

- `D_metric = -2.7645e-23`;
- `D_species = -2.1952e-17`;
- condition číslo hustotnej kompenzácie je približne `2.99e22`;
- rezíduum `D'` je `1.2297e-22`, kým derivácia skrátenej série je `9.5360e-25`.

Rezíduum je absolútne malé a voči veľkým rušiacim sa druhovým členom je na úrovni `2.66e-17`, ale pre aktívnu projektovanú premennú je približne 129-krát väčšie než dostupná derivácia série.

Na NID/shallow je rovnaký activity-relative pomer približne 5.7 %. Absolútne rezíduum rastie z `1.2297e-22` na `9.0864e-22`, teda približne rovnakým faktorom ako `z`. To ukazuje na zdedenú chybu najnižšieho hmotového koeficientu z float64 least-squares solvera, nie na chybu K7a Jacobiánu.

## Obmedzenie staršieho PASS

PASS K7b.1 znamená iba, že výsledok spĺňa vopred zapísanú zmiešanú absolútnu/relatívnu toleranciu. Neznamená, že NID/deep seed má dostatočne presnú aktívnu deriváciu pre evolúciu. Activity-relative audit preto obmedzuje rozsah tvrdenia, ale spätne nemení výsledok preregistrovanej brány.

## Nové podkoľaje

1. **K7b.3a — preferovaná:** znovu vyriešiť štandardný Puiseuxov lineárny systém vo vysokej presnosti a odstrániť float64 koeficientový floor.
2. **K7b.3b:** presná constraintová projekcia nízkych koeficientov v projektovanej báze; musí mať ledger každej zmeny.
3. **K7b.3c:** používať iba shallow seed. Toto je slabšia záložná cesta a nesmie nahradiť deep/shallow kontrolu bez osobitného rozsudku.

Najprv sa preverí K7b.3a. Jacobián, jeho znamienka ani tolerancie K7b.1 sa nemenia.

## Reprodukcia

- `scripts/165_script_A2_K4_C7_7c_K7b_registered_coefficient_export.py`
- `scripts/166_script_A2_K4_C7_7c_K7b1_high_precision_coefficient_constraint_audit.py`
- `scripts/167_script_A2_K4_C7_7c_K7b2_four_surface_coefficient_floor_scaling.py`

