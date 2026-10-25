# Proof Attack 4 — Edition IX (22 October 2026)

## Exact limited theorem: frozen-meridional swirl-only repair
In smooth axisymmetric cylindrical Navier–Stokes for r>0, replacing
u_theta=U by U+W and freezing u_r,u_z changes radial convection by
-(2UW+W^2)/r and changes axial convection by exactly zero.
If the original meridional momentum equations are satisfied and
only pressure delta-p is permitted to adapt, then
  d_r(delta-p)=(2UW+W^2)/r, d_z(delta-p)=0,
so d_z[(2UW+W^2)/r]=0.
For any fixed (r,t) with U(r,z,t)>0 for all real z and W(r,.,t)
smooth and compactly supported in z, W must vanish identically:
the bracket is constant, vanishes off support, and hence
W/U is a continuous function taking values in {0,-2},
zero off support and thus zero everywhere.
The same argument holds on a connected axial interval with a
zero of W and strict U>0. This is a genuine restricted theorem,
NOT a theorem against arbitrary unforced Navier–Stokes corrections.

## Exact linear Stokes response
For smooth axisymmetric pure swirl v0 and smooth axisymmetric cutoff
chi, g=nu chi d_zz v0 is itself divergence-free and azimuthal.
The Duhamel mild solution w(t)=int_0^t exp(nu(t-s)Delta)g(s) ds
is solenoidal and azimuthal, and corrects precisely the isolated
linear Stokes residual, with L2 and H1 heat-semigroup bounds.
The remaining nonlinear projected residual comprises
P[(u0.grad)w+(w.grad)u0+(w.grad)w] plus any background remainder.
This candidate need NOT be compactly supported and is not a
solution to the coupled nonlinear source collar problem.

## Independent controls
- Cylindrical exact centrifugal difference: PASS.
- Toy smooth perturbation U=r exp(-r^2-z^2), W=eps r z exp(-r^2-z^2):
  d_z[(2UW+W^2)/r] at z=0 is exactly 2 eps r exp(-2r^2), nonzero.
- Known periodic decaying-shear unforced solution:
  A exp(-nu k^2 t) sin(kz) e_x, with pressure zero: PASS.
- Stationary-shear nonzero-residual negative control: PASS.
- Source-specific true annular cancellation: HOLD.
- New Lean module N1MeridionalCompatibilityScalar.lean only formalizes
  scalar consequences; full cylindrical calculus and Stokes mild
  result are NOT machine-formalized. GitHub CI must confirm compilation.

## Remaining decisive targets
Solve the actual coupled order-one Oseen/Stokes meridional,
swirl and pressure system in the annulus with correct boundary
matching, source amplitudes, and nonzero initial datum.
Then certify all orders, convergence, exact zero physical forcing,
global geometry, and the full Lean theorem. No unforced blowup proof.
