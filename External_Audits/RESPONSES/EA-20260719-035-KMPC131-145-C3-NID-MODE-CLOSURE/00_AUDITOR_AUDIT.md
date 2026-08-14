# Externý audit — EA-035 C3 NID mode closure

## Povinné metadáta

- Auditor/model/verzia: **Claude Fable 5 (Anthropic)**, spustený v prostredí
  Claude Code; model ID `claude-fable-5`. Nezávislý externý auditor, odlišný
  dodávateľ od tvorcu skriptov (Codex/OpenAI) aj autora teórie (Martin Jambor).
- Dátum, čas a časová zóna: **2026-07-20**, Central Europe Standard Time
  (`UTC+02:00`); referenčný časový bod behov `2026-07-20T19:48:39+02:00`.
- Audit mode: **nezávislý externý read-only forenzný audit + T2 reprodukcia
  KMPC-145**. Žiadny package ani živý projektový súbor nebol zmenený; všetky
  behy prebehli v nových dočasných kópiách adresára `REPRO`.
- Package revision: `EA-20260719-035-KMPC131-145-C3-NID-MODE-CLOSURE`,
  stav `SEALED_READY_FOR_EXTERNAL_AUDIT` (seal 2026-07-19).
- SHA-256 `01_MANIFEST_SHA256.tsv`:
  `DA09F7256985F97C69B2058BC6216215586316A6C7A69E0ECA8B0B1DEA109E5C`
  — **INDEPENDENTLY_RECOMPUTED** (Python `hashlib` aj PowerShell `Get-FileHash`),
  zhoda s očakávanou hodnotou.
- Najvyššia dosiahnutá úroveň: **T2** pre read-only KMPC-145;
  **T1** pre numeriku KMPC-131/142/143/144.
- KMPC-145 tier: `T2_REPRODUCIBLE_READ_ONLY_COMPOSITION` — dosiahnuté a
  nezávisle reprodukované.
- KMPC-131/142/143/144 tier: `T1_PRIMARY_FORMULA_AND_RECEIPTS` — forenzne
  overené proti primárnym rawom a zdrojom; **nie** nezávisle T2 reprodukované.
