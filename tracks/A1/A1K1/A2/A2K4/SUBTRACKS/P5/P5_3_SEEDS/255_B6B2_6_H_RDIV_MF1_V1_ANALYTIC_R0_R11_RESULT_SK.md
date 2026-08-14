# B6b-2.6 — H_RDIV-MF1-v1 analytický výsledok R0–R11

**Task:** `A2K4-B6B2-6-H-RDIV-MF1-V1-ANALYTIC-RESULT-20260726-122`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.6`  
**Autor teórie a schválenej testovacej rodiny:** Martin Jambor  
**Vykonanie analytického testu:** Codex, hlavný orchestrátor  
**Stav:** `RESULT_FOR_INDEPENDENT_PHYSICS_AUDIT / NO_RUN / NO_PYTHON`  
**Zmrazená preregistrácia:** dokument 254, SHA-256
`9AF71F8289D6D5D1072439BF322F261480C76A3AACC8F3A55FCDE10BE9C02B99`  
**Freeze receipt:** event ledger cez task121, SHA-256
`1701E295DD20DA9BA60289866FAEC0D6A2AA52214A11AE6682954F5BCD092C4E`

## 1. Presný rozsah

Vyhodnotené boli iba zmrazené testy `R0–R11` pre regular first-upward-root
rodinu. Primárnym objektom je jednotkovo atómová counting measure

```text
N_div^FP(B)
  = sum_c 1_{tau_div(c)<infinity}
          1_B(c,tau_div(c),Y_div^-(c,tau_div)),
```

a jej dual predictable projection

```text
dR_div = (dN_div^FP)^p
```

voči filtrácii `(G_tau)`. Delta-flux formula sa použila iba ako ekvivalentná
reprezentácia jednoduchých transverzálnych koreňov.

Nebola zvolená fyzická identita `chi_div`, hodnota `chi_c`, evolution law,
cell congruence, fyzická normalizácia `dmu_cell` ani reset mapa.

## 2. Analytické kontroly

### 2.1 Jednotkový atóm a delta-flux ekvivalencia

Pre jednoduchý upward root `tau_*`, kde

```text
chi_div(tau_*) = chi_c,
D_u^- chi_div(tau_*) > 0,
chi_div(s) < chi_c v dostatočne malom ľavom okolí,
```

platí distribučná identita

```text
I_pre-first delta_Uchi(chi_div-chi_c) [D_u^- chi_div]_+ d tau
  = delta(tau-tau_*) d tau.
```

Integrál cez root je `1`. `I_pre-first` odstráni všetky neskoršie korene
rovnakej parent identity a genealogické vyradenie parenta zabráni ďalšiemu
countu. Dcéra dostáva nové ID.

### 2.2 Orientačne zachovávajúca reparametrizácia

Pre hladké `z=f(chi_div)` s `f'>0` platí pri jednoduchom koreni

```text
delta(f(chi_div)-f(chi_c))
  = delta(chi_div-chi_c)/f'(chi_c),

[D_u^- f(chi_div)]_+
  = f'(chi_c)[D_u^- chi_div]_+.
```

Faktory sa zrušia, takže event count nezávisí od hladkej rastúcej zmeny
škály alebo jednotky crossing coordinate.

### 2.3 Pozitivita a projekcia

`N_div^FP` je kladná lokálne konečná integer-valued measure. Pre každú
nezápornú predictable testovaciu funkciu `H` dual predictable projection
spĺňa

```text
E[integral H dN_div^FP] = E[integral H dR_div] >= 0.
```

Preto `dR_div>=0`. Toto neurčuje jeho fyzickú intenzitu bez fyzickej
dynamiky a ensemble law.

## 3. Výsledok R0–R11

