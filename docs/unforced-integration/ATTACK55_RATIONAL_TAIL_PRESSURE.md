# Attack 55 — a non-Gaussian 1/r profile seed, full nonlinear pressure, and exact closure obstruction

**Date:** 21 November 2026. **Status:** exact analytic-PDE nonexample, verified in independent symbolic representations. **No nonzero exact singular profile; no Lean certificate; no unforced finite-time blow-up theorem.**

## Constructed divergence-free seed

In cylindrical coordinates r,z and similarity time s, H=1+r²+z², use arbitrary C¹ amplitudes a(s), b(s):

    W_r=b*r*z/H^(3/2);
    W_theta=a*r/H;
    W_z=b*(2+r²+2z²)/H^(3/2).

Its poloidal streamfunction is psi=b*r²/sqrt(H), so divergence is identically zero. In Cartesian form,

    W= a*(-y,x,0)/H + b*(xz,yz,2+x²+y²+2z²)/H^(3/2).

The field is globally smooth with |∇^j W|=O((1+|y|)^(-1-j)) for j<=2. Its nonzero critical tail is

    W=(1/R)[2b cos(theta) e_R - b sin(theta) e_theta + a sin(theta) e_phi]+O(R^-3).

Thus the seed meets smoothness, solenoidality, spatial decay, and (when a,b are periodic) the *twisted* periodicity hypothesis with identity isometry. It has infinite spatial L² energy, like a bare self-similar critical-tail profile; physical finite-energy data would require separate localized matching.

## The actual nonlinear Poisson pressure, uniquely decaying

Write R=|y|, mu=z/R, P2(mu)=(3mu²-1)/2. For the full equation

    ∂s W+1/2(W+y·∇W)-ΔW+(W·∇)W+∇q=0

the pressure must satisfy -Δq=∂iWj ∂jWi. The exact source is

    S=a²[A0(R)+A2(R)P2(mu)] + b²[B0(R)+B2(R)P2(mu)],

    A0=2(R²-3)/[3(1+R²)^3],
    A2=-8R²/[3(1+R²)^3],
    B0=2R²(R²-5)/[3(1+R²)^4],
    B2=4R²(4R²+7)/[3(1+R²)^4].

No mixed ab term appears in S; the mixed angular advection remains in the PDE.

The exact unique decaying solution is

    q=a²[q0a+q2a P2(mu)]+b²[q0b+q2b P2(mu)],

    q0a= -1/[3(1+R²)],
    q0b= -(2R²+1)/[6(1+R²)²],
    q2a= [(1+R²)atan(R)-R-(2/3)R³]/[R³(1+R²)],
    q2b= [16R^5+35R³+21R-21(R^4+2R²+1)atan(R)]/[12R³(1+R²)²].

All apparent R=0 singularities are removable:
q2a=-2R²/15+O(R^4), q2b=2R²/5+O(R^4).
Therefore q(s,0)=-a(s)²/3-b(s)²/6 and grad q(s,0)=0.

Independent radial equations verified *exactly* for l=0,2:

    q_l''+2/R*q_l'-l(l+1)/R²*q_l=-S_l.

An independent Cartesian gradient-square computation agrees at three nontrivial exact points. For a=b=1, q(0)=-1/2 and q(R=1,mu=0)=-5/8+3pi/32.

## Theorem 55: the pressure-complete rational seed cannot close the unforced PDE

On z=0, W_r=0, ∂zW_theta=0 and q is axisymmetric. Thus the full theta residual, including the genuinely nonlinear convection, simplifies to

    N_theta(s,r,0)= r/(1+r²)*a'(s)+r(11+3r²)/(1+r²)^3*a(s).

Exact N=0 for all r>0 forces a'=0 by r→∞ and then a=0 at r=1.

At y=0, the full axial residual is

    N_z(s,0)=2b'(s)+11b(s),

because W_z(s,0)=2b, ΔW_z(s,0)=-10b,
(W·∇)W_z(s,0)=0 and ∂zq(s,0)=0.

Along the positive z axis at spatial infinity, ∂sW_z=2b'(s)/sqrt(1+z²), while linear drift, diffusion, nonlinear convection and the explicitly solved pressure gradient are O(z^-3). Multiplying the axial PDE by z and taking z→∞ gives b'=0, hence b=0.

This proves a=b=0 **without assuming temporal periodicity**. The nonzero member a=b=1 has exact axial PDE residual 11 at the origin and physical speed 2 there, so it is not an a posteriori small-error certificate.

## Actual completion targets and release discipline

A valid singularity construction now requires a much richer core with time-dependent spatial shapes, exact pressure from -Δq=∂iWj∂jWi, and a validated inverse of the *full* non-selfadjoint linearized operator on the critical-tail space. The standard inverse-bilinear test 4M²Kδ<1 is meaningful only after proving the inverse norm M, nonlinearity constant K, residual δ in their respective physical function spaces, compatibility/gauge, and nonzero separation. None is supplied by the present seed.

The external Alpöge–Buckmaster formal interface includes 15 named CellSystemCondition fields (see Attack53). Its announced numerical interval certificate and validator were not available at the authors' public GitHub repository at the time of this check. These data cannot be invented or inferred from the conditional Lean proof.

Originality versus Nečas–Růžička–Šverák (1996), Tsai (1998), and recent 2026 claimed constructions remains unverified. The user-session four-page manuscript includes a meridional-streamfunction/pressure contour figure and complete symbolic verifier.

**Release status: ANALYTIC RATIONAL-ANSATZ EXCLUSION; EXACT PRESSURE; GENUINE PROFILE EXISTENCE OPEN; LEAN CONTINUUM THEOREM OPEN.**
