# A2-K11 — stav po revízii 45 s SHA `973905D...`

**Dátum:** 2026-07-13  
**Stav:** `PREŽÍVA IBA HYPOTÉZU — 10/100 = G1 (historický checkpoint 15)`  
**Aktívny krok:** K11.1

## Zmena oproti predchádzajúcemu stavu

Nová revízia skriptu 45 napravila numerickú toleranciu a prešla krokovým,
`k` a amplitúdovým testom. Staršie výhrady „výsledok pod atol“ a
„neprejdený krok“ sa preto nesmú prenášať na hash `973905...`.

Fyzikálny stav sa nemení, pretože bodový audit 54 našiel relatívne
Einsteinovo rezíduum `1.0` v aktívnom bode a jeho lineárne škálovanie až na
`825.515`. Rovnice a znamienko silového štvorvektora zostávajú
nekonzistentné s deklarovaným kovariantným modelom.

## Ďalší krok sa nemení

K11.1 musí pred ďalším superhorizontovým behom:

1. odvodiť pravidelný momentum-transfer operátor;
2. odvodiť úplné kontinuity, Eulerove rovnice a Einsteinove constrainty;
3. dokázať ich vzájomnú propagáciu cez Bianchiho identity;
4. zostaviť všetky nezávislé superhorizontové módy, nie iba jeden
   kompenzovaný relatívny vektor;
5. až potom opakovať numeriku.

Scratch hodnota `1.71e-16` zostáva bez dôkazovej váhy, kým nebude uložený
presný skript, SHA-256 a výstup.

## Aktualizácia 2026-07-14 — externý skript 47

Skript `47_script_A2_K11_S8_K1b_fully_consistent_einstein_test.py` bol
reprodukovaný, ale jeho `PASS_RIGOROUS_S8_K1b_AUDIT` bol zamietnutý.

Rozhodujúce dôvody:

- koeficient `-(4-3 delta)` mieša barotropický uzáver s tlakom `c_s^2=1`;
- sadzby `lambda/(aE)` a `gamma/(aE)` sú pri constant proper-time modeli
  nesprávne; musia byť delené `E`;
- pri štarte je interakcia umelo zosilnená faktorom `1090.9`;
- fuel kontinuita a energy recoil zostávajú nekonzistentné;
- `final_relative_residual` je pri `A=1e6` a `1e8` prakticky `1.0`;
- lineárne škálovanie je zabudovaná vlastnosť homogénnej lineárnej ODE.

Nejde o novú koľaj, pretože nebol pridaný nový operátor ani stupeň voľnosti.
Kanonický stav a ďalší krok sa nemenia:

```text
A2-K11 = PREŽÍVA IBA HYPOTÉZU — 10/100 = G1 (historický checkpoint 15)
M-015  = NEVYDANÁ
```

Autoritatívny audit je
`Audit/A2_K11_AUDIT_SCRIPTU_47_GEMINI_NAVRHU.md`.


