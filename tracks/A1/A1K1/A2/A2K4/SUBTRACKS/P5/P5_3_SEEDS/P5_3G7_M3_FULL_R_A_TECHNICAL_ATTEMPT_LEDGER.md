# P5.3g7-M3-FULL/R-A — register technických pokusov

**Dátum založenia:** 2026-07-16  
**Route:** `A1-K1 -> A2-K4 -> P5 -> P5.3g7-M3-FULL/R-A`  
**Technická architektúra:** `ARCH-A`  
**Stav:** `ARCH_A_COMPLETED / HISTORICAL_PACKAGE_10_CLOSED / PASS_J4_SENTINEL_SUPPORT`  
**historical_packages_total:** `10`  
**consecutive_technical_failures:** `0/10` po vecne úspešnom KMPC-031  
**Nasledujúci technický balík:** `NONE; no attempt 11 in ARCH-A`  
**Fyzické pokusy:** `0`  
**Fyzikálna hĺbka K4:** bez zmeny, `60/100 = G6`

## 1. Legacy architektúra — zachovaná a konzervatívne započítaná

| Legacy pokus | Výsledok | Dôvod obmedzenia |
|---:|---|---|
| KMPC-022 | `DO_NOT_RUN_TECHNICAL` | PF-055 `numpy.bool_` JSON serializácia; výsledok nevznikol |
| KMPC-023 | `RUNNABLE_REVIEW_ONLY` | PF-056: M1 normalizácia bola iba post-check, `rank=76/77` |
| KMPC-024 | `M1_ANCHOR_ONLY / DO_NOT_USE_PHYSICS` | M1 opravená; PF-058: nebola overená úplná `Phi^0` fuel veža/rows; PF-063: pressure source mal 3× chybnú neadiabatickú časť |

Tieto tri pokusy patria neúplnej 11-zložkovej architektúre. Tá je
`SUPERSEDED_INCOMPLETE_STATE_CONTRACT`, nie fyzikálne mŕtva K4 a nie
`TECHNICAL_STOP` po dosiahnutí capu 10. Keďže však mechanizmus, rovnice a
fyzikálny suffix K4 zostávajú rovnaké, pokusy sa pri konzervatívnom audite
prenášajú do spoločného countera P5.3g7-M3. Premenovanie modulu ani doplnenie
stavov counter nevynuluje.

Úplný kontrakt R-A je nová technická realizácia toho istého fyzikálneho
problému. Preto pokračuje pokusom `4/10`, nie novým `0/10`.

## 2. Vstupná brána pred technickým pokusom 4

Pokus 4 je zakázaný, kým Markdownový B1 balík neuzavrie:

1. coefficient manifest `Phi^0/Phi^1 × z^j`;
2. synchronné fuel/ash continuity a Euler rows z rovnakého `Q_A^mu`;
3. presnú total-energy a total-momentum left-null/Bianchi identitu;
4. ordered state/RHS manifest s úplnou `Phi^0` vežou `delta_f,U_f`,
   dynamickým `U_c` a explicitným `Phi^1` spectator fuel blokom;
5. K4-viazaný `h,eta` seed a steam rail;
6. nulové limity `gamma->0`, `A_f->0` a background bez Fourierovho `k`.

## 3. Nemenná história desiatich balíkov

