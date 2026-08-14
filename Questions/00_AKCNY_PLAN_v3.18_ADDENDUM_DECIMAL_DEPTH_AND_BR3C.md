# Akčný plán v3.18 — jemná hĺbka a pokračovanie BR3C

**Dátum:** 2026-07-14  
**Aktuálny stav K4:** `ŽIVÁ; 66.0/100; G6 PASS; G7 OTVORENÁ`

## Poradie a viditeľný bodový postup

| Poradie | Úloha | Acceptance | Prírastok po PASS | Možná hĺbka | Stav |
|---:|---|---|---:|---:|---|
| 1 | BR3C-a: dva fyzikálne rovnaké počiatočné stavy v dvoch skorých hĺbkach | všetky species, metric a `F3`; rovnaká normalizácia | `+0.2` | `66.2` | **NEXT** |
| 2 | BR3C-b: obe skoré evolúcie v časovom limite | konečné premenné; žiadny tichý placeholder | `+0.3` | `66.5` | PENDING |
| 3 | uzavrieť species/mode ledger evolučného stavu | všetky registrované módy skutočne evolvované | `+0.2` | `66.7` | PENDING |
| 4 | porovnať obe štartové hĺbky na spoločnom neskoršom bode | zhoda v predregistrovanej tolerancii | `+0.3` | `67.0` | PENDING |
| 5 | BR3C-c: `00`, `0i`, trace a traceless rezíduá | absolútna aj škálovaná brána pre každé | `4 x +0.1` | `67.4` | PENDING |
| 6 | BR3C-d: polovičný krok | transfer aj rezíduá konvergujú | `+0.2` | `67.6` | PENDING |
| 7 | BR3C-d: prísnejšia tolerancia | transfer aj rezíduá konvergujú | `+0.2` | `67.8` | PENDING |
| 8 | BR3C-e: zmena počiatočnej hĺbky a `lmax` | spoločné neskoré riešenie ostáva v tolerancii | `+0.2` | `68.0` | PENDING |
| 9 | BR4: plný photon/polarization/neutrino/steam/recombination backend | päť podcheckpointov C7.9 po `0.2` | `+1.0` | `69.0` | PENDING |
| 10 | coupled transfery a integrovaný G7 rozsudok | päť podcheckpointov C7.10 po `0.2` | `+1.0` | `70.0` | PENDING |

Body sa pripisujú iba v poradí. Neskorší úspešný test nepreskočí skoršiu
otvorenú alebo neúspešnú podmienku. `70.0` vznikne iba úplným PASS G7.

## Povinné numerické pravidlá

- každý skript má vnútorný limit najviac `50 s` a vonkajší limit najviac
  `60 s`;
- timeout alebo chýbajúci backend je `UNCLOSED`, nie automatická fyzikálna
  smrť;
- relatívne rezíduum musí mať absolútnu a aktívnu škálovanú bránu;
- nulový limit, amplitúdové škálovanie a kroková/tolerančná konvergencia sa
  nesmú nahradiť podmienkou „výsledok je malý“;
- každý nový skript, výstup, REVIEW/FAIL a dôvod zostáva archivovaný.

## Dokumentácia a vydanie

Po fyzikálnom rozhodovacom balíku zostáva v pláne:

1. rozdeliť dokumentáciu do logických adresárov bez mazania historických a
   mŕtvych koľají;
2. aktualizovať SK/EN registre, stavové pointery a changelog;
3. pred Zenodo publikáciou commitnúť reprodukčný stav do repozitára
   `github.com/jambormartinsvk-netizen/cellular-universe`;
4. vydať novú v3.x, pokiaľ sa nezmení fundament; pri fundamentálnej zmene
   použiť v4;
5. ku každej publikovanej Zenodo verzii priložiť changelog a kontrolné súčty.

