# H8 dynamically restricted two-mode correction gate — 29 October 2026

The current H8 source-freeze checklist still has no single authenticated singular periodic tuple (core, local potential, cutoff, physical stress, pressure and shapers). Consequently the concrete projected residuals, propagator exponents and nonlinear retention estimates for that **actual** source are not certified.

## Exact new identities

For a smooth periodic solenoidal prepared carrier U, let W=∂zU and M=||U||², N=||W||². Then <U,W>=0. The rank-two carrier projection is P_AT f=<f,U> U/M + <f,W> W/N. The amplitude-channel residual obeys

c_A(t)=<G,U>/M = (log M)'/2 + ||∇U||²/M,

where G=U_t−ΔU+P div(U⊗U).

If ||U||∞≤Cτ^(−A), ||W||∞≤Cτ^(−1), and U has a lower bound cτ^(−A) at one point, then any exact correction w=αU+aW+v with α=o(1), a=o(τ^D), ||v||∞=o(τ^(−A)) retains terminal speed divergence. Here A=1/2+h and D=1/2−h.

## Exact diagnostic counterexample

For U=τ^(−A) sin(z)e_x, <G,W>=0 and Q_AT G=0, but c_A=A/τ+1. The exact unforced shear u=K(t0)e^(−(t−t0))sin z e_x has w=u−U with a=0, Q_AT w=0 and α→−1, fully canceling the prepared singularity. An amplitude condition is independent of translation matching.

## Dynamically restricted positive-control and nonlinear warning

For U=τ^(−1−h)sin z e_x, the homogeneous linearized equation admits V=C(t)sin y cos z e_x+Z(t)sin y e_z, Z=εe^(−(t−t0)), C'+2C=−KZ, C(t0)=0. It is divergence-free and exactly orthogonal to U and W. The complementary response grows only O(τ^(−h)), although the instantaneous strain has size τ^(−1−h). This is a diagnostic, not an authentic H8 solution.

Its quadratic nonlinearity projects to carrier amplitude:
P_A Pdiv(V⊗V)=−(ZC/(2K))U, while the translation projection vanishes. This shows the dynamically favorable linear subspace is not invariant under the full nonlinearity.

## Verification and release status

The additional exact regression module passed 7/7 locally. The combined nearby H8 regression suites passed 37/37. The 77-page existing cumulative PDF was preserved and a three-page Appendix L appended; the resulting PDF has 80 pages, with first 77 page text streams identical. No fresh full Lean existential theorem is claimed.

Next authentic gate: source-fixed values of c_A, <G,W>/N and Q_ATG; modulation of both amplitude and translation with moving projections; a nonlinear complementary estimate strong enough to imply the pointwise retention conditions.

The proof gate JSON remains OPEN.
