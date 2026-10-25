# Edition XI (23 October 2026) — pressure-independent n1 annular witness

The previously exact source first-order collar sign is
R_theta,1(r0,0,t0) = 8 K(r0,t0) q(t0)^(-2D) rho_o > 0.
For the actual prescribed stage, continuity yields a small open
neighborhood of constant positive sign. Any nonnegative nonzero
smooth compact radial/axial bump zeta supported there defines
Phi=zeta(r,z)e_theta, with div Phi=0. Thus <grad p,Phi>=0
for every suitable p, while
  <R_1,Phi>=2*pi*integral R_theta,1*zeta*r dr dz > 0.
Therefore the specified retained first-order source residual
has a positive Leray-projected H^-1 dual norm and cannot be
removed by pressure-only adjustment.

The exact nonlinear correction identity for a background u_B is:
  partial_t w -nu Delta w +(u_B.grad)w+(w.grad)u_B+
  (w.grad)w + grad pi = -R_B.
Pairing with Phi and integrating by parts gives the necessary
correction budget in N1_Pressure_Free_Witness_Edition_XI_20261023_Insert.tex.
This is not a constructive solution: velocity corrections may supply
the required nonzero solenoidal term.

Verification: symbolic divergence and smooth-step midpoint pass;
source-shaped, non-authentic fixture K(r)=r exp(-r²) yields 121
sampled positive residuals, 22x22 positive quadrature pairing and
10000/10000 exact scalar controls. The fixture mesh/quadrature is
NOT an interval-certified source-region margin. The analytic
existence of SOME neighborhood depends only on local continuity.

Lean source N1PressureFreeWitnessScalar.lean contains finite scalar
candidate implications only, not the field, integral, Leray projector
or full PDE. Do not claim kernel PASS without completed CI.
The full frozen source physical residual, inhomogeneous annulus
boundary-value problem, matching/axis conditions, nonzero initial
data, actual zero-force reconstruction and complete Lean unforced
finite-time singularity theorem remain OPEN/HOLD.

Full cumulative manuscript TeX updated in the audit branch.
Separate 23-page cumulative research/addendum PDF includes
the two-page Edition XI note plus 21-page Edition X baseline.
Not a freshly rebuilt full master-paper PDF.
