# Externý audit — `EA-20260722-040-SM-CONSTRAINT-FUNCTION-B0-B2`

## Povinné metadáta

- Auditor/model/verzia: `/root/ea040_external_audit`; Codex / GPT-5.6,
  `external_auditor` profile, reasoning `high`
- Dátum a časová zóna: `2026-07-23`, `Europe/Bratislava`
- Audit mode: `BLIND`
- Package revision: `SEALED_READY_FOR_AUDIT`
- SHA-256 strojového manifestu `01_MANIFEST_SHA256.tsv`:
  `3C4CF33C6C04BFC44C6425AEAFC9D5B062B8E4B64E1A39FB9D117A42034FB4A8`
- Overenie manifestu: `PASS` — `15/15` manifestových položiek, source/copy
  parita `15/15`, package `22`, response `1`, `REPRO=0`, runtime-map rows
  `0`, duplicate physical hash groups `0`, temp files `0`
- Overenie rulesetu/configu: `PASS`; všetkých päť package hashov súhlasí s
  charterom a packaged role manifestom; auditor
  `/root/ea040_external_audit != /root` kurátor a
  `!= /root/ea038_external_audit` curatorial reviewer
- Najvyššia dosiahnutá úroveň: `T1_PRIMARY_FORMULA`
- Oficiálna vetva bez odchýlky: `NOT_RUN` — balík nemá scientific runtime
- Deklarované odchýlky: `0`

## Prostredie

- OS/architektúra: `Microsoft Windows 10.0.26200`, `x64`; proces `x64`
- PowerShell: `7.6.3`
- Python: `NOT_RUN / NOT_QUERIED`
- NumPy: `NOT_USED / NOT_QUERIED`
- SciPy/SymPy: `NOT_USED / NOT_QUERIED`
- BLAS/LAPACK: `NOT_USED / NOT_QUERIED`

## Procesný ledger

| Fáza | Presný príkaz | Exit code | Wall time | Output SHA-256 | Stav |
|---|---|---:|---:|---|---|
| manifest preflight | `pwsh -NoProfile -File External_Audits\TOOLS\Test-ExternalAuditPackage.ps1 -PackagePath External_Audits\PACKAGES\EA-20260722-040-SM-CONSTRAINT-FUNCTION-B0-B2` | `0` | `2.4 s` | `N/A` — iba stdout; generated JSON súbor nevznikol | `PASS 96/96` |
| smoke | `NOT_RUN` | `N/A` | `N/A` | `N/A` | balík nemá runtime |
| official audit | `NOT_RUN` | `N/A` | `N/A` | `N/A` | ručný T1 formula audit |
| declared deviation | `NONE` | `N/A` | `N/A` | `N/A` | `0 odchýlok` |

## Odpoveď na presnú otázku

1. **Áno v deklarovanom T1 rozsahu.** Constraint-first mapa je lokálna na
   úrovni použitých stavov a energetickej projekcie, rozmerovo konzistentná
   a jej backgroundový ledger zachováva energiu. Nie je to ešte úplný
   kovariantný collision/recoil operátor ani odvodená mikrofyzika.
   `[OBSERVED_IN_PRIMARY, INDEPENDENTLY_RECOMPUTED]`
2. **Áno pre diskrétnu eventovú vetvu.** Oddelenie invariantnej miery
   `R_J` a energie udalosti `E_J` je nutné; background určuje iba ich súčin
   `Q_D=R_JE_J`. Platí však obmedzenie F-001 pre distribúciu energií
   udalostí. `[INDEPENDENTLY_RECOMPUTED]`
3. **Áno.** `r_s=(2/g_*)epsilon_J^2` a
   `beta_s=r_s/(1+r_s)` sú správne označené ako rekonštruovaná hypotéza na
   `0<=epsilon_J<=1`. Faktor `2/g_*` vstupuje raz ako podmienený high-T
   birth ratio `Q_s/Q_M`, nie ako druhý energetický multiplikátor ani ako
   pozorovaný zákon. `[OBSERVED_IN_PRIMARY, INDEPENDENTLY_RECOMPUTED]`
4. **Áno.** B0 je iba `ANALYTIC_CONDITIONAL_SCREEN`; B1 je iba
   `CONDITIONAL_FUNCTION_FAIL` pre spoločnú 1280-e-foldovú backgroundovú
   mapu a prompt identifikáciu energie udalosti s priemernou bunkovou
   energiou. Nejde o všeobecný STOP pary, S-M ani K4.
   `[OBSERVED_IN_PRIMARY, INDEPENDENTLY_RECOMPUTED]`
5. **Áno ako otvorenie ďalšieho analytického kroku, s obmedzením.** B2
   oprávňuje constraint-first tvorbu konečnej, vopred odôvodnenej množiny
   eventových kandidátov, ale sám nedokazuje jej neprázdnosť, konečnosť ani
   žiadny konkrétny `R_J`/`E_J`. Pred tvorbou kandidátov treba uzavrieť, či
   `E_J(Y)` je deterministická energia pri danom `Y`, alebo rozšíriť
   kandidátny kontrakt o distribúciu eventových energií. Relaxačný a iný
   prompt operátor zostávajú samostatne otvorené.
   `[INFERRED_FROM_PROJECT_DOCS, INDEPENDENTLY_RECOMPUTED]`

