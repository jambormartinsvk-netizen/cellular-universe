# Akčný plán v3.18 — dodatok po K4/C7.7c-K4

## Rozhodnutie

Po troch ohraničených technických neuzavretiach C7.7c sa aktivuje plánovaný prechod z hĺbky na šírku. K4 ostáva živá na 66,5/100; neinvestuje sa do nej ďalší dlhý beh, kým nepoznáme skorý stav nezačatých koľají.

## Poradie

| Priorita | Úloha | Výstup | Stop podmienka |
|---:|---|---|---|
| 1 | A2-K8, rekonštrukcia a lacný audit G0–G2 | audit, otázky, skripty a stav | porušenie zákona/rozsahu alebo dokončenie G2 |
| 2 | A2-K9, rekonštrukcia a lacný audit G0–G2 | audit, otázky, skripty a stav | porušenie zákona/rozsahu alebo dokončenie G2 |
| 3 | porovnanie živých K4/K7/K8/K9/K11/K12 | jednotná tabuľka jemnej hĺbky a ceny ďalšej brány | rozhodnutie o najvýhodnejšom pokračovaní |
| 4 | návrat ku K4 iba ak ostane prioritná | profilovanie NIV a nový vopred registrovaný solver | pevný časový limit na každý pokus |

## K4 backlog

- profilovať podiel času NID/NIV a jednotlivých segmentov bez predlžovania fyzikálneho behu,
- odvodiť analytický alebo blokový Jacobian,
- preveriť vhodnosť BDF/LSODA alebo transformácie nezávislej premennej,
- až potom vytvoriť C7.7c-K5; neopakovať K2–K4.

## Bodovanie

Skóre sa zvyšuje iba za vopred uzavretú fyzikálnu alebo numerickú podbránu. Samotná optimalizácia, syntaktický PASS ani analytická plocha použitá iba ako mierka body nepridávajú.

