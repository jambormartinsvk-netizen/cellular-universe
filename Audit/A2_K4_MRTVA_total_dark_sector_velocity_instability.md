# A2-K4 — MŔTVA: smer celkovej tmavosektorovej rýchlosti

**ID:** M-011  
**Dátum:** 2026-07-13  
**Stav:** `MŔTVA — ARCHIVOVANÁ`

## Presná koľaj

```text
Q_f^mu=-Gamma rho_f u_d^mu,
Q_c^mu=+Gamma rho_f u_d^mu,
(rho_c+delta rho_f)theta_d=rho_c theta_c+delta rho_f theta_f.
```

## Dôvod smrti

Symbolická interakčná matica relatívnych rýchlostí má

```text
det M=-r^2/(1+delta r)<0,
```

teda fyzický kladný relatívny eigenmód. Plný prvý superhorizontový systém s Einsteinovými constraintmi dal voči konzistentnému `Gamma=0` modelu

```text
relative-velocity gain=108028.1391,
log gain=11.5901470.
```

Kroková aj `k` konvergencia prešli a globálne `00` rezíduum bolo `3.01385e-10`.

## Rozsah

Výpočet používa perfektnú radiáciu a je prvým superhorizontovým testom, nie náhradou plnej Boltzmannovej hierarchie. Koľaj však už narazila na predregistrovanú stenu fyzického relatívneho módu, ktorý by bez mikrofyzického dôvodu vyžadoval ručné potlačenie počiatočnej amplitúdy.

## Zachované neúspešné behy

- skript 28: iba JSON serializačná chyba po dokončení integrácie;
- skript 29: `REQUIRES_FULL_REVIEW` pre nedostatočne jemný krok a zle podmienenú bodovú normu constraintu;
- skript 30: konvergentný finálny nástupca bez zmeny fyziky.

## Podmienka znovuotvorenia

Nové odvodené počiatočné podmienky alebo mikrofyzická akcia musia dokázať absenciu rastúceho módu. Samotná zmena numerického kroku, gauge alebo tiché predefinovanie `u_d` nestačí.

