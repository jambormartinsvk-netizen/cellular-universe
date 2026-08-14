# Akčný plán v3.18 — Zenodo publikačná brána

## Rozhodnutie

Najbližší verejný kandidát zostáva `R3.18-DOC`. Aktuálny stav je `NO-GO`, kým neprejde release checklist. Otvorená K4/G7 neblokuje dokumentačné vydanie, ale blokuje nové tvrdenia o úplnej perturbatívnej teórii a nové kozmologické predikcie.

## Poradie vydávacej práce

| Krok | Úloha | Výstup | Stop podmienka |
|---:|---|---|---|
| Z1 | dokončiť inventár a cieľovú adresárovú mapu | manifest starých ciest a návrh nových | nejasná kolízia alebo rozbitie auditných odkazov |
| Z2 | vytvoriť jediný kanonický verejný stav v3.18 | `READ_FIRST`, tabuľka tvrdení a otvorených brán | rozpor medzi aktuálnymi dokumentmi |
| Z3 | vyplniť changelog v3.17 -> v3.18 | šablóna s `OLD -> NEW -> REASON -> EVIDENCE` | materiálna zmena bez dôkazu |
| Z4 | zosúladiť SK/EN a README/citácie | jazykový a citačný audit | rozdiel významu SK/EN |
| Z5 | pripraviť čistý release tree | bez cache, secrets a lokálnych závislostí | nejasný pôvod súboru |
| Z6 | vytvoriť manifest a SHA-256 | zmrazený RC balík | akákoľvek ďalšia zmena resetuje RC |
| Z7 | commit, tag a release audit | Git SHA, tag, podpísaný checklist | auditný FAIL |
| Z8 | Zenodo draft, preview a publish | nový verziový DOI | nezhoda draftu s tagom |
| Z9 | post-publish download/hash/citation kontrola | `PUBLISHED AND VERIFIED` | hash alebo DOI nezhoda |

## Oddelenie od fyzikálnej práce

- K4 profilovanie a A2 práca pokračujú v pracovnej vetve.
- Po zmrazení RC sa doň nepridávajú nové priebežné audity.
- Nové výsledky po RC patria do nasledujúceho changelogu, ak nejde o kritickú chybu RC.
- `R3.18-PHYS/PREDICTION` sa nezačne iba premenovaním DOC balíka; potrebuje vlastný scope a fyzikálne brány.

