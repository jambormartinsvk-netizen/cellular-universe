#!/usr/bin/env python
"""BR3B-2g clone adding the missing higher-multipole regularity gate.

Script 126 is preserved as REVIEW: its equations admitted homogeneous L3/L4
solutions whose unscaled F3/F4 do not vanish in the regular z->0 hierarchy.
This clone extends the checked transformation in script 126 with two sets of
zero conditions:

* standard L3 below m+2 and L4 below m+4;
* fractional L3 below the first feedback layer and fractional L4 throughout
  the present bounded scope (its first physical layer is two powers later).

No physical equation or transfer coefficient is otherwise changed.
"""

from __future__ import annotations

from pathlib import Path


SOURCE = Path(__file__).with_name(
    "126_script_A2_K4_3b_RG_BR3B2g_l3_ash_full_ledger.py"
)
MARKER = "]\n\nfor label, old, new in replacements:\n"
if SOURCE.read_text(encoding="utf-8").count(MARKER) != 1:
    raise RuntimeError("script 126 extension marker is not unique")

extra = r'''    (
        "standard_hierarchy_regularity",
        '            for name in ("h", "eta", "dg", "dn", "db", "dc", "sig", "L3", "L4"):\n'
        '                initial.append((name, 0, 0.0))\n'
        '\n'
        '        def ledger(vector):',
        '            for name in ("h", "eta", "dg", "dn", "db", "dc", "sig", "L3", "L4"):\n'
        '                initial.append((name, 0, 0.0))\n'
        '\n'
        '        hierarchy_m = 2 if mode == "NID" else 1\n'
        '        for exponent in std_exponents:\n'
        '            if 1 <= exponent < hierarchy_m + 2:\n'
        '                initial.append(("L3", exponent, 0.0))\n'
        '            if 1 <= exponent < hierarchy_m + 4:\n'
        '                initial.append(("L4", exponent, 0.0))\n'
        '\n'
        '        def ledger(vector):',
    ),
    (
        "fractional_hierarchy_regularity",
        '        def ledger(vector, split=False):\n'
        '            rows = row_pairs(vector)\n'
        '            if split:\n'
        '                return {row: np.asarray([rows[row][1].get(j, 0.0) for j in frac_exponents], float)\n'
        '                        for row in CORE_ROWS + CARRY_ROWS}\n'
        '            return np.asarray([rows[row][1].get(j, 0.0)\n'
        '                               for row in CORE_ROWS + CARRY_ROWS for j in frac_exponents], float)',
        '        def ledger(vector, split=False):\n'
        '            rows = row_pairs(vector)\n'
        '            if split:\n'
        '                return {row: np.asarray([rows[row][1].get(j, 0.0) for j in frac_exponents], float)\n'
        '                        for row in CORE_ROWS + CARRY_ROWS}\n'
        '            values = [rows[row][1].get(j, 0.0)\n'
        '                      for row in CORE_ROWS + CARRY_ROWS for j in frac_exponents]\n'
        '            first_l3 = 4 if mode == "NID" else 3\n'
        '            first_l4 = first_l3 + 2\n'
        '            values.extend(vector[findex[("L3", j)]]\n'
        '                          for j in frac_exponents if j < first_l3)\n'
        '            values.extend(vector[findex[("L4", j)]]\n'
        '                          for j in frac_exponents if j < first_l4)\n'
        '            return np.asarray(values, float)',
    ),
'''

text = SOURCE.read_text(encoding="utf-8").replace(
    MARKER, extra + "]\n\nfor label, old, new in replacements:\n", 1
)
code = compile(text, str(Path(__file__)), "exec")
exec(code, {"__name__": "__main__", "__file__": str(Path(__file__))})
