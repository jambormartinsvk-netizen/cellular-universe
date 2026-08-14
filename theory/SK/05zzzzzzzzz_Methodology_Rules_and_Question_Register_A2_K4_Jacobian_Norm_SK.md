# Dodatok k 05 — A2-K4, norma Jacobianu a FD chyba (SK)

**Dátum:** 2026-07-14  
**Stav:** záväzný dodatok; staršie pravidlá sa nemenia

## Kontrola duplicity

AR34–AR37 riešia constraintové derivácie, kompenzované zdroje, condition hranice tolerancií a activity certifikáty. Neurčujú normu Jacobianu ani minimálny audit FD chyby. AR38 vypĺňa túto samostatnú medzeru.

## AR38 — Jacobianový verdict musí uviesť súradnicovú normu a chybu diferenciácie

`max|J|`, singulárne hodnoty, SVD condition číslo a top couplings sa nesmú označiť za fyzikálne invarianty bez uvedenia stavovej škály a normy. Pri diagonálnej transformácii `y=S w` sa musia odlíšiť `J_y` a `J_w=S^-1 J_y S`.

Ak je RHS lineárny, uprednostní sa priamy koeficientový alebo bázový Jacobian. Ak sa použije FD, musí sa vykonať krokový sweep alebo porovnanie s priamym Jacobianom a SVD cutoff sa musí odvodiť zo zmeranej FD chyby. Vlastné čísla sú pri exaktnej podobnostnej transformácii invariantné, ale jednotlivé numerické vlastné čísla nenormálnej matice môžu byť citlivé; samotný spektrálny polomer nie je úplný stability verdict.

## Q66 — Ako neskorší audit obmedzil Jacobianové tvrdenia 151/152?

Veľké `max|J|` a SVD hodnoty opisovali obálkové numerické súradnice, nie fyzikálny Jacobian. Priamy fyzikálny test dal `max|J_y|=43.535`, kým obálkové hodnoty boli až `4.19×10^14`. Condition proxy s cutoffom `10^-14` bol stiahnutý, pretože zmeraná FD chyba pri kroku `10^-7` bola rádovo `10^-10`.

