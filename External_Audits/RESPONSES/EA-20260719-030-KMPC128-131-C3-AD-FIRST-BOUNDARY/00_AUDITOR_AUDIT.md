# Externý audit — EA-030 KMPC-128 až 131 C3 AD hranica

- Audit ID:
- Auditor/model/verzia:
- Dátum a časová zóna:
- Read-only: áno/nie
- Audit mode: reprodukčný/forenzný
- Manifest PASS/FAIL:
- Najvyšší dosiahnutý tier:
- Python/NumPy/BLAS/OS/architektúra:

## Rozsah a nonclaims

Auditujem:

Výslovne neauditujem:

## Integrita a reprodukcia

| Vetva | Presný príkaz | exit code | wall time | generated JSON SHA-256 | výsledok |
|---|---|---:|---:|---|---|
| manifest/preflight |  |  |  | n/a |  |
| smoke 4/4 |  |  |  | n/a |  |
| missing prerequisite |  |  |  | n/a |  |
| AD/.005 official |  |  |  |  |  |
| AD/.05 official |  |  |  |  |  |

## Kontroly tvrdení

| Tvrdenie | Evidence tag | Metóda | Výsledok |
|---|---|---|---|
| KMPC-128→131 nemení rovnice/prahy |  |  |  |
| AD/.005 gamma0 a af0 PASS |  |  |  |
| AD/.05 zlyháva iba tailom |  |  |  |
| nulové limity a af0 bridge na .05 PASS |  |  |  |
| `.15` zostal NOT_RUN |  |  |  |

## Nálezy

### F-001 — [CRITICAL/MATERIAL/MINOR/EDITORIAL]

- typ:
- presný zdroj:
- pozorované:
- očakávané:
- dopad na package tier:
- dopad na fyzikálny verdict:
- minimálny reprodukčný test:

## Neautoritatívne odporúčanie

`AGREE_IN_SCOPE / AGREE_WITH_LIMITATION / DISAGREE / CANNOT_AUDIT`

Odôvodnenie:

Čo by zmenilo odporúčanie:

## Trigger kontrola

- K4 score:
- prediction table:
- release:
- Zenodo:

## Vyhlásenie autority

Tento externý posudok nemení projektový PASS/REVIEW/STOP. Autoritatívny zápis
vykonáva iba hlavný orchestrátor.
