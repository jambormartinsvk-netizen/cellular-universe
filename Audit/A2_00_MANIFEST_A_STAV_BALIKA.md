# A2.0 — manifest, stav a ďalší krok

**Overené:** 2026-07-13  
**Stav kroku:** **A2.0 VYBAVENÁ V DEKLAROVANOM EFEKTÍVNOM ROZSAHU**

## 1. Vedecký výsledok

- A2-K1 má uzavretý kovariantný ledger s `Q^mu=Gamma rho_f u_c^mu`.
- Celková energia a hybnosť sa párovo zachovávajú.
- `Gamma` musí byť konštantný skalár; `lambda=Gamma/H0` je iba parametrizácia.
- Palivová uzávera `c_s,f^2=1`, `pi_f=0` je pracovný efektívny postulát, nie odvodená mikrofyzika.
- A2-K1 **PREŽÍVA 48/100** a postupuje do A2.1.
- A2-K2 s barotropickým `c_s,f^2=w_f=-0.97703` je **MŔTVA — ARCHIVOVANÁ** pre gradientovú nestabilitu.

## 2. Manifest súborov

| Súbor | Veľkosť | SHA-256 |
|---|---:|---|
| `Questions/A2_Q20_problem_perturbacii_a_kolaje.md` | 5 880 B | `5BC4CE8EA40D158F17AAD1CB6903F056FF55406BE637BF4A8C6F7EAA6AE9657B` |
| `Audit/A2_00_kovariantny_ledger_zloziek_a_interakcii.md` | 8 422 B | `2959287A7E94BD5E9861AD208F2075F20BD7869CD312D3863AD9F33991083BF2` |
| `Audit/A2_K2_MRTVA_barotropicke_palivo_gradientova_nestabilita.md` | 2 912 B | `404440224511C2C5BC83AFA40F75588F7190D91981F5B6C6126FF0CBCAFBF9EE` |
| `scripts/21_script_A2_barotropic_fuel_gradient_instability.py` | 2 252 B | `D620AFDB6C0175D5AAC593131ABEDE2036090D8C04B53AEB540B1E5B91A04817` |
| `scripts/README_AUDIT_SCRIPT_21.md` | 1 651 B | `1A80F38045BB5FA4CA70565CF1FD0E326A172D66AA0611840265CBF776D3F1BE` |
| `Audit/ADDENDUM_REGISTER_MRTVYCH_KOLAJI_A2.md` | 995 B | `1CC16E24B46E762E345E3C6CD7038B31F652BBD202DD56CE805209241D3DC922` |
| `theory/SK/05d_Methodology_Rules_and_Question_Register_A2_00_SK.md` | 1 274 B | `9003CF1478E3A9ADC53E5EECD4D8186B1367D057BDC3FD1230AED31C9278CAAA` |
| `theory/EN/05d_Methodology_Rules_and_Question_Register_A2_00_EN.md` | 1 280 B | `C81FE6B7C9F92790B9D13EA41BBD640E438170595EB7F9F03B81B9C8F72B09E0` |

## 3. Technická kontrola

- `python -m py_compile scripts/21_script_A2_barotropic_fuel_gradient_instability.py`: **PASS**, návratový kód 0.
- samotný skript: **PASS diagnostiky**, `VERDICT=MRTVA_BAROTROPIC_CLOSURE`.
- SK register 05d: jeden blok Q20 a jeden blok M-008.
- EN register 05d: jeden blok Q20 a jeden blok M-008.

## 4. Rozsah dokončenia

A2.0 uzatvára iba:

- zoznam efektívnych zložiek;
- kovariantný smer a párovú bilanciu prenosu;
- význam `Gamma`;
- výber aktívnej perturbačnej koľaje;
- smrť barotropickej uzávery.

Neuzatvára lineárne rovnice, superhorizontovú stabilitu, ghost test, CLASS/CAMB ani dáta.

## 5. Autoritatívny ďalší krok

**A2.1:** odvodiť úplné lineárne skalárne perturbácie aktívnej A2-K1 v Newtonovej gauge:

1. perturbovaný `Q^mu` a `delta Q`;
2. kontinuitu a Eulerovu rovnicu paliva;
3. kontinuitu a Eulerovu rovnicu CDM;
4. štandardné baryónové a radiačné väzby;
5. Einsteinove constrainty;
6. nulový limit `Gamma->0`;
7. prvý analytický superhorizontový test.

Pôvodná rastová rovnica V3 sa nesmie použiť ako predpoklad. Môže sa objaviť iba ako odvodený limit, ak ho úplný systém dovolí.

