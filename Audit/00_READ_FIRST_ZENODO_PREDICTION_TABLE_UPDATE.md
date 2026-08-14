# Čítaj ako prvé — zmena predikčnej tabuľky a Zenodo

## Povinné rozhodnutie

```text
Vieme, že stará hodnota je chybná? -> PT1: odvolať ju bez čakania na náhradu.
Máme validovanú novú hodnotu?       -> PT2: vydať aktualizovanú tabuľku.
Je nová hodnota ladená na dáta?     -> nie PREDICTION; označiť FIT/ESTIMATE.
```

## Autoritatívne dokumenty

1. `Questions/PREDICTION_TABLE_UPDATE_AND_ZENODO_RELEASE_PROTOCOL.md`;
2. `Questions/ZENODO_RELEASE_CHECKLIST_v3.18_ADDENDUM_PREDICTION_TABLE.md`;
3. `Questions/ZENODO_CHANGELOG_TEMPLATE_ADDENDUM_PREDICTION_TABLE.md`;
4. SK/EN register AR49 a Q75.

## Aktuálny blocker v3.18

Celá publikovaná tabuľka v3.17 ešte nemá riadkový audit aktuálnosti. R3.18-DOC ju nesmie automaticky skopírovať. Každý riadok musí dostať jeden z piatich stavov:

- `STILL CURRENT`;
- `SCOPE NARROWED`;
- `WITHDRAWN`;
- `REPLACEMENT VALIDATED`;
- `RECALCULATION OPEN`.

Odvolaná hodnota smie mať náhradu `NOT YET AVAILABLE`. To je vedecky poctivejšie než ponechať známu chybnú hodnotu ako aktuálnu predpoveď.

