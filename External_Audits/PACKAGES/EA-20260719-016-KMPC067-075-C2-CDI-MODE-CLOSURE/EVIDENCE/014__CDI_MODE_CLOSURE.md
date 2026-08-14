# KMPC-067–075 — C2 CDI mode closure

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Autoritatívny stav:** `CDI MODE PASS / C2 4/10 PASS / K4 LIVE 60/100`  

CDI/k=.005 je uzavretý na accepted support `[0,7]` voči auditu `[0,9]`
rawom KMPC-073 SHA
`B7B2B7231E20D90D7EA71F1934B795296B7B0C2772148988C0FCFB2CF96E8498`.
CDI/k=.15 je uzavretý na `[0,5]` voči `[0,7]` rawom KMPC-075 SHA
`19F5F0B38CFE62C6E2ECA277EE5F959D866967027C5AF721CF4B2E1A30B999B9`.

KMPC-075 zachoval presne tú istú auditnú 104×104 maticu a constant ako
KMPC-074. Tri korekcie znížili max relatívne driver rezíduum z
`3.8441418852221534e-10` na `1.1149921347627513e-16`; correction relative
L2 bol už v prvom kroku iba `3.1355859878288963e-15`. Nejde o úpravu prahu
ani rovníc.

Technické PF-081–084 a checkpoint KMPC-070 ostávajú v auditnej stope, ale
nemajú fyzikálny hlas. Skóre K4 ostáva `60/100` a P5 `3.5/6`, pretože uzavretie
jedného z piatich C2 módov nie je uzavretím celej P5.3 brány. C2 postupuje z
`2/10` na `4/10`; ďalší predregistrovateľný atóm je BI/k=.005
`[0,5]→[0,7]`, M1 depth 7.
