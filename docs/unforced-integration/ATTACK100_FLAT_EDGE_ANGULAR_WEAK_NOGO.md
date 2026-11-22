# Attack 100 — exact flat-edge weighted-angular no-go for the Attack 99 diagnostic

**Tony Newton · 22 November 2026**  
**Status:** `AD_ANGULAR_WEIGHTED_WEAK_NO_GO__ORIGINAL_CASE006_HOLD`.  
**No unforced 3D Navier–Stokes singularity theorem.** No authentic 4-patch source freeze. No global H8 inverse.

## Reopened exact sources

- Original 122-page Case006 SHA-256 `56ff24696ac58bef19bcf339d297d3af8b0401e46d5e8125c7fb1d054f01a758`. Read original (193)–(194), (250)–(252), (258)–(273), Appendix AD and **Appendix U** (weighted angular duality), plus Appendix W (flat-boundary limitations).
- Attack99 committed note `ATTACK99_NONSEPARABLE_TOROIDAL_FLUX_INVERSE.md` on parent branch. This source's finite shaper is the object below.
- The original physical Case006 C4 maps, twelve overlap stresses, nine jets, pressure and complete final profile remain **unfrozen**.

## Exact source and its angular divergence

Let `x=r-2`, `z∈(-1,1)`, `b(s)=Z^-1 exp[-1/(1-s²)]` on |s|<1, 0 outside. Put

    A=2+x/2; D=-(1+x/2)/2; h=A+D*z;
    p=b'(x)/b(x); k=p*h+partial_x h;
    u=-partial_z(h*b(z)); v=k*b(z);
    rho=rho0*b(x)^2*b(z)^2/r², rho0=1229/4443.

The poloidal field is `P_r=b(x)u/r`, `P_z=b(x)v/r`. The fixed physical cone-centre angular entries are `beta=R*_(r theta)<0`, `gamma=R*_(theta z)>0`. Define the authentic Appendix AD axial moments I0,I2,L0,L2, and the Attack99 Gram coefficients

    G11=A² L0 +D² L2; G12=-I0/8;
    G22=I0*(p*A+1/2)^2+I2*(p*D-1/4)^2;
    Delta=G11*G22-G12²>0;
    c1=(beta*G22-gamma*G12)/Delta;
    c2=(gamma*G11-beta*G12)/Delta;
    Theta=rho0*I0*b(x)/r*(c1*u+c2*v).

This shaper satisfies both **integrated** angular flux conditions of Attack99 and is C-infinity compact. Set `T=(P+Theta e_theta)⊗(P+Theta e_theta)`, `S=T-rho R*`, `f=div S`, with `p0=0`. Its angular equation (and that of any source-matched angular correction) is

    r²*f_theta = partial_r(r² S_rtheta)+partial_z(r² S_thetaz).

## Theorem 100.1 — the entire source has a nonremovable t^-4 flat-edge component

Put `w(z)=b'(z)/b(z)=-2z/(1-z²)^2`. Let

    R2=c1*h²,
    R1=2*c1*D*h-c2*h*k,
    R0=c1*D²-c2*D*k,
    Z1=-c1*h*k,
    Z0=-c1*D*k+c2*k².

The exact complete angular stress components (including beta/gamma centre) are

    r²*S_rtheta=rho0*I0*b(x)^2*b(z)^2*(R2*w²+R1*w+R0-beta/I0),
    r²*S_thetaz=rho0*I0*b(x)^2*b(z)^2*(Z1*w+Z0-gamma/I0).

Differentiating *both* components gives the exact identity

    r²*f_theta/(rho0*I0*b(x)^2*b(z)^2)
      = c1'(x)*h(x,z)^2*w(z)^2 -c1*h*k*w'(z)
        +P1(x,z)*w(z)+P0(x,z),

where

    P1=(partial_x+2p)R1+partial_z Z1+2Z0-2gamma/I0,
    P0=(partial_x+2p)R0+partial_z Z0-2p beta/I0.

The leading coefficient identity follows from

    (partial_x+2p)R2+2Z1
      = c1'*h²+2*c1*h*(partial_x h)+2p*c1*h²-2*c1*h*k
      = c1'*h²

because `k=p*h+partial_x h`. **This coefficient was exactly verified independently by symbolic algebra and 40,000 rational randomized jet identities.**

