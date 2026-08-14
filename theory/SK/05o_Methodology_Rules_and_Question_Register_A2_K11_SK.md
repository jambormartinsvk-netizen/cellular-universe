# REGISTER 05 — SK dodatok k A2-K11

**Dátum:** 2026-07-13  
**Status:** záväzný dodatok; existujúce pravidlá sa nemenia

## Kontrola duplicity

P3 už všeobecne vyžadovalo adaptívny solver, fyzikálne hranice a kontrolu
konvergencie. Neurčovalo však zákaz akceptovať výsledok pod absolútnou
toleranciou, zákaz logického bypassu konvergencie ani amplitúdový test
lineárnej sústavy. AR13 je preto presnejšie nové obmedzenie, nie duplikát.

Staršie pravidlá používali percentá pokroku, ale nedefinovali spoločný
význam skóre pre živé a mŕtve koľaje. AR14 zavádza iba auditnú hĺbku a
nemení žiadny starší fyzikálny rozsudok.

## AR13 — Numerický PASS musí byť rozlíšený, konvergentný a constraintový

Numerická brána nesmie prejsť, ak testovaná konečná amplitúda leží pod
absolútnou toleranciou solvera. Podmienky konvergencie sa nesmú nahradiť
výrazom typu `converged OR result_is_small`. V lineárnej homogénnej sústave
sa musí bezrozmerný transfer zachovať pri spoločnom škálovaní počiatočnej
amplitúdy. Constraint sa hodnotí relatívne na aktívnych bodoch; malé
absolútne rezíduum pri relatívnej hodnote rádu jedna nie je dôkaz zachovania.

Každá interakcia musí mať vlastný skutočný nulový limit. Beh s jednou
nenulovou väzbou sa nesmie nazvať `uncoupled`. Machine-label `PASS` sa pri
nesplnení ktorejkoľvek predregistrovanej brány audítorsky prehlasuje za
neplatný dôkaz a pôvodný výstup sa zachová.

## AR14 — Skóre N/100 je hĺbka auditu, nie pravdepodobnosť pravdy

Skóre koľaje udáva najvzdialenejšiu zdokumentovanú auditnú bránu. Mŕtva
koľaj si ponechá maximálne dosiahnuté skóre spolu s kódom a dôvodom smrti;
číslo ju nesmie oživiť. Živá koľaj musí pri skóre uviesť, ktoré brány ešte
neprešla. Jednotná stupnica je v
`Audit/A2_KATALOG_STAV_SKORE_A_DOVOD_SMRTI_K1_AZ_K11.md`.

## Q42 — Dokazuje opravený skript 45 superhorizontové prežitie alebo S8?

**Stav:** `NIE.`

Auditovaná revízia skriptu 45 opravila iba faktor sadzby na `1/E`. Jej
predložený mínusový projektor je pri deklarovanej konvencii anti-drag,
rovnice sú neúplné, relatívne `00` rezíduum je `1.0` a výsledok leží pod
`atol`. Skript 53 navyše zamietol amplitúdové škálovanie aj krokovú
konvergenciu. Skript nepočíta `S8`.

Fyzikálna trieda ortogonálneho momentum-transferu preto pokračuje iba ako
`A2-K11 PREŽÍVA FORMULAČNÚ BRÁNU — 15/100`. Ďalšia povinná brána K11.1 je
lokálny operátor s tlmiacim znamienkom, pravidelným `rho_f->0` limitom a
úplnými constraint-preserving perturbáciami.

## Obmedzenie starších formulácií

- všetky staršie `PASS` formulácie skriptu 45 odteraz znamenajú iba, že
  daná revízia programu dobehla; fyzikálna brána neprešla;
- veta v skripte 51 o nezmenenom skripte 45 platila iba pre snapshot pri
  vzniku 51; aktuálna auditovaná revízia sa identifikuje SHA-256;
- starý aktuálny vstupný súbor Q20 končiaci pri K5 je obmedzený novším
  `Questions/00_READ_FIRST_A2_Q20_AFTER_K11_0.md`.

