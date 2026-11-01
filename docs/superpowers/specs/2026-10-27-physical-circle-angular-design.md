# Cartesian stress pulled around a physical circle — design

## Objective

Join two existing kernel certificates: the Cartesian nonaxisymmetric axial
divergence contains `(-y n_x+x n_y)/r`, and periodic angular FTC removes
`(1/r)∂θ n` after azimuthal integration. The missing correspondence
is to certify `∂θ[n(r cos θ,r sin θ)]` by an actual chain rule, including
automatic endpoint equality.

## Chosen method

Use Mathlib's derivative of the real-parameter circle
`γ_r(θ)=(r cos θ,r sin θ)` and the Frechet chain rule for
`n : ℝ×ℝ→ℝ`. At each angle the derivative is the genuine linear map
`Dn(γ_r(θ))` applied to `(-r sin θ,r cos θ)`. Prove this equals the
Cartesian angular directional derivative `-y n_x+x n_y`, where the
partials are the values of the linear map on coordinate basis vectors.
The full-circle endpoint identity follows from the trigonometric
period; no ad hoc periodicity assumption on the physical pullback.

Then invoke the existing angular FTC with explicit integrability of
the pulled-back derivative. The resulting theorem removes the physical
`K_θz` contribution under the angular mean.

## Alternatives rejected for this step

- Globally differentiating `atan2`: unnecessary branch-cut complications.
- Assuming the pullback derivative or endpoint equality: repeats the
  prior conditional result instead of closing its geometric gap.

## Limits

Theorems apply to a genuinely differentiable tensor component `n`
at points of a fixed circle and an integrable derivative on its
parameter interval. They do not authenticate specific H8 fields,
perform axial integrations, commute radial differentiation under a
double integral, or construct a positive compact source-matched stress.

## Acceptance

Pinned Lean kernel checks the chain rule, coordinate directional
identity, automatic physical-circle boundary equality and exact
angular-integrated cancellation. No `sorry`, `admit` or extra axioms;
CI, exact regression suite, paper scope and PR are updated.
