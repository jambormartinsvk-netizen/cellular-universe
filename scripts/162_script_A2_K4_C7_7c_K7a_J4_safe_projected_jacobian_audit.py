#!/usr/bin/env python
"""Immutable cancellation-safe revision of projected-Jacobian script 159.

Only ell's float64 evaluation is changed from 2*(q+1) to the algebraically
identical denominator_x/denominator.  The known unreliable double-precision
finite-difference T-prime check is intentionally retained and visible.  This
script is not the final verdict; script 163 combines it with the 80-digit J3
audit.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "159_script_A2_K4_C7_7c_K7a_projected_jacobian_audit.py"
)
source_text = SOURCE.read_text(encoding="utf-8")

legacy_ell = '        \'            ell = 2.0*(projected_bg["q"] + 1.0)\\n\'\n'
safe_ell = (
    '        \'            ell_fuel = z_bg**p\\n\'\n'
    '        \'            ell_transfer = g2*(1.0/(p+1.0)-0.5)\\n\'\n'
    '        \'            ell_denominator = (\\n\'\n'
    '        \'                1.0+mu*z_bg\\n\'\n'
    '        \'                +ell_fuel*(1.0+ell_transfer*z_bg**2)\\n\'\n'
    '        \'            )\\n\'\n'
    '        \'            ell_denominator_x = (\\n\'\n'
    '        \'                mu*z_bg\\n\'\n'
    '        \'                +ell_fuel*(p+(p+2.0)*ell_transfer*z_bg**2)\\n\'\n'
    '        \'            )\\n\'\n'
    '        \'            ell = ell_denominator_x/ell_denominator\\n\'\n'
)
if source_text.count(legacy_ell) != 1:
    raise RuntimeError("script 159 legacy ell marker is not unique")
source_text = source_text.replace(legacy_ell, safe_ell, 1)

legacy_report = '        \'                "ell": float(ell),\\n\'\n'
safe_report = (
    '        \'                "ell": float(ell),\\n\'\n'
    '        \'                "ell_method": "denominator_x/denominator",\\n\'\n'
    '        \'                "legacy_double_Tprime_fd_retained": True,\\n\'\n'
)
if source_text.count(legacy_report) != 1:
    raise RuntimeError("script 159 ell report marker is not unique")
source_text = source_text.replace(legacy_report, safe_report, 1)

source_text = source_text.replace(
    '"test": "A2-K4 C7.7c-K7a projected D-M Jacobian audit"',
    '"test": "A2-K4 C7.7c-K7a-J4 cancellation-safe projected Jacobian audit"',
    1,
)
source_text = source_text.replace(
    '"PASS_C7_7C_K7A_PROJECTED_JACOBIAN"',
    '"CAPTURED_C7_7C_K7A_J4_SAFE_PROJECTED_AUDIT"',
    1,
)

code = compile(source_text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})

