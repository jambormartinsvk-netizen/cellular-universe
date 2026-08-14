# Akčný plán v3.18 — po K7c P2 M-prime ledgeri

Dátum: 2026-07-15

## Uzavreté

- `SCI-A2K4-C7G5-K7C-P2-MLEDGER` dokončené;
- jednoduchá `math.fsum` príčina zomrela s faktorom zlepšenia `1×` na
  všetkých troch checkpointoch;
- K7c.3e fsum evolúcia je `DISQUALIFIED_BEFORE_CREATION`;
- A2-K4 ostáva živá `66.5/100`, K7c REVIEW, score effect NONE.

## Ďalšie poradie

1. `SCI-A2K4-C7G5-K7C-P3A-ZERO-IDENTITY`: bez ODE auditovať dve exaktné
   backgroundové identity a float64 cancellation rezíduá.
2. Iba po PASS vytvoriť samostatnú P3a-B evolúciu s jedinou zmenou dvoch
   identicky nulových koeficientov.
3. Zopakovať 100/200/400 s pôvodnými prahmi `8–32` a `<1e-6`.
4. Ak algebraická koľaj zomrie, pokračovať lokálnou tuhosťou/eigenmódmi.
5. Vyššiu pracovnú presnosť ponechať ako ďalšiu samostatnú koľaj.
6. Žiadny CMB/S8 beh pred konvergovanou evolúciou.

## Dokumentácia

- aktualizovať route K7c history a artefaktový manifest;
- checker 200 je aktuálny snapshot po skripte 199;
- PF-023/PF-024 ostávajú v error ledgeri;
- pred každým ďalším Pythonom znovu vykonať AR58 preflight a zapísať ľudské
  očakávania.

