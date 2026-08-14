# Hlavný posudok externého auditu EA-037

**Dátum:** 2026-07-22  
**Externá odpoveď:** `00_AUDITOR_AUDIT.md`  
**SHA-256 externej odpovede:**
`8946C9E2E9363C6FEC9F70E7B35E3CB7A9990D59AA80EF2E92074AD8B356CFAF`  
**Auditor:** nezávislý Codex audit agent / GPT-5 family  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Autorita spracovania:** hlavný orchestrátor  
**Výsledok spracovania:** `ACCEPTED_AGREE_IN_SCOPE_T2`

## 1. Autoritatívny rozsudok

```text
PACKAGE_R6_PREFLIGHT = PASS_249_OF_249
PACKAGE_INTEGRITY = PASS_EXACT_PRE_POST_SNAPSHOT
KMPC131_NIV_K0P15_TIER = T2_REPRODUCIBLE_CALCULATION
OFFICIAL_WITHOUT_DEVIATION = PASS_EXIT_0_EXPECTED_REVIEW
CORRECTED_FIELD_PARITY = PASS_DIFF_0
NEW_MISSING_INPUT_GUARDS = PASS_2_OF_2_FAIL_CLOSED
EA036_FINDINGS_F001_F003 = CLOSED
PROJECT_NIV = 7_OF_9_PASS_UNCHANGED
GLOBAL_C3 = 43_OF_45_PASS_UNCHANGED
K4_DEPTH = 60_OF_100_UNCHANGED
PHYSICS_STOP = NONE
EXTERNAL_AUDIT_PAUSE = CLOSED
```

Externý audit sa prijíma v celom deklarovanom EA-037 scope. Odstraňuje
reprodukčnú neistotu EA-036 a nezávisle reprodukuje existujúci REVIEW ako
očakávaný fyzikálny stav, nie ako technical failure. Neudeľuje PASS dvom
NIV atómom; otvára iba metodickú možnosť pripraviť úzky predregistrovaný
same-matrix multi-rank successor.

## 2. Prijaté výsledky

1. R6 preflight prešiel `249/249`; manifest `30/30`, runtime mapa
   `25/25`, exact REPRO coverage a hardcoded dependency checks prešli.
2. Whole-package snapshot pred/po je exact
   `CBD619F6...4C54A0C`; package ostal immutable.
3. Fresh compile/help/smoke/official prešli. Official bez odchýlky skončil
   exit `0` za `8.7 s` a vytvoril generated JSON SHA-256
   `2545020C78CA4C480CBF264EF4D53CDE1F404CA45C0C0A4E4DCE5B361A7E9615`.
4. Candidate ostal `REVIEW_C3_ZERO_VARIANT_PAIR_UNCLOSED`, pair false;
   nevznikol technical failure.
5. Po vopred povolenej normalizácii šiestich runtime hodnôt a absolútneho
   koreňa jednej provenance cesty zostalo `0` rozdielov. Normalizovaný SHA
   reference aj generated rawu je
   `68C561CDB249CD1A957B97A02AEC06BEF28D302305ABDCE39185207324E17521`.
6. Relatívny provenance suffix a B1 source SHA ostali exact. Nijaké
   fyzikálne číslo, brána, prah, identity ani support sa nenormalizovali.
7. Missing-script88 aj missing-source-map26 official vetvy prešli
   fail-closed bez success rawu a bez nového fyzikálneho verdiktu.
8. Reprodukcia potvrdila štyri primárne M3 driver boundaries, plné ranky,
   prechádzajúce holdout/common/tail/background a odvodenú povahu af0
   bridge false.

## 3. Spracovanie nálezu

| ID | Spracovanie | Dopad a náprava |
|---|---|---|
| F-001 | `ACCEPTED_MINOR_TOOL_RUNTIME_DISCLOSURE` | R6 preflight používa API dostupné v PowerShell 7+, preto budúce pokyny musia volať `pwsh`, nie legacy `powershell.exe`. Tool dostáva explicitný version guard a protokol/checklist požiadavku. T2, numerika a fyzika nie sú dotknuté. |

Neostal nijaký `CRITICAL` ani `MATERIAL` nález. EA-036 F-001 až F-003 sú
uzavreté. Agentový posudok zostáva náhradnou externou kontrolou v rovnakej
platformovej rodine a netvrdí T3 nezávislý equation builder.

## 4. Stav po spracovaní

- NIV ostáva `7/9 PASS`; posledné dva atómy ostávajú REVIEW;
- globálne C3 ostáva `43/45 PASS`; aggregate ostáva zakázaný do `45/45`;
- K4 ostáva živá na `60/100`, bez fyzikálneho STOP;
- external audit pause pre first REVIEW je uzavretá;
- prediction table, release a Zenodo sa nemenia.

## 5. Ďalší predregistrovaný krok

Smie vzniknúť jeden nový versioned successor pre kartézsky súčin
`gamma0+af0 × accepted rank 104 + audit rank 130`. Predregistrácia musí
zmraziť:

- presne tri same-matrix residual corrections pre každý zo štyroch solve;
- byteovo identickú maticu, RHS/konštantu, support `[-1,6]→[-1,8]`, M1
  depth 8, nominal KMPC-126 autoritu a všetky prahy;
- zákaz fitu na independent holdout;
- povinné opätovné holdout/common/tail/background/bridge/logical brány;
- stop pri technical failure alebo zostávajúcom REVIEW; PASS sa smie
  prideliť až novým interným auditom rawu.

Stav EA-037: `ASSESSED_BY_MAIN_ORCHESTRATOR_T2_ACCEPTED`.  
Stav projektu: `C3_43_OF_45 / NEXT_NIV_K0P15_MULTI_RANK_PREREGISTRATION`.
