# P3a-B skript 204 — PF-030 parser-order failure

Dátum: 2026-07-15  
Stav: **DO_NOT_RUN_TECHNICAL**  
Fyzika vykonaná: **nie**

Skript 204 prešiel `py_compile`, ale jeho `--help` neobsahoval povinný
`--output`. Audit zdroja ukázal, že argument bol patchom vložený až za
`args = parser.parse_args()`. Beh s predregistrovaným `--output` by preto
skončil parserovou chybou ešte pred seed source a evolúciou.

Nevznikol raw JSON ani grid checkpoint. Skript sa neopravuje pod rovnakým
číslom; zostáva zachovaný s markerom `DO_NOT_RUN_TECHNICAL`. Nový nástupca
musí vzniknúť z čistého skriptu 197, registrovať všetky argumenty pred
`parse_args()` a help test musí explicitne vyžadovať `--output`.

P3a-A PASS, predregistrácia P3a-B a hĺbka A2-K4 `66.5/100` sa nemenia.