| Pokus | Dátum | Technický míľnik | Výsledok | Kategória a presný dôvod | Dôkaz/oprava |
|---:|---|---|---|---|---|
| 1 | 2026-07-16 | KMPC-022 | `TECHNICAL_FAILURE` | PF-055 `SCRIPT_IMPLEMENTATION_FAILURE`: `numpy.bool_` nebolo JSON serializovateľné; autoritatívny výsledok nevznikol | chyba zachovaná v error ledgeri; runner nepoužívať |
| 2 | 2026-07-16 | KMPC-023 | `TECHNICAL_FAILURE` | PF-056 `SCRIPT_IMPLEMENTATION_FAILURE`: M1 normalizácia bola iba post-check mimo solve; navyše PF-057 stale identifikátor | výsledok iba `REVIEW_ONLY`; kontrakt sa musí presunúť pred solve |
| 3 | 2026-07-16 | KMPC-024 | `TECHNICAL_FAILURE` | PF-058 až PF-060 a PF-063 `SCRIPT_IMPLEMENTATION_FAILURE`: nebola vyriešená/overená úplná `Phi^0` fuel veža, pressure source bol v neadiabatickej časti 3× chybný, ochrana bola tautologická a deklarovaný two-start test nevykonal dve nezávislé integrácie | zachovať len M1 anchor a k-cancel scope; nepoužiť frakčný trace/holdout ako fyzikálny dôkaz |
| 4 | 2026-07-16 | KMPC-025 B1 preflight | `PASS_ALGEBRA_SCOPE / TECHNICAL_FAILURE` | PF-064 `SCRIPT_IMPLEMENTATION_FAILURE`: state guard overoval lokálny count/unique a fixtures iba porovnávali s tým istým lokálnym tuple | raw 15/15 a JSON zachované; nepoužiť ako celý B1 PASS; pokus 5 oddelí contract a validator |
| 5 | 2026-07-16 | KMPC-026 independent contract guard | `PASS_R_A_B1_CONTRACT_GUARD_ONLY` | PF-064 opravená samostatným contract modulom a spoločným validatorom; 9/9 checks, 9/9 chybných fixtures odmietnutých | B1 uzavretá iba preflight scope; povoľuje preregistráciu pokusu 6, bez bodov |
| 6 | 2026-07-16 | KMPC-027 full M3-TCA0 seed | `TECHNICAL_TIMEOUT / PHYSICS_NOT_RUN` | compile/help/smoke PASS; prvý AD full-mode shard prekročil 4.8 s interný limit počas extended holdout matice; bez AD verdictu, ostatné módy NOT_RUN | dokumenty 38–39; failure JSON SHA `6AB1...A475` |
| 7 | 2026-07-16 | KMPC-028 atomic M3-TCA0 sharding | `REVIEW_TRUNCATION_EXTENSION_REQUIRED / TECHNICALLY_EXECUTED` | compile/help PASS; sentinel AD/0.05/nominal dobehol, všetky rovnice/ranky/holdouty PASS, ale J2/J4 tail `3.27e-3 > 1e-6`; zvyšných 44 podľa stop pravidla NOT_RUN | dokumenty 40–42; immutable JSON SHA `2294...FC83`; bez fyzikálnej smrti |
| 8 | 2026-07-16 | KMPC-029 support ladder J4/J6/J8 | `REVIEW_J8_NUMERICAL_DRIVER_RESIDUAL` | J6 PASS; J8 plný rank/holdout/guards PASS, iba driver `1.5577e-10 > 1e-10` na `fuel_Euler[8]`; aggregate NOT_RUN | dokumenty 43–45; J6 SHA `658495...C4636A`, J8 SHA `1EE3FC...D51AB8`; bez fyzikálneho STOP |
| 9 | 2026-07-16 | KMPC-030 J8 one-refinement + ladder | `TECHNICAL_COMPLETE / REVIEW_TAIL_METRIC_SEMANTICS` | všetkých 22 numerical checks PASS; pôvodný `fuel_Euler[8]` incident reprodukovaný a jedna korekcia dala driver `1.71e-16`, holdout `3.37e-11`; raw deep tail mieša roundoff drift zakázaného `U_b[0]` s added powers | dokumenty 46–47; JSON SHA `8CB706...3C6F`; posledný pokus 10 iba rozloží tail bez solve a bez zmeny prahov |
| 10 | 2026-07-16 | KMPC-031 no-solve deep-tail provenance | `PASS_SUPPORT_TRUNCATION_J4_SENTINEL_SCOPE / ARCH_A_COMPLETED` | raw FAIL reprodukovaný; common drift oddelený od added powers; 25/25 checks a oba J4/J6, J6/J8 tails PASS bez zmeny prahov | dokumenty 48–50; JSON SHA `C547F8...92FF6`; celý P5.3/K4 ostáva otvorený |

Jeden pokus je jeden vopred oznámený compile/import/help/smoke/run balík
pre konkrétny míľnik. Každá fáza má vlastný krátky timeout. Markdown,
read-only audit a hash inventár sa nepočítajú ako technický pokus.

Podľa najnovšieho pravidla sa cap posudzuje z po sebe idúcich technických
zlyhaní. Spätne čítaný aktívny counter po balíkoch 1–10 je
`1,2,3,4,0,1,0,0,0,0`: balíky 5, 7, 8, 9 a 10 priniesli vecný
interpretovateľný čiastkový výsledok a counter vynulovali. Táto rekonštrukcia
nemení ich scoped fyzikálny význam ani nemaže historické incidenty.

## 4. Stav po desiatom balíku

KMPC-031 úspešne uzavrel vopred definovaný cieľ, preto je architektúra
`COMPLETED_AT_HISTORICAL_PACKAGE_10` a nevznikne pokus 11 tej istej ARCH-A.
Aktívny counter je však `0/10`, nie `10/10`.

Ak by desiaty balík technicky zlyhal:

Po desiatom **po sebe idúcom** neúspešnom technickom balíku dostane daná
implementačná línia
`TECHNICAL_STOP` s presnou kategóriou script, Python, sandbox alebo
build/adapter. K4 zostane `REVIEW_TECHNICAL_UNRESOLVED` a nesmie sa označiť
za fyzikálne mŕtvu. Vecný úspešný výpočet counter vynuluje; smoke, compile,
hash-only kontrola alebo premenovanie nie. Úplná história zostáva zachovaná.
