# S-M/Q18/Q22 — P1 STOP súčasného korpusu a brána autorovho vstupu

**Dátum:** 2026-07-22  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → S-M/Q18/Q22`  
**Stav:** `REVIEW_BLOCKED_BY_AUTHOR_PHYSICAL_INPUT / P1_STOP_CURRENT_CORPUS / NO_CODE_AUTHORIZED`  
**Autor teórie:** Martin Jambor  
**Procesná a source-lineage kontrola:** Codex (OpenAI), dva nezávislé
read-only agentové posudky  
**Predchodca:** EA-039 T2 prijatý; C3 `45/45`; K4 `60/100`; P5 `3.5/6`

## 1. Autoritatívny výsledok tejto brány

Aktuálny projekt neobsahuje explicitný lokálny zdroj pary ani úplný
production/collision kernel. Obsahuje iba:

1. efektívny neskorý backgroundový kanál
   `Q^mu = Gamma rho_f u_c^mu`, ktorý vedie `F→C` a paru nevytvára;
2. dôkaz, že hladká kladná skorá FLRW bump história s párovým rezervoárom
   môže matematicky existovať;
3. podmienený historický budget založený na `Delta N_eff=0.0535`;
4. conditional S-C0 rozdelenie spoločného collisionless sektora.

Žiadna z týchto položiek neurčuje elementárnu udalosť, lokálny clock,
energetický rezervoár, invariantnú mieru, collision operator, momenty,
vypnutie zdroja alebo fyzické korelácie porúch. Preto sa nesmie vytvoriť
Python runner, vybrať bump profil ani spätne fitovať čas/amplitúdu.

Tento výsledok je P1 STOP **súčasného korpusu**, nie smrť celej triedy S-M
ani A2-K4.

## 2. Presná existujúca hranica M0/Q22a-G0

Fundamentálny kandidát musí mať aspoň

```text
nabla_mu T_s^(mu nu) = +S_s^nu,
nabla_mu T_e^(mu nu) = -S_s^nu,
S_s^nu = C_s(chi, I_1, ...) u^nu,
```

kde `chi` je lokálny dynamický stav, `e` je explicitný rezervoár s úplným
`T_e^(mu nu)` a `C_s` nemá ako voľný argument kozmický čas, `ln a`,
globálne `H0` ani realizovaný Fourierov mód `k`.

Tento zápis je iba M0/backgroundová FLRW projekcia. Úplný S-M zdroj musí
pripustiť

```text
S_s^nu = C_s u^nu + J_s^nu,    u_nu J_s^nu = 0.
```

Kernel musí odvodiť `J_s^nu`, birth frame a ich perturbácie. V presnom
FLRW limite môže `J_s^nu=0` vyplynúť z izotropie; nesmie sa to však vopred
predpokladať pre poruchy.

Spoločná brána Q22a-G0 navyše vyžaduje:

- definíciu elementárnej udalosti, jej energie a invariantnej miery;
- úplný štvorvektorový ledger všetkých produktov so súčtom nula;
- odvodený branch ratio alebo dôkaz nulového produktu;
- pri sekvenčnom procese odvodený kernel alebo explicitný medzistav;
- z toho istého mechanizmu `delta Q_A`, tlak, shear/noise a spoločný
  zdroj/korelácie `P_AB(k)`.

Súčasné `delta`, `lambda` a backgroundový skalárny transfer tieto položky
neurčujú.

## 3. FIXED / DERIVED / OPEN

| oblasť | stav |
|---|---|
| neskorý `F→C` ledger | `DERIVED_BACKGROUND_ONLY`; conservation áno, steam source nie |
| skorý ukončený parný relikt | `PHYSICALLY_POSSIBLE_NOT_DERIVED`; konštruktívna trieda, nie bunkový zákon |
| lokálny `chi` a jeho evolúcia | `OPEN` |
| rezervoár `e` a `T_e^(mu nu)` | `OPEN` |
| elementárna udalosť, energia, invariantná miera | `OPEN` |
| `C[f]`, `C_s` a všetky momenty | `OPEN` |
| birth frame, priestorové `Q_s^mu`, Eulerove znamienka | `OPEN` |
| produkčný tlak, shear, noise, disperzia a fyzické počiatočné multipóly/closure | `OPEN`; post-decoupling collisionless hierarchy je `FIXED_CONDITIONAL_P5_S1` |
| produkcia, thermalizácia, decoupling, source-off | `OPEN` |
| korelácie AD/CDI/BI/NID/NIV alebo nový mód | `OPEN`; S-C0 je iba conditional referencia |
| total energy/momentum identity jedného steam kernelu | `OPEN` |
| pozitivita, entropia, stabilita a kauzalita konkrétnej vetvy | `OPEN` |

## 4. Scope correction pre `Delta N_eff`

Hodnota `Delta N_eff=0.0535` je v aktuálnom pláne
`SUPERSEDED IN SCOPE / CONDITIONAL ESTIMATE`; náhrada zatiaľ neexistuje.
V S-M sa preto nesmie použiť ako cieľ pre voľbu kernelu, branch ratio,
času ani amplitúdy.

Smie zostať iba explicitne označeným legacy benchmarkom/sensitivity case.
Z neho odvodená hranica `f_R,direct < približne 3.2e-5` platí iba
podmienene v historickej perzistentnej neskorej formulácii. Pri novej
odvodenej normalizácii sa musí prepočítať. Bez podmienky však zostáva
platný kvalitatívny záver, že registrovaný neskorý A1 kanál sa nesmie
potichu premenovať na významný steam source.

## 5. Dve dovolené vstupné vetvy autora teórie

### A. Exit/reheating rezervoár

Táto vetva je najbližšia dnes prežívajúcemu dvojepochovému koridoru:
skorý ukončený parný relikt a neskorý takmer čistý `F→C`.

Autor musí dodať alebo schváliť:

1. čo je lokálny stav/pole rezervoára `e`;
2. jeho stavové premenné, jednotky, doménu, `T_e^(mu nu)` a stavovú rovnicu;
3. lokálny decay/transfer zákon a invariantný clock `chi`;
4. zdroj energie/hybnosti pary a ledger ostatných produktov;
5. či popol a para vznikajú paralelne alebo sekvenčne;
6. ktoré konštanty a počiatočné podmienky sú nové.

### B. Jazvová/event vetva

Autor musí dodať alebo schváliť:

1. lokálny stav `chi=(n_I, xi, ...)`, význam každej premennej a dynamiku;
2. definíciu elementárneho zlyhania/delenia, jeho energiu a invariantnú
   mieru udalostí;
3. `T_I^(mu nu)` alebo iný explicitný energetický rezervoár jazvy;
4. mapu udalosti na popol, paru a prípadný medzistav;
5. odvodený alebo nulový branch ratio;
6. nové konštanty a počiatočné podmienky.

### Spoločné povinné vstupy pre obe vetvy

Autor musí pri A aj B dodať alebo výslovne schváliť aj:

1. fyzikálny mechanizmus skorého `source-off`, ktorý nie je voľným časom,
   a presný source-off/null limit;
2. produktovú kinematiku a matrix element alebo collision operator `C[f]`,
   z ktorého sa dajú odvodiť birth frame, tlak, shear a šum;
3. steam interakcie a kritérium thermalizácie/decouplingu, alebo explicitné
   tvrdenie a dôvod, že para je collisionless od vzniku;
4. počiatočný štatistický stav a noise prescription potrebný na odvodenie
   `P_AB(k)` a módových korelácií;
5. source-off pozostatkový zákon vrátane `rho_s proportional a^-4` a
   všetkých párových energy/momentum identít.

Codex smie z autorovho vstupu formalizovať rovnice, odvodiť dôsledky a
auditovať ich. Nesmie sám vybrať rezervoár, event/kernel, podiel produktov,
čas produkcie ani nový voľný parameter.

## 6. Predregistrovaný proces po úplnom autorovom vstupe

Po výslovnom autorovom výbere a dodaní alebo schválení spoločných povinných
fyzikálnych vstupov vzniknú tri samostatné vedecké artefakty:

1. immutable author-input/preregistration dokument s exact source hashmi
   a rozhodovacími vetvami; po jeho uzavretí sa SHA zapíše do samostatného
   immutable receiptu alebo existujúceho append-only route registra;
2. operator derivation + M0–M2/Q22a-G0 constraint passport;
3. nezávislý formula/process audit.

Textová derivácia smie udeliť nanajvýš `PASS_MAPY`, `PASS_SCOPE`,
`PASS_FORMULA_SCOPE`, prípadne `NONEMPTY_WITNESS`. Nemôže udeliť
`COMPUTED_STOP_SCOPE`, fyzikálny P5.3 PASS, zvýšiť K4, odvodiť
`Delta N_eff` bez mechanizmu ani otvoriť P5.4/G8/G9.

Ucelená formulačná časť následne patrí do malého T1 externého balíka.
Kód možno predregistrovať až po prijatí tohto T1 auditu.

## 7. Aktuálny STOP

Kým autor teórie nevyberie a fyzikálne nedefinuje vetvu A alebo B, platí:

```text
REVIEW_BLOCKED_BY_AUTHOR_PHYSICAL_INPUT
P1_STOP_CURRENT_CORPUS
NO_CODE_AUTHORIZED
```

P5.4, G8, G9, nový C3 suffix, nový fit a zmena prediction table zostávajú
zakázané. Python error ledger sa nemení, pretože nejde o technickú chybu.

## 8. Primárne autority

- `Audit/Q22A_M0_CLOCK_AND_RESERVOIR_PROVENANCE_AUDIT_2026-07-16.md`;
- `Audit/Q22A_P1_1_EXISTING_SOURCE_MAP_AUDIT_2026-07-16.md`;
- `Audit/Q22A_P1_2_EXTENDED_CORPUS_SOURCE_AUDIT_2026-07-16.md`;
- `Audit/Q22A_Q4_Q72_MICROPHYSICAL_OPERATOR_BRIDGE_AUDIT_2026-07-15.md`;
- `Questions/Q22A_PHYSICALLY_SURVIVING_CORRIDOR_2026-07-16_SK.md`;
- `Questions/Q22A_EARLY_STEAM_FUNCTION_EXISTENCE_AUDIT_SK.md`;
- `Questions/Q22A_S2_STEAM_ONLY_DELTA_NEFF_BUDGET_RESULT_SK.md`;
- `theory/SK/05c_Methodology_Rules_and_Question_Register_v3.18_ADDENDUM_SK.md`;
- `theory/SK/05zzzzzzzzzzzzzzzzz_Methodology_Rules_and_Question_Register_Particle_Production_Moments_SK.md`;
- `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/25_P5_3G7_INPUT_RAILS_SK.md`;
- `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/51_P5_3G7_S1_BRANCH_AND_SUPPORT_TRANSFER_CONTRACT_SK.md`.
