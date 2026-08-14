# Pokyny pre externého auditora

Najprv overte TSV manifest, source/copy parity a runtime mapu. Potom auditujte
vzorec → base → runner → raw lineage a spustite reprodukciu v pracovnej kópii
`REPRO`, nie v zapečatenom adresári.

Pri každom procese uveďte presný príkaz, exit code, wall time, verziu Pythonu,
NumPy/BLAS, OS/architektúru a SHA-256 generated JSON. Zaznamenajte každú
odchýlku od pokynov. Parent official má vonkajší limit 10 s; štyri child
support workery majú každý interný limit 4.8 s.

Povinné kontroly:

1. manifest a exact 29-položkový runtime register;
2. smoke `4/4`, bez raw a bez fyziky;
3. negatívny chýbajúci-prerequisite guard;
4. official `.005` a `.05` v fresh copy;
5. field parity generated JSON voči priloženým rawom po odstránení iba polí
   pomenovaných `runtime_seconds` a vnorených worker runtime polí;
6. nezávislý prepočet najhorších `.05` tail hodnôt a pomeru k `1e-6`;
7. potvrdenie, že generated JSON pre `.005` je PASS a `.05` iba tail REVIEW.

Odpoveď musí oddeliť package tier od fyzikálneho verdiktu a označiť hlavné
tvrdenia tagmi `OBSERVED_IN_PRIMARY`, `INDEPENDENTLY_RECOMPUTED`,
`INFERRED_FROM_PROJECT_DOCS` alebo `CONTEXT_ONLY`.

