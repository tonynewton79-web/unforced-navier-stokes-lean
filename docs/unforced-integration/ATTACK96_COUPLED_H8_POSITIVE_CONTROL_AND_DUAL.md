# Attack 96 — manufactured coupled H8 control and fixed-envelope dual screen

**22 November 2026 | Tony Newton**  
**Release state: MANUFACTURED_COUPLED_POSITIVE_CONTROL__ACTUAL_H8_SOURCE_HOLD.**  
This mathematical note **does not prove unforced 3D Navier–Stokes blow-up**. Previous Attack95 compact source-curl no-go for unchanged meridional velocity and forcing is retained.

## Authenticated user sources

The original 122-page Case 006 PDF was reopened and hashed: SHA-256
`56ff24696ac58bef19bcf339d297d3af8b0401e46d5e8125c7fb1d054f01a758`.
Reopened 12-page H8 source SHA-256
`10d70e2f2820980ce471411079e3a06b7f05550aa54cf5dc1c29844d3339a826`.

Use original Case006 (247)–(252), (269)–(273), **Appendix Y** (sharp coupled cone polar), **Appendix AA** (compact unweighted meridional curl right inverse), and Appendix AB (weighted obstruction). These source results are previously stated in the manuscript; the novel integration in this attack is a manufactured NS-residual positive control and an explicitly testable pressure-invariant dual for the swirl repair.

## The exact physical four-field equation

On annular rectangle Omega=(a,b)x(c,d), a>0, use

    H=[[-D,C,A],[C,0,B],[A,B,D]]
    C(H)=max(8|B|, 2|C|+4|D|, 2|A-4B|+4|D|)
    kappa=15971/122900.

Cylindrical divergence:

    div(H)_r=-D_r+A_z-D/r
    div(H)_theta=C_r+B_z+2C/r
    div(H)_z=A_r+D_z+A/r.

Write E=A-4B. Eliminating pressure yields

    curl_rz(f_m)-4L_E(B)=L_E(E)+L_D(D),
    L_E(e)=e_rr-e_zz+e_r/r-e/r²,
    L_D(d)=2d_rz+d_z/r.

Appendix AA proves smooth compact E,D exist for smooth compact g if and only if
integral g drdz=0 and integral r²g drdz=0. This is NOT a fixed-weight or H8 cone bound.

## Theorem 96.1 — any compact stationary coupled NS residual is in this unweighted range

Take a smooth compact *axisymmetric divergence-free* u=(ur,utheta,uz) and nu>0. Define

    f=-nu Delta u+(u.grad)u=div T,
    T=u tensor u-nu(grad u+(grad u)^transpose).

Set B=T_theta,z and C=T_r,theta. Then div(H)_theta=f_theta **exactly**.
For g=curl(f_m)-4L_E B the compact tensor identity gives
integral g=0 and integral r²g=-2 integral r f_z=0. The last integral is zero because f=div T and T is compact.
Apply Appendix AA's explicit linear compact right inverse to obtain E,D, set A=4B+E. The residual meridional vector is curl-free; its compact pressure potential exists on the simply connected annular rectangle. Thus

    f=div H+grad p,

with smooth compact H and p.

The output is a compact stress representing a nonzero *forced residual*, NOT a solution of f=0. The source's unweighted AA theorem is used here, not claimed original prior art.

## Theorem 96.2 — coupled strong-shear moment-neutral manufactured velocity

Choose central positive smooth b0(r) equal to 1 on an interior annular band J, and two auxiliary nonnegative smooth b1,b2 supported on disjoint separated radial bands outside J. Let phi0=r^-11 b0, phi1=b1, phi2=b2. Put Mi=integral r²phi_i dr and Ni=integral r³phi_i dr. Their auxiliary moment determinant Delta=M1N2-M2N1 is nonzero because the weighted mean radii N1/M1 and N2/M2 are distinct. Define

    c1=(M2*N0-N2*M0)/Delta,
    c2=(N1*M0-M1*N0)/Delta,
    tau=phi0+c1*phi1+c2*phi2.

