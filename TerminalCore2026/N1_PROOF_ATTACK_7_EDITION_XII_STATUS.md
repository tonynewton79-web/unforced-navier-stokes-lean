# Proof Attack 7 — Edition XII (23 October 2026)

## Mathematical theorem: nonflat immediate correction
For any sufficiently regular divergence-free background u_B, define its
**entire physical** unforced momentum residual
R_B = partial_t u_B - nu Delta u_B + (u_B.grad)u_B + grad p_B.
Suppose a smooth compact divergence-free test Phi satisfies
B=<R_B(t0),Phi>>0 and a genuinely force-free correction
u=u_B+w starts with w(t0,.)=0.

Subtracting the full NSE identities, pairing with Phi, and using
that all spatial derivatives of w vanish at t0 gives EXACTLY
<partial_t w(t0),Phi>=-B<0.
Thus any correction w with w_t(t0)=0 is impossible under these
assumptions. If w is C1 in time with values in L2, for some delta>0:
norm(w(t))_2 >= B*(t-t0)/(2*norm(Phi)_2) for t0<t<t0+delta.

This is a conditional classical local compatibility theorem, not a
singularity discovery and not proof that the actual source-collar
residual survives unchanged after all later edits.

## Exact smooth-background positive control
Take pure Gaussian swirl u_B=r exp(-r^2-z^2)e_theta, p_B=0, nu=1,
globally smooth divergence-free and finite energy. Its actual
azimuthal physical residual is
R_theta=2r(5-2r^2-2z^2)exp(-r^2-z^2).
On r in [1/2,1], z in [-1/2,1/2] this is >=(5/2)exp(-5/4)>0.
The compact C3 test zeta=(r-1/2)^4(1-r)^4(1/4-z^2)^4
has exact weighted mass int zeta*r dr dz=1/270950400,
giving <R,Phi> >= 5*pi*exp(-5/4)/270950400 > 0.
C_infinity positive test approximations exist within the strict
positive neighborhood. High-precision quadrature independently
gave B~=7.27892839717989282191209e-8 vs analytic lower
1.66097072570147392191317e-8.

## Negative control
For g(z)=exp(-z^2), -g''(0)=2>0 yet int_R -g'' dz=0.
Local positivity cannot justify a global torque no-go; source
matching and a fully coupled response may still exist.

## Verification and release
Independent SymPy/rational proof script verifies Gaussian
vector-Laplacian, compact-bump beta mass, azimuthal solenoidality,
a positive numerical pairing above an analytic lower, the
zero-global-torque counterexample and 10,000 exact-rational scalar
cases. 10000/10000 pass. New Lean candidate
N1NonflatStartupScalar.lean formalizes scalar sign and rational
identities ONLY, not the continuum integrals, full functional
differentiation, matched source, or NSE. Kernel CI status must be
independently checked and must not be presumed PASS.

## Remaining OPEN/HOLD
Authenticate the complete physical residual for ONE source profile
across collar/matching transitions; solve the coupled inhomogeneous
n=1 parabolic/elliptic problem with necessary nonflat startup jet;
reconcile pressure and meridional equations, initial data and
infinity/axis conditions; close n=2 and the entire infinite
hierarchy; prove physical zero-force reconstruction; formalize
full result in Lean. No proof of unforced 3D singularity.

The cumulative paper source is updated in GitHub Draft PR #1.
The 25-page Edition XII PDF is an addendum that prepends this
two-page theorem to the previous 23-page Edition XI cumulative
addendum; it is not a newly compiled full-length master PDF.
