# A2-K4 / K7c P1 — konečný audit čistého samostatného RK4

Dátum: 2026-07-15  
Koľaj: A2-K4  
Auditná hĺbka: `66.5/100` bez zmeny  
Verdikt reprodukcie: **PASS**  
Fyzikálny verdikt evolúcie: **REVIEW, nie smrť**

## Výsledok ľudskou rečou

Tá istá krátka evolúcia porúch bola vypočítaná troma čoraz jemnejšími pevnými RK4 mriežkami: 100, 200 a 400 krokov. Čistý skript 197 už neobsahuje starý adaptívny solver ani nedosiahnuteľný blok. Napriek tomu presne zopakoval anomáliu skriptov 184/185: jemnejšia mriežka nepriniesla menší rozdiel.

To uzatvára implementačnú otázku. Problém nebol spôsobený tým, že v starom generovanom súbore zostal nedosiahnuteľný `solve_ivp`. Neuzatvára to však fyziku: výsledok ešte nemá očakávanú konvergenciu RK4 a nesmie sa použiť na CMB, S8 ani na potvrdenie koľaje.

## Predregistrované očakávania a výsledok

| Kontrola | Zmrazené očakávanie | Výsledok | Verdikt |
|---|---:|---:|---|
| rozdiel 100/200 | `1.4432726876921487e-6 ± 1e-12` | `1.44327268769215e-6` | PASS |
| rozdiel 200/400 | `[3.931235e-6, 3.931245e-6]` | `3.93123964056996e-6` | PASS reprodukcie |
| pomer `(100/200)/(200/400)` | historicky `[0.36,0.375]` | `0.367129155088317` | PASS reprodukcie |
| dominantná zložka | `M` | `M` | PASS |
| klasický RK4 konvergenčný pomer | fyzikálne `8–32`, stred približne 16 | `0.367129155088317` | FAIL fyzikálnej brány |
| rozdiel 200/400 | fyzikálne `<1e-6` | `3.93123964056996e-6` | FAIL fyzikálnej brány |
| density cancellation monitor | `<5e-12` | `1.36721924142781e-22` | PASS monitora |
| momentum cancellation monitor | `<5e-12` | `4.32321445172391e-17` | PASS monitora |
| normalizovaný safety maximum | `<1e8` | `1` | PASS |
| interný čas | `<20 s` | `6.906 s` | PASS |

Density a momentum čísla sú algebraické cancellation monitory rekonštruovaných veličín. Nie sú nezávislým dôkazom dynamického zachovania Einsteinových constraintov a nesmú sa tak citovať.

## Čo P1 dokázal

1. Vykonaná cesta bola iba `P1_CLEAN_STANDALONE_FIXED_CLASSICAL_RK4_ONLY`.
2. Zdroj 197 neobsahuje súvislý token starého adaptívneho solvera a má jeden entry point.
3. Rovnice, background, seed, škála, `L5=0` closure a kroky boli mechanicky prevzaté zo skriptu 179 s hashom `8f45dc698817992e4fb2b859a7cafa49d225b4f7f5fd54b07f88ca99059bd441`.
4. Každá mriežka zapísala samostatný checkpoint pred nasledujúcou mriežkou.
5. Historický neasymptotický, módom `M` dominovaný výsledok je reprodukovateľný bez legacy solvera.

## Čo P1 nedokázal

- že rovnice koľaje K4 majú stabilnú konvergovanú evolúciu;
- že príčinou je iba spôsob sčítania členov `M'`;
- že je správna plná fotónová/neutrínová Boltzmannova hierarchia;
- že prešli štyri počiatočné plochy alebo celý časový interval;
- že možno vypočítať CMB likelihood, S8 alebo meniť tabuľku predpovedí;
- že K4 získava ďalšie body.

## Stav koľaje

A2-K4 ostáva **ŽIVÁ na `66.5/100`**. P1 je regresný audit a nepridal fyzikálnu hĺbku. K7c ostáva REVIEW. Smrť koľaje z tohto výsledku nevyplýva, pretože ešte nebol oddelený problém sčítania, algebraickej kondície, tuhosti a pracovnej presnosti.

## Formálne chyby počas prípravy

PF-013 až PF-016 sú zachované v `scripts/00_PYTHON_FORMAL_ERROR_LEDGER.md`. Žiadna nevykonala fyziku ani nezmenila výsledok P1. PF-016 je opakovanie už známej PF-011 (`foreach` priamo do pipeline) a preto vedie k novému pravidlu aktívneho error-ledger preflightu; samotné uloženie poučenia bez jeho načítania pred príkazom nestačí.

## Dôkazy a SHA-256

| Súbor | SHA-256 |
|---|---|
| `scripts/197_script_A2_K4_C7_7c_K7c_P1_clean_standalone_RK4.py` | `088b4cd58f57a30bd061d30042ba3e2cb5021df9bf320003ed8291d86fb6c022` |
| `scripts/198_script_python_corpus_status_audit_after_K7c_P1_clean_RK4.py` | `b68d6e78d171fa976e8ff18b1210ac2947b005df6e1de0b6b648137aeac79273` |
| `Audit/A2_K4_K7C_P1_20260715_grid100.json` | `c5d78c95236da0ed10262c324808861820c972bacb45733c8d597232df5a8028` |
| `Audit/A2_K4_K7C_P1_20260715_grid200.json` | `26e2aaa23c3606362ce907a42a68a3aa23882b4993e8a5c15b133c26a9f321d6` |
| `Audit/A2_K4_K7C_P1_20260715_grid400.json` | `7acc8fc191a711c3ada13a4ac495302679a93d2aeb3610823e82a8e8ade7245e` |
| `Audit/A2_K4_K7C_P1_CLEAN_RK4_RAW_2026-07-15.json` | `a5a94550bb7542090d6244237326404a5a5cd2298d4d70a53c061b2a6b791ba5` |
| `Audit/A2_K4_K7C_P1_CORPUS_CHECKER_198_2026-07-15.json` | `f925a8b89aa59b82178ef36a26262419fc2ff99a242e5555526b7c8760941ec7` |

Checker 198 auditoval 202 ostatných `.py` súborov, eviduje 69 karanténnych položiek, cieľ 197 označil `NOT_IN_QUARANTINE` a potvrdil `no_target_script_executed=true`. `NOT_IN_QUARANTINE` znamená iba povolenie na predregistrovaný beh, nie fyzikálny PASS.

## Nasledujúci krok

P2 vytvorí nový číslovaný, iba diagnostický term ledger rovnice `M'`; neúplný skript 186 sa nemení ani nespúšťa. Najprv sa na rovnakých uložených stavoch porovná obyčajný súčet, `math.fsum` a 80-dps referencia. Až samostatný následný beh smie meniť spôsob výpočtu RHS. Ak `fsum` nevysvetlí rozdiel a neprinesie predregistrované zlepšenie, táto podkoľaj sa označí za mŕtvu s číslami a pokračuje sa algebraickou kondíciou/tuhosťou.

P1 nemení tabuľku predpovedí a sám nespúšťa Zenodo release trigger.
