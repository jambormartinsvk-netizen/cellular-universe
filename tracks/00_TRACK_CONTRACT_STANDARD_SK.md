# Štandard kontraktu koľaje

Tento dokument je povinná šablóna pre každú aktívnu, blocked alebo novú
fyzikálnu koľaj. Mŕtva koľaj môže mať stručnejší stavový dokument, ale musí
odkazovať na dôvod smrti, skripty a immutable výsledky. Jeden výpočet nesmie
zmeniť koľaj mimo jej kontraktu.

## Povinné polia

1. Úplná route cesta a ľudský cieľ.
2. Rodičovská formulácia, presný stavový priestor a zakázané redukcie.
3. Konečný zoznam brán v poradí, s PASS, STOP a REVIEW.
4. Aktuálny stav každej brány, dôkazový artefakt a najbližší krok.
5. Hĺbka, vedecká podpora a pracovný progress, ak sú definované.
6. Rozsah, ktorý výsledok nepokryl.
7. Aktuálne živé, mŕtve a historické deti s dôvodom.
8. Pravidlo aktualizácie a release oporný bod.
9. Formula-provenance ledger: rodičovská rovnica, nižší tvar, mapa členov,
   nezávislé rezíduum, limity a rozmery.
10. Pred konkrétnou neznámou funkciou alebo kernelom stav `FS-GATE-01`:
    behaviorálny obal, okrajové hodnoty, stav prieniku a odkaz na svedka
    alebo certifikát prázdnosti.

## Pravidlo použitia

Pred každým novým Python výpočtom sa prečíta kontrakt aktuálnej koľaje.
Predregistrácia konkrétneho behu uvedie jeho bránu a nesmie rozšíriť fyziku
bez zmeny kontraktu, novej koľaje alebo explicitného review. Historický PASS
mimo aktuálneho kontraktu je iba historický dôkaz presne uvedeného rozsahu.
Textový alebo AST PASS sa v kontrakte vždy označí ako `PASS_MAPY`/
`PASS_SCOPE`; formula PASS sa smie zapísať až po AR66.2.
