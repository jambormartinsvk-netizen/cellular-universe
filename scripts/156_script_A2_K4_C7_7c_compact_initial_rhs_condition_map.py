#!/usr/bin/env python
"""Compact immutable output wrapper for condition-map script 155."""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "155_script_A2_K4_C7_7c_initial_rhs_condition_map.py"
)
text = SOURCE.read_text(encoding="utf-8")

old = """    output = {
        \"test\": \"A2-K4 C7.7c initial RHS cancellation-condition map\",
"""
new = """    compact_results = {}
    compact_fields = (
        \"fsum\", \"sum_abs_terms\", \"cancellation_condition\",
        \"standard_forward_roundoff_bound\", \"signal_to_roundoff_bound\",
    )
    for compact_mode, compact_mode_results in results.items():
        compact_results[compact_mode] = {}
        for compact_surface, compact_surface_result in compact_mode_results.items():
            compact_results[compact_mode][compact_surface] = {
                \"x\": compact_surface_result[\"x\"],
                \"density_condition\": {
                    field: compact_surface_result[\"density_condition\"][field]
                    for field in compact_fields
                },
                \"rhs_conditions\": {
                    name: {field: condition[field] for field in compact_fields}
                    for name, condition in compact_surface_result[\"rhs_conditions\"].items()
                },
            }

    output = {
        \"test\": \"A2-K4 C7.7c compact initial RHS cancellation-condition map\",
"""
if text.count(old) != 1:
    raise RuntimeError("script 155 compact output insertion point is not unique")
text = text.replace(old, new, 1)

old_results = '        "results": results,\n'
new_results = '        "results": compact_results,\n'
if text.count(old_results) != 1:
    raise RuntimeError("script 155 results replacement point is not unique")
text = text.replace(old_results, new_results, 1)

code = compile(text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
