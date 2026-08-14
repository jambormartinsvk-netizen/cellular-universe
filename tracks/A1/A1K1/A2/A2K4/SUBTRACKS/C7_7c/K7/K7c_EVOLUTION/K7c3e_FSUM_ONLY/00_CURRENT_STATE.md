# K7c.3e — iba presnejšie finálne sčítanie `M'`

Stav: **STOP / MŔTVA**  
Dátum: 2026-07-15  
Score effect: `NONE`

Hypotéza tvrdila, že nekonvergenciu K7c spôsobuje obyčajné ľavostranné
sčítanie deviatich float64 členov `M'` a že ho vyrieši `math.fsum`.

Skript 199 na troch bitovo zhodných P1 checkpointoch zistil zlepšenie `1×`
vo všetkých prípadoch. Obyčajný súčet a `math.fsum` dali rovnaký výsledok.
Vetva je preto mŕtva a nesmie sa znovu otvoriť iba inou summation rutinou.

Príčina nezrovnalosti leží pred finálnym súčtom: dve koeficientové
kombinácie sa vo float64 vytvárajú odčítaním veľkých členov, hoci sú podľa
backgroundových identít presne nulové. To patrí do novej P3a vetvy, nie do
oživenia tejto vetvy.

Rozhodujúci audit:
`Audit/A2_K4_C7_7C_K7C_P2_MPRIME_LEDGER_FINAL_AUDIT_2026-07-15.md`.
