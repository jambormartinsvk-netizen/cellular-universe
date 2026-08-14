# Dodatok k 05 — AR69, vlastníctvo artefaktov a base jadra (SK)

**Dátum:** 2026-07-16  
**Rozsah:** nové pravidlo; staršie pravidlá sa nemenia

## Kontrola duplicity

AR59 určuje route, AR61 históriu a AR62 verziovanie spoločného jadra. Chýba
však záväzná väzba medzi koľajou, runnerom, base modulom, výsledkom a auditom.
AR69 dopĺňa túto väzbu bez zmeny uvedených pravidiel.

## AR69 — Jeden artefakt má jedného vlastníka a úplnú dôkazovú reťaz

Každý skript, base modul, výsledok a audit má jedného route-conditioned
vlastníka. Manifest koľaje zapisuje úplnú reťaz
`gate → preregistrácia → runner → base+SHA → výsledok → audit → verdikt`.
Historický súbor sa nekopíruje do viacerých koľají; spoločný artefakt patrí
najbližšiemu spoločnému uzlu a ostatné koľaje ho iba odkazujú.

Base modul použitý vo výsledku je nemenný podľa verzie alebo SHA-256. Oprava
vytvorí novú verziu/hash, zoznam všetkých dotknutých manifestov, nové
výsledky a rozdielový audit. Technický PASS runnera ani algebraický PASS
modulu sa nesmie zapísať ako fyzikálny PASS celej koľaje.

Fyzické presúvanie historických súborov je zakázané, kým neexistuje Git
baseline, úplný `OLD_PATH → NEW_PATH` a SHA manifest a kontrola všetkých
závislostí. Navigačné adresáre dovtedy obsahujú odkazy, nie kópie.

Kanonický layout je `tracks/00_ROUTE_AND_ARTIFACT_LAYOUT_SK.md`.

