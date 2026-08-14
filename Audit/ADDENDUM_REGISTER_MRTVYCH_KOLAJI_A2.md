# Dodatok registra mŕtvych koľají — A2

**Dátum:** 2026-07-13  
**Nadväzuje na:** `Audit/REGISTER_MRTVYCH_KOLAJI_A_DOKAZOV_v3.18.md`

## M-008 — A2-K2, striktne barotropické palivo

- **Stav:** `MŔTVA — ARCHIVOVANÁ`.
- **Hypotéza:** `p_f=w_f rho_f` a fyzikálna pokojová zvuková rýchlosť `c_s,f^2=dp/d rho=w_f=-0.97703`.
- **Dôvod smrti:** záporné `c_s,f^2` mení krátkovlnnú vlnovú rovnicu na exponenciálnu a vytvára gradientovú nestabilitu s mierou úmernou `k`.
- **Skript:** `scripts/21_script_A2_barotropic_fuel_gradient_instability.py`.
- **Výstup:** `scripts/README_AUDIT_SCRIPT_21.md`.
- **Úplný audit:** `Audit/A2_K2_MRTVA_barotropicke_palivo_gradientova_nestabilita.md`.
- **Čo nezomrelo:** A2-K1 s efektívnym `c_s,f^2=1` ani iná odvodená mikrofyzika s nezáporným gradientovým členom.
- **Podmienka novej koľaje:** nová mikrofyzická akcia alebo uzávera, ktorá mení hlavný gradientový člen a preukáže `c_s,f^2>=0`; nie iba nový grid.

