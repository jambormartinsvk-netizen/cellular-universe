# L2-B2 — predregistrácia: prenos formulácie do general-synchronous/BR/P5 línie

**Stav pred behom:** `PRIPRAVENÉ`  
**Skript:** `scripts/239_script_lineage_L2_B2_general_synchronous_ast_audit.py`  
**Vnútorný limit / vonkajší limit:** 5 s / 10 s  
**Metóda:** AST a presné textové kontrakty; bez importu modelov, ODE, skóre a prepisu zdrojov.

## Otázka

Preniesla sa po K7 redukcii pôvodná A2-K4 formulácia so stavom `U_c` a
energy-frame `U_d` niekam inde v korpuse korektne, alebo sa aj general-
synchronous/BR línia potichu zmenila na testové pole či projektovaný stav?

## Povinné rozdelenie pred výsledkom

| Trieda | Cieľové súbory | Čo musí byť pravda, aby trieda sedela |
|---|---|---|
| Kandidát plného skorého systému | 66, 89, 90 | explicitné `UC`/`U_c`, relatívny `U_d`, constraint a dynamická RHS |
| Testové pole | 85, 86, 95 | `U_c` existuje, ale scope explicitne vylučuje backreaction/fixed metric |
| Wrapper alebo neskorší checker | 92, 94, 140, 143, 148 | sám neurčuje fyzickú RHS alebo explicitne deklaruje obmedzený stav |
| Redukovaný potomok | 130, 136, 155 | seed/projekcia môže niesť meno `U_c`, ale nemá sa vydávať za plný evolučný K4; 136/155 sa majú zachytiť ako starý `K_MPC` rad |
| P5 statický kontrakt | 236 | explicitne deklaruje `U_c`, `U_b`, `M_full`, bez ODE a bez skóre |

## Očakávaný výsledok

Očakáva sa, že 66/89/90 zachovávajú `U_c` a majú explicitné constrainty;
85/86/95 sú užitočné, ale iba fixed-metric test field; 136/155 sú redukované
K7 pokračovanie a P5.1 je len správny statický základ. `PASS` znamená, že
mapa je presná a že sa nesmie zlúčiť test field, plný systém a diagnostika.
Nie je to fyzikálny PASS žiadnej z nich.

## STOP

Chýbajúci/neparsovateľný zdroj, timeout alebo nesúlad predregistrovanej
triedy zastavuje mapu. Potom sa nič neprepočítava: najprv sa vysvetlí, či
ide o zmenu formulácie alebo chybu auditu.

## Korekcia auditného pravidla po prvom statickom behu

Prvý nemenný výstup `RUN_LINEAGE_L2_B2_GENERAL_SYNCHRONOUS_AUDIT.json`
správne zastal za 0.094 s. Príčina je **PF-039 auditora**, nie fyzikálny
nález: skript 85 vyjadruje test-field obmedzenie vetou „cannot close G7"
namiesto doslovného „fixed metric". Predregistrované pravidlo sa preto
rozširuje iba o túto explicitnú scope vetu. Mení sa klasifikátor, nie
testovaná fyzika, cieľové súbory ani prahy. Opravený beh dostane nový,
nemenný názov `..._RERUN1.json`.

## Druhá korekcia klasifikácie po RERUN1

`RERUN1` prešiel mapu, ale export odhalil, že skript 66 síce nesie `U_c`
a constrainty, no nemá `U_d`. Preto nie je plný energy-frame kandidát; je
to **standard/null baseline**. Povinnosť `U_d` zostáva pre skutočné plné
kandidáty 89 a 90. Ide o PF-040: prvý kontrolný súčet pre triedu „full"
nevyžadoval všetky prvky vlastnej predregistrácie. Nový `RERUN2` zmení iba
triedu 66 a kontrolné kritérium; fyziku, zdroje, limity aj rozsah nemení.

## Ďalší postup

Ak mapa prejde, vznikne L2-B2 verdict s konkrétnym rozsahom každého
artefaktu. Až potom P5.2 preverí Einsteinove constrainty v plnom stave.
