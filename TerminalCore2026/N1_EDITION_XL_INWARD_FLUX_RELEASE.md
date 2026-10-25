# Edition XL — a single-flow signed inward flux, and radial concentration barrier

25 October 2026 | Tony Newton | Newton Astro Labs

## Status

**PROVED analytically:** one global smooth exactly unforced whole-space flow has signed inward angular-momentum flux through all sufficiently small radii simultaneously for one common positive initial time interval. An independent whole-space energy inequality forces any hypothetically amplified radial-flux peak to narrow logarithmically and imposes a quantitative H² cost.

**NOT PROVED:** any terminal tau^-h Reynolds-torque growth, retained OpenAI Section 10 pointwise blowup, numerical original-source profile, or complete kernel-checked Lean 3D NSE proof.

## Exact nonaxisymmetric datum and flux

Let eps=nu/1000, rho²=x²+y²+z², r²=x²+y².
u0=curl(eps exp(-rho²)[x-r²*y] e_z).
This is nonzero, smooth, divergence-free and rapidly decaying.
The critical Fourier X^-1 norm bound is unchanged from Edition XXXVII:
(2pi)^(-3/2)||u0||_X^-1/nu <=1/(100 sqrt(pi))<1/16.
The standard convergent small-data Fourier mild solution supplies global smooth **unforced** NSE evolution with reconstructed pressure.

With Gamma=r*u_theta,
bar(u_r'Gamma')(0,r,z)=-eps² r³ exp(-2rho²),
T(0,r,z)=4eps²r²(1-r²)exp(-2rho²).
Both were separately checked from the full initial quadratic advection.
Choose the explicit smooth nonnegative normalized axial bump
eta(z)=C exp[-1/(1-z²)] for |z|<1, zero otherwise.
The advective cylinder flux is F(R,t)=R² integral eta ur utheta dtheta dz.
At t=0,
F(R,0)=-2pi eps² R⁴exp(-2R²) integral eta(z)exp(-2z²)dz<0.
Near the axis the angular covariance J(r,z,t)/r³ has a continuous extension,
with initial value -eps² exp(-2z²). Therefore there are common Rstar,delta>0
(not assigned unsupported numerical values) such that for **all** 0<R<=Rstar
and all 0<=t<=delta,
F(R,t)<= -pi eps²exp(-2) R⁴.
This includes every radius R_j=2^-j Rstar of a **single fixed flow**.

## Terminal amplification obstruction

For any smooth finite-energy unforced flow of energy E0,
B_eta=||eta||infinity E0/2, at each fixed time:
integral_0^infty |F(R,t)| dR/R <= B_eta.
Hence if |F|>=A on an interval I, then log-width(I)<=B_eta/A.
If |F(R0,t)|>=A, some R_c in [R0,R0 exp(4B_eta/A)] satisfies
|R_c partial_R F(R_c,t)|>=3A²/(16B_eta).
In particular any hypothetical tau^-h flux peak must have half-height
logarithmic width <=(2B_eta/c) tau^h, and radial logarithmic derivative
magnitude >=const tau^-2h somewhere nearby. This is a necessary condition
on a proposed amplified flux, **not** a theorem the flux must amplify.

For C2=4/(pi sqrt(2)3^(7/8)), by interpolation:
||Delta u(t)||₂ >=
 (|F(R,t)|/[pi R²||eta||_1 C2² E0^(1/4)])^(2/3).
If R_tau=sqrt(2Xtau) and |F(R_tau,1-tau)|>=c tau^-h for all
sufficiently small tau, then ||Delta u||₂>=const tau^-2(1+h)/3
and its squared time integral diverges. Again necessary, not contradictory.

## Verification

Exact SymPy cylindrical Fourier averages and full mean-advection identity;
exact Gaussian axial weighted integrals and logarithmic flux sum.
25,000 exact rational inward-sign tests.
Independent 25,000 exact rational concentration/radial-derivative tests.
Three-page standalone LaTeX/PDF compiled and visually checked.
Finite Lean scalar lemmas and isolated GitHub workflow committed; full
PDE theorem is not formalized and CI success requires separate confirmation.
The original actual Section 10 source remains FAIL_CLOSED_MISSING_SOURCE_DATA.

## Why this is not an unforced blowup theorem

The globally smooth example has inward flux decaying like R⁴ and no
singularity at t=1. A hypothetical divergent radial advective flux is a
different condition than the prior necessary **integrated torque or
angular oscillation** tau^-h requirement. No bridge from such flux to
pointwise source-swirl retention has been proved.

Next: derive a source-matched signed flux lower bound for one unforced
evolution with certified viscosity, axial leakage, moving-boundary and
angular-mode losses, or rule out a proposed concentration profile.
