# Changelog neinvazívneho upratania adresárov

## ORG-E20260716-001

**Zmena:** zavedený kanonický layout, register vlastníctva base modulov a
hashové zmrazenie existujúcich neversionovaných modulov.  
**Starý stav:** `scripts/baseScripts/00_README.md` a register tvrdili, že
žiadny modul neexistuje; neskôr už vznikli tri rodiny modulov.  
**Nový stav:** moduly sú viditeľné, vlastnené konkrétnou route, hashované a
označené presným rozsahom.  
**Dôvod:** predísť kopírovaniu vzorcov a umožniť nájsť všetky behy dotknuté
jednou opravou.  
**Fyzikálny dosah:** žiadny nový PASS ani STOP.

## ORG-E20260716-002

**Zmena:** historické skripty sa nepresúvajú; koľaje dostávajú odkazy a
manifesty.  
**Dôvod:** inventár z 2026-07-15 našiel 468 väzieb, ktoré by fyzický presun
mohol rozbiť.  
**Budúca podmienka presunu:** Git baseline, úplná path/SHA mapa, oprava
odkazov po závislostných komponentoch a samostatné regresné brány.

## ORG-E20260716-003

**Zmena:** vytvorené samostatné uzly A2-K1 až K9, K11, K12 a oddelená route
A1-K2/A2-K10; A2-K4/P5 dostala BASE/RUNNERS/RESULTS/AUDIT_THREADS registre.  
**Kontrola:** všetkých 11 A1-K1/A2 uzlov má track, manifest, base register a
HISTORY; base hashe `11/11`, nezhody `0`.  
**Audit:** `Audit/DIRECTORY_AND_BASESCRIPT_REORGANIZATION_AUDIT_2026-07-16.md`.
