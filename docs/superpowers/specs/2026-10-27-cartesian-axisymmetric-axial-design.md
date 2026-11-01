# Axisymmetric Cartesian-to-cylindrical axial source: design

## Intent

Build the next genuine geometric Lean bridge for the manuscript's annular
pressure-compensated flux identity. In particular, calculate the Cartesian
axial divergence of an axisymmetric mixed tensor written in orthonormal
cylindrical components, instead of taking the cylindrical divergence formula
as an unproved definition.

## Scope

Fix an axial height `z`, away from the symmetry axis. Let the physical
Cartesian components of the axial tensor column be

`K_xz = (x M(r) - y N(r))/r`,
`K_yz = (y M(r) + x N(r))/r`,
`r = sqrt(x^2+y^2)`.

Here `M` is the cylindrical `rz` mixed component and `N` the cylindrical
`θz` component; both may vary with radius but not with azimuth. Prove
their *actual Cartesian partial derivative* sum is `M'(r)+M(r)/r`.
Include the axial derivative of `C(z)=K_zz+p` without discarding pressure.
Use hypotheses about first derivatives at the evaluation point, not global
smoothness or unjustified differentiation under an integral.

## Approaches considered

1. **Explicit polar geometry and Mathlib derivative rules (selected).** Proves
   a source-meaningful Cartesian divergence formula with exact hypotheses.
2. Assume the cylindrical divergence formula and only integrate it. Faster,
   but repeats the earlier conditional bridge without proving geometry.
3. Full nonaxisymmetric, spatially rotating Cartesian tensor calculus.
   Ultimately necessary, but requires multivariable field derivatives and
   angular chain rules beyond this focused unit.

## Non-goals

- No assertion about arbitrary angular dependence, spatially rotated H8
  frames, the authentic source/cutoff, or a singular PDE solution.
- No implicit zero-pressure or zero-swirl assumption.
- No inference of the source-integral hypotheses of the existing
  `PressureCompensatedFlux` theorem from only pointwise smoothness.

## Success criteria

Lean 4.34.0-rc2 checks the geometry theorem and the pressure-source
corollary with only standard kernel foundational axioms; a smoke test
evaluates a nonzero azimuthal mixed stress example exactly. CI includes
the smoke target, and the existing Python tests still pass.
