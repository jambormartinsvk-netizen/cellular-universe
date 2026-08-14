# A2-K4 / C7.7c / K7c.3 — predregistrácia krátkej projektovanej ODE NID/deep

Dátum: 2026-07-15  
Vstup: K7c.1 a K7c.2 PASS  
Rozsah: prvý evolučný smoke-test, bez bodov

## Trajektória

- mód/povrch: iba `NID/deep`;
- začiatok `x=-25.0`, koniec `x=-24.75`;
- checkpointy: začiatok, polovica a koniec;
- projektovaný stav má presne 13 zložiek z K7c.1;
- počiatočný seed sa vezme zo skriptu 178, vrátane autoritatívnych HP `D,M`.

## Rovnice

Použije sa explicitný projektovaný RHS zauditovaný v K7a/K7b:

```text
[h, eta, delta_gamma, D, delta_b, delta_c,
 U_gamma, M, sigma_fs, L3_fs, L4_fs, delta_f, U_f]
```

`delta_fs,U_fs` sa rekonštruujú algebraicky iba v RHS. Neintegrujú sa ako ďalšie premenné. `L5=0` zostáva deklarovaným ohraničeným closure; plná hierarchia sa v tomto kroku netvrdí.

## Numerika

- solver `DOP853`;
- `rtol=1e-10`, normalizovaný `atol=1e-12`;
- `max_step=0.02`;
- integruje sa `w_i=z_i/S_i`;
- `S_i=max(abs(seed_NID_deep_i), abs(seed_NID_shallow_i), 1e-300)`;
- táto envelope škála sa používa iba pre error control integrácie, nie pre Jacobián/SVD alebo lokálnu fyzikálnu diagnostiku;
- najviac 200 000 RHS volaní, normalizovaný safety cap `1e8`;
- vnútorný limit najviac 25 s a vonkajší limit najviac 30 s.

## Brány

1. zdrojový skript 178 prejde a vráti presných 13 mien;
2. solver skončí úspešne a dosiahne `x=-24.75`;
3. všetky tri checkpointy, stavy a RHS sú konečné;
4. safety cap a limit RHS volaní sa neprekročia;
5. stav sa netriviálne zmení: `max(abs(w_final-w_start)) > 1e-12`;
6. na checkpointoch zostanú `Omega_fs>0`, rekonštruované species konečné a škálované density/momentum constraint rezíduá `<5e-12`;
7. metrické identity `h'=3D+2s^2 eta`, `eta'=M` sú v implementácii kontrolované bez duplicitného pridania constraintu ako dynamickej rovnice.

## Rozhodovanie

- PASS povoľuje rovnaký krátky test NID/shallow, potom NIV.
- Timeout, príliš veľa RHS volaní alebo solver failure je REVIEW a vytvára technickú podkoľaj; nezabíja K4.
- Nefinite fyzikálny stav alebo reprodukovateľné constraint zlyhanie pri konvergovanom behu môže zabiť túto K7c reprezentáciu.
- Tento smoke-test nemení skóre `66.5/100`.
