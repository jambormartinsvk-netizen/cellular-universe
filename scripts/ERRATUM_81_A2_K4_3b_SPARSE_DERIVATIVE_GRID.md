# Rozsah skriptu 81 — riedka derivatívna mriežka

Skript 81 korektne rekonštruoval Newtonovské potenciály z dokumentovaných
CAMB transferov. Jeho nezávislá kontrola `Psi=(sigma'+H sigma)/k` však
derivovala dáta na mriežke s pomerom susedných `k tau` rovným 2.

Pri CDI a BI, kde sú potenciály malé, vznikli maximálne absolútne rezíduá
`5.48e-5` a `4.13e-5`; pôvodná brána `2e-5` preto správne vydala
`REVIEW_REQUIRED`. Nejde o fyzikálnu smrť ani chybu algebraickej Weylovej
identity. Skript 82 opakuje nezávislú kontrolu s predregistrovaným pomerom
1.25. Skript 81 sa zachováva ako negatívny test numerickej derivácie.
