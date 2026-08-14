# Dodatok k 05 — A2-K4/C7.7c, podmienený dôkaz aktivity (SK)

**Dátum:** 2026-07-14  
**Stav:** záväzný dodatok; staršie pravidlá sa nemenia

## Kontrola duplicity

AR34 rieši podmienenie constraintovej derivácie, AR35 prirodzenú škálu kompenzovaných zdrojov a AR36 vopred odvodenú condition hranicu tolerancie. Neurčujú však, čo tvorí platný dôkaz dynamickej aktivity komponentu, ktorého zdroj leží pod aritmetickou hranicou použitej presnosti. AR37 vypĺňa iba túto medzeru.

## AR37 — Aktivita pod condition hranicou vyžaduje samostatný certifikát

Komponent sa nesmie vyhlásiť za aktívny ani neaktívny iba podľa double-precision evolúcie, ak vopred vypočítaný pomer jeho zdroja k roundoff hranici nie je väčší než `1`. Sprísňovanie `atol`, predlžovanie runtime ani nenulový JSON kľúč nie sú dôkazom. Vyžaduje sa aspoň jeden z týchto certifikátov:

1. konvergentný výpočet vo vyššej presnosti s počiatočnými koeficientmi v rovnakej presnosti;
2. algebraicky projektovaná kompenzovaná báza s overeným nulovým limitom a constraintmi;
3. analytický/Puiseuxov koeficientový dôkaz s nenulovým vedúcim členom a uzavretou rekurenciou.

Prahy fyzikálnej aktivity sa tým neznižujú. Numerická nerozlíšiteľnosť zostáva `REVIEW_UNCLOSED`, nie fyzikálna smrť.

## Q64 — Ako neskorší condition audit obmedzil starú formuláciu C7.7c?

Staršia formulácia požadovala, aby všetkých 13 komponentov prešlo activity podmienkou v každej zo štyroch double-precision trajektórií. Audit skriptmi 155/156 ukázal, že NID celková hustota a `h_x` majú na deep aj shallow povrchu signal/roundoff pomer pod `0.2`. Jediný double beh preto nemôže byť univerzálnym certifikátom všetkých 13 komponentov.

Požiadavka „každý komponent musí mať dôkaz aktivity“ zostáva. Obmedzená je iba stará implementačná požiadavka „ten istý double-precision evolučný test musí byť dôkazom pre každý komponent“. Rozlíšiteľné komponenty zostávajú numerické; condition-limited komponenty musia prejsť AR37.

## Q65 — Aký je ďalší krok A2-K4/C7.7c?

`C7.7c-K7a`: odvodiť projektované kompenzované zdroje `D=sum Omega_A delta_A` a momentum `M` priamo z registrovaných rovníc a vyššie-presných Puiseuxových koeficientov. Pred PASS K7a/K7b sa nesmie spustiť ďalšia evolúcia ani zvýšiť skóre nad `66.5/100`.

## Q99 — Čo ešte musí A2-K4 splniť po K7d?

K7d neskorším auditom uzavrela G0–G7 a zvýšila strict support/WBS na
`90/100`; tým obmedzila starú odpoveď Q65, ktorá bola správna iba pred
K7a/K7b. Otvorené ostávajú presne dve povinné brány:

1. `C7-G8` — plná fotónová, polarizačná a neutrínová Boltzmannova
   hierarchia so samostatnou baryónovou rýchlosťou, Thomsonovým rozptylom,
   rekombináciou na presnom K4 backgrounde, multipólovou konvergenciou a
   Einsteinovými constraintmi;
2. `C7-G9` — CMB/S8 likelihood na fyzike zmrazenej po G8.

Lacný coefficient alebo skorý hierarchy screen G8 nepridáva body. Až plný
G8 PASS zvýši support na `95/100` a otvorí G9. Timeout alebo backendová chyba
je REVIEW; fyzikálny STOP vyžaduje platnú numeriku a nezávislé potvrdenie.
Autoritatívne kritériá sú v route dokumente
`G8_FULL_BOLTZMANN/00_PREREGISTRATION.md`.

