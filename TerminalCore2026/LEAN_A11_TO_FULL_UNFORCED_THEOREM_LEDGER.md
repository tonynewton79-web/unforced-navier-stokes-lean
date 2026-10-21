# A.11 N_s/E proof and start-to-finish unforced Navier--Stokes Lean ledger

21 October 2026. This is a **dependency ledger, not a completed theorem**.
The originating OpenAI Theorem 1.1 is FORCED. A proposed unforced
extension cannot inherit its proof.

## Completed conditional mathematics

1. With genuine S(infinity)=0 and Pi(infinity)=0, source (4.16) gives
   N_s/E=E{4 eta(h D_s-A P_s)
      -(1-eta^2)[2 g(D_s-P_s)+(D_s)_eta-(P_s)_eta]}.
2. If future ell<=0 and |g|<=eps, source tail integrals imply
   0<=P_s<=1/2 and
   |N_s|/E<=E[4hD_s+4A P_s+2eps(D_s+P_s)].
3. If the source upper budgets E<=lambda/4, 4hD_s<=61/100,
   P_s<=1/2, 2A<=1001/1000 and 2eps(D_s+1/2)<=1/100 all
   hold on BOTH whole (A.11) supports, then
   |N_s|/E<=1621 lambda/4000<lambda/2, with
   at least 379 lambda/4000 strict slack.
4. Under independently established Q_s>=lambda/2, source slope and
   radial scale bounds, the normalized strict cone margin is at least
   32117077/80000000>2/5.
5. A11NsQuantitativeSlack.lean is a FINITE scalar proof candidate with no
   admitted lemmas. New GitHub Actions jobs are queued; kernel SUCCESS
   has not been observed. It does not prove the analytic source premises.
6. a11_ns_quantitative_slack_exact.py checks all displayed rational
   implications and rejects incomplete or budget-failing test cells.
   Exact arithmetic does not authenticate the prescribed source fields.

## Full formalization dependencies (must be discharged in order)

* [ ] Formalize source sigma, sigma', fixed A.9/A.11 bumps and exact
      radial/source-coordinate definitions, no convenient surrogate.
* [ ] Construct a single admissible Appendix A parameter tuple with
      all moment corrections, terminal matching and stress controls.
* [ ] Prove actual A.9 pulse end M=J=M_eta=J_eta=0 from integral data.
* [ ] Prove A.11 azimuthal coefficients, eta derivatives, future slope
      and infinity moment/pressure gauge from that same tuple.
* [ ] Produce independently validated interval E, ell, g, D_s, P_s
      bounds over a full closed cover of BOTH A.11 supports.
* [ ] Connect these intervals by a Lean soundness theorem to the
      conditional scalar N_s/E margin and Q_s/radial stress cone.
* [ ] Verify A.29--A.30 residuals and the full stress cone on every
      other stage, including centerline accuracy near lambda*10^-10.
* [ ] Freeze the actual Appendix-B leading profile, pressure trace,
      complex tube and a numerical or symbolic contraction certificate.
* [ ] Construct genuine n=1 and n=2 UNFORCED correction solutions and
      prove the complete higher-order coefficient source hierarchy.
* [ ] Formalize common-radius analytic Banach spaces, pressure shift,
      source-to-recurrence correspondence and convergence.
* [ ] Prove physical-coordinate zero-force Navier--Stokes residual,
      incompressibility, axis regularity and the precise stated
      local or global unforced claim. No assumption of residual zero.
* [ ] Run a clean Lean/mathlib build and '#print axioms' on the actual
      end theorem; inspect all evidence and obtain independent review.

## Release claim

A sharper **conditional** normalized A.11 stress inequality and an exact
verification-design improvement. NOT a certified source interval instance,
NOT a completed Lean PDE proof, and NOT an unforced Navier--Stokes blowup.
