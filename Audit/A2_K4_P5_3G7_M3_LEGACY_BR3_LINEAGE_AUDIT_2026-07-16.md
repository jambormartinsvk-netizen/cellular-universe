# A2-K4/P5.3g7-M3 — lineage audit starého BR3 Puiseux reťazca

**Dátum:** 2026-07-16  
**Verdikt:** `REGRESSION_ORACLE_ONLY / NO_TRANSFERRED_PASS`  
**Dopad na A2-K4:** koľaj ostáva živá na `60/100`; M3 ostáva pred behom.

## Otázka auditu

Možno staré BR3 výsledky 95–124 priamo použiť ako P5.3g7-M3 seed po oprave
`K_MPC=0.05`, alebo treba prísnejšie odvodenie?

## Výsledok po artefaktoch

| Artefakt | Čo naozaj preukázal | Prečo nestačí pre M3 | Dnešné použitie |
|---|---|---|---|
| 95 | módové leading fuel/ash zdroje na presnom A1 backgrounde | metrika bola pevný test field; žiadny backreaction holdout | oracle pre mocniny a leading `delta_f,U_f` |
| 98–100 | exact Bianchi kompatibilita background dressingu pre päť módov | spoločný sektor, nie úplný módový reťaz; `eta_x,U_gamma` ostali symbolické | algebraický oracle kompatibility |
| 104–116 | NID/NIV skoré relative-radiation, shear a matter vrstvy | čiastkové matice a neskôr opravený neutrínový shear oracle | poradie vrstiev a regresné pomery |
| 119 | žiadny fyzikálny výsledok | zachovaný `SyntaxError`, vonkajší zoznam ostal neuzavretý | `DO_NOT_RUN_TECHNICAL`; nástupca 124 |
| 124 | NID/NIV zmiešaný reťazec s malým rezíduom po auditovaných technických opravách | `00`,`0i`, trace a traceless boli v jednej riešiacej matici; žiadny nezávislý holdout; iba NID/NIV | `REGRESSION_ONLY`, nie constraint PASS |
| 89 | dynamická trace/`0i` evolúcia | počiatočné `h_x` bolo zrekonštruované z `00`; traceless používal zle podmienenú druhú deriváciu | historický REVIEW |
| 90 | conditioned DAE | `00` rekonštruovalo metriku priebežne | enforced constraint podľa AR45 |

## Dve fyzikálne obmedzenia starého BR3

### 1. Módová normalizácia

Vykonaná cesta 124 deklaruje prvý rád na jednotku

```text
rho_f/rho_r = Phi z^p,   z=k a/(H0 sqrt(Omega_r0)).
```

Bez explicitného `Phi(k)=A_f(H0 sqrt(Omega_r0)/k)^p` tento koeficient nie je
globálny background. Staré čísla možno porovnávať iba po tejto amplitúdovej
transformácii.

### 2. Neúplný exact-A1 frakčný background

Vykonaná cesta 124 vložila do frakčnej časti denominatora iba leading položku
`D1_0=1`. Exact-A1 transfer však už na ďalších rádoch vyžaduje

```text
D1_2 = G2[-1/2+1/(p+1)],
D1_3 = (-G2 MU/2)[-1/3+1/(p+2)],
```

čo je palivová korekcia plus backgroundový popol. Tieto členy ležia v
rozsahu starého NID/NIV reťazca. Preto jeho neskoršie frakčné koeficienty
nie sú autoritatívnym exact-A1 oraclom, aj keď jeho vlastná skrátená sústava
mala plnú hodnosť a malé rezíduum.

## Obmedzenie staršieho PASS

Formulácia „BR3B-2f-5 PASS“ zostáva pravdivá pre presne zadanú skrátenú
maticu 124. Neskorší audit ju obmedzuje takto:

> Nejde o P5 M3 PASS ani o dôkaz propagácie `00/0i`. Je to dôkaz, že stará
> prvotriedna NID/NIV Puiseuxova truncation mala spoločné riešenie po použití
> všetkých deviatich rovníc naraz.

Historické skripty, JSON a dôvody sa nemažú. Nový runner ich smie použiť iba
ako porovnávací export, nikdy ako zdroj koeficientu alebo očakávaného PASS.

## Povinný nástupca

P5 M3 musí:

1. zahrnúť AD/CDI/BI/NID/NIV;
2. použiť `Phi(k)` transformáciu a exact-A1 `D1` aspoň cez potrebný rád;
3. určiť metriku z trace/traceless a species rovníc;
4. ponechať `00`,`0i` mimo riešiacej matice;
5. niesť dynamický stav `U_c` a jeho prvý nenulový rád;
6. rozlíšiť podmienenú S-C paru od fyzikálne odvodenej S-M vetvy;
7. overiť viac než jeden perturbatívny mód `k` pri rovnakom backgrounde.

Predregistrácia nástupcu je
`tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/27_P5_3G7_M3_MODE_RESOLVED_PUISEUX_PREREGISTRATION_SK.md`.
