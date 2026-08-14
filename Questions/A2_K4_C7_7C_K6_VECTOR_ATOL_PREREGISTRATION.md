# A2-K4 / C7.7c-K6 — predregistrácia fyzikálneho stavu s vektorovým atol

**Dátum:** 2026-07-14  
**Stav:** A2-K4 živá na `66.5/100`; numerické podkoľaje C7.7c-K4 a C7.7c-K5 mŕtve.  
**Cieľ:** zachovať komponentovú presnosť analytickej obálky bez transformácie fyzikálneho stavového vektora.

## 1. Základ a odlišnosť

- K4 integrovala normalizovaný stav `w=y/S_env`; zomrela na extrémne nenormálny škálovaný Jacobian.
- K5 pridala úplné diagonálne vyváženie; zomrela na timeout a zmenu komponentového chybového rozpočtu faktorom `D`.
- K6 integruje priamo pôvodný fyzikálny stav `y` a používa analytickú obálku iba v tolerancii solvera.

K6 nie je návratom ku K1: K1 mala jedno spoločné absolútne `atol`, ktoré ignorovalo malé komponenty. K6 má pevný vektor

`atol_i = atol_factor × max(|y_i,start|, |y_i,series(x=-18)|, 10^-300)`,

kde `atol_factor=10^-12`.

## 2. Jediná povolená zmena

Vo fyzikálnej integrácii skriptu 139 sa skalárne `atol` nahradí vyššie definovaným 13-zložkovým vektorom. Stav, RHS a všetky fyzikálne operácie ostávajú v pôvodných jednotkách.

Nesmie sa pridať:

- transformácia stavového vektora;
- maticové vyváženie;
- zmena solvera, `rtol`, `max_step`, rovníc alebo počiatočných podmienok;
- adaptívna zmena tolerančného vektora počas trajektórie.

## 3. Pevné nastavenie

- DOP853;
- `rtol=10^-10`;
- `atol_factor=10^-12`;
- `max_step=0.02`;
- segment najviac jeden e-fold;
- `L5=0`, 13 komponentov;
- safety cap `10^12` vo fyzikálnych premenných;
- prvé behy s vnútorným/vonkajším limitom najviac `8/10 s`.

## 4. Brány

### K6a — NID/deep prvý segment

PASS vyžaduje dokončenie `-25→-24`, konečný stav a RHS konečné, neprekročený safety cap a úplný zápis segmentových metrík.

### K6b — ostatné prvé segmenty

Po PASS K6a: NIV/deep, NID/shallow, NIV/shallow. Každý samostatne limitovaný.

### K6c — úplná evolúcia

Po PASS všetkých štyroch prvých segmentov: úplná segmentovaná evolúcia po `x=-18`.

### K6d — komponentový audit aktivity

Aktivita sa hodnotí iba podľa vopred stanovených prahov. PASS K6a–K6c ešte neudeľuje body.

## 5. Skóre a rozsudky

- K4 zostáva `66.5/100` počas K6a–K6c.
- `+0.2` sa udelí iba za úplný PASS K6d.
- Timeout K6a zabíja K6, nie automaticky fyzikálnu A2-K4.
- Pri neúspechu sa výsledok a skript zachovajú; ďalšia numerická zmena vyžaduje nový audit príčiny a novú podkoľaj.
