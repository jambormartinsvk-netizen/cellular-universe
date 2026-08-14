# Q22a-K3 — výsledok minimálneho paralelného ledgeru

**Verdikt:** `REVIEW_BLOCKED_UNDERIVED_BRANCH_RATIO_B`  
**Algebraický stav:** `PASS_ALGEBRA_REVIEW_BLOCKED`  
**Skóre:** `bez fyzikálneho skóre`  
**Skript a príloha:** `scripts/256_script_Q22A_K3_parallel_branching_audit.py`,
`scripts/results/q22a/RUN_Q22A_002_K3_PARALLEL_BRANCHING_AUDIT.json`.

## Overený výsledok

Najjednoduchší paralelný ledger má nutne tvar

```text
Q_F = -Gamma rho_F
Q_C = b Gamma rho_F
Q_R = (1-b) Gamma rho_F.
```

Pre ľubovoľné `b` sa zdroje presne sčítajú na nulu. `b=1` sa presne redukuje
na K1 (iba popol) a `b=0` na K2 (iba para). To je užitočná kontrola, že
všetky tri grafy používajú rovnaký conservation ledger.

## Prečo to zatiaľ nie je fyzikálna predikcia

Derivácia zachovania dáva `d(Q_F+Q_C+Q_R)/db=0`: sama teda nemá ako vybrať
jednu hodnotu `b`. Súčasné A1 rovnice obsahujú iba efektívny limit `b=1` a
neobsahujú operátor delenia, ktorý by z geometrie buniek odviedol pomer
produktov. Nulový súčet preto nemôže byť zamenený za dôkaz paralelného vzniku.

Nastaviť `b` podľa `N_eff`, `H0` alebo `S8` by bol nový empirický fit. To je
zakázané metodikou; K3 je preto živá, ale zablokovaná na **odvodení** `b`, nie
na ďalšom numerickom prehľadávaní.

## Čo matematika a pozorovania ešte musia urobiť

1. Zadať jeden lokálny covariantný operátor udalosti delenia `J` alebo
   collision kernel. Musí určiť `Q_F^mu,Q_C^mu,Q_R^mu` a tým aj `b`, prípadne
   ukázať, že `b` je funkcia už existujúcich parametrov (`lambda`, `delta`,
   geometria siete).
2. Až potom z rovnakého operátora odvodiť `delta Q_A`, relatívne hybnosti a
   korelačnú maticu `P_AB(k)`.
3. S odvodeným `b` porovnať K1/K3 s BBN (`Delta N_eff`), CMB, izokurvatúrami
   a rastom štruktúr. Dáta budú koľaje súdiť; nesmú spätne vyrábať `b`.

Bez kroku 1 nie je poctivý výpočet K3 backgroundu ani porúch možný. K4–K7 by
navyše pridali časový kernel/oneskorenie, takže sa neotvárajú pred týmto
základným uzavretím.
