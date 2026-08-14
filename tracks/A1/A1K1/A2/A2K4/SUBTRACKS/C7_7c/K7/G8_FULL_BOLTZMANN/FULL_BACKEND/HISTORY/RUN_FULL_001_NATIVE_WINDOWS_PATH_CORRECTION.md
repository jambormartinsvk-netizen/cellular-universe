# FULL RUN-001 — korekcia interpretácie: native Windows path

**Predchádzajúci záver o ACL:** obmedzený neskorším auditom.  
**Fyzika vykonaná:** nie.

Rovnaké zlyhanie nastalo aj pod elevated identitou. To vyvracia hypotézu,
že koreňom je vlastníctvo checkoutu. Skutočná príčina je syntax `root` v
CLASS vstupnom súbore: `class.exe` je natívna Windows binárka a nemožno jej
odovzdať MSYS cestu `/d/Teoria/...` na interné otvorenie súboru.

V3 zmení iba riadok `root` na Windows kompatibilné
`D:/Teoria/external/CLASS/build/full_reference/class_`. Pôvodné chybové
beh-y a skoršie interpretácie zostávajú zachované, ale nesmú sa citovať ako
dôkaz ACL problému. Nasleduje jeden bounded reference retry.
