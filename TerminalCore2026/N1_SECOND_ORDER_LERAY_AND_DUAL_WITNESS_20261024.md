# Proof Attack 14 — projected two-step correction and meridional dual witness
Date: 24 October 2026

**STATUS: rigorous source-independent functional-analytic reduction and a
Gaussian positive-control witness. This is NOT a source-matched unforced
terminal correction, a finite-time blowup theorem, or an end-to-end Lean proof.**
No claim of priority is made for the standard Leray–Stokes/Picard machinery.

## A. An explicit second-order projected parametrix

Work on the flat three-torus (alternatively on R^3 with its usual Fourier
Sobolev norms). Fix nu>0, s>5/2 and t0, and take a sufficiently regular,
divergence-free background u_B with complete physical residual

  R_B = partial_t u_B - nu Delta u_B + (u_B dot grad)u_B + grad p_B.

All the following equalities are identities for smooth data; mild solutions
suffice after the usual regularity interpretation. Write P for the Leray
projection, S(t)=exp(nu t Delta) and B(a,b)=P[(a dot grad)b].
Let A = sup_t ||u_B(t)||_(H^s), F=sup_t ||P R_B(t)||_(H^s).

Define the first and second responses with zero initial data:

  w1(t) = - integral_(t0)^t S(t-v) P R_B(v) dv,

  N1(t) = B(u_B,w1)+B(w1,u_B)+B(w1,w1),

  w2(t) = - integral_(t0)^t S(t-v) N1(v) dv.

Then w=w1+w2 is solenoidal and w(t0)=0. Its *projected physical
unforced residual* is exactly

  E2 = B(u_B,w2)+B(w2,u_B)+B(w1,w2)+B(w2,w1)+B(w2,w2).

This follows by expanding the quadratic nonlinearity, using
(partial_t-nu Delta) w1=-P R_B and
(partial_t-nu Delta) w2=-N1. Importantly, it does not assume R_B=0.

The unprojected identity holds with the explicit mean-zero correction pressure

  pi = - Delta^(-1) div [R_B
            + (u_B dot grad)w + (w dot grad)u_B + (w dot grad)w].

The total pressure is p_B+pi. In the periodic case the Poisson source has
zero spatial mean because it is a divergence; choose the mean-zero inverse.
There is **no** arbitrary omission of div R_B.

For the usual inhomogeneous H^s norms, Fourier multiplier calculus gives

  ||integral_(t0)^t S(t-v) g(v) dv||_(C_t H^s)
      <= H_nu(T) ||g||_(C_t H^(s-1)),

  H_nu(T) = T + sqrt(2T/(e nu)),

since sqrt(1+|k|^2) exp(-nu r |k|^2)
<= 1+(2e nu r)^(-1/2).
Choose C_s such that ||B(a,b)||_(H^(s-1))
<= C_s ||a||_(H^s) ||b||_(H^s).
With W1=TF and W2=C_s H_nu(T) (2 A W1+W1^2),

  ||w1||_(C_t H^s) <= W1,
  ||w2||_(C_t H^s) <= W2,
  ||E2||_(C_t H^(s-1)) <= C_s (2 A W2+2 W1 W2+W2^2).

For fixed A,F as T tends to zero, this explicit construction therefore
produces O(T^(3/2)) *upper bounds* on the second-order projected residual.
It does not make E2 exactly zero, does not prove fixed-point continuation to
the singular time, and does not by itself establish that the correction is
asymptotically subleading to the singular carrier.

## B. An explicit meridional, pressure-independent necessary response

This section is on the whole space R^3, not the torus. Consider the smooth
stationary finite-energy Gaussian pure swirl u_B=U(r,z)e_theta with

  U(r,z)=r exp[-(r^2+z^2)].

Its meridional nonlinear residual is
(R_B)_r = -U^2/r = -r exp[-2(r^2+z^2)],
(R_B)_z = 0, modulo any gradient of the background pressure.
The viscous term is azimuthal, hence does not affect the theta-component
of curl R_B. Consequently,

  (curl R_B)_theta = partial_z (R_B)_r - partial_r (R_B)_z
                   = 4 r z exp[-2(r^2+z^2)].

For r in [1/2,1], define chi(r)=(r-1/2)^4(1-r)^4,
and set chi=0 outside. Put psi(r,z)=chi(r)chi(z) and define
Phi=curl(psi e_theta). Since support is away from the axis, Phi is a
compactly supported divergence-free C^2 vector field.

Integration by parts in three dimensions, with measure 2pi r dr dz,
gives the *positive pressure-free pairing*

  <R_B,Phi>
    = <curl R_B, psi e_theta>
    = 8pi integral_[1/2,1]^2
       r^2 z exp[-2(r^2+z^2)] chi(r)chi(z) dr dz
    > pi exp(-4) / (322560)^2 > 0,

using the exact beta integral
integral_(1/2)^1 chi(r) dr = 1/322560,
r^2>=1/4, z>=1/2 and exp[-2(r^2+z^2)]>=exp(-4).
The strict inequality holds on the positive-measure interior.

Therefore any smooth force-free correction w with w(t0)=0, evolving from
this exact Gaussian background, satisfies the *necessary* startup condition

  <partial_t w(t0),Phi> = -<R_B(t0),Phi>
                       < -pi exp(-4)/(322560)^2.

In particular, ||P R_B(t0)||_(L^2)
>= [pi exp(-4)/(322560)^2] / ||Phi||_(L^2) > 0,
and the initial correction must have a nonzero meridional response.
This illustration does not substitute for a source-matched test on the
published forced singular carrier; it is a pressure-independent
positive control and an explicit template for that test.

## C. Why terminal closure remains the main obstruction

If the lower source-leading H^3 scaling from Edition XVIII transfers
to the **complete** chosen background, A(tau) is at least on the order of
tau^[-(5/4+3h/2)]. For terminal slabs T=theta tau, the necessary
smallness of the *sufficient* standard H^3 contraction coefficient
H_nu(T) A(tau) fails: its lower order is
tau^[-(3/4+3h/2)] as tau->0.

This is an obstruction to this isotropic contraction estimate, NOT an
impossibility theorem for alternative anisotropic norms or coupled
correction schemes. The transfer from leading exterior to the final
full background is itself unproved.

## D. Exact next proof obligations

1. Evaluate the full projected first-order residual of the **actual**
   A.11/A.19-corrected source in physical cylindrical/Cartesian coordinates,
   including the collar and both joining regions.
2. Build its genuine coupled meridional/swirl/pressure response, with
   common parameter tuple and correctly matched endpoint data.
3. Prove source-certified interval/cone and norm estimates in anisotropic
   spaces strong enough to continue the correction to t=1.
4. Prove the correction cannot cancel the source-leading H^3 singularity.
5. Formalize the actual function spaces, Leray projection, pressure,
   integrals, and derivative/bootstrapping statements in Lean and give a
   single kernel-checked theorem independent of unproved PDE assumptions.

Reproducible finite audit: verify_n1_second_order_dual.py. The script tests
only the rational cutoff mass, the formal bilinear cancellation, numerical
Gaussian derivative identity, and the scalar bound calculations; analytic
theorems are proved by the mathematics above, not by those finite tests.

RELEASE STATUS: PARTIAL SOURCE-INDEPENDENT EXACT RESULT; FULL UNFORCED
FINITE-TIME SINGULARITY AND END-TO-END LEAN PROOF OPEN.
