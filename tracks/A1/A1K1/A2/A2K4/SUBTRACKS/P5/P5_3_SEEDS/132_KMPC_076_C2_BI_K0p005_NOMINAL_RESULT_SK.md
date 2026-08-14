# KMPC-076 — C2 BI/k=.005 nominal: výsledok

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `IMMUTABLE / REVIEW_C2_BI_K0p005_SUPPORT_07_09_REQUIRED`

Raw
`RUN_KMPC_076_P5_3G7_C2_BI_K0p005_NOMINAL.json` má SHA-256
`B053B523C00032360F8FAFC47189C577B9B3D426778D881A2BD110DE3C4FCA00`.
Compile, help, behaviorálny smoke aj official beh skončili exit code 0.

| Brána | Výsledok |
|---|---|
| M1 depth 7 | PASS |
| core a S-C0 | PASS |
| common `0…5` | PASS; maximum `5.868385058267079e-13 < 1e-8` |
| F0 tail `6,7` | PASS; `delta_f(z=.01)=8.516111250963451e-8` |
| M3 tail `6,7` | REVIEW; `sigma_fs(z=.01)=1.4946243588293508e-5 > 1e-6` |
| background | PASS |

Fail je iba tail-only vetva zmrazeného stromu. Nejde o fyzikálny STOP,
zmenu rovníc ani dôkaz nestability. Autoritatívny nástupca musí porovnať
accepted `[0,7]` s audit `[0,9]` pri M1 depth 9 a nezmenených prahoch.

CDI história KMPC-068/069 ukázala, že dve hlboké solve v jednom procese
prekročia limit 4.8 s. Preto sa nástupca od začiatku predregistruje ako
dvojfázový hashovaný checkpoint: prvá fáza vypočíta `[0,7]` bez fyzikálneho
verdiktu, druhá z neho audituje `[0,9]`. Nový všeobecný wrapper smie meniť
iba identitu a segmentáciu; rovnice, prahy a support ostávajú vlastníctvom
zmrazeného C2 jadra.
