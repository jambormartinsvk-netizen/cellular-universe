# Pokyny externému auditorovi EA-045

1. Pracujte iba so sealed balíkom a auditujte iba T1 otázku z dokumentu 00.
2. Najprv načítajte `EVIDENCE/009` až `013`; overte exact hashe voči
   charteru, profile voči manifestu a separation-of-duties identity.
3. Overte package-local manifest: všetkých `13` copy hashov, `20` package
   files, jednu response šablónu, `REPRO=0`, runtime rows `0`, nulové
   duplicity a absenciu temp súborov. Live-side R6 tool sa tu nespúšťa;
   jeho receipt je curator provenance, nie package-only príkaz.
4. Bez zápisu do balíka si listnite source archive a zobrazte iba
   `main.tex` na štandardný výstup; neextractujte ho do balíka a
   nevyhľadávajte live projekt ani internet.
5. Overte source-exact Boltzmann/EMT/conservation/wall-profile/terminal
   interface claims a presné boundary medzi nimi a W10 passportom.
6. Overte každý W10 missing field a S0–S13 mapu voči source/receipt/result;
   `TOTAL_EMT_ONLY` nesmie byť povýšené na disjunktný RW1 ledger a plasma
   flow nesmie byť potichu premenený na parent-cell flow.
7. Nevytvárajte W10 mapping, no-go, new physics, physical verdict, score,
   depth ani run permission. Nevykonávajte Python, solver, download alebo
   generated JSON.
8. Zapíšte do response presný príkaz, exit code a wall time pre každú
   vykonanú package-local kontrolu; nebežiace smoke/official vetvy označte
   `NOT_RUN`, lebo neexistujú. Každú odchýlku uveďte explicitne.
9. Každý hlavný záver označte evidence tagom a osobitne uveďte dopad na
   package tier a na fyzikálny scope/verdict.

Povinné ledger termíny: `generated JSON`, `exit code`, `wall time`,
`odchýlka`.
