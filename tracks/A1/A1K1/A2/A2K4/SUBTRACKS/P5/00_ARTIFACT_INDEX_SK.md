# P5 — index artefaktov a bezpečný poriadok

**Účel:** navigovať P5 bez presúvania historických skriptov a immutable
výsledkov. Tento index nie je nový dôkaz ani náhrada kontraktu.

## Autoritatívny stav

Čítaj najprv `00_WORK_PLAN.md`. P5 je v čiastočnom seedovom review; G8 a
P5.4 sú blokované. Aktuálne artefakty sú rozdelené podľa brány, nie podľa
poradia vzniku súborov.

| Brána | Dokumentácia | Runner / shared kód | Autoritatívny výsledok | Stav |
|---|---|---|---|---|
| P5.1 | `Independent_Audits/K_MPC_0_05/15–16` | `236`, `baseScripts/p5_general_synchronous/coefficient_identities.py` | `RUN_KMPC_003_P5_1_GENERAL_SYNCHRONOUS_STATIC_LEDGER.json` | PASS, structural |
| P5.2 | `P5_2_CONSTRAINT_LEDGER/00–01` | `241`, `constraint_identities.py` | `RUN_KMPC_004_P5_2_FULL_CONSTRAINT_LEDGER_RERUN1.json` | PASS, structural |
| P5.3a | `P5_3_SEEDS/00–01` | `242` | `RUN_KMPC_005_P5_3A_SEED_PROVENANCE_AUDIT.json` | PASS mapy; seed regularita otvorená |
| P5.3b | `P5_3_SEEDS/02–03` | `243`, `adiabatic_seed_identities.py` | `RUN_KMPC_006_P5_3B_ADIABATIC_LEADING_SEED_RERUN1.json` | PASS, iba AD leading |
| P5.3c | `P5_3_SEEDS/04` | `244` | `RUN_KMPC_007_P5_3C_ADIABATIC_FINITE_STARTS.json` | PASS, iba AD dve plochy |
| P5.3d | `P5_3_SEEDS/05–06` | `245` | `RUN_KMPC_008_P5_3D_STANDARD_MODE_LEADING_SEEDS.json` | PASS, päť štandardných módov |
| P5.3e | `P5_3_SEEDS/07–08` | `246` | `RUN_KMPC_009_P5_3E_INTERNAL_REGULARITY.json` | PASS, interné leading módy |
| P5.3f–g3 | `P5_3_SEEDS/09–21` | `247`, `252–254` | `RUN_KMPC_015...` až `RUN_KMPC_017...` | formula/mapa v deklarovanom rozsahu; nie plný seed |
| P5.3g4 | `P5_3_SEEDS/22` + gauge erratum | `255`, `photon_tca_first_order.py` | `RUN_KMPC_018_P5_3G4_PHOTON_TCA_FIRST_ORDER.json` + `RUN_KMPC_021...` | PASS iba spolu so synchronným gauge bridge |
| P5.3g5 | `P5_3_SEEDS/23` | `256`, `early_opacity_ledger.py` | `RUN_KMPC_019_P5_3G5_EARLY_OPACITY_AND_EINSTEIN_LEDGER.json` | PASS, early-time formula scope |
| P5.3g6 | `P5_3_SEEDS/24` | `260` | `RUN_KMPC_021_P5_3G6_RERUN1_SYNCHRONOUS_PHOTON_GAUGE_BRIDGE.json` | PASS, presná gauge mapa |
| P5.3g7-M1 | `P5_3_SEEDS/26` | bez runnera; primárny BMT → script-84 mapovací audit | žiadny (textový `PASS_MAPY`) | štandardný nulový-limit `h,h'` je zmapovaný |
| P5.3g7-M3 | `P5_3_SEEDS/27–31` + datované M3 audity | KMPC-023/024; oba iba REVIEW | `RUN_KMPC_024...RERUN2.json` | M1/štandard PASS, ale `STOP_M3_RUNNER_CONTRACT`: chýbali dynamické `delta_f,U_f`; bez fyzikálneho verdictu K4 |
| P5.3g7-M3-FULL/R-A B1 | `P5_3_SEEDS/32–36` | 264/KMPC-025 limited; 265/KMPC-026 autoritatívny contract guard | `RUN_KMPC_025...` algebra-only; `RUN_KMPC_026...` contract PASS | PF-063 pressure opravený; PF-064 obmedzil raw 15/15; nezávislý validator 9/9 + 9 negatívnych fixtures PASS; seed solve ešte nebežal |
| P5.3g7 R-A attempts 6–9 | `P5_3_SEEDS/37–47` | `271/KMPC-027` timeout; `272/KMPC-028` J4; `273/KMPC-029` J6/J8; `274/KMPC-030` one-refinement | KMPC-030 SHA `8CB706...3C6F` | historická postupnosť; KMPC-030 technicky dobehol, tail semantics REVIEW |
| P5.3g7 R-A attempt 10 / ARCH-A closure | `P5_3_SEEDS/48–50` | `275/KMPC-031`, no-solve | SHA `C547F818...92FF6` | `PASS_SUPPORT_TRUNCATION_J4_SENTINEL_SCOPE`; historical packages 10, active counter 0/10; celý P5.3 otvorený |
| P5.3g7 S-C0 passport | `P5_3_SEEDS/51–56` | `276/KMPC-032` PF-069; `277/KMPC-033` RERUN1 | failure SHA `51C7B3...1EA03`; result SHA `4CED9D...CFE8C` | `PASS_S_C0_LOWER_MOMENT...ONLY`; S-M, `F_l>=3`, CDI C1 a coverage otvorené |
| P5.3g7 CDI C1 | `P5_3_SEEDS/57–59` | `278/KMPC-034`, base `cdi_c1_coverage.py` | SHA `37FB4453...DCE20` | core/common PASS; `[0,1]` insufficient; vtedajší `[0,3]` remainder open neskôr obmedzil KMPC-035 |
| P5.3g7 CDI support step 2 | `P5_3_SEEDS/60–62` | `279/KMPC-035`, base `cdi_support_ladder.py` | SHA `A9BD519F...E42A01` | scoped core/common PASS; `[0,3]` remainder REVIEW; M1 order-7 provenance blokuje step 3; nie Fourier C2 |
| P5.3g7 M1 order-7 provenance | `P5_3_SEEDS/63–65` | `280/KMPC-036`, base `m1_order7_provenance.py` | SHA `39BB3886...B7B497` | regression/shape/rank/anchor/condition/holdout PASS; tri power7 driver precision REVIEW; support step 3 BLOCKED |
| P5.3g7 CDI order-7 boundary closure | `P5_3_SEEDS/67–74` | `281–283/KMPC-037–039` | SHA `BDF33172...CE016` | dve technické stopy zachované; KMPC-039 same-matrix boundary PASS |
| P5.3g7 CDI support step 3 | `P5_3_SEEDS/75–76` | `284/KMPC-040`, base `cdi_support_step3.py` | SHA `69C78F70...BD219` | CDI `[0,5]` adequate iba `.05/nominal`; bez `[0,9]` |
| P5.3g7 BI C1 + support step 2 | `P5_3_SEEDS/77–80` | `285–286/KMPC-041–042` | SHA `8BB006EF...AE183`, `E5F18DA4...8CA61` | BI `[0,1]` aj `[0,3]` insufficient; core/common stabilné |
| P5.3g7 BI M1 order-7 provenance | `P5_3_SEEDS/81–82` | `287/KMPC-043`, base `bi_m1_order7_provenance.py` | SHA `B02D1D16...61EB0` | historický lower/structural PASS + 5 driver/1 holdout REVIEW; neskôr uzavrel KMPC-044 |
| P5.3g7 BI order-7 boundary closure | `P5_3_SEEDS/83–84` | `288/KMPC-044`, base `bi_m1_order7_numerical_boundary.py` | SHA `C3BD732C...F1C36` | one correction + one 80-dps QR uzavreli 121+18; BI support step 3 odblokovaný pre prereg |
| P5.3g7 BI support step 3 | `P5_3_SEEDS/85–86` | `289/KMPC-045` PF-074; `290/KMPC-046` owner nástupca | failure SHA `FFFF0616...330C01`; result SHA `60EC5A80...15FB1` | BI `[0,5]` adequate iba `.05/nominal`; bez `[0,9]`; NID next |

