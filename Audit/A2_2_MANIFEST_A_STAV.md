# A2.2 — reprodukčný manifest K3/K4

**Dátum:** 2026-07-13  
**A2-K3:** `MŔTVA — ARCHIVOVANÁ` (M-010)  
**A2-K4:** `MŔTVA — ARCHIVOVANÁ` (M-011)  
**Nasleduje:** A2-K5

## 1. Rozhodovacie výsledky

### K3

```text
lambda/delta=6.530256856769699
H0 Delta t=0.9351169230555114
interaction exponent=6.106553698664636
amplification=448.7893835174898
step convergence=9.189536296867442e-9
sign/null checks=10/10 PASS
```

### K4

```text
det M=-r^2/(1+delta r)<0
symbolic checks=12/12 PASS
endpoint checks=5/5 PASS
K4 relative-mode transfer=1.587308465541289
Gamma=0 transfer=1.4693472258019427e-5
interaction gain=108028.1391401522
interaction log gain=11.590147019763728
step convergence=8.680938881923069e-8
k convergence=6.28286457989886e-11
global relative 00 residual=3.0138484197632644e-10
```

## 2. Zachované neúspešné behy

- skript 28: integrácie dokončené, JSON serializácia `numpy.bool_` zlyhala;
- skript 29: serializácia opravená, ale kroková a bodová constraint brána neprešli;
- skript 30: jemný konvergentný nástupca bez zmeny fyzikálnych rovníc alebo kill prahu.

Podrobné dôvody sú v `scripts/ERRATUM_28_29_A2_K4_JSON_SERIALIZATION.md` a `scripts/ERRATUM_29_30_A2_K4_CONVERGENCE_AND_CONSTRAINT.md`.

## 3. Povinné typografické erratum

V hlavnom audite treba výraz `lambda/E delta` v rovnici `u_f,x` čítať ako `lambda/(E delta)`. Skripty používali správny menovateľ od prvého behu. Pozri `Audit/ERRATUM_A2_2_K4_UF_DENOMINATOR.md`.

## 4. SHA-256

| Súbor | SHA-256 |
|---|---|
| `scripts/13_script_A1_K1_cdm_background_audit_exact_zstar.py` | `7FB9E3BF82ABE1A1985E426AA37F00B40329EEA9781B4334B20359A99898BA6E` |
| `scripts/25_script_A2_K3_superhorizon_velocity_instability.py` | `7AECD362FE7106114D737163A70DD9AC059A4158E4465F8023CDB8FEFF6C1C9F` |
| `scripts/26_script_A2_K3_equation_sign_and_null_limit_audit.py` | `F41560EC69C75CF5FB1D60F0F659F0B348BEBE683FBAF1C3A24E54379E39FA7C` |
| `scripts/27_script_A2_K4_equation_sign_null_and_eigenvalue_audit.py` | `7D416EAAFD149D9D046D3372126D7B6126C9D92DC4EE0697E1C8C67FCA6D58AB` |
| `scripts/28_script_A2_K4_full_superhorizon_relative_mode.py` | `E27587AED5DCED17EAE8603E55EE835C27E64B76EC871CB246E1E7F313891227` |
| `scripts/29_script_A2_K4_full_superhorizon_relative_mode_serialized.py` | `C5AAE2D8628E77E8C6C44932A0E8CD2690F6ACE6B22691BD36F4E3E907F1EBBA` |
| `scripts/30_script_A2_K4_full_superhorizon_relative_mode_converged.py` | `1225473EA0302E12682A3DA4CDDF279941CE45AA901772E6F44745225F28DC4A` |
| `scripts/31_script_A2_K4_frame_endpoint_crosscheck.py` | `0C694A6B63AE29AC5B2CD714287BECB154CCE35A362A7E8A07E455298212A323` |
| `scripts/ERRATUM_28_29_A2_K4_JSON_SERIALIZATION.md` | `03F8D31C9A73E76D8206748F9EA977FB0CC89DEC019509529F9D9D2EC5BD1F97` |
| `scripts/ERRATUM_29_30_A2_K4_CONVERGENCE_AND_CONSTRAINT.md` | `457EA85E05522DC71AE0E905BAAEA8AC3C5BDAB0A715D2795224D48C36CE18EE` |
| `scripts/README_AUDIT_SCRIPTS_25-30.md` | `1C5A44467CBFFB85034930359D875D5396AB695ED9AF77AD78E1A0BF4DF74F3C` |
| `Audit/A2_2_odvodenie_a_test_A2_K3_A2_K4.md` | `399FF711099803A7BC5CDEE5336829B06635344CD510F6FC5FE8DA6401AE3F70` |
| `Audit/ERRATUM_A2_2_K4_UF_DENOMINATOR.md` | `4B3885F04C6ADA7F2D177645A3472E954F70293E1007A6AC1F0CCE169C8E2BA1` |
| `Audit/A2_K3_MRTVA_superhorizontova_rychlostna_nestabilita.md` | `AB187A7D7B73BFED5DD186698FA2420C1465A02F38598940E99073B7D75FB386` |
| `Audit/A2_K4_MRTVA_total_dark_sector_velocity_instability.md` | `DFF3B21D150B1855AC753C5E783667D13F08999F1E1CF426632B969FBEA9EB3B` |
| `Audit/ADDENDUM_REGISTER_MRTVYCH_KOLAJI_A2_M010_M011.md` | `DC47F436D080860D5B040895E5001A44AA427CEBF5068D55259AA49689397FDF` |
| `Audit/00_READ_FIRST_A2_AFTER_K4_WITH_ERRATUM.md` | `6D8A9280CCA314AF1D238709E4146D836EF5266045EDC0EDDB94961F65B45A18` |
| `Questions/A2_2_STAV_PO_K3_K4_A_AKCNY_PLAN.md` | `B3AAECA87F61F900B8155E52ADB551C0B5ADA2E01F95E237A3A13828A0E0E487` |
| `theory/SK/05f_Methodology_Rules_and_Question_Register_A2_2_SK.md` | `A2CB5311314BD7CDC34C2DF6CB7AA984B42209843C33BCF37B9501AFC4830537` |
| `theory/EN/05f_Methodology_Rules_and_Question_Register_A2_2_EN.md` | `DB68091DAAD8318857DF671D1695E38245165FBA6B9200EDF047E9A3970B36EB` |

Hash tohto manifestu a dodatku skriptu 31 sa má dopočítať v nadradenom release manifeste, aby nevznikla sebareferencia.

## 5. Aktuálny stav Q20

Fenomenologické fluidné smery K1–K4 sú archivované ako mŕtve. A2-K5 sa nesmie vytvoriť ďalším ľubovoľným smerom `Q^mu`; musí odvodiť interakciu, kinetiku a povolené počiatočné módy z lokálnej mikrofyziky.

