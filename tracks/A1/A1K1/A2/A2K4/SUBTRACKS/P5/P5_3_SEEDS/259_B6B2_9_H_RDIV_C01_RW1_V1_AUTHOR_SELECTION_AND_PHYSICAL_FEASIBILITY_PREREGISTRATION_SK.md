# B6b-2.9 — H_RDIV-C01-RW1-v1 autorov výber a preregistrácia fyzickej feasibility

**Task:** `A2K4-B6B2-9-H-RDIV-C01-RW1-V1-PREREG-20260727-143`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.9`  
**Autor teórie a výberu:** Martin Jambor  
**Formalizácia:** Codex, hlavný orchestrátor  
**Stav:** `FINAL_PREREGISTRATION / PASS_FOR_FREEZE / C01_RW1_AUTHOR_SELECTED_E3_TEST_BRANCH / NO_RUN / NO_PYTHON`  
**Nadradený blocker:**
`PHYSICAL_CHI_THRESHOLD_DYNAMICS_AND_RESET_NOT_SELECTED_OR_DERIVED`

## 1. Autorovo rozhodnutie a jeho presný rozsah

Martin Jambor po prijatí mapy C01–C10 a výsledku H_BIO-ECHO-v1 rozhodol:

```text
pokracuj s C01-RW1
```

V kontexte dokumentu 256 ide o explicitný výber
`RDIV-C01-RW1` ako prvej `E3_PROVISIONAL` testovacej fyzickej podvetvy.
Výber znamená pokračovať s kumulatívnou lokálnou pre-event prácou prestavby
nového rozhrania. Neznamená:

- fyzickú pravdivosť C01;
- hotový `R_div` alebo P4 physical witness;
- autorovo určenie konkrétneho mikroskopického carrieru, `P_rec` alebo
  hodnoty `W_*`;
- uzavretie D03, MF1, P5.3, P5.4 alebo A2-K4;
- zmenu skóre, hĺbky alebo povolenie Pythonu.

Ostatné C02–C10 zostávajú zachované ako neaktívne zálohy. Ich pokusový
counter ani verdict sa výberom C01 nemení.

## 2. Čo je výberom C01 zmrazené

Pre jeden aktívny parent cyklus sa testuje:

```text
W_rec(tau_birth) = 0,
D_u W_rec = P_rec(Y_div^-) >= 0,
W_* > 0,
D_u W_* = 0 počas parent cyklu,
chi_div = W_rec / W_*,
chi_c = 1.
```

Event je prvý jednoduchý transverzálny upward crossing `chi_div=1` v
regular v1 mantineli dokumentu 254. Preto pri frozen `W_*` platí

```text
D_u chi_div = P_rec / W_* >= 0.
```

`W_rec` znamená iba kumulatívnu prácu, ktorá už bola fyzicky vykonaná alebo
nevratne zaviazaná na prípravu konkrétneho nového rozhrania. Nie je to
proper-time timer, zásoba paliva, energia budúcich produktov, realizovaný
event count ani makroskopický expansion output.

## 3. Povinný lokálny carrier proti skrytému history clocku

Samotný zápis integrálu

```text
W_rec(tau) = integral P_rec d tau
```

nie je fyzický carrier. Kandidát musí v lokálnom pre-event stave obsahovať
fyzicky realizovaný stav `Z_rec`, ktorý nesie pamäť prípravy rozhrania.
Prípustná je napríklad lokálna konfigurácia väzieb, rozhrania, deformácie
alebo iný konečný state record, ale táto preregistrácia nijakú z nich
nevyhlasuje za pravdivú.

Povinná identifikovateľnosť je:

```text
W_rec = W[Z_rec]
```

alebo ekvivalentná lokálna Markovská augmentácia, z ktorej možno `W_rec`
určiť bez globálnej histórie. Ak dve fyzicky identické lokálne konfigurácie
majú rozdielne `W_rec` iba preto, že agent pridal nepozorovateľný integrátor,
ide o `REVIEW_HIDDEN_HISTORY_CLOCK`, nie o physical witness.

`Z_rec` musí byť lokálny difeomorfne korektný state na causal supporte
parent bunky. Biologický comparator smie motivovať požiadavku pamäte, ale
nesmie určiť jej Planckovskú identitu.

Fyzický witness musí navyše odvodiť future-directed jednotkovú parent
worldline tangentu `u_cell`, regular cell congruence a invariantnú lokálne
konečnú occupation measure `dmu_cell` alebo jej proper-density ekvivalent.
Analógia alebo všeobecný interface model sa nepočíta ako physical witness,
kým nie je explicitne zmapovaný do `Y_div`, `u_cell` a `dmu_cell`.
Chýbajúce odvodenie je
`REVIEW_CELL_CONGRUENCE_AND_MEASURE_OPEN`, nie formálny PASS eventovej miery.

## 4. Zdroj, rezervoár a conservation ledger

`P_rec` musí mať lokálny pre-event pôvod v causal energy/current alebo v
stress-work kanáli. Bez zvolenia mikrofyziky sa zavádza iba účtovný obal:

```text
E_res >= 0,                 lokálny spotrebovateľný rezervoár,
S_in  >= 0,                 lokálny causal incoming power,
L_ext >= 0,                 export/strata mimo RW1 work channel,
P_rec = P_store + P_diss + P_RW1export >= 0,
D_u E_res = S_in - P_rec - L_ext.
```

Kanály `P_store`, `P_diss` a `P_RW1export` sú nezáporné a vzájomne disjunktné:
ide o uloženú interface/configuration energiu, účtovanú disipáciu a prípadný
export, ktorý je sám súčasťou RW1 work channelu. `L_ext` obsahuje iba straty
mimo týchto troch kanálov. Nijaká položka `P_rec` sa nesmie zopakovať v
`L_ext`; nijaká položka sa nesmie započítať dvakrát medzi zložkami `P_rec`.

Celý lokálny stress-energy/current ledger musí preukázať, kam každý kanál
vstupuje. `W_rec` je iba cumulative work ledger, nie ďalší energy stock,
ktorý možno pripočítať k `E_res` alebo k destináciám `P_rec`.
Nezápornosť rezervoára je viability podmienka: pri `E_res=0` musí platiť
`P_rec+L_ext<=S_in`, takže účtovný obal nemôže pokračovať do záporného
rezervoára.

Presná source-off definícia je:

```text
S_in = 0 a nie je dostupný účtovaný spotrebovateľný lokálny rezervoár/current
  => P_rec = 0
  => D_u W_rec = 0.
