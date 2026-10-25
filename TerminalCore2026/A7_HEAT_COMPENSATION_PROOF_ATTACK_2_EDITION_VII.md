# Proof Attack 2 (Edition VII): Heat exterior and global pressure-moment restoration

## Source-equivalent theorem (exact, independent paper proof)
Appendix A.6--A.7 of the OpenAI forced source uses
H(Z) = Gamma(1+h)^(-1) integral_0^inf exp(-v) v^h (1+Zv)^(-h) dv,
Z=2(1-eta^2)/X. H(0)=1 and 0<H(Z)<1 for Z>0.

For the actual replacement Enew=Ecl[1+chi_K(H-1)], 0<=chi_K<=1,
set q=chi_K(1-H). Then 0<=q<1 and
Enew^2-Ecl^2= -Ecl^2 q(2-q) <= 0.
The heat-only pressure discrepancy D=(1/2) integral(Enew^2-Ecl^2)dlogX
obeys
-2 h(1+h)(1-eta^2) integral(Ecl^2 chi_K /X)dlogX <= D <= 0.
For |eta|<1, D<0 when the cutoff is nonzero on positive measure.
At eta=+/-1, D=0 exactly. Therefore the bare heat replacement
is NOT pressure neutral.

## Original compensation mechanism
Source Proposition A.7 compensates this defect in a reserved U=0
patch by matching three moments: pressure mass (1/2) integral E^2 dlogX,
S moment (-1/2) integral E^2 dX, and the renormalized angular
moment integral sqrt(2X)(E-Epow)dX. M and J are unchanged as U=0.
The normalized three weights are f*x^(-3/2-lambda),
-f*x^(-1/2-lambda), sqrt(2*x). They form a strict Chebyshev system;
three ordered disjoint positive bumps give an invertible 3x3
linear moment matrix.

## New explicit conditional inverse gate
For L c + Q(c)+d=0, with m>=norm(L^-1), delta=norm(d),
quadratic norm and two-point Lipschitz constant K, the condition
4*m^2*K*delta<1/2 suffices for a unique small root
norm(c)<=2*m*delta, by contraction. The source's real m,K,delta
have NOT been frozen or certified. This is a quantitative conditional
test of a standard local-inverse argument, not a new global theorem.

## Fundamental unforced-from-rest no-go
Any smooth finite-energy unforced Navier--Stokes solution with
zero initial velocity and sufficient decay has energy(t)=0 by
the classical energy identity and is identically zero. The
originating construction is forced and starts from rest.
A distinct unforced finite-time blowup construction must use
nonzero initial data or a justified different setting.

## Evidence and release status
Independent script verifies symbolic sign, exact rational and
generalized Vandermonde controls, 10,000 synthetic rational trials,
and 8 actual source heat-kernel integrals. Negative control:
heat-only pressure preservation REFUTED.
Lean A7HeatPressureScalar.lean: finite candidate, CI not yet confirmed;
gamma integral and full PDE NOT formalized.
Cumulative manuscript TeX input and GitHub CI updated.
The produced 15-page Edition VII PDF prepends the new three-page
Attack 2 note to the previous 12-page Edition VI addendum. It is
NOT a freshly compiled full-length master-paper PDF.
Remaining: actual three-bump source intervals and root,
all stress cones, Appendix B, unforced n=1,2 and higher orders,
physical zero-force residual, and complete Lean theorem.
