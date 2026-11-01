# H8 Attack N/O — exact physical Rayleigh and return-flow gate

**Scope:** Finite-profile conditional identities and classical disk spectral facts. No authenticated singular H8 source or unforced finite-time blow-up theorem is established.

## Source consistency audit

The authentic terminal core uses the implicit coordinates tau=T-t=q(1-eta^2), z=q^(1/2-h)eta, X=r^2/(2q). An H8 source-native note separately uses q=1-t. The two descriptions require an off-axis pullback; the cutoff, vector-potential gauge, shell shapers, seven-ray stress and periodic pressure have not been frozen as one physical tuple.

For a compact axisymmetric divergence-free conditional profile, the exact physical Jacobian yields M=||U||²~tau^(1/2-3h) M0 and N=||partial_z U||²~tau^(-1/2-h)N0. Differentiated profile-symbol assumptions give
c_A=tau^-1(R_U/M0 - (1/2-3h)/2)+O(tau^-1+2h)
and b_T=tau^-1(A/2+(R_W+S_W)/N0)+O(tau^-1+2h).
The translation source g_T and e_T reduce to finite time/advection profile quadratures. No numerical H8 coefficients are asserted.

## New sharp spectral and return-flow facts

For compact axisymmetric solenoidal U, integrated horizontal flux ∫ U_z dxdy is independent of z and equals zero since U vanishes outside an axial interval. A positive axial core therefore forces negative axial return flow on every intersected slice.

When support is inside r≤R sqrt(tau), the transverse planar vector is angular Fourier m=1 and has sharp disk Dirichlet constant j_(1,1)^2≈14.6819706421. The axial radial scalar also has mean zero; its sharp constrained Dirichlet constant is j_(2,1)^2≈26.3746164272 (Euler-Lagrange minimizer J0(j2 r)-J0(j2)). Both improve on the unrestricted j_(0,1)^2≈5.7831859629 used in the preliminary Appendix N support-only estimate. These Bessel spectral facts are classical, not independently novel.

With theta=||U_z||²/||U||², the improved physical support inequality is:
||grad U||²/||U||² ≥ [j1² + (j2²-j1²)theta] /(R² tau).

For X≤X*, |eta|≤eta*, R²=2X*/(1-eta*²), the resulting amplitude coefficient lower bound is
liminf tau c_A ≥ (1-eta*²)/(2X*) [j1²+(j2²-j1²)theta0] - (1/2-3h)/2.

If beta=1+alpha→1 and tau c_A→c0>0, the exact nonlinear amplitude equation beta'+c_A beta=F_A requires
lim_epsilon→0 [∫_(t0)^(T-epsilon) F_A(s)ds]/log((T-t0)/epsilon)=c0.
This is a necessary logarithmically averaged leading-order amplitude-injection law, not a constructive unforcing bound.

## Tests and release

11 new H8 Appendix N/O tests pass, including independent Bessel Rayleigh quotients and an exact divergence-free profile regression. 22 related local tests pass in combined scope. The five-page Appendix N/O source compiles after two LaTeX passes without reference or layout warnings. The prior 83 pages of the cumulative PDF are preserved exactly in extracted text; the extended PDF has 88 pages.

The GitHub manuscript includes a compact Appendix N/O summary, regression tests and this audit. The download package contains the complete five-page editable LaTeX source. Hosted CI does not supply a completed Lean singularity theorem, and the proof-gate JSON remains OPEN.

**Unproved:** The actual gauge-fixed H8 source and pressure/stress tuple; numeric coefficients c_A,g_T,b_T,e_T; the complementary propagator; nonlinear amplitude injection and terminal translation matching; and the L∞ terminal retention bound.