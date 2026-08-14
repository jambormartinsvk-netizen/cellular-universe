# ERRATUM skriptov 40/41 — konvergencia adiabatického módu

**Dátum:** 2026-07-13  
**Prvý beh:** skript 40  
**Konvergentný nástupca:** skript 41

Skript 40 prešiel konečnosťou, počiatočnými constraintmi, globálnym 00
constraintom, `k` konvergenciou a bránou bez výbuchu relatívnej rýchlosti.
Nesplnil iba fixný krokový prah:

```text
výsledok = 1.1441025e-6
prah = 1.0e-6
```

Maximálny generovaný relatívny mód klesol pri polovičnom kroku z
`1.52455e-6` na `3.80450e-7` po normalizácii počiatočnou spoločnou
rýchlosťou, teda približne faktorom štyri. To zodpovedá diskretizačnému zvyšku
smerujúcemu k nule, nie fyzikálnemu rastu.

Skript 41 nemení rovnice, počiatočný mód, vlnové čísla ani prah. Používa jemnú
dvojicu krokov `6.25e-5` a `3.125e-5`. Skript 40 sa zachováva ako pôvodný
konvergenčne neuzavretý beh.
