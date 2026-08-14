#!/usr/bin/env python3
"""PreToolUse na Write: blokuje vytvaranie novych vnorenych podkolaji v A2,
kym je stanica A0 nerozhodnuta. Exit 2 = tvrdy blok.

Precedens: D2SW0...D2SW16, 17 urovni vnorenia, pohyb fyzikalnej hlbky nula.
"""
import json, os, re, sys

try:
    ev = json.load(sys.stdin)
except Exception:
    sys.exit(0)

path = (ev.get("tool_input") or {}).get("file_path") or ""
p = path.replace("\\", "/")

if re.search(r"/A2/.*/(SUBTRACKS|D2SW|B6b)", p, re.I) and not os.path.exists(p):
    sys.stderr.write(
        f"BLOKOVANE: {os.path.basename(p)}\n"
        "Vytvaranie novej vnorenej podkolaje v A2 je zakazane, kym nie je\n"
        "rozhodnuta stanica A0 (AGENTS.md §3.3, tracks/A0/00_STATION.md).\n\n"
        "Precedens: D2SW0..D2SW16 = 17 urovni vnorenia, 222 taskov,\n"
        "pohyb fyzikalnej hlbky NULA. Delenie problemu nie je pokrok.\n\n"
        "Zakonny dalsi krok podla AGENTS.md §4.1 (HRUBY_KANDIDAT_FIRST):\n"
        "postav najhrubsieho explicitneho kandidata, nie presnejsi opis toho,\n"
        "co chyba.\n")
    sys.exit(2)
sys.exit(0)
