# Attack 99 — a nonseparable toroidal cross-flux right inverse in the exact source shaper class

**Tony Newton | 22 November 2026**  
**Status:** APPENDIX_AD_COUPLED_ANGULAR_MARGINALS_MATCHED__ACTUAL_CASE006_SOURCE_OPEN.  
**No unforced 3D Navier–Stokes singularity theorem. No complete seven-ray H8 inverse. No claim of external priority.**

## Directly reopened, hash-checked sources

- Original 122-page Case006, SHA-256 `56ff24696ac58bef19bcf339d297d3af8b0401e46d5e8125c7fb1d054f01a758`, especially toroidal Eq. (193), streamfunction Eq. (194), torque moments (250)–(252), source cone (258)–(273), and Appendix AD (1)–(8).
- Twelve-page H8 cone source, SHA-256 `10d70e2f2820980ce471411079e3a06b7f05550aa54cf5dc1c29844d3339a826`.
- Preceding Attack98 branch: `feature/attack98-angular-flux-full-diagnostic-20261122`.

Original Remark 9.23 deliberately leaves the **actual** four-patch physical shapers/cutoffs and source representative unfrozen. The object treated below is a **new fully specified toroidal extension of the source's Appendix AD diagnostic**, not that original global physical preparation.

## Definitions of the one shared diagnostic field

Let `b(s)=Z^{-1}exp[-1/(1-s²)]` for |s|<1 and 0 outside, where `Z=int_-1^1 exp[-1/(1-s²)]ds`. Set x=r-2, z in (-1,1), r in (1,3); `mu=1/2,lambda=-1/2,K1=K2=ell=c=1` and

    a(x)=2+x/2,  d(x)=-(1+x/2)/2,  p(x)=b'(x)/b(x)=-2x/(1-x²)².
    Psi(r,z)=b(x)*(a(x)+d(x)z)*b(z),
    P_r=-Psi_z/r,     P_z=Psi_r/r,    P_theta=0.
    rho(r,z)=rho0*b(x)^2*b(z)^2/r², rho0=1229/4443.

The exact original source cone centre `R*=b* tensor b* - I/3` has

    alpha=R*_(rz)=-4443/9832,
    beta=R*_(rtheta)=-147 sqrt(182)/9832 -21 sqrt(2)/2458,   beta<0,
    gamma=R*_(thetaz)=147 sqrt(182)/9832 -21 sqrt(2)/2458, gamma>0.

Define `I0=int b(z)^2 dz>0`, `I2=int z² b² dz>0`, `L0=int b'(z)² dz>0`, `L2=int z² b'(z)² dz>0`. The original Appendix AD already proves `int P_r P_z dz=alpha Rbar`, where `Rbar=rho0*I0*b(x)²/r²`. The axial boundary defect q and axial primitive J vanish for the compact diagnostic, provided the swirl has no r/z component.

## Theorem 99.1 — exact two-angular-flux toroidal inverse

For each x in (-1,1), define two smooth functions of z:

    u_x(z)=-partial_z[(a+d*z)b(z)],
    v_x(z)=[p(x)*(a+d*z)+a'(x)+d'(x)*z]*b(z).

Then `P_r=(b(x)/r) u_x` and `P_z=(b(x)/r) v_x`.

Let the two-by-two Gram matrix `G_ij=int (u_x,v_x)_i (u_x,v_x)_j dz`. Direct integration by parts gives **exactly**

    G11=a² L0 +d² L2,
    G12=(I0/2)(a*d'-d*a')=-I0/8,
    G22=I0*(p*a+1/2)^2 + I2*(p*d-1/4)^2.

Its determinant `Delta=G11 G22-G12²` is strictly positive for every -1<x<1. Define

    c1=(beta G22-gamma G12)/Delta,
    c2=(gamma G11-beta G12)/Delta,

and the *nonseparable*, source-allowed compact toroidal velocity

    Theta(r,z) = (rho0*I0*b(x)/r)*(c1(x)u_x(z)+c2(x)v_x(z)).

Then **at every radius** in (1,3),

    int P_r Theta dz = beta * Rbar(r)  <0,
    int P_z Theta dz = gamma* Rbar(r)  >0.

Take the complete diagnostic velocity `U=P+Theta e_theta`, and choose `T=U tensor U`, the **same** rho, `p0=0`, `S=T-rho R*`, `f=div S`. The streamfunction field is unchanged, so the five axial/angular marginals are now

    Tcal=alpha Rbar; Rcal=Rbar>0; q=0; J=0;
    Bbar_can=int S_(thetaz) dz=0;
    Cbar_can=int S_(rtheta) dz=0.

