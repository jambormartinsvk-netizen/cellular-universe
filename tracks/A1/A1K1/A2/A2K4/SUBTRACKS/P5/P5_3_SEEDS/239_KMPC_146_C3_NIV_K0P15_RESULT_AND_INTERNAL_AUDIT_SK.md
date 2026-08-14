# KMPC-146 — C3 NIV/k=0.15 výsledok a interný audit

**Dátum:** 2026-07-22  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → NIV/k=0.15`  
**Verdikt auditu:** `AUDIT_LOGIC_FALSE_NEGATIVE / PF-129`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)

## 1. Audítorská autorita

Predregistrácia 238 bola uzavretá pred prvým Python procesom. Compile
`4/4`, help a smoke prešli; smoke nevykonal fyziku. Presne jeden official
beh vytvoril immutable raw
`RUN_KMPC_146_P5_3G7_C3_NIV_K0p15_ZERO_VARIANT_PAIR_MULTI_RANK_REFINEMENT.json`
so SHA-256
`BA595163C3A2E1D464558B035FE478A16E36678FA215C46B124E4062DC77227E`.
Parent runtime bol `2.906 s`, všetky štyri workery skončili za
`1.579–1.985 s`.

## 2. Vecný výsledok korekcií

| shard | rank | baseline driver | refined driver | refined abs fallback | selection |
|---|---:|---:|---:|---:|---|
| gamma0 / accepted | 104 | `1.0986663411e-10` | `1.6265720141e-16` | `2.4651903288e-31` | PASS |
| gamma0 / audit | 130 | `9.9000884730e-8` | `1.6624145908e-16` | `7.8886090522e-31` | PASS |
| af0 / accepted | 104 | `1.4819148859e-10` | `1.7247095144e-16` | `2.9582283946e-31` | PASS |
| af0 / audit | 130 | `1.4168295759e-7` | `2.1394287413e-16` | `4.6838616247e-31` | PASS |

Každý shard má target rank exact, tri kroky,
`EXACT_SAME_MATRIX_AND_CONSTANT`, úspešnú selection rule, exact predecessor
baseline a obnoveného solver ownera. `gamma0` aj `af0` majú
`logical_atom_pass=true`; core, common, tail, background, null-limit aj
bridge brány prešli. Všetky shared worker parity kontroly sú true.

## 3. Jediná false množina a koreňová príčina

`same_matrix_multi_rank_audit` obsahuje presne štyri false polia:

```text
gamma0/accepted/f0_exact_predecessor_parity
gamma0/audit/f0_exact_predecessor_parity
af0/accepted/f0_exact_predecessor_parity
af0/audit/f0_exact_predecessor_parity
```

Živý worker payload držal mocninové kľúče F0 state ako Python `int`, kým
hashovo načítaný predecessor ich po JSON serializácii držal ako `str`.
Parent porovnal objekty pred spoločnou publish projekciou. Po serializácii
KMPC-146 rawu sú všetky štyri F0 stromy exact zhodné s predecessorom:

| shard | JSON-projected SHA-256 current = predecessor |
|---|---|
| gamma0 / accepted | `F82A2448D3AF70E917618DAE1EBF1FDA6802287FDB30109DF883E7052D2493A6` |
| gamma0 / audit | `94053B35E062D4B0B37C58C7B810B86397A4E69A0033AABFCD8B7F3B0F1F4D5D` |
| af0 / accepted | `93A387F6AAD2F29BCCDC7D8E965B87425DB798FE6773167491F7E38A0AD7E47B` |
| af0 / audit | `848CB15A1CF7AAD2E2302AE7B0D27F7CBA525A724DB72ACD3AF438047C897B2B` |

Toto je rovnaká trieda chyby ako PF-112/PF-128: nekanonizovaná hranica
in-memory objekt verzus publikovaný JSON. Nie je to fyzikálna alebo
numerická odchýlka.

## 4. Autoritatívne rozhodnutie

Skriptový REVIEW sa neprijíma ako fyzikálny REVIEW. Raw je úplná evidencia
úspešných korekcií, ale chybná odvodená parent kompozícia zatiaľ nesmie
udeliť nové atómy. Stav preto zostáva NIV `7/9`, globálne C3 `43/45` a K4
`60/100`; C3 aggregate ostáva zakázaný. Active technical counter je do
úspešnej opravy `1/10`.

Runner 390 a immutable raw sa nesmú opakovať. Povolený je iba nový
predregistrovaný read-only successor, ktorý:

1. hashovo načíta KMPC-146 raw a KMPC-131 predecessor;
2. vyžaduje presnú štvorku false parity polí a všetky ostatné refinement aj
   fyzikálne brány true;
3. overí exact JSON-semantic F0 parity pre všetky štyri shardy;
4. zmení iba štyri parity booleany a odvodené refinement/pair/candidate
   polia, pričom protected snapshot pred/po ostane identický;
5. deklaruje a overí `0` worker, solver a fyzikálnych volaní.

Až interný audit read-only výsledku môže udeliť NIV `9/9` a C3 `45/45`.
Potom sa pred ďalším výpočtom vytvorí externý auditný balík tejto uzávierky.