| ID | Výsledok | Dôvod | Nepokrýva |
|---|---|---|---|
| `R0` | `PASS_LINEAGE_SCOPE` | `chi_div` zostáva samostatný E3 division coordinate; nebol stotožnený s `chi_D`, PH1 ani energy clockom | fyzický význam `chi_div` |
| `R1` | `PASS_FORMAL_TYPE_AND_UNITS` | `[delta]=U_chi^-1`, `[D_u^-chi]=U_chi/T`, `[dmu_cell]=T×count`; výsledkom je jednotkový event count | fyzickú jednotku alebo normalizáciu stavu |
| `R2` | `PASS_FORMAL_COVARIANCE_AND_REPARAMETRIZATION` | `chi_div`, `chi_c` a `D_u^-chi_div` sú skaláre; proper-time measure je invariantná; `f'>0` faktory sa zrušia | existenciu regular `u_cell`/congruence |
| `R3` | `PASS_LOCAL_SCOPE_GUARD` | objekt používa iba local pre-event state, causal support a `(G_tau)`; bez `t,a,ln a,H0,k,S8` | úplnosť fyzického local state |
| `R4` | `PASS_REGULAR_FIRST_UPWARD_ROOT` | setová definícia a simple-root delta ekvivalencia countujú prvý upward root presne raz | jump, tangent a multiple roots sú `OUTSIDE_V1_SCOPE` |
| `R5` | `PASS_CANDIDATE_GENEALOGICAL_BOOKKEEPING` | parent sa vyradí, dcéry majú nové ID a reset striktne pod prah | fyzickú reset mapu/distribúciu |
| `R6` | `PASS_FORMAL_POSITIVITY_LOCAL_FINITE` | kladná locally finite counting measure a dual predictable projection zachovávajú pozitivitu | fyzickú neprázdnosť crossing supportu |
| `R7` | `PASS_COUNT_COMPENSATOR_TYPING` | setový `N_div^FP` je realized count; `R_div` je jeho dual predictable projection voči explicitnej filtrácii | evaluovateľný physical rate law |
| `R8` | `PASS_CANONICAL_UNIT_NORMALIZATION` | doslovný once-only count má `kappa_div=1`; `kappa<0` a `kappa>1` sú v tomto v1 scope vylúčené; voľné `0<=kappa<1` je nová neschválená thinning fyzika | všeobecné multi-event alebo thinning rodiny mimo v1 |
| `R9` | `PASS_REGULAR_NULL_LIMITS` | bez active cells, bez regular first upward roots alebo iba s regular downward roots je `R_div=0` | tangent/multiple/jump nie sú null dôkaz, ale mimo v1 |
| `R10` | `PASS_FORMAL_NONZERO_INTERIOR` | explicitný regular člen nižšie dá jeden jednotkový division atom | physical `R_div` closure alebo P4 witness |
| `R11` | `PASS_SCOPE_GUARD` | nevznikol `C_x`, `Pi_J`, steam/completion, fit, P5.4 ani Python | všetky následné fyzikálne vrstvy |

## 4. Formálny člen neprázdneho v1 priestoru

Zvoľme iba na dôkaz matematickej neprázdnosti jednu parent worldline s
vlastným časom `tau`, kladnú konštantu `T_*` a

```text
chi_div(tau) = tau/T_*,
chi_c = 1,
tau_birth = 0,
tau_div = T_*,
D_u^- chi_div = 1/T_* > 0.
```

Pre `0<=tau<T_*` je `chi_div<chi_c`. Parent sa v `T_*` vyradí a každá
dcéra dostane nové ID s `chi_reset=0<1`. Setová measure má presne jeden
jednotkový atóm. Delta-flux integrál cez `T_*` je takisto `1`.

Tento príklad je

```text
FORMAL_FIRST_PASSAGE_MAPPING_WITNESS,
```

nie fyzický model bunky. `tau/T_*` nie je povolený globálny kozmický clock;
je to lokálny proper-time parametrický príklad existencie. Nie je tvrdením,
že reálna `chi_div` je vlastný čas alebo že `T_*` má fyzickú hodnotu.

## 5. Exact scoped exclusions a hranice

V zmrazenej regular `v1` rodine sú presne vylúčené iba podtriedy s:

- nescalárnou crossing coordinate použitou ako invariantný skalár;
- nezhodnými jednotkami `chi_div` a `chi_c`;
- negatívnou measure/weight alebo `kappa_div<0`;
- `kappa_div>1` pri deklarovanom one-crossing/one-event countovaní;
- resetom tej istej parent identity;
- daughter resetom `>=chi_c` bez explicitnej hysterézy/refractory state.

Skokové, tangenciálne a násobné korene nie sú tým vylúčené fyzikálne; sú
iba `OUTSIDE_H_RDIV_MF1_V1_REGULAR_SCOPE`.

## 6. Najsilnejší výsledok a zostávajúci blocker

R0–R11 dokazujú, že formálny regular first-passage mantle nie je
matematicky prázdny a môže generovať kladnú once-only division event measure.
Nedokazujú, že taký crossing existuje vo fyzickej bunke ani že vieme jeho
rate vypočítať.

Najsilnejší scoped výsledok je

```text
PASS_H_RDIV_MF1_V1_FORMAL_FIRST_PASSAGE_MANTLE_BEHAVIORAL_OPEN.
```

Zostávajúci blocker je

