# Start-to-finish Lean obligations for the proposed UNFORCED terminal-core theorem

20 October 2026. This is a dependency ledger, NOT a completed proof.
The originating OpenAI whole-space theorem uses smooth external forcing.

## 1. Source outer construction (OPEN)
- Freeze and independently verify one admissible tuple Md,Td,Pstar,Tf,lambda,h,c0,XR.
- Formalize the true sigmoid, A.9 axial and A.11 azimuthal end bumps separately.
- Prove all five radial moment equations and pressure normalization.
- Produce source-derived interval bounds for every radial interval.
- Pulse: the main convolution A.28 now has a *mathematical* bound using
  ||R0''||<=192000, but the A.29-A.30 w moment/pressure error
  |w-(2A R0-Cd A R0')|<=10^-6 has NOT been certified.
- Cone: both strict stress margins, joining-stage relaxed cone, full terminal
  endpoint and parameter-dependent radial scale remain to be checked.

## 2. Analytic axis profile (OPEN)
- Certify the genuine exterior pressure trace, common complex tube and
  nonlinear Appendix B fixed-point bounds for exactly that tuple.
- Certify the axis matching and shear conditions.

## 3. Higher unforced corrections (OPEN)
- Derive and solve actual n=1,2 startup equations and pressure gauges.
- Define and prove full two-space Banach estimates and all-order recurrence.
- Prove uniform local convergence of the actual unforced series.

## 4. Physical theorem (OPEN)
- Define physical axisymmetric fields and cylindrical operators in Lean.
- Prove axis regularity, divergence free identity, local kinetic energy.
- Prove physical momentum residual equals **zero** with f=0.
- Prove the claimed theorem (distinguish local from whole-space statements).

## Current scalar check modules
A11ConeMargin.lean; A11NsExteriorTail.lean; A5PulseFiniteGates.lean.
These are finite scalar proof candidates. No sorry or new axiom was added
to A5PulseFiniteGates.lean. A successfully completed pinned GitHub workflow
is required even to call those new candidate lemmas kernel-checked.
The analytic sigmoid proof, validated interval sources, full
Banach/PDE analysis and physical theorem are NOT formalized.

## Non-negotiable completion gates
(1) independently validated source tuple and moments;
(2) source-generated interval certificate for all cones and residuals;
(3) actual source-to-Lean definitions for analytic functions, integrals,
infinite sums and physical differential operators;
(4) no admitted axioms/sorry in the final theorem dependency closure;
(5) reproducible successful kernel replay and specialist mathematical review.
