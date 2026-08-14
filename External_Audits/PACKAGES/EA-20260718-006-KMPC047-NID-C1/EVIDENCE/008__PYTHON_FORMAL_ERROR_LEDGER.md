# Register formálnych a implementačných chýb Python skriptov

Dátum účinnosti: 2026-07-15  
Stav: záväzný živý register

## Účel

Tento súbor je trvalá projektová pamäť chýb vzniknutých pri tvorbe alebo skladaní Python skriptov. Formálna, parserová, serializačná, markerová, CLI alebo runtime-API chyba nie je fyzikálny výsledok. Neúspešný skript sa nemaže ani ticho neopravuje; dostane technický stav a oprava nové číslo, nové immutable run ID alebo explicitne auditovaný nemenný wrapper.

Podľa pracovného pravidla `WORKING-TECH-INCIDENT-NONCONSUMPTION` technický
incident nespotrebuje fyzikálny pokus a nemôže vydať fyzikálny STOP ani
zabiť rodičovskú koľaj. Pevný cap technických opráv neplatí. Opakovaná
trieda chyby vynúti preflight, zdieľaný base test alebo architektonickú
zmenu technickej cesty; fyzikálny suffix sa nemení, kým sa nemenia rovnice,
mechanizmus alebo rozsah.

Neskoršie spresnenie používateľa zavádza cap `10` technických pokusov na
jednu konkrétnu implementačnú vetvu. Najnovšie spresnenie ho definuje ako
cap 10 **po sebe idúcich** technických zlyhaní. Vecný technicky úspešný
výpočet s platnou provenienciou a aspoň čiastkovým interpretovateľným
výsledkom aktívny counter vynuluje; compile, `--help`, smoke, hash-only a
prázdny test ho nevynulujú. Po desiatom po sebe idúcom technickom neúspechu sa
vetva označí `TECHNICAL_STOP` s kategóriou
`SCRIPT_IMPLEMENTATION_FAILURE`, `PYTHON_OR_DEPENDENCY_FAILURE`,
`SANDBOX_OR_ENVIRONMENT_FAILURE` alebo `BUILD_OR_ADAPTER_FAILURE` a s
presným dôvodom. Fyzikálna koľaj tým neumiera; zostáva
`REVIEW_TECHNICAL_UNRESOLVED` a môže použiť inú predregistrovanú technickú
architektúru s vlastným ledgrom. Historické balíky sa ani po resete nemažú;
route-local ledger vedie osobitne `historical_packages_total` a
`consecutive_technical_failures`.

Globálna pamäť asistenta medzi nezávislými úlohami nie je zaručená. Autoritatívnou pamäťou sú preto tento register, pravidlá `05` a auditné MD.

## Povinná kontrola pred numerickým behom

1. `python -m py_compile <script>` s externým limitom.
2. Krátky CLI/parser smoke-test, ak skript používa argumenty.
3. JSON serializačný smoke-test, ak skript exportuje machine-readable výsledok; NumPy/SymPy skaláre sa musia konvertovať na natívne typy.
4. Pri generovanom zdroji skontrolovať presný zdrojový súbor, jedinečnosť markera, skompilovať vygenerovaný text a exportovať identitu skutočne vykonanej cesty.
5. Každý beh musí spĺňať AR29: externý timeout je povinný; dlhší skript má aj interný deadline a checkpoint/RHS cap.
6. Gate importujúci JSON musí spĺňať AR51 a zlyhať uzavreto pri chýbajúcom kľúči.

Úspešný `py_compile` nestačí na odhalenie nesprávneho poradia JSON kľúčov, zlej markerovej cesty, fail-open logiky ani nedosiahnuteľného kódu. Preto nasleduje aj minimálny behaviorálny smoke-test.

## Povinný zápis chyby

Každá nová chyba dostane riadok s: identifikátorom, dátumom, skriptom, kategóriou, presným symptómom/exception, príčinou, informáciou či sa fyzika vôbec vykonala, stavom starého skriptu, nástupcom a preventívnou kontrolou. Ak existuje výstup alebo checksum, ostáva pri auditnom MD.

## Aktuálny register

| ID | Skript/beh | Kategória a symptóm | Koreňová príčina | Vykonaná fyzika? | Stav a nástupca | Povinná prevencia |
|---|---|---|---|---|---|---|
| PF-001 | 118/119 | `SyntaxError` v generovanom zdroji | chybná skladba textového patchu | nie | zachované ako syntax-error stopy; neskoršie klony | `py_compile` vygenerovaného zdroja pred behom |
| PF-002 | 173 | marker-path `RuntimeError` | wrapper patchoval 171, marker bol v texte 170 | nie | technicky mŕtvy; oprava 174 | overiť presný zdroj a `count==1` ešte pred fyzikou |
| PF-003 | 179 | `K7c.2 seed names changed` | poradie `dict` po `sort_keys=True` bolo mylne považované za stavové poradie | nie | technicky mŕtvy; oprava 180 | kontrolovať množinu kľúčov a vektor skladať explicitne cez `NAMES` |
| PF-004 | 181 | safety-cap pred prvým stĺpcom | jednotková fyzikálna sonda pri škále rádovo `1e-29` | nie | technicky mŕtvy; oprava 182 | sondovať v normalizovaných súradniciach po dôkaze linearity |
| PF-005 | 183 | JSON serializácia NumPy bool | machine export dostal nenatívny skalár | výpočet áno, export nie | technicky mŕtvy export; oprava 184 | rekurzívna konverzia a JSON smoke-test |
| PF-006 | 172/175 | latentný fail-open rank check | `.get(a)==.get(b)` je pravda pri dvoch chýbajúcich kľúčoch | áno; skutočné kľúče boli prítomné | numerický PASS sa neruší; nový fail-closed nástupca povinný | AR51: existencia, typ, konečnosť a až potom porovnanie |
| PF-007 | 183–185 | nedosiahnuteľný starý `solve_ivp` | fixed-RK4 bol vložený pred skorý return, legacy blok ostal za ním | fixed-RK4 áno; legacy nie | výsledky ostávajú REVIEW; nový samostatný solver | AR52 a export vykonanej path identity |
| PF-008 | 186 | nedokončený súbor končiaci `__K7C3D_CONTINUE__` | tvorba bola prerušená pred dokončením ledgeru | nie | neautoritatívna zachovaná stopa; náhrada s novým číslom | pred spustením EOF/entry-point kontrola, `py_compile` a output smoke-test |
| PF-009 | 187, prvý auditný beh | falošné negatíva statických markerov | príliš krehké doslovné substringy nerešpektovali skladané reťazce wrapperov | numerické porovnanie áno; statický súhrn ešte nie | markery opravené a audit zopakovaný | kontrolovať presný zdroj wrappera a vyžadovať známy pozitívny fixture |
| PF-010 | skorší dlhý Python beh zastavený používateľom | prevádzkové porušenie timeoutu | beh nemal účinný krátky externý limit/kontrolný interval | bez autoritatívneho úplného výsledku | TIMEOUT/STOPPED, nie fyzikálny verdikt | AR29: externý limit každý raz, kontrola do 10 s, úseky najviac 60 s |

