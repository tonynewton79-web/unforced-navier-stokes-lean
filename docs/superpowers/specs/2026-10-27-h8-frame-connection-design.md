# H8 spatial-frame connection: proof design

## Intent

Extend the kernel-checked physical-circle angular bridge to stresses whose
coefficient matrix is expressed in a spatially rotating orthonormal frame.
The result is a local tensor differentiation theorem, not an H8 source match.

## Two routes considered

1. **Coordinatewise product rule, followed by matrix algebra (chosen):**
   every scalar component has an explicit `HasDerivAt` hypothesis; its actual
   physical derivative is computed using finite sums and the product rule.
   Orthogonality and its differentiated identity then yield the commutator.
   This exposes all derivative hypotheses to reviewers.
2. **Assume a tensor derivative identity directly:** terser, but risks
   moving the missing differential calculation into an opaque hypothesis.

## Scope

For 3x3 real `FrameMatrix` E(t), H(t), prove entrywise

`d/dt [E H E^T] = dE H E^T + E dH E^T + E H dE^T`.

For orthogonal E at t and a tangent derivative satisfying
`dE^T E + E^T dE=0`, set `Ω=E^T dE` and prove

`d/dt [E H E^T] = E (dH + Ω H - H Ω) E^T`.

Also prove skew symmetry `Ω^T=-Ω`, the `dE=EΩ` identity, a
constant-frame specialisation, and a nonconstant 2D-rotation-in-3D
test where dropping the commutator gives the wrong answer.

## Constraints

- No `sorry`, `admit`, new axioms, or equality asserted on paper only.
- Work in the existing `RotatingFrameDual.FrameMatrix` representation.
- Clearly distinguish pointwise frame identity from the authentic H8 source.
- No unproved differentiation-under-integral, compact support, positivity,
  or Navier--Stokes PDE resolution claim.

## Acceptance

Pin-matched Lean smoke file builds and prints only foundational axioms;
regressions and manuscript integration tests pass; the manuscript and CI
state the exact differential scope and remaining H8 cutoffs/frame bounds.
