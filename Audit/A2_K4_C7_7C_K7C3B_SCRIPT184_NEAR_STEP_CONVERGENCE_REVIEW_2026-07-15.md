# A2-K4 / C7.7c / K7c.3b — REVIEW skriptu 184 tesne nad krokovým prahom

Dátum: 2026-07-15  
Stav: **REVIEW, nie PASS a nie fyzikálna smrť**

Pevné RK4 mriežky 100/200 krokov dosiahli koniec za 9.11 s a 1 203 RHS volaní. Všetky brány okrem jednej prešli:

- max normalizovaný coarse/fine endpoint rozdiel: `1.44327e-6`;
- preregistrovaný prah: `<1e-6`;
- dominantná zložka: `M = 1.44327e-6`;
- `eta = 3.67e-7`, `sigma_fs = 4.04e-8`, ostatné menšie;
- density constraint: `1.37e-22`;
- momentum constraint: `4.32e-17`;
- maximum normalizovaného stavu: `1.0`;
- netriviálna zmena trajektórie: `0.01188`.

Prah sa neuvoľňuje. Výsledok ukazuje, že adaptívny 200-tisícový zásek nebol fyzikálnou explóziou. Na rozhodnutie o asymptotickej RK4 konvergencii vzniká K7c.3c s ďalším faktorom 2 v kroku.

