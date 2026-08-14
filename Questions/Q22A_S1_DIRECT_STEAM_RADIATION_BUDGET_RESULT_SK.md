# Q22a-S1 — výsledok sita priamej pary z celkového radiačného rozpočtu

**Verdikt:** `K2_STOP_WITHIN_FROZEN_A1; K3_DIRECT_STEAM_FRACTION_BOUNDED`  
**Typ dôkazu:** `aproximácia / konzervatívne backgroundové sito; bez skóre`  
**Skript a výsledky:** `scripts/258_script_Q22A_S1_direct_steam_radiation_budget_screen.py`,
`RUN_Q22A_004...json` a konvergenčný `RUN_Q22A_005...json` v
`scripts/results/q22a/`.

## Výsledok

Pri zamrznutých A1 vstupoch je dnes

```text
X_r = 9.55038e-5,
q = lambda X_f/E = 9.72307e-2,
X_r/q = 9.82239e-4.
```

Pre čistý priamy kanál K2 (`f_R=1`) sa pri spätnom behu stane `X_r` zápornou
už pri prvom kroku `Delta ln a≈-0.001`. Preto K2 nemôže kontinuálne bežať s
registrovanou intenzitou do voľnej relativistickej zložky a zároveň zachovať
dnešný A1 radiačný rozpočet.

Najväčší podiel, ktorý zachová iba **kladnosť celého** `X_r` až po
rekombináciu, je

```text
f_R,max = 0.0043830983  (0.4383 %).
```

Polkrokový beh (`0.0005` namiesto `0.001`) dal identickú hranicu v zobrazenej
presnosti; K1 zostala pozitívna a K2 opäť zlyhala. Numerický rozsudok je teda
stabilný.

## Dôležité obmedzenie

Táto hranica je veľmi **zhovievavá**, nie plný observačný limit. Dovoľuje,
aby sa spätne znižovala aj hustota štandardných fotónov a neutrín, hoci CMB
ich samostatne vyžaduje. Preto sa nesmie čítať ako povolenie `0.4383 %`
priamej pary. Je to len horný strop z pozitívnosti.

Nasledujúce sito S2 preto oddelí štandardnú radiáciu od registrovanej parnej
rezervy `Delta N_eff=0.0535`. Až jeho výsledok bude relevantný pre priamy
parný produkt K2/K3; plný BBN/CMB likelihood ostáva neskoršia brána.