| PF-011 | PowerShell inventár 174–176/187 | `ParserError: An empty pipe element is not allowed` | výstup `foreach` bol nesprávne pipovaný priamo bez obalenia alebo medzipremennej | nie; Python sa nespustil | príkaz technicky mŕtvy; oprava cez `$items = foreach (...) {...}; $items | ...` | orchestration smoke-test; zložité `foreach` výstupy vždy najprv uložiť do premennej |

| PF-012 | 189 a závislý 190 | `RuntimeError: generated parser marker is not unique` pri `--help` | parserový patch bol vložený do wrapper vrstvy 169, ale cieľový parser vzniká až v ďalšej generovanej vrstve 166 | nie | 189 `DO_NOT_RUN_TECHNICAL`; 190 technicky nepoužiteľný; nové číslované nástupce povinné | pred patchom zostaviť mapu všetkých compile/exec vrstiev a marker overiť v skutočnom texte bezprostredne pred jeho vykonaním |

| PF-013 | PowerShell generovanie 197, prvý pokus | `ParserError: Unexpected token '__main__'` | vo vnútri PowerShell double-quoted reťazca bolo chybne použité C-style escapovanie `\"`; PowerShell vyžaduje backtick alebo bezpečné skladanie z literal častí | nie; Python sa nespustil a cieľový súbor nevznikol | príkaz technicky mŕtvy; opravený príkaz musí použiť literal marker a pred zápisom overiť zdroj aj cieľ | pri zmiešaní shell/Python syntaxe skladať markery z single-quoted literal častí a pred veľkým generovaním urobiť parserový smoke-test |

| PF-014 | čítacia kontrola zdroja 179 | `Could not find file` | cesta bola zostavená z čísla a odhadnutého starého názvu namiesto autoritatívneho inventára | nie; iba neúspešné čítanie | príkaz technicky mŕtvy, bez zmeny súborov | pred použitím číslovaného skriptu získať presnú cestu cez filtrované `rg --files` |

| PF-015 | prvý inventár cesty 179 | inventár našiel dve položky vrátane `__pycache__/*.pyc` | filter hľadal prefix 179 bez obmedzenia na zdrojové `.py` a bez vylúčenia cache | nie; iba kontrolný inventár | príkaz fail-closed správne zastal, bez zmeny súborov | používať `rg --files scripts -g '*.py' -g '!**/__pycache__/**'` a vyžadovať presne jeden výsledok |

| PF-016 | post-run inventár piatich P1 dôkazov | opakovaný `ParserError: An empty pipe element is not allowed` | napriek PF-011 bol `foreach` znovu priamo napojený na pipeline; známa prevencia nebola pred príkazom uplatnená | nie; parser zastal pred akýmkoľvek čítaním, zápisom alebo behom | príkaz technicky mŕtvy, P1 výsledok nedotknutý | pred každým PowerShell `foreach` príkazom povinne vyhľadať PF-011/PF-016 a použiť `$items = foreach (...) {...}`; pipeline až v samostatnom príkaze |

| PF-017 | hromadná MD aktualizácia po P1, prvý pokus | fail-closed `status recommendations marker count is not one` | viacriadkový exact marker a cieľový MD používali odlišnú konvenciu koncov riadkov | nie; všetky zápisy boli až za validačnými kontrolami, preto sa nezmenil žiadny cieľ | príkaz technicky mŕtvy, bez čiastkového zápisu | pred viacriadkovými presnými náhradami normalizovať zdroj aj marker na LF, validovať všetky počty a až potom zapisovať |

| PF-018 | hromadná MD aktualizácia po P1, druhý pokus | `ParserError: You must provide a value expression following the '+' operator` | volanie funkcie `LF` bolo vložené priamo za operátor `+` bez zátvoriek alebo medzipremennej | nie; parser zastal pred všetkými zápismi | príkaz technicky mŕtvy, bez čiastkového zápisu | viacriadkové dodatky najprv uložiť do samostatnej premennej, potom normalizovať a až následne konkatenovať |

| PF-019 | samostatná aktualizácia centrálneho registra, prvý pokus | `Invoke-History: A positional parameter cannot be found` | pomocná funkcia bola pomenovaná `R`, čo v PowerShell koliduje s case-insensitive aliasom `r` pre `Invoke-History` | nie; zlyhanie pri prvej náhrade pred zápisom | príkaz technicky mŕtvy, register nezmenený | nepoužívať jednoznakové názvy pomocných funkcií; použiť explicitný nekolidujúci názov a prípadne `Get-Command` smoke-test |

| PF-020 | prvá záverečná MD konzistenčná kontrola | `ParserError: Variable reference is not valid` pri `"$p:..."` | dvojbodka bezprostredne za interpolovanou PowerShell premennou bola interpretovaná ako súčasť mena/scope | nie; parser zastal pred kontrolou aj zápisom | príkaz technicky mŕtvy, dokumenty nezmenené | pri premennej nasledovanej dvojbodkou použiť `${p}` alebo bezpečnejšie formátovací operátor `'{0}:{1}' -f ...` |

| PF-021 | kontrola duplicity AR59/Q83 cez `rg` | prázdny výsledok skončil exit code 1 a shell ho označil ako zlyhanie | `rg` používa 1 pre legitímny stav bez zhody; príkaz nerozlíšil no-match od technickej chyby | nie; iba read-only vyhľadávanie | príkaz interpretačne neuzavretý, súbory nezmenené | po `rg` akceptovať exit 0 alebo 1, pri 1 zapísať `NO_MATCH`, a zlyhať iba pri exit >1 |

| PF-022 | prvá konzistenčná kontrola adresárového návrhu V2 | falošný negatív `V2HasStationModel=false` pri reálne prítomnom texte | opak PF-009: krehký doslovný marker nepočítal s Markdown backtickmi okolo `A1`, `A2`, `A3` | nie; read-only kontrola, súbory nezmenené | kontrola korektne našla aj štyri reálne chýbajúce prázdne riadky; obsahové markery však treba písať významovým regexom a overiť pozitívny fixture |

## Pravidlo aktualizácie

Register sa doplní hneď po identifikovaní chyby a pred pokračovaním opravenou fyzikálnou koľajou. Opravený nástupca nesmie vymazať dôvod zlyhania predchodcu. Ak neskorší audit zmení interpretáciu, pridá obmedzenie alebo nový riadok; historický text sa neprepisuje potichu.

Prevádzkové timeouty sú osobitne záväzne definované v `scripts/00_EXECUTION_TIME_LIMITS.md` a AR29.

