# Dodatok k 05 — centrálna karanténa historických skriptov (SK)

Dátum: 2026-07-15  
Stav: záväzný dodatok; staršie pravidlá sa nemenia

## Kontrola duplicity

AR29 upravuje časové limity, AR53 evidenciu formálnych chýb a AR54 očakávania pred behom. Chýbalo pravidlo, ktoré pred každým historickým spustením vyžaduje centrálnu stavovú kontrolu a odlišuje technicky nespustiteľný, fyzikálne neautoritatívny, environmentálne blokovaný, review-only a superseded súbor. AR55 vypĺňa túto prevádzkovú medzeru bez zmeny starších rozsudkov.

## AR55 — Karantenizovaný skript sa rutinne nespúšťa

Pred spustením každého existujúceho `scripts/*.py` sa musí skontrolovať `scripts/00_DO_NOT_RUN_SCRIPT_REGISTRY.md` alebo vykonať checker 188 s `--target` a explicitným timeoutom.

Skript so stavom `DO_NOT_RUN_TECHNICAL`, `DO_NOT_USE_PHYSICS`, `ENVIRONMENT_BLOCKED`, `RUNNABLE_REVIEW_ONLY` alebo `SUPERSEDED` sa nesmie použiť v bežnom dôkaznom reťazci. Priamy beh je prípustný iba ako vopred registrovaná reprodukcia starej chyby alebo historická regresia; musí uviesť očakávaný error/REVIEW a nesmie prepísať nástupcu.

Status sa viaže na celý názov a SHA-256 revíziu, nie iba číslo skriptu. Pôvodné súbory sa nepremenúvajú ani nedostávajú nové komentáre, aby sa zachovali historické hashy a odkazy. Oprava má dostať nový číslovaný súbor alebo auditovaný nemenný wrapper.

`NOT_IN_QUARANTINE` nie je fyzikálny PASS. Znamená iba neprítomnosť známeho blokovacieho dôvodu. Všetky ostatné metodologické a fyzikálne brány zostávajú povinné.

Pri novej chybe sa pred pokračovaním aktualizujú: formálny error ledger, karanténa checkera 188 a datovaný MD register.

## Q80 — Aký je aktuálny výsledok prvého korpusového auditu?

Checker bez spustenia cieľov prečítal 192 Python súborov. Našiel presne zachované syntaxové chyby 118/119, nedokončený 186 bez execution entry a zosúladil 62 karantenizovaných súborov: 18 technických, 7 fyzikálne neautoritatívnych, 2 environmentálne blokované, 21 review-only a 14 superseded. Target smoke-test zablokoval 118 exitom 2 a nekarantenizovaný 176 iba označil `NOT_IN_QUARANTINE` bez fyzikálneho kreditu.
