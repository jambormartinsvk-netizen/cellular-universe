# READ FIRST — A2 po K7c P3b

Dátum: 2026-07-15

Aktuálne: **A2-K4 je živá na `66.5/100`; P3b kroková konvergencia PASS,
celý C7-G5 je ešte PARTIAL PASS / REVIEW.**

- P3a-A dokázalo dve presné nulové identity.
- Source-delta audit 207 potvrdil, že skript 205 odstránil iba tieto dva
  nulové členy a nezmenil ostatnú fyziku ani numerický kontrakt.
- P3b dalo `diff200/400 = 3.0308221211e-14` a RK4 pomer `16.004121`.
- Starý P1 ne-RK4 výsledok ostáva zachovaný, ale platí iba pre legacy
  float64 zápis; nie je už blockerom kanonicky opravených rovníc.
- Fsum-only vetva zostáva mŕtva.
- Hĺbka sa nemení, pretože jedna NID/deep krátka kroková konvergencia nie je
  celá G5 ani G4/G6.

Najbližší vedecký krok je nová preregistrácia v poradí:

1. G5 metódová a tolerančná kontrola na rovnakej ploche;
2. G4 netautologické activity/constrainty;
3. G6 NID/NIV × deep/shallow.

Kľúčový audit:
`Audit/A2_K4_C7_7C_K7C_P3B_ZERO_IDENTITY_RK4_FINAL_AUDIT_2026-07-15.md`.

