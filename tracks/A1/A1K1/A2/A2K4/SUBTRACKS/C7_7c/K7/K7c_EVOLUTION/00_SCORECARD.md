# K7c — score effect

K7c dodala rodičovský G3 PASS (váha 10). Historický G5 blocker z P1 je po
P3a/P3b obmedzený na chybnú float64 reprezentáciu dvoch presných núl.
Aktuálna opravená formulácia má krokovú časť G5 PASS, ale celý G5 ostáva
REVIEW bez metódovej a tolerančnej konvergencie. G4 ostáva otvorená, pretože
cancellation monitory P1 nie sú nezávislé dynamické constrainty. Ostatné
váhy patria rodičovskému K7 scorecardu a nesmú sa tu sčítať druhýkrát.

P2, P3a-A a izolovaná P3b majú `score effect: NONE`. P3b preukázala iba
krokovú konvergenciu na jednej krátkej NID/deep ploche. STOP vetvy
`K7c.3e fsum-only` nemení rodičovskú hĺbku `66.5/100`; iba zabraňuje
opakovať už vyvrátené riešenie.

