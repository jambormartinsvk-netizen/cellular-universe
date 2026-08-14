# Q22a-K2 — preregistrácia priameho limitu `F -> R`

**Stav pred behom:** `PRIPRAVENÉ; bez fyzikálneho skóre`  
**Koľaj:** Q22a-K2 (iba priamy radiačný/parný produkt, nulový popol)

## Čo sa počíta ľudskou rečou

Skúma sa druhý nulový limit: všetka prenesená energia by šla z paliva priamo
do pary/radiácie. Nehodnotí sa ešte BBN ani CMB. Testuje sa, či možno takýto
limit vložiť bez zmeny do už zmrazeného A1-K1 backgroundu.

## Zmrazené rovnice a očakávanie

```text
K2: Q_F=-Gamma rho_F, Q_C=0, Q_R=+Gamma rho_F.
A1-K1: Q_F=-Gamma rho_F, Q_C=+Gamma rho_F, Q_R=0.
```

Oba ledgery zachovávajú energiu. Pri `Gamma rho_F != 0` sa však ich príjemca
zdroja líši, preto musí K2 zmeniť evolúciu hmoty aj radiácie a patrí do novej
backgroundovej vetvy A1, nie pod už overený A1-K1.

## PASS / STOP / ďalší postup

* **PASS štruktúry:** conservation a presné preukázanie rozdielu voči A1-K1.
* **STOP v rámci A1-K1:** K2 sa nesmie maskovať ako rovnaký background alebo
  používať K1 predikcie.
* **Nejde o fyzikálnu smrť K2:** na samostatnej A1 vetve by potrebovala
  odvodený operátor a potom BBN/`N_eff`/CMB brány.

## Limity

Bez ODE a bez dát; interný limit 5 s, vonkajší limit 10 s.