## Presný scope B0/B1/B2

- **B0** potrebuje: jeden parent drain rozdelený na prompt `s` a `M`;
  `Q_s=beta_sQ_D`, `Q_M=(1-beta_s)Q_D`; porovnanie produktov pri narodení
  v úzkom poslednom exit/rethermalization intervale; približne konštantné
  `y_e=y_x`; identifikáciu `E_cell/E_P=rho_e/rho_P=y_x`; doménu
  `0<=y_x<=1`; rekonštruovaný kandidát `r_s=(2/g_*)y_x^2`; a
  `2/g_*` iba ako podmienený high-T endpoint. Tepelný prepis
  `y_x~(T_x/T_P)^4` je osobitný comparator, nie súčasť jadrovej identity.
- **B1** pridáva: `e` je energia nesúca tú istú A13 zrýchlenú vetvu;
  `w_e=-1+delta` na testovanom intervale; `delta=0.02297`; `y_i=1`;
  `N=1280` po poslednú relevantnú produkciu; expandujúcu vetvu `H>0`,
  `rho_e>0`; nezáporný drain `Q_D>=0`; a rovnakú prompt mapu
  `beta_s proportional y_e^2`. Záver sa týka iba neschopnosti obnoviť
  relevantný high-T birth ratio v tomto spoločnom scope.
- **B2** sa týka iba diskrétnej eventovej vetvy. Vyžaduje oddeliť event rate
  a event energy, zachovať lokálny energy/recoil ledger a neskôr dodať
  vyššie momenty/noise kernel. Nevyberá Planckovské udalosti, neurčuje
  `R_J`, `E_J` ani causal collection region, nedokazuje Poissonovský šum a
  nevylučuje relaxation/collision alebo inú prompt vetvu.

## Overenie tvrdení

| Tvrdenie | Tag dôkazu | Primárny zdroj path + riadok/pole | Metóda | Výsledok |
|---|---|---|---|---|
| Package a ruleset integrita | `INDEPENDENTLY_RECOMPUTED` | `01_MANIFEST_SHA256.tsv`; `00_SCOPE_AND_READ_ORDER.md`; `EVIDENCE/009`–`013` | R6 preflight, county a SHA-256 | `PASS`; `96/96`, hashe exact |
| Produktový energy ledger | `INDEPENDENTLY_RECOMPUTED` | `EVIDENCE/014`, riadky 584–615 a 685–711 | algebraická suma zdrojov | `-Q_D+beta Q_D+(1-beta)Q_D-Gamma_C rho_M+Gamma_C rho_M=0` |
| Rozmery B2 | `INDEPENDENTLY_RECOMPUTED` | `EVIDENCE/014`, riadky 860–879 | prirodzené jednotky | `[R_J]=E^4`, `[E_J]=E`, `[Q_D]=E^5`; `nu_J`, `epsilon_J`, `j_D` bezrozmerné |
| Slabý prompt limit | `INDEPENDENTLY_RECOMPUTED` | `EVIDENCE/014`, riadky 885–904 | `beta=r/(1+r)=r+O(r^2)` | `j_s=beta nu_J epsilon_J ~ (2/g_*)nu_J epsilon_J^3` |
| Integrovaná energia | `INDEPENDENTLY_RECOMPUTED` | `EVIDENCE/014`, riadky 918–935 | násobenie continuity rovnice `a^3` a integrácia | znamienka aj tlaková práca sú správne |
| B0 birth ratio | `INDEPENDENTLY_RECOMPUTED` | `EVIDENCE/014`, riadky 735–790 | dosadenie definície `beta` | `beta/(1-beta)=r=(2/g_*)y_x^2`; iba deklarovaný prompt kandidát |
| B1 hranica | `INDEPENDENTLY_RECOMPUTED` | `EVIDENCE/014`, riadky 792–852 | integrácia `d ln rho/dN<=-3delta` | `3delta N=88.2048`; `log10 y_x<=-38.30`; štvorcové potlačenie `<=10^-76.6` |
| Identifikovateľnosť backgroundu | `INDEPENDENTLY_RECOMPUTED` | `EVIDENCE/014`, riadky 854–913 | faktorizačná algebra | background fixuje iba `R_JE_J`; prompt yield závisí osobitne od event energy |
| Jediné použitie `2/g_*` | `OBSERVED_IN_PRIMARY` | `EVIDENCE/014`, riadky 885–898; `EVIDENCE/006`, A12 | formula-lineage kontrola | `PASS`; raz v birth ratio, následná evolúcia nie je druhé vetvenie |
| Oddelenie prompt/sequence/cohort | `OBSERVED_IN_PRIMARY` | `EVIDENCE/014`, riadky 584–668 | mechanizmová term mapa | `PASS`; prompt `e->s+M`, lokálny tok `M->C`, kohortové `d_C` iba diagnostika |

## Rozdiely generated JSON voči reference

