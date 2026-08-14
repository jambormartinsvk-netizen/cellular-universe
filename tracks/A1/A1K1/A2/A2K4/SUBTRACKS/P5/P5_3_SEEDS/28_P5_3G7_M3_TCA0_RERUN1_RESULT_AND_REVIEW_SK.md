# P5.3g7-M3/TCA0 RERUN1 — výsledok a povinné review

**Dátum:** 2026-07-16  
**Runner:** `261_script_KMPC_023_P5_3g7_mode_resolved_full_seed_audit_rerun1.py`  
**Výsledok:** `RUN_KMPC_023_P5_3G7_M3_TCA0_RERUN1.json`  
**Verdikt:** `REVIEW_BLOCKED_M3`  
**Fyzikálna hĺbka A2-K4:** bez zmeny, `60/100`

## Ľudský význam výsledku

Runner úspešne zostavil módovo rozlíšené Puiseuxove rady pre tri Fourierove
módy a potvrdil, že opravený background už nezávisí od voľby `k`. Následne
však štandardný nulový-limit seed neprevzal už prijatú M1 amplitúdu metriky
ako vstupnú podmienku. Lineárna sústava preto mala v každom prípade jednu
voľnú normalizačnú/gauge amplitúdu. Least-squares riešič si z tejto rodiny
vybral minimálnu normu, nie M1 normalizáciu.

Preto sa frakčné K4 constrainty zatiaľ nesmú fyzikálne interpretovať. Boli
vyrátané nad nesprávne zvoleným členom tej istej štandardnej rodiny riešení.
Toto nie je fyzikálny STOP A2-K4, ale chyba väzby M1 vstupu do M3 runnera.
Je to konkrétny prípad už existujúceho pravidla AR50: presná normalizačná
kotva sa musí vynútiť tvrdou rovnosťou alebo elimináciou, nie iba post-checkom.

## Čo prešlo

- päť presných identít má symbolické rezíduum presne nula:
  `Phi z^p=A_f a^p`, `D1_j2` a `D1_j3` k-cancel, druhorádová identita
  `U_c` a nulový limit `lambda→0`;
- relatívny rozdiel backgroundu medzi `k={0.005,0.05,0.15} Mpc^-1` je
  `4.46e-16` pri `a=1e-6` a `1.37e-16` pri `a=1e-4`, teda bezpečne pod
  predregistrovaným limitom `1e-12`;
- podmienené S-C rozdelenie pary má presnú hybnostnú/hustotnú kanceláciu;
- všetky frakčné driver matice majú plnú hodnosť a driver rezíduá sú približne
  `1e-15` až `1e-14`.

Tieto body sú platné iba v deklarovanom algebraickom/M3-TCA0 rozsahu.
Neuzatvárajú finite opacity, P5.4, G8 ani fyzikálny pôvod pary.

## Čo neprešlo a prečo

Každý z 15 štandardných prípadov (`3 k × 5 módov`) mal hodnosť `76/77`.
Driver rovnice boli vyriešené na `~10^-14`, ale M1 `h` koeficient nebol
súčasťou určujúcej matice; až po riešení sa iba porovnal s očakávaním.

Príklady:

| `k [Mpc^-1]` | mód | očakávaný M1 `h` | pozorovaný `h` | relatívny rozdiel | štandardný holdout |
|---:|---|---:|---:|---:|---:|
| 0.005 | AD | 0.5 | 0.0499525509 | 0.900095 | 1.08011 |
| 0.05 | AD | 0.5 | približne 0.4955 | 0.009024 | 0.06801 |
| 0.15 | NID | podľa M1 mapy | — | 0.005623 | 2.63e-5 |
| 0.15 | NIV | podľa M1 mapy | — | 0.4419 | 2.99e-2 |

CDI a BI vybrali prakticky nulový člen namiesto nenulovej M1 amplitúdy, čo
dáva relatívny rozdiel `1.0`. Závislosť od `k` v tejto tabuľke neznamená
znovuobjavenú závislosť backgroundu; ide o rozdielnu veľkosť neukotveného
štandardného seedového módu v súradnici `z=k/H_r`.

Z toho vyplývajú aj zlyhania `00/0i`, zakázaných skorých vrstiev a väčšiny
dvojštartových kontrol. Tie sa teraz nepočítajú ako nezávislé dôvody smrti,
pretože všetky používajú ten istý neukotvený štandardný vstup.

## Stav artefaktov

- RERUN1 runner je `RUNNABLE_REVIEW_ONLY`: reprodukuje nález, ale nesmie sa
  citovať ako PASS alebo STOP K4;
- base modul `mode_resolved_puiseux.py` je revízia `V1_UNANCHORED_M1` a je
  `REVIEW_ONLY` pre plný M3 verdict;
- immutable JSON sa zachováva bez zmeny;
- pôvodný KMPC-022 runner ostáva `DO_NOT_RUN_TECHNICAL` pre PF-055.

## Povolený ďalší krok

Jediná povolená oprava RERUN2 musí vložiť už predregistrovanú M1 amplitúdu
ako tvrdú externú podmienku elimináciou príslušného `h` stĺpca. Nesmie meniť
fyzikálne rovnice, rady, `k`, štartovacie plochy ani reziduálne prahy.
Očakávaná redukovaná hodnosť je `76/76` a M1 anchor musí byť splnený na
strojovú presnosť. Ak potom štandardné `00/0i` holdouty neprejdú, RERUN2
končí REVIEW/STOP architektúry bez tretieho opravného suffixu.
