# Proof Attack 15 — exact gamma-mixture exterior heat identity
Date: 24 October 2026

**Status: source-specific exact analytic identity and an annular pure-swirl
positive control. NOT a globally smooth, finite-energy, unforced blow-up
solution. No mathematical originality/priority claim is made for the
underlying heat-kernel profile.**

## Original source-leading exterior data

For h>0, A=1/2+h and R>0, write

  f(R)=c_inf 2^A E[g(R,V)],
  g(R,v)=R^(-1)(R^2+4v)^(-h),
  V distributed as Gamma(shape=1+h,scale=1).

The source exterior expression from Theorem 4.6(v), equation (4.29) of
the original forced construction reduces to this profile. We derive a
previously unrecorded *in our local proof ledger* exact identity for it.

Let p_h(v)=exp(-v) v^h/Gamma(1+h). Define
L_theta f=f_RR+R^(-1)f_R-R^(-2)f.

## Theorem: self-similar radial heat equation

For all R>0 and h>0,

  L_theta f = (1/2+h) f + (R/2) f_R.                 (1)

Proof. Let S=R^2+4v and D=L_theta-A-(R/2)partial_R.
Direct differentiation gives the exact pointwise rational identity

  (Dg)/g = 4h[R^2(1+h-v)-4v^2]/S^2
         = 4h[(1+h-v)/S-4(1+h)v/S^2].

Because p_h'(v)/p_h(v)=h/v-1 and
partial_v g/g=-4h/S, the last expression equals

  Dg = 1/p_h(v) * partial_v
          [p_h(v) * (4h v/S) * g(R,v)].              (2)

At v=0 the bracket vanishes as v^(1+h), and as v->infinity
it vanishes exponentially. Integrating (2) in v proves (1).
Differentiation under the integral is justified for fixed R>0
by exponential integrability and the strictly positive denominator.

Consequently, for tau=1-t>0 and viscosity nu=1, the axially
independent pure-swirl field

  U(r,t) = tau^(-A) f(r/sqrt(tau)),

satisfies exactly

  partial_t U = partial_rr U+r^(-1)partial_r U-r^(-2)U

on every r>0. For viscosity nu other than one, the gamma-mixture
requires the corresponding 4 nu v scaling rather than 4v.

## An exact annular unforced Navier-Stokes patch

Set u=U(r,t) e_theta, independent of z, on a cylindrical annulus
r in (a,b) with 0<a<b (local in space and prior to t=1). The
centripetal term is -(U^2/r)e_r. The local pressure

  p(r,t) = integral_(r_*)^r U(s,t)^2/s ds

has partial_r p=U^2/r and partial_z p=0. It follows from (1)
that this idealized leading exterior satisfies the **unforced**
Navier-Stokes equations on that annulus, with no external forcing.
This does not establish that the *complete gluing of inner, collar,
oscillatory, and meridional source fields* satisfies them.

## Critical axis obstruction (why this is NOT a blow-up solution)

For h>0, by dominated convergence,

  lim_(R->0+) R f(R)
    = c_inf 2^A 4^(-h) E[V^(-h)]
    = c_inf 2^(1/2-h)/Gamma(1+h) > 0.

Therefore at every fixed tau>0,

  U(r,t) ~ [c_inf 2^(1/2-h)/Gamma(1+h)] tau^(-h)/r
    as r->0+.

The idealized exterior-only swirl is ALREADY singular on the axis
for every t<1 and is not an admissible smooth finite-energy global
initial datum. The source construction avoids this by replacing the
exterior near the axis; the cutoffs and joins produce the actual
uncancelled forcing/compatibility obligations. There is no
Millennium-problem solution in this local annular identity.

## Stronger next attack

The exterior leading patch is **not** the appropriate target for
a global "heat defect" correction: it solves its heat equation
identically. Instead, isolate the genuine projected forcing arising
from the matched transition/terminal collar, axis replacement,
non-axisymmetric changes and meridional coupling. Freeze ONE actual
source-compatible parameter tuple and certify those PDE source terms
in physical coordinates. Then prove a compatible correction in
anisotropic norms, including global pressure, axis regularity,
energy, and terminal noncancellation.

Independent tests:
TerminalCore2026/verify_n1_heat_exterior.py checks the rational
integration-by-parts coefficient identity for 45 exact rational
triples and four separate 45-digit derivative/quad evaluations.
These are supplemental tests, not a substitute for the proof.

STATUS: SOURCE-EXTERIOR LOCAL IDENTITY PROVED; SOURCE-MATCHED
FORCE-FREE GLUING AND FULL LEAN NAVIER-STOKES BLOWUP THEOREM OPEN.
