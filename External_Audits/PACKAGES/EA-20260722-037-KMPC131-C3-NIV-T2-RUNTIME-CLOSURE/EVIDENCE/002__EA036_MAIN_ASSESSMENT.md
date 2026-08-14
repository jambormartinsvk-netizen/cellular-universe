# Hlavný posudok externého auditu EA-036

**Dátum:** 2026-07-22  
**Externá odpoveď:** `00_AUDITOR_AUDIT.md`  
**SHA-256 externej odpovede:**
`2D34CD6659E26134C697A79553374305F70AA10D53666727645D7882ED759746`  
**Auditor:** nezávislý Codex audit agent / GPT-5 family  
**Obmedzenie nezávislosti:** samostatný agent a fresh runtime, ale rovnaká
platformová rodina; používateľ túto náhradu externého auditora výslovne
povolil, lebo iná možnosť nebola dostupná  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Autorita spracovania:** hlavný orchestrátor  
**Výsledok spracovania:** `ACCEPTED_AGREE_WITH_LIMITATION_T1`

## 1. Autoritatívny rozsudok

```text
PACKAGE_DECLARED_MANIFEST = PASS_31_OF_31
PACKAGE_PREFLIGHT_LEGACY = PASS_221_OF_221
PACKAGE_RUNTIME_CLOSURE = FAIL_MISSING_2_HARDCODED_HASH_INPUTS
KMPC131_NIV_K0P15_TIER = T1_PRIMARY_RAW_FORENSICS
EXTERNAL_RECOMMENDATION = AGREE_WITH_LIMITATION
PROJECT_NIV = 7_OF_9_PASS_UNCHANGED
GLOBAL_C3 = 43_OF_45_PASS_UNCHANGED
K4_DEPTH = 60_OF_100_UNCHANGED
PHYSICS_STOP = NONE
REFINEMENT_AUTHORIZATION = NOT_YET_OPEN
```

Externý posudok sa prijíma v T1 rozsahu. Potvrdzuje, že existujúci raw
lokalizuje REVIEW na štyri M3 driver numerical boundaries a nepodporuje
fyzikálny STOP. Neprijíma sa pôvodné tvrdenie, že EA-036 je úplná T2
kapsula. Dva posledné NIV atómy preto ostávajú REVIEW a nijaký PASS sa
nepridáva.

## 2. Prijaté výsledky

1. Manifestová source/copy parita prešla `31/31`; pôvodný package po audite
   stále prechádza svojím historickým preflightom `221/221` a zostal
   byteovo nezmenený.
2. Fresh compile, help a smoke prešli; smoke mal `4/4` receipts, nevykonal
   fyziku a nevytvoril raw.
3. Official vetva fail-closed skončila pred fyzikou, pretože runtime kapsule
   chýbali dva exact-hash vstupy: script 88 a M1 source-map 26.
4. Oba samostatné missing-nominal a missing-aggregate guardy prešli
   fail-closed bez fyziky a outputu.
5. T1 forenzná kontrola potvrdila plný rank `104/104` a `130/130`, štyri
   M3 driver residualy nad `1e-10` a všetky štyri independent holdouty pod
   `1e-9`. Common, tail, background, M1, null-limit a frozen kontrakty
   prešli.
6. Nepravdivý af0 audit bridge je odvodený z refined nominal verzus
   nerefinovaný C3 solve; nie je nezávislým fyzikálnym nálezom.
7. Úzky successor musí pokryť kartézsky súčin
   `gamma0+af0 × rank 104+130`, zachovať maticu, RHS, support
   `[-1,6]→[-1,8]`, M1 depth 8, nominal autoritu a všetky prahy.

## 3. Spracovanie nálezov

| ID | Spracovanie | Povinná náprava |
|---|---|---|
| F-001 | `ACCEPTED_MATERIAL` | Nový versioned balík musí priložiť exact-hash `scripts/88_script_A2_K4_3b_RG_BR1_synchronous_Einstein_and_transfer_ledger.py` a `tracks/.../26_P5_3G7_M1_STANDARD_METRIC_SOURCE_MAP_SK.md`, zaradiť ich do manifestu/runtime mapy a overiť official vetvou. EA-036 sa nemení. |
| F-002 | `ACCEPTED_MATERIAL` | Fresh parity kontrakt musí vopred pomenovať aj vnorený `frozen_B1_left_null_Bianchi.runtime_seconds` a absolútny koreň `frozen_algebra_source`; pri ceste sa zachová exact relatívny suffix a SHA zdroja. Fyzikálne polia sa normalizovať nesmú. |
| F-003 | `ACCEPTED_PROCESS_DEFECT` | Preflight sa rozšíri o exact coverage všetkých fyzických súborov pod `REPRO/` a o statickú kontrolu lokálnych ciest deklarovaných v source hash mapách. Historické `221/221` preto nie je dôkaz runtime úplnosti. |

Nálezy nemenia fyziku, ale blokujú T2 a tým aj otvorenie refinementu podľa
predregistrovaného handoffu 237.

## 4. Agentová nezávislosť

Audit vykonal oddelený agent s vlastným procesným ledgerom, fresh
dočasnými kópiami a výhradným vlastníctvom response súboru. Hlavný
orchestrátor mu neposkytol výsledkovú úpravu ani nezapisoval response.
Keďže ide o rovnakú modelovú/platformovú rodinu, posudok sa nepovyšuje na
T3 ani na úplne nezávislú implementáciu. Pre používateľom povolený
náhradný externý posudok je táto hranica explicitná a prijatá.

## 5. Stav a ďalší postup

- NIV ostáva `7/9 PASS`; `NIV/.15/gamma0` a `af0` ostávajú REVIEW;
- globálne C3 ostáva `43/45 PASS` a aggregate je zakázaný;
- K4 ostáva živá na `60/100`; prediction table, release a Zenodo sa nemenia;
- najbližší krok je minimálny opravný T2 balík s novým ID, nie nový
  vedecký výpočet;
- refinement možno predregistrovať až po úspešnom T2 posudku opravného
  balíka a bez zmeny frozen rovníc alebo prahov.

Stav EA-036: `ASSESSED_BY_MAIN_ORCHESTRATOR_T1_LIMITATION`.  
Stav projektu: `C3_43_OF_45 / NIV_K0P15_REVIEW / T2_PACKAGE_REPAIR_REQUIRED`.