## Dodatok PF-023 a PF-024

| ID | Skript/beh | Kategória a symptóm | Koreňová príčina | Vykonaná fyzika? | Stav a nástupca | Povinná prevencia |
|---|---|---|---|---|---|---|
| PF-023 | generovanie checkeru 200, prvý pokus | fail-closed marker not unique; cieľový súbor nevznikol | opakovanie PF-009/PF-022: krehký doslovný marker sa nezhodoval s reálnym raw-regex riadkom v zdroji 198 | nie; Python sa nespustil a zápis bol až za všetkými kontrolami | príkaz technicky mŕtvy | hľadať významový začiatok riadku FAIL_OPEN cez ukotvený regex, vyžadovať presne jednu zhodu a vkladať podľa indexu zhody |
| PF-024 | prvý pokus o zápis PF-023 | JavaScript SyntaxError pred volaním shellu | Markdown backticky vo vnorenom PowerShell here-stringu ukončili JavaScript template literal nástroja | nie; shell sa vôbec nespustil | orchestration príkaz technicky mŕtvy | pri functions.exec nevkladať raw Markdown backticky do JavaScript template literal; použiť text bez backtickov alebo bezpečne skladané dvojito citované riadky |
## Dodatok PF-025 až PF-027

| ID | Skript/beh | Kategória a symptóm | Koreňová príčina | Vykonaná fyzika? | Stav a nástupca | Povinná prevencia |
|---|---|---|---|---|---|---|
| PF-025 | Markdown aktualizácia po P2 | aj triviálny `Write-Output` visel v spúšťacej vrstve | prihlasovací PowerShell profil/launcher sa nevrátil; s `login=false` rovnaký test prešiel | nie | všetky visiace bunky ukončené, bez zápisu | pre ohraničené auditné príkazy použiť `login=false`, ak login shell neprejde krátkym echo smoke-testom |
| PF-026 | povinný `apply_patch` po P2 | zabudovaný nástroj zlyhal na `windows sandbox helper_unknown_error`; externý WindowsApps obal vrátil `Access is denied` | chybná sandbox inicializácia a zákaz priameho spustenia packaged Codex binary | nie | žiadny pokus nezapísal súbor; dočasný fallback je `git apply --no-index --check` a až potom apply | najprv skúsiť štandardný `apply_patch`; fallback použiť iba po zdokumentovanom zlyhaní a vždy s oddeleným `--check` |
| PF-027 | prvé fallback diffy po P2 | `corrupt patch` alebo `patch does not apply` | manuálne nesprávny začiatok/počet riadkov hunku a príliš široký kontext | nie; každý diff zastavil `--check` pred zápisom | neúspešné diffy technicky mŕtve; malé hunks s `--unidiff-zero` prešli | pri fallbacku deliť zmenu na malé hunks, používať `--recount` pre nové súbory a nikdy neobísť prekontrolu |

Tieto tri položky nemenia fyzikálny rozsudok P2 ani vstupy P3a.

## Dodatok PF-028 a PF-029

| ID | Skript/beh | Kategória a symptóm | Koreňová príčina | Vykonaná fyzika? | Stav a nástupca | Povinná prevencia |
|---|---|---|---|---|---|---|
| PF-028 | prvý statický preflight skriptu 201 | falošný zákaz solvera po nájdení slova `RK4` | regex miešal dokumentačný text rozsahu so skutočným importom alebo volaním | nie; Python sa nespustil | kontrola technicky mŕtva; významový regex pre import/call prešiel | statické zákazy viazať na syntax importu/volania, nie na samotné odborné slovo v reťazci alebo komentári |
| PF-029 | prvý py_compile/help/smoke preflight 201 | združený PowerShell príkaz nevrátil výstup a bol ukončený | tri Python procesy a pipeline boli spojené do jednej bunky, takže timeout nelokalizoval fázu | nie; žiadny autoritatívny JSON nevznikol | samostatné priame `cmd.exe /d /c C:\Python311\python.exe ...` behy prešli | jedna Python fáza na jeden externe ohraničený príkaz; version, compile, help a smoke nespájať |


## Dodatok PF-030

| ID | Skript/beh | Kategória a symptóm | Koreňová príčina | Vykonaná fyzika? | Stav a nástupca | Povinná prevencia |
|---|---|---|---|---|---|---|
| PF-030 | P3a-B skript 204 | `--help` neobsahoval povinný `--output` | patch vložil `parser.add_argument` až za `args = parser.parse_args()` | nie; prebehol iba py_compile a help, bez seed source, ODE alebo výstupu | 204 `DO_NOT_RUN_TECHNICAL`; nový nástupca 205 z čistého 197 | po každom parser patchi overiť poradie v AST/zdroji a v help výstupe explicitne vyžadovať každý nový argument |

## Dodatok PF-031

| ID | Skript/beh | Kategória a symptóm | Koreňová príčina | Vykonaná fyzika? | Stav a nástupca | Povinná prevencia |
|---|---|---|---|---|---|---|
| PF-031 | P3a-B source auditor 206 | `RuntimeError: assignment 'x_start' count changed: 0` | AST extraktor podporoval iba samostatný `ast.Name`, nie tuple target `x_start, x_final` | nie; 197/205 neboli importované ani spustené a output nevznikol | 206 `DO_NOT_RUN_TECHNICAL`; nástupca 207 | pri extrakcii assignmentov pokryť Name aj Tuple target, pre tuple mapovať zodpovedajúci prvok value tuple a pridať pozitívny fixture pred plným auditom |

