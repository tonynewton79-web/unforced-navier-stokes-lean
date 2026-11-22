# Attack 95 — source-curl obstruction and explicit compact shear repair

**Tony Newton · 22 November 2026**  
**State: KINEMATIC_REPAIR_CONSTRUCTED / SOURCE_CURL_HOLD.**  
Full unforced Navier–Stokes finite-time blow-up and an end-to-end Lean PDE proof remain OPEN.

## Reopened original sources

- Tony Newton, 122-page Case 006 (original SHA-256 `56ff24696ac58bef19bcf339d297d3af8b0401e46d5e8125c7fb1d054f01a758`), §9.3.3 equations (199)-(210), §9.4.1 equations (250)-(252), Proposition 9.20 (255)-(257).
- OpenAI, *Finite Time Blowup for Navier–Stokes* (a **forced** theorem), Appendix B.5-B.6, B.22 and B.26, Lemma B.4, Proposition B.5: https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf

The original Case006 Bessel comparison yields a≥10 on 6≤Ye≤6.1. On this shell the actual B.26 upstream continuation instead has a_up=kappa0*p1r with 0<a_up<4/5. These are different profiles; importing the Bessel inequality into the B.26 continuation is invalid.

## Theorem 95.1 — meridional pressure-curl obstruction

Let two smooth **axisymmetric** viscous flows on a cylindrical chart have the SAME meridional velocities (ur,uz), but possibly different physical swirl utheta and tilde utheta, pressures and forces. The differences of their radial and axial momentum equations are

    ∂r δp = δfr + [tilde utheta² - utheta²]/r
    ∂z δp = δfz.

Eliminating pressure exactly:

    ∂z δfr - ∂r δfz = -∂z[(tilde utheta²-utheta²)/r].     (95.1)

If δfr=δfz=0, the difference of squared swirl is independent of z on each radial column. If the swirl increment is compact in z, that difference is zero everywhere; a sign-preserving replacement is therefore **identical to the original swirl**. No nonzero compact pure-toroidal repair can keep both meridional velocity and meridional forcing unchanged, even when pressure is allowed to change.

This is a conditional source-preservation no-go, not an exclusion of coupled toroidal/poloidal reconstruction or helical alternatives.

If δQ=[tilde utheta²-utheta²]/r differs by Qstar between two axial levels separated by Δz, (95.1) also forces the meridional source-curl sup to be at least |Qstar|/Δz. For fixed anisotropic self-similar amplitude utheta=q^(-1/2-h) F(r/sqrt(q), z/q^(1/2-h)), a nonzero compact fixed-profile swirl change forces a source-curl lower scale c*q^(-2-h). Pressure-only changes cannot repair this curl because curl(grad p)=0.

## Theorem 95.2 — explicit compact kinematic shear replacement

Choose a smooth step Theta flat at 0 and 1. On positive s put
- beta_plus(s)=Theta((s-5.9)/0.1)*Theta((6.2-s)/0.1), which is 1 on 6≤s≤6.1 and 0 outside (5.9,6.2).
- beta_minus(s) any nonzero nonnegative smooth bump supported in (6.4,6.8).
- c_beta=(integral beta_plus(s)ds/s)/(integral beta_minus(s)ds/s)>0; beta=beta_plus-c_beta beta_minus.
- S(s)=integral_0^s beta(v)dv/v. Thus S=0 outside (5.9,6.8).
- zeta(eta) smooth, =1 on I_j=[-j/7,-j/9], and compactly supported in a slightly larger source chart.

Put Ye=chi(eta)*Lambda_c*r²/(2q) and

    m(Ye,eta)=exp[-5 zeta(eta) S(Ye)];
    F_new(Ye,eta)=m(Ye,eta)*F_up(Ye,eta).

Because r∂r Ye=2Ye, the modified angular logarithmic shear is

    a_new = a_up +10*zeta(eta)*beta(Ye).

On I_j×[6,6.1], a_new=a_up+10>10. The multiplier is exactly one outside its compact annulus, remains positive, and defines an exactly divergence-free pure-swirl increment that is C4-equivariant when localized within a torus chart. The exact amplitude ratio is

    m(6.1)/m(6)=(60/61)^5=777600000/844596301≈0.92067654,

a relative change of 7.932346% across the thin shell. This repairs **only kinematics** and is not an actual solution of either PDE. By Theorem 95.1 its meridional source/velocity must be altered.

## Proposition 95.3 — conditional two-moment neutralization

Use precisely Case006 equation (250):

    M_i(eta)=integral R² tau_i(R,eta) dR
    N_i(eta)=integral R² G(R,eta) tau_i(R,eta) dR.

For the shell repair tau0 and auxiliary radial bumps tau1,tau2, suppose the actual physical moment determinant det=M1*N2-M2*N1 is nonzero. Then with

    c1=(M2*N0-N2*M0)/det;
    c2=(N1*M0-M1*N0)/det,

the composite tau=tau0+c1*tau1+c2*tau2 has M=N=0 identically. Equation (251) then makes its integrated toroidal slice torque vanish, including its axial-viscous term. The physical determinant, source support, radial shaper norms and stress-cone compatibility remain NOT certified. Integrated zero torque does **not** imply the pointwise source-curl compatibility nor positive seven-ray cone.

## Theorem 95.4 — ninth-jet cost of a fixed self-similar shape

Let q=T-t, D=1/2-h, gamma=1/2+h, and a nonzero smooth compact vector profile Phi(X,Y,Z). On a torus chart set

    v_q=q^(-gamma) Phi(x/sqrt(q),y/sqrt(q),z/q^D).

Exact change of variables gives

    ||∂x^9 v_q||_2 = c0 q^(-17/4-3h/2), c0>0.

The linear heat residual satisfies

    ||∂x^9(∂t-nu*Delta)v_q||_2
       = q^(-21/4-3h/2)(c1+O(q^(2h))), c1>0.

The positive coefficient follows from the maximum principle applied to
L Phi=gamma Phi+(X∂X+Y∂Y)Phi/2+D Z∂Z Phi-nu Delta_(X,Y)Phi,
and compact support implies ∂X^9 L Phi is nonzero.

**This is a raw linear heat-source theorem, NOT a lower bound on the FULL nonlinear PDE residual after cancellation.** The actual fixed-shape assumption and all nine-jet compensator bounds must be checked before applying it to Case006.

## Final outstanding research gates

1. Construct a coupled toroidal-poloidal source alteration whose meridional source-curl equals (95.1) on the original support, with exact periodic pressure and full four-patch cross interactions.
2. Verify the physical auxiliary moment determinant uniformly on one admissible I_j; build the M=N=0 compensators without destroying the target shear.
3. Certify positive cone coefficients at **every point**, rather than only slice-integrated torque.
4. Prove raw ninth-jet losses cancel in the actual **nonlinear** residual, with source-native cutoff widths and moving frames.
5. Establish physical nine-block M_terminal, rho(M_terminal)<1, and retention of the original terminal trace.

No such physical completion is contained in the current Attack95 paper. Python exact rational regressions and Lean finite algebra are NOT a Navier–Stokes PDE proof.
