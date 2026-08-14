# A3/Q20 — stav a akčný plán po oprave číslovania koľají

**Dátum:** 2026-07-13  
**Nahrádza pre budúcu prácu:**
`Questions/A3_STAV_A_AKCNY_PLAN_PO_M012_A_K3a_0.md`  
**Starší súbor zostáva historickou auditnou stopou.**

## Kanonický stav

| Koľaj | Stav |
|---|---|
| A2-K1 | `MŔTVA M-009` |
| A2-K2 | `MŔTVA M-008` |
| A2-K3 | `MŔTVA M-010` |
| A2-K4 | `MŔTVA M-011` |
| A2-K5 | `MŔTVA M-012` — konkrétna konformná akcia, historicky aj `K5/K1` |
| **A2-K6** | `PREŽÍVA K6.0 — 40/100`; historický alias `K5/K3a` |
| **A2-K7** | `ČAKÁ`; historický alias `K5/K4a` |
| **A2-K8** | `ČAKÁ`; historický alias `K5/K2a` |
| **A2-K9** | `ČAKÁ`; historický alias `K5/K6` |
| **A1-K2/A2-K10** | `ČAKÁ`; historický alias `A1-K2/A2-K6a` |

## Aktívny krok A2-K6.1

1. odvodiť úplné gauge-invariantné rovnice akcie
   `f=-f1(phi)rho_c+eta Z^2`;
2. overiť nulové limity `eta->0` a `f1->0`;
3. odvodiť presné `G_cc`, `G_cb`, `G_bc`, `G_bb`;
4. použiť predregistrovaný grid `eta={0,0.1,0.5,1,2,5}`;
5. rozhodnúť `PREŽÍVA N/100` alebo `MŔTVA M-013`;
6. ak K6 zomrie, ďalšia koľaj je A2-K7, nie dieťa K5.

## Paralelný krok dokumentácie

Pri budúcom uprataní sa staré názvy neprepisujú bez stopy. Mapa presunov a
aliasov musí obsahovať toto errátum. Nové názvy súborov, sekcií a skriptov
už používajú A2-K6 až A2-K10.

## Rozhodovacie dokumenty

- `Audit/ERRATUM_taxonomie_novych_A2_kolaji_po_M012.md`
- `Questions/A2_KANONICKY_STROM_NOVYCH_KOLAJI_PO_PRICINACH_SMRTI.md`
- `Audit/A2_analyza_hlavnych_pricin_smrti_kolaji.md`

## Zachovanie histórie

Staršie formulácie s `K5/K...` nie sú vymazané, pretože vysvetľujú, ako
chybná taxonómia vznikla. Od tohto dokumentu však nemajú riadiť poradie ani
rodičovstvo koľají.
