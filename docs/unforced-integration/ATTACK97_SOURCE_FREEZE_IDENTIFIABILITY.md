# Attack 97 — physical-source freeze gate and exact Appendix AD identifiability theorem

**Date:** 22 November 2026. **Research status:** PHYSICAL_SOURCE_TUPLE_UNFROZEN__EXACT_PROFILE_DISCRIMINATOR. This is **not** a proof of an unforced Navier–Stokes singularity, an original Case 006 H8 source certificate, or a weighted inverse.

## Reopened primary sources

- Original 122-page *Carrier-Independent Structured Stress Route, Case006* (SHA-256 `56ff24696ac58bef19bcf339d297d3af8b0401e46d5e8125c7fb1d054f01a758`), Proposition 9.12, Remark 9.23, eqs. (194), (242), (269)–(273), Appendices Y, AC, AD and AE.
- Original H8 *Fourfold Solenoidal Detectors and Stress Cone Bounds* (SHA-256 `10d70e2f2820980ce471411079e3a06b7f05550aa54cf5dc1c29844d3339a826`).
- The prior Attack 96 branch provides a manufactured coupled control but **not** the authentic prepared physical source.

**Exact source-freeze decision:** Remark 9.23 deliberately leaves the final cutoff, the physical shell shaper profiles and the stress representative unspecified. Appendix AC explicitly requires the *complete* T, rho and boundary/gauge q to evaluate the source-only cone. Consequently no unique original `(f_m,B,C,rho,T,p0,patch_maps)` can be frozen as the actual physical data in this attack. The machine-readable ledger below records nulls instead of substituting the manufactured control.

## Original source-only flux

In the physical cylindrical chart, write `H=[[-D,C,A],[C,0,B],[A,B,D]]` and `C(H)=max(8|B|,2|C|+4|D|,2|A-4B|+4|D|)<=kappa*rho`, with

    alpha=(R*)_{rz}=-4443/9832,   kappa=15971/122900.

For complete full structured stress T, K=rho*R*, S=T-K and force representative f=div S+grad p0, set

    Tbar(r)=integral_c^d mean_theta(T_rz) dz
    Rbar(r)=integral_c^d mean_theta(rho) dz
    q(r)=[mean_theta(S_zz+p0)]_{z=c}^{z=d}
    J(r)=(1/r)*integral_a^r s F_z(s) ds.

Appendix AC (5) gives **exactly**

    J(r)=Tbar(r)-alpha*Rbar(r)-[Tbar(a)-alpha*Rbar(a)]
       +(1/r)*integral_a^r s q(s) ds.

The compact representative with zero boundary traces has `J=Tbar-alpha*Rbar`. Necessary cone marginal tests at **every** r are

    |J|<=kappa*Rbar,
    |Bbar|<=kappa*Rbar/8,
    |J-4Bbar|<=kappa*Rbar/2,

with Bbar the axial integral of the corrected H_theta,z. Passing these is NOT full Appendix Y dual feasibility, let alone the smooth weighted inversion (273).

## Theorem 97.1 — one allowed normalized source family, opposite screen outcomes

Use precisely the Appendix AD (4)–(7) **smooth normalized diagnostic**. Let b(s)=Z^-1 exp[-1/(1-s²)] on |s|<1 and zero outside, `B2=int b²>0`; set

    phi1=b(x), phi2=(1+mu*x)b(x)
    Xi1=b(zeta), Xi2=(1+lambda*zeta)b(zeta)
    x=r/ell-2, zeta=z/c, mu=1/2, -1<lambda<1.

All four shapers are compact C-infinity, nonnegative, and normalized. With positive K1,K2, streamfunctions `Psi_j=K_j phi_j Xi_j` give the original poloidal velocity class. Direct Wronskian and integration by parts give

    phi1*phi2'-phi2*phi1'=mu*b(x)^2,
    integral Xi1'Xi2 dzeta=-lambda*B2/2,
    Tbar_lambda(r)=mu*lambda*K1*K2*B2*b(x)^2/(2*r²*ell).

