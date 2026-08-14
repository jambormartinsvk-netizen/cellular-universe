#!/usr/bin/env python3
"""SessionStart hook: stav sa overi PRED prvou pracou, nie po nej.
Vystup na stdout sa vlozi Claudovi do kontextu."""
import json, os, subprocess, sys

root = os.environ.get("CLAUDE_PROJECT_DIR", ".")
lint = os.path.join(root, "scripts", "check_state.py")
state = os.path.join(root, "tracks", "00_STATE.json")

if not os.path.exists(lint):
    print("check_state.py nenajdeny - stav neovereny"); sys.exit(0)

r = subprocess.run([sys.executable, lint, state], capture_output=True, text=True)
print(r.stdout)

if r.returncode == 1:
    print("""
=========================================================================
STAV JE PORUSENY (BLOCK).

Podla tracks/00_POST_AUDIT_PLAN_2026-08-14_SK.md ma toto sedenie PRAVE DVE
zakonne moznosti:
  1. opravit uvedene porusenia
  2. pracovat na stanici A0 (tracks/A0/00_STATION.md)

Ziadna ina praca sa nezacina. Zjemnenie specifikacie P5.3 blockeru je
zakazane (AGENTS.md §4.1). Na konci sedenia spusti /session-close.
=========================================================================""")
