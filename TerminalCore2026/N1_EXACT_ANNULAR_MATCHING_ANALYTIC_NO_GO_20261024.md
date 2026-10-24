# Proof Attack 16 / Edition XXI: Analyticity obstruction to exact annular gluing
Date: 24 October 2026

**A restricted conditional no-go for an exact-gluing strategy, not a proof
against all unforced finite-time blowup constructions.** The analyticity
premise uses established spatial analyticity of strong unforced
Navier–Stokes solutions at positive times, not original work.

Let h>0, c_inf>0, t0 in (0,1), tau=1-t0 and let
  f(R)=c_inf 2^(1/2+h) E_{V~Gamma(1+h,1)}
            [R^-1 (R^2+4V)^(-h)].
Let the source-leading idealized exterior swirl field on r>0 be
  u_ext(x,y,z)=tau^(-(1/2+h)) f(r/sqrt(tau)) e_theta,
  r=sqrt(x^2+y^2).

The function u_ext is real-analytic on the *connected*
punctured-axis domain Omega={r>0}. For fixed r>0, this follows by
local holomorphic differentiation of the gamma integral, dominated
uniformly for complex R in a sufficiently small disk centered at
each positive real R. It is analytic as a Cartesian vector
field because e_theta=(-y/r,x/r,0) is analytic for r>0.

### Restricted analytic non-gluing theorem

Suppose u is a finite-energy H^s (s>5/2) strong solution of
unforced 3D Navier–Stokes on R^3 with viscosity nu>0, defined
on [0,T) with t0 in (0,T), and suppose the standard
positive-time spatial analyticity theorem applies to u(t0).
Then u(t0) **cannot coincide identically** with u_ext on
any nonempty open subset of Omega.

Proof. Real-analytic identity continuation on connected Omega
would imply u(t0)=u_ext everywhere on Omega. But as r->0,

  u_ext ~ C tau^(-h) e_theta/r,
  C=c_inf 2^(1/2-h)/Gamma(1+h)>0.

This fails even local L^2 near the axis, since in any finite
z-interval its squared norm contains integral_0^epsilon dr/r.
This contradicts u(t0) in H^s(R^3), and proves the theorem.

Note that u_ext is also independent of z, hence globally
infinite-energy even away from the axis; the axis argument
already yields a strictly local contradiction.

The theorem is stronger than merely observing a bad singular
extension: a smooth global unforced solution cannot **exactly
match the singular analytic exterior profile on any open
annular space-time patch at a positive time**, even if the
solution is patched elsewhere with smooth nonanalytic cutoffs.
Positive-time analytic smoothing defeats such exact patching.

**Scope and limitations:**
- An *asymptotic* match with a nonzero analytic error is NOT
  excluded. The published source's actual full exterior and
  oscillatory corrections may differ from the leading profile.
- The theorem does NOT exclude global smooth solutions whose
  annular profile approximates the leading exterior to high
  order, nor does it prevent singularity at t=1.
- A purely C-infinity cut-off glued field may be smooth but is
  not automatically an unforced NSE solution, precisely because
  the unforced PDE enforces positive-time analyticity.
- No Lean theorem of analytic regularization or identity
  continuation has been produced in this repo.

**Established prior-art analyticity inputs:**
Ping Zhang, "3-D Anisotropic vs. Classical Incompressible
Navier–Stokes Equations", ICM 2026, Sec. 4,
DOI 10.1137/25M1801980, reviews spatial analyticity
of strong Navier–Stokes solutions, including the original
Masuda/Foias–Temam results and whole-space extensions.
https://doi.org/10.1137/25M1801980

**Next genuine research target:** prove a quantitative *approximate*
analytic matching bound which allows sufficiently small nonzero
annular mismatch but controls its continuation toward the axis,
pressure and the terminal norm. Exact zero error is ruled out
in the stated strong-solution regime; a viable construction must
use an analytically compatible nonzero matching tail.

STATUS: RESTRICTED SOURCE-SPECIFIC MATCHING OBSTRUCTION,
NO UNFORCED BLOWUP PROOF, NO FULL LEAN CERTIFICATE.
