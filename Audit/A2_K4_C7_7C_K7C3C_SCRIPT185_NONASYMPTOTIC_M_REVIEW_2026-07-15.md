# A2-K4 / C7.7c / K7c.3c — REVIEW neasymptotickej M konvergencie

Dátum: 2026-07-15  
Stav: **REVIEW; ďalšie slepé zjemňovanie zastavené**

Mriežky 200/400 krokov dosiahli koniec za 6.56 s a 2 403 RHS volaní, ale endpoint rozdiel sa zhoršil:

- predchádzajúci 100/200 rozdiel: `1.44327e-6`;
- nový 200/400 rozdiel: `3.93124e-6`;
- pomer predchádzajúci/nový: `0.367`, nie očakávaných približne 16;
- dominantná zložka: `M = 3.93124e-6` v normalizovanej škále;
- density constraint: `1.37e-22`;
- momentum constraint: `4.32e-17`;
- safety maximum: `1.0`.

Toto nie je fyzikálna explózia ani constraint failure. Je to neasymptotické numerické správanie sústredené v kompenzovanom `M` smere. Ďalší krok nesmie iba zmenšiť krok alebo zvýšiť limit. Musí rozložiť `M'` na jednotlivé členy a porovnať bežný double súčet, kompenzovaný `math.fsum` a 80-dps súčet pri rovnakom stave.

