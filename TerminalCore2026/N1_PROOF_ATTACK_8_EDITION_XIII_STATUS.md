# Proof Attack 8 / Edition XIII (23 October 2026)
## Status: CONDITIONAL FIRST LINEAR GATE CLOSED; COMPLETE UNFORCED PDE OPEN

Let u_B be a smooth divergence-free physical background with full NSE
residual R_B=dt u_B - nu Delta u_B + (u_B.grad)u_B + grad p_B.
On a time interval with R_B continuous into H1 and bounded u_B,
grad u_B, the exact Leray Stokes first response
w1(t)=-integral_t0^t exp(nu(t-s)Delta) P R_B(s) ds
with pressure increment -Delta^(-1)div R_B exists, is solenoidal,
starts from zero and has initial jet w1_t(t0)=-P R_B(t0).
The corrected momentum residual is EXACTLY
(u_B.grad)w1+(w1.grad)u_B+(w1.grad)w1.
If M=sup norm(R_B)_H1 and U=sup(||u_B||infty+||grad u_B||infty),
then ||w1||_H1<=a M, and ||residual||_H-1<=U a M+C4^2 a^2 M^2,
a=t-t0. Pressure cancels the gradient residual, with no assumption
that the initial source residual is solenoidal.
For a divergence-free compact Phi, the initial response pairing
matches the Edition XII nonflat-jet theorem.

For a stationary Gaussian pure swirl U=r exp(-r^2-z^2), p_B=0, nu=1,
its **full** physical residual is
Rr=-r exp(-2(r^2+z^2)), Rz=0,
Rtheta=2r(5-2r^2-2z^2)exp(-(r^2+z^2)).
The meridional curl d_z Rr - d_r Rz=4rz exp(-2(r^2+z^2))
is nonzero at r>0,z!=0; hence the projected initial correction
necessarily has a meridional component.

Independent known control: 3D periodic sinusoidal shear
u_B=A sin(kz)e_x, w1=(exp(-nu k²(t-t0))-1)u_B gives an
EXACT smooth unforced solution and zero nonlinear remainder.
This is established simple prior art and NOT blow-up.
Independent symbolic Gaussian and shear identities passed,
500 random finite Fourier Leray projection idempotence/orthogonality
tests passed, and 10000 exact rational Young inequalities passed.

CRITICAL HOLD:
The construction is a standard conditional first LINEAR correction,
not a globally supported/matched source-collar solution;
the heat kernel is nonlocal, and the nonlinear remainder is
generally nonzero. The actual source's full physical residual and
its uniform H1/time bounds approaching t=1 remain uncertified.
The next attack must solve the nonlinear Oseen/NS perturbation
with actual geometry, all exterior matching, nonzero initial data,
terminal singularity, and full order-by-order Lean kernel proof.
The submitted Lean module N1ProjectedStokesScalar.lean formalizes
only elementary scalar algebra. Github CI must return a completed
successful run before claiming kernel verification.

GitHub cumulative master TeX is updated; the separate cumulative
Edition XIII PDF is a 27-page research addendum (2 new + 25 prior),
not a freshly compiled complete master-paper PDF.
