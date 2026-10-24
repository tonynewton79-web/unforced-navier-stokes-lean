# A.11 endpoint source certification and Lean dependency boundary

21 October 2026. **The proposed unforced Theorem 1.1 is OPEN.**
The originating OpenAI Theorem 1.1 has smooth external forcing.

## New proven conditional results

On the two disjoint A.11 corrections, let `Ec=Eb(1+sum ci beta_i)`.
Under the actual source coefficient bounds
`|ci|<=192 lambda^28`, `|ci_eta|<=12 lambda^28`,
`|beta|<=640/3`, `|beta'|<=200000`, put
`delta=40960 lambda^28<10^-31` for `lambda<=1/20`.
Then simultaneously on both complete correction supports:

- `(1-delta)Eb <= Ec <= (1+delta)Eb`.
- `|partial_eta log Ec| <= 2560 lambda^28/(1-delta)`.
- `|ellc+lambda| <= 38400000 lambda^28/(1-delta)<lambda/2`.
- `|partial_eta ellc| <=2400000 lambda^28/(1-delta)^2`,
  where the cancellation is **exact**.

For the normalized corrected/base tail moments from the terminal
S and pressure gauge:
`kappa^-2 Db<=Dc<=kappa^2 Db` and similarly for P,
with `kappa=(1+delta)/(1-delta)` and `kappa^2<=1+8delta`.

Between the extreme support endpoints `yminus,yplus`, the
uncorrected source has exact slope `ellb=-lambda`. Thus
`Db'=2lambda Db-1/2` and
`Pb'=(1+2lambda)Pb-1/2`; both are monotone or constant,
so extrema occur at endpoints.

A source-authenticated A.11 `|Ns|/E<lambda/2` proof may therefore
be reduced to enclosing `Eb(yminus)/lambda`, the two base
D/P endpoint moments, the actual correction coefficients and the
true terminal/gauge/future-slope hypotheses. With independently
proven `Qs` and radius gates, the earlier strict cone margin follows.

## New code

- `A11_Endpoint_Tail_Comparison_Insert.tex`: written mathematical proof.
- `A11EndpointScalar.lean`: finite exact scalar algebra only; does not
  formalize source integrals or unforced fluid PDE.
- `a11_endpoint_exact.py`: all-index rational coefficient comparisons
  and symbolic derivative/endpoint ODE checks.
- `a11_endpoint_gate.py`: **ALWAYS returns conditional status** even
  when supplied arithmetic bounds pass; never authenticates source inputs.

## Release-critical steps, in order

1. Formalize source smooth step, its derivative and exact distinct
   A.9/A.11 corrections in Lean.
2. Derive true A.11 moment-correction coefficient and eta-jet bounds.
3. Verify S(infinity)=0, pressure gauge, positive tails and stage
   integrability from one true parameter tuple.
4. Generate replayable outward intervals for Eb(yminus), base D/P
   endpoints and Qs from exact source stage formulas.
5. Prove both A.11 support stresses, the whole exterior and full
   A.29–A.30 pulse stress ratio for the SAME source tuple.
6. Certify Appendix B nonlinear contraction and the distinct UNFORCED
   n=1,2 coefficients, all-order recurrence and analytic convergence.
7. Formalize the Cartesian physical coordinate conversion, axis
   regularity and vanishing unforced NS residual.
8. Run all proof objects through the Lean kernel with no sorry, admit
   or user axioms; independent source solver and mathematical review.

Scalar lemmas and synthetic/checker-furnished interval boxes alone
are not an A.11 source certificate, Lean proof or Millennium solution.
The entire uploaded user ledger accompanies the downloadable ZIP.
