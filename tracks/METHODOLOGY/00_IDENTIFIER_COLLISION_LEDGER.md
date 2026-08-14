# Kolízny ledger identifikátorov rodiny 05

**Dátum kontroly:** 2026-07-16  
**Rozsah:** SK headings overené; documentation steward potvrdil rovnakú
množinu tokenov v EN pároch  
**Stav:** release blocker; historické ID sa neprepisujú

## Potvrdené kolízie

| ID | Historický význam A | Historický význam B | Zaobchádzanie |
|---|---|---|---|
| AR8 | audit prenosu formulácie do implementácie | povinná sila sa nemaže | dva odlišné významy; release alias/mapa povinná |
| AR9 | efektívny ledger nerozhoduje skrytú postupnosť | Git commit pred Zenodo | dva odlišné významy; release alias/mapa povinná |
| AR37 | condition hranica aktivity | neskoršie brány nie sú automaticky nezávislé | dva odlišné významy |
| AR38 | Jacobianová norma a FD chyba | neúplný zdrojový vektor | dva odlišné významy |
| AR39 | zachovanie neúspešnej stopy pri oprave odčítania | PASS neauditovanej premennej sa nededí | dva odlišné významy |
| Q20 | séria aktualizácií A2 | rovnaká otázka v čase | viesť ako revízie `Q20@artefakt`; jeden aktuálny redirect |
| Q64 | dopad G8–G10 na dôveru v G7 | obmedzenie starej C7.7c formulácie | dva odlišné významy |
| Q65 | kompatibilita K4 po BR3B | ďalší krok C7.7c | dva odlišné významy |
| Q66 | regularita NID/NIV | obmedzenie Jacobian tvrdení | dva odlišné významy |
| Q67 | obmedzenie staršej K7a | úplnosť NID/NIV common-fuel reťazca | dva odlišné významy |
| Q72 | collision kernel produkcie popola | skorá evolúcia K4 po BR3C-b | dva odlišné významy |

## Zámok

- Historické súbory a ID sa nemenia.
- Jednoduché spojenie dodatkov do release 05 je zakázané.
- AR70 bol pridelený až po kontrole, že rozsah AR1–AR69 bol obsadený a AR70
  sa nevyskytoval; zostáva jedinečný.
- Ďalšie globálne AR/Q ID sa neprideľuje, kým nevznikne úplná release mapa
  `historický súbor + ID -> jednoznačný release alias/ID`.
- Nová pracovná téma sa dovtedy označuje stabilným textovým ID auditného
  threadu, nie improvizovaným AR/Q číslom.

## Release podmienka

Release builder musí používať schválenú kolíznu a supersession mapu. Pri
každom kolíznom ID uvedie zachovaný historický názov, nové jednoznačné ID
alebo alias, dôvod a spätné odkazy na všetky zdrojové súbory.
