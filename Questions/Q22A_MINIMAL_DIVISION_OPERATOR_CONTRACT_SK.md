# Q22a — minimálny kontrakt operátora delenia

**Účel:** zmeniť otázku „vzniká popol a para naraz alebo postupne?“ na
jednoznačný matematický vstup, ktorý sa dá auditovať.  
**Stav:** `NÁVRH VSTUPU; nie je fyzikálnym tvrdením ani novým parametrom`.

## Čo musí nový predpoklad povedať

Nemusí hneď obsahovať úplnú teóriu všetkých buniek. Musí však pre jednu
lokálnu udalosť delenia `J` povedať aspoň toto:

1. **Miera udalostí:** čo je skalár `J(x)` a z ktorých už existujúcich
   veličín sa skladá. Musí mať jasné jednotky a kladný limit. Ak sa používa
   `lambda`, treba ukázať presné mapovanie na dnešné `Gamma rho_F`.
2. **Energia a hybnosť produktov:** trojica kovariantných zdrojov
   `Q_F^mu,Q_C^mu,Q_R^mu` s identitou
   `Q_F^mu+Q_C^mu+Q_R^mu=0`. Nestačí napísať iba hustoty; pri odlišných
   rýchlostiach produktov rozhodujú aj priestorové zložky.
3. **Rozdelenie energie:** ak vznikajú oba produkty pri tej istej udalosti,
   musí byť podiel `b` odvodená funkcia existujúcej geometrie/stavu, napr.
   `b=b(delta,C,... )`, a nie číslo zvolené po dátach.
4. **Časové poradie:** ak je produkt neskorší, treba normalizovaný kernel
   `K(s)` v lokálnom vlastnom čase (`s>=0`) alebo ekvivalentnú dynamickú
   medzizložku. Jeho stredný čas nesmie byť voľne doladený.
5. **Poruchy:** z rovnakého operátora musí plynúť `delta Q_A` a spoločný
   zdroj fluktuácií `S`, z ktorého sa odvodí `P_AB(k)`. Konkrétny realizovaný
   Fourierov mód nikdy nevstupuje do homogénneho `H(a)`.

## Ako z kontraktu vzniknú koľaje

| Výstup operátora | Otvorená koľaj | Prvá fyzikálna brána |
|---|---|---|
| `Q_R=0` identicky | K1 | zhoda s A1 ledgerom, potom A2 perturbácie |
| `Q_C=0` identicky | K2 | nová A1 vetva: BBN/`N_eff`/CMB |
| `0<b<1`, bez oneskorenia | K3 | nová A1 vetva a `delta Q_A` |
| sekundárny `C->R` kernel | K4/K6 | odvodená doba, entropia, BBN/CMB |
| sekundárny `R->C` kernel | K5/K7 | odvodená doba, voľná dráha, rast |

## Pracovný postup po dodaní hypotézy

1. Najprv sa vykoná čisto algebraický covariantný ledger a nulové limity.
2. Potom background bez fitovania nových podielov/časov.
3. Až po pozitivitných a BBN bránach sa odvodia poruchy a Einsteinove
   constrainty.
4. Nakoniec sa predregistruje a vykoná porovnanie s CMB, `N_eff`,
   izokurvatúrami, rastom a lensingom.

Ak zatiaľ taký operátor nie je, je to korektne `OTVORENÁ` fundamentálna
otázka Q22a, nie technická chyba, ktorú vyrieši viac numerických behov.
