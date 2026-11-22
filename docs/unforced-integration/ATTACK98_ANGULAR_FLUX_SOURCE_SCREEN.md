# Attack 98 — exact angular-flux obstruction for the frozen Appendix AD diagnostic

**22 November 2026, Tony Newton**  
**Status:** COMPLETE_APPENDIX_AD_DIAGNOSTIC_REFUSED_BY_ANGULAR_ONE_SIDED_CONE__ORIGINAL_SOURCE_UNFROZEN.  
**No unforced Navier–Stokes blow-up proof or original H8 source failure is asserted.**

## Source reopening and scope

Original 122-page Case006 SHA-256 `56ff24696ac58bef19bcf339d297d3af8b0401e46d5e8125c7fb1d054f01a758`. Original H8 twelve-page PDF SHA-256 `10d70e2f2820980ce471411079e3a06b7f05550aa54cf5dc1c29844d3339a826`. Read Case006 (258)-(273), Remark 9.23, Appendices AC and AD, and H8 *Fourfold Solenoidal Detectors* Section 3.1-3.2.

The source explicitly does NOT freeze its final physical (original) shapers, cutoff, four-patch mixed stress, rho or pressure. Its Appendix AD has a fully specified **mathematical diagnostic**, which is the only source object evaluated below. The actual original physical H8 source is still NOT TESTABLE.

## One entire, consistent AD diagnostic on one common chart

On 1<r<3 and -1<z<1 define `b(s)=Z^{-1}exp[-1/(1-s²)]` for |s|<1, zero otherwise, `Z=int_-1^1 exp[-1/(1-s²)] ds`, `N2=int_-1^1 b²`. Freeze all of:

- `K1=K2=ell=c=1, mu=1/2, lambda=-1/2`;
- `Phi1=b(r-2), Phi2=(1+(r-2)/2)b(r-2)`;
- `Xi1=b(z), Xi2=(1-z/2)b(z)`;
- `Psi=Phi1 Xi1+Phi2 Xi2, P_r=-Psi_z/r, P_z=Psi_r/r, P_theta=0`;
- `T=P tensor P, p0=0, rho=(1229/4443)*b(r-2)^2*b(z)^2/r²`;
- `K=rho R*, S=T-K, f=div S+grad p0`, with the fixed **physical** (r,theta,z) R* of Case006 (258)-(265).

Let alpha=R*_(rz)=-4443/9832, beta=R*_(rtheta), gamma=R*_(thetaz). Define the source moments

    Tcal(r)=int_-1^1 T_rz dz,
    Rcal(r)=int_-1^1 rho dz,
    q(r)=[S_zz+p0]_{z=-1}^{z=1},
    J(r)=(1/r) int_1^r s (int_-1^1 f_z(s,z) dz) ds.

The exact Wronskian/axial-overlap formulas yield

    Rcal(r)=(1229/4443)*N2*b(r-2)^2/r² >0 on 1<r<3,
    Tcal(r)=alpha*Rcal(r),  q(r)=0,  J(r)=0.

This **passes the original scalar axial AC test** with maximal reserve. A rigorous absolute rational enclosure (not a numerical quadrature heuristic) is

    1229/1079649 < Rcal(r) < 117984/72569, for 7/4 <= r <= 9/4.

Proof uses Z in [exp(-4/3),2 exp(-1)], N2 in [exp(-2/3)/4,2 exp(2/3)], the analogous b(r-2)^2 bounds, and 2<e<3. The exact ratios are far more useful than the coarse absolute enclosure.

## Original fixed physical cone centre and source's *angular* data

From the original frame b*=(35 e1+2 e2)/sqrt(1229),

    beta=-147 sqrt(182)/9832-21 sqrt(2)/2458,
    gamma=147 sqrt(182)/9832-21 sqrt(2)/2458.

The frozen diagnostic has T_(rtheta)=T_(thetaz)=0, so S_(rtheta)=-beta*rho, S_(thetaz)=-gamma*rho. The canonical angular source lift H_ang has

    C_can=-beta*rho, B_can=-gamma*rho,
    Cbar_can=-beta Rcal, Bbar_can=-gamma Rcal.

Rigorous tight rational enclosures:
`213/1000 < -beta < 214/1000`, `189/1000 < gamma < 190/1000`. Importantly, Bbar for an arbitrary alternative compact inverse is NOT fixed: the source determines its *angular divergence*, not its internal B.

## Theorem — NO compact source-matching cone correction for this diagnostic

Let H=[[-D,C,A],[C,0,B],[A,B,D]] be any smooth compact correction satisfying `div H+grad p=div(T-rho R*)` on the annular cylinder. Angular-average the physical theta equation and integrate across z. Since the axial B traces and p angular mean vanish, and all tensors vanish at the inner radial collar, the exact cylindrical identity forces for EVERY alternative correction

    Cbar(r):=int_-1^1 <C>_theta dz = -beta Rcal(r).

The original *absolute* H8 cap enforces `|C|<=g*rho/2`, `g=15971/122900`.
More decisively, the **larger original one-sided seven-ray floors** (H8 Section 3.1) impose

    -g*rho <= C <= (g+k)*rho/2, k=22371/122900.

Hence every one-sided feasible correction must obey

    Cbar <= ((g+k)/2)*Rcal = (19171/122900)*Rcal.

But the exact radical inequalities sqrt(91/200)>2/3, sqrt(2)>7/5 yield

    -beta > 2597/12290 = 25970/122900 > 19171/122900.

Since Rcal>0 in the support, **contradiction**. The AD diagnostic cannot satisfy even the full original one-sided ray floors, not merely the conservative absolute budget. This obstruction is **independent of the AD axial asymmetry lambda**, so applies to all purely poloidal AD profiles with the same positive rho, centre R* and compact traces. It is not a contradiction for the original physically unfrozen C4 construction, which may possess nonzero toroidal cross-stress or boundary terms.

## Corollary — mandatory *physical* toroidal-radial stress

For ANY future fully frozen physical source with the same original fixed centre R* and vanishing angular/axial endcap defects, write Ucal(r)=int <T_(rtheta)> dz. The same angular flux identity forces `Cbar=Ucal-beta*Rcal`, so one-sided cone feasibility requires

    Ucal/Rcal <= beta+(g+k)/2 < -6799/122900.

Under the narrower absolute cap the required amount is `Ucal/Rcal< -35969/245800`. These are genuine quantitative **source-freeze targets** for coupled toroidal–poloidal preparation; they are not measured values of the original source. With nonvanishing boundary flux, keep the complete angular endcap and radial-trace terms before applying this screen.

## Five-field freeze accounting and release holds

This one frozen diagnostic computes Tcal, Rcal, q, J and the **canonical** Bcal exactly, plus the inverse-independent forced Ccal. An arbitrary H8 inverse's Bcal is not determined by source data, and the genuine original physical Case006 does not specify a unique source tuple. Neither its four localized maps nor its 12 overlap tensors, complete pressure, final envelope, nine-jet bounds, compact weighted inverse, terminal matrix or singular trace is certified.

Run `python research/attack98/verify_attack98.py`. A finite exact verification or Lean algebra declaration certifies ONLY the stated rational identities. Do not promote the failure of the AD diagnostic into failure of the full original Case006 or success on the Navier–Stokes Millennium problem.
