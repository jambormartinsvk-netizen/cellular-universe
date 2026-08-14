# REGISTER 05 — SK dodatok k novej revízii A2-K11

**Dátum:** 2026-07-13  
**Status:** záväzné obmedzenie Q42; existujúce pravidlá sa nemenia

## Kontrola duplicity

Nepridáva sa nové pravidlo. AR13 sa iba aplikuje na novú revíziu skriptu 45
a Q43 zaznamenáva, ktoré staršie výhrady boli opravené a ktoré zostali.

## Q43 — Zmenili `atol=1e-16`, `rtol=1e-12` a nový krokový test rozsudok K11?

**Stav:** `NUMERICKY ČIASTOČNE ÁNO; FYZIKÁLNE NIE.`

Hash `973905...` má konečný transfer `1.99286e-13` nad `atol`, krokovú
metriku `7.59611e-7`, `k` metriku `1.72964e-7` a amplitúdovú metriku
`1.40315e-7`. Tieto numerické námietky sú uzavreté v prospech novej
revízie.

Bodový test však našiel maximum pri `a=9.17247e-4`, nie pri nulovom
konečnom stave. Constraintové členy mali rovnaké znamienko a bodové
relatívne rezíduum `1.0`. Po amplitúdovom škálovaní sa absolútne rezíduum
zväčšilo z `8.25515e-10` na `825.515`, takže nejde o šum/šum.

Jeden utlmený počiatočný vektor nedokazuje stabilitu všetkých módov a skript
nepočíta `S8`. Kanonický stav zostáva
`A2-K11 PREŽÍVA IBA FORMULAČNÚ BRÁNU — 15/100`.

## Obmedzenie Q42

Q42 zostáva odpoveďou `NIE`, ale jej dôvody „pod atol“ a „neprejdený krok“
platia iba pre starší hash `61558...`. Pre aktuálny hash `973905...` sú
rozhodujúce neuzavreté rovnice, nesprávna znamienková mapa, bodové
constraintové zlyhanie a chýbajúci test všetkých módov.

## Q55 — Zachraňuje nový skript 47 koľaj A2-K11?

**Stav:** `NIE; PASS SKRIPTU 47 JE NEPLATNÝ DÔKAZ.`

Nepridáva sa nové pravidlo: uplatňujú sa AR13, AR14 a AR28. Skript 47 nie je
novou koľajou, pretože nemení operátor ani stupne voľnosti K11.

Audit reprodukoval jeho čísla, ale zistil:

- hybrid koeficientu barotropického `c_s^2=w` a tlaku `c_s^2=1`;
- proper-time sadzby `1/(aE)` namiesto `1/E`, s raným faktorom `1090.9`;
- neúplné kontinuity a nesprávny energy recoil;
- obrátené constraintové znamienka;
- bodové relatívne `00` rezíduum prakticky `1.0`;
- amplitúdové škálovanie, ktoré je automatickou vlastnosťou lineárnej ODE.

K11 zostáva na `15/100`; M-015 sa nevydáva. Staršie tvrdenie, že skript 47
je „fully consistent Einstein test“, je obmedzené auditom
`Audit/A2_K11_AUDIT_SCRIPTU_47_GEMINI_NAVRHU.md`.

