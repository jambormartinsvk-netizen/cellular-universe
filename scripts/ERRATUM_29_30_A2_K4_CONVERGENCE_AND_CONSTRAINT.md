# Erratum skriptu 29 a konvergentný nástupca 30

**Dátum:** 2026-07-13

## Prečo skript 29 nerozhodol

Skript 29 korektne vypočítal veľké interakčné zosilnenie, ale neprešiel dvoma numerickými bránami:

- dvojica krokov `5e-4/2.5e-4` dala relatívny rozdiel logaritmu rastu `1.389e-6`, nad prahom `1e-7`;
- bodová normalizácia Einsteinovho constraintu bola zle podmienená, keď všetky jeho členy súčasne prechádzali blízko nuly.

Preto skript 29 správne vrátil `REQUIRES_FULL_REVIEW` a zostáva zachovaný.

## Čo mení skript 30

- používa kroky `1.25e-4` a `6.25e-5`;
- integruje background iba po presný `x_star`, nie do nepoužitého skoršieho intervalu;
- constraint hodnotí globálnou normou `max|C|/max(sum|C_i|)`;
- zachováva aj bodový diagnostický údaj nad nenulovým floorom.

## Čo nemení

- fyzikálne rovnice skriptu 28;
- entalpickú definíciu `u_d`;
- počiatočný relatívny mód;
- hodnoty `k/H0`;
- porovnanie s konzistentným `Gamma=0` modelom;
- fyzikálnu kill bránu viac než jedného dodatočného interakčného e-foldu.

