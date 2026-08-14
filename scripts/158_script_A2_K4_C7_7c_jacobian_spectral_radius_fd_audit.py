#!/usr/bin/env python
"""Immutable extension of 157 adding FD spectral-radius error."""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "157_script_A2_K4_C7_7c_jacobian_scaling_and_fd_audit.py"
)
source_text = SOURCE.read_text(encoding="utf-8")
MARKER = "'''\n\nextended = source_text.replace"
if source_text.count(MARKER) != 1:
    raise RuntimeError("script 157 spectral-radius extension marker is not unique")

addition = r'''    (
        "fd_spectral_radius_output",
        '                    "spectral_relative_error": float(\n',
        '                    "spectral_radius": float(\n'
        '                        np.max(np.abs(audited_eigenvalues))\n'
        '                    ),\n'
        '                    "spectral_radius_relative_error": float(\n'
        '                        abs(\n'
        '                            np.max(np.abs(audited_eigenvalues))\n'
        '                            -np.max(np.abs(envelope_eigenvalues))\n'
        '                        )/max(\n'
        '                            1.0, float(np.max(np.abs(envelope_eigenvalues)))\n'
        '                        )\n'
        '                    ),\n'
        '                    "spectral_relative_error": float(\n',
    ),
    (
        "spectral_radius_test_identity",
        '"test": "A2-K4 C7.7c Jacobian scaling and FD audit"',
        '"test": "A2-K4 C7.7c Jacobian scaling, FD, and spectral-radius audit"',
    ),
    (
        "spectral_radius_execution_verdict",
        '"CAPTURED_C7_7C_JACOBIAN_SCALING_FD_AUDIT"',
        '"CAPTURED_C7_7C_JACOBIAN_SPECTRAL_RADIUS_FD_AUDIT"',
    ),
'''

extended = source_text.replace(
    MARKER, addition + "'''\n\nextended = source_text.replace", 1
)
code = compile(extended, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
