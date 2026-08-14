# KMPC-131/146/147 — C3 NIV mode-closure interný audit

**Dátum:** 2026-07-22  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → NIV`  
**Verdikt:** `PASS_C3_NIV_MODE_9_OF_9`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)

## 1. Rozsah a autorita

Tento audit nemení rovnice ani nepočíta nový fyzikálny výsledok. Spája:

- interné audity 233 a 235 pre NIV `k=.005` a `.05`;
- KMPC-131 NIV/.15 predecessor raw SHA
  `88DFD9AAD5F378CBD9F7E7D1AA9738C40855CA0EC9FD191A77C682D643A0CFE6`;
- KMPC-146 four-shard multi-rank raw SHA
  `BA595163C3A2E1D464558B035FE478A16E36678FA215C46B124E4062DC77227E`;
- audit 239, ktorý izoloval PF-129 bez fyzikálnej odchýlky;
- KMPC-147 read-only correction raw SHA
  `2780A8D6527C892E1EF665B59D514DD94A95495D536C56DFE3332A113956B16E`.

Externý audit EA-037 T2 nezávisle reprodukoval KMPC-131 NIV/.15 REVIEW a
uzavrel jeho runtime/parity auditnú pauzu. KMPC-146/147 sú nová úzka
nástupnícka evidencia a musia dostať nový externý balík.

## 2. Audit KMPC-147

Read-only smoke aj official použili iba štandardný JSON/hash kód. Official
má `workers=0`, `solvers=0`, `physics=0`, runtime `0.016 s` a nevytvoril
failure raw. Všetkých 13 input checks aj následné correction checks sú true.

Štyri F0 parity stromy sú JSON-semanticky exact a všetky štyri refinement
rows po oprave prešli. Interný protected snapshot má identické pred/po SHA
`9F76DD48A83DEC2AB825A0E1B2B0D22B443F5965868BCAAFD46812033E360A0A`.
Nezávislá PowerShell projekcia nad publikovanými rawmi tiež našla exact
zhodu; obe strany mali SHA
`F93FAA594D45265C72374B04167BEDAD9FC95EAEACB6021E8389221F6B329DAC`.
Pôvodný KMPC-146 runtime `2.906 s` ostal zachovaný a nový read-only runtime
je iba v novom auditnom bloku.

## 3. Fyzikálna evidencia NIV/.15

KMPC-146 zachoval exact predecessor baselines a na tej istej matici/RHS
znížil všetky štyri target drivery:

```text
gamma0/accepted rank104: 1.0987e-10 -> 1.6266e-16
gamma0/audit    rank130: 9.9001e-8  -> 1.6624e-16
af0/accepted    rank104: 1.4819e-10 -> 1.7247e-16
af0/audit       rank130: 1.4168e-7  -> 2.1394e-16
```

Pre každý shard prešli tri corrections, selection rule, absolute fallback,
driver a provenance. `gamma0` aj `af0` majú core, holdout, common, tail,
background, null-limit, bridge a logical atom true. PF-129 menila iba
odvodenú typovú parity kompozíciu, nie tieto hodnoty.

## 4. Autoritatívne účtovanie

| jednotka | pred auditom | prírastok | po audite |
|---|---:|---:|---:|
| NIV/.15 | `1/3` | `+2` nulové varianty | `3/3 PASS` |
| NIV mód | `7/9` | `+2` | `9/9 PASS` |
| globálne C3 | `43/45` | `+2` | `45/45 logical PASS` |
| K4 hĺbka | `60/100` | `0` | `60/100` |

Udeľujem `PASS_C3_NIV_K0P15_3_OF_3` a
`PASS_C3_NIV_MODE_9_OF_9`. Globálna logical coverage C3 je `45/45`.
Technický counter sa po úspešnej read-only náprave resetuje na `0/10`;
PF-129 ostáva v historickom ledgeri.

Toto samo nezvyšuje K4 a nespúšťa P5.4, G8, G9, release, Zenodo ani zmenu
prediction table. Globálny C3 aggregate ešte nebol vykonaný. Najbližší krok
je minimálny externý auditný balík pre KMPC-146/147 a tento audit; až po
jeho spracovaní smie vzniknúť samostatne predregistrovaný read-only C3
aggregate.
