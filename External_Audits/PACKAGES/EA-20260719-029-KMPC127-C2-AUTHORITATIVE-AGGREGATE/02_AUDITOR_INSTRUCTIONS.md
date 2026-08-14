# Pokyny pre externého auditora — EA-029

1. Čítajte v poradí z dokumentu 00.
2. Overte oba manifesty pred spustením Pythonu.
3. Každú behavior vetvu spustite v samostatnej čerstvej kópii `REPRO`.
4. V negatívnej vetve odstráňte iba KMPC-126 input; nesmie vzniknúť output.
5. V success vetve nemeňte rawy, hashe, kandidátov, prah ani kód.
6. Generated raw porovnajte s Evidence 004 po odstránení iba
   `runtime_seconds`; žiadna iná normalizácia nie je povolená.
7. Skontrolujte, že kód neimportuje solver a že agregát nič nefitoval.
8. Vyplňte prázdnu response šablónu mimo immutable package adresára.

Ak sa reprodukcia odchýli, uveďte prvú odlišnú bránu a presný súbor/hash.
Nemeňte projektové verdikty ani obsah balíka.
