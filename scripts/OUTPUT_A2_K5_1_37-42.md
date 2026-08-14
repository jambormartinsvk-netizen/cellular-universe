# A2-K5.1 — rozhodovacie výstupy skriptov 37 až 42

**Dátum behov:** 2026-07-13

## Skript 37

```text
checks = 13/13 PASS
beta_0 = 1.52883319743
min meff^2/H0^2 = 21.5384259282
status = PASS_K5_1_EQUATION_GATE
```

## Skript 38 — odmietnutý

```text
global relative 00 residual = 0.106559262
threshold = 1e-5
status = FAIL_OR_DEAD_REVIEW
```

Príčina bola implementačná: zdvojené `X_f` v skalárnej entalpii. Fyzikálny
transfer skriptu 38 je neplatný.

## Skript 39 — finálny relatívny mód

```text
coupled transfer = 6.977880288e-6
lambda=0 transfer = 1.469347225e-5
coupled/null gain = 0.474896619
log gain = -0.744658143
step difference = 2.36820e-9
k difference = 6.94518e-13
global 00 residual = 1.47543e-9
status = PASS_K5_1_SUPERHORIZON_GATE
```

## Skript 40 — konvergenčne odmietnutý

```text
step difference = 1.1441025e-6
threshold = 1.0e-6
other physical checks = PASS
status = FAIL_OR_DEAD_REVIEW
```

## Skript 41 — finálny adiabatický mód

```text
max relative / initial common velocity = 9.44204e-8
final relative ratio = -8.89039e-8
step difference = 2.86030e-7
k difference = 6.93128e-10
global 00 residual = 1.21728e-10
status = PASS_K5_1_ADIABATIC_GATE
```

## Skript 42 — kvázistatický limit

```text
all independent coefficient differences = 0.0
Geff/G today:
  q=30  -> 5.56540453
  q=100 -> 5.66461504
  q=300 -> 5.67354344
status = PASS_K5_1_QS_CROSSCHECK
```

Záver: superhorizontové brány prešli, subhorizontový rastový alarm zostáva.