Then both integrals r² tau and r³ tau vanish exactly; tau=r^-11 on J. With an axial bump f(z)>0, constant on subinterval I, u_theta=f(z)tau has a=-r*d_r(log|u_theta|)=11 on JxI. Add an overlapping nonzero poloidal streamfunction Psi_P using ur=-PsiP_z/r and uz=PsiP_r/r. This is a smooth compact, genuinely coupled divergence-free manufactured velocity. For the declared diagnostic G=r, the two toroidal moments vanish on every z-slice. **No actual Case006 G(r,eta) determinant or helical spectral gap is certified**.

## Theorem 96.3 — a strict H8 cone margin exists with an ADAPTED envelope

For u_epsilon=epsilon*u0, the stationary tensor decomposes T_epsilon=epsilon*T1+epsilon²*T2. By linearity of the fixed Appendix-AA reconstruction, H_epsilon=epsilon*H1+epsilon²*H2 with smooth compact H1,H2. Choose a smooth envelope rho0 equal to 1 on the common compact supports and vanishing beyond a slightly larger annulus. With Li=sup C(Hi) finite, select epsilon>0 such that epsilon L1+epsilon² L2<=kappa/2. Then

    f_epsilon=div H_epsilon+grad p_epsilon,
    C(H_epsilon)<=kappa*rho0/2.

The original baseline ray coefficient floor (172/1229)*rho0 therefore retains at least (1/100+kappa/2)*rho0 pointwise. Multiplying by epsilon does not alter a=11.

This is a **positive control for the 4-field grammar with envelope CHOSEN AFTER reconstruction**. The physical Case006 rho and prepared source g have not been used; no source-matched H8 certification, virial normalization, nine-jet closure or singular trace follows.

## Theorem 96.4 — a new fixed-envelope, pressure-invariant centrifugal-source screen

For a compact meridional target f_m=(-Q,0), where the swirl increment gives

    Q=(2*u_theta_old*w+w²)/r,

and a compact four-field correction with C(H)<=kappa*rho, define for each smooth compact scalar Psi

    psi_r=-Psi_z/r, psi_z=Psi_r/r,
    Ppsi=(psi_r)_z+(psi_z)_r,
    Spsi=(psi_z)_z-(psi_r)_r.

The **necessary source-only bound** is

    |integral Psi*Q_z drdz| <=
      kappa * integral r*rho*(|Ppsi|+|Spsi|/4) drdz.

Proof: apply the sharp coupled polar in Case006 Appendix Y:
|integral r*(f_m dot psi+4B Ppsi)|<=integral r*hC(Ppsi,Spsi);
hC<=k|Ppsi|/2+k|Spsi|/4; and 4|B Ppsi|<=k|Ppsi|/2.
Pressure vanishes against divergence-free psi. Triangle inequality gives the displayed bound. If the full cone is partly spent already, replace the RHS kappa*rho by the available *incremental* budget, when justified.

For old swirl zero and w=epsilon*tau(r)*f(z), choose Psi=b(r)*f*f' with b>=0. The inequality gives a real amplitude ceiling

    epsilon² <= [kappa integral r rho (|Ppsi|+|Spsi|/4)]
       / [2 (integral b*tau²/r dr)(integral (f*f')² dz)]

for positive denominator. This test can rule out *the fixed physical rho* even if both source moments vanish and an unweighted H exists.

## Independent exact polynomial diagnostic

On r∈(1,2), z∈(0,1) put phi=(r-1)^4*(2-r)^4,
f=z^4*(1-z)^4, tau=phi''/r², and Psi=r^5*phi²*f*f'.
Then integral r²tau=integral r³tau=0 exactly, yet
integral Psi*(epsilon²*tau²*f²/r)_z = epsilon²*(2096/59657815174123018125)>0.
For fully smooth C_c-infinity replace phi,f by flat nonzero bumps; the moment cancellations and strict positivity persist. Polynomial numbers are diagnostics, not a claim of endpoint C-infinity.

## Physical release gate — still OPEN

The actual Case006 rho, source g, B,C after full four-patch transport, joint polar inequalities for the physical source, source-compatible auxiliary moment determinant, cone-interior E,D, full pressure, source-native nine jets, M_terminal and terminal singular trace have NOT been measured or proved. The fixed-envelope source-first dual test above is the next decisive discriminator; unweighted or manufactured positive controls do not close (273). No numerical matrix or solved Millennium problem is claimed.

Independent exact replay: research/attack96/verify_attack96.py. Finite Lean checks cover rational cone and moment algebra only.
