# A2-K4 / C7.7c / K7a-J4 — preregistrácia zloženého projektovaného Jacobiánu

**Dátum registrácie:** 2026-07-14, pred prvým behom J4  
**Predpoklad:** J3 prešiel na NID/NIV a deep/shallow

## Účel

Overiť celý projektovaný Jacobián po odstránení numericky nestabilného zápisu `ell = 2*(q+1)`, ale nevyhlásiť starú dvojpresnú konečnú diferenciu \(T'\) za platnú. J4 preto skladá dva nezávislé dôkazy:

1. revíziu projektovaného Jacobiánu s priamym `ell = denominator_x/denominator`;
2. 80-ciferný J3 audit \(T'\) na tom istom povrchu.

## Nemenná postupnosť

1. Spustiť projektovaný algebraický audit bez ODE.
2. Zachovať starú dvojpresnú FD kontrolu \(T'\) iba ako diagnostiku; jej už zdokumentované zlyhanie sa nesmie skryť ani premenovať na PASS.
3. Spustiť autoritatívny 80-ciferný J3 audit.
4. Až potom zložiť verdikt.
5. Povrchy bežia v poradí NID/deep, NID/shallow, NIV/deep, NIV/shallow. Prvý nový neúspech postup zastaví.

## Brány na každom povrchu

- výstupy oboch podbehov sa dajú jednoznačne načítať a patria rovnakému módu/povrchu;
- všetky pôvodné brány projektovaného auditu okrem starej `K7a_Tprime_fd` sú `true`;
- stará `K7a_Tprime_fd` zostane vo výstupe a jej hodnota sa reportuje, ale nerozhoduje za J4;
- J3 má verdikt `PASS_C7_7C_K7A_J3_CANCELLATION_SAFE_TPRIME` a všetky jeho brány sú `true`;
- použitý spôsob je explicitne `ell = denominator_x/denominator`;
- žiadna rovnica, fyzikálny koeficient ani pôvodný tolerančný prah sa nemení;
- každý podbeh aj celý zložený beh má časový limit.

## Rozhodovanie

- **PASS K7a-J4:** všetky štyri povrchy splnia všetky vyššie brány.
- **REVIEW:** akákoľvek iná chyba než už identifikovaná stará FD diagnostika.
- J4 je stále algebraická/Jacobiánová brána. Neudeľuje body hĺbky, neoveruje ODE evolúciu a sama neuzatvára C7.7c.