`NOT_APPLICABLE`. Balík je statický T1, neobsahuje reference ani generated
JSON a počas auditu nevznikol generated JSON súbor.

## Nálezy

### F-001 — `MATERIAL`

- Typ: `PHYSICAL / FORMAL / SCOPE-TIER`
- Presný zdroj: `EVIDENCE/014`, riadky 860–903 a 937–943
- Pozorované: B2 zapisuje jednu hodnotu `E_J(Y)` a následne
  `Q_s=beta_s(E_J/E_P)R_JE_J`. To je uzavreté pre deterministickú
  (monochromatickú) energiu udalosti pri danom `Y`, nie všeobecne pre
  udalosti s rozdelením energií.
- Očakávané: pred tvorbou kandidátov explicitne deklarovať deterministický
  scope alebo použiť marked-event mieru. Pri distribúcii platí schematicky
  `Q_D=R_J <E>` a `Q_s=R_J <beta(E/E_P)E>`; pre nelineárne `beta` nemožno
  všeobecne nahradiť druhý priemer hodnotou `beta(<E>/E_P)Q_D`.
- Dopad na package tier: žiadny; zostáva `T1_PRIMARY_FORMULA`.
- Dopad na fyzikálny scope/verdict: nemení rozmerovú kontrolu, conservation,
  B0/B1 ani záver `MACRO_IDENTIFIABILITY=PRODUCT_ONLY`. Obmedzuje tvrdenie,
  že dvojica funkcií `R_J(Y),E_J(Y)` je úplný minimálny popis všetkých
  diskrétnych eventových kandidátov.
- Minimálny reprodukčný test: porovnať dve eventové populácie s rovnakým
  `R_J<E>` a odlišným rozptylom energie; kvôli `beta(E)E ~ E^3` v slabom
  limite dajú odlišné `Q_s`.
- Navrhovaná oprava: pridať pred B2 candidate generation invariant
  `EVENT_ENERGY_STATUS=DETERMINISTIC_GIVEN_Y`, alebo rozšíriť konečný
  kandidátny kontrakt o vopred odôvodnenú distribúciu/markové momenty.

Iné package-integrity, dimensional, conservation, algebraické,
documentation alebo tier odchýlky som nenašiel.

## Nonclaims a odchýlky

- Audit neodvodzuje ani nevyberá `R_J`, `E_J`, `Gamma_D`, `Gamma_C`, clock,
  causal collection region, matrix element, collision operator alebo noise
  kernel.
- Nepotvrdzuje existenciu vzácnych Planckovských udalostí ani nepovoľuje
  `epsilon_J=1`.
- Nepovyšuje reconstructed `beta_s` na jedinečný alebo odvodený zákon a
  nepoužíva `Delta N_eff=0.0535`, `0.90 K` či `53 GHz` ako cieľ.
- Nevykonáva T2 reprodukciu, computed verdict, Python, fit ani likelihood.
- Nemení `K4=60/100`, `P5=3.5/6`, `P5.4=NOT RUN`, D03/D04–D11 ani blokovanie
  G8/G9.
- Deklarované odchýlky od package postupu: `0`.

## Neautoritatívne odporúčanie

`AGREE_WITH_LIMITATION`

Mapa, B0/B1 scope, dimensional/conservation algebra aj B2 product-only
identifikovateľnosť sú konzistentné. Pred tvorbou eventových kandidátov treba
uzavrieť F-001 ako explicitný deterministický-domain invariant alebo ako
markovú distribúciu energií; nejde o dôvod na širší STOP.

## Vyhlásenie autority

Tento externý posudok nemení projektový `PASS/REVIEW/STOP`, skóre ani hĺbku.
Autoritatívne spracovanie vykonáva iba hlavný orchestrátor v novom súbore
odpovede.

## Handoff

```text
TASK_ID=EA-20260722-040-SM-CONSTRAINT-FUNCTION-B0-B2
ROLE=external_auditor
ROLE_CONFIG_SHA256=6B1AF6C55E725E7A2332F30F0337713F1A7E254402E7F8A5A64BB689569C9A14
READ_SET_CONFIRMED=SEALED_PACKAGE_ONLY_PLUS_DECLARED_R6_PREFLIGHT
INPUT_HASH_CHECK=PASS_15_OF_15
FILES_CHANGED=External_Audits/RESPONSES/EA-20260722-040-SM-CONSTRAINT-FUNCTION-B0-B2/00_AUDITOR_AUDIT.md
PYTHON_PROCESSES=0
FINDINGS_BY_SEVERITY=MATERIAL_1; OTHER_0
NONCLAIMS=PRESERVED
RECOMMENDATION=AGREE_WITH_LIMITATION
NEXT_ROLE=main_orchestrator
DONE_WHEN=main_orchestrator_assesses_response_without_rewriting_sealed_package_or_audit
```

`LIVE_SCIENTIFIC_ARTIFACTS=0`; `LIVE_CENTRAL_REGISTERS_UPDATED=0`;
`FILES_CHANGED_TOTAL=1` response; `AUDIT_PACKAGE_COPIES=0` nových.
