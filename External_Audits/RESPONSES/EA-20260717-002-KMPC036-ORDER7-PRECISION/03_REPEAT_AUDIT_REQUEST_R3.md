# Žiadosť o opakovaný externý audit — R3

Prosím auditovať revíziu `R3_REFREEZE_AFTER_EXTERNAL_TECHNICAL_STOP` balíka
`EA-20260717-002-KMPC036-ORDER7-PRECISION`.

## Primárna otázka

Odstránilo doplnenie presného KMPC-035 prerequisite pôvodný
`FileNotFoundError` a je teraz predpísaná `--audit` vetva reprodukovateľná
bez obídenia guardov?

## Povinné kontroly

1. Over celý R3 manifest.
2. Over hash prerequisite v `EVIDENCE/015` aj v `REPRO/`.
3. Spusť smoke a oficiálny audit presne podľa dokumentu 03, oba s externým
   timeoutom 10 s.
4. Zapíš Python, NumPy, BLAS/LAPACK, OS/architektúru, exit code a wall time.
5. Rozlíš technický výsledok od fyzikálneho; neprideľuj projektový verdikt.
6. Ak sa podmnožina floor-level failov líši od Windows referencie, porovnaj
   absolútne rezíduá, `term_norm`, rank, anchor, regresie a holdouty.

Nie je potrebné opakovať nepredregistrované mixed-precision experimenty.
Ak ich napriek tomu vykonáš, označ ich oddelene ako deklarovanú odchýlku.

Výstup ulož ako nový Markdown. Ak nemáš zápisové právo, vráť celý text;
hlavný orchestrátor ho importuje verbatim bez prepisovania starších súborov.
