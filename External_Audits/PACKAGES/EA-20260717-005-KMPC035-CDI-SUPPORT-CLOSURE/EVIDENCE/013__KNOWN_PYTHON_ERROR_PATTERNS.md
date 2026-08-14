# Známe chybové vzory Python skriptov a povinné kontroly

Dátum: 2026-07-15  
Stav: záväzný checklist pred tvorbou a auditom skriptu

Tento dokument dopĺňa konkrétny incidentový register `00_PYTHON_FORMAL_ERROR_LEDGER.md`. Pred vytvorením nového skriptu a pred auditom starého skriptu sa preveria nižšie uvedené triedy. Nález vzoru nie je automaticky fyzikálny FAIL.

## 1. Syntaxová chyba vo vygenerovanom zdroji

**Príklady:** 118/119.  
**Symptóm:** `SyntaxError`, nezatvorený zoznam/zátvorka; wrapper môže sám kompilovať, ale text, ktorý skladá, nie.  
**Kontrola:** skompilovať finálny vygenerovaný text cez `compile(...)`/`py_compile`, nie iba wrapper. Marker musí mať presne jeden výskyt.  
**Rozsudok:** `DO_NOT_RUN_TECHNICAL`; fyzika sa nevykonala.

## 2. NumPy/SymPy skalár v JSON

**Príklady:** 28, staré revízie 66/67, 91, 93, 101, 120, 183.  
**Symptóm:** `TypeError: ... is not JSON serializable` až po drahom výpočte.  
**Kontrola:** pred fyzikou vytvoriť reprezentatívny output a zavolať `json.dumps`; rekurzívne konvertovať `np.bool_`, `np.integer`, `np.floating` a SymPy booleany na natívne `bool/int/float/str`.  
**Pozor:** úspešný výpočet bez exportu nemá machine verdict.

## 3. Nesprávna markerová cesta alebo nejednoznačný marker

**Príklady:** 133, 163, 173.  
**Symptóm:** marker má 0 alebo viac než 1 výskyt, prípadne wrapper patchuje inú transformačnú vrstvu.  
**Kontrola:** exportovať cestu zdroja, počet markerov, hash pred/po, skompilovať vygenerovaný text a exportovať `executed_path_id`.  
**Oprava:** nový nemenný wrapper; starý sa nemaže.

## 4. Poradie JSON kľúčov zamieňané za poradie stavového vektora

**Príklad:** 179 po `sort_keys=True`.  
**Symptóm:** správna množina stavov je odmietnutá alebo sa vektor zloží v nesprávnom poradí.  
**Kontrola:** overiť `set(payload)==set(NAMES)` a vektor vždy skladať `[payload[name] for name in NAMES]`. Nikdy nepoužívať `tuple(dict)` ako fyzikálne poradie.

## 5. Fail-open porovnanie chýbajúcich polí

**Príklad:** 172/175 rank check.  
**Symptóm:** `mapping.get(a)==mapping.get(b)` dá `True` pri `None==None`.  
**Kontrola:** najprv `a in mapping and b in mapping`, typ, konečnosť/kladnosť a až potom rovnosť. Povinný negatívny smoke-test odstráni každý kľúč samostatne aj oba.

## 6. Nepodporované API alebo slice

**Príklad:** 170, `mpmath.matrix[:, list]`.  
**Symptóm:** runtime `TypeError`, hoci syntax prešla.  
**Kontrola:** minimálny API smoke-test s rovnakým typom objektu; pri mpmath zostaviť explicitnú maticu cez riadky/stĺpce.  
**Pozor:** starý chybný výraz môže zostať v opravenom wrapperi iba ako replacement marker; raw textový linter ho potom nesmie automaticky považovať za vykonanú cestu.

## 7. Jednotková sonda v zle škálovaných súradniciach

**Príklad:** 181.  
**Symptóm:** `e_j` vo fyzikálnej premennej pri škále `S_j~1e-29` vyvolá normalizovanú amplitúdu `~1e29` a safety cap.  
**Kontrola:** pri lineárnom RHS použiť `(f(S_j e_j)-f(0))/S_j`; linearitu najprv overiť zo všetkých rovníc a sledovať stavové ochranné vetvy.

## 8. Tautologický alebo enforced check vydávaný za nezávislý dôkaz

**Príklady:** `rhs[0]-(3D+2s²eta)`, `rhs[1]-M`, self-checky 178 a species spätné skladanie z `D/M`.  
**Kontrola:** každý check označiť `independent_gate`, `enforced_identity` alebo `cancellation_monitor`. Posledné dve kategórie majú `score_effect: NONE`.

## 9. Nedosiahnuteľný legacy kód po skorom returne

**Príklad:** 183–185.  
**Symptóm:** nový blok sa vloží pred starý solver a skončí `return`; text starého solvera ostane ako falošný budúci marker.  
**Kontrola:** samostatná funkcia alebo nový skript; export `executed_path_id`; AST/reachability audit. Marker v nedosiahnuteľnom kóde sa nesmie patchovať.

## 10. Nedokončený súbor bez vstupného bodu