| PF-032 | 221, prvý `--help` preflight | `ModuleNotFoundError: No module named 'camb'` počas importu shared modulu | `structural.py` použil `Path(...).parents[4]` namiesto koreňa projektu `parents[3]`, takže nehľadal `D:\Teoria\.deps\python` | nie; prešiel iba `py_compile`, SCREEN ani JSON sa nespustili | G8 RUN-001 je technický `DO_NOT_RUN`; lokálna cesta sa opraví a celý preflight sa opakuje | pri module v `scripts/baseScripts` overiť odvodený `ROOT` krátkym import/CLI behom; `py_compile` samotné neoveruje závislosti |
| PF-033 | 221, druhý `--help` preflight | vonkajší timeout `10 s` počas CAMB importu | kompilácia potvrdzuje syntax, nie štartovací čas importu; žiadne ODE ani audit neboli vykonané | nie | prvý pokus je `TIMEOUT_TECHNICAL`; predregistrovaný jeden opakovaný CLI/import pokus s limitom `15 s` | exact/structural balík môže mať externe najviac 15 s; timeout nemení fyzikálny stav a nesmie viesť k obchádzaniu importu |
| PF-034 | 221, RUN-001 | falošný `STOP_G8_IMPLEMENTATION_MAPPING` v kontrole `combined_Euler_to_K7_background_notation` | porovnanie nedefinovalo explicitne `inv1r=1/(1+R)` a `load_fraction=R/(1+R)`; zvyšných 39/40 identít bolo nulových | nie; ODE ani rekombinácia nebežali | immutable RUN-001 aj 221 ostávajú; 233 je úzko obmedzený opravný wrapper | pri symbolických skratkách vždy porovnávať generický zápis až po dosadení všetkých definujúcich rovností; neprepisovať starý výsledok |
| PF-035 | S2 inventár, jednorazový `import scipy` probe | Python environment probe bežal bez predchádzajúceho Markdown očakávania | procesné pravidlo „pred každým Python behom MD“ nebolo aplikované na zdanlivo triviálny import | nie; žiadne ODE, model ani JSON | probe je zdokumentovaný, neautoritatívny a nesmie sa citovať ako S2 test | aj dependency/import/version probe musí mať pred behom očakávanie alebo sa vykoná až v riadnom preflighte |
| PF-036 | 234, prvý preflight/run | `ModuleNotFoundError: No module named 'scripts.baseScripts'` | Runner bežal ako `scripts\\234...py`, preto je `D:\\Teoria\\scripts` importný koreň; import redundatne začínal `scripts` | nie; program skončil pred integráciou i vytvorením JSON | import zmenený na `baseScripts.k_mpc_005...`; opakuje sa rovnaký predregistrovaný beh | import overovať rovnakým spôsobom, akým sa skript reálne spúšťa; `py_compile` importy nerieši |
| PF-037 | 235, prvý P3 beh | `KeyError: 'x=-16.0'` pri skladaní checkpointovej tabuľky | `integrate_samples` zoradil ciele opačne vzhľadom na smer spätnej integrácie; po `x=-18` už nebolo možné zapísať skoršie minutý `x=-16` | nie; A1 trajektória síce bežala, ale skript skončil pred verdictom a pred immutable JSON | zoradenie zmenené tak, aby `pop()` navštevoval `-2,-4,...,-18`; opakuje sa identická P3 brána | pri spätnej integrácii testovať poradie checkpointov na aspoň troch cieľoch a pred verdictom vyžadovať úplnosť množiny checkpointov |
| PF-038 | 237, prvý L1 source audit | falošný nález `U_c` v K7 legacy | audit hľadal podreťazec `uc`, ktorý sa objavil v slovách ako `success` a `structural`, nie ako Python identifikátor | nie; išlo iba o statické čítanie zdrojov a výsledný JSON má verdict STOP | kontrola zmenená na regex s hranicami Python identifikátora; opakuje sa tá istá predregistrovaná L1 mapa | source audity musia rozlišovať identifikátory od voľného textu; pri kritickej premennej ukázať presné zhody |
| PF-039 | 239, prvý L2-B2 source audit | falošný STOP test-field klasifikácie pre skript 85 | scope matcher poznal iba doslovné „fixed metric"/„no back-reacted", hoci 85 ekvivalentne deklaruje „cannot close G7" pre chýbajúce back-reacted constrainty | nie; iba statické čítanie, bez importu alebo ODE; immutable STOP JSON ostáva zachovaný | rovnaký audit sa opakuje do nového `RERUN1` JSON po úzkom rozšírení explicitnej scope frázy | pred použitím scope regexu vyžadovať pozitívne fixtures pre všetky predregistrované varianty slovnej deklarácie; neinterpretovať STOP matcheru ako fyzikálny STOP |
| PF-040 | 239, L2-B2 RERUN1 | neúplné kritérium triedy „full early system" | predregistrácia vyžadovala `U_d`, ale kontrolný súčet overoval pri 66 iba `U_c` a constraint; export ukázal, že 66 `U_d` nemá | nie; iba statické čítanie, RERUN1 JSON ostáva historickým záznamom obmedzenej mapy | 66 sa preklasifikuje na standard/null baseline; nový RERUN2 vyžaduje `U_c`, `U_d` a constraint pre plné kandidáty 89/90 | každá trieda s povinnými prvkami musí mať programovo overený každý prvok; po PASS porovnať exportované polia s vlastnou predregistráciou |
| PF-041 | 241, prvý P5.2 constraint ledger | falošný STOP pri photon-baryon slip definícii | test porovnal voľný symbol `Slip` s jeho definíciou bez substitúcie, preto správne vrátil nenulový rozdiel `Slip+U_b-U_gamma` | nie; šlo o symbolický ledger bez ODE; immutable STOP JSON ostáva zachovaný | nástupca použije dosadenie definície a samostatný test rozdielnosti `U_gamma`,`U_b`; nový výstup je RERUN1 | pri testovaní definície vždy odlíšiť voľnú rovnicu od rezídua po dosadení a exportovať obidva tvary |
| PF-042 | 243, prvý P5.3b seed ledger | `TypeError: cannot determine truth value of Relational` | všeobecná symbolická nerovnosť `8-6 delta>0` nemala deklarovaný rozsah `delta`, hoci A1-K1 ho má zmrazený | nie; skript spadol pred JSON výstupom a bez ODE | nerovnosť sa zopakuje na `delta=0.02297`, algebraické identity ostávajú všeobecné | pri symbolickej nerovnosti explicitne uviesť fyzikálny interval alebo zmrazený vstup; nenechať SymPy implicitne rozhodovať relačný objekt |
| PF-043 | 248, P5.3g1 prvý source audit | falošný negatív pre BR2-90 `l=1` rovnicu | doslovný marker vyžadoval `2.0*f[2]`, zatiaľ čo ekvivalentný zdroj používa `2*f[2]` | nie; išlo o source/provenance audit bez ODE, JSON ostáva historickou stopou | 248 je neúplný source výstup; nástupca 249 normalizuje whitespace aj numerické literály, ale nemení samostatný blokér `F1=qnu` | kritické source porovnanie normalizovať cez AST alebo významový regex a pred behom overiť všetky známe ekvivalentné formy |
| PF-044 | 251, P5.3g3 prvá derivácia `F2` | formula-lineage chyba: kandidát použil pomocnú `tn`, nie návratovú veličinu `qn=4 tn/(3k)` zo skriptu 84 | ručný prepis lower seedov zastal pred konverziou na vrátený vektor; nezávislá sémantická kontrola odhalila nefyziologickú `q` závislosť NIV | nie; bez ODE, kandidát nie je fyzikálny výsledok | JSON 014 a 251 sú `DO_NOT_USE_FORMULA_INPUT`; nástupca musí použiť explicitne `qn` a zdrojový hash | pri prenose funkcie do symbolického ledgeru mapovať každý pomocný symbol až po return vektor; overiť jednotky/škálovanie na aspoň jednom mode |
| PF-045 | 252, P5.3g3a prvý sémantický audit | falošný blokér z požiadavky presnej invariancie `eta` pri fixnom `k tau` | pri zmene `k` sa mení `Omega_m tau`; materiová korekcia `eta` preto nemusí byť presne rovnaká, hoci vedúci rad je | nie; zdrojová sonda bez ODE, JSON ostáva historický | 252 je `DO_NOT_USE_FOR_SEMANTIC_STOP`; nástupca testuje iba skutočný návratový `qn` a explicitne oddelí materiové korekcie | pri fixed-`k tau` škálovaní deklarovať, ktoré subleading premenné závisia od `tau`; nežiadať presnú invarianciu mimo radiation-leading limitu |

