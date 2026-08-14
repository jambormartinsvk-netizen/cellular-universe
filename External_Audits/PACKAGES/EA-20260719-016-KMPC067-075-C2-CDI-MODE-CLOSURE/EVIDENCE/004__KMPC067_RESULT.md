# KMPC-067 — C2 CDI/k=.005 nominal: výsledok

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `TECHNICAL_COMPLETE / REVIEW_SUPPORT_07_09_REQUIRED`  

## Autoritatívny technický záznam

- raw: `RUN_KMPC_067_P5_3G7_C2_CDI_K0p005_NOMINAL.json`;
- SHA-256: `DC11201E7301831153F4D3D5450A95FC1D5F311E5EE3E9176BDE6E471F657F8F`;
- execution: `TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT`;
- candidate, nie verdikt:
  `REVIEW_C2_CDI_K0p005_SUPPORT_07_09_REQUIRED`.

M1, core, common a background guard prešli. Common maximum bolo
`1.0722718963875644e-14` (F0) a `1.6074492959453351e-12` (M3), oba pod
prahovou hodnotou `1e-8`. M1 driver scaled bol `8.508441758421102e-14`
a holdout scaled `5.3625723820239704e-14`.

Tail F0 prešiel; jeho maximum pri `z=.01` bolo
`8.516111251905205e-8`. Tail M3 neprešiel iba na `z=.01`: stav
`sigma_fs` dosiahol `1.4946248807986404e-5` oproti zmrazenému prahu
`1e-6`. Pri `z=1e-4` M3 prešiel. Absolútna tail obálka problematického
`sigma_fs` bola `6.690481436922586e-14`; rozhodujúca je však vopred
zmrazená relatívna vetva, preto ju nemožno po výsledku zameniť za absolútnu.

## Význam a ďalší krok

Výsledok nevyvracia CDI mód a nemení skóre ani verdikt. Izoluje jednu
support otázku: či sa príspevok, ktorý je pri `[0,5]→[0,7]` ešte priveľký,
uzavrie pri predregistrovanom rozšírení `[0,7]→[0,9]`. Nasleduje iba tento
successor s M1 depth 9; žiadna korekcia prahu, vstupu alebo rovníc nie je
povolená.

Auditný balík sa podľa protokolu R4 ešte nevytvára. CDI mód nie je uzavretý
a nevznikol STOP ani technický blocker.