Since `G22→infinity` as x→±1 but G11 is finite,

    c1(-1)=beta/G11(-1), c1(+1)=beta/G11(+1),
    G11(+1)-G11(-1)=4L0+L2/2>0.

As beta<0, `c1(+1)>c1(-1)`. Hence there is a compact interior radial interval J and m>0 with c1'≥m there. Also h(x,1)=3/2+x/4≥5/4, while with t=1-z,

    w(z) ~ -1/(2t²),   w'(z) ~ -t^-3.

Thus on J and sufficiently small t, **r² f_theta ≥ const*b(x)²*b(z)²*t^-4 >0**.

## Theorem 100.2 — NO bounded weak weighted angular inverse, even before other H8 components

The original fixed cone (and both absolute/one-sided seven-ray budgets) gives finite constants a,b with `|C|<=a rho`, `|B|<=b rho`. If a source-matched H existed, angularly average it. Appendix U's necessary weighted dual then reads, for every compact smooth test psi,

    |∫∫ r² f_theta psi dr dz|
      <=∫∫ r² rho [a|partial_r psi|+b|partial_z psi|] dr dz.

Choose smooth nonnegative radial phi supported in 2+J and smooth nonnegative axial zeta supported inside (-1,1). For small t put

    z_t=1-t, delta_t=t²/100,
    psi_t(r,z)=phi(r)*zeta((z-z_t)/delta_t).

The flat weight b(z)² is comparable to b(z_t)² on the width delta_t because `|partial_z log b|=O(t^-2)`. The **source** side has lower bound `c*b(z_t)^2*delta_t*t^-4=c*b(z_t)^2*t^-2`. The available weighted **capacity** is bounded by `C*b(z_t)^2*(delta_t+1)`. Dividing by b(z_t)^2 gives a contradiction as t→0. This excludes **all** divergence-equivalent bounded weak angular stresses under the original rho, including every pressure gauge and every smooth full four-field H8 tensor.

The entire proof is for the **Attack99 source diagnostic**. It does not disprove the original unfrozen C4 four-patch preparation, nor any redesigned toroidal shaper/weight. The published weighted dual criterion is classical L1/Linfinity Hahn–Banach duality specialized in the source's Appendix U; no new generic functional-analysis theorem is claimed.

## Proposition 100.3 — the torque moment has four additional exact gates

The first radial moment of the diagnostic toroidal field is `Mhat(z)=∫_1^3 r² Theta(r,z) dr`. Write four constants

    m0=∫_-1^1 (x+2)b(x)[-c1 D+c2(pA+A')]dx,
    m1=∫_-1^1 (x+2)b(x)c2(pD+D')dx,
    n0=∫_-1^1 (x+2)b(x)c1 A dx,
    n1=∫_-1^1 (x+2)b(x)c1 D dx.

Then **exactly**

    Mhat(z)=rho0*I0*b(z)*[m0+m1*z-(n0+n1*z)*w(z)].

Since w(z) has double poles at both endpoints, `Mhat≡0 iff m0=m1=n0=n1=0`. The finite polynomial rank is 4, independently checked. None of these four genuine integrals was measured as zero. The original *second* torque moment `N=∫ R² G tau,dR` additionally requires the real prepared G and similarity chart, which are still missing. No torque-neutrality promotion is made.

Even if those further moments could be cancelled, Theorem 100.2 already excludes the **unchanged** Attack99 shaper from the same fixed-envelope H8 angular equation.

## Scope and next decisive attack

The obstruction is caused by a radially varying coefficient c1'(x) multiplying the squared axial logarithmic derivative near the infinitely flat edge. A replacement toroidal profile must suppress this leading coefficient, alter the envelope with a fully justified source choice, or relocate the correction away from the flat edge. Any replacement must recheck **both** angular fluxes, **both** torque moments, the complete seven-ray cone, the meridional source and the unforced PDE. Do not reuse Attack99's integrated-flux success as a pointwise-cone proof.

Reproduction: `research/attack100/verify_attack100.py`, independent fractions-only verifier, exact finite Lean identities, and the accompanying four-page mathematical paper. The full continuum dual proof is not claimed Lean-certified. All G0–G8 physical NS release gates remain OPEN.
