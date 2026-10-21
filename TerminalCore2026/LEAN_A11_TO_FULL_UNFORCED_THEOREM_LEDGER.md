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


## 21 October 2026: local tail-derivative cancellation

The exact A.11 corrected field is `Ec=Eb*(1+u)`, where
`Eb` is independent of eta after interpolation and
`u=sum_i c_i(eta)*beta(y-yi)` is supported on two disjoint
logarithmic intervals of total length `3/5`.

**New proof component, source-conditional:**
For `D=S/(X Ec^2)`, `P=-Pi/Ec^2`, `g=(log Ec)_eta`,
and source gauges `S(infinity)=Pi(infinity)=0`, the
combination `2*g*(D-P)+D_eta-P_eta` has an exact future-support
representation:

`[1+u(y)]^-2 * integral_0^infinity Rb(y,t)*(1-exp(-t))
*(1+u(y+t))*u_eta(y+t) dt`.

The *local* normalization derivative cancels. If the baseline
future slope `ell_b<=0`, source coefficients satisfy
`|c_i|<=192*lambda^28`, `|c_i_eta|<=12*lambda^28`,
and the actual smooth-step derivative bump satisfies
`|beta|<=640/3`, the absolute value is
`<=1536 lambda^28 (1+delta)/(1-delta)^2 <1/1000`,
with `delta=40960 lambda^28` and `lambda<=1/20`.

Paired with the earlier positive baseline tail comparison
`D_c<233/100`, `E_c<=lambda/4`,
`0<h<=lambda/100`, this proves the improved
**conditional** source stress bound

`|Ns|/Ec < (63/250)*lambda`,
strict slack `lambda/2-|Ns|/Ec>(31/125)*lambda`.

It no longer needs a separate assumption that *corrected*
future slopes are nonpositive (only the baseline future slope).
With the actual `Qs>=lambda/2`, slope and radial gates,
the strict cone is `>=144343/312500>9/20`.

**Submitted to GitHub:**
`A11_Local_Parameter_Derivative_Cancellation_Insert.tex`;
`A11LocalDerivativeCancel.lean` (scalar cancellation/rational
margins ONLY);
`a11_local_derivative_exact.py` (symbolic plus exact Fraction
conditional tests). The cumulative manuscript and GitHub CI
inputs have been updated. No Lean kernel PASS for the new module
is claimed until the relevant CI run succeeds.

**Still NOT source-authenticated:** one frozen true tuple and
interval enclosures for corrected c_i/c_i_eta, terminal
S(infinity)=Pi(infinity)=0, Eb/lambda, Dc, Qs,
radial lower bounds, full stress stages, Appendix-B nonlinear
contraction, the different unforced n=1,2 correction solutions,
common-radius convergence, or the Cartesian zero-force PDE.
Do NOT mark the full 10-stage Lean dependency ledger as done.
The originating OpenAI Theorem 1.1 is a **forced** result.


## 21 October 2026 — exact interpolation derivative and true two-bump jets

The Appendix-A baseline azimuthal field is exactly separable
`E(X,eta)=e(X)/(1+eta²)` through the axial pulse, including
its two U-only corrections. Hence the entrance normalized
angular moment `r_p=I_p/(Xp Hp)` is **eta independent**,
not merely C¹-bounded. On the actual A.10 interpolation,
with `a=1-lambda`, `theta=1-sigma(t/Tf)`,
`J0=log(1+eta²)`, and
`G=exp[(1-theta)(J0-log2)]`, direct differentiation
of `I_y=XH` gives

`r_f = e^(-a Tf)/G(Tf) * [r_p+int_0^Tf e^(at) G(t)dt]`,
`r_f_eta = -J0_eta e^(-a Tf)/G(Tf) *
   [r_p+int_0^Tf theta(t)e^(at)G(t)dt]`.

From `r_p<=20/17`, `Tf>0`, and
`0<lambda<=1/20`, one obtains
`0<=r_f<=40/17`, `|r_f_eta|<=40/17`.
Across BOTH full width-3/10 A.11 correction supports,
the source's subsequent `30 log(1/lambda)` plateau
then gives uniformly

`|r_b-1/(1-lambda)|<18 lambda^28`,
`|r_b_eta|<12 lambda^28`.

The exponential maximum is certified by the monotonicity
of `exp[(1-lambda)63/20]*lambda^(30(1-lambda)-28)`
and the exact finite Taylor/geometric remainder bound
`exp(1197/400)<20`.

The genuine A.11 two-bump matrix has
`||B^-1||∞<3/2`, but its **first column** has norm
at most `35/164`. Differentiating the exact
`B c+Q(c)=(Delta_I,0)` system with eta-independent
weights yields the improved small-branch estimates

`|c_i|<=54 lambda^28`, `|c_i_eta|<6 lambda^28`.

This **discharges the four imported entrance/correction
eta-jet numerical premises** in the prior conditional Qs and
Ns source theorem, without synthetic entrance intervals.

**Still outstanding:** one simultaneous source-admissible
parameter realization; the terminal S and pressure gauges,
tail/energy bounds and stress-cone endpoints outside these
supports; Appendix B contraction; the entire unforced
similarity hierarchy and physical zero-force PDE residual.
The attached short paper proves the source analytic lemmas;
the GitHub Lean module `A11EntranceJetScalar.lean`
formalizes only finite rational inequalities (CI must pass
before any kernel claim). The full start-to-finish Lean proof
and proposed unforced Theorem 1.1 remain OPEN.
