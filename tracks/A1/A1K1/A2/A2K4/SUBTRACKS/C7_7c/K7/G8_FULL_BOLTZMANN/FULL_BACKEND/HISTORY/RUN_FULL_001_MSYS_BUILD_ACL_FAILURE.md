# FULL RUN-001 V2 — technické zlyhanie ACL build adresára

**Stav:** `TECHNICAL / DO_NOT_INTERPRET`  
**Fyzika vykonaná:** nie.

V2 parameter file presmeroval root do CLASS build adresára, ale MSYS proces
bežiaci pod sandbox identitou nemá zápis ani tam. Checkout bol pôvodne
vytvorený pri schválenom elevated klone, preto je jeho build adresár vlastnený
inou identitou.

Ďalší a posledný smoke pokus spustí nezmenenú binárku rovnakou elevated
identitou, s rovnakým `CLASS_REFERENCE_SMOKE_V2.ini`, rovnakými limitmi a
bez K4 zmeny. To je ACL oprava, nie zmena numeriky ani fyziky.