```

Ak `S_in=0`, ale `E_res>0`, príprava smie dočasne pokračovať iba
konzervatívnym čerpaním `E_res`; nejde ešte o úplný source-off. Kandidát musí
zaručiť, že integrované `P_rec+L_ext` neprekročí počiatočný rezervoár plus
integrovaný vstup.

## 5. Completion work `W_*`

`W_*` je kladná práca potrebná na dokončenie jedného konkrétneho budúceho
rozhrania. Musí byť predikovateľne určená z lokálneho pre-event stavu
najneskôr na začiatku parent cyklu a potom zmrazená.

Prípustný fyzický pôvod môže používať lokálnu prácu na väzbu, interface
tension a geometriu nového rozhrania, ale musí explicitne odvodiť jednotku
energie a účtovnú konvenciu. Schematický obal

```text
W_* ~ integral_(Sigma_new) gamma_I dA + W_link + W_other
```

je iba dimensional/source template. `gamma_I`, `Sigma_new`, `W_link` ani
`W_other` tým nie sú fyzicky zvolené. `delta=1/(<k>+C)` a `C=28` sú
bezrozmerné štrukturálne obmedzenia; samy nemôžu určiť `W_*`.

Fit `W_*` podľa `S8`, `H0`, division rate, biologického delenia alebo
post-event produktov je zakázaný.

## 6. Event, parent retirement a daughter reset

Pri prvom regular crossing-u `W_rec=W_*`:

```text
parent ID sa vyradí,
event dostane jedno canonical EVENT_ID_div,
dcéry dostanú nové canonical cell ID,
Z_rec,daughter = R_reset^Z(local event state),
W[Z_rec,daughter] = W_rec,daughter = 0,
chi_div,daughter = 0 < 1.
```

Rodičovský work credit sa nesmie skopírovať do oboch dcér. Energia alebo
stav, ktoré po evente fyzicky zostávajú v novom rozhraní, patria do
samostatného conservation/post-event ledgera a nesmú sa súčasne viesť ako
nový dcérsky `W_rec` kredit. Reset nie je platný, ak zdedený `Z_rec` stále
dáva `W[Z_rec]>0`. Táto preregistrácia neotvára `C_x`, `Pi_J`, paru ani
completion produkty.

## 7. Predregistrovaný no-Python feasibility screen W0–W12

| ID | Kontrola | PASS podmienka | Fail-closed význam |
|---|---|---|---|
| `W0` | autor a epistemická trieda | C01-RW1 je autorom vybraná E3 testovacia podvetva, nie fakt alebo closure | overclaim=`PROCESS_CONTRACT_FAILURE` |
| `W1` | typ a jednotky | `[W_rec]=[W_*]=E`, `[P_rec]=E/T`, `chi_div` je lokálny bezrozmerný skalár a `chi_c=1` | nedefinované=`REVIEW_ILL_TYPED`; dokázaná nezhoda=`PRECHECK_EXCLUDED_SCOPE` |
| `W2` | fyzický carrier | lokálny `Z_rec` alebo ekvivalentný finite state fyzicky nesie informáciu potrebnú na určenie `W_rec` | iba nepozorovateľný integrátor=`REVIEW_HIDDEN_HISTORY_CLOCK`; žiadna carrier trieda=`REVIEW_PHYSICAL_CARRIER_OPEN` |
| `W3` | lokálny pôvod výkonu | `P_rec>=0` je odvodený z pre-event causal current/stress-work/reservoir kanála | chýbajúci pôvod=`REVIEW_POWER_PROVENANCE_OPEN`; globálny/post-event zdroj=`PROCESS_CONTRACT_FAILURE` |
| `W4` | conservation | existuje lokálny energy-momentum ledger bez double countu `W_rec` a energy stocku | chýbajúci ledger=`REVIEW_CONSERVATION_LEDGER_OPEN`; dokázaná energia zadarmo=`PRECHECK_EXCLUDED_SCOPE` |
| `W5` | source-off | bez externého vstupu aj dostupného účtovaného rezervoára je `P_rec=0`; uložený rezervoár sa smie iba konzervatívne vyčerpať | samovoľný rast=`PRECHECK_EXCLUDED_SCOPE` |
| `W6` | threshold provenance | `W_*>0` má lokálny energetický pôvod, je určený pred eventom a počas cyklu frozen | fitted/moving/post-event threshold=`PROCESS_CONTRACT_FAILURE`; pôvod otvorený=`REVIEW_THRESHOLD_ENERGY_OPEN` |
| `W7` | regular first passage a cell measure | `P_rec/W_*>0` pri prvom crossing-u; trajektória je v regular v1 absolútne spojitá; fyzicky odvodené `u_cell`, regular congruence a invariantné lokálne konečné `dmu_cell` dávajú parent count once-only | chýbajúce cell objekty=`REVIEW_CELL_CONGRUENCE_AND_MEASURE_OPEN`; jump/tangent/multiple root=`OUTSIDE_H_RDIV_MF1_V1_REGULAR_SCOPE`; repeated count=`REVIEW_DOUBLE_COUNT` |
| `W8` | nekruhovosť | `P_rec,W_*,Z_rec` nepoužívajú `R_div`, `Q_D`, realizovaný event, produkty, `Theta_cell`, `a`, `H0`, `k`, `S8` ani biology target | kruh/leakage=`PROCESS_CONTRACT_FAILURE` |
| `W9` | daughter semantics | parent retirement, new daughter IDs a lokálna `R_reset^Z` dá `W[Z_rec,daughter]=W_rec=0`; residual interface/configuration energy ide do oddeleného conservation/post-event state bez work-credit kópie | same-ID, zdedené `W[Z_rec]>0` alebo double credit=`PRECHECK_EXCLUDED_SCOPE` v1 |
| `W10` | physical nonzero witness | aspoň jeden explicitný lokálny pred-event stav má identifikovaný carrier, odvodené `P_rec,W_*`, disjunktný conservation ledger, fyzické `u_cell`/congruence/`dmu_cell`, reachable regular crossing a fyzický `Z_rec` reset | iba algebraický toy=`REVIEW_NO_PHYSICAL_RW1_WITNESS`; chýbajúca cell measure=`REVIEW_CELL_CONGRUENCE_AND_MEASURE_OPEN` |
| `W11` | nulové limity a quotient | bez vstupu aj dostupného rezervoára a pri `W_rec<W_*` nevznikne nový regular crossing; `W_*` musí byť kladné, konečné a fyzicky zdrojované; current-dose/link-count opis sa quotientuje s C01, ak nemení prediction pri rovnakom fyzickom stave | `W_*=0` alebo undefined=`REVIEW_ILL_TYPED / REVIEW_THRESHOLD_ENERGY_OPEN`, nie null limit; false division=`REVIEW_NULL_LIMIT_FAILURE`; duplicate branch=`QUOTIENT_TO_C01` |
| `W12` | scope guard | bez `C_x`, `Pi_J`, steam/completion, S8/H0 fitu, P5.4, Pythonu, skóre alebo run zmeny | okamžitý fail-closed návrat |

## 8. Zmrazené rozhodovacie vetvy

```text
Ak W0-W9 a W11-W12 prejdú iba ako mantinely, ale W10 nemá fyzický witness:
  PASS_RW1_PHYSICAL_FEASIBILITY_CONTRACT_ONLY
  / REVIEW_RW1_PHYSICAL_CARRIER_POWER_THRESHOLD_CONSERVATION_CELL_MEASURE_AND_RESET_OPEN.

