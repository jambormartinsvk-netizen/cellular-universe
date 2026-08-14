# Externý audit — EA-034 C3 BI mode closure

## Povinné metadáta

- Auditor/model/verzia: Claude Code / Claude Fable 5 (`claude-fable-5`), Anthropic; externý auditor nezávislý od tvorcu skriptov (Codex/OpenAI)
- Dátum a časová zóna: 2026-07-19, 21:37 (Central Europe Standard Time, UTC+02:00)
- Audit mode: `FORENSIC + REPRODUCTION` (blind nebol možný — auditor pracoval priamo v repozitári; balík aj živé zdroje boli hashovo krížovo overené)
- Package revision a SHA-256 manifestu: `SEALED_READY_FOR_EXTERNAL_AUDIT` (05_PACKAGE_HISTORY.md, 2026-07-19); SHA-256 `01_MANIFEST_SHA256.tsv` = `74BCE72D4D3CFC1AA7068EA36F93B600F00A1659E8D23B8768E664198A0868EB`
- Overenie manifestu: `PASS` — 21/21 položiek nezávisle prepočítaných (copy hash, source hash aj copy==source parita), runtime mapa 2/2, duplicitné fyzické hash skupiny v balíku: 0 z 28 súborov
- Najvyššia dosiahnutá úroveň: `T2` (iba pre read-only KMPC-141 vetvu)
- Exact KMPC-139 tier: `T1` — forenzne potvrdený z primárnych receiptov a zdrojov; **v tomto balíku nebol T2 reprodukovaný** (transitívny 80-dps runtime closure nie je súčasťou balíka; exact fyzika nebola auditorom spúšťaná — v súlade s pokynmi)
- Read-only KMPC-141 tier: `T2` — dosiahnutý; vygenerovaný JSON je **byte-identický** s reference `EVIDENCE/013` (zhodný SHA-256 vrátane `runtime_seconds`; povolená normalizácia nebola ani potrebná)
- Oficiálna KMPC-141 vetva bez odchýlky: `PASS`
- Deklarované odchýlky: 4 × `DECLARED_DEVIATION`, žiadna nemení výsledok — pozri „Nonclaims a odchýlky"

## Prostredie

- OS/architektúra: Windows 11 Pro 10.0.26200 (Windows-10-10.0.26200-SP0), x64
- Python: 3.11.3 (`C:\Python311\python.exe`)
- Knižnice použité official vetvou: `standard library only` — runner 385 importuje iba argparse, copy, hashlib, json, pathlib, sys, time, traceback, typing (overené čítaním zdroja aj úspešným behom v čistej kópii bez site-packages závislostí)

## Procesný ledger

Reprodukčné vetvy bežali z koreňa čerstvej dočasnej kópie `REPRO/`
(scratchpad `ea034_repro_copy1`), každá ako samostatný proces s vonkajším
timeoutom `10 s`. Negatívny guard bežal v druhej čistej kópii
(`ea034_repro_copy2`). Originálny balík: hash celého stromu (28 súborov)
pred aj po behoch identický — `PACKAGE_UNCHANGED`.

| Fáza | Presný príkaz | Exit code | Wall time | Generated JSON SHA-256 | Stav |
|---|---|---:|---:|---|---|
| package preflight | `& "D:\Teoria\External_Audits\TOOLS\Test-ExternalAuditPackage.ps1" -PackagePath "D:\Teoria\External_Audits\PACKAGES\EA-20260719-034-KMPC138-141-C3-BI-MODE-CLOSURE"` | 0 | 0.587 s | n/a | PASS — `{"checks":129,"failed":0,"passed":true}` |
| compile | `python -c "from pathlib import Path; p=Path(r'scripts\385_script_KMPC_141_P5_3g7_C3_BI_k0p15_supersession_scope_correction.py'); compile(p.read_text(encoding='utf-8'), str(p), 'exec'); print('COMPILE_PASS')"` | 0 | 0.125 s | n/a | PASS — `COMPILE_PASS` |
| help | `python scripts\385_..._supersession_scope_correction.py --help` | 0 | 0.172 s | n/a | PASS — usage vypísaný |
| smoke | `python scripts\385_..._supersession_scope_correction.py --smoke --mode BI --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8` | 0 | 0.203 s | n/a | PASS — `mode=SMOKE_NO_PHYSICS`, `physics_executed=false`, `worker_calls=0`, `solver_calls=0`, všetky source/corrected checks true |
| official audit | `python scripts\385_..._supersession_scope_correction.py --audit --mode BI --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8` | 0 | 0.203 s | `6F44B553BD01BB0516389643511C2858D0EBEA61380C4A8ABFE4E572909231A2` | PASS — `pair_pass=true`, `HP_M1_exact_resume_pass=true`, `worker_calls=0`, `solver_calls=0`, script-reported `runtime_seconds=0.016 s` |
| missing-prerequisite guard | v 2. čistej kópii zmazaný `RUN_KMPC_140_..._READ_ONLY_AGGREGATE.json`, potom identický smoke príkaz | 2 | 0.188 s | n/a | PASS (fail-closed) — stderr `KMPC-141 pre-output technical failure: FileNotFoundError: KMPC-141 frozen source missing: ...`, stdout prázdny, žiadny nový súbor nevznikol (`no_success_json=true`) |
| declared deviation | opakovaný smoke v kópii 1 (iba na zachytenie plného `physics_executed` poľa do logu) | 0 | ~0.2 s | n/a | informatívny re-run; read-only, bez vplyvu |

