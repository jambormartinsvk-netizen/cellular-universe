# K11-CS2 full v002 — pokus 5/10 source-AST výsledok a audit

**Dátum:** 2026-07-16  
**Autoritatívny verdict:** `PASS_ARCH_A_SOURCE_AST_EXACT_SET_AND_REGISTERED_TRUNCATION_ONLY`  
**Dobový technický zápis:** `5/10 použitých poradových miest`  
**Aktuálna interpretácia:** `historical_packages_total=5`,
`consecutive_technical_failures=0/10`  
**Fyzikálna hĺbka:** bez zmeny, `10/100 = G1`  
**Release trigger:** žiadny

## 1. Výsledok

```text
checks = 55
failed = 0
state counts L=4/6/8 = 25/33/41
internal runtime = 0.032 s
external wall = približne 1.5 s
exit = 0
```

Prešli pinned CAMB source hash, AST rovnice `J_eq/G_eq/E_eq`, ich `ell=2`
zdroje a substitúcie, `get_hierarchies range(2,lmax)`, exact ordered state
contract, negatívne fixtures, hardcoded racionálne koeficienty a metadata
numerického top rezu.

## 2. Hashy

```text
JSON = 2180093D79D0D449CAA056507819FB7EB349013958CD808192F572728892EE58
runner 270 = B84B3E85710B1B14CCE12EFCA3A8467BBAD645E54460F821C3C6D60888162D34
lazy package init = C3C739B916745581B8AEA8C698DFA82FFA441A8E9FF7F57FDAEDE32DAEF39391
source-AST base = 58385E957E379AA1BFFB6F97453F58DD33682CAB05FFF097C9D8D7DC616B5203
contract = 30610E17EA247B035962439EBF40467F33ACDBAB26298E3CBD47EC57DA48B42E
CAMB symbolic = F380B56A15F678F6D8DBA8981BBE5A4E57377050945ADE91C6CD4B9262C7A608
```

Recorded runner a package-init hashes sa zhodujú s následným nezávislým
PowerShell hash auditom.

## 3. Čo PASS znamená

- state/RHS contract už nepridáva neexistujúce `E_0,E_1`;
- presné vnútorné CAMB koeficienty sú pripnuté k auditovanému zdroju;
- horný rez je viditeľne numerický a povinne vyžaduje konvergenciu;
- ľahký audit už neplatí skrytý CAMB/SymPy import overhead.

## 4. Čo PASS neznamená

Nie je to full DAE, TCA, HyRec/opacity, regular-mode basis, constraint
propagácia, evolučná `lmax` konvergencia ani CMB/S8 dôkaz. Univerzálna exact
finite-`L` closure zostáva mŕtva ako K11-TC-A0. K11 preto nedostáva G2 ani
body.

## 5. Nasledujúca brána

Pred ďalším Python balíkom treba samostatne predregistrovať full v002
thermal/TCA/DAE implementáciu. Musí použiť tento contract, exact-A1
background, source-pinned opacity/thermal adaptér, TCA/full mapu, nezávislé
Einstein/Bianchi holdouty a neskôr `lmax` aj closure-family sweep. Ďalšie
historické poradové číslo v tej istej ARCH-A je 6; aktívny counter je pred
ním `0/10`.
