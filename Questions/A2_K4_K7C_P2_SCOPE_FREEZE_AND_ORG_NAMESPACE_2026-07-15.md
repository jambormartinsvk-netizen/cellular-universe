# Zmrazenie vedeckého P2 a oddelenie organizačných skratiek

Dátum: 2026-07-15  
Typ: organizačný ochranný záznam; bez fyzikálneho výpočtu

## Autoritatívne ID

Plné ID starého kroku P2 je:

`SCI-A2K4-C7G5-K7C-P2-MLEDGER`

Krátke `P2`, `K7c-P2` a `K7c.3d` sú historické aliasy toho istého
vedeckého kroku. Organizačná fáza sa musí zapisovať `ORG-V2-P1` alebo
`ORG-V2-P2`; nikdy iba `P2`. Pilot spoločného jadra má ID
`BASE-V001-PARITY-197` a externý audit `AUD-C7G5-K7C-P1-RK4`.

## Nezmenený rozsah vedeckého P2

1. Skript 186 zostáva `DO_NOT_RUN_TECHNICAL`, nemení sa a nespúšťa sa.
2. Vznikne nový číslovaný iba diagnostický skript.
3. Použijú sa identické uložené NID/deep checkpointy
   `x=-25,-24.875,-24.75`; nepridáva sa nová ODE.
4. Rovnica `M'` sa rozloží na všetkých deväť už odvodených aditívnych členov.
5. Na tom istom zozname float64 členov sa porovná pôvodný súčet,
   `math.fsum` a 80-dps `mpmath.fsum`.
6. Povinný výstup obsahuje jednotlivé členy, znamienka, absolútne veľkosti,
   `sum_abs_terms/abs(HP_sum)`, obe chyby, zlepšovací faktor a škálovanú chybu.
7. Diagnostika nemení RHS, background, seed, closure, skóre ani fyzikálny verdikt.
8. Samostatná `fsum` evolučná podkoľaj smie vzniknúť až po výsledku P2.
9. `fsum` vysvetlenie prežije iba pri zlepšení najmenej 10 na každom
   aktívnom checkpointe. Timeout alebo technická chyba je REVIEW, nie smrť K4.

## Autoritatívne zmrazené zdroje

| Súbor | SHA-256 pri tomto zázname | Úloha |
|---|---|---|
| `Questions/A2_K4_C7_7C_K7C3D_M_RHS_TERM_LEDGER_PREREGISTRATION.md` | `D3307305E7B46F43E992B4AB37B53A29114D339061199B66A0510A81CAAF43C3` | presný rozsah a rozhodovanie P2 |
| `Questions/A2_K4_C7_7C_NEXT_RUN_PREREGISTERED_EXPECTATIONS.md` | `985F038EBD5DA6057DF9F1445E5D4B29E93ABE7A3B07F723EEB9C7444E64F487` | spoločné P0/P1/P2 očakávania |
| `Audit/A2_K4_K7C_P1_CLEAN_STANDALONE_RK4_FINAL_AUDIT_2026-07-15.md` | `382BA6463A561E5C317D54DCF37998AEAB5DF7EC046E31A1C896774C626B861B` | dôvod aktivácie P2 |
| `Questions/A2_K4_K7C_P1_CLEAN_STANDALONE_RK4_PRERUN.md` | `8AC07427DC4C5616FA0D7774781D32279EFB4B8C60C58FD93F75C1BBE4D294E9` | zmrazený P1 kontrakt |

Ak sa hash prvých dvoch zdrojov zmení, P2 sa nesmie spustiť, kým samostatný
audit nevysvetlí zmenu. Organizačný strom používa iba odkazy a tieto súbory
neprepisuje.

## Poradie práce

Neinvazívne `ORG-V2-P1` môže prebehnúť pred výpočtom, pretože iba vytvára
indexy, `HISTORY` a manifesty. Najbližší **vedecký výpočet** však zostáva
`SCI-A2K4-C7G5-K7C-P2-MLEDGER`. `BASE-V001-PARITY-197` ani externý audit
nesmú potichu nahradiť, zúžiť alebo rozšíriť jeho predregistráciu.

