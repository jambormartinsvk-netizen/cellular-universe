# L0b — inventár potomkov A2-K4 pre lineage audit

**Dátum:** 2026-07-15  
**Metóda:** read-only vyhľadanie `K_MPC`, `k_mpc`, `physical_rhs`,
`projected_state_names`, `U_c` a `general_synchronous`; bez Pythonu a ODE.

## Záver inventára

Nejde o jeden chybný runner. K4 obsahuje viac historických implementačných
rodín. Každá dostane vlastný scope verdict; textový nález sám nie je
fyzikálnym rozsudkom.

| Balík | Rozsah | Predbežný dôvod auditu | L2 postup |
|---|---|---|---|
| B1 — K7 projected lineage | 159–161, 166, 177–186, 197, 199–210, 213–216 | používa `D,M` a/alebo 13-state `physical_rhs`; vysoké riziko dedenia chýbajúceho `U_c` | jeden state/contract audit, potom presné rozdelenie na zdroj, checker a výsledok |
| B2 — general-synchronous/BR lineage | 66, 77–86, 89–115, 130–155 | časť explicitne používa `U_c`; treba odlíšiť test-field, seed a plnú metric evolúciu | overiť C1–C6 po skupinách, nie preniesť K7 STOP automaticky |
| B3 — G8 screen lineage | 221, 233, `baseScripts/a2_k4_g8/*`, RUN-002 až RUN-004 | oddelené `U_b`, ale aktuálny `M` nemá `U_c`; screen môže byť matematicky platný v úzkom limite | označiť presný screen-only rozsah a zákaz FULL reuse |
| B4 — A1/K_MPC repair lineage | 11/13, 234–236 a `baseScripts/k_mpc_005/*` | zdroj exact-A1 backgroundu a P5 kontraktu | už čiastočne P2a/P3/P5.1; L2 len overí rozhrania |
| B5 — P5 successor | 236, budúce P5.2–P5.4 | musí od začiatku niesť celý C1–C6 kontrakt | každý nový skript prejde L1 pred fyzikálnym behom |

## Zoznam s najvyššou prioritou

1. **B1 autority:** `159`, `177–179`, `181–186`, `197`, `199`, `203–210`,
   `213–216`. Najprv treba určiť, ktoré z nich samy definujú RHS a ktoré
   len auditujú alebo čítajú immutable výsledok.
2. **B2 fyzikálny most:** `66`, `85`, `86`, `89–91`, `95`, `130`, `136`,
   `140`, `143`, `148`, `155`. Tu môže existovať platná general-synchronous
   fyzika, ktorú K7 neskôr nesprávne zredukovala.
3. **B3:** `221`, `233` a shared modul. Ich výsledky sa nesmú mazať; treba
   ich priamo označiť ako štandardné hierarchy/TCA screeny bez plného K4
   momentum sektora.

## Rozhodovací strom

```text
definuje skript fyzikálnu RHS alebo stav? ── áno → L2 equation audit
                                           └─ nie → číta len rodiča?
                                                     ├─ áno → scope/provenance audit
                                                     └─ nie → mimo tejto línie
```

Tak sa zabráni dvom opačným chybám: neprepočítať skript, ktorý fyziku vôbec
neurčuje; alebo naopak ponechať fyzikálnu RHS bez kontroly len preto, že
prešla numerickou bránou.

## Ďalší krok

**L2-B1:** fail-closed audit state names, backgroundu a závislostí pre
celý K7 projected lineage. Výstup bude mať pre každý skript jeden z troch
stavov: `DEFINES_LIMITED_RHS`, `CHECKER_OF_LIMITED_RHS`,
`HISTORICAL_RESULT_OF_LIMITED_RHS`. Až potom sa rozhodne, čo treba znova
počítať.
