# P5.3a — predregistrácia auditu pôvodu plných seedov

**Koľaj:** `A1-K1 → A2-K4 → P5 → P5.3a`  
**Skript:** `scripts/242_script_KMPC_005_P5_3a_seed_provenance_audit.py`  
**Limit:** 5 s interný / 10 s vonkajší; bez importu modelu a bez ODE.

## Otázka

Sú štartové hodnoty `U_c`, `U_f` a `delta_f` v BR2 89/90 odvodeným
regulárnym exact-A1 seedem, alebo len nulovým rozšírením štandardného
`Gamma=0` CLASS seedu?

## Očakávania

Očakáva sa, že 84 deklaruje `Gamma=0`, 89/90 importujú jeho `class_seed`,
a ich `initial()` nastaví klasické zložky, zatiaľ čo nové dark-sector
komponenty ostávajú po `zeros()` nevyplnené. 86 má tie isté nuly iba v
explicitne označenom fixed-metric test field. PASS auditu znamená presnú
identifikáciu medzery, nie PASS regularity ani fyzikálnu smrť A2-K4.

## Rozhodnutie

- ak sa medzera potvrdí: P5.3 ostáva `REVIEW_BLOCKED` a nasleduje odvodenie
  Puiseux/Frobenius koeficientov pre `U_c`, `U_f`, `delta_f`;
- ak sú plné seed koeficienty už explicitne prítomné: prejsť na ich
  constraint a dvojštartový audit;
- chýbajúci zdroj alebo timeout: technický STOP mapy, nie fyziky.
