# K7c P3a-A — predbehové očakávania skriptu 201

Dátum: 2026-07-15  
Stabilné ID: `SCI-A2K4-C7G5-K7C-P3A-ZERO-IDENTITY`  
Typ: presná algebra a 80-dps kontrola bez ODE  
Score effect: `NONE`

## Ľudský význam

P2 ukázalo, že chyba nevzniká pri finálnom sčítaní deviatich členov, ale pri
zostavení dvoch koeficientov z čísel, ktoré sa majú presne vyrušiť. Skript
201 má overiť iba to, či ich nulovosť skutočne vyplýva z už registrovaných
definícií backgroundu. Neopravuje evolúciu a nepočíta CMB ani S8.

## Zmrazené vstupy

- skript 199 SHA-256:
  `911F7DDBDC6B41C019CD041FC024A2B8FAF9CF2A27A1F35686ECB6649BAD8DF9`;
- P2 raw JSON SHA-256:
  `C268A63CE34888744E48A8BD784651C75B243B25705E74C301299DA69499FA5C`;
- očakávaný P2 verdikt:
  `STOP_P2_SIMPLE_FSUM_EXPLANATION_IN_THIS_SCOPE`;
- plochy: `x=-25,-24.875,-24.75,-23`.

## PASS brány

1. exaktná racionálna redukcia `Omega_b/Omega_gamma=4R/3` je nulová;
2. exaktná redukcia `W_gamma=2 Omega_gamma (1+R)` je nulová;
3. po týchto substitúciách sú presne nulové koeficienty
   `c_U=3 Omega_b/2-W_gamma R/(1+R)` a
   `c_delta=W_gamma/[4(1+R)]-Omega_gamma/2`;
4. na každej zmrazenej ploche sú všetky backgroundové hodnoty konečné;
5. 80-dps normalizované rezíduum každej zo štyroch identít je
   `<=1e-70`;
6. vstupné hashe, P2 verdikt, ID testu a množina plôch sú presné.

Nenulový float64 zvyšok sa exportuje ako dôkaz cancellation, ale nie je
podmienkou PASS. Skript nesmie importovať ani spustiť ODE a nesmie prepísať
existujúci výstup.

## Rozhodovanie

- všetky brány PASS: `PASS_P3A_EXACT_ZERO_IDENTITY`; smie sa pripraviť
  oddelená P3a-B evolúcia;
- ktorákoľvek presná alebo 80-dps brána FAIL: algebraická P3a vetva STOP;
- provenance chyba, formálna chyba alebo timeout: REVIEW, bez fyzikálneho
  rozsudku.

Interný limit je 5 s, externý limit 10 s. Očakávaný runtime je pod 1 s.
Výstup: `Audit/A2_K4_K7C_P3A_ZERO_IDENTITY_RAW_2026-07-15.json`.
