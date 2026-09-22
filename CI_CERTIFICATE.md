# CI Verification Certificate

## Certified artifact

`UnforcedClosure.lean`

## Repository checkpoint

Commit:

`7d7f33200e4553afbb80a29ce6435b44511c2f4a`

## GitHub Actions

Workflow:

`Verify Lean closure`

Run:

`#12`

Run ID:

`35779131542`

Result:

**SUCCESS**

## Verified commands

```bash
lake update
lake exe cache get
lake env lean UnforcedClosure.lean
lake build
python verify_unforced_closure.py
python -m pytest -q test_unforced_closure.py
```

All completed successfully.

## Environment

Lean:

`leanprover/lean4:v4.34.0-rc2`

Mathlib:

`85e3a25e006c35636f0e53b0e9296caca2685bc0`

Frozen upstream Navier–Stokes repository commit:

`f9e8bc5b38b6e212696e8a30e3e91517af887bbd`

## Formal scope

The certified Lean artifact establishes the abstract closure results encoded in
`UnforcedClosure.lean`, including:

- exact exponent identities;
- positivity of the required scalar margins;
- fixed-point plus right-inverse implies exact zero residual;
- scalar ball invariance;
- finite Neumann support preservation.

The successful Lean run reports no `sorryAx` dependency for
`fixedPoint_implies_zero_residual`.

This certificate applies to the abstract unforced-closure layer only. It does not
yet certify the PDE-specific hypotheses or the final unforced three-dimensional
Navier–Stokes finite-time blow-up theorem.

## Next formal gate

The next release target is a PDE integration layer connecting the frozen upstream
Navier–Stokes formalization to the certified abstract closure machinery.
