# A2-K11 — ortogonálny momentum-drag operátor

**Stav:** `WITHDRAW_FALSE_PASS / LIVE_BACKUP / WAITING_FOR_DERIVED_REGULAR_ORTHOGONAL_OPERATOR_AND_FULL_DAE_CONTRACT`  
**Workflow fáza:** `CONTRACT_DRAFT_NOT_OPEN / ACTIVE_TECHNICAL_COUNTER_0_OF_10`  
**Post-error stav:** `R8 PRE-SOLVER BLOCKER MAPPED — 2026-07-16`  
**FS-GATE-01:** `NONEMPTY_WITNESS_K11_R_CONSTITUTIVE_CLASS / REVIEW`;
scoped STOP uniformnej regularity + exact pole cancellation; bez zmeny skóre  
**Max. hĺbka:** `10/100`

**K11-CS1:** `UNDETERMINED_REVIEW / FULL MULTISPECIES DAE REQUIRED`;
`PASS_EARLY_INDICIAL_NULL_LIMIT`; bez zmeny hĺbky
**K11-CS2/S0 po PF-062:** `PASS_FORMULA_IDENTITIES_ONLY /
STOP_STATE_REGISTER_V001`; full DAE, regular basis a propagátor ešte
`NOT_IMPLEMENTED`; bez zmeny hĺbky
**K11-CS2/full v002:** `PASS_SOURCE_AST_STRUCTURAL_ONLY /
FULL_THERMAL_TCA_DAE_NOT_IMPLEMENTED`; historical packages `5`, active
counter `0/10`; v003 vznikne iba pri zmene fyziky
**CLASS/HyRec source map:** `BACKEND_FEASIBLE_SOURCE_INJECTION_POINTS_FOUND /
FULL_V002_NOT_IMPLEMENTED`; bez zmeny hĺbky

K11 skúma prenos hybnosti bez zmeny backgroundového prenosu energie. Staré
skripty 45–54 testovali konkrétny zápis a jeho numerickú stabilitu, ale
nesmú sa citovať ako fyzikálny PASS: audit odhalil neuzavretú kovariantnú
definíciu, problematické znamienka/constraint interpretácie a chýbajúci
regulárny operátor. Stabilné tlmenie zvolenej ODE nie je dôkazom existencie
fyzikálnej sily.

`K11-TC-A0` je scoped technicko-matematický STOP univerzálnej finite-`L`
closure; `K11-TC-A3` je structural enablement. Ani jeden stav nezatvára
rodičovskú K11 koľaj a aktívny counter zostáva `0/10`.

Ďalší krok je nový kovariantný ortogonálny operátor s nulovým backgroundom,
presnou momentum conservation a regulárnym `delta→0` limitom.

Pokus o postup ku G5 sa zastavil pred G2/G3. Projector je ansatz, nie
odvodený lokálny operátor; staré numerické tlmenie preto nepridáva body.

Bez znalosti presnej funkcie už platí: sila musí tlmiť, zaniknúť pri
rovnakej rýchlosti alebo chýbajúcom médiu a jej reakcia musí zostať konečná
pri `delta rho_f->0`. Staré znamienko a `Upsilon=gamma rho_c` túto spoločnú
množinu nespĺňajú.

FS-GATE našla explicitný zdravý momentový svedok
`Upsilon_R=Gamma rho_c delta rho_f/(rho_c+delta rho_f)`. Je kladný,
regularizuje obe Eulerove sadzby, zachováva celkovú hybnosť a tlmí relatívny
mód sadzbou `Gamma`; nulový FLRW heat a PSD noise štruktúra sú možné.
Mikrofyzický pôvod, úplné rovnice a stabilita však chýbajú, preto G2/G3 ani
skóre nepostúpili.

Zároveň je mŕtva podtrieda, ktorá chce byť uniformne regulárna pri
`delta->0` a súčasne rušiť celý M-009 pól `Gamma/delta` pre všetky malé
`delta`. Pri pevnom `delta=0.02297` zostáva účinnosť otvorená, ale potrebná
sadzba musí byť odvodená, nie fitovaná. Úplný dôkaz je v
`ARTIFACTS/FS_GATE_01_K11_R_REGULAR_ORTHOGONAL_DRAG_RESULT_AND_AUDIT.md`.

Následný exaktný audit navyše ukázal, že interaction-only velocity matica
má pre každé pasívne `Upsilon>0` determinant
`-(Upsilon/rho_c)(Gamma/delta)<0`. Samotný drag teda nikdy neurobí tento
podblok Hurwitz; podtrieda
`K11-R-PASSIVE-INTERACTION-BLOCK-HURWITZ-CURE` je mŕtva. Plný K11 systém
ostáva REVIEW iba preto, že Hubble, pressure, density a metric väzby robia
kozmologický systém väčší než tento neuzavretý podblok.

CS1 odvodila úplný dark `k->0` blok a constraintovú plochu, ale ukázala,
že fyzický symbol musí obsahovať aj baryóny, fotóny, neutrína, paru a scaled
shear. Pri finite proper-time sadzbách nové interakcie v radiačnej ére
škálujú ako `O(a^2)`, takže leading Frobenius basis je GR-like. M-009 sa tým
obmedzuje na konečnú/neskorú amplifikáciu, nie nový primordiálny indiciálny
exponent. Full fixed-delta stabilita zostáva REVIEW a má už iba jeden
povolený následný krok K11-CS2.

