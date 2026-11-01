# H8 joint-cone and variable-frame correction design

## Intent and scope

Preserve the genuine, historically CI-checked Navier--Stokes/H8 lemmas while
repairing the invalid cell-mass-only physical-frame support enclosure and
recording the exact two-coordinate projection of the one-sided seven-ray cone.
The complete unforced PDE theorem is not claimed.

## Alternatives considered

1. Freeze the Cartesian shear test at a representative angle and keep the
   original error allowance. Rejected: the angular test varies even if the
   physical stress frame is constant; this is falsified when frame error is zero.
2. Integrate the frozen-frame support against the density on every cell.
   Mathematically exact, but requires analytic or interval integration data.
3. **Selected:** retain the integral formula in the paper, and allow an
   explicitly certified test-tensor variation error in the rational Python
   enclosure. This also supports rigorous cellwise support interval inputs.

## Deliverables

- Exact hexagon projection and constructive lift for the physical one-sided
  coefficient floor, plus a joint sharp support function.
- An angular-variation regression and a frame/test variation certificate in
  Python; legacy constant-test data must not silently masquerade as a
  variable-angle physical certificate.
- A Lean finite-dimensional necessary theorem and constructive-rational
  witnesses, with any uncompiled declarations explicitly marked pending.
- Integrated manuscript replacement, not an appended research-diary page.
- One source-freeze checklist for missing authentic H8 fields and pressure,
  together with unchanged OPEN global proof gates.

## Hard boundaries

No original common tuple `(E, chi, core, shapers, rho, Rstar, g, p)` is frozen
in the available repository. No claim of source-matched stress existence,
nonlinear exact correction, terminal blow-up, or Clay/Lean completion is made
without genuinely supplied, verified analytic witnesses. Existing project
changes must not be discarded.

## Verification

Run an exact rational regression, the full Python suite with dependencies,
LaTeX compilation and PDF page/layout checks, and the pinned Lean checks or
GitHub Actions receipts. Record failures and queued checks as such.