- Deklarované odchýlky: **1 metodologická** (`DECLARED_DEVIATION`, viď sekcia
  „Nonclaims a odchýlky"). Žiadna vecná odchýlka od pokynov.

## Prostredie

- OS/architektúra: Microsoft Windows NT `10.0.26200.0` (Windows 11 Pro), x64;
  shell PowerShell `7.6.3`.
- Python: CPython `3.11.3` (`python` == `py` launcher).
- Použité knižnice:
  - Reprodukovaný skript KMPC-145 importuje **iba Python standard library**
    (`argparse`, `copy.deepcopy`, `hashlib`, `json`, `os`, `pathlib`, `sys`,
    `time`, `traceback`) — žiadna tretia strana, žiadny NumPy/SciPy.
  - Auditné nástroje auditora: `hashlib`, `json`, `csv`, `subprocess`, `os`,
    `time` (všetko stdlib) a PowerShell `Get-FileHash -Algorithm SHA256` na
    nezávislú krížovú kontrolu hashov a `Test-ExternalAuditPackage.ps1`.

## Procesný ledger

| fáza | presný príkaz | exit code | wall time | generated JSON SHA-256 | stav |
|---|---|---:|---:|---|---|
| package preflight | `& "D:\Teoria\External_Audits\TOOLS\Test-ExternalAuditPackage.ps1" -PackagePath "…\EA-20260719-035-KMPC131-145-C3-NID-MODE-CLOSURE"` | `0` | `2.262 s` | n/a | `171/171 PASS, failed=0` |
| compile | `python -c "…compile(p.read_text('utf-8'),str(p),'exec');print('COMPILE_PASS')"` (p = `scripts\389_script_KMPC_145_…py`) | `0` | `0.161 s` | n/a | `COMPILE_PASS` |
| help | `python scripts\389_script_KMPC_145_…py --help` | `0` | `0.189 s` | n/a | usage/options vypísané |
| smoke | `python scripts\389_script_KMPC_145_…py --smoke --mode NID --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8` | `0` | `0.244 s` | n/a (smoke nič nezapíše) | `physics_executed=false`, 10/10 checks true, counts 0/0/0 |
| official | `python scripts\389_script_KMPC_145_…py --audit --mode NID --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8` | `0` | `0.187 s` | `0D3D0968F85D9B5F00AA5186119CFB6647274C1CA7327F0106B573EAA5DC8C1C` | `pair_pass=true`, 14/14 correction checks, 2 parity opravené, snapshot identický |
| missing KMPC-131 guard | (odstránený `RUN_KMPC_131_…ZERO_VARIANT_PAIR.json`) `python scripts\389_…py --smoke --mode NID --k 0.15 --result-dir scripts\results\k_mpc_005 --max-runtime-seconds 4.8` | `2` | `0.293 s` | n/a (žiadny) | fail-closed, `immutable input missing or hash-mismatched` |
| missing KMPC-144 guard | (odstránený `RUN_KMPC_144_…AF0_AUDIT_SAME_MATRIX_REFINEMENT.json`) `python scripts\389_…py --smoke …` | `2` | `0.248 s` | n/a (žiadny) | fail-closed, `immutable input missing or hash-mismatched` |

Pracovný adresár všetkých štyroch KMPC-145 fáz a smoke guardov bol koreň
dočasnej kópie `…\scratchpad\repro_main\REPRO` (resp. `guard_131\REPRO`,
`guard_144\REPRO`). Originálny package nebol nikdy pracovným adresárom ani
miestom generated outputu. Každý proces mal vonkajší timeout `10 s`; žiadny
proces timeout nedosiahol (`TIMED_OUT=False`). Vnútorný read-only cap `4.8 s`
bol zadaný a skript ho vynucuje (`--max-runtime-seconds` musí byť presne `4.8`).

Package pred/po nemennosť: `01_MANIFEST_SHA256.tsv` SHA-256 pred aj po celom
audite `DA09F7…E5C`; počet package súborov `36` nezmenený; v originálnom
`REPRO` nevznikol žiadny `RUN_KMPC_145_…PARITY_SCOPE_CORRECTION.json`.
**INDEPENDENTLY_RECOMPUTED.**

## Odpoveď na presnú otázku

Odpovede pokrývajú body 1–5 dokumentu 00 (a ich rozšírené znenie 1–6 z
zadania). Pri každom bode je uvedený evidence tag.

**1. NID nulové varianty pri k = 0.005, 0.05, 0.15 dávajú šesť scoped PASS
atómov a spolu s tromi nominal atómami uzatvárajú NID 9/9 — POTVRDENÉ.**
`INDEPENDENTLY_RECOMPUTED` + `OBSERVED_IN_PRIMARY`. Každý mode-k pár má
`logical_atom_accounting = {existing_nominal:1, new_zero_variants:2,
total_logical_atoms:3}` (rawy 014/016/017). Finálne rawy: `.005` (014)
`pair_pass=true`; `.05` (016, KMPC-143) `pair_pass=true`; `.15` (017, KMPC-145)
`pair_pass=true`. Tri k × dva nulové varianty = **šesť nulových atómov**; plus
tri nominal atómy = **9/9**. Mode-local postup `3/9→5/9→7/9→8/9→9/9` je
konzistentný s globálnymi bodmi 33→35→37→38→39.

**2. Globálny C3 register 33/45 → 39/45 (o šesť, nie o deväť) — POTVRDENÉ.**
`INDEPENDENTLY_RECOMPUTED` + `INFERRED_FROM_PROJECT_DOCS`. Tri NID nominal
atómy už boli v uzavretom BI stave `33/45` (EVIDENCE/002 r.110). Šesť nových
nulových atómov posúva register na `39/45` (EVIDENCE/002 r.135–136, 145).
Medzistav `37/45` (r.128; prereg 007 r.8) = 33 + 4 uzavreté (.005 a .05), potom
+2 (.15 gamma0, af0) = 39. Rekonštrukcia `33 + 6 = 39` sedí presne.

**3. KMPC-143 a KMPC-144 používajú iba predregistrované same-matrix korekcie
lokalizovaných audit-driver hraníc, bez fitu na holdout a bez zmeny rovníc,
matice, RHS, supportu či prahov — POTVRDENÉ.** `INDEPENDENTLY_RECOMPUTED` +
`OBSERVED_IN_PRIMARY`. Provenance v R144/017: `matrix_identity =
EXACT_SAME_MATRIX_AND_CONSTANT`, `target_rank = 104`, `iterations = 3`,
`selection_rule_pass = true`. `accepted_solve` je bit-invariantný pri každom
prechode (015↔016, R131↔R144, R144↔017 — kanonické hashe zhodné). Holdout
zostáva nezávislý a PASS (`< 1e-9`), do driver solve nebol pridaný (primárne
zdroje 024/025/026). Audit M3 drivery klesli pod `1e-10`: `.05` af0
`1.3994e-10→1.5468e-16`, gamma0 `1.9348e-10→1.0698e-16`; `.15` af0
`4.1866e-10→1.3514e-16` (gamma0 audit `9.8546e-11` bez refinementu — už PASS).

**4. PF-127 a PF-128 sú technické/formálne false-negative chyby bez nového
fyzikálneho verdiktu — POTVRDENÉ.** `OBSERVED_IN_PRIMARY` +
`INFERRED_FROM_PROJECT_DOCS`. PF-127 (KMPC-142) je legacy whole-object identity
equality proti redukovanej mape; `physics_executed=false`, bez rawu, bez
verdiktu (012, 004). PF-128 (KMPC-144) je parent-only parity false-negative
(integer vs. string JSON kľúče, runtime, nový true provenance check); v R144 sú
**všetky fyzikálne brány af0 aj gamma0 true**, no `pair_pass=false` drží iba
dvojica parity checks (012 r.568, 010). Ani jeden nedostal fyzikálny STOP ani
nový verdikt (`orchestrator_verdict = NOT_ASSIGNED_BY_SCRIPT`, candidate-only).

**5. KMPC-145 mení iba dve parity projekcie a odvodené polia, chránený vedecký
snapshot ostáva identický — POTVRDENÉ.** `INDEPENDENTLY_RECOMPUTED`. Official
beh: `operation_counts = workers/solvers/cpqr = 0/0/0`; `corrected_fields =
{af0_accepted_exact_predecessor_parity, gamma0_variant_exact_predecessor_parity}`
(presne dva); `protected_snapshot_sha256_before == after ==
EBD4021F5BC285551D2EE8DC521E0A9DE23BA6D61CDE5D6DEBAE473BAA2FD97D`. Variantové
subtrees af0/gamma0 (vrátane driverov) sú v 017 identické s R144.

**6. Interný záver `PASS_C3_NID_MODE_9_OF_9`, globálne `39/45`, bez fyzikálneho
STOP, K4 `60/100` bez zmeny — ZODPOVEDÁ DÔKAZOM.** `OBSERVED_IN_PRIMARY`. Každý
raw nesie `K4_score_effect = NONE_60_OF_100_UNCHANGED`; žiadny raw neasertuje
STOP; candidate polia sú výslovne „…CANDIDATE_ONLY". Účtovanie a fyzikálna
línia sú vzájomne konzistentné naprieč rawmi aj plánom 002.

## Overenie tvrdení

| tvrdenie | evidence tag | primárny path + pole/riadok | metóda | výsledok |
|---|---|---|---|---|
| Integrita balíka 171/171, manifest self-hash | `INDEPENDENTLY_RECOMPUTED` | `01_MANIFEST_SHA256.tsv`; `Test-ExternalAuditPackage.ps1` | preflight exit 0 + Python `hashlib` recompute | PASS (self-hash `DA09F7…E5C`, 29/29 copy+source+parity, 0 dup, 36+1) |
| NID `.005` pair PASS, support `[0,7]→[0,9]` | `OBSERVED_IN_PRIMARY` | `EVIDENCE/014` `.pair_pass`, `.support_depth_spec` | JSON parse | PASS (`pair_pass=true`, `M1_depth=9, accepted=[0,7], audit=[0,9]`) |
| NID `.05` identity + refinement línia | `INDEPENDENTLY_RECOMPUTED` | `EVIDENCE/015`→`016` `variants.*.audit_solve.m3.diagnostics` | driver recompute + accepted_solve hash | PASS (drivery `1.3994e-10→1.5468e-16`, `1.9348e-10→1.0698e-16`; accepted_solve invariant) |
| NID `.15` refinement fyzika PASS | `INDEPENDENTLY_RECOMPUTED` | `REPRO/…131`→`…144`→`017`; provenance `iterations/target_rank` | driver + gates + provenance | PASS (af0 `4.1866e-10→1.3514e-16`, abs `9.8321e-15→9.8608e-32`, rank 104, 3 iter, všetky brány true) |
| PF-128 presne dve parity false-negative položky | `OBSERVED_IN_PRIMARY` | `…144` `same_matrix_refinement_audit.checks` | JSON parse (false-set) | PASS (false = `af0_accepted_exact_predecessor_parity`, `gamma0_variant_exact_predecessor_parity`) |
| KMPC-145 protected snapshot a operation counts | `INDEPENDENTLY_RECOMPUTED` | generated `read_only_parity_scope_correction.*` | reprodukcia + JSON parse | PASS (before==after==`EBD4021F…FD97D`, counts 0/0/0, 14/14 checks) |
| generated/reference field parity okrem runtime | `INDEPENDENTLY_RECOMPUTED` | generated vs `EVIDENCE/017` | rekurzívny deep-diff | PASS (1 rozdiel pred / 0 rozdielov po odstránení top-level `runtime_seconds`) |
| oba negatívne guardy fail-closed | `INDEPENDENTLY_RECOMPUTED` | smoke po odstránení 131 / 144 | reprodukcia | PASS (exit 2, správna správa, žiadny success/failure JSON) |
| NID `9/9`, globálne `39/45`, K4 `60/100` | `OBSERVED_IN_PRIMARY` + `INFERRED_FROM_PROJECT_DOCS` | rawy `logical_atom_accounting`, `K4_score_effect`; `EVIDENCE/002` r.110/135/145 | účtovná rekonštrukcia | PASS (`33+6=39`, NID 9/9, K4 nezmenené) |

## Rozdiely generated JSON voči reference

Reprodukovaný official výstup:
`…\repro_main\REPRO\scripts\results\k_mpc_005\RUN_KMPC_145_P5_3G7_C3_NID_K0p15_PARITY_SCOPE_CORRECTION.json`.

- generated JSON SHA-256:
  `0D3D0968F85D9B5F00AA5186119CFB6647274C1CA7327F0106B573EAA5DC8C1C`
- reference SHA-256 (`EVIDENCE/017`):
  `226BF91F7DF12953D0DF53C2CEC676190067FA8D782211C68507FA8EAD874D6A`
  (zhoduje sa s manifestom).
- počet rozdielov **pred** normalizáciou: **1**
  - `/runtime_seconds`: `0.0159999999741558` (generated) vs
    `0.030999999995401595` (reference) — povolený nedeterministický top-level
    runtime.
- počet rozdielov **po** odstránení top-level `runtime_seconds`: **0**
- nepovolené rozdiely: **žiadne** (`INDEPENDENTLY_RECOMPUTED`).

Field parity je teda úplná: `protected snapshot`, varianty, koeficienty,
residualy, holdout, prahy, identity, brány, corrected_fields aj source hashe sú
bit-identické s reference po jedinej povolenej normalizácii.

## Nálezy

Žiadny nález závažnosti **CRITICAL** ani **MATERIAL**. Nezistila sa žiadna
zmena vedeckých hodnôt/prahov, žiadna nepravdivá aktívna brána, žiadne chybné
účtovanie ani nereprodukovateľná KMPC-145 vetva. Dva minoritné nálezy pre
úplnosť a transparentnosť:

**F-01 — MINOR — typ: dokumentácia/úplnosť.**
- Súbor/pole: `EVIDENCE/001__…INTERNAL_AUDIT.md` §5 a `EVIDENCE/002` odkazujú na
  účtovné erráta v zdrojových dokumentoch „220/223/225"; v balíku sú kópie 220
  (`003`) a 225 (`006`), ale zdroj „223" nie je priložený.
- Pozorovaný stav: errátum 223 nie je priamo inšpekovateľné v tomto balíku.
- Očakávaný stav: pre plnú auditovateľnosť účtovnej korekcie by bol prítomný aj
  zdroj 223 alebo explicitná poznámka, že jeho obsah je pokrytý 220/225.
- Minimálna reprodukcia: `dir EVIDENCE\` — chýba kópia zdroja 223.
- Dopad na tier: žiadny. Dopad na fyzikálny verdikt: žiadny — frozen raw hashe
  (014/016/017 aj REPRO vstupy) sú nezávisle overené a globálne účtovné body
  (33/37/38/39) sú vzájomne konzistentné, takže errátum sa preukázateľne
  nemohlo dotknúť rawov ani fyzikálnych verdiktov (mení iba mode-local naratív).
- Navrhovaná oprava: v budúcom balíku priložiť zdroj 223 alebo jednoriadkovú
  poznámku o jeho pokrytí.

**F-02 — EDITORIAL — typ: dokumentácia/inštrumentácia.**
- Súbor/pole: `REPRO/scripts/389_…py`, smoke payload
  `operation_counts = {workers:0, solvers:0, cpqr:0}` (a rovnako v official
  vetve) sú zapísané ako literály, nie ako inštrumentované počítadlo.
- Pozorovaný stav: nulové počty sú deklarované, nie merané.
- Očakávaný stav: hodnoty sú vecne pravdivé — statická inšpekcia skriptu
  potvrdzuje, že neobsahuje žiadne worker/solver/CPQR/fyzikálne volanie (iba
  načítanie, hashovanie a JSON projekcie).
- Minimálna reprodukcia: čítanie zdroja `389_…py` (žiadny import ani call
  numerického jadra).
- Dopad na tier: žiadny. Dopad na fyzikálny verdikt: žiadny.
- Navrhovaná oprava: voliteľne doplniť runtime počítadlo pre úplnú
  inštrumentáciu namiesto literálov (kozmetické).

## Nonclaims a odchýlky

Povinné vyhlásenie (verbatim):
**„KMPC-131/142/143/144 numerika nebola v tomto balíku T2 reprodukovaná."**
Tieto vetvy boli overené iba forenzne (T1): proti immutable rawom, provenance
poliam a primárnym `.py` zdrojom. Balík neobsahuje celý izolovaný Python
runtime ani tranzitívny numerický dependency closure pre tieto vetvy, preto ich
nezávislá T2 numerická reprodukcia nebola vykonaná a nemôže byť tvrdená.

Potvrdenie nonclaims dokumentu 00 — balík **ani tento audit** netvrdí:
- úplné C3 `45/45` — **netvrdené** (zostáva `39/45`);
- uzavretie NIV — **netvrdené** (šesť NIV nulových atómov ostáva otvorených);
- C3 aggregate — **netvrdené**;
- T3 nezávislá implementácia — **netvrdené**;
- empirické potvrdenie teórie — **netvrdené**;
- zvýšenie K4 nad `60/100` — **netvrdené** (K4 `60/100` nezmenené);
- uzavretie S-M mikrofyziky — **netvrdené**;
- povolenie P5.4, G8 alebo G9 — **netvrdené**.
Same-matrix refinement nie je nový fyzikálny zákon ani fit na holdout — tento
audit to potvrdzuje (`accepted_solve` invariantný, holdout mimo fitu).

`DECLARED_DEVIATION` (1, metodologická): Prvý PowerShell beh zachytával stdout
cez asynchrónne event handlery, čo kozmeticky preusporiadalo konzolové riadky.
Preto som smoke aj official zopakoval cez Python `subprocess` so synchrónnym
zachytením a ako autoritatívny artefakt beriem on-disk official JSON. Časy v
ledgeri pochádzajú z časovaného behu; exit kódy a obsah sú vo všetkých behoch
zhodné. Žiadna iná odchýlka; použil som presné príkazy z dokumentu 03.

## Neautoritatívne odporúčanie

**`AGREE_IN_SCOPE`.**

Zdôvodnenie: Integrita balíka je nezávisle reprodukovaná (`171/171`, self-hash
manifestu, `29/29` source/copy parity, runtime mapa `3/3`, `0` duplicitných
hash skupín, `36 + 1` súborov). Read-only KMPC-145 dosahuje **T2** a bol úplne
reprodukovaný: compile/help/smoke/official `exit 0`, smoke
`physics_executed=false` s 10/10 input checks a nulovými počtami, official
`pair_pass=true`, `14/14` correction checks, presne dve opravené parity polia,
chránený snapshot identický `EBD4021F…FD97D`, a field parita s reference `017`
má **nula** rozdielov po jedinej povolenej normalizácii `runtime_seconds`. Oba
negatívne guardy sú fail-closed (`exit 2`, správna správa, žiadny success/failure
JSON). T1 numerická línia je forenzne potvrdená proti primárnym rawom na plnú
presnosť (accepted_solve invariantný; same-matrix `EXACT`, rank 104, tri
iterácie; drivery `.05` a `.15` presne podľa očakávaní; holdout nezávislý a
PASS; PF-127/PF-128 formálne false-negatives bez STOP a bez nového verdiktu).
Účtovanie `33 + 6 = 39/45` a NID `9/9` sú nezávisle rekonštruované a
konzistentné; K4 `60/100` sa nemení. Jediné obmedzenie je deklarovaná tier
hranica — numerika `131/142/143/144` ostáva **T1** — ktoré definícia
`AGREE_IN_SCOPE` výslovne zahŕňa („T1 numerical lineage PASS"). Nenašiel sa
žiadny evidence gap (nie `REVIEW_EVIDENCE_GAP`) ani zmena vedeckých hodnôt,
nepravdivá aktívna brána či chybné účtovanie (nie `DISAGREE`).

## Vyhlásenie autority

Tento externý posudok nemení projektový `PASS/REVIEW/STOP`, C3 register ani
K4 score. Je to read-only nezávislé odporúčanie. Autoritatívne spracovanie a
akúkoľvek zmenu registra alebo skóre vykonáva iba hlavný orchestrátor po
vyhodnotení tohto posudku.