Ak current corpus alebo nový primárny zdroj dá explicitný Z_rec, P_rec, W_*,
disjunktný conservation ledger, fyzické u_cell/cell congruence/dmu_cell a
fyzický Z_rec reset spĺňajúci W0-W12:
  CANDIDATE_PHYSICAL_RW1_WITNESS_FOUND_PENDING_INDEPENDENT_AUDIT;
  ešte nie P4 closure ani zvýšenie skóre.

Ak konkrétna podtrieda potrebuje energiu zadarmo, post-event príčinu,
double credit alebo fitted threshold:
  PRECHECK_EXCLUDED_SCOPE iba pre túto podtriedu.

Ak sa v current corpus fyzický carrier alebo energetická škála nenájde:
  REVIEW_RW1_PHYSICAL_PROVENANCE_CARRIER_POWER_THRESHOLD_CONSERVATION_CELL_MEASURE_AND_RESET_OPEN;
  nie STOP C01 ani A2-K4.

Nikdy z tohto screen-u:
  pravda C01,
  physical R_div/P4/MF1/D03 closure,
  výpočet steam/completion,
  zmena K4=60/100 alebo P5=3.5/6,
  RUN_AUTHORIZED=true alebo Python.
```

## 9. Prvý analytický execution scope po freeze

Po nezávislom audite a externom SHA receipte sa presne raz bez Pythonu:

1. preverí current corpus na fyzický `Z_rec`, causal source/stress-work,
   threshold work/geometry, disjunktný conservation ledger, fyzické
   `u_cell`/cell congruence/`dmu_cell` a fyzický `Z_rec` reset;
2. odlíši exact odvodenie, referenčný fyzikálny template a E3 voľbu;
3. zostaví prípustnú množinu
   `(Z_rec,P_rec,W_*,u_cell,dmu_cell,R_reset^Z)` alebo presný chýbajúci
   source-lineage blocker; iba analogický zdroj bez mapovania do
   `Y_div/u_cell/dmu_cell` sa nepočíta ako witness;
4. nevytvorí číselnú hodnotu len z Planckovej dimenzie, `delta` alebo `C=28`;
5. výsledok zapíše do jediného dokumentu 260 a odovzdá na nezávislý audit.

## 10. Auditný handoff

```text
TASK_ID: A2K4-B6B2-9-H-RDIV-C01-RW1-V1-PREREG-AUDIT-20260727-144
ROLE: physics_track_auditor
ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
ASSIGNED_AGENT_TASK_ID: /root/rdiv_prereg_audit_v2
ARTIFACT_AUTHOR_TASK_ID: /root task143
STATIC_AUDITOR_TASK_ID: N/A_NO_PYTHON
INTERNAL_AUDITOR_TASK_ID: /root/rdiv_prereg_audit_v2 task144
PACKAGE_CURATOR_TASK_ID: N/A_THIS_PHASE
EXTERNAL_AUDITOR_TASK_ID: N/A_THIS_PHASE
SEPARATION_OF_DUTIES_CHECK: PASS; /root task143 != /root/rdiv_prereg_audit_v2 task144
ROUTE: A1_K1_A2_K4_P5.3_B6b-2.9_H_RDIV_C01_RW1_v1
CURRENT_PHASE: FINAL_PREREGISTRATION_AWAITING_EXTERNAL_SHA_RECEIPT
ALLOWED_NEXT_ACTION: main orchestrator records the final document SHA outside this file; only then execute the frozen no-Python W0-W12 screen into document260
ALLOWED_READS: mandatory bootstrap; documents254,256-259; event ledger tasks128-143; exact current theory sources; role config/manifest
ALLOWED_WRITES: none
FORBIDDEN_ACTIONS: edit; infer unapproved carrier/P_rec/W_*; physical verdict; open C_x/Pi_J/steam/completion; Python; S8/H0/time/k fit; score/depth/run change; package work
IMMUTABLE_INPUT_PATHS_AND_SHA256: document254=9AF71F8289D6D5D1072439BF322F261480C76A3AACC8F3A55FCDE10BE9C02B99; document256=3BA221F3D88C90EC961F4B48835C046E5C2DA287DFB0130BC81E99034F8F9975; document257=E1C7E4EAE83F13736A67EECB8419F428C646716F25831A9AF139BB414918DB4A; document258=58222D1A66698FE54AAEC5C204628C789BB2EDA78D270698EE018D25E4815A61
PREREG_SHA256: RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only audit recommendation; after freeze one no-Python result document260
LIVE_FILE_BUDGET: 1 prereg + 1 append-only ledger now; later 1 result; central plan 0; package copies 0
DONE_WHEN: final bytes preserve the unambiguous author selection without overread; C01 work fraction is separated from a hidden timer and energy stock; source-off includes stored-reservoir precision; W0-W12 distinguish formal mantle, physical witness, scoped no-go and missing provenance
NEXT_ROLE: main_orchestrator
```