| PF-046 | Q22a validačný read-only príkaz | falošný `Missing` pri kontrole SK/EN registra | kontrola použila historicky nesprávny názov `05c_..._SK.md`; skutočný SK súbor je `05c_..._v3.18_ADDENDUM_SK.md` a EN analóg | nie; príkaz skončil pred obsahovou kontrolou, žiadny súbor sa nemenil | technicky mŕtvy iba validačný príkaz; druhý príkaz použil presné cesty a potvrdil zrkadlenie Q18 | pre oba jazykové registre najprv získať presné názvy cez `rg --files`; absenciu cesty nikdy neinterpretovať ako absenciu fyzikálneho záznamu |
| PF-047 | prvý odkaz M0 do Q22a track mapy | `apply_patch` nenašiel viacriadkový kontext | patch predpokladal zalomenie vety po „zrýchlenú fázu“, ale skutočný Markdown mal vetu v jednom odseku | nie; `apply_patch` fail-closed nezapísal nič | technicky mŕtvy prvý patch; druhý patch s načítaným presným rozsahom prešiel | pred patchom existujúceho textu vždy načítať presné riadky cieľa; nespájať zobrazené zalomenie terminálu so skutočným zalomením súboru |
| PF-048 | Q22a SK/EN validačný príkaz pre deriváciu funkcie | falošný `VALIDATION_FAILED` pre SK dokument | spoločný zoznam markerov použil anglické frázy `one trajectory`, `non-empty family` a `empty set` aj pre slovenský dokument | nie; išlo o read-only validáciu a žiadny fyzikálny výpočet ani zápis sa neuskutočnil | prvá kontrola je technicky mŕtva; opakovanie používa samostatné SK a EN markery | pri dvojjazyčnej validácii mať explicitne oddelené jazykové fixtures; anglický marker nesmie overovať slovenský preklad |
| PF-049 | Q22a P1–P5 work-plan validácia | falošný `WORK_PLAN_VALIDATION_FAILED` pre SK plán | kontrola znovu prevzala anglické poradie slov `P1 STOP`, kým slovenský plán používa ekvivalent `STOP P1` | nie; read-only kontrola skončila bez zmeny plánu či fyzikálneho stavu | prvá kontrola je technicky mŕtva; opakovanie používa jazykovo presný marker | v SK/EN validačných fixtures kontrolovať významovo správny preklad aj poradie slov, nie mechanicky zdieľaný token |
| PF-050 | P1.1 source-map validácia | falošný `P1_1_VALIDATION_FAILED` na SK marker | kontrola hľadala nesprávny pád „P2-ready kandidáta“, kým audit správne uvádza „P2-ready kandidátov“ | nie; read-only validácia bez výpočtu a bez zmeny fyzikálneho záveru | prvá kontrola je technicky mŕtva; opakovanie používa presný marker z uloženého auditu | validačný fixture odvodiť z prečítaného obsahu alebo použiť stabilný status token, nie ručne skloňovanú opisnú frázu |
| PF-051 | P1.1 source-map druhá validácia a oprava PF-050 | opakovaný falošný `P1_1_VALIDATION_FAILED` | PF-050 nesprávne predpokladal, že audit obsahuje alternatívny pád opisného markeru; audit má iba stabilné statusy a vetu o piatich P1 poliach | nie; read-only validácia, audit ani fyzikálny verdikt neboli prepísané | PF-050 zostáva historickou stopou neúspešnej opravy; tretia kontrola používa iba `P1.1 COMPLETE; P1 STOP` a „Žiadny kandidát nemá všetkých päť P1 polí“ | pri oprave validačného markeru najprv zobraziť jeho reálne zhody; status tokeny sú vhodnejšie než opisné jazykové frázy |
| PF-052 | P1.2 extended-corpus validácia | falošný `P1_2_VALIDATION_FAILED` na dvoch opisných markerov | kontrola vyžadovala celé vety, ktoré Markdown zlomil do susedných riadkov a plán formuloval „P1 STOP je tým potvrdený v prehľadanom relevantnom korpuse“ s iným medzitextom | nie; read-only kontrola bez výpočtu a bez zmeny P1 verdictu | prvá kontrola je technicky mŕtva; nástupca overuje stabilné statusy, názvy auditov a SK/EN Q18 scope | pri dlhom Markdown texte nepoužívať doslovné viacslovné vety citlivé na zalomenie; validovať krátky status token a samostatne existenciu odkazu |
| PF-053 | 255 / RUN_KMPC_018 P5.3g4 | formula-provenance scope error: k synchronnému photon `F_gamma2` drive bol bez gauge mosta pridaný symbolický CAMB `shear` | runner zmiešal správny MB collision blok so shear termom z odlišného symbolického rozhrania; nulové algebraické rezíduum preto neoveruje fyzický synchronný seed | iba algebra `C X + epsilon D=0`; nie fyzikálny photon seed ani ODE | JSON 018 ostáva immutable `ALGEBRA_PASS_COLLISION_BLOCK`; fyzikálny seed verdict je `REVIEW_GAUGE_BINDING`; nástupca 257/P5.3g6 musí najprv uzavrieť gauge mapu | pri skladaní rovníc z rôznych zdrojov povinne exportovať metric/gauge basis každého symbolu a vyžadovať presnú mapu pred kombinovaním členov |
| PF-054 | 257 / RUN_KMPC_020 P5.3g6 | falošný STOP na marker `legacy73_lower_photon_equation_omits_metric_source` | runner hľadal photon lower equation v Python skripte 73, ale tá je uložená v sprievodnom audite `Audit/A2_K4_3B_HIERARCHY_MODE_TAXONOMY_RECOMBINATION_AUDIT.md` | algebraické mapovanie sa vykonalo a prešlo; JSON 020 však je fail-closed a nie je autoritatívny | 257/020 sú zachované ako technická stopa; jeden nástupca 260 zmení iba správny zdroj markera | pri provenance markeri najprv overiť, či je tvrdenie v zdrojovom `.py`, alebo v jeho auditnom `.md`; cestu exportovať spolu s markerom |
| PF-055 | 261 / prvý KMPC-022 M3-TCA0 beh | `TypeError: Object of type bool is not JSON serializable` po zostavení payloadu | aspoň jedna porovnávacia hodnota ostala `numpy.bool_`; smoke test pokrýval iba symbolické natívne booleany a neotestoval plný vnorený payload | matice mohli prebehnúť, ale neexistuje immutable JSON ani vedecký verdict; výstupná cesta ostala neprítomná | pôvodný runner hash `6f7499...6846b` je `DO_NOT_RUN_TECHNICAL`; RERUN1 pridáva iba rekurzívnu konverziu `np.generic.item()` a zachováva rovnaký base hash `5a89cf...b7ae` | každý nový plný payload pred prvým vedeckým behom previesť rekurzívne na natívne typy a JSON-serializovať v behaviorálnom smoke fixture, nie iba v úzkom symbolickom smoke teste |
| PF-056 | 261/KMPC-023 RERUN1 + `mode_resolved_puiseux.py` V1 | formula-väzbová chyba: všetkých 15 štandardných seedov malo `rank=76/77`; M1 amplitúda zlyhala, hoci driver rezíduá boli `~1e-14` | prijatá M1 normalizačná kotva sa vypočítala až po `lstsq` ako post-check a nevstúpila do určujúcej sústavy; porušenie existujúceho AR50 | algebra a matice áno, ale frakčné holdouty nie sú fyzikálne interpretovateľné nad neukotveným štandardným členom | RERUN1 a V1 sú `RUNNABLE_REVIEW_ONLY`; posledný RERUN2 použije tvrdú elimináciu M1 stĺpca bez zmeny fyziky | pred solve programovo overiť, že každá presná kotva je eliminovaná alebo tvrdou rovnosťou v určujúcej matici; plná hodnosť sa kontroluje po odstránení kotiev |
| PF-057 | KMPC-023 RERUN1 JSON | embedded pole `test` uvádza stale `KMPC-022`, hoci runner, filename a source hash sú KMPC-023 | RERUN1 prevzal label z base návratového payloadu a po serializačnej oprave ho neprepísal | áno; identitu vykonaného zdroja jednoznačne určujú cesta a SHA, takže výsledok sa neruší, ale label je zavádzajúci | immutable JSON ostáva s auditným vysvetlením; RERUN2 musí prepísať vlastný test/run ID a exportovať V1 aj overlay hash | smoke/gate musí vyžadovať rovnosť CLI run ID, embedded test ID, output basename a manifestovanej source identity |
| PF-058 | KMPC-023/024 + V1 frakčný M3 solver | contract-parity chyba: runner deklaroval úplný P5 seed, ale matica mala iba 11 premenných a vynechala dynamické `delta_f,U_f` aj `fuel_continuity/fuel_Euler` | vedúci formula PASS P5.3d bol neoprávnene povýšený na pevnú celú frakčnú vežu; kontrola počtu stavov porovnala maticu iba so svojím lokálnym `VARS`, nie s nadradeným P5 kontraktom | áno; výsledok je platný iba pre neúplný ansatz a jeho nenulové holdouty nesmú zabiť K4 | KMPC-023/024 a V1 sú `DO_NOT_USE_PHYSICS`; V2 ostáva použiteľný iba na M1 anchor; ďalší runner zakázaný do architektonického auditu úplného stavu | pred implementáciou generovať state/row manifest z nadradeného kontraktu a fail-closed porovnať presnú množinu; lokálne `rank==unknowns` nikdy nenahrádza parity kontrolu povinných druhov a rovníc |
| PF-059 | V2 M1 overlay, guard pred monkeypatchom | podmienka `original_solver is not v1.solve_standard_seed` je tautologicky false bezprostredne po priradení | guard porovnáva objekt s tou istou aktuálnou referenciou, nie s očakávaným symbolom/hashom V1 | áno; M1 eliminácia a exportované source hashe ostávajú platné, guard však neposkytuje deklarovanú ochranu | V2 ostáva `M1_ANCHOR_ONLY`; budúci modul musí overiť explicitný očakávaný callable/source hash pred overlayom | každý identity guard musí mať nezávislý frozen expected objekt/hash a negatívny smoke fixture |
| PF-060 | KMPC-023/024 `two_start_power` | názov a brána predstierajú dva štarty, ale kód iba dvakrát vyhodnotí ten istý konečný Puiseuxov rad a normu porovná s jednou mocninou | algebraická diagnostika bola pomenovaná ako štartovací/konvergenčný test; pri NID/NIV sa mieša viac mocnín a shallow `z` dosahuje približne 2.31/6.93 | áno; výsledok je iba leading-power/truncation diagnostika, nie nezávislý fyzikálny FAIL | immutable JSON sa nemení; autoritatívny audit zúžil význam, budúci skutočný two-start test patrí až ODE/evolúcii | názov kontroly musí zodpovedať vykonanej operácii; two-start vyžaduje dve nezávislé integrácie a asymptotické plochy `z<<1` |

