# Attack 97 — physical source-freeze contract and known exact-core leading cross term

**Source-reopened status:** PHYSICAL_SOURCE_TUPLE_UNFROZEN. Do not replace missing authentic source fields with the Appendix AD diagnostic or the manufactured Attack 96 control.

## Source-computable first-order stress contribution

From original Case006 Appendix AE, its regular-axis comparison is

    q=1-t, A=1/2+h, D=1/2-h,
    u_r^(0)=-2*r/q,
    u_z^(0)=4*z/q+j0*q^(-A).

For an original normalized poloidal shaper Psi=K*Phi(r/ell)*Xi(z/c), with mXi=int Xi(zeta) dzeta, the **exact leading core×shaper axial shear** (Appendix AE (2)) is

    T0(r)= -2*K*c*mXi/q * d_r[Phi(r/ell)/r²].

With the actual core u_c=u^(0)+delta_u, Appendix AE (3) gives the exact uncomputed correction

    Rc(r)= (K*Phi'(r/ell)/(r*ell))*delta_I(r)
         -(K*Phi(r/ell)/(r*c))*delta_J(r),

    delta_I(r)=int delta_u_r(r,z)*Xi(z/c) dz,
    delta_J(r)=int delta_u_z(r,z)*Xi'(z/c) dz.

The original source proves this leading term changes sign and cannot be controlled by C*Phi² near a flat radial edge unless other first-order contributions cancel. No bound for the complete original Rc, quadratic overlap, gauge or 4-patch representative is provided. This is an explicit known term and **not** the final T.

## Minimum required immutable physical tuple

Required fields, each with a numerical/symbolic source, precise units/normalization, complete domain, and hash:

- Actual core u_c, Pi0 and Pi0'' with remainder E; complete time/axial/radial parameter selection (original eqs. 199–210, 255).
- Complete normalized smooth shapers Phi_theta, Phi_j, Xi_j with amplitudes, transition cutoffs, radii and flat edge derivative enclosures (193–194; Remark 9.23).
- Original four localized C4 patch/frame maps and all twelve ordered mixed transport terms (Appendix N).
- Full symmetric prepared stress T and a gradient/gauge representative p0 for the projected forcing g, with source identity checked (242), not T=P tensor P by convenience.
- Original moment-normalized flat envelope rho, local cone R*, and physically determined angular stresses B,C (265–273).
- Compact-domain endpoint traces, q(r)=[mean(S_zz+p0)]_{z=c}^{z=d}, and source integrals Tbar,Rbar,J,Bbar including all boundary defects (Appendix AC).
- Complete source-specific smooth nine-jet and graph-norm bounds, H8 weighted inverse and terminal-coupling matrix with singular-trace retention.

The source-only *necessary* inequalities on each radius are

    |J|<=kappa*Rbar,
    |Bbar|<=kappa*Rbar/8,
    |J-4*Bbar|<=kappa*Rbar/2,

with alpha=-4443/9832, kappa=15971/122900 and

    J=Tbar-alpha*Rbar-[Tbar(a)-alpha*Rbar(a)]
       +(1/r)*integral_a^r s*q(s) ds.

At flat edges Rbar=0, enforce J=Bbar=0, never an undefined ratio. A strict interval violation rejects that selected original source. Passing the scalar test does not establish the full Appendix Y dual, nonaxisymmetric blocks, smooth compact weighted inverse or full NS PDE theorem.

## Exact source indeterminacy

The separate proof in `ATTACK97_SOURCE_FREEZE_IDENTIFIABILITY.md` produces two smooth normalized shaper choices from original Appendix AD with the same rho_diag yet opposite scalar screening outcomes. This is decisive evidence that the original free profiles cannot be silently treated as a uniquely specified physical field.

**Next audit after obtaining missing data:** perform interval evaluation of actual Tbar,Rbar,q,J,Bbar for one compact patch; then Appendix Y coupled solenoidal all-test dual and strict flat-weight source cone. Neither step is certified here.