Poznámka ku generated JSON: SHA-256 vygenerovaného raw sa zhoduje s reference
`EVIDENCE/013` **byte-po-byte**, t. j. aj bez normalizácie `runtime_seconds`
(oba behy zaznamenali `0.01600000000325963 s` — artefakt granularity Windows
monotonic timera, nie kopírovanie). Seal-time beh orchestrátora mal iný
`runtime_seconds` (generated SHA `EA94A317...A177B1` per 05_PACKAGE_HISTORY),
čo potvrdzuje, že `runtime_seconds` je jediné behovo-variabilné pole.

## Odpoveď na presnú otázku

Áno — primárne zdroje a immutable receipts potvrdzujú všetky štyri časti
presnej otázky z dokumentu 00, v deklarovaných tier hraniciach:

1. **Lokálna 45-s výnimka bola obmedzená iba na dva BI/.15 exact workery,
   obnovila deadline ownera a oba 80-dps systémy prešli.** `OBSERVED_IN_PRIMARY`
   — runner 015: overlay `_local_exact_deadline_overlay` sa inštaluje výlučne
   vo vetve `--worker-exact-variant` (riadok 482), prijíma iba presne `45.0`
   (riadok 62–67), `finally` vždy obnovuje `_FROZEN_DEADLINE_FACTORY`
   (riadok 83); official vetva vynucuje coefficient limit presne `4.8 s`
   (riadok 545–546). Raw 012: 4/4 coefficient workery `returncode=0` s
   `runtime_limit_seconds=4.8` (runtime 1.219–1.75 s), 2/2 exact workery
   `returncode=0`, `technical_pass=true`, `runtime_limit_seconds=45.0`,
   runtime `19.922 s` (gamma0) a `21.344 s` (af0),
   `local_45s_deadline_owner_active=true` aj
   `original_deadline_owner_restored=true` v oboch; driver
   `pass_driver=true` (max rel. rezíduá `1.019e-81` / `8.615e-82`),
   non-fit holdout `pass_holdout=true` s `rows_added_to_driver_solve=0`
   (max rel. `4.250e-15` / `7.071e-15`), `precision_dps=80`. Historická
   autorita 45 s: raw 014 (KMPC-112) `runtime_limit_seconds=45.0`,
   `runtime_seconds=34.86 s`.
2. **KMPC-140 doplnil iba schema alias bez opakovania fyziky.**
   `OBSERVED_IN_PRIMARY` — zdroj 016: deepcopy + `contract_guard :=
   successor_contract_guard`, kanonický SHA-256 roundtrip dokazuje nezmenené
   existujúce polia (riadky 258–266), žiadny worker/solver/CPQR import ani
   volanie; raw KMPC-140 register: `worker_calls=0`, `solver_calls=0`,
   `CPQR_calls=0`, `physics_repeated=false`, 4 aliasy, 0 zmenených hodnôt,
   0 zmenených child run_id. Parent chyba KMPC-139 forenzne potvrdená v
   tracebacku 012: `KeyError('contract_guard')` v v3 agregátore riadok 359
   (zdroj 019), zatiaľ čo base 017 publikuje `successor_contract_guard`
   (riadok 339).
