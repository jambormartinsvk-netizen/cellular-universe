# Q20/A2 — čítaj ako prvé po BR3B-2f-5 skripte 124

Dátum: 2026-07-14

| Koľaj | Stav | Kanonické skóre | Aktuálna interná brána |
|---|---|---:|---|
| A2-K4 | **ŽIVÁ** | **60/100 = G6** | G7/BR3B-2g: `l=3` + ash ledger |

## Aktuálny rozsudok

BR3B-2f-5 **PREŠLA**. NID aj NIV zmiešané reťazce od najskoršieho fuel
sektora po common fuel sú úplné v auditovanom prvom ráde v `Phi`:

- NID: `p -> p+1 -> p+2 -> p+3`;
- NIV: `p-1 -> p -> p+1 -> p+2`.

Obe matice majú hodnosť `36/36`; všetkých 26 kontrol prešlo. K4 preto žije,
ale skóre zostáva 60/100, lebo celý G7 ešte neprešiel.

## Dôležité erratum

Skript 108 v neutrínovom shear zdroji použil fotónovú rýchlosť. Jeho staré
shear čísla už nie sú kanonický oracle. Súbor ani výsledok sa nemaže; dôvod
obmedzenia a corrected-oracle koeficienty sú v audite BR3B-2f-5. Skripty
118–123 sú rovnako zachované so stavom a dôvodom, prečo nemajú finálnu
dôkaznú váhu.

## Nasleduje

BR3B-2g: doplniť prvý neskorší `l=3` feedback, ash transfer a prvý gravitačný
ash sektor. Až potom BR3C s evolúciou z dvoch skorých hĺbok.

Autoritatívny audit:
`Audit/A2_K4_3B_RG_BR3B2F5_FULL_MIXED_CHAIN_AUDIT.md`.

