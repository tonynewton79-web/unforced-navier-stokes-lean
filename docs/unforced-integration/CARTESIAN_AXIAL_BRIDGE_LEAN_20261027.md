# Axisymmetric Cartesian axial-divergence Lean certificate

27 October 2026. Source: `UnforcedPatching/CartesianAxialBridge.lean`;
regression: `UnforcedPatching/CartesianAxialBridgeSmoke.lean`.

## The physical geometric identity

At fixed height `z`, define `r = sqrt(x^2+y^2)` with `r>0`, and take
radial cylindrical mixed stresses `M(r)=K_rz` and `N(r)=K_θz`.
The Cartesian components of the actual axial tensor column are

```
K_xz = x*M(r)/r - y*N(r)/r,
K_yz = y*M(r)/r + x*N(r)/r.
```

For differentiable `M,N`, Lean proves (using actual one-dimensional
Cartesian partial derivatives with the other coordinate frozen)

```
∂x K_xz + ∂y K_yz = M'(r) + M(r)/r.
```

No assumption `N=0` is made. Its terms cancel because `N` is
axisymmetric. The geometric `M/r` term is present. The Lean theorem
`cartesianAxisymmetricNonzeroSwirlExample` verifies a concrete case
`M(r)=r^2`, `N(r)=7r`, `(x,y)=(3,4)`, where the Cartesian divergence is
exactly `15`.

The separate theorem `cartesianAxialPressureBalance` appends
`∂z C(z)` for the axial trace `C(z)=K_zz+p` (at the evaluation point
`(x,y)`), giving the complete axisymmetric pointwise axial source
`f_z=M'(r)+M(r)/r+∂z(K_zz+p)`.

## Precise proof boundary

This closes a real Cartesian-to-cylindrical pointwise geometry subcase,
but **not** the entire manuscript's source-to-FTC chain. In particular:

- General nonaxisymmetric stress has an additional
  `r^-1 * ∂θ K_θz` term; averaging it with verified angular periodicity
  is a separate obligation.
- Spatially varying H8 frames require explicit connection terms when
  differentiating `E H Eᵀ`; this theorem treats only the physical
  axisymmetric tensor components at a fixed height.
- Axial and azimuthal integration, radial differentiation under the
  integrals, authentic Case 006 cutoffs/coefficients, pressure boundary
  representatives, weighted cone support, and compactness remain open.
- No Navier–Stokes blow-up or global unforced PDE closure follows.

Lean target: `lake build UnforcedPatching.CartesianAxialBridgeSmoke`.
The smoke module prints foundational axioms of the main theorem, the
pressure corollary, and the nonzero-swirl example. Never treat
`#check` alone as semantic source authentication.
