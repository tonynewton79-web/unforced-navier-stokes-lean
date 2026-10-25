# Lean: ten-state source to proposed unforced Theorem 1.1

21 October 2026. This is an explicit proof-obligation ledger, **not a
completed theorem**. The originating OpenAI 166-page source theorem uses
smooth, compactly supported external forcing.

## Verified analytic/source identities
- Source (4.15)--(4.16) yields five normalized moments, their five first
  parameter jets, and two scale-free Q/N formulas.
- The ten-state system splits into eight forward moment states and two
  backward infinity-gauge pressure states.
- An all-stage **conditional** exact-rational ODE comparison theorem gives
  whole-cell and endpoint tubes from already certified input bounds.
  Reference-stage and pure exterior-tail tests pass; negative controls
  reject unsafe step lengths.
- On the actual A.9 pulse, ell=-lambda, ell_eta=0, and
  g=-2eta/(1+eta^2); all ten moments have exact integrating-factor
  formulas, including closed forms for i, i_eta, p, p_eta.
- The stable pulse kernels are highly localized in xi=lambda*y, and the
  energy kernels live on fixed xi in [0,13], avoiding an impractical
  1/lambda generic time-subdivision requirement.

## Lean files submitted, NOT kernel-certified
- NormalizedMomentPulseScalar.lean
- TenStateAffineTubes.lean
- PulseTransferScalar.lean

These contain scalar identity/comparison proof candidates, not the
smooth source integrals, interval ODE theorem, true cone or PDE.

## Missing proof gates, in required order
1. Specify ONE jointly admissible Appendix-A parameter tuple with the
   precise A.9 axial and distinct A.11 azimuthal corrections.
2. Independently enclose a,a_eta,ell,ell_eta,E,g,R,R' on every radial
   stage and eta-cell, including analytic error bounds. Verify
   E_y=(ell-1/2)E and g_y=ell_eta.
3. Formalize interval arithmetic, source integrals, ODE comparison,
   compact pulse convolution and the complete rational source cell cover.
4. Certify Q_s>0, e_Q,e_N,eta*m_eta and all strict pulse ratio budgets
   on every pulse cell. Conditional source intervals alone are insufficient.
5. Certify the stress cone on ALL exterior stages, transitions and
   terminal matching.
6. Certify the Appendix-B nonlinear analytic profile, pressure trace,
   common radii and quantitative contraction.
7. Solve and verify the distinct n=1,2 UNFORCED startup equations,
   all-order analytic recurrence and physical-coordinate reconstruction.
8. In Lean define the physical NS fields, divergence, force-free
   momentum residual and axis/pressure regularity, then prove the
   precisely stated target from checked premises.
9. Obtain clean Lean kernel acceptance with no admitted/unverified
   axiom and independent source/mathematical review.

Current result: source algebra and conditional tube arithmetic pass;
full source profile, pulse 10^-6 ratio, all-stage stress cone, complete
Lean PDE proof and unforced Theorem 1.1 remain OPEN.
