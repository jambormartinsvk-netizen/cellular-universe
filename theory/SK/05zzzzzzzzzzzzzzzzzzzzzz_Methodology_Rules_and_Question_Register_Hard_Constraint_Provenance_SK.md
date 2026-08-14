# Dodatok k 05 — tvrdé kotvy a proveniencia registra (SK)

Dátum: 2026-07-15  
Stav: záväzný dodatok; staršie pravidlá sa nemenia

## Kontrola duplicity

AR39 rieši katastrofické odčítanie a zachovanie neúspešnej numerickej stopy. AR45 zakazuje dvojité započítanie constraintu. Ani jedno neurčuje, že presne zadané fyzikálne kotvy nesmú byť iba mäkkými least-squares riadkami, ani že register z hlavného solve sa nesmie prepísať referenčným limitom. AR50 vypĺňa túto medzeru bez zmeny starších pravidiel.

## AR50 — Fyzikálne kotvy sú tvrdé a každý register musí niesť provenienciu solve

Počiatočná podmienka, regularitná nula alebo normalizačná kotva označená ako presná sa pri numerickom riešení koeficientov musí vynútiť tvrdou rovnosťou alebo elimináciou premennej. Menšie globálne least-squares rezíduum neospravedlňuje jej posun.

Ak sa tá istá solve funkcia volá pre fyzikálny background aj referenčný limit, každý exportovaný register musí obsahovať a overiť identitu módu, backgroundových parametrov a účelu volania. Neskorší referenčný solve nesmie potichu prepísať register používaný na fyzikálny verdikt. Krížové porovnanie registrov z rôznych backgroundov je `REVIEW`, nie fyzikálny PASS ani smrť.

## Q76 — Ktoré staršie formulácie K7b obmedzil neskorší audit?

- K7b.3a v skriptoch 168/169 je mŕtva, pretože vysoká presnosť ponechala fyzikálne kotvy ako mäkké LS riadky a posunula ich.
- Skript 170 je iba technicky mŕtvy pre nepodporovaný mpmath rez matice.
- Skript 171 opravil rez, ale jeho HP register sa prepísal neskorším `mu=0` solve; nie je autoritatívnym fyzikálnym HP registrom.
- Skript 172 preto porovnal rôzne backgroundy a jeho REVIEW nesmie zabiť K4.
- Skript 173 skončil na nesprávnej ceste textového markera pred výpočtom.
- Autoritatívna oprava je 174/175 a konečný štvorpovrchový verdikt je skript 176.

