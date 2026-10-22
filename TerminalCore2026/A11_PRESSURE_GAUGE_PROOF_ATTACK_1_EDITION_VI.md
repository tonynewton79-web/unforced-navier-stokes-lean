# Proof Attack 1 / Edition VI — exact source terminal pressure gauge

## Source-confirmed result

In the original OpenAI *Finite Time Blowup for Navier–Stokes*,
Appendix A, equation (A.21) defines Pi0(eta) as minus one-half
the integral of the squared reference azimuthal field, with
the later pressure-neutral corrections omitted.

The second exact A.11 moment equation is
R2=2v(q1+z q2)+w(q1^2+z q2^2)=0.
On the prescribed disjoint translated sigma' supports,
integral(E_corrected^2-E_reference^2)dy = C(eta)*R2.
The support lengths are 3/10 and centers differ by 2.
The pressure transport law Pi_y=E^2/2 therefore gives
Pi(infinity,eta)=C(eta)*R2(eta)/2=0.
On an exact C1 branch its TOTAL eta derivative vanishes.

The result is **already in source Lemma A.5**, not new mathematics.
Edition VI independently verified it, removed a redundant
baseline-pressure numerical calibration from this source-local
dependency list, and supplies a separate finite Lean candidate.

## Independent verification

- Exact symbolic square expansion, translation factor and derivative: PASS.
- Actual sigma' bump 68-digit integrals, 2 lambda values x 5 eta values: PASS.
- Adversarial negative case A19 amplitude equation only: R2=2/5 => REFUTED.
- New Lean module: A11PressureIntegralGate.lean, **CI pending**;
  this is not a full integral-support formalization.

## Still OPEN

One genuine A.11/A.19 joint corrected source family;
later edits preserving pressure; complete stress cones; Appendix B;
unforced n=1,2 and all-order correction equations; exact
zero-force physical Navier–Stokes residual; full Lean proof.
