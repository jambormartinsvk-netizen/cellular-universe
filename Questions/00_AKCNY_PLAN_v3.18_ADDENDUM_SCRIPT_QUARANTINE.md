# Akčný plán v3.18 — karanténa a kontrola známych chýb

Dátum: 2026-07-15

## Pred každým skriptom

1. zapísať očakávania podľa AR54;
2. skontrolovať centrálny register alebo spustiť checker 188 `--target`;
3. pri karanténe použiť nástupcu; starý skript iba pri explicitnej reprodukcii chyby;
4. vykonať limitovaný `py_compile`, CLI, JSON a dependency smoke-test podľa známych patternov;
5. spustiť výpočet s AR29 limitmi;
6. po novej chybe pred pokračovaním doplniť error ledger, checker a MD register.

## Údržba

- raz pred Git/Zenodo snapshotom zopakovať ne-exekučný celý korpusový audit;
- ak sa zmení hash karantenizovaného súboru, status je `REVIEW_STATUS_DRIFT`, kým sa revízia nezaudituje;
- nové wrappery musia exportovať `executed_path_id` a kontrolovať markery;
- zvyšných 130 nekarantenizovaných súborov sa neoznačuje automaticky za aktívne; certifikácia zostáva viazaná na konkrétny audit.

Fyzikálna priorita K4 ani skóre `66.5/100` sa touto prevádzkovou zmenou nemenia.
