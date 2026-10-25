# Edition XLI — Intermittent radial variation and near-axis Reynolds torque

25 October 2026 | Tony Newton | Newton Astro Labs

## Authenticated analytical result (single smooth unforced flow)

For any smooth finite-energy exactly zero-forcing solution in R3,
F_R(t)=R² int eta(z) u_r(R,theta,z,t)u_theta(R,theta,z,t) dtheta dz,
where eta is a compact axial weight whose support has length L,
let D_I=int_I ||grad u(t)||_2² dt and E0=||u(0)||_2².

For any radius R and time interval I, with S3 any standard homogeneous
Sobolev H1->L6 constant,

int_I sup_{0<rho<=R}|F_rho(t)|dt
<=int_I int_0^R |partial_rho F_rho|drho dt
<=||eta||_infty D_I [
 S3² (pi L)^(2/3) R^(4/3) + S3 (pi L)^(1/3) R^(5/3)]
<=||eta||_infty E0/(2nu) [same bracket].

The proof retains the full exact no-forcing energy dissipation,
the cylindrical radius factors, and the velocity-gradient contribution.
On I_tau=[1-2tau,1-tau] with R_tau=2sqrt(X tau), the LHS is
o(tau^(2/3)), by absolute continuity of the enstrophy dissipation.
This is a space-time radial-variation bound; it does NOT bound an
isolated derivative spike at one time/radius.

## Intermittent derivative lower bound / concentration cost

If |partial_R F_R| >= A_tau on a radial interval of width ell_tau
for times of measure |W_tau|, then A_tau*ell_tau*|W_tau|
is at most the RHS above. If ell_tau~sqrt(tau),
|W_tau|~tau, and A_tau~tau^(-alpha), no fixed-positive such
profile can persist for alpha>=5/6. Slower profiles are not excluded.

The previous Edition XL pointwise moving-radius dissipation bound
is stronger when applied only to F_{R(t)}; the new result is genuinely
about **radial total variation and intermittent derivative spikes**.
It is NOT a positive terminal-cascade theorem.

## Angular-frequency leakage after differentiation

Let J=avg(u_r' Gamma'), K=avg(u_z' Gamma') and
T=-r^-1 partial_r(rJ)-partial_z K.
Truncating to Fourier modes |m|<=N leaves an error <=
[1/(2pi(N+1)²)](
  r^-1 Utheta Gtheta + Utheta_r Gtheta + Utheta Gtheta_r
  + Ztheta_z Gtheta + Ztheta Gtheta_z).
Mixed angular-radial and angular-axial derivatives are explicitly
present; a small raw flux tail alone cannot certify a small TORQUE tail.

## Leading universal axis-jet coefficient

For U=u_x,V=u_y,W=u_z evaluated on the symmetry axis,
a=U(0,0,z,t), b=V(0,0,z,t),
J3=[a(-2Uxy+Vxx-Vyy)+b(Uxx-Uyy+2Vxy)]/8,
K2=(b Wx-a Wy)/2,
T(r,z,t)=r²(-4J3-partial_z K2)+O(r⁴).
First-transverse-derivative quadratic covariance terms CANCEL.
The exact Edition XXXVII Gaussian produces Lambda=-4epsilon²exp(-2z²)
and verifies the formula independently.

## Verification and release limits

Exact independent SymPy checked Gaussian flux, its total radial
variation, universal Cartesian second jets, and leading Gaussian
coefficient. 40,000 seeded exact Fraction cases passed.
A scholarly 3-page LaTeX PDF was compiled twice and rendered/visually
inspected. The release ZIP is checked against SHA-256.

Only elementary scalar implications were written in Lean;
kernel CI is unconfirmed, and the full Fourier/Sobolev/Navier--Stokes
PDE and singularity are not formalized.
The OpenAI Section 10 numerical source is still unfrozen. It is
a FORCED smooth blowup construction; a source-preserving zero-force
solution and the required positive terminal torque lower bound
are NOT established.

**Next gate:** derive an exact source-compatible positive signed torque
or velocity-jet amplification mechanism for one fixed unforced flow,
while meeting radial BV, viscous dissipation, angular-mode leakage,
the entire moving-cylinder balance and the pointwise swirl criterion.
