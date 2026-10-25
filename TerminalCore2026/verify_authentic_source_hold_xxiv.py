"""Fail-closed verification of unresolved source-to-unforced theorem gate."""
import json
from pathlib import Path
p=Path(__file__).with_name("FULL_UNFORCED_SOURCE_CERTIFICATE_REQUIRED_20261022.json")
d=json.loads(p.read_text())
missing=[]
for name,val in [
 ("source profile",d["source_identity"]["profile_sha256"]),
 ("A.11 support",d["stage_intervals"]["A11_both_supports_and_gap"]),
 ("exact unforced PDE",d["analytic_lean_gates"]["physical_coordinate_zero_force_residual"]),
 ("end-to-end Lean",d["analytic_lean_gates"]["full_Lean_kernel_declarations_and_build"])
]:
    if val is None: missing.append(name)
assert missing and d["status"]=="FAIL_CLOSED_MISSING_SOURCE_DATA"
print("EXPECTED HOLD, missing:",", ".join(missing))
print("This is a verifier of honest release status, not a proof of the theorem.")
