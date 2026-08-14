# Jednotná sekvenčná stupnica hĺbky — manifest SHA-256

**Dátum:** 2026-07-14  
**Rozsah:** AR30/Q57, rekalibrácia A2-K1 až K12, K7 podkoľaje a aktuálne
stavové dokumenty  
**Fyzikálne rozsudky:** nezmenené

## Kontrolné súčty

```text
266651278e22b291d84e0360cd280b093f53937338d00a1c653df1b759c497f5  Audit\JEDNOTNA_SEKVENCNA_STUPNICA_HLBKY_A2_A_REKALIBRACIA_K1_K12.md
0b17f6d800cbd25122637b3cfab709c9722216e00fcb6c17e622488eeef9495c  Audit\A2_K4_2_SCORE_RECALIBRATION_ADDENDUM_59_TO_60.md
c02de85ca97d19ad20500f8ddc60bc48df5dc72b411200bc457a74fbce6d4eea  theory\SK\05zzz_Methodology_Rules_and_Question_Register_Sequential_Depth_SK.md
41debaf94271c32f80d16f8fdb53d14bf1c7376b769a8b7ebd973eb32f6009cd  theory\EN\05zzz_Methodology_Rules_and_Question_Register_Sequential_Depth_EN.md
069d9665ef0430a49f2ad831de0c119cc61ebaf455b6b3527130901bfd2d0a59  Audit\A2_KATALOG_STAV_SKORE_A_DOVOD_SMRTI_K1_AZ_K11.md
c6fee454b4fcd8ad1700b6fbd8459c02def675786c6f5b6e2688bfed6f419f5f  Audit\A2_K7_PODKOLAJE_KANONICKY_STAV_A_MAX_HLBKA.md
634764bdd6722724061541db9b27c8073350307ebb81bbccd850986593502fcc  Audit\A2_KATALOG_KOLAJI_K1_AZ_K10_ZROZUMITELNY_SUMAR.md
f8dcc79b7b7b3e9f0597a407d6682e94182896aefa021642575cfe8d5af645be  Questions\00_READ_FIRST_A2_Q20_CURRENT_STATE.md
af2f17371849c9e62effe1a23a19201299e58e886c205fa3e7decbb63338fcba  Questions\00_AKCNY_PLAN_v3.18_AKTUALNY_2026-07-13.md
a5b6c26adff214ab91af7ce881737306deb0c51e653ad813a467c9bb6ea16a0c  Questions\A1_K1_A2_AUDITNY_PROGRAM_A_STOPPING_KRITERIUM.md
a6a0463e5e8fb97683e0cf9b69636f463547f36d4e2b859581edfe7926c56c3d  Questions\A2_K12_PROBLEM_KOLAJE_A_DALSI_POSTUP.md
67363cb286f04c52665e01a5a16ba736f4fcbfe76004ab16bb074320027131a4  Questions\A2_K11_STAV_A_AKCNY_PLAN_PO_AUDITE_SKRIPTU_45.md
6cb59ee7aaf557e4fe01dddf1a997e4dea8882f5d9b207caa1d6cb9ebd555b1a  Questions\A2_K11_STAV_PO_REVIZII_973905D_A_DALSI_KROK.md
```

## Changelog významu skóre

- predtým: najhlbší vykonaný test mohol byť vydávaný za max. hĺbku;
- teraz: skóre je iba najvyššia sekvenčne prejdená G-brána;
- najhlbší test a brána smrti sú samostatné polia;
- historické percentá sa nemažú, ale nie sú kanonickým porovnávacím skóre;
- K4 sa rekalibruje `59 -> 60=G6` bez zmeny fyziky;
- K5 `75 -> 40=G4`, pričom G8 hybridný kill M-012 zostáva platný;
- K6 `60 -> 30=G3`, pričom G6 no-go M-013 zostáva platný;
- K7 checkpointy 32–42 sa zachovávajú ako intra-G3, kanonická hĺbka je G2=20.

Pri budúcej úprave ktoréhokoľvek zahrnutého súboru sa vytvorí nový manifest;
tento snapshot sa spätne neprepisuje.
## Validačný log

- všetkých 13 kontrolných súčtov bolo úspešne vypočítaných bezprostredne
  pred vytvorením manifestu;
- samostatná kontrola očakávaných G-skóre a neprítomnosti starých
  neoznačených kanonických tvrdení skončila `CANONICAL_SCORE_CONSISTENCY_OK`;
- dva následné dávkové replaye hashov zostali visieť v orchestračnom obale a
  boli ručne ukončené po 30 sekundách; podľa AR29 majú stav
  `TIMEOUT — VALIDÁCIA NEUZAVRETÁ`, nie hash mismatch ani fyzikálny FAIL;
- krátky samostatný odtlačok tohto manifestu po timeoutoch prešiel:
  `C8F58FD179A4B29BF155C4510E9B3A53BF90D5B31A0783A5644926389C3FB5EE`
  pre verziu manifestu pred pridaním tohto validačného logu.

