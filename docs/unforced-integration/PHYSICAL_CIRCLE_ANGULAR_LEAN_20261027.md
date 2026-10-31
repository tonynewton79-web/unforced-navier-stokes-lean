# Physical-circle source derivative and angular average: Lean certificate

27 October 2026. Modules `PhysicalCircleAngular.lean` and
`PhysicalCircleAngularSmoke.lean` are a direct continuation of the
Cartesian nonaxisymmetric and periodic angular FTC certificates.

## What is now proved

For `γ_r(θ)=(r*cos θ,r*sin θ)` and a physical Cartesian scalar stress
component `n : ℝ×ℝ→ℝ`, a genuine Frechet derivative `Dn` at
`γ_r(θ)` supplies the exact chain-rule derivative

```
d/dθ [n(γ_r(θ))] = Dn(γ_r(θ))[-r sin θ, r cos θ]
                     = -y * n_x + x * n_y.
```

The coordinate identity uses the continuous linear derivative evaluated
on Cartesian coordinate directions `(1,0)` and `(0,1)`. After dividing
by the radius, this is **exactly** the angular term in the previously
verified nonaxisymmetric Cartesian axial divergence.

The physical circle itself satisfies `γ_r(2π)=γ_r(0)`, so the
pulled-back physical stress has equal endpoints without an extra
periodicity assumption. Under explicitly assumed interval integrability
of the angular derivative, the kernel proves

```
∫_0^(2π) Dn(γ_r(θ))[-r sin θ,r cos θ] dθ = 0.
```

With `r>0` and integrable remainder `A`, this gives

```
⟨A + (1/r) * ∂θ[n(γ_r(θ))]⟩ = ⟨A⟩.
```

All seven public declarations in the smoke module compile with only
`propext`, `Classical.choice`, and `Quot.sound` reported by Lean.

## Exactly what remains

- The authentic Case 006/H8 physical mixed stress must be supplied as
  an explicit differentiable Cartesian function at all points of every
  relevant circle, including its varying orthogonal frame.
- Interval integrability of its circle derivative is still required.
- The full axial trace `K_zz+p` and angularly averaged source must be
  axially integrated, with a certified interchange of radial
  differentiation and integration. This is the next analytic gate
  before the conditional radial pressure-flux identity can be applied
  to the authentic source.
- The positive coefficient cone, compact-support construction and
  global PDE closure are not produced by this geometry theorem.

No claim of an unforced Navier--Stokes singular solution follows.
