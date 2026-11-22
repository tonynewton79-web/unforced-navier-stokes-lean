# Attack 101 — axial-interior toroidal repair and a flux–torque moment obstruction

**Tony Newton · 22 November 2026**  
**Release:** `AXIAL_INTERIOR_FLUX_REPAIR__AFFINE_TORQUE_NO_GO__PHYSICAL_G_HOLD`.

**Unforced 3D Navier–Stokes theorem: OPEN. Actual original Case006 four-patch source and physical torque weight: UNFROZEN.**

## Source provenance

Reopened, checked originals: 122-page *Carrier-Independent Structured Stress Route, Case 006*, SHA-256 `56ff24696ac58bef19bcf339d297d3af8b0401e46d5e8125c7fb1d054f01a758`, especially (193)–(194), (250)–(252), Appendix AD; 12-page H8 source SHA-256 `10d70e2f2820980ce471411079e3a06b7f05550aa54cf5dc1c29844d3339a826`. Parent branch Attack100 proves a weighted angular no-go for the **unchanged** Attack99 flat-axial-edge shaper.

## Theorem A — remove the specific squared axial-logarithmic-derivative source

Freeze the original Appendix AD diagnostic on 1<r<3, -1<z<1 with x=r-2, b(s)=Z^{-1}exp[-1/(1-s²)], normalized by int b=1, rho0=1229/4443, I0=int b(z)² dz, rho=rho0 b(x)²b(z)²/r². Set

    A(x)=2+x/2=1+r/2; D(x)=-(1+x/2)/2=-r/4;
    h(x,z)=A+D*z; p(x)=b'(x)/b(x);
    u_x(z)=-partial_z[h(x,z)*b(z)];
    v_x(z)=(p*h+partial_x h)*b(z);
    P_r=b(x)*u_x/r; P_z=b(x)*v_x/r.

Original centre signed flux targets are beta=(R*)_(r theta)<0 and gamma=(R*)_(theta z)>0.

Choose E(t)=exp(-1/t) for t>0 and 0 otherwise, and the explicit smooth even cut-off

    chi(z)=E(1/4-z²)/(E(1/4-z²)+E(z²-1/16)).

Then chi=1 on |z|<=1/4 and chi=0 on |z|>=1/2. For each x form

    G11=int chi u_x² dz;
    G12=int chi u_x v_x dz;
    G22=int chi v_x² dz;
    Delta=G11*G22-G12².

**Exact analytic assertion:** Delta>0 uniformly in -1<x<1; indeed Delta/p² tends to a *strictly positive* Gram determinant of (-partial_z(hb),hb) at each radial endpoint. On the inner interval chi=1, u/b is rational with uncancelled double poles at z=±1, whereas v/b is affine; they cannot be proportional. v is not identically zero because A D'-D A'=-1/4. The endpoint Gram limit is strictly positive since -partial_z(hb) and hb are not proportional. Therefore the inverse coefficients below extend smoothly after multiplication by the flat radial bump.

    d1=(beta*G22-gamma*G12)/Delta;
    d2=(gamma*G11-beta*G12)/Delta;
    Theta_chi=(rho0*I0*b(x)/r)*chi(z)*(d1*u_x+d2*v_x).

Then Theta_chi belongs to C_c^infinity on the open annulus and satisfies at EVERY r:

    int P_r*Theta_chi dz=beta*Rbar(r);
    int P_z*Theta_chi dz=gamma*Rbar(r);
    Rbar=rho0*I0*b(x)²/r².

Theta_chi is exactly zero in an open collar near z=±1. Thus the former Attack100 axial w(z)² leading source term with w=b'/b is absent there. **Not proved:** its *radial* flat-edge weighted angular inverse, pointwise H8 cone, full source matching or torque moments.

## Theorem B — an additional, basis-independent flux–torque obstruction

For ANY smooth compact Theta satisfying the FIRST rtheta flux target above (not just Theta_chi), define

    M2(z)=int_1^3 r² Theta(r,z) dr;
    M3(z)=int_1^3 r³ Theta(r,z) dr;
    qb(z)=((2-z)*b'(z)-b(z))/4.

Using A=1+r/2, D=-r/4 and int_1^3 r*b(r-2)dr=2 gives the exact identity

    int b'(z)*M2(z) dz + int qb(z)*M3(z) dz
      = -2*beta*rho0*I0 > 0.        (101.1)

Proof: substitute P_r=-(b(x)/r)[A b'+D(zb)'] into the exact flux equality, cancel b(x)/r in the interior, multiply by r², integrate r, and use the source normalization. No quadrature or asymptotic limit is involved.

In particular, M2=M3=0 is IMPOSSIBLE. If M2=0 then

    ||M3||_L1 >= 2*abs(beta)*rho0*I0/||qb||_Linfty > 0.    (101.2)

This proof uses neither the second angular flux nor the choice of toroidal basis.

## Corollary C — an affine G cannot make both original torque moments vanish

Case006 (250) defines the two physical toroidal torque moments as M=int R² tau and N=int R² G tau. On the normalized Appendix AD chart, suppose the SAME toroidal profile tau=Theta is used and **hypothetically** G(r,z)=g0(z)+g1(z)*r with nonzero g1(z). The conditions M2=0 and N=0 force M3=0, contradicting (101.1). This excludes EVERY toroidal-basis extension for that affine-weight diagnostic, not the original source with an unfrozen, generally nonaffine G(R,eta).

More generally if G=g0+g1 r+e and M2=N=0, then

    abs( int int r² * [qb(z)/g1(z)] * e(r,z)*Theta(r,z) dr dz )
      = 2*abs(beta)*rho0*I0.       (101.3)

Hence the physical deviation e from an affine weight must pay a finite, explicit weighted-toroidal amplitude budget. A failure of this bound would reject THAT frozen physical weight/profile combination. No actual source interval value for G, g1 or e is supplied here.

## Independent reproducibility

A full four-page LaTeX/PDF mathematical proof, exact symbolic verifier and independent stdlib-Fractions verifier are supplied in the ChatGPT artifact packet. The symbolic checker verifies polynomial-cutoff Gram identities at five rational radii with 5,000 exact inversions, source A/D identities and affine torque relations; the independent checker verifies 30,000 exact source–moment examples and normalized radial mass. Polynomial cutoff samples are **diagnostic only**; the smooth C-infinity theorem above is proved analytically and is not inferred from those samples.

## Original source hold

The true physical G(R,eta), same-field torque amplitude normalization, four C4 patch maps and 12 mixed terms, true full pressure and fixed envelope, both actual torque moments, nine-jet source, original H8 one-sided cone, weighted inverse, terminal matrix, retained singular trace and full unforced Navier–Stokes PDE are NOT certified. Do not transplant a static diagnostic affine-G no-go into the unknown physical G. Do not report a solved Millennium problem or a kernel-certified analytic theorem from the finite tests.

**Next target:** Freeze the actual G(R,eta) on the same shaper chart and evaluate (101.3); then search a smooth torque-correcting nullspace of BOTH angular flux functionals that preserves the axial-interior cutoff and addresses the remaining radial flat-edge cone.
