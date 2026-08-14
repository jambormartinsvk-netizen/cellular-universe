# A2-K9.1 — predregistrácia auditu jedného produkčno-rozptylového operátora

## Otázka

Stačí požiadavka „jeden operátor určuje produkciu aj elastický prenos hybnosti“ na prejdenie G2, alebo musí byť ešte zadaný konkrétny collision kernel/maticový element a distribučné funkcie?

## Zmrazený test

1. Porovnať rodinu produkčných kernelov s rovnakým nultým momentom a rovnakou backgroundovou energiou, ale rozdielnym lineárnym prvým momentom.
2. Pridať number-conserving elastický moment `R^mu`, ktorý je nulový na backgrounde, ale ľubovoľný v lineárnej hybnosti.
3. Overiť škálovanie: rozdiel energie pri malom pôrodnom drift-e musí byť `O(v^2)`, kým rozdiel hybnosti je `O(v)`.
4. Rozhodnúť, či background A1 alebo samotné slovo „jeden“ určujú koeficient rozptylu.

## Rozsudok

- G2 PASS iba pri explicitnom spoločnom kerneli, ktorý bez dodatočného fitu určí nultý aj prvý moment a celkovú spätnú reakciu.
- Ak možno meniť lineárny momentum transfer bez zmeny A1 backgroundu, rodič K9 ostáva na G1, nie je však mŕtvy.
- Dva nezávislé po výsledku zvolené koeficienty `S_n` a `gamma_drag` porušujú definíciu K9.

## Limity

Interný limit každého skriptu 5 s, externý limit 10 s, bez kozmologického fitu.

