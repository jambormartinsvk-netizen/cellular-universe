# Q22a — v akom poradí delenie vytvára palivo, popol a paru?

**Stav:** `OTVORENÝ REGISTER KOLAJÍ; bez prideleného skóre`  
**Rodičovská otázka:** Q22 (`S -> P_S(k) -> zeta`) a K-N1a.  
**Pravidlo:** žiadna postupnosť sa nesmie rozhodnúť slovným výkladom ani
pozorovaním, že sa „hodí“. Každá dostane rovnaký ledger a rovnaké testy.

**Dôležité obmedzenie:** existujúci A1 tok `F -> C` je efektívny
coarse-grained backgroundový ledger. Sám neurčuje, či sa pri jednej
mikroudalosti tvorí aj para, či produkty vzniknú naraz, alebo či jedna zložka
vznikne až z druhej. Nie je preto verdiktom nad mikroskopickým poradím.

Provenienčný audit `Audit/Q22A_EFFECTIVE_LEDGER_VS_MICROSEQUENCE_PROVENANCE_AUDIT_2026-07-15.md`
potvrdil, že A16 a pipeline 09 neobsahujú bunkový `F->R` ani konverzný
collision kernel. K1 preto zostáva iba baseline; K3 je blokovaná na odvodenom
podiele a K4–K7 sa pred takým odvodením neotvárajú.

## Premenné a hranica problému

`F` je palivo/energia dostupná pre delenie, `C` popol (hmotný relikt) a `R`
para/radiačný relikt. `J` označuje lokálnu udalosť delenia. Tu sa skúma iba
kauzálne poradie vzniku produktov; nejde o pridanie nového voľného parametra
ani o zmenu homogénneho exact-A1 backgroundu.

Bez spätných slučiek a s `F` ako zdrojom existuje sedem kanonických možností.
Spätné premeny `C<->R` sú samostatné fyzikálne procesy, nie ďalší slovný
variant tej istej postupnosti, a smú vzniknúť až s vlastným mikrofyzickým
operátorom.

## Koľaje

| Koľaj | Kauzálny graf | Ľudský význam | Stav |
|---|---|---|---|
| Q22a-K1 | `F -> C` | iba popol; para je nulový limit | BASELINE EFFECTIVE PASS; nie mikroverdikt |
| Q22a-K2 | `F -> R` | iba para; popol je nulový limit | MŔTVA v perzistentnej priamej voľno-relativistickej forme: parný rozpočet `Delta N_eff` |
| Q22a-K3 | `F -> C`, `F -> R` | delenie vytvorí oba produkty paralelne | ŽIVÁ IBA V NEVÝZNAMNOM priamom parnom limite `f_R<~3.2e-5`; `b` nie je odvodené |
| Q22a-K4 | `F -> C -> R` | najprv vznikne popol, časť sa neskôr zmení na paru | ČAKÁ NA Q18/Q23: odvodený skorý alebo konečný kernel, nie perzistentný neskorý zdroj |
| Q22a-K5 | `F -> R -> C` | najprv vznikne para, z nej neskôr kondenzuje/nukleuje popol | ČAKÁ NA Q18/Q23: priama perzistentná prvá vetva `F->R` je M-015 |
| Q22a-K6 | `F -> C`, `F -> R`, `C -> R` | paralelná tvorba plus neskorá vetva popol -> para | ČAKÁ NA Q18/Q23 a na odvodený podiel/kernely |
| Q22a-K7 | `F -> C`, `F -> R`, `R -> C` | paralelná tvorba plus neskorá vetva para -> popol | ČAKÁ NA Q18/Q23 a na odvodený podiel/kernely |

K1 a K2 sú povinné nulové limity; nie sú „nudné“ — určia, či dáta vôbec
vyžadujú oba produkty. K2 už prešla štrukturálnym auditom v
`Q22A_K2_DIRECT_STEAM_RESULT_SK.md`: energiu zachová, ale pri nenulovom
prenose mení A1-K1 background a patrí do novej A1 vetvy. K3 je najjednoduchší
spoločný zdroj. K4–K7 majú dodatočný časový kernel a preto vyššie riziko
neodvodenej voľnosti. Pozorovateľne ukotvené sitá S1/S2 tento priestor
sprísnili: `Q22A_S2_STEAM_ONLY_DELTA_NEFF_BUDGET_RESULT_SK.md` usmrtila K2 v
jej dodanej perzistentnej priamej forme a obmedzila priamu parnú časť K3 na
`f_R<~3.2e-5`. To nie je odvodenie vetvenia; je to dôvod, prečo sa nemá ďalej
hľadať veľká paralelná priama para.

Sito tým neurčilo, **kedy** vznikol už zadaný parný relikt. Táto otázka už
patrí do Q18/Q23: `dot(rho_steam)+4H rho_steam=C_steam` cez zrýchlenú fázu,
exit a reheating. M0 provenance audit navyše uzavrel, že súčasná teória ešte
nemá lokálny clock/stav ani rezervoár tohto `C_steam`. K4–K7 sa neotvoria,
kým z tejto histórie nevznikne odvodený časový kernel; v opačnom prípade by
iba obchádzali M-015 novým parametrom.

Fyzikálne prežívajúci koridor je zhrnutý v
`Q22A_PHYSICALLY_SURVIVING_CORRIDOR_2026-07-16_SK.md`: malý skorý ukončený
parný relikt plus neskorý A1-K1 transfer prakticky celý do popola. Je
nevyvrátený týmto sitom, ale zostáva podmienený Q18/Q23, nie je PASS teórie.

