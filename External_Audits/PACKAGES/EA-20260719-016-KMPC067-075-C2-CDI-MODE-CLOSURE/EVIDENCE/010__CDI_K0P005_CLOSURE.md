# KMPC-067–073 — C2 CDI/k=.005 support closure: výsledok

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Stav:** `PASS_C2_CDI_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY`  

## Výsledok

KMPC-067 ukázal, že pôvodný accepted `[0,5]` nestačí voči auditu `[0,7]`:
M3 `sigma_fs` tail pri `z=.01` bol `1.4946248807986404e-5` oproti prahu
`1e-6`. Predregistrovaný krok `[0,7]→[0,9]` bol po technickom
checkpoint-resume reťazci autoritatívne dokončený v KMPC-073.

KMPC-073 raw:
`RUN_KMPC_073_P5_3G7_C2_CDI_K0p005_SUPPORT_07_09_PHASE_ORDER_SUCCESSOR.json`,
SHA-256 `B7B2B7231E20D90D7EA71F1934B795296B7B0C2772148988C0FCFB2CF96E8498`.

Všetky brány prešli. Pri `z=.01` je F0 tail maximum
`1.8112781292166595e-11` a M3 maximum `4.767720828639666e-9`
(`sigma_fs`), teda s rezervou pod `1e-6`. Common maximum je
`1.3175255748165247e-13` (F0) a `8.299685175722042e-13` (M3), pod `1e-8`.
M1 depth 9 prešiel s driver scaled `1.95500903896024e-13` a holdout scaled
`7.92379361880252e-13`. Production contract aj celý 13-stavový order prešli.

## Technická stopa bez fyzikálneho účinku

- KMPC-068 a 069: timeout/PF-081–082, bez fyzikálneho raw;
- KMPC-070: immutable checkpoint bez verdiktu, SHA
  `AD8CD12F5E6CBABE28C512DFDA6D3867C3E713F5582E152F6289CD78540A7D00`;
- KMPC-071: PF-083, JSON order artefakt, `DO_NOT_USE_PHYSICS`;
- KMPC-072: PF-084 v smoke, audit sa nespustil;
- KMPC-073: jediný autoritatívny výsledkový candidate pre `[0,7]→[0,9]`.

CDI/k=.005 je uzavretý na accepted `[0,7]`. Skóre sa ešte nemení, pretože
CDI mód vyžaduje aj nezávislý k-bod `.15`. Auditný balík sa vytvorí až po
uzavretí celého CDI módu alebo pri skutočnom STOP/blockeri.
