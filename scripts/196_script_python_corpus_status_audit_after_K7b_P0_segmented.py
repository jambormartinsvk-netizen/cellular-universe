#!/usr/bin/env python
"""Corpus-audit successor after segmented K7b P0 evidence and aggregator 195."""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "188_script_python_corpus_status_and_known_error_audit.py"
)
source_text = SOURCE.read_text(encoding="utf-8")

replacements = (
    ("EXPECTED_CORPUS_EXCLUDING_SELF = 192", "EXPECTED_CORPUS_EXCLUDING_SELF = 200"),
    (
        '"corpus_count_excluding_auditor_is_192"',
        '"corpus_count_excluding_auditor_is_200"',
    ),
    (
        '"test": "bounded non-executing Python corpus status and known-error audit"',
        '"test": "bounded corpus status audit after segmented K7b P0 evidence"',
    ),
)
for old, new in replacements:
    if source_text.count(old) != 1:
        raise RuntimeError(f"script 188 segmented-P0 marker count changed: {old!r}")
    source_text = source_text.replace(old, new, 1)

marker = "\n\nFAIL_OPEN = re.compile"
insertion = '''

QUARANTINE["188_script_python_corpus_status_and_known_error_audit.py"] = item(
    "SUPERSEDED", "immutable 192-target snapshot", "196_script_python_corpus_status_audit_after_K7b_P0_segmented.py"
)
QUARANTINE["189_script_A2_K4_C7_7c_K7b3b2_fail_closed_physical_mu_gate.py"] = item(
    "DO_NOT_RUN_TECHNICAL", "PF-012: parser marker patched one wrapper layer too early", "192_script_A2_K4_C7_7c_K7b3b2a_fail_closed_physical_mu_gate.py"
)
QUARANTINE["190_script_A2_K4_C7_7c_K7b_P0_fail_closed_regression_gate.py"] = item(
    "DO_NOT_RUN_TECHNICAL", "depends on technically dead script 189", "195_script_A2_K4_C7_7c_K7b_P0_segmented_offline_aggregate.py"
)
QUARANTINE["191_script_python_corpus_status_audit_after_K7b_P0.py"] = item(
    "SUPERSEDED", "intermediate 195-target snapshot", "196_script_python_corpus_status_audit_after_K7b_P0_segmented.py"
)
QUARANTINE["193_script_A2_K4_C7_7c_K7b_P0a_PF012_corrected_regression_gate.py"] = item(
    "SUPERSEDED", "monolithic aggregate hit its preregistered internal timeout", "195_script_A2_K4_C7_7c_K7b_P0_segmented_offline_aggregate.py"
)
QUARANTINE["194_script_python_corpus_status_audit_after_PF012.py"] = item(
    "SUPERSEDED", "intermediate 198-target snapshot", "196_script_python_corpus_status_audit_after_K7b_P0_segmented.py"
)

FAIL_OPEN = re.compile'''
if source_text.count(marker) != 1:
    raise RuntimeError("script 188 segmented-P0 quarantine marker is not unique")
source_text = source_text.replace(marker, insertion, 1)

code = compile(source_text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})

