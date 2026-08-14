# A1K1 -> A2K4 — entalpicky vážený energy-frame

**Stav:** `LIVE_ACTIVE / P5 / CONTRACT_RC_FROZEN_AUDIT_PENDING`  
**Fyzikálna hĺbka:** `60/100`  
**Historická technická hĺbka K7:** `66.5/100` — neprenosná na K4  
**Aktívna formulácia:** `SUBTRACKS/P5`

A2-K4 smeruje prenos energie a hybnosti podľa spoločnej entalpicky váženej
rýchlosti tmavého sektora. Plná implementácia povinne obsahuje samostatné
`U_c`, `U_f` a `U_d=(1-beta)U_c+beta U_f`.

Historická K7 reduced-RHS implementácia nemala dynamické `U_c`. Jej G0-G7
výsledky zostávajú auditovateľnou históriou presne tejto redukovanej sústavy,
ale K7 sa nepoužíva pre G8/G9 a jej implementačný terminál nie je fyzikálny
STOP A2-K4.

Aktívny P5 už uzavrel P5.1, štrukturálnu P5.2, C2 `10/10` coverage a C3
`45/45` logical coverage. Otvorený je fyzikálny S-M/D03 witness. Autor zvolil
carrier `Z_rec=[B_rec,Sigma_prep]_rel`; exact contract 293 je zmrazený a čaká
na nezávislý matematicko-logický audit. Po jeho PASS nasledujú analytické
D1-D2, nie Python ani ďalšia source operácia.

Q1R1-V3 je uzavretá pomocná source línia s reusable checkpointom. Jej
historické technické chyby zostávajú v histórii, ale nový fyzikálny atóm má
aktívny counter `0/10`.

- hrubý plán: `00_WORK_PLAN.md`;
- detail P5: `SUBTRACKS/P5/00_WORK_PLAN.md`;
- historická K7: `SUBTRACKS/C7_7c/K7/00_WORK_PLAN.md`;
- história: `HISTORY/00_EVENT_LEDGER.md`.
