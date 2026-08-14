# Erratum 67B — aritmetický midpoint backgroundu znížil rád RK4

**Dátum:** 2026-07-14  
**SHA-256 verzie pred opravou 67B:**
`73B77A06C8EF7314431C92B38AEC8473348A0B2F99C88DC337B7210454071688`

Po oprave JSON skript 67 správne vydal `REQUIRES_REVIEW`. Pri krokoch
`5e-4` a `2.5e-4` boli rozdiely finálnej matice

```text
0.0154335 a 0.00385880
```

voči adaptívnej referencii. Pokles približne faktorom štyri ukázal druhý,
nie štvrtý rád. Príčinou bol riadok

```text
sm = 0.5*(s0+s1)
```

ktorý poskytoval background v polkroku iba s chybou druhého rádu. Oprava
vypočíta `sm` samostatným polkrokovým RK4 z `s0` pomocou tej istej
backgroundovej ODE.

Toto erratum nemení perturbatívne rovnice, počiatočnú bázu, referenčné čísla
ani prahy. Ide o opravu nezávislého solvera. Predchádzajúci `REQUIRES_REVIEW`
sa zachováva ako platný diagnostický neúspech; fyzikálny rozsudok čaká na
nový celý beh.

