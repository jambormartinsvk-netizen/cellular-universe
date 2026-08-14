# KMPC-100 — KMPC-099 publication receipt: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `8/10`

## Dôvod

KMPC-099 standalone diagnostika aj exclusive zápis prešli. Immutable raw
existuje so SHA
`93780C85488F17831562238D61FF2ADA70182163B488687BAB49BA9A6E96ECD9`.
Proces vrátil nonzero až po zápise, pretože terminálny summary stabilného
harnessu očakával legacy pole `atom_id`, ktoré minimalistický diagnostický
payload nemal.

KMPC-100 nesmie opakovať matrix ani fyzikálny výpočet. Je to iba read-only
receipt už publikovaného raw.

## Povinné read-only kontroly

Receipt musí fail-closed overiť:

- presný SHA a meno raw KMPC-099;
- `COMPLETED_DIAGNOSTIC_ONLY`, `DIAGNOSTIC_ONLY` a passed diagnostic contract;
- úplný source-hash ledger V7;
- presný REVIEW kandidát;
- native/frozen/expected rank `98/98/98`;
- nulový autoritatívny HP-M1 solve a `pass_c2_atom_candidate=false`;
- že receipt nevykonal žiadny nový matrix ani fyzikálny výpočet.

Výstup smie pridať legacy summary polia `atom_id`, `M1.pass`, core/common/tail
a background pass iba s explicitným stavom `NOT_EVALUATED_RECEIPT_ONLY` a
hodnotou false. Tieto polia nie sú fyzikálny výsledok.

## Interpretácia

Ak receipt prejde, KMPC-099 raw sa stáva čisto publikovaným diagnostickým
dôkazom a technický counter sa po internom audite resetuje na `0/10`.
Autoritatívne C2 skóre, K4 hĺbka a všetky verdikty ostávajú nezmenené.

## Zmrazená implementácia pred prvým Python behom

- V8 receipt modul:
  `28B4950759B494228AFF74A2078CD5D2A13C2D66051B02CD5C7845585702DB59`;
- runner 344:
  `C164D6909B2CF090CF807103BB80E8822FBBBA7F41A76349F0506A4DBE5EA1AA`;
- atomický/high-precision harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`;
- statická kontrola: `37/37` source a `13/13` prerequisite hashov sedelo;
  všetkých `53` dlhých hash výskytov malo presne 64 hex znakov.

Od tohto bodu sú V8 a runner 344 immutable.
