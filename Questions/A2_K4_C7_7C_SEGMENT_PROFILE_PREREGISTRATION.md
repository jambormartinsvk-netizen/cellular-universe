# A2-K4 / C7.7c — predregistrácia segmentového profilu

**Dátum:** 2026-07-14  
**Stav pri zápise:** A2-K4 je živá, technicky pozastavená na C7.7c, jemná hĺbka `66.5/100`.  
**Úloha:** lokalizovať zdroj výpočtového spomalenia analyticky škálovaného auditu C7.7c bez zmeny fyziky a bez pridelenia bodov.

## 1. Nemenné prvky

Profil musí použiť rovnaké:

- rovnice, znamienka, background a počiatočné stavy ako posledný predregistrovaný C7.7c-K4 pokus;
- analytické obálkové škálovanie `s_i=max(|y_i(x_start)|,|y_i^series(x=-18)|,1e-300)`;
- solver DOP853, `rtol=1e-10`, normalizované `atol=1e-12`, `max_step=0.02` a jednobodové segmenty dĺžky najviac jeden e-fold;
- 13-zložkový BR3C stav a ohraničenú uzáveru `L5=0`.

Profil nesmie meniť operátor, fyzikálne koeficienty, počiatočné podmienky ani tolerancie. Jeho výsledok nie je fyzikálny PASS/FAIL a nemení skóre koľaje.

## 2. Poradie a časové limity

Každý samostatný proces má:

- vnútorný limit najviac `8 s` vrátane vytvorenia autoritatívneho vstupu;
- vonkajší limit `10 s`;
- najviac jeden profilovaný mód/povrch v jednom procese;
- zastavenie po prvom požadovanom segmente alebo pri časovom limite.

Poradie:

1. `NIV/deep` — hlavný podozrivý podľa počtu RHS volaní v BR3C-b;
2. `NIV/shallow` — rozlíšenie závislosti od počiatočného povrchu;
3. `NID/deep` — kontrola, či je problém špecifický pre NIV;
4. iba ak ostane časová rezerva, `NID/shallow`.

Ak prvý segment prejde, môže nasledovať nový, opäť samostatne limitovaný beh s prefixom o jeden segment dlhším. Timeout sa zapisuje ako lokalizačný výsledok, nie ako smrť koľaje.

## 3. Povinný záznam

Pre každý pokus sa zachová:

- mód, povrch, interval a počet dokončených segmentov;
- wall time, `nfev`, počet RHS volaní a počet solverových bodov;
- minimálny, mediánový a maximálny akceptovaný krok, ak sú dostupné;
- maximum absolútneho normalizovaného stavu a názov dominantnej zložky;
- `nfev` na akceptovaný krok ako orientačný indikátor numerickej náročnosti;
- explicitný stav `CAPTURED`, `TIMEOUT_UNCLOSED` alebo `ERROR_UNCLOSED`.

## 4. Rozhodovacie pravidlo

- Profil je úspešný iba v zmysle **získania diagnostiky**; nepridáva body.
- Ak sa náročnosť koncentruje v NIV, ďalšia revízia C7.7c-K5 smie meniť iba jeden numerický prvok adresujúci NIV škálu alebo Jacobian.
- Ak je podobná aj v NID, treba najprv preveriť spoločnú normalizáciu, background interpoláciu alebo metrickú spätnú väzbu.
- Ak je náročnosť viazaná na konkrétny segment, C7.7c-K5 sa predregistruje iba pre tento interval a až potom sa opakuje celý audit.
- Žiadny profilový timeout nie je fyzikálny dôvod na označenie A2-K4 za mŕtvu.

## 5. Skóre

Pred profilom: `66.5/100`.  
Po profile: `66.5/100` bez ohľadu na diagnostický výsledok.  
Ďalších `+0.2` možno prideliť až za úplný, vopred predregistrovaný PASS C7.7c, nie za profil.
