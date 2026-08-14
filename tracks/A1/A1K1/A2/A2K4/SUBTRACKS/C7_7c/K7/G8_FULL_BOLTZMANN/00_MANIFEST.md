# C7-G8 — manifest

**Stav:** `SCREEN S0–S3 PASS / FULL K4 ADAPTER PROHIBITED: background + missing U_c`  
**Support pred G8:** `90/100`  
**Autoritatívna predregistrácia:** `00_PREREGISTRATION.md`

## Adresáre

- `ARTIFACTS/` — immutable JSON, SHA-256 manifesty a finálne výstupy;
- `HISTORY/` — nefunkčné alebo neskôr obmedzené verzie s dôvodom;
- `REVIEWS/` — externé audity a odpovede na audit;
- `scripts/baseScripts/a2_k4_g8/` — spoločný operátor volaný konfiguráciami.

## Vstupné autority

- `scripts/73_script_A2_K4_3b_hierarchy_and_regular_mode_taxonomy_audit.py`;
- `scripts/74_script_A2_K4_3b_CAMB_recombination_interface_reference.py`;
- `scripts/76_script_A2_K4_3b_exact_CAMB_hierarchy_coefficients_alias_fixed.py`;
- `scripts/213_script_A2_K4_C7_7c_K7d_integrated_G4_G6_G7_runner.py`;
- `Audit/A2_K4_C7_7C_K7D_G4_G6_G7_FINAL_AUDIT_2026-07-15.md`.

## Výsledky

| Run | Rozsah | Stav | Bodový účinok |
|---|---|---|---:|
| RUN-000 | exact CAMB coefficient sanity check | PASS 22/22 | 0 |
| RUN-001 | S0+S1, prvá implementácia 221 | TECHNICAL STOP PF-034 (39/40; chybná substitúcia) | 0 |
| RUN-002 | S0+S1, opravný wrapper 233 | PASS 40/40 exact identities | 0 |
| RUN-003 | S2, direct/TCA K4-background overlap | PASS; overlap `7.06e-11`, slip `4.89e-9` | 0 |
| RUN-004 | S3, `lmax=8/12/16` hierarchy-tail sweep | PASS; `12→16=5.29e-16`; nonzero closure | 0 |

RUN-001 je uložený immutable spolu s dôvodom v `HISTORY/`; nikdy sa
neprepisuje. Autoritatívnym S0+S1 výsledkom je RUN-002 a jeho audit.
S0–S3 sú uzavreté. Zdrojový CLASS/HyRec reference backend už prešiel, ale
K4 adapter ešte nebežal; audit je v
`FULL_BACKEND/ARTIFACTS/RUN_FULL_000_001_CLASS_REFERENCE_BACKEND_AUDIT.md`.
Žiadny SCREEN ani štandardný reference beh sa nesmie ticho povýšiť na G8
PASS.

RUN-FULL-002 následne preukázal k‑závislosť surového palivového background
člena. Adapter je preto blokovaný až do odvodenia globálnej normalizácie;
pozri `FULL_BACKEND/03_K4_BACKGROUND_UNIVERSALITY_GATE.md`.

## Spresnenie blockeru po audite `K_MPC=0.05` (2026-07-15)

Globálna skorá normalizácia už má parameter-bookkeeping riešenie:
`A_f=7809.27010196` je určený zo zmrazeného A1 closure bez nového fitu.
Následný test však ukázal, že normalizovaný **skrátený K7 rad** prejde do
`D<0` pri `a≈0.70896`; nesmie sa preto použiť ako celý CLASS background.
G8 ostáva blokované bez zmeny skóre. Prípustný nástupca potrebuje novú
deriváciu K7/G8 porúch z plného kladného `D_A1(a)`, vrátane constraintov a
nulového limitu. Záznam: `Independent_Audits/K_MPC_0_05/08_P3_FULL_BACKGROUND_VS_TRUNCATED_K7_RESULT_SK.md`.

P4c následne zistila, že súčasná K7 13-zložková báza neobsahuje dynamické
`U_c` ani CDM hybnosť v `M`; nemôže teda reprezentovať
`Q^mu=Gamma rho_f u_d^mu` pri nenulovej relatívnej rýchlosti. SCREEN
výsledky ostávajú historicky platné pre redukovanú RHS, ale FULL G8 sa na nej
nesmie spustiť. Presný dôvod a povinný stavový nástupca:
`Independent_Audits/K_MPC_0_05/13_P4C_K7_MISSING_UC_EXACT_BACKGROUND_STOP_SK.md`.
