# Q22a-K3 — preregistrácia minimálneho paralelného ledgeru

**Stav pred behom:** `PRIPRAVENÉ; bez fyzikálneho skóre`  
**Koľaj:** Q22a-K3 (`F -> C` a `F -> R` pri tej istej udalosti)

## Čo sa počíta ľudskou rečou

Ak sa pri delení vytvorí naraz popol aj para, musí sa energia jedného zdroja
rozdeliť. Označme podiel do popola `b`; potom zvyšok `1-b` ide do pary.
Audit sa nepokúša tento podiel vymyslieť ani fitovať. Skúma presne to, čo
hovorí matematika bez nového mikrofyzického operátora.

## Zmrazené rovnice a očakávanie

```text
Q_F = -Gamma rho_F
Q_C = b Gamma rho_F
Q_R = (1-b) Gamma rho_F.
```

Pre `0<=b<=1` musí byť `Q_F+Q_C+Q_R=0`. Hraničné hodnoty majú presne
redukovať K3 na už definované nulové limity: `b=1` je K1 a `b=0` je K2.
Zachovanie energie samo nesmie určiť jednu konkrétnu hodnotu `b`.

## PASS / STOP / ďalší postup

* **PASS algebra:** exact conservation a presné nulové limity.
* **REVIEW_BLOCKED:** ak A1 ani iný registrovaný mikrofyzický operátor
  neurčuje `b`, K3 nie je fyzikálne povolené rozšírenie. `b` sa nesmie
  potichu pridať ako parameter ani doladiť na `N_eff`, `S8` alebo `H0`.
* **STOP:** nepozitivita produktu pri `0<=b<=1` alebo nezhoda s nulovými
  limitmi.
* **Po behu:** až explicitný operátor delenia alebo nezávisle odvodená
  frakcia môže odblokovať background, poruchy a observačné testy K3.

## Bezpečnostné limity behu

Skript je symbolický, bez ODE a bez dát. Interný limit je 5 s, vonkajší
limit 10 s. JSON je len príloha; stav koľaje zostáva v Markdownu.