3. **KMPC-141 nahradil chybnú rovnosť fail-closed podmnožinovou podmienkou,
   nezmenil vedecké hodnoty ani thresholdy a jeho official vetva je
   reprodukovateľná.** `OBSERVED_IN_PRIMARY` + `INDEPENDENTLY_RECOMPUTED` —
   chybný predikát lokalizovaný v 017 riadky 651–662 (`original_false ==
   ['M3_driver','M3_independent_00_0i_holdout']`); opravený predikát v 385
   (riadky 258–273): neprázdnosť, podmnožina scope, zákaz false mimo scope,
   exact uzavretie drivera, exact potvrdenie holdoutu; legacy hodnota
   zachovaná ako diagnostika mimo aktívnych checks (história neprepísaná).
   Protected scientific snapshot: nezávisle prepočítaný auditorom funkciou
   `scientific_snapshot`+`canonical_sha256` nad frozen KMPC-140 vstupom aj
   reference 013 — oba `C289C8997FEC93FD3BB754C638137962EF64DF27366B22FF52C1E8B516B0F949`,
   zhodné s tvrdením interného auditu. Thresholdy byte-semanticky identické
   naprieč 012 payloadmi, KMPC-140 raw a 013 (`driver 1e-10, holdout 1e-9,
   common 1e-8, tail 1e-6, absolute_fallback 1e-12, background_relative
   1e-12`). Reprodukcia: byte-identický output (ledger vyššie).
4. **Scoped záver `PASS_C3_BI_MODE_9_OF_9`, globálne `33/45`, K4 `60/100`
   zodpovedá priloženým dôkazom.** Zero-variant pair rawy
   `OBSERVED_IN_PRIMARY`: 010 (k=.005, `pair_pass=true`), 011 (k=.05,
   `pair_pass=true`), 013 (k=.15, `pair_pass=true`) = 6 nulových atómov;
   nominal atómy troch k a účtovanie AD/CDI/nominal registra
   `INFERRED_FROM_PROJECT_DOCS` (001 §5, 002 riadky 110–122; aritmetika
   sedí: 15 nominal + 6 AD + 6 CDI + 6 BI = 33; zvyšok NID/NIV 0/12 →
   33+12=45). Žiadny fyzikálny STOP nevznikol (všetky zlyhania boli
   technické receipty bez fyzikálneho verdiktu; exact rezíduá hlboko pod
   prahmi). C3 aggregate do 45/45, P5.4, G8, G9 zostávajú zakázané
   (002 riadky 121–122, 141).

## Overenie tvrdení

| Tvrdenie | Tag dôkazu | Primárny zdroj path + riadok/pole | Metóda | Výsledok |
|---|---|---|---|---|
| KMPC-139 má 4/4 coefficient a 2/2 exact successful payloady | OBSERVED_IN_PRIMARY | `EVIDENCE/012...json` → `worker_process_records.*` (všetkých 6 `returncode=0`, `stderr=""`, `parse_error=""`), `successful_worker_payloads` (4+2 kľúče) | JSON parsing skriptom auditora | PASS |
| exact runtimes a driver/non-fit holdout brány PASS | OBSERVED_IN_PRIMARY | `012` → `exact_boundary_wave.gamma0.runtime_seconds=19.92199999999866`, `af0=21.343999999997322`; `high_precision_boundary.driver.pass_driver=true`, `holdout.pass_holdout=true`, `rows_added_to_driver_solve=0`, holdout shape `[16,104]`, `precision_dps=80` | JSON parsing; číselné porovnanie s interným auditom 001 §2 (zhoda na všetkých 8 uvádzaných hodnotách vrátane absolute fallback maxím) | PASS |
| 45-s owner je lokálny a obnovený; coefficient cap ostáva 4.8 s | OBSERVED_IN_PRIMARY | `EVIDENCE/015...py:53-87,482,545-548` (overlay iba v exact roli, akceptuje iba 45.0, finally obnova, 4.8 vynútené); `012` → `technical_checks.local_45s_deadline_owner_active=true`, `original_deadline_owner_restored=true` (oba varianty); 4× `runtime_limit_seconds=4.8` v coefficient wave | čítanie zdroja + JSON parsing | PASS |
| KMPC-140 mení iba alias a nevolá solver | OBSERVED_IN_PRIMARY | `EVIDENCE/016...py:246-284` (SHA-roundtrip dôkaz nezmenených polí), `:1-21` (žiadne physics importy); KMPC-140 raw → `read_only_parent_recovery` (`worker/solver/CPQR=0`, `physics_repeated=false`, alias register 4/0/0) | čítanie zdroja + JSON parsing | PASS |
| stará rovnostná supersession podmienka je false negative | OBSERVED_IN_PRIMARY | `EVIDENCE/017...py:651-662` (equality predikát); KMPC-140 raw → oba varianty: jediné false = `original_false_set_exact`, `original_false_checks=['M3_driver']`, exact driver aj holdout true; `008` PF-126 | čítanie zdroja + JSON parsing (checky `legacy_equality_false`, `all_other_evidence_checks_true` v smoke) | PASS — false negative potvrdený |
| nová podmnožinová podmienka je fail-closed a vecne korektná | OBSERVED_IN_PRIMARY + INDEPENDENTLY_RECOMPUTED | `REPRO/scripts/385...py:243-300` (5 podmienok: neprázdnosť, podmnožina, zákaz mimo scope, exact uzavretie drivera, exact potvrdenie holdoutu; legacy retained ako diagnostika); `:153-240` prísna fail-closed validácia vstupu (`original_false == ['M3_driver']` vynútené) | čítanie zdroja + vlastný beh official vetvy + negatívny guard | PASS — smer zlyhania konzervatívny (pri nesplnení ktorejkoľvek podmienky nevznikne PASS, iba technical failure) |
| protected scientific snapshot a thresholdy sa nemenia | INDEPENDENTLY_RECOMPUTED | snapshot(KMPC-140 raw) = snapshot(013) = `C289C899...F949` (auditorov vlastný prepočet funkciami z 385); thresholds dict identický v 012/KMPC-140/013 | vlastný výpočet kanonického SHA-256 + dict porovnanie | PASS |
| KMPC-141 official je reprodukovateľný s field parity okrem runtime | INDEPENDENTLY_RECOMPUTED | generated `...SUPERSESSION_SCOPE_CORRECTED.json` v čerstvej kópii → SHA `6F44B553...231A2` == reference `EVIDENCE/013` (byte-identický; deep-diff 0 rozdielov aj pred normalizáciou) | plná reprodukcia compile/help/smoke/official + deep-diff | PASS (silnejšie než požiadavka) |
| scoped BI 9/9 a globálne C3 33/45 zodpovedá rawom | OBSERVED_IN_PRIMARY (6 nulových atómov: 010/011/013 `pair_pass=true`) + INFERRED_FROM_PROJECT_DOCS (nominal atómy a AD/CDI register: 001 §1/§5, 002:110-122) | pozri stĺpec | JSON parsing + aritmetická kontrola (15+18=33; 33+12=45) | PASS v deklarovanom scope |