**Príklad:** 186.  
**Symptóm:** syntax môže prejsť, ale `main()` sa nevolá, chýba výstup a súbor končí pokračovacím markerom.  
**Kontrola:** AST entry-point kontrola, `--help` smoke-test, očakávaný minimálny JSON output. Nástupca dostane nové číslo.

## 11. Timeout alebo chýbajúci interný limit

**Príklady:** 45/46/47/51, 107/112, 142–154, 180.  
**Kontrola:** AR29 — externý timeout vždy; kontrola do 10 s; úsek najviac 60 s; dlhší beh segmentovať; nový dlhý skript má `--max-runtime-seconds`, deadline a RHS/iteration cap.  
**Rozsudok:** timeout je `REVIEW/UNCLOSED`, nie fyzikálny FAIL. Opakovať iba pri novej numerickej zmene, nie iba dlhším čakaním.

## 12. Chýbajúci compiler/backend

**Príklady:** 78/105.  
**Symptóm:** symbolická cesta vyžaduje Fortran/C compiler, ktorý prostredie nemá.  
**Kontrola:** dependency smoke-test pred výpočtom; ak existuje auditovaný precompiled output, použiť jeho hashovaný nástupca. Stav je `ENVIRONMENT_BLOCKED`.

## 13. Starý oracle alebo register z iného backgroundu

**Príklady:** legacy shear oracle 121; prepísanie physical-mu registra v 171/172.  
**Kontrola:** každý register nesie producenta, mód, povrch, backgroundové parametre, účel solve a checksum. Referenčný solve nesmie prepísať fyzikálny register.

## 14. Číselná metrika závislá od súradnicovej škály

**Príklady:** envelope Jacobian/SVD 151/152, relatívna chyba pri nulovom signále.  
**Kontrola:** reportovať fyzikálny aj škálovaný operátor, invariantné spektrum, dve FD mierky a absolútny aj relatívny test s activity floorom. Condition proxy pod FD šumovým dnom nemá dôkaznú váhu.

## Povinný rýchly postup

1. skontrolovať `00_DO_NOT_RUN_SCRIPT_REGISTRY.md` alebo checker 188 s `--target`;
2. načítať tento checklist a incidentový ledger;
3. zapísať očakávania podľa AR54;
4. vykonať limitovaný syntax/CLI/JSON/dependency smoke-test;
5. až potom fyzikálny beh;
6. pri chybe aktualizovať ledger aj karanténu pred pokračovaním.
## 15. Marker je hľadaný v nesprávnej generovanej vrstve

**Symptóm:** vonkajší wrapper prejde `py_compile`, ale pri `--help` skončí na `marker is not unique` alebo `count=0`, hoci hľadaný text existuje v logicky očakávanom finálnom skripte.  
**Príčina:** wrapper patchuje text ďalšieho wrappera, nie ešte nevygenerovaný finálny text; compile/exec reťazec má väčšiu hĺbku, než predpokladal autor. PF-012 v skripte 189 patchoval parser vo vrstve 169, pričom parser vznikol až vo vrstve 166.  
**Kontrola:** pred patchom zapísať mapu `vonkajší súbor -> generovaný wrapper -> finálny vykonávaný text`; marker overiť v texte bezprostredne pred konkrétnym `compile/exec`; `--help` musí prejsť celou skutočnou cestou.  
**Rozsudok:** starý wrapper `DO_NOT_RUN_TECHNICAL`; neopravovať potichu, vytvoriť nového číslovaného nástupcu a zachovať marker-path dôvod.

## 16. Auditný balík má import closure, ale chýba runtime dátový vstup

**Príklad:** externý balík 003/KMPC-035 vynechal immutable KMPC-034 JSON,
ktorý `run_smoke` aj `run_audit` otvárajú až za behu.

**Symptóm:** všetky Python moduly a ich hashe sedia, ale oficiálna vetva
skončí `FileNotFoundError` ešte pred interpretovateľným výsledkom.

**Kontrola:** popri import grafe vytvoriť strojový zoznam každého
`open/read_text/json.load/config` vstupu, jeho presnej runtime cesty, roly a
SHA-256. Spustiť `Test-ExternalAuditPackage.ps1` pred zapečatením.

**Rozsudok:** package tier T2 je neuzavretý; direct-solver bypass je iba
deklarovaná odchýlka a nemení fyzikálny verdict.

## 17. Exclusive publish zanechá temp súbor pri kolízii

**Príklad:** runner 279 zapísal temp, potom volal `os.link`, a cleanup bol
vykonaný iba po úspešnom linku.

**Kontrola:** precheck existencie cieľa pred drahým behom; temp názov
vlastnený procesom; `temporary.unlink(missing_ok=True)` vo `finally`;
negatívny fixture musí vyvolať kolíziu po temp write a potvrdiť nezmenený
cieľ aj nulový počet temp súborov.

**Rozsudok:** technická/hygienická chyba bez fyzikálneho dopadu; historický
runner sa neprepisuje a oprava vzniká v novom nástupcovi alebo wrapperi.
