# Nonaxisymmetric axial geometry and azimuthal cancellation — design

## Intent and accepted direction

Continue the source-to-flux formalization after the Cartesian axisymmetric
bridge. In the nonaxisymmetric case the tangential mixed-stress component
is not ignorable pointwise; its angular derivative cancels only after
periodic angular averaging.

## Chosen architecture

1. A local Cartesian theorem for arbitrary C¹ mixed-stress pullbacks
   `m(x,y)=K_rz` and `n(x,y)=K_θz`, away from the axis. Define the Cartesian
   axial column as `(x m-y n)/r`, `(y m+x n)/r`. Prove by **genuine x- and
   y-derivatives** the formula
   `∂x K_xz+∂y K_yz = m/r+(x m_x+y m_y)/r+(-y n_x+x n_y)/r`.
   The last numerator is the angular directional derivative, not zero.
2. A separate interval-FTC theorem for a `2π`-periodic angular profile
   `N(θ)` with integrable derivative. Show its angular derivative integral
   is exactly zero, and transfer that cancellation to angular averages
   of a general source with coefficient `1/r`.

## Alternatives considered

- Define a global `atan2` chart and express every field as `M(r,θ)`.
  This introduces global branch-cut chart issues irrelevant to the local
  cylindrical divergence identity.
- Start from the cylindrical divergence formula as an assumption. This
  would not reduce the remaining geometric gap.

## Scope limits

The Cartesian theorem uses Cartesian partial differentiability; proving
that a *specific H8* tensor supplies those functions and their derivatives
is separate. The FTC theorem uses periodicity and integrability, and does
not assume a genuine H8 profile is periodic until that is authenticated.
No Fubini interchange, differentiation through axial integrals, spatially
varying H8 frame derivatives, compactness or PDE singularity is claimed.

## Release requirements

Lean 4.34.0-rc2 / pinned Mathlib, no `sorry`/`admit`/custom axioms,
explicit smoke tests with nonzero angular derivative and a periodic
nonconstant example, the original Python suite, and CI smoke targets.
