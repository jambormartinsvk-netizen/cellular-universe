# A2-K4 / C7.7c / K7b.3b — preregistrácia hard-constrained solvera

**Dátum:** 2026-07-15, pred prvým behom  
**Nadväzuje na:** fyzikálnu smrť K7b.3a

## Rozdiel oproti 3a

Počiatočné podmienky a registrované hierarchické regularitné nuly sa už nebudú minimalizovať ako mäkké least-squares riadky. Príslušné premenné sa vyjmú zo zoznamu voľných neznámych a dosadia sa ako tvrdé rovnosti. Least-squares sa rieši iba pre zostávajúce koeficienty.

Nonzero NID/NIV kotvy sa vyhodnotia pri 80 dps z registrovaných parametrov `N_eff`, nie z ich zaokrúhleného float64 pomeru. Všetky ostatné fixované hodnoty musia byť explicitne prítomné v pôvodnom zozname `initial`; nevzniká veľkostný cutoff.

## Nemenný rozsah

- rovnaké dynamické riadky, mocniny, background a normalizácia;
- 80 dps, rovnaká matica pred elimináciou fixovaných stĺpcov;
- pôvodné double a mŕtve 3a výsledky zostávajú zachované;
- bez ODE a bez bodov;
- každý beh má vnútorný a vonkajší limit.

## Brány

1. žiadne dve tvrdé podmienky nesmú fixovať tú istú premennú na rôzne hodnoty;
2. všetky fixované koeficienty sa po riešení zhodujú s cieľom s absolútnou chybou `<1e-60`;
3. redukovaná matica má plný rank a všetky hodnoty sú konečné;
4. high-precision lineárne rezíduum nie je väčšie než pôvodné double rezíduum;
5. všetky pôvodné zdrojové a K7b.1 brány prejdú;
6. `D'` activity-relative chyba je `<0.1` na NID/deep aj NID/shallow;
7. `U_fs` rekonštrukcia a momentový constraint ostanú v pôvodnom limite `<5e-12`.

## Rozhodovanie

- Prvý neúspech zastaví 3b a musí byť zapísaný pred ďalšou koľajou.
- Ak 3b zlyhá iba preto, že frakčný/palivový reťazec zostal double, vznikne samostatná 3d pre jednotný high-precision reťazec; nesmie sa potichu rozšíriť rozsah 3b.
- PASS deep aj shallow môže odstrániť NID koeficientový floor, ale stále nie je evolučným PASS.

