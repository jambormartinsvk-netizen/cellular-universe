# A2-K4.3b-RG-BR — audit BR1, BR2 a BR3A

**Dátum:** 2026-07-14  
**Verdikt:** `ČIASTOČNÝ PASS; KOĽAJ ŽIVÁ; K4.3b NEUZAVRETÁ`  
**Kanonická hĺbka:** `60/100 = G6`

## Auditná otázka

Má K4 konzistentný synchronous Einstein–matter ledger a regulárnu skorú
backreaction pre sedem módov, alebo predchádzajúce zlyhania predstavujú
fyzikálnu smrť?

## Fyzikálny výsledok

Kovariantne deklarovaný K4 fluidný systém prešiel symbolickú bilanciu energie
a hybnosti. Sedem módov prešlo skorú back-reacted DAE evolúciu, dve štartové
hĺbky a štyri Einsteinove rovnice plus energy/momentum ledger. Dva velocity
zvyšky nad pevnou toleranciou boli preukázateľne pod explicitnou IEEE-754
condition hranicou.

Neobjavil sa invariantný rast, nesúlad zákona zachovania ani chybný nulový
limit. Nevznikol dôvod smrti.

## Audit numerických zlyhaní

| Beh | Stav | Príčina | Rozsudok |
|---|---|---|---|
| 89 | REVIEW | konečná druhá derivácia `eta` násobená `(Hconf/H0)^2` | numericky nevhodný test, nie fyzika |
| 90 | REVIEW | kompenzované zdroje tvorené zo surových `X_A~a^-4` | catastrophic cancellation, nie fyzika |
| 91 prvý beh | ERROR_UNCLOSED | `numpy.bool_` v JSON | výstupná chyba |
| 92 | REVIEW | dve velocity cancellation rezíduá nad pevnou absolútnou hranicou | vyžiadala condition audit |
| 93 prvý beh | ERROR_UNCLOSED | `numpy.bool_` v JSON | výstupná chyba |
| 94 | PASS | explicitná species-resolved round-off hranica | BR2 uzavretá |

Tieto skripty a erratá sa zachovávajú. Žiadny z uvedených REVIEW/ERROR stavov
nie je mŕtva koľaj.

## Prečo BR3A mení čítanie exponentov

Backgroundové mocniny `3.93109` a `4.93109` zostávajú správne. Nie sú však
úplnými poruchovými exponentmi. Každý zdroj ich násobí vedúcou mocninou
príslušného AD/CDI/BI/NID/NIV seedu. Skript 95 analyticky aj numericky overil
päť módovo závislých tlakových a ash-transfer exponentov.

Tým sa obmedzuje staršia formulácia bez jej prepisovania: staré čísla sú
prefaktory, nie univerzálne konečné rády každej poruchy.

## Čo ešte nebolo dokázané

- BR3A extrahovala fuel a ash zdroje v pevnej regulárnej metrike;
- ešte chýba koeficient indukovanej frakčnej korekcie metriky a ostatných
  species v spoločnom Puiseuxovom systéme;
- skorý photon–baryon sektor použil vedúcu tight-coupling uzáveru;
- neprebehla plná opacity/polarization/recombination hierarchia v
  modifikovateľnom backende;
- neprebehla neskorá CMB/LSS likelihood brána.

Preto G7 ako atómová brána neprešla a skóre sa nemení.

## Ďalší krok

`BR3B`: zostaviť módovo závislý lineárny koeficientový systém pre indukované
frakčné `h_x`, `eta`, photon/baryon a kolektívne free-streaming korekcie.
Overiť jeho hodnosť, konečnosť, štyri Einsteinove koeficientové rezíduá a
dve hĺbky. Až potom otvoriť plný backendový krok.

## Reprodukcia a primárne zdroje

- skripty 88–95, ich erratá a výstupový súbor v `scripts`;
- [Ma & Bertschinger — Cosmological Perturbation Theory](https://arxiv.org/abs/astro-ph/9506072);
- [Bucher, Moodley & Turok — primordial perturbation modes](https://arxiv.org/abs/astro-ph/0007360);
- [CLASS `perturbations.c`](https://raw.githubusercontent.com/lesgourg/class_public/master/source/perturbations.c);
- [CAMB transfer conventions](https://camb.readthedocs.io/en/latest/transfer_variables.html).