Audit `Q22A_EARLY_STEAM_FUNCTION_EXISTENCE_AUDIT_SK.md` navyše dokazuje
existenciu celej triedy hladkých, pozitívnych skorých **efektívnych FLRW**
zdrojových funkcií `S_steam(x)` s párovým ledgerom. Nevyberá ich tvar ani
nepreukazuje lokálnu mikrofyziku; presne tento rozdiel uzatvára
`Audit/Q22A_M0_CLOCK_AND_RESERVOIR_PROVENANCE_AUDIT_2026-07-16.md`.

## Povinný výpočtový postup pre každú koľaj

1. **Mikroledger:** odvodiť `Q_F^mu`, `Q_C^mu`, `Q_R^mu` z jedného rozdelenia
   alebo collision kernelu a dokázať `sum_A Q_A^mu=0`. Podiely ani oneskorenia
   sa nesmú fitovať po dátach.
2. **Background:** odvodiť ODE pre `rho_F,rho_C,rho_R`; otestovať kladnosť,
   nulové limity a zhodu/odchýlku od zmrazeného A1 ledgeru. Pri zdroji do `R`
   vypočítať BBN a `Delta N_eff`, nie ho len pomenovať „para“.
3. **Poruchy:** z rovnakého operátora odvodiť `delta Q_A`, hybnostné frame-y a
   korelačnú maticu `P_AB(k)`. Pri transláčnej invariancii ten istý `k`
   prechádza všetkými zložkami cez transfery, ale amplitúdy a znamienka sú
   výsledok, nie predpoklad.
4. **Pozorovania:** pred dátami zmraziť vstupy; potom testovať CMB, BBN,
   `N_eff`, rast, lensing, izokurvatúry, `f_NL` a prípadnú voľnú dráhu popola.
5. **Rozsudok:** `PREŽÍVA`, `REVIEW_BLOCKED` alebo `MŔTVA` s presným dôvodom.
   Mŕtvy graf a jeho skripty zostanú archivované.

Matematika najprv z každej topológie vyrobí odlišné testovateľné `H(a)`,
`N_eff`, korelácie `P_AB(k)`, izokurvatúry a časové oneskorenia. Pozorovania
potom vyberú alebo vylúčia koľaje. Ani matematika bez mikrofyzického
operátora, ani samotný fit dát bez takého operátora nesmú rozhodnúť poradie.

## Poradie práce podľa perspektívy

Najprv sa musí zreprodukovať **Q22a-K1 ako baseline**, lebo je jedinou
postupnosťou, ktorú už explicitne obsahuje zmrazený A1 ledger:
`Q_F=-Gamma rho_F`, `Q_C=+Gamma rho_F`, `Q_R=0`. To neznamená, že K1 je
pravda o mikrofyzike; iba že je nulový nový-predpokladový referenčný bod.

Audit Q22a-K1 prešiel ako baseline v
`Q22A_K1_BASELINE_EFFECTIVE_LEDGER_RESULT_SK.md`: `Q_F+Q_C+Q_R=0` a `Q_R=0`
sú presné v oboch A1 implementáciách. To stále nie je mikroverdikt.

Potom je najperspektívnejšia Q22a-K3 (paralelná tvorba), ale smie sa fyzikálne
otvoriť až po odvodení podielu energie medzi `C` a `R` z mechanizmu delenia.
Jej minimálny algebraický audit je preregistrovaný v
`Q22A_K3_PARALLEL_BRANCHING_PREREGISTRATION_SK.md`. Voľný podiel by bol nový
fit a K3 by ním automaticky neprešla. Jej výsledok
`Q22A_K3_PARALLEL_BRANCHING_RESULT_SK.md` potvrdil presný ledger aj oba
nulové limity, ale potvrdil aj to, že conservation samo `b` neurčí. K2 je
druhý nulový limit; K4–K7 sa neotvoria, kým K3 nepovie, či vôbec treba
oneskorenú sekundárnu premenu.

## Vzťah ku K_MPC

Tieto koľaje môžu odvodiť spoločný zdroj `S` a maticu `P_AB(k)`, prípadne
korelačný scale `k_*`. Nijaká z nich nesmie vložiť konkrétny Fourierov mód do
univerzálneho `H(a)`. Historické `K_MPC=0.05` tým nie je spätne ospravedlnené.

## Presný vstup potrebný na pokračovanie

Šablóna `Q22A_MINIMAL_DIVISION_OPERATOR_CONTRACT_SK.md` uvádza minimálny
covariantný obsah hypotézy o udalosti delenia. Kým nie je splnený, K3–K7 sa
nebudú nahrádzať voľnými podielmi, časmi ani dlhými numerickými gridmi.

Mostový audit `Audit/Q22A_Q4_Q72_MICROPHYSICAL_OPERATOR_BRIDGE_AUDIT_2026-07-15.md`
preveril existujúce odvodenia `delta`, `lambda`, Q4 a Q72. Ich spoločný
výsledok je Q22a-G0: najprv treba uzavrieť elementárnu udalosť aj úplný
kinetický momentový ledger; dnešný efektívny `Q` na to nestačí.

**Aktuálny stop bod Q22a-G0:** `REVIEW_BLOCKED_BY_Q4-P0_DEFINITIONAL_INPUT`.
Kontrola korpusu potvrdila, že `xi`, energia jazvy, počet pokusov a „pasca #7"
nemajú mimo samotnej otázky Q4 fyzikálnu definíciu. Najbližší zmysluplný krok
nie je nový solver, ale ich presné zadefinovanie podľa šablóny operátora.