Thus the *entire integrated Appendix AC axial and angular source screen* has zero defect, rather than merely passing the scalar axial test. At each r the true negative rtheta stress lies between -0.214 Rbar and -0.213 Rbar; the true positive theta-z stress lies between 0.189 Rbar and 0.190 Rbar.

This statement is an exact, fully source-class diagnostic construction. It is NOT the original four-patch source and does NOT certify the pointwise cone or the original toroidal slice moments (250).

## Proposition 99.2 — explicit uniform Gram coercivity and smooth compactness

Set

    d1=L0-I0²/(4I2)>0,
    d2=L2-I0/4>0.

Both are strictly positive by Cauchy–Schwarz applied to `int z b'b=-I0/2`; equality would make b a noncompact Gaussian-type or power-law profile, contradicting its flat endpoints. The component of u_x orthogonal to V=span{b,zb} has squared norm `a²d1+d²d2`, while v_x lies in V. Since

    a*d'-d*a'=-1/4,

the distance of v_x from the span of `(a+d z)b` obeys

    ||v_x||² >= I0*I2/[16*(a² I0+d² I2)].

Consequently, for all interior x,

    Delta >= (a²d1+d²d2)*I0*I2/[16*(a²I0+d²I2)]
          >= ((9/4)d1+(1/16)d2)*I0*I2/
             [16*((25/4)I0+(9/16)I2)] =: delta_* >0.

The radial logarithmic derivative p(x) has only rational endpoint poles, while G11, G12, G22 and the inverse coefficients are rational functions of p(x) whose common denominator is strictly positive and grows quadratically for |p|→infinity. They extend smoothly as x→±1. Multiplication by the flat radial bump b(x) produces a Cc-infinity toroidal field. The axial profiles are flat at z=±1.

## Theorem 99.3 — a single separable toroidal shaper CANNOT solve both flux targets

Suppose `Theta=F(x)H(z)` and both equalities in Theorem 99.1 hold at every radius with Rbar>0. Because beta,gamma are nonzero, the ratio of the two axial overlaps is the fixed constant gamma/beta. Put

    h0=int b H, h1=int z b H,
    j0=int b' H, j1=int (zb)' H.

The flux ratio forces the rational identity

    p(x)*(a h0+d h1)+a' h0+d' h1
     =-(gamma/beta)*(a j0+d j1).

Since `p(x)=-2x/(1-x²)^2` has second-order poles at BOTH x endpoints, the affine polynomial `a h0+d h1` must vanish at both endpoints (indeed to second order), so h0=h1=0 because a and d are independent affine functions. The remaining identity forces j0=j1=0. Then both flux integrals vanish, contradicting the nonzero targets. Thus nonseparability is essential for exact simultaneous marginal matching in this flat diagnostic.

The attached verifier independently checks the polynomial identity has rank 4 and tests a nonsingular two-profile Gram inverse in 12,000 exact rational cases.

## Proposition 99.4 — the naive pointwise stress lift still fails at flat axial edges

Although `int S_(rtheta)dz=int S_(thetaz)dz=0`, the CANONICAL local angular correction `C_can=S_(rtheta)=P_r Theta-beta*rho` is not bounded by a constant times rho. Indeed `p_z=b'(z)/b(z)=-2z/(1-z²)^2`, and for any x where c1(x)≠0,

    C_can/rho = I0*(u_x/b(z))*
                    [c1*(u_x/b(z))+c2*(v_x/b(z))]-beta,

whose leading term at z→±1 is `I0*c1*(a+d*z)^2 p_z^2`. This diverges. Such x exist near either radial boundary because `c1(x)→beta/G11(x)≠0` as x→±1. Thus **the canonical tensor S=T-rho R*** fails the pointwise original H8 C/rho cap. Other divergence-equivalent tensors may redistribute the stress; no full weighted inverse impossibility follows.

## What Attack99 does NOT solve

- The actual original Case006 core and off-axis Pi0/E jets, final normalized poloidal/toroidal shapers, four localized C4 patch maps and all twelve ordered mixed stresses were NOT frozen.
- The torque-neutral source moments M,N from (250), time derivatives, viscous angular actuator (251), pressure and global force-curl compatibility are NOT satisfied merely by the flux identities.
- The full Appendix Y moving-frame dual, original fixed rho and positive pointwise seven-ray margin, a smooth weighted inverse, nine-jet and terminal coupling matrix remain OPEN.

This is a source-native **positive control at the entire angular marginal level** plus a separability no-go and canonical-flat-boundary warning, not a solution of an unforced Navier–Stokes PDE. Main is unchanged.