**Opakovanie známej PF-011/PF-016 (2026-07-16):** pri read-only
PowerShell sumarizátoroch sa trikrát znovu použil priamy `foreach {...} |
Format-*`. Parser zastal pred čítaním výsledku a nič nezapísal. Nezakladá sa
nové PF číslo, lebo koreň aj prevencia sú totožné: výstup cyklu sa vždy
najprv uloží do `$rows` a až potom sa samostatne pošle do pipeline.

## Dodatok PF-061

| ID | Skript/beh | Kategória a symptóm | Koreňová príčina | Vykonaná fyzika? | Stav a nástupca | Povinná prevencia |
|---|---|---|---|---|---|---|
| PF-061 | 262 / K11-CS2 S0 RUN-001 | base dokončil 36/36 exact checks a zapísal JSON za 1.125 s, ale vonkajší shell nepozoroval exit do 10 s a ukončil bunku kódom 124 | presná lifecycle príčina nie je dokázaná; bezprostredne po zápise runner duplicitne tlačil celý payload na stdout a capture/exit cesta sa nevrátila, hoci po timeout-e nezostal Python proces | iba exact algebra; žiadna ODE ani fyzikálna evolúcia | RUN-001 je `REVIEW_EXTERNAL_EXIT_TIMEOUT`; 262 `DO_NOT_RUN_TECHNICAL`; 263 mení iba output na stručný flush a vytvorí nový immutable JSON | veľký payload pri `--output` neduplikovať na stdout; vždy vyžadovať zároveň vnútorný runtime aj úspešný vonkajší exit, úplný súbor sám nestačí |

## Dodatok PF-062

