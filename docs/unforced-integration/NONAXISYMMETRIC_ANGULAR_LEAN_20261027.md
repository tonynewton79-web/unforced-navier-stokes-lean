# Nonaxisymmetric Cartesian axial source and angular FTC certificate

27 October 2026.

Modules:

- `UnforcedPatching/NonaxisymmetricAxialBridge.lean` and smoke regression;
- `UnforcedPatching/AngularMean.lean` and smoke regression;
- imported reusable radius derivatives in `CartesianAxialBridge.lean`.

## Exact pointwise geometry

At a fixed axial height, let `m(x,y)=K_rz`, `n(x,y)=K_θz`, and
`r=sqrt(x²+y²)>0`. With genuinely differentiable Cartesian pullbacks,
define `K_xz=x*m/r-y*n/r`, `K_yz=y*m/r+x*n/r`. The kernel proves

```
∂x K_xz + ∂y K_yz
  = (x*m_x+y*m_y)/r + m/r + (-y*n_x+x*n_y)/r.
```

The last numerator is the polar directional derivative `∂θ n`;
the pointwise theorem never discards it. A pressure corollary adds
`∂z(K_zz+p)` at fixed Cartesian coordinates, with an explicit
`HasDerivAt` witness. An independently checkable example with
`m=0`, `n(x,y)=x`, `(x,y)=(3,4)` has divergence `-4/5`, illustrating
that angular terms can be locally nonzero.

## Exact full-period angular cancellation

For an independently supplied `2π`-periodic angular profile `G(θ)`
and interval-integrable derivative `D(θ)`, with differentiability on
the complete unoriented interval, the kernel proves

```
∫_0^(2π) D(θ) dθ = 0,
⟨A+(1/r)*D⟩_θ = ⟨A⟩_θ  (r>0),
⟨A⟩_θ = (1/(2π)) ∫_0^(2π) A(θ) dθ.
```

The example `G(θ)=(2π)θ-θ²` has zero equal endpoint values and
the nonconstant derivative `D(θ)=2π-2θ`, which integrates exactly
to zero by the same theorem.

## Remaining source-match requirements

The two theorems are independent: a separate semantic step must show
that the actual angular pullback of `K_θz` along the cylindrical circle
has derivative `-y*n_x+x*n_y`, has a periodic trace, and satisfies the
integrability hypotheses. Then axial integration, radial differentiation
under the integral, physical rotating-frame derivatives, authentic H8
profile/cutoff data and coefficient-cone support must be verified before
the source-native flux identity can be invoked. There is no complete
H8 source match or unforced Navier–Stokes singularity theorem.

Pinned Lean target smoke modules: `AngularMeanSmoke` and
`NonaxisymmetricAxialBridgeSmoke`. Both print the axioms of all three
declarations (including independent nonzero angular examples). No
`sorry`, `admit`, or custom `axiom` is accepted.
