# P4a — C7-G5 metódová a tolerančná šírka

Stav: **PASS**  
Verdikt: `PASS_P4A_G5_METHOD_TOLERANCE_BREADTH`  
Stabilné ID: `SCI-A2K4-C7G5-K7C-P4A-METHOD-TOLERANCE`

Všetky tri prípady DOP853-medium, DOP853-tight a Radau-tight prešli
štrukturálne. Všetky štyri preregistrované rozdiely sú `<=1e-8`; namerané
maximum je `1.7526952112e-13`.

Celý C7-G5 je PASS. Strict C7-W1 support sa mení `40 -> 60/100`, WBS-1
`48 -> 60/100`, blocker zostáva `0/100`. Jemná hĺbka A2-K4 zostáva
`66.5/100` bez samostatného depth crosswalku.

Finálny audit:
`Audit/A2_K4_C7_7C_K7C_P4A_G5_METHOD_TOLERANCE_FINAL_AUDIT_2026-07-15.md`.

Najbližší krok: predregistrovať jeden integrovaný balík `C7-G4+G6+G7`.

