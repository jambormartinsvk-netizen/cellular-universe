# K7c.3b — predbehový dodatok k uzavretiu RK4 mriežky

Dátum: 2026-07-15  
Stav: zapísané pred prvým výpočtovým behom K7c.3b

Pôvodné kroky `0.002/0.001` nedelia presne polovicu intervalu s dĺžkou `0.125`; hrubá mriežka by potrebovala neuniformný zvyškový krok. Aby začiatok, midpoint aj koniec ležali na oboch uniformných mriežkach, kroky sa pred prvým výsledkom opravujú na:

- hrubá mriežka `h=0.0025`, 100 krokov;
- jemná mriežka `h=0.00125`, 200 krokov.

Pomer krokov zostáva 2:1. Interval, RHS, seed, envelope škála, RK4 metóda, limit 2 000 RHS volaní, safety cap a acceptance `endpoint difference <1e-6` sa nemenia. Pôvodná predregistrácia sa nemaže.
