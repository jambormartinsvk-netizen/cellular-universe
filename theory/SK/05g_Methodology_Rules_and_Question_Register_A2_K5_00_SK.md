# REGISTER 05 — SK aktualizácia Q20 po A2-K5.0

**Dátum:** 2026-07-13  
**Nové pravidlá:** žiadne

## Q20 — A2-K5 rozdelená na mikrofyzikálne koľaje

- A2-K1 až A2-K4 zostávajú mŕtve M-009, M-008, M-010 a M-011.
- A2-K5/K1: kanonické skalárne palivo a konformne viazané CDM;
  `PREŽÍVA IBA K5.0 — 45/100`, rastová brána je červená.
- A2-K5/K2: explicitný časticový rozpad; čaká.
- A2-K5/K3: k-essence/prúdová akcia; čaká.
- A2-K5/K4: explicitný dynamický mediátor; čaká.
- A2-K5/K5: sieťová elastická/topologická akcia; čaká a môže vyžadovať v4.

Nezakladá sa nové Q21; ide o vnorené koľaje existujúcej Q20.

## Výsledok K5/K1

Lokálna akcia presne reprodukuje `Q=Gamma rho_f`, má správne znamienko
kanonickej kinetiky, `c_s^2=1` a kladné rekonštruované backgroundové
`m_phi^2` aj `m_eff^2`. Nulový limit `lambda->0` pri pevnom `delta>0` je
regulárny. Limit `delta->0` pri pevnom `lambda` je singulárny, pretože
`beta proportional lambda/sqrt(delta)`.

Kvázistatický test zvýšil vážený rast hmoty o `5.20–5.30 %`; diagnostická
projekcia posunula interné `S8` približne na `0.920`. Nie je to plná
CMB-normalizovaná predikcia, preto zatiaľ nevzniká M-012. Nasleduje úplný
relativistický A2-K5.1 a potom CLASS/CAMB.

## Neskorším auditom obmedzené staršie formulácie

- A1-K1 je backgroundové účtovníctvo, nie živá perturbácia.
- K5/K1 neoživuje A2-K1 M-009.
- staré ad hoc trenie nemožno citovať bez piatej sily od tej istej väzby;
- `S8=0.8745` nie je výslednou predikciou K5/K1;
- popol v K5/K1 nie je po zrode neinteragujúci: `m_c=m_c(phi)`.

Úplný audit: `Audit/A2_K5_00_canonical_scalar_action_reconstruction_and_growth_risk.md`.