| ID | Skript/beh | Kategória a symptóm | Koreňová príčina | Vykonaná fyzika? | Stav a nástupca | Povinná prevencia |
|---|---|---|---|---|---|---|
| PF-062 | K11-CS2 S0 base + 263/RUN-002 | state-contract false PASS: 36/36 checks zahŕňalo počty 27/35/43, ale register mal nadbytočné `E_gamma_0,E_gamma_1` | lokálny register vytvoril CAMB E-mode multipóly od 0, hoci `E_eq(2)` začína reťazec pri `E_2`; count test porovnal register iba s vlastnou chybnou formulou `4l+11`, nie s nadradenou presnou množinou stavov | iba exact algebra, bez ODE; CAMB J/G/E koeficientové identity ostávajú platné | v001 `PASS_FORMULA_IDENTITIES_ONLY / STOP_STATE_REGISTER`; 263 `RUNNABLE_REGRESSION_ONLY`; full v002 opraví state set na `E_2...`, count `4l+9` ako technická oprava 2/2 | state parity kontrolovať presnou množinou voči nadradenému kontraktu a pridať negatívny fixture pre zakázané extra stavy; lokálny count/unique test sám nikdy nie je parity dôkaz |

## Mapovanie starého capu 2/2 na cap 10

- P5.3g7-M3: KMPC-022/023/024 sa konzervatívne počítajú ako spoločné
  technické pokusy `1–3/10`; úplný R-A preflight bude pokus `4/10`.
- K11-CS2: PF-061/PF-062 uzavreli neúplnú S0-v001 architektúru. Full v002
  má odlišný presný state kontrakt a vlastný ledger `0/10`.
- Counter sa nesmie vynulovať premenovaním alebo patchom rovnakého runnera.
  Nulovanie vyžaduje preukázateľne inú technickú architektúru a rozdielový
  audit príčiny. Ani jeden technický incident nie je fyzikálny pokus.

## Dodatok PF-063

| ID | Skript/modul | Kategória a symptóm | Koreňová príčina | Vykonaná fyzika? | Stav a nástupca | Povinná prevencia |
|---|---|---|---|---|---|---|
| PF-063 | `mode_resolved_puiseux.py` V1 a V2 M1 overlay/KMPC-023/024 | fuel pressure source použil `delta_f+9delta(2-delta)U_f+3gamma(2-delta)U_f`, teda trojnásobok správnej neadiabatickej časti | koeficienty `9delta` a `3gamma` z fuel continuity boli prenesené do pressure ratio; kovariantne konzervovaný script 88 pri rovnakej U-konvencii vyžaduje `delta_f+(2-delta)(3delta+gamma)U_f` | matice áno, ale frakčné trace/holdouty nie sú autoritatívnym testom správneho tlaku | legacy V1/V2 ostávajú `DO_NOT_USE_PHYSICS` pre M3; M1 anchor a k-cancel scope sa nemení; R-A B1 používa tlak zo scriptu 88 | tlak odvodiť zo zvoleného `c_s^2,c_a^2,Q^mu` a overiť total-energy aj total-momentum product-rule left-null pred vložením do Einstein trace |

## Dodatok PF-064

| ID | Skript/modul | Kategória a symptóm | Koreňová príčina | Vykonaná fyzika? | Stav a nástupca | Povinná prevencia |
|---|---|---|---|---|---|---|
| PF-064 | 264/KMPC-025 `full_ra_b1_preflight.py` | raw `15/15` napriek tomu, že exact state guard overoval iba count/unique a negatívne fixtures iba `candidate !=` lokálny `STATE` | lokálny manifest auditoval sám seba; chýbal nezávislý contract modul a spoločná validačná funkcia pre implementáciu aj negatívne fixtures | iba exact algebra, bez solve/ODE; algebraické left-null nuly zostávajú platné | `PASS_ALGEBRA_SCOPE / STOP_CONTRACT_GUARD`; 264 a JSON zachovať; pokus 5 použije samostatný contract a fail-closed validator | exact-set parity vždy porovnať s nezávislým nadradeným tuple; všetky negatívne fixtures musia prejsť tou istou validačnou cestou ako produkčný manifest |

## Dodatok PF-065 až PF-067

| ID | Skript/modul | Kategória a symptóm | Koreňová príčina | Vykonaná fyzika? | Stav a nástupca | Povinná prevencia |
|---|---|---|---|---|---|---|
| PF-065 | 266/268 K11-CS2 full-v002 attempts 1 a 3 | payload checks PASS a internal runtime pod limitom, ale celý proces skončil external timeout 124 | interný timer začal až po ťažkom CAMB/SymPy importe; súčet import overheadu a auditu prekročil 10 s | iba structural algebra/source parity; bez ODE | attempts 1/3 diagnostické, nie autoritatívne; attempt 4 prešiel na lightweight source-AST architektúru | internal runtime musí pokrývať aj import alebo sa musí reportovať samostatný process-wall budget; pred full sweepom zmerať cold import a neštiepiť beh na shard, ak overhead dominuje |
| PF-066 | 267 K11-CS2 attempt 2 L4 | správne checks a exit 0, ale JSON niesol stale verdict `ATTEMPT_1` | číslo pokusu bolo zakódované v zdieľanom base verdict stringu | iba structural algebra; bez ODE | attempt 2 zastavený po L4, L6/L8 nebežali; attempt 3 oddelil generický scope verdict od `technical_attempt` | base verdict nesmie obsahovať číslo orchestration pokusu; ordinal, run ID a fyzikálny scope sú samostatné polia a negatívny fixture odmietne stale ID |
| PF-067 | `a2_k11_cs2/__init__.py` pri runneri 269 | lightweight AST audit mal internal 0.047 s a 55/55, no wall skončil timeout 124 | package initializer eager importoval legacy `full_multispecies_constrained_dae` a tým CAMB/SymPy ešte pred ľahkým submodulom | žiadna nová fyzika; source-AST kontrakt sa vypočítal | attempt 4 diagnostický; lazy `__getattr__` init + runner 270 prešli attempt 5 za ~1.5 s wall | package `__init__` nesmie eager importovať voliteľné heavy backendy; ľahké contract/source moduly musia mať cold-import smoke a recorded init hash |

## Dodatok PF-068

| ID | Skript/modul | Kategória a symptóm | Koreňová príčina | Vykonaná fyzika? | Stav a nástupca | Povinná prevencia |
|---|---|---|---|---|---|---|
| PF-068 | 271/KMPC-027 attempt 6 | AD full-mode shard prekročil interný limit 4.8 s počas zostavovania extended holdout matice; failure JSON pozná iba mód, nie aktuálny `k/variant` | jeden proces zoskupil 3 k × 3 varianty × primary/J+2; smoke jedného primary solve nebol dostatočný wall-work odhad; exception context neexportoval vnútorný subshard | smoke vykonal úzky AD nominal primary algebraický solve 12/12, ale plný AD verdict nevznikol; žiadna ODE ani fyzikálny pokus | attempt 6 `TECHNICAL_TIMEOUT`; 271 `DO_NOT_RUN_FULL_MODE / SMOKE_REGRESSION_ONLY`; pokus 7 smie iba shardovať po `mode×k×variant` s rovnakou fyzikou | runtime predregistráciu odvodiť z počtu solve blokov; každý proces má mať jeden auditný atóm a failure payload musí niesť mode/k/variant/last_completed_phase |

