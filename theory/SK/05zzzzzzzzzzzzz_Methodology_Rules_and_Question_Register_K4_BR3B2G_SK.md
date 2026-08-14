# 05 — Dodatok metodiky a registra: K4/BR3B-2g (SK)

Dátum: 2026-07-14

Tento dodatok nemení existujúce pravidlá.

## AR42 — Vyšší multipól musí mať gradientovo generovanú regularitu

Po zavedení rescalovaných vyšších multipólov môže koeficientová sústava
obsahovať matematicky regulárne homogénne riešenia, ktoré po spätnej
transformácii zodpovedajú nenulovému skorému multipólu bez zdroja z nižšej
hierarchie. Taký mód nie je dovolená počiatočná podmienka štandardnej
Boltzmannovej hierarchy.

Pred rankovým alebo fyzikálnym rozsudkom sa musí explicitne vynulovať každý
vyšší multipól pod jeho prvým gradientovo generovaným rádom. Až potom má
hodnosť, nulový smer a porovnanie so skoršími koeficientmi fyzikálny význam.

Ak nepridaná regularita kontaminuje skoršie koeficienty, výsledok je
`REVIEW_UNCLOSED`, nie smrť koľaje. Pôvodný skript sa zachová s dôvodom a
oprava vznikne v novom číslovanom klone.

## Q69 — Prešla K4 prvým `l=3` a gravitačným ash sektorom?

**Stav: ÁNO; K4 ŽIVÁ, G7 OTVORENÁ.**

Skript 127 po pridaní regularity prešiel `40/40` kontrol pri odrezaní 5 aj 6.
NID/NIV fyzikálne matice majú rank `66/66`; lambda-zero common koeficienty
reprodukujú skript 124 na `~10^-16`. Skript 128 nezávisle prešiel `16/16`
exaktných identít.

Prvý `L3` feedback a ash `delta_c` vznikajú pri NID `p+4` a NIV `p+3`.
Ash/CDM stress gravituje pri NID `p+5` a NIV `p+4`. Je nenulový, ale malý.

BR3B-2g PASS neuzatvára celý G7. Nasleduje BR3C dvojhĺbková evolúcia a audit
všetkých štyroch Einsteinových constraintov. Skóre ostáva `60/100 = G6`.

