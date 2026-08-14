# A2-K4 / C7.7c-K5 — predregistrácia vyváženej podobnostnej transformácie

**Dátum:** 2026-07-14  
**Východiskový stav:** A2-K4 živá, `66.5/100`; C7.7c-K4 numerická podkoľaj mŕtva.  
**Cieľ:** odstrániť preukázanú nenormalitu numerických súradníc bez zmeny fyziky.

## 1. Jediná povolená zmena

Pre každú zo štyroch trajektórií samostatne:

1. zostaviť pôvodnú analytickú obálku `S_env` zo skriptu 147;
2. na počiatočnom povrchu vypočítať 13×13 Jacobian normalizovaného systému centrálnym rozdielom s pevným krokom `10^-7`;
3. vypočítať diagonálne vyváženie bez permutácie `J_bal=D^-1 J_env D`;
4. použiť počas celej trajektórie pevnú škálu `S_bal=S_env D` a premennú `z=S_bal^-1 y`.

Matica `D` sa počas trajektórie nesmie adaptívne meniť. Zmena je podobnostná transformácia; rovnice v pôvodných fyzikálnych premenných `y` ostávajú totožné.

## 2. Nemenné prvky

- rovnice, koeficienty, znamienka a background;
- počiatočné stavy a referenčný rad pri `x=-18`;
- DOP853, `rtol=10^-10`, normalizované `atol=10^-12`, `max_step=0.02`;
- segment dĺžky najviac jeden e-fold;
- uzávera `L5=0` a 13 registrovaných komponentov;
- fyzikálny safety cap `10^12`;
- vnútorný/vonkajší limit prvých behov `8/10 s`.

## 3. Poradie brán

### K5a — hlboké prvé segmenty

1. NID/deep `-25→-24`;
2. NIV/deep `-25→-24`.

PASS každej trajektórie vyžaduje:

- zachovanie spektra po vyvážení s relatívnou odchýlkou `<10^-8`;
- zníženie `max|J_ij|` aspoň o faktor `10^6`;
- dokončenie jedného segmentu v limite;
- konečný stav a RHS konečné a pod safety cap;
- zápis `nfev`, prijatých krokov a veľkostí krokov.

### K5b — plytké prvé segmenty

Po PASS oboch hlbokých behov sa rovnaká brána zopakuje pre NID/shallow a NIV/shallow.

### K5c — úplná evolúcia a aktivita

Po PASS všetkých štyroch prvých segmentov sa spustí úplná segmentovaná evolúcia po `x=-18`, potom nezávislý komponentový audit C7.7c. Úplný audit musí používať vopred stanovené prahy aktivity a nesmie ich meniť podľa výsledku.

## 4. Rozsudky a skóre

- Diagnostika vyváženia ani K5a/K5b nepridáva body; K4 ostáva `66.5/100`.
- `+0.2` patrí iba úplnému PASS C7.7c-K5c.
- Timeout alebo numerické zlyhanie K5a/K5b zabíja iba numerickú podkoľaj K5, nie automaticky A2-K4.
- Fyzikálna A2-K4 môže zomrieť až na fyzikálnom teste, porušení constraintov, nesprávnom nulovom limite alebo nezhode s úplnou hierarchiou — nie na samotnej cene konkrétnej súradnicovej reprezentácie.

## 5. Stop pravidlo

Pri prvom neúspechu sa beh zastaví a zapíše sa presný dôvod. Bez nového auditu príčiny sa nesmie potichu zaviesť ďalšie škálovanie, nový solver ani uvoľniť tolerancia.
