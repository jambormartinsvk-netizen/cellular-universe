#!/usr/bin/env python
"""Versioned successor of checker 188 after adding K7b P0 scripts 189/190.

Script 188 remains the immutable 192-target snapshot.  This wrapper changes
only the expected corpus count/check name, the audit identity, and registers
188 as superseded for routine use.  Target scripts are still never executed.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "188_script_python_corpus_status_and_known_error_audit.py"
)
source_text = SOURCE.read_text(encoding="utf-8")

replacements = (
    ("EXPECTED_CORPUS_EXCLUDING_SELF = 192", "EXPECTED_CORPUS_EXCLUDING_SELF = 195"),
    (
        '"corpus_count_excluding_auditor_is_192"',
        '"corpus_count_excluding_auditor_is_195"',
    ),
    (
        '"test": "bounded non-executing Python corpus status and known-error audit"',
        '"test": "bounded corpus status audit after K7b P0 scripts 189/190"',
    ),
)
for old, new in replacements:
    if source_text.count(old) != 1:
        raise RuntimeError(f"script 188 successor marker count changed: {old!r}")
    source_text = source_text.replace(old, new, 1)

marker = "\n\nFAIL_OPEN = re.compile"
insertion = '''

QUARANTINE["188_script_python_corpus_status_and_known_error_audit.py"] = item(
    "SUPERSEDED",
    "immutable corpus snapshot fixed at 192 targets before scripts 189/190",
    "191_script_python_corpus_status_audit_after_K7b_P0.py",
)

FAIL_OPEN = re.compile'''
if source_text.count(marker) != 1:
    raise RuntimeError("script 188 quarantine-extension marker is not unique")
source_text = source_text.replace(marker, insertion, 1)

code = compile(source_text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})