```text
PHYSICAL_CHI_THRESHOLD_DYNAMICS_AND_RESET_NOT_SELECTED_OR_DERIVED.
```

Otvorené zostávajú fyzická identita `chi_div(Y_div)`, reachable domain,
`chi_c`, evolution law, regular `u_cell`/congruence, fyzická cell measure a
daughter reset mapa. Preto `R_DIV_PHYSICAL_CLOSURE=OPEN`.

## 7. Stav a nonclaims

```text
H_RDIV_MF1_V1 = RESULT_FOR_INDEPENDENT_AUDIT
FORMAL_FIRST_PASSAGE_MAPPING_WITNESS = yes
R_DIV_PHYSICAL_CLOSURE = OPEN
P4_PHYSICAL_WITNESS = no
P4_PHYSICAL_WITNESS_ATTEMPTS_CONSUMED = 0
MF1_MF2_MF3_MF4 = OPEN_UNCHANGED
F01_F03 = OPEN_UNCHANGED
D03 = PARTIAL_CANDIDATE_BRIDGE_BEHAVIORAL_OPEN_UNCHANGED_PENDING_AUDIT
K4 = 60/100_UNCHANGED
P5 = 3.5/6_UNCHANGED
RUN_AUTHORIZED = false
PYTHON_PROCESSES = 0
LIVE_SCIENTIFIC_ARTIFACTS = 1
LIVE_CENTRAL_REGISTERS_UPDATED = 1
LIVE_TOTAL_FILES = 2
AUDIT_PACKAGE_COPIES = 0
```

## 8. Auditný handoff

```text
TASK_ID: A2K4-B6B2-6-H-RDIV-MF1-V1-RESULT-AUDIT-20260726-123
ROLE: physics_track_auditor
ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
ASSIGNED_AGENT_TASK_ID: /root/rdiv_prereg_audit_v2
ARTIFACT_AUTHOR_TASK_ID: /root task122
STATIC_AUDITOR_TASK_ID: N/A_NO_PYTHON
INTERNAL_AUDITOR_TASK_ID: /root/rdiv_prereg_audit_v2 task123
PACKAGE_CURATOR_TASK_ID: N/A_THIS_PHASE
EXTERNAL_AUDITOR_TASK_ID: N/A_THIS_PHASE
SEPARATION_OF_DUTIES_CHECK: PASS
ROUTE: A1_K1_A2_K4_P5.3_B6b-2.6_H_RDIV_MF1_v1
CURRENT_PHASE: ANALYTIC_RESULT_PHYSICS_AUDIT
ALLOWED_NEXT_ACTION: read-only audit exact R0-R11 result against frozen document254 and receipt task121
ALLOWED_READS: mandatory bootstrap; documents244,245,251-255; event ledger through task121; feasibility gate; role config/manifest
ALLOWED_WRITES: none
FORBIDDEN_ACTIONS: edit; select physical chi_div/chi_c/dynamics/u_cell/measure/reset; C_x/Pi_J/steam/completion; Python; S8/H0/time/k fit; state/score/depth/RUN change
IMMUTABLE_INPUT_PATHS_AND_SHA256:
  document254=9AF71F8289D6D5D1072439BF322F261480C76A3AACC8F3A55FCDE10BE9C02B99
  event_ledger_through_task121=1701E295DD20DA9BA60289866FAEC0D6A2AA52214A11AE6682954F5BCD092C4E
  physics_role_config=0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
  agent_manifest=EA48FEF9348EFEA1F681EF8A3D35F69038FABE57B07D9F8BC70CB3D670F3FE91
PREREG_SHA256: 9AF71F8289D6D5D1072439BF322F261480C76A3AACC8F3A55FCDE10BE9C02B99
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only audit recommendation
DONE_WHEN: R0-R11 rows, proofs, formal witness, exclusions, remaining blocker and nonclaims independently verified
NEXT_ROLE: main_orchestrator
```

## 9. Auditné otázky

1. Sleduje výsledok presne zmrazený R0–R11 scope bez post-hoc zmeny?
2. Je setová first-root measure primárna a delta-flux iba platnou simple-root
   ekvivalenciou?
3. Je dual predictable projection správne použitá bez predstierania fyzicky
   evaluovateľnej intenzity?
4. Dokazuje príklad s `tau/T_*` iba matematickú neprázdnosť a nepoužíva
   kozmický clock ako fyzikálny vstup?
5. Sú exact exclusions a outside-v1 prípady správne oddelené?
6. Ostávajú všetky fyzické vstupy a následné vrstvy otvorené bez P4
   physical witnessu, skóre alebo run zmeny?
