# P3a-B skript 203 — prerušený scaffold

Dátum: 2026-07-15  
Stav: **DO_NOT_RUN_TECHNICAL**  
Fyzika vykonaná: **nie**

Skript 203 vznikol ako bitová kópia skriptu 197 a dostal iba prvú časť
plánovaného P3a-B patchu. Dva auditované nulové členy boli odstránené z
`M'` a bola začatá provenance/output vrstva, ale verdict, structural
checks a konečný fail-closed export neboli dokončené.

Skript neprešiel `py_compile`, source-delta audit, corpus checker ani
fyzikálny beh. Nesmie sa používať na rozhodnutie a nesmie sa dokončiť
potichu pod rovnakým číslom. Zostáva zachovaný ako historický dôkaz.

Nasledujúci pokus musí dostať nové číslo, začať z čistého skriptu 197,
zopakovať celý kontrolovaný patch a zaradiť 203 do karantény s týmto
dôvodom. P3a-A PASS a hĺbka A2-K4 `66.5/100` tým nie sú dotknuté.