## Zachované neautoritatívne artefakty

- `RUN_KMPC_004_P5_2_FULL_CONSTRAINT_LEDGER.json` — PF-041 STOP pred
  opravou slip substitúcie; zachovaný, neprepisovať, nepoužiť ako verdict.
- prvý P5.3b beh nevytvoril JSON (PF-042); dôvod je v
  `scripts/00_PYTHON_FORMAL_ERROR_LEDGER.md`.
- `RUN_KMPC_020...` od runnera 257 — PF-054: patcher hľadal marker v zlom
  zdroji. Je technický STOP, nie fyzikálny výsledok; nahrádza ho 260/RUN021.

## Pravidlo poriadku

1. Starý číslovaný runner zostáva v `scripts/`, pretože jeho číslo a hash
   môžu byť citované auditom.
2. Znovupoužiteľná matematika ide iba do `scripts/baseScripts/p5_general_synchronous/`.
3. Nové výsledky P5 idú do `scripts/results/k_mpc_005/`; nikdy sa
   neprepisujú, opravný beh dostáva `RERUNn`.
4. Nová dokumentácia P5 ide do príslušnej brány pod týmto adresárom.
5. Ak bude neskôr nutný presun historického súboru, najprv sa vydá manifest
   stará cesta → nová cesta + SHA-256; pôvodná cesta sa zachová ako
   read-only pointer alebo sa presun nevykoná.

Šablóna pre všetky ďalšie koľaje: `tracks/00_TRACK_CONTRACT_STANDARD_SK.md`.
