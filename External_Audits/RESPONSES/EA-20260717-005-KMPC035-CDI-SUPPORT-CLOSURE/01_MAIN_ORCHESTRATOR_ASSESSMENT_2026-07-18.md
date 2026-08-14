# Hlavné orchestrátorské posúdenie — EA-20260717-005

**Dátum:** 2026-07-18  
**Posúdenie:** `AGREE_WITH_LIMITATION`  
**Projektový verdikt:** nezmenený  
**Python:** v tomto spracovaní nespustený

## Autoritatívny záver

Audit 005 nezískal oficiálny T2, pretože deklarovaný audit balíka zlyhal
fail-closed na chýbajúcich runtime závislostiach:

- `scripts/88_script_A2_K4_3b_RG_BR1_synchronous_Einstein_and_transfer_ledger.py`,
- `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/26_P5_3G7_M1_STANDARD_METRIC_SOURCE_MAP_SK.md`.

Tieto súbory boli otvorené až v official audit vetve cez runtime hash guard,
ale neboli v balíku ani v runtime dependency mape. Ide o recidívu triedy
PF-070. Statický preflight 168/168 preto nebol dostatočný dôkaz behaviorálnej
closure.

## Čo audit vecne podporil

Deklarované odchýlky D1–D3 nezávisle reprodukovali:

- 180/180 koeficientov KMPC-035;
- core a common brány;
- presný tail-failure pattern iba pre `delta_f` a `sigma_fs` pri `z=1e-2`;
- zachovanie zmrazených prahov a oddelenie cross-platform diagnostiky;
- collision-safe publish správanie vrátane nulových dočasných súborov;
- exact B1 algebraické rezíduá `0` v izolovanom D3 teste.

Tieto výsledky podporujú existujúci úzko ohraničený verdikt:

`PASS_CDI_SUPPORT_STEP_2_CORE_AND_COMMON_03_05_STABILITY_ONLY / REVIEW_CDI_SUPPORT_03_REMAINDER_UNCLOSED`

Nie sú však oficiálnym T2 reprodukčným PASS runnera 281, pretože D2 obchádza
official `run_audit` a B1 guard.

## Nové prijaté obmedzenia

1. `N1` je vysokozávažná procesná chyba delivery closure a vyžaduje nový balík,
   nie úpravu zapečateného EA-005.
2. `N3–N6` sú menšie metodické dlhy: `sum` vs `math.fsum`, diagnostický rozsah
   `base_powers`, cross-state tail reduction a nepresná `required_by` mapa.
3. `N7` je iba obmedzenie overiteľnosti tree seal z plochej kópie.
4. `N8` potvrdzuje, že spoločný equation engine znamená T2/reprodukciu, nie T3
   nezávislosť rovníc.

## Ďalší predregistrovaný krok

Vyrobiť nový balík `EA-006` s:

- oboma chýbajúcimi súbormi v presných runtime cestách a v `EVIDENCE/`;
- doplnenou negatívnou fixture pre chýbajúcu dependency;
- pravdivou mapou `required_by=smoke` vs `audit`;
- povinným behaviorálnym pre-seal behom smoke **aj official audit** v čerstvej
  kópii REPRO;
- záznamom exit codes a failure/success JSON v package history.

Poradie fyzikálnej práce sa nemení: `KMPC-036 M1 order-7 closure` → prípadný
`CDI support step 3`. Audit 005 nepovoľuje step 3, `[0,9]`, P5.4, G8 ani G9.

## Druhá kontrola hlavného orchestrátora

Druhá read-only kontrola 2026-07-18 potvrdila N1 priamo zo zapečateného zdroja:

- `full_ra_b1_preflight.py` obsahuje oba chýbajúce súbory v
  `EXPECTED_HASHES` a `build_preflight()` ich bezpodmienečne hash-otvára;
- balík ich neobsahuje v presných REPRO cestách, `EVIDENCE/` ani v
  `04_RUNTIME_DEPENDENCY_MAP.tsv`;
- projektové originály existujú a ich SHA-256 presne zodpovedajú očakávaným
  hodnotám `0F13DA6C...8364` a `7C927999...999B`;
- identifikátor `EA-006` ešte nie je obsadený.

D1–D3 sa interpretujú striktne: D1 potvrdzuje metriky z raw JSON, D2
reprodukuje koeficienty implementácie mimo official guardu a D3 potvrdzuje
vnútornú symbolickú konzistenciu po neutralizovaní hash lookupu. Ani jedna
odchýlka sama neoveruje nezávislú správnosť fyzikálnych rovníc a spolu
nedosahujú official T2 ani T3.

Behaviorálny pre-seal beh odporúčaný pre EA-006 vyžaduje spustenie Pythonu.
V aktuálnom vlákne zostáva Python zakázaný; bez neskoršieho výslovného
povolenia možno EA-006 pripraviť iba staticky a nesmie dostať označenie
`BEHAVIORALLY_PREFLIGHTED` ani `SEALED_READY_FOR_T2`.
