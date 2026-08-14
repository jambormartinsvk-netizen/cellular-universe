# A2-K4.2 — dôkazový manifest SHA-256

**Dátum:** 2026-07-14  
**Algoritmus:** SHA-256  
**Rozsudok snapshotu:** `PREŽÍVA K4.2 — 59/100`  
**Ďalšia brána:** K4.3

Tento manifest fixuje presný stav analytických/numerických skriptov, výstupu,
auditu, metodických dodatkov a kanonických stavových dokumentov po uzavretí
K4.2. Historické manifesty K4.1 a M-011 sa neprepisujú; zostávajú snapshotmi
svojho času.

## Kontrolné súčty

```text
a81ee0f2e54153b6e021be7b397b980f0ae78d878b3f92b1a23c2b874138523b  Questions\A2_K4_2_PROBLEM_BRANY_A_KILL_KRITERIA.md
7471480db0eca5ea3c632f08acdb8ef3716ff1f0a1081a52bf3e4ff2ee107820  scripts\69_script_A2_K4_2_high_k_principal_symbol.py
19d6ab7482d1090f254eaee60b639eb103463d53190bf413b8957173dc99bb78  scripts\70_script_A2_K4_2_subhorizon_regular_basis.py
ac332c94dbbd122d3934ad98c6ec23a531334f60544afe8cf3b376af723bf1ca  scripts\71_script_A2_K4_2_q300_convergence_gates.py
33d9938c441f9e75c15b1382c684830ee5070a04ad60477c4912b00128511572  scripts\OUTPUT_A2_K4_2_69_71.md
2e98fbc6c4742e9f91e2537dc9edd8d84f457527c5ad134cb7867933bf5c8133  Audit\A2_K4_2_HIGH_K_SUBHORIZONTOVY_AUDIT_A_ROZSUDOK.md
5610db920b439eb8fec7f11c603b3f62b5bb06c01338ece7a50799204bc7d6ba  theory\SK\05zz_Methodology_Rules_and_Question_Register_A2_K4_2_SK.md
b39b12f5f0cf2eaf91f5efca012e2348638102a3864506ac31fcce2afcc924c2  theory\EN\05zz_Methodology_Rules_and_Question_Register_A2_K4_2_EN.md
155c5bd8daec440f378878f560872f731667890313028b8d04a773b7178c891b  Questions\00_READ_FIRST_A2_Q20_CURRENT_STATE.md
7bdaffa52e4e80d5f30ee28c65b49a59799659e35cd01baeceef2ebe581644e3  Questions\A1_K1_A2_AUDITNY_PROGRAM_A_STOPPING_KRITERIUM.md
2168aab54dd4e6443e9ca7d656aae1b4c76961dba834a4007bafc0edb004a6d3  Questions\00_AKCNY_PLAN_v3.18_AKTUALNY_2026-07-13.md
87e9edf086c48646a1e7a22599af57ee740bc0106f07b11c25bc2e88a0ae04b1  Audit\A2_KATALOG_STAV_SKORE_A_DOVOD_SMRTI_K1_AZ_K11.md
e9062ce8218640fe81d4a67297e700de79cc2724a4ead14144eaf24a4badbbdf  Audit\A2_KATALOG_KOLAJI_K1_AZ_K10_ZROZUMITELNY_SUMAR.md
4095478bda359c296f56527e0a5b34dff1018f3e4ddc26ab8910d5b4c282da0c  Audit\A2_K4_1_UPLNA_REGULARNA_CONSTRAINT_BAZA_A_ROZSUDOK.md
```

## Reprodukčné príkazy a limity

```text
python scripts\69_script_A2_K4_2_high_k_principal_symbol.py --max-runtime-seconds 10
# externý limit 15 s

python scripts\70_script_A2_K4_2_subhorizon_regular_basis.py --q Q --lambda LAMBDA --x-start X --background-step STEP --rtol RTOL --atol ATOL --samples 1601 --max-runtime-seconds 50
# externý limit 60 s; Q in {30,300,1000}; LAMBDA in {0.15,0}

python scripts\71_script_A2_K4_2_q300_convergence_gates.py --max-runtime-seconds 50
# externý limit 60 s
```

Všetky fyzikálne behy skončili pred limitom. Syntaktická kontrola skriptov
69–71 prešla. `git diff --check` nebolo možné použiť, pretože `D:\Teoria`
v čase snapshotu ešte nebolo Git pracovným stromom; nejde o fyzikálnu ani
numerickú bránu. Napojenie na plánovaný GitHub repozitár zostáva samostatnou
organizačnou úlohou pred Zenodo vydaním.

