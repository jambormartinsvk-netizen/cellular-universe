# KMPC-140 — read-only agregácia úspešných KMPC-139 workerov

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → BI/.15`  
**Stav:** `PREREGISTERED / INPUT_AND_SOURCE_HASH_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Autorita 45 s:** výslovná voľba používateľa  
**Technický predchodca:** KMPC-139 / PF-125

## 1. Dôvod a rozsah

KMPC-139 vykonal celú predregistrovanú fyziku. Immutable failure receipt
obsahuje štyri úspešné coefficient payloady a dva úspešné 80-dps exact
payloady. Parent zlyhal až po ich dokončení, pretože zdedený KMPC-131
agregátor očakáva historický kľúč `contract_guard`, zatiaľ čo novší worker
publikuje rovnakú položku pod kľúčom `successor_contract_guard`.

KMPC-140 je výlučne read-only publish successor. Nesmie spustiť worker,
coefficient solve, exact solve, CPQR ani inú fyziku. Smie:

1. načítať presne jeden hashovo zmrazený KMPC-139 failure receipt;
2. vyžadovať presnú množinu `4 coefficient + 2 exact` payloadov a šesť
   úspešných process records;
3. overiť run/role/mode/k/variant/support identity, limity, exact owner
   lifecycle, `technical_pass=true` a `exact_boundary_pass=true`;
4. vytvoriť hlboké kópie coefficient payloadov;
5. iba v kópiách doplniť alias
   `contract_guard := successor_contract_guard` a overiť ich rovnosť;
6. zavolať frozen KMPC-137 parent aggregate nad kópiami a pôvodnými exact
   payloadmi;
7. publikovať jeden nový immutable parent raw s úplnou provenienciou.

Child `run_id=KMPC-139` aj worker roly ostávajú pre agregátor zachované.
Iba výsledný parent receipt dostane `run_id=KMPC-140`; zdrojové payloady ani
failure receipt sa nemenia.

## 2. Frozen vstup a implementácia

| artefakt | SHA-256 |
|---|---|
| KMPC-139 failure receipt | `FBACDAB50EAC1D7ADB38104560F04806252E5A2DD19E605289A33B7E35FC334B` |
| frozen KMPC-137 wrapper | `489ED57D2F874CAC60E7733050C7DB4E8D59AABAD197827965F6322B80515D0D` |
| runner 384 | `F2B4D0D377BE437307FA07391619BC7A797B37EE7FC7C8D519D799D7778A5153` |

Prípustná schema transformácia je presne jedna pridaná top-level položka v
každom coefficient payloade. Existujúce hodnoty, polia, listy a mapy musia
ostať nezmenené; normalizačný register musí uviesť štyri aliasy a nulový
počet zmenených existujúcich hodnôt.

## 3. Predbežné očakávanie

Na základe už publikovaných worker dát očakávame:

- `gamma0` exact driver aj non-fit holdout PASS;
- `af0` exact driver aj non-fit holdout PASS;
- obidve nulové varianty a ich BI/.15 pair PASS candidate;
- nulové solver/worker volania v KMPC-140;
- runtime výrazne pod všeobecným `4.8 s` limitom read-only parenta.

Očakávanie nie je verdikt. Autoritatívny BI/.15 a BI-mode verdict smie
prideliť až následný interný audit.

## 4. Fail-closed vetvenie

- hash, schema, identity, process record, exact brána alebo alias nerovnosť:
  nový immutable technical failure, bez verdiktu a bez alternatívneho aliasu;
- aggregate exception: nový immutable technical failure, bez opakovania
  fyziky; ďalší successor smie byť znovu iba úzky read-only adapter;
- aggregate dokončený, ale `pair_pass=false`: REVIEW candidate, bez úpravy
  prahov;
- aggregate dokončený a `pair_pass=true`: PASS candidate, potom povinný
  interný audit celej BI trojice `.005/.05/.15`.

## 5. Povinný preflight

Pred official režimom musí oddelene prejsť compile, `--help` a `--smoke`.
Smoke smie iba načítať a overiť receipt, preukázať presnú schema transformáciu
na kópii a potvrdiť `physics_executed=false`. Source hash runnera sa musí
zapísať do tejto predregistrácie ešte pred prvým Python procesom.

## 6. Súborový rozpočet

Koherentná výpočtová jednotka má presne: jednu predregistráciu, jeden runner
a jeden raw/technical receipt. Interný audit, plán a externý balík sa vytvoria
iba po vecnom uzavretí BI; nový base modul nevzniká.