K11-CS2 je predregistrovaná v
`ARTIFACTS/K11_CS2_FULL_MULTISPECIES_CONSTRAINED_DAE_PREREGISTRATION.md`.
Očakávanie pred behom je nepriaznivé (`ln` relatívneho transferu približne
`10–13`), ale fyzický STOP je povolený iba po úplnom species/stress ledgeri,
netautologických Einstein/Bianchi holdoutoch a konvergencii. Aktuálny stav
zostáva `REVIEW` a `10/100 = G1`.

S0 RUN-002 prešiel exact K11/A1/CAMB formula identitami. PF-062 však odhalil,
že state register pridal neexistujúce CAMB scalar E-mode položky `E_0,E_1`;
lokálny count bol tautologický. Formula identity zostávajú PASS, state
contract v001 je STOP a správny count je `4*lmax+9`. Neobsahoval ODE ani
constraint propagáciu, preto neudeľuje G2/G3 ani body. Plný propagátor musí
byť nová versioned base revízia a posledná technická oprava 2/2.

Full v002 kontrakt je zmrazený v
`ARTIFACTS/K11_CS2_FULL_V002_PF062_LAST_REPAIR_PRERUN.md`. Matematický audit
okrem PF-062 našiel aj chýbajúci explicitný horný closure: generic CAMB
rekurencia pri `ell=lmax` odkazuje na neregistrovaný `lmax+1`. Fyzikálny
audit zároveň vyžaduje `x_e/opacity/T_b` vypočítané na exact-A1 backgrounde.
Štandardná ΛCDM tabuľka alebo necertifikovaný post-recombination handoff
nemôžu udeliť PASS ani STOP. Preto sa posledný runner nespustí ako
čiastková oprava registra; musí byť celý alebo skončí
`REVIEW_BLOCKED_IMPLEMENTATION` bez v003.

Neskorší priamy pokyn používateľa obmedzil formuláciu „technická oprava
2/2“: technické incidenty sa evidujú a opravujú, nespotrebujú fyzikálny
pokus a nemôžu zabiť ani natrvalo zablokovať K11. V002 zostáva fyzickým
suffixom; jeho interný balík a runner sa smú technicky opravovať bez vzniku
v003, pokiaľ sa nemenia rovnice, mechanizmus, prahy ani rozsah.

Následné spresnenie zaviedlo cap 10 pokusov na jednu technickú
architektúru. V002/ARCH-A začína `0/10`. Po desiatom technickom neúspechu
zomrie iba ARCH-A s explicitným dôvodom script/Python/sandbox/build; K11
zostane `REVIEW_TECHNICAL_UNRESOLVED` a môže dostať inú zdokumentovanú
technickú architektúru.

Následná read-only mapa pripla CLASS/HyRec ako uskutočniteľný zdrojový
backend: exact-A1 `H(z)` sa vedie priamo do HyRec. Nie je to však drop-in
adapter. CLASS potrebuje coupled fuel/ash background, custom perturbácie a
regular modes; jeho `pol0...polL` báza ani dynamický TCA stav nie sú náš
CAMB-E register 25/33/41. Presná mapa a blockery sú v
`ARTIFACTS/K11_CS2_CLASS_HYREC_ARCHITECTURE_SOURCE_MAP_AND_FEASIBILITY_AUDIT.md`.
Tento krok nepridal G-bránu ani body.

Analytická COMP skratka je mŕtva: hoci na jednej ploche existuje nenulová
density/momentum/pressure kompenzovaná dark priamka, pressure conversion ju
okamžite opustí. V skorom radiačnom limite by jej invariantnosť vyžadovala
anti-drag. Scoped výsledok
`K11-CS2-COMP-INVARIANT-DARK-SUBSPACE: EMPTY_CERTIFIED_SCOPE` nezabíja K11;
dokazuje, že plný metric/species propagátor nemožno obísť.

Po zrušení starého capu 2/2 bol full v002 znovu posúdený. Counter zostáva
`0/10`: informatívny attempt 1 ešte blokuje chýbajúca horná uzávera
kanonického CAMB `E_gamma_L`, prípadne ekvivalentná presná CLASS↔CAMB-E mapa.
Exact register `4L+9 = 25/33/41`, negatívne fixtures a interface podmienky sú
zmrazené v
`ARTIFACTS/K11_CS2_FULL_V002_CONTRACT_CLOSURE_AND_ATTEMPT1_READINESS_2026-07-16.md`.
Najprv sa auditne skúma technická koľaj K11-TC-A; žiadny ODE ani bod.

K11-TC-A audit následne preukázal invariantný no-go iba pre univerzálnu
presnú finite-`L` CAMB-E closure: konečný register neurčuje voľný
`E_(L+1)`. Táto podkoľaj je mŕtva ako `K11-TC-A0`, nie K11. Aktívna
technická cesta `K11-TC-A3` používa presné vnútorné CAMB riadky, výslovne
numerický top rez a povinný budúci `lmax`/closure sweep. Po štyroch
zdokumentovaných technických incidentoch prešiel pokus 5 ľahkým pinned-source
AST auditom `55/55`, counts `25/33/41`, exit 0. Dobový zápis bol `5/10`; ide iba
o structural scope bez ODE a hĺbka zostáva `10/100`. Podľa neskoršieho
pravidla ide o `historical_packages_total=5` a aktívny counter sa po tomto
vecnom úspechu vynuloval na `0/10`.
