# Q20/A2 — čítaj ako prvé po K4.3b-RG skripte 86

**Dátum:** 2026-07-14  
**Aktuálny stav:** `A2-K4 ŽIVÁ 60/100; K4.3b-RG ČIASTOČNE PREŠLA, ALE NIE JE UZAVRETÁ`

Tento súbor nahrádza ako stavový pointer
`00_READ_FIRST_A2_Q20_AFTER_K4_3B_73_74.md`. Starší súbor sa nemaže.

## Čo už prešlo

- päť kolektívnych AD/CDI/BI/NID/NIV seedov v regulárnej synchronous gauge;
- analytické CLASS koeficienty proti CAMB s maximálnym L2 rezíduom `1.52e-5`;
- dva exaktné interné `nu-steam` módy;
- species-resolved hodnosť sedem;
- presný K4 mocninový register vrátane frakčných exponentov;
- general-synchronous test-field evolúcia K4 pre päť kolektívnych módov;
- dve štartové hĺbky a `lambda=0` kontrola.

## Čo neprešlo alebo bolo obmedzené

- CAMB nuly pred interným štartom sú placeholdery, nie fyzikálne seedy;
- lokálny symbolický `pi_r` export nemá Fortran kompilátor;
- odvodené Newtonovské CDI/BI potenciály sú hlboko mimo horizontu
  cancellation-noisy;
- skript 85 nemal dosť vysoký synchronous rád pre NID/NIV Newtonovskú
  transformáciu; jeho veľké hodnoty nie sú fyzikálnou smrťou.

## Prečo skóre zostáva 60/100

G7 je atómová kanonická brána. Test-field PASS ešte neobsahuje fuel
stress-energy spätnú reakciu ani spoločné `00`, `0i`, slip a `ij` rezíduá.
Preto sa medziskóre nad 60 nezavádza.

## Bezprostredný krok

**K4.3b-RG-BR:** back-reacted general-synchronous Puiseux solver so siedmimi
módmi a frakčnými rádmi `a^3.93109` a `a^4.93109`. Až jeho úplný PASS môže
uzavrieť K4.3b a otvoriť K4.3c.

## Autoritatívna stopa

1. `Audit/A2_K4_3B_RG_REGULAR_SEEDS_PUISEUX_AND_SYNCHRONOUS_TEST_FIELD_AUDIT.md`;
2. `Questions/A2_K4_3B_RG_STAV_A_DALSI_KROK_PO_86.md`;
3. `scripts/OUTPUT_A2_K4_3B_RG_77_86.md`;
4. skripty 77–86 a ich erratá;
5. SK/EN dodatok `05zzzzzz`.