Doplnkové overenia: source hashe v raw 012 (`base=489ED5...`, `runner=36C041...`)
sedia s manifestovými hashmi 018 a 015 (`OBSERVED_IN_PRIMARY`); 013
`source_hashes` obsahuje KMPC-139 failure receipt `FBACDAB5...334B`, KMPC-140
raw `DF45DF6A...638F` aj runner 385 `007687D1...54C4` — všetko zhodné s
manifestom a predregistráciami 004–007 (`INDEPENDENTLY_RECOMPUTED` hashe).
Lineage PF-123→126 v ledgeri 008 a karanténa runnerov 382/383/384 v DNR 009
sú vnútorne konzistentné s receiptami (`CONTEXT_ONLY`).

## Rozdiely generated JSON voči reference

Žiadne. Deep-diff po odstránení top-level `runtime_seconds`: 0 rozdielov;
navyše aj samotné `runtime_seconds` sa náhodou zhodovalo (granularita
Windows monotonic timera ~15.6 ms; oba behy `0.01600000000325963`), takže
súbory sú byte-identické (zhodný SHA-256). Povolená normalizácia nebola
potrebná; žiadne iné behovo-variabilné pole neexistuje.

## Nálezy

### F-001 — `EDITORIAL`

- Typ: `DOCUMENTATION`
- Presný zdroj: `01_MANIFEST_SHA256.md`, posledný riadok tabuľky
- Pozorované: display path `REPRO/scripts/results/k_mpc_005/RUN_KMPC_140_...READ_ONLY_AGGREGATE.json` je skrátený výpustkou, zatiaľ čo ostatné riadky uvádzajú plné mená
- Očakávané: plný copy path aj v čitateľskej MD tabuľke
- Dopad na package tier: žiadny — dokument sám deklaruje, že strojovým zdrojom pravdy je `01_MANIFEST_SHA256.tsv`, ktorý je úplný a správny
- Dopad na fyzikálny scope/verdict: žiadny
- Minimálny reprodukčný test: porovnať posledný riadok MD s riadkom 22 TSV
- Navrhovaná oprava: voliteľná kozmetická — pri budúcom balíku negenerovať skrátené display paths

### F-002 — `EDITORIAL`

