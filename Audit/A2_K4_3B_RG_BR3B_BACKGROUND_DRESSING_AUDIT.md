# Audit A2-K4.3b-RG BR3B — fyzikálne doplnenie pozadia

Dátum: 2026-07-14  
Rozsudok koľaje: **ŽIVÁ**  
Kanonická maximálna hĺbka: **60/100 = G6**  
G7: **ROZPRACOVANÁ, NIE PREJDENÁ**

## Aký veľký dopad má aktuálny stav K4

Dopad je veľký pre rozhodovanie o A1-K1, ale zatiaľ nie pre pozorovateľnú úspešnosť modelu.

1. K4 je prvá A2 koľaj, ktorá uzavrela G1–G6 a vstúpila do úplného Einstein–Boltzmann problému. A1-K1 preto zatiaľ nemožno označiť za slepú vetvu.
2. Nový audit odstránil konkrétne riziko smrti: nekompatibilná hodnosť zo skriptu 97 nevznikla porušením Bianchiho identít teórie, ale vložením palivového stressu bez povinného doplnenia pozadia a Eulerových rovníc.
3. Fyzikálne odvodené doplnenie, bez nového fitu, dáva presne nulové Bianchiho rezíduá a správnu hodnosť vo všetkých piatich štandardných počiatočných módoch pre spoločný `h_x` sektor.
4. Audit súčasne zväčšil rozsah práce: NID a NIV obsahujú skoršie kompenzované relatívne radiačné sektory. Tie musia byť vyriešené pred spoločným palivovým sektorom.
5. K4 stále nemá plný fotónový/neutrínový backend, CMB transfery, spektrá ani likelihood. Nemožno preto tvrdiť, že prešla G7 alebo že jej observačná životaschopnosť je vysoká.

Praktický význam: K4 už nie je iba slovná možnosť a prežila najťažšie predbežné konzistenčné brány. Zároveň jeden úspešný koeficientový sektor nemožno zameniť za úspešný CMB model. Skóre ostáva 60/100.

## Audit tvrdenia zo skriptu 97

Skript 97 vložil palivový stress ako izolovaný pravý člen. Matica odozvy mala plnú stĺpcovú hodnosť 7, ale rozšírená matica hodnosť 8. Chýbajúci štandardný metrický člen bol vo všetkých módoch `-delta/2`; ľavé nulové obštrukcie boli `3 delta/2`.

Staršia formulácia „izolovaný palivový zdroj je nekompatibilný“ je správna iba pre zámerne neúplný ansatz. Nesmie sa čítať ako „K4 porušuje Einsteinove constrainty“. Neskorší audit 98–100 ju obmedzil takto: úplný zdroj musí obsahovať aj zmenu radiačných váh, sklonu `Hconf`, metrické krížové členy a Eulerovo nútenie.

## BR3B-2a a BR3B-2b

BR3B-2a odvodila dve presné podmienky kompatibility. Čisto algebraický doplnok `Ctr=Ctl=-3 delta/2` pri `C00=C0i=0` obnoví hodnosť, ale nie je fyzikálnym riešením a nebol tak interpretovaný.

BR3B-2b rozšírila zdroj na

`[Jgc, Jge, Jnc, Jns, Jne, C00, C0i, Ctr, Ctl]`.

V kompaktnom tvare sú dve podmienky

`2(r-1) C00 + Ctr - 3(R_gamma Jgc + R_fs Jnc) + 3 delta/2 = 0`,

`2(r-1) C00 - 6(r+1) C0i + Ctl - 3(R_gamma Jgc + R_fs Jnc) - 12(R_gamma Jge + R_fs Jne) + 3 delta/2 = 0`.

Šmykový zdroj `Jns` nevstupuje priamo do týchto dvoch identít, ale ostáva potrebný na vyriešenie odozvy a hierarchie.

## BR3B-2c — fyzikálny spoločný sektor

Z expanzie

`Omega_f=y~a^(4-3 delta)`,

`Hconf_x/Hconf=-1+(4-3 delta)y/2+O(y^2)`

a zo štandardného `0i` constraintu boli odvodené všetky potrebné členy spoločného sektora. Vloženie do úplného zdrojového vektora dáva dve presné nuly a hodnosť `rank(A)=rank(A|b)=7` pre AD, CDI, BI, NID a NIV.

Rozsudok: **PASS pre spoločný `h_x` sektor**, nie PASS pre celé G7.

## BR3B-2d — skoršie sektory NID/NIV

Presne sa potvrdilo:

- NID: `R_gamma delta_gamma + R_fs delta_fs=0` a `R_gamma U_gamma + R_fs U_fs=0` vo vedúcom kompenzovanom sektore;
- NIV: rovnaké dve vážené kompenzácie sú presne nulové;
- napriek nulovému celkovému vedúcemu stressu sú jednotlivé relatívne módy nenulové a pozadie ich núti pri skorších necelých mocninách;
- neutrínový šmyk a vyššie multipóly rozhodnú, či kompenzácia ostane metrickým nulovým módom alebo začne spätne pôsobiť.

Rozsudok: **PASS poradia a kompenzácie; fyzika hierarchie otvorená**.

## Technická chyba skriptu 101

Skript 101 skončil `ERROR_UNCLOSED` pre JSON serializáciu `SymPy BooleanTrue`. Nešlo o timeout ani fyzikálny fail. Skript ostáva zachovaný. Skript 102 je explicitne označený opravený klon; mení iba konverziu logických hodnôt a dáva PASS všetkých siedmich kontrol.

## Čo ešte K4 potrebuje pred 70/100

1. BR3B-2e: šmyk a minimálna regulárna neutrínová hierarchia `l>=3` pre NID/NIV v správnom poradí mocnín.
2. Vyriešiť indukované koeficienty všetkých sektorov, nie iba spoločný `h_x` sektor.
3. Overiť všetky štyri Einsteinove rezíduá v najmenej dvoch skorých hĺbkach a pri nezávislej zmene presnosti.
4. Implementovať úplnú fotónovú a neutrínovú Boltzmannovu hierarchiu v backende.
5. Porovnať fyzikálne transfery s nulovým limitom a nezávislou referenčnou implementáciou.

Až spoločný úspech týchto bodov uzavrie G7 a zvýši jednotné skóre na 70/100.

