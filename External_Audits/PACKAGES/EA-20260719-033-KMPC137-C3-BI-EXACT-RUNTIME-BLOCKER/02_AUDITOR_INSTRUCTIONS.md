# Pokyny externému auditorovi

1. Auditujte iba otázku a T1 hranicu v dokumente 00.
2. Spustite package preflight a uveďte presný príkaz, exit code a wall time.
3. Overte source/copy hashe všetkých 27 položiek; balík nemeňte.
4. Zo source a rawov overte `34.86 s / limit 45 s` v KMPC-112 a
   `4.8 s worker / 9 s parent` v KMPC-137.
5. Overte, že KMPC-137 má `4/4` úspešné coefficient shardy, `0/2` exact
   payloady a `physics_verdict=NONE_TECHNICAL_FAILURE`.
6. Overte, že KMPC-136/137 nemenia exact equations, matrix shape, 80 dps ani
   thresholdy; ak to z T1 source nemožno potvrdiť, označte presnú medzeru.
7. Zoraďte tri cesty podľa minima matematickej zmeny, auditovateľnosti,
   runtime rizika a počtu nových artefaktov.
8. Pri každom závere použite evidence tag. Každú odchýlku označte
   package-integrity, implementation, numerical, physics, documentation
   alebo scope/tier.
9. Nevykonávajte official Python; žiadny generated JSON sa neočakáva.
   Dobrovoľný beh je `DECLARED_DEVIATION` a nemení tier ani verdikt.
10. Nemeňte projektový verdikt, score ani zákaz automatického KMPC-138.