Fix the **same** Appendix AD flat diagnostic envelope independently of lambda:

    rho_diag=rho0*r^-2*b(x)^2*b(zeta)^2,
    rho0=1229*K1*K2/(4443*c*ell).

For T=P tensor P, p0=0 and the compact source representative, the boundary term q and T(a),R(a) vanish; hence

    Tbar_lambda/Rbar = (4443/4916)*lambda,
    J_lambda/Rbar = (4443/4916)*(lambda+1/2).

Thus the exact original **necessary axial screen** is equivalent to

    -143017/222150 <= lambda <= -79133/222150.

The source-allowed lambda=-1/2 passes **only this marginal test**. The equally normalized choices lambda=0 and lambda=+1/2 **fail** it. For lambda=+1/2, `|J|/(kappa*Rbar)=111075/15971 > 6.95`. The unmeasured final shaper selection is therefore a mathematically substantive choice and cannot be frozen from the supplied source by inference.

## Theorem 97.2 — sharp integrated angular allocation

For any real J,

    inf_b max(8|b|, 2|J-4b|) = |J|

with the minimizer b=J/8. Proof: if m is the maximum, `|J|<=4|b|+|J-4b|<=m`; equality at J/8. Therefore freely allocating the integrated angular stress B cannot weaken `|J|<=kappa*Rbar`. If the actual `Bbar=0` is **prescribed**, the admissible diagnostic lambda interval is instead

    -63523/111075 <= lambda <= -47552/111075.

These are radial marginal budgets, NOT constructions of a divergence-matched B,C or a positive seven-ray margin.

## Corollary 97.3 — mandatory cancellation of a physically omitted remainder

Write full `Tbar=Tbar_lambda+Tbar_rest` and retain q and the inner radial trace. Define

    E(r)=Tbar_rest(r)-[Tbar(a)-alpha*Rbar(a)]
         +(1/r)*integral_a^r s*q(s) ds.

Then the exact source-only identity becomes

    J/Rbar=(4443/4916)*(lambda+1/2)+E/Rbar.

If the original H8 cone is feasible, necessarily on every radius with Rbar>0,

    |E|/Rbar >= ( (4443/4916)*abs(lambda+1/2)-kappa )_+.

For lambda=+1/2 the necessary remainder magnitude is at least `23776/30725` times Rbar; for lambda=0 it is at least `79133/245800` times Rbar. They are **requirements**, not measured remainder values. Without source-certified bounds on core×shaper terms, the complete four-patch overlap stresses, and boundary/gauge q, no physical PASS or FAIL follows.

## Independent envelope-orientation theorem

When the exact compact representative has q=0 and zero inner radial traces,

    (alpha-kappa)*Rbar <= Tbar <= (alpha+kappa)*Rbar.

Both endpoints are negative, since `alpha+kappa=-79133/245800<0`. Consequently **any actual complete compact representative with Tbar>=0 at a radius where Rbar>0 is excluded**, regardless of the size of the nonnegative envelope. This statement does **not** apply if pressure or axial boundary terms are unknown.

## Release-critical next source freeze

Specify on one shared physical patch: final nonnegative smooth `rho` normalized by original virial data, actual Case006 core continuation and Pi0 pressure, toroidal/poloidal shapers, all 4 localized patch maps and all 12 cross terms, complete symmetric T, physically selected p0, and the resulting f_m,B,C and q. Evaluate Tbar,Rbar,J,Bbar and full Appendix Y dual integrals with validated intervals and flat boundary tails. Only then attempt the compact weighted inverse with strict reserve. Do not use the adapted Attack96 envelope or the Appendix AD diagnostic as if they are the actual prepared physical source.

**Verification:** `python research/attack97/verify_attack97.py` — exact Wronskian and overlap, 30,000 sharp polar trials, 15,000 remainder gates, 10,000 sign comparisons. This is finite algebra, not complete Lean or PDE certification. Main remains unchanged.
