# READ FIRST — A2 po K7c P3a-A

Dátum: 2026-07-15

Aktuálne: **A2-K4 je živá na `66.5/100`; P3a-A PASS, evolučná G5 stále REVIEW.**

- P1 reprodukovalo nekonvergentný RK4 pomer `0.367129`.
- P2 zabilo fsum-only vetvu: `math.fsum` dalo iba `1×` zlepšenie.
- P3a-A presne dokázalo, že dva problematické koeficienty `M'` sú nula.
- Najhoršie 80-dps normalizované rezíduum bolo `2.5069e-81 < 1e-70`.
- P3a-A neintegrovalo ODE a nemá skórový účinok.
- Aktuálny corpus checker 202 prešiel s 206 ostatnými skriptmi a 71
  karanténnymi položkami.
- Najbližší krok je izolovaná P3a-B RK4 100/200/400, nie CMB/S8.

Ak P3a-B prejde pomerom `8–32` aj `diff200/400 < 1e-6`, otvorí širší
G4/G6 audit. Ak nie, algebraická evolučná vetva zomrie a nasleduje samostatný
audit lokálnej tuhosti/eigenmódov.

Kľúčový audit:
`Audit/A2_K4_C7_7C_K7C_P3A_EXACT_ZERO_IDENTITY_FINAL_AUDIT_2026-07-15.md`.