## Dodatok PF-069

| ID | Skript/modul | Kategória a symptóm | Koreňová príčina | Vykonaná fyzika? | Stav a nástupca | Povinná prevencia |
|---|---|---|---|---|---|---|
| PF-069 | 276/KMPC-032 `s_c0_coefficient_passport.py` | `TypeError: invalid input: np.float64(...)` pri prvom skutočnom M1 koeficiente | helper `_q` rozpoznal numpy skalár ako `float`, ale použil `repr(value)`, ktorý zachoval textový wrapper `np.float64(...)`; `SymPy Rational` prijíma číselný text, nie konštruktorový výraz | nie; hash/contract/smoke prešli, ale audit zastal pred prvou S-C0 identitou a vytvoril iba failure JSON SHA `51C7B3...1EA03` | 276 a V1 hash ostávajú `DO_NOT_RUN_AUDIT_TECHNICAL`; úzky verzovaný overlay zmení iba konverziu konečného `numbers.Real` na `repr(float(value))` | pred plným auditom musí behaviorálny smoke obsahovať natívny `float` aj `numpy.float64`; pri numerických skalároch najprv overiť konečnosť po explicitnej konverzii na builtin typ |

## Dodatok PF-070 a PF-071

| ID | Skript/balík | Kategória a symptóm | Koreňová príčina | Vykonaná fyzika? | Stav a nástupca | Povinná prevencia |
|---|---|---|---|---|---|---|
| PF-070 | externý balík `EA-20260717-003` / runner 279 | smoke aj official audit skončia na chýbajúcom `RUN_KMPC_034...json`; cieľový T2 nie je z balíka dosiahnuteľný | package closure zachytil jedenásť Python importov, ale nie runtime-opened immutable regresný JSON, hoci ho `run_smoke` aj `run_audit` povinne hashujú | nie v oficiálnej vetve externého balíka; auditor urobil iba deklarovanú direct-solver odchýlku | balík 003 ostáva immutable a `T2_UNCLOSED_DELIVERY`; náprava je nový balík `EA-20260717-005` | každý balík má `04_RUNTIME_DEPENDENCY_MAP.tsv`; package preflight overí importy aj každý JSON/config/data vstup v presnej runtime ceste pred stavom READY |
| PF-071 | runner 279 `_write_atomic_exclusive` | pri publish kolízii po vytvorení temp súboru môže `os.link` zlyhať a ponechať `.tmp-KMPC-035` | cleanup nasleduje až po úspešnom `os.link`, nie v `finally`; chýbal negatívny race/collision fixture | nejde o fyziku; kanonický cieľ sa neprepíše, ale hygiena failure vetvy je neuzavretá | historický runner 279 sa nemení; package-local nástupca EA-005 používa `try/finally` a collision fixture | každý exclusive publish musí kontrolovať cieľ pred drahým behom, odstraňovať iba vlastný temp v `finally` a mať fixture, ktorá vytvorí kolíziu medzi temp write a linkom |

## Dodatok PF-072

| ID | Skript/beh | Kategória a symptóm | Koreňová príčina | Vykonaná fyzika? | Stav a nástupca | Povinná prevencia |
|---|---|---|---|---|---|---|
| PF-072 | 281 / KMPC-037 V3 same-matrix 80-dps solve | `mpmath.qr_solve` po úspešnom preflighte skončil `ValueError: matrix is numerically singular`; failure JSON SHA `7F1B5B...315E1` | malý 3×2 QR smoke overil iba API, nie numerickú životaschopnosť zmrazenej 121×98 matice; presná príčina singularity v ne-pivotovanom mpmath QR ešte nie je uzavretá | V0–V2 sa mohli interne vypočítať, ale runner skončil pred payloadom a nič z nich nie je autoritatívny fyzikálny výsledok | 281 a base hash `CE2922...7A80C` sú `DO_NOT_RUN_TECHNICAL`; KMPC-036 REVIEW ostáva bez zmeny; dovolený je najprv read-only diagnózny audit algoritmu a až potom nový predregistrovaný nástupca | high-precision smoke musí prebehnúť na presnej zmrazenej matici alebo na jej uloženom decomposition passe; API smoke malej plnohodnostnej matice nestačí |

## Dodatok PF-073

| ID | Skript/beh | Kategória a symptóm | Koreňová príčina | Vykonaná fyzika? | Stav a nástupca | Povinná prevencia |
|---|---|---|---|---|---|---|
| PF-073 | 282 / KMPC-038 smoke | `AttributeError: module 'mpmath' has no attribute 'householder'`; failure SHA `E85E6C...DA64F` | overlay cielil exportný modul `mpmath`, hoci interná Householder callable je metóda kontextu `mpmath.mp`; statická kontrola zdroja neoverila runtime owner objekt | nie; compile/help a runner fixtures prešli, base smoke zastal pred zero-diagonal solve a plný audit sa nespustil | 282 a v2 overlay sú `DO_NOT_RUN_TECHNICAL`; jediný nástupca smie zmeniť owner na `mp.mp.householder` a musí ho overiť v smoke pred auditom | pri monkeypatch/context overlayi smoke musí overiť existenciu, owner, bound `__self__`, modul/názov callable a úspešné obnovenie presne na runtime objekte, ktorý volá knižničná metóda |

## Dodatok PF-074

| ID | Skript/beh | Kategória a symptóm | Koreňová príčina | Vykonaná fyzika? | Stav a nástupca | Povinná prevencia |
|---|---|---|---|---|---|---|
| PF-074 | 289 / KMPC-045 BI support step 3 | audit po support solve zastal na `AttributeError: bi_c1_coverage` nemá priamy `_s_c0_actual_coefficient_guard`; následný stderr print vyvolal `NameError: sys is not defined` | BI wrapper vlastní helper cez explicitný owner chain `bi_c1_coverage.c1`, ale nový step-3 kód použil neoverený priamy export; runner zároveň nepokryl skutočnú exception-report vetvu behaviorálnym smoke | čiastkové solve vznikli iba v pamäti, ale audit nedokončil S-C0/core/tail payload a canonical JSON nevznikol; nič sa fyzikálne neinterpretuje | 289 a base SHA `1ABB16...36CC8` sú `DO_NOT_RUN_AUDIT_TECHNICAL`; failure JSON SHA `FFFF0616...330C01` ostáva immutable; KMPC-046 smie opraviť iba owner bridge a import `sys` | pri helperi prenášanom wrapperom smoke musí overiť presný owner chain a obnovu bridge; runner smoke musí priamo serializovať a smerovať syntetickú failure správu cez ten istý stderr objekt ako reálna exception vetva |
