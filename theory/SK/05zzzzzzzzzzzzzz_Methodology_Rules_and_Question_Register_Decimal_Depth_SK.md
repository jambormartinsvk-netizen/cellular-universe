# Dodatok k 05 — jemná desatinná auditná hĺbka (SK)

**Dátum:** 2026-07-14  
**Stav:** záväzný dodatok; staršie pravidlá sa nemenia

## Kontrola duplicity

AR14 oddelila hĺbku auditu od pravdepodobnosti pravdy. AR18 zabránila, aby
výsledok podkoľaje automaticky povýšil rodiča. AR30 zaviedla rovnaké
sekvenčné brány G1–G10 po desiatich bodoch. Chýbal však spôsob, ako bez
udelenia celej brány zobraziť auditovaný postup **vnútri** otvorenej brány.
AR43 dopĺňa práve túto medzeru.

## AR43 — Stav koľaje má pevnú bránu aj jemnú auditnú hĺbku

Každá aktuálna stavová tabuľka musí rozlišovať:

1. **poslednú úplne prejdenú kanonickú bránu**, napr. `G6 PASS`;
2. **jemnú auditnú hĺbku**, napr. `66.0/100`;
3. **stav aktívnej brány**, napr. `G7 OTVORENÁ`.

Interval medzi dvoma kanonickými bránami má presne `10.0` auditných bodov.
Pred ďalším výpočtom sa rozdelí na zoradené dôkazové checkpointy s váhou
`0.1` až `1.0` bodu. Váhy v jednom intervale musia dať presne `10.0`.

Pre koľaj s poslednou prejdenou bránou `Gg` je jemná hĺbka

```text
D_fine = 10*g + súčet váh súvisle prejdených checkpointov brány G(g+1).
```

Platia tieto obmedzenia:

- checkpoint musí mať pred výpočtom zapísaný výstup, acceptance kritérium,
  závislosti a dôkazový súbor;
- body sa neprideľujú za čas, počet behov, počet rovníc, dokumentáciu samu
  osebe ani za priaznivý výsledok bez uzavretej brány;
- skóre rastie iba po **súvislom** poradí checkpointov; neskorší vykonaný
  test za otvorenou medzerou sa vedie ako najhlbší vykonaný test, nie ako
  získaný bod;
- čiastočný PASS checkpointu nedáva pomernú časť jeho váhy, ak jeho vlastný
  register výslovne neobsahuje menšie checkpointy;
- jemná hodnota `69.8/100` stále neznamená `G7 PASS`; do `70.0/100` sa koľaj
  dostane iba integrovaným rozsudkom celej G7;
- jemná hĺbka nepromuje rodiča cez pravidlo AR18 a nie je pravdepodobnosťou,
  confidence ani percentom pravdivosti;
- ak neskorší audit zruší predpoklad získaného checkpointu, aktuálna jemná
  hĺbka sa zníži a zmena sa zdôvodní v changelogu; historické maximum a
  chybný dôkaz sa nemažú;
- mŕtva koľaj si ponechá poslednú úplnú bránu, maximálnu dosiahnutú jemnú
  hĺbku, najhlbší vykonaný test, skripty a dôvod smrti.

Checkpointy sa nesmú umelo drobiť iba preto, aby skóre rástlo. Každý musí
uzatvárať samostatne auditovateľné fyzikálne alebo numerické tvrdenie.

## Prechod starších koľají

Staršie celé skóre zostáva správnym údajom o poslednej prejdenej bráne.
Desatinné body sa spätne nevymýšľajú podľa toho, kde koľaj zomrela. Koľaj bez
spoľahlivého zoradeného ledgeru ostáva napríklad na `40.0/100` a jej hlbší
vykonaný no-go sa naďalej uvádza osobitne.

Jednorazová rekonštrukcia živej K4 je prípustná, pretože jej G7 balíky boli
chronologicky pomenované a archivované pred týmto dodatkom. Ich váhy sa
zmrazujú pred BR3C; nesmú sa meniť podľa jeho budúceho výsledku.

## Q70 — Ako sa má odteraz zobrazovať reálny postup K4?

**Stav:** `66.0/100; G6 PASS; G7 OTVORENÁ.`

Šesť po sebe idúcich dôkazových balíkov G7 je uzavretých po `1.0` bode.
Neznamená to, že prešla K4.3b ani celá G7. Znamená to, že aktuálny stav už
nezamlčuje prácu medzi 60 a 70. Detailný zmrazený ledger je v
`Audit/A2_DECIMAL_GATE_DEPTH_SCORING_AND_K4_RECALCULATION.md`.

## Obmedzenie starších formulácií

- Staré vety „skóre zostáva 60, kým neprejde celá G7“ odteraz znamenajú iba
  `posledná úplná brána zostáva G6`; nezakazujú jemnú hĺbku 60.1–69.9.
- Staré vety „podbrána sama nezvyšuje skóre“ naďalej platia pre udelenie
  celej kanonickej brány. Jemný checkpoint iba zobrazuje auditovanú cestu k
  nej.
- Zákaz priemerného alebo čiastočného fyzikálneho PASS zostáva v platnosti.
  AR43 zavádza evidenciu hĺbky, nie hlasovanie testov ani priemer výsledkov.

