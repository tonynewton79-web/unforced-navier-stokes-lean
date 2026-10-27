# Pressure-compensated cylindrical flux: Lean FTC certificate

**27 October 2026 — continuum radial integral completed in Lean.**

The module `UnforcedPatching/PressureCompensatedFlux.lean` certifies the
radial fundamental-theorem-of-calculus step of the manuscript's
pressure-compensated annular H8 gate, using pinned Lean `4.34.0-rc2` and
Mathlib `85e3a25e006c35636f0e53b0e9296caca2685bc0`.

## Precisely proved statement

For positive radii `0 < a ≤ r`, suppose the axially integrated shear
`S`, axial source marginal `F`, and full axial boundary trace `q` obey

\[
 S'(x)=F(x)-q(x)-\frac{S(x)}{x}
\qquad (a\le x\le r)
\]

in the sense of `HasDerivAt` at every point of the closed interval.
Assume both `x ↦ x F(x)` and `x ↦ x q(x)` are interval-integrable.
Then the compiled declaration `pressureCompensatedFluxIdentity` proves

\[
\frac1r\int_a^r sF(s)\,ds
=S(r)-\frac arS(a)+\frac1r\int_a^r s q(s)\,ds.
\]

The proof separately checks the conservative derivative
`(x*S(x))'=x*(F(x)-q(x))` and applies Mathlib's
`intervalIntegral.integral_eq_sub_of_hasDerivAt`. No assumption silently
eliminates the inner trace or the axial pressure/tensor boundary term.

The additional theorem `pressureCompensatedFluxSupportGate` transports
any certified shear bound `-Bminus ≤ S(r) ≤ Bplus` to the corresponding
**pressure-compensated source-primitive** bound. The exact example
`q(s)=2s`, `a=1`, `r=2` proves its boundary primitive is `7/3`,
not zero. A separate zero-trace theorem applies only when that trace
vanishes identically on the full radial interval.

## Open semantic gates

- Derive the assumed averaged balance from the original Cartesian
  tensor divergence, the angular average and axial integration. This
  requires all cylindrical geometric/connection terms.
- Supply authentic Case 006/H8 `S`, `F`, `q` from the same localized core,
  shapers, pressure and rotating source frame with verified cutoffs.
- Certify the physical seven-ray cone support at every slice, including
  frame-error bounds; the bound in the new theorem is *assumed*.
- Build a compact source-matched weighted symmetric-divergence inverse,
  the nonlinear unforced correction and terminal-retention estimate.

Accordingly, this is a new **continuum radial FTC proof**, not a
formalization of the complete three-dimensional PDE reduction or an
unforced finite-time singularity.

## Reproduce

```sh
lake exe cache get
lake build UnforcedPatching.PressureCompensatedFluxSmoke
```

The smoke file prints the axioms of five relevant declarations and
contains no `sorry`, `admit`, or custom axiom. The physical-gate CI
workflow includes the smoke target.
