# A2-K4 / C7.7c / K7c.3a.1 — predregistrácia normalizovaného basis probe

Dátum: 2026-07-15  
Rodič: K7c.3a / skript 181

Jediná povolená zmena je nahradiť fyzikálny jednotkový probe `e_j` lineárne ekvivalentným probe `S_j e_j` a stĺpec vydeliť `S_j`. Tým safety cap vidí normalizovanú amplitúdu 1.

Zakázané sú zmeny RHS, seedu, škály, spektrálneho prahu `1e-10`, RHS-rekonštrukčného prahu `1e-12` a časových limitov. Stále sa nevykoná ODE ani FD/SVD condition diagnostika.

PASS znamená iba platný operátorový profil. FAIL spektrálnej similarity alebo `A*y` po tejto oprave sa musí zdokumentovať pred ďalším solverom.