- Typ: `DOCUMENTATION`
- Presný zdroj: `EVIDENCE/013...json` → `process_architecture` (kľúče); `EVIDENCE/015...py:624-631`
- Pozorované: register `local_exact_runtime_exception` (scope, limity, historická autorita, `equations_matrices_thresholds_changed=false`) zapisuje iba KMPC-139 runner do svojho official outputu, ktorý pre parent KeyError nikdy nevznikol; vo finálnom reťazci KMPC-140/141 je 45-s výnimka evidovaná nepriamo (`read_only_parent_recovery.exact_limit_seconds=45.0`, exact payloady s `runtime_limit_seconds=45.0` a owner-lifecycle checks)
- Očakávané: nič nechýba voči tvrdeniam balíka — dôkazová stopa výnimky je úplná cez 012+015; ide o traceability poznámku pre budúcich auditorov
- Dopad na package tier: žiadny
- Dopad na fyzikálny scope/verdict: žiadny
- Minimálny reprodukčný test: `python -c "import json; d=json.load(open('EVIDENCE/013...json')); print('local_exact_runtime_exception' in d['process_architecture'])"` → `False`
- Navrhovaná oprava: žiadna nutná; prípadne v budúcom read-only successor reťazci prenášať aj tento register

Žiadny `CRITICAL`, `MATERIAL` ani `MINOR` nález. Nebola nájdená zmena
thresholdov ani vedeckých hodnôt, false položka mimo scope, neobnovený
owner, ani nereprodukovateľná KMPC-141 vetva.

## Nonclaims a odchýlky

Potvrdenie nonclaims balíka (auditor ich neporušuje ani nerozširuje):
netvrdí sa T2 reprodukcia 45-s exact výpočtu, T3 nezávislá implementácia,
C3 `45/45`, C3 aggregate, fyzikálny STOP, zvýšenie K4 nad `60/100`,
uzavretie S-M mikrofyziky ani povolenie P5.4/G8/G9. Lokálna výnimka nemení
všeobecný K4-B2 runtime kontrakt — v zdrojoch je zapísaná ako frozen
konštanta iba pre `BI/.15/gamma0|af0/exact-boundary` procesné roly.

**Explicitne: exact KMPC-139 nebol v tomto balíku T2 reprodukovaný.**
Auditor exact fyziku nespúšťal (v súlade s pokynmi a T1 hranicou balíka);
45-s vetva je potvrdená forenzne zo zamrznutých receiptov a zdrojov.

`DECLARED_DEVIATION` zoznam:

1. Preflight bol volaný s absolútnym `-PackagePath` z koreňa `D:\Teoria`
   (ekvivalent relatívneho tvaru v pokynoch).
2. Reprodukčné vetvy boli orchestrálne spúšťané pomocným Python harnessom
   v session scratchpade (mimo balíka aj RESPONSES), aby bol vynútený
   vonkajší `10 s` timeout a presné meranie wall time; argv aj pracovný
   adresár zodpovedajú príkazom dokumentu 03 (interpreter
   `C:\Python311\python.exe` = `python`). Balík zostal nezmenený —
   hash stromu 28 súborov pred/po behoch identický.
3. Jeden dodatočný informatívny re-run smoke vetvy v kópii 1 (zachytenie
   plného `physics_executed=false` výpisu); read-only, bez vplyvu.
4. Nad rámec povinností: nezávislý prepočet protected snapshot hashov
   z KMPC-140 vstupu a reference 013 (obe `C289C899...F949`) — posilňuje,
   nemení závery.

Nezostalo nič neoverené z povinných úloh 1–10 zadania; tokenový ani
dôkazový deficit nenastal.

## Neautoritatívne odporúčanie

`AGREE_IN_SCOPE`

- Integrita balíka: PASS (129/129 preflight; 21/21 nezávislé hashe; 0 duplicít).
- KMPC-141 official/field parity: PASS na najsilnejšej možnej úrovni
  (byte-identický output); missing-input guard fail-closed PASS.
- T1 exact lineage KMPC-139 (4/4 + 2/2, runtimes 19.922/21.344 s pod 45 s,
  driver/holdout PASS, owner lifecycle, coefficient 4.8 s) potvrdená
  z primárnych zdrojov.
- Logická oprava supersession predikátu je vecne korektná, fail-closed,
  nemení vedecké hodnoty ani thresholdy a neprepisuje históriu (legacy
  diagnostika zachovaná; holdout vedený ako `already_passing_exactly_confirmed`,
  nie ako pôvodne false).
- Scoped záver `PASS_C3_BI_MODE_9_OF_9` / C3 `33/45` / K4 `60/100` / bez
  STOP je podložený v deklarovanom scope (nulové atómy primárne; nominal a
  AD/CDI register z projektových dokumentov).

## Vyhlásenie autority

Tento externý posudok nemení projektový `PASS/REVIEW/STOP`, C3 register ani
K4 score. Autoritatívne spracovanie vykonáva iba hlavný orchestrátor v novom
súbore odpovede.
