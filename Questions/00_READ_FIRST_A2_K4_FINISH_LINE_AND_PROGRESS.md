# READ FIRST — A2-K4 finish line a viditeľný pokrok

Dátum: 2026-07-15

## Aktuálne tri čísla

- jemná hĺbka: `66.5/100`;
- strict support C7-W1: `40/100`;
- pracovný progress WBS-1: **`48/100`**.

Hĺbka nie je percento dokončenia. WBS-1 zobrazuje aj úspešnú krokovú časť
G5, ale nie je vedecký score ani pravdepodobnosť pravdy.

## Zostávajúca finish line

Šesť balíkov: dokončenie G5, potom G4, G6, G7, G8 a G9. Dokončenie znamená
buď úplný PASS, alebo reprodukovateľný fyzikálny STOP s dôkazmi.

Realistický odhad: 25–40 pracovných dní, približne 5–8 týždňov. G8 a G9 sú
časovo najťažšie. Platný no-go môže koľaj uzavrieť skôr.

## Ochrana pred nekonečným vetvením

- najviac dve technické opravy na balík;
- Q99 je strop aktuálnej A2-K4 bez novej fyzikálnej vetvy;
- očakávaný posledný flat script je 225–232, hard stop 240;
- po skripte 212 sa používajú zdieľané verziované runners a konfigurácie,
  nie nový Python súbor pre každý parameter;
- technická chyba patrí do error ledgeru, nie do nového Q alebo P-suffixu.

Autoritatívne dokumenty:

- `Audit/A2_K4_COMPLETION_DISTANCE_WORK_ESTIMATE_AND_ANTI_PROLIFERATION_AUDIT_2026-07-15.md`;
- `Questions/A2_K4_BOUNDED_COMPLETION_PLAN_AND_NUMBERING_CAP_2026-07-15.md`;
- `tracks/A1/A1K1/A2/A2K4/00_PROGRESS.md`.
