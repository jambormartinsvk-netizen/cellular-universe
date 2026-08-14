# A2-K4 / K7b P0 — predregistrácia segmentovaného rerunu po timeoute 193

Dátum: 2026-07-15  
Typ: `REGRESSION`; fyzika, tolerancie a očakávania nezmenené  
Skóre: `NONE`; A2-K4 ostáva `66.5/100`

## Dôvod segmentácie

Monolitický agregátor 193 skončil na internom limite 15 s bez úplného payloadu. Segmentácia nemení žiadny výpočet; iba zachová výstup každého prípadu pred ďalším behom. Zvýšenie child limitu nad 8 s nie je povolené.

## Povinné prípady a očakávania

| ID | Skript | Argumenty | Očakávanie |
|---|---|---|---|
| B-NID-D | 175 | NID/deep | exit 0, pôvodný PASS |
| B-NID-S | 175 | NID/shallow | exit 0, pôvodný PASS |
| C-NID-D | 192 | NID/deep, fault none | exit 0, fail-closed PASS |
| C-NID-S | 192 | NID/shallow, fault none | exit 0, fail-closed PASS |
| NIV-D | 166 | NIV/deep | exit 0, K7b.1 PASS |
| NIV-S | 166 | NIV/shallow | exit 0, K7b.1 PASS |
| F-R | 192 | NID/deep, remove reduced_rank | exit 1, REVIEW, presne tri rank checky false |
| F-F | 192 | NID/deep, remove free_count | exit 1, REVIEW, presne tri rank checky false |
| F-B | 192 | NID/deep, remove both | exit 1, REVIEW, presne tri rank checky false |

Pozitívne metriky, relatívna tolerancia `1e-4`, exact NID physics fingerprint a solver counts `30/58/58/0` ostávajú podľa pôvodnej P0 predregistrácie. Negatívny dynamics fingerprint musí byť rovnaký ako C-NID-D.

## Limity a uchovanie

- každý vedecký prípad: interný limit 8 s, externý limit 12 s;
- výsledok každého prípadu sa uloží do samostatného nového JSON súboru pred ďalším prípadom;
- pri timeoute sa daný prípad označí REVIEW a ďalšie prípady môžu pokračovať;
- offline agregátor nesmie spustiť child proces a má externý limit 5 s;
- zmena očakávania po výsledku je zakázaná bez nového dodatku.

