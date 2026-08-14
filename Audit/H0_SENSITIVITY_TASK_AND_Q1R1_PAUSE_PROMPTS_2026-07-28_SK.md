# Prompty: uzavretie Q1R1 auditu a samostatný `H0` sensitivity audit

**Dátum:** 2026-07-28  
**Stav:** `PROMPT_ONLY / NO_RUN_AUTHORIZATION / NO_VERDICT_CHANGE`

## 1. Prompt pre aktuálne bežiacu Q1R1 úlohu

```text
Dokonči iba aktuálne rozbehnutý nezávislý statický audit skriptu 291S.
Po jeho výsledku sa zastav a podaj stručný súhrn:

1. PASS alebo presné blockery statického auditu;
2. ktoré súbory boli od posledného handoffu zmenené;
3. či je 291S bezpečný a pripravený na SelfTest;
4. aktuálne počítadlá source operácií, technických zlyhaní a balíkov;
5. najmenší ďalší krok.

Nespúšťaj SelfTest, sieťový GET, redirect ani nový V4 nástupca. Neotváraj
ďalší fyzikálny atóm a nemeň PASS/REVIEW/STOP, skóre alebo hĺbku. Cieľom je
iba uzavrieť už rozbehnutý read-only statický audit a vytvoriť bezpečný bod
na rozhodnutie používateľa.
```

Ak úloha ani po približne 15 minútach neposkytne nový stav auditu, možno ju
zastaviť. Statický audit je read-only a dá sa znovu vykonať bez straty
vedeckého výsledku. Už zapísané artefakty a ledger sa nesmú mazať ani
vracať späť.

## 2. Prompt pre novú samostatnú úlohu `H0`

```text
Pracuj v D:\Teoria ako fyzikálny a numerický auditor. Cieľom je pripraviť a
po splnení všetkých fail-closed pravidiel vykonať minimálny trojbodový audit
citlivosti backgroundu H0 na legacy steam/Delta N_eff. Q1R1 nie je
závislosťou tejto podmienenej backgroundovej úlohy a nesmie ju blokovať.

Najprv vykonaj celý povinný bootstrap podľa D:\Teoria\AGENTS.md. Načítaj
najmä:

- tracks/00_PROJECT_OPERATING_SYSTEM.md
- tracks/00_CURRENT_EXECUTION_PLAN.md
- tracks/00_READ_FIRST.md
- najnižší relevantný work plan a active handoff
- tracks/METHODOLOGY/05_WORKING_Methodology_Rules_and_Question_Register_SK.md
- Audit/V3_18_PT1_CONDITIONAL_STEAM_AND_H0_ENVELOPE_PROPOSAL_2026-07-28_SK.md
- Audit/Q1R1_RUNTIME_AND_H0_S8_DEPENDENCY_AUDIT_2026-07-28_SK.md

Pred akýmkoľvek Python artefaktom načítaj celý DNR register, error patterns,
formal error ledger, execution limits a baseScripts ownership/version
registre. Python je fail-closed: najprv Markdown preregistrácia, SHA receipt,
nezávislý statický audit a až potom explicitné RUN_AUTHORIZED.

Vedecká otázka:

Ak sa zachová rovnaký backgroundový model, delta, lambda, hustotné definície,
jednotky a kalibračná kotva, aké hodnoty H0, r_d a theta_* alebo použitej
ekvivalentnej akustickej kotvy vzniknú pre:

Delta N_eff = 0
Delta N_eff = 0.02675
Delta N_eff = 0.0535

Najprv urob lineage audit historickej pipeline, ktorá uvádzala
H0 približne 66.37 km/s/Mpc. Povinne rozlíš:

1. či H0 pipeline skutočne rieši z nezávislej observačnej kotvy, alebo je H0
   iba zadaný vstup, ktorý sa následne znovu exportuje;
2. či Delta N_eff vstupuje iba do fyzikálne správnych radiačných a
   sound-horizon členov;
3. či homogénny background po oprave KMPC neobsahuje Fourierov mód k ani
   fixné K_MPC=0.05;
4. či sa pri zmene Delta N_eff potichu nerefitujú delta, lambda, Omega_m,
   amplitúda paliva, zakrivenie alebo iný parameter;
5. či sa používajú konzistentné jednotky H0 v km/s/Mpc a Mpc^-1.

Povinný STOP/REVIEW pred numerikou:

- Ak H0 je iba vstup, nevytváraj falošný interval. Vráť
  STOP_H0_PIPELINE_NOT_SOLVING_H0 a presne uveď, ktorá nezávislá rovnica alebo
  observačná kotva chýba.
- Ak background zostáva závislý od perturbatívneho k, vráť
  REVIEW_BACKGROUND_K_DEPENDENCE_UNRESOLVED a nič nefituj.
- Ak steam normalization nie je oddeliteľná bez zmeny ďalších parametrov,
  vráť REVIEW_STEAM_SENSITIVITY_NOT_IDENTIFIABLE.
- Technická chyba nie je fyzikálny STOP; zapíš ju do formal error ledgera a
  zachovaj chybný artefakt podľa DNR pravidiel.

Pred behom zapíš ľudskou rečou očakávania:

- všetky výstupy musia byť konečné a fyzikálne kladné;
- bod Delta N_eff=0.0535 má reprodukovať historický výsledok iba v rozsahu
  odôvodnenom numerickou a lineage toleranciou, nie povinne presne 66.37;
- smer monotónnosti H0 vopred nevyhlasuj za PASS podmienku, kým ho
  analyticky neodvodíš;
- nulový bod znamená steam-null sensitivity endpoint, nie tvrdenie, že
  teória predpovedá nulovú paru.

Implementačný rozpočet:

- najviac 1 nový versioned base modul a 1 tenký runner;
- najviac 5 live vedeckých artefaktov pre celý atóm;
- žiadne zmeny v theory/;
- každý proces má externý timeout, kontrolu najneskôr každých 10 s a segment
  najviac 60 s;
- nový runner má interný --max-runtime-seconds, checkpointy, collision guard
  a publikuje official output presne raz;
- najprv smoke, potom tri body, potom nezávislá konvergencia/nulový limit;
- nepoužívaj staré DNR skripty ako autoritatívny runner.

Použi math_script_auditor na nezávislý statický audit pred prvým procesom a
physics_track_auditor na read-only interpretáciu výsledku. Iba hlavný agent
smie prijať autoritatívny verdict. Po uzavretom atóme použi
progress_goal_reviewer.

Výsledok môže dostať iba stav BACKGROUND_SENSITIVITY_ENVELOPE. Nesmie byť
označený ako posterior, confidence interval, plný CMB fit alebo predikcia
teórie. Nespúšťaj S8, P5.4, G8, G9, CLASS patch ani likelihood.

Na začiatku oznám presný plánovaný zoznam a počet súborov. Na konci uveď
LIVE_SCIENTIFIC_ARTIFACTS, LIVE_CENTRAL_REGISTERS_UPDATED, TOTAL_FILES_CHANGED
a AUDIT_PACKAGE_COPIES. Všetky trvalé závery zapíš do Markdownu; strojový
JSON môže byť iba príloha.
```

## 3. Procesný výkaz

```text
LIVE_SCIENTIFIC_ARTIFACTS: 0
LIVE_AUDIT_ARTIFACTS: 1
LIVE_CENTRAL_REGISTERS_UPDATED: 0
TOTAL_FILES_CHANGED: 1
AUDIT_PACKAGE_COPIES: 0
PYTHON_PROCESSES: 0
```
