# FULL RUN-001 — štandardný CLASS/HyRec smoke: očakávanie

Toto je nulový referenčný beh nezmeneného CLASS, nie K4 výpočet. Používa
štandardnú plochú ΛCDM konfiguráciu s HyRec, `l_max_scalars=100`, výstupom
`tCl` a exportom background/thermodynamics. Účelom je dokázať, že nový
zdrojový backend, štandardná rekombinácia a lineárne perturbácie fungujú pred
akoukoľvek K4 modifikáciou.

Očakávanie: návratový kód 0, vytvorené background a thermodynamics tabuľky,
konečné kladné `z`/ionizácia/opacity v exporte. Shell má interný limit 45 s,
vonkajší 55 s. Fail je technický `REFERENCE_BUILD_REVIEW`, nie rozsudok o
K4. Výstupy idú pod `FULL_BACKEND/ARTIFACTS/CLASS_REFERENCE_SMOKE` a
neprepisujú žiadny zdroj CLASS.

## Dodatok po ACL zlyhaní

Prvý parameter file nemohol z MSYS zapisovať do auditného `D:` adresára a
skončil pred fyzikou. V2 nemení štandardné parametre; iba root presúva do
CLASS `build/full_reference/`. Výstupy tým ostávajú mimo source adresárov a
jeho Git súborov. Pre tento retry platí rovnaký limit 45/55 s.

## Dodatok po V2 ACL zlyhaní

Aj build adresár je vlastnený elevated checkout identitou. Posledný identický
smoke pokus preto použije elevated shell, ktorý zdroj vytvoril. Mení sa iba
prístupová identita procesu; konfigurácia V2, zdroj, compiler a fyzika sú
nemenné.

## Dodatok po native-path audite

Elevated identita nezmenila zlyhanie, preto ACL nebolo koreňom. `class.exe`
potrebuje Windows cestu vo vlastnosti `root`; V3 mení výlučne `/d/...` na
`D:/...`. Predchádzajúce V1/V2 sú technické stopy, nie fyzikálne výsledky.
