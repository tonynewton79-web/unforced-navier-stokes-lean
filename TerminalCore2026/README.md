# Lean audit: exact local terminal-core Navier–Stokes preprint

Source: Tony Newton, *Exact Local Unforced Terminal-Core Dynamics in Three-Dimensional Navier–Stokes: Anisotropic Concentration and Swirl Reversals*, Zenodo v1 (19 October 2026), DOI: 10.5281/zenodo.23474915.

This paper differs from the repository's earlier periodic-torus unforcing paper (Zenodo 22903432). The previous PDE-specific gaps and certificates do not settle the claims of the new paper.

## Finite theorems in TerminalCore2026.lean

Equations (12), (35), (57), (58), (59), (61), and (62) are encoded as algebraic identities or inequalities, including coefficientwise radial inversion, the spatial critical exponent, the L3 power, the Serrin exponent, and positivity of the local-energy decay power. A green pinned CI run would certify only the precise Lean statements, not the manuscript's main PDE theorem.

## Essential analytic/PDE formalization gaps

1. Independently import or derive the exact similarity chain rules (15)-(18).
2. Formalize the complete coefficient hierarchy (23)-(28) and the valuation ladder (30)-(31).
3. Define the doubled analytic norm (37)-(38) and prove bounded multiplication, radial regular-singular inversion, and composite pressure estimates (39)-(44).
4. Instantiate all four current-order blocks (47)-(50) and prove the uniform O(1/n) operator estimate (51) in an appropriate concrete Banach space.
5. Prove the scalar convolution majorant (53), its uniform coefficient bound, and one common analytic convergence domain.
6. Justify arbitrary required physical differentiation; reconstruct the actual velocity and pressure and prove their divergence and unforced momentum residual vanish pointwise.
7. Separately verify the global-smoothing assumptions and any continuation/reversal theorems.

Never replace items 1-6 by unverified hypotheses and then advertise a full Lean proof of Theorem 1.1.

## Replay

```sh
lake update
lake exe cache get
lake env lean TerminalCore2026.lean
python -m pip install sympy
python TerminalCore2026/check_equations.py
```

The branch and draft pull request are staging grounds; await successful GitHub Actions kernel compilation and then a line-by-line proof-scope audit.

## Sharpened constant (19 October 2026)

The denominator-weight identity in manuscript equation (45) admits a sharp all-index coefficient ratio of **8**, replacing the previously sufficient constant 16 from Appendix B.2. In particular the two-eta-derivative radial inverse has the improved coefficient-space bound `8 R / rho^2` for both `nu=1` and `nu=2`.

The inequality `two_derivative_ratio_le_eight` in `TwoDerivativeWeight.lean` passed pinned GitHub Actions run `39262059263`. The exact proof uses `4(a+1)^3-(a+2)^2(2a+1)=a^2(2a+3)>=0`, and sharpness is obtained by `a=0, nu=1, b -> infinity`.

A typeset three-page scholarly mathematical supplement, `Sharp_Weight_Ratio_Manuscript_Update.tex`, has been successfully built in GitHub Actions run `39262528882` and published as workflow artifact `terminal-core-sharp-weight-ratio-pdf`. The 16-page original article has **not** been overwritten or silently replaced. Its exact LaTeX project is needed for a fully integrated manuscript revision.

The abstract array transport theorem subsequently added to `TwoDerivativeWeight.lean` is a distinct theorem: judge it by its own CI run, not the earlier successful ratio-certificate run.


## Cumulative analytic amendment: three inverse channels and ideal norms

The new cumulative manuscript source is
`TerminalCore2026/Terminal_Core_Cumulative_Analytic_Amendment.tex`.
It supersedes the earlier stand-alone weight-ratio supplement for manuscript
integration. The printed research packet consists of the original 16 pages,
unchanged, followed by this single, newly typeset four-page cumulative
amendment. This is not represented as a re-typeset edit of the unpublished
original LaTeX source.

Writing the ambient coefficient weight as
`w(a,b)=R^(-a) rho^(-b) b! binom(2a+b,b)/((a+1)^2 (b+1)^2)`,
the precise normalized coefficient multiplier for
`J_nu d_eta^k` satisfies for `nu >= 1`:

- `T_0 <= 4R/(a+1)^2`;
- `T_1 <= 8R/[rho(a+1)]`;
- `T_2 <= 8R/rho^2`, with 8 sharp.

The zero- and one-derivative bounds provide concrete constituent
`O(n^-2)` and `O(n^-1)` estimates in the induced analytic norm on
the radial ideals `I_n`. The delayed two-derivative channel is only `O(1)`.
The sums and similarity shifts are treated explicitly in the amendment.

**Norm clarification:** `I_m=X^m B` must use the norm inherited from the
absolute radial-indexed coefficient space, not the quotient norm
`||X^m f|| = ||f||_B`. Under the quotient norm,
`J_nu d_eta^2` is unbounded, witnessed by `X^m exp(k eta)` as `k -> infinity`.
This does not invalidate the induced-norm estimate; it removes an
otherwise ambiguous possible interpretation.

Independent exact regression:
`python TerminalCore2026/exact_radial_channels.py`.
New Lean statement:
`TerminalCore2026/FirstDerivativeChannel.lean` (CI status must be checked
on its own latest commit). The earlier sharp all-index two-derivative
inequality remains separately kernel-certified.

### Remaining full PDE theorem obligations

The three multiplier bounds do NOT yet instantiate all four physical
current-order operators (47)–(50). In particular the actual maps
`U_n -> V_n[U_n]`, leading-profile products, and the composite
pressure integration/shift must be proved bounded in the same
radial-valuation-indexed space, with explicit uniform constants.
The full `||K_n|| <= C/(n+1)` estimate, majorant, differentiated
normal convergence and unforced PDE identity are NOT machine-checked.


## Fourth-round four-block and explicit majorant theorem (2026-10-19)

The cumulative manuscript has been **updated**, not split into competing notes:
`Terminal_Core_Cumulative_Analytic_Amendment.tex` now includes
`Four_Block_and_Majorant_Insert.tex` and is rebuilt through the existing
manuscript Actions workflow. The original 16-page deposited preprint remains
unchanged; the new cumulative standalone amendment is seven pages.

**Key correction to the earlier argument.** In the induced weight norm,
the bare radial derivative `D_X` is unbounded: the normalized monomial
`w_{m,0} X^m` has norm 1, but its `D_X` image has norm `m`.
The bare axial parameter derivative is also unbounded. Thus an
`O(n)` bound for a standalone `T_{a,n}`, or boundedness for
`partial_eta A_X`, cannot be invoked prior to radial inversion.
This observation does not disprove the coupled estimate. The new proof
estimates composites using the product-derivative commutators.

The exact decomposition of the swirl--swirl source has been encoded in
`SwirlDiagonal.lean`. The pressure and other source decompositions
are independently replayed in `four_block_and_majorant_exact.py`.

**Concrete analytic norm theorem:** Assuming the explicit leading
multipliers `v,g,H,k,m_phi,m_U,q_phi,q_U,s_1,s_2,s_3,phi_0`,
and the multiplier derivatives displayed in the manuscript, all
belong to one fixed induced analytic coefficient space with the stated
Banach multiplication bound, the manuscript derives
`||K_phi_phi|| <= C_phi_phi/(n+1)`,
`||K_phi_U|| <= C_phi_U/(n+1)^2`,
`||K_U_phi|| <= C_U_phi/(n+1)^2`,
`||K_U_U|| <= C_U_U/(n+1)`,
with all four constants displayed, and therefore
`||K_n|| <= C_K/(n+1)`.

**Independent remaining gates:** The precise source-to-norm
verification of all imported leading multipliers and the pressure
normalization has not been formally checked, nor has the complete
lower-order forcing recurrence or the differentiable PDE
reconstruction. Accordingly this is a conditional analytic-space
estimate, not an end-to-end proof of the manuscript's Theorem 1.1.

**Constructive scalar majorant:** The proof introduces
`M = 1/[16(1+C1)]`, chooses `R` according to explicit finite
conditions, and proves `A_n <= M R^n/(n+1)^2` from the scalar
recurrence. Its key all-order inequality is
`sum_(i=1)^(n-1) 1/[(i+1)^2 (n-i+1)^2] <= 4/(n+2)^2`.
The finite polynomial inequality and budget gates have been
submitted in `MajorantBounds.lean`; the exact finite rational
regression is in `four_block_and_majorant_exact.py`.

Do not claim the new Lean files passed CI until their current run has
completed successfully. An older green run is not transferable to
these new declarations.


## Cauchy-profile bridge — next Lean test (19 October 2026)

The cumulative mathematical manuscript has been updated to include
`CauchyProfileBridge_Insert.tex`, and the PDF should now be rebuilt
as one eight-page supplement appended to the original 16-page paper.

**Quantified bridge.** For the exact doubled analytic weight in (37),
if a function has uniform Cauchy bounds
`|∂_eta^b F_a(eta)| <= M S^-a delta^-b b!` on the chosen compact
core, then `R <= S/4` and `rho <= delta/4` imply
`||F||_(R,rho) <= M`. This follows from
`(j+1)^2 q^j <= 1` for every natural `j` and `0<=q<=1/4`;
the binomial factor in the weight only improves the estimate.
An exact proof appears in the current TeX manuscript.

The source multipliers needed for the conditional four-block
estimate are all holomorphic on any common complex product
neighborhood on which the actual leading profiles are holomorphic,
`V0(0,eta)=0`, and `L(eta)=1-2h eta^2` does not vanish.
For `0<h<1/100` and `|eta|<=2`,
`|L(eta)|>23/25` by a complex triangle bound.

**Lean theorem scope:** `CauchyProfileBridge.lean` contains three
all-natural-index statements: polynomial-geometric absorption,
two-index absorption, and the normalized Cauchy jet-array majorant.
The workflow compiles that module and checks the exact finite
regression in `profile_cauchy_exact.py`. These kernel statements
do not prove Cauchy's integral theorem in Lean, nor do they
instantiate the actual imported Navier--Stokes profiles.

**Open scientific gate:** Check a concrete holomorphic extension and
explicit complex-radius bounds for the particular source leading
profiles. Then independently verify all full lower-order recurrence
terms and termwise differentiated physical PDE reconstruction.
Do not claim the full Theorem 1.1 is Lean-certified at this stage.

**CI status discipline:** The current workflow run must complete
successfully before this new module is described as kernel-verified.
Previously successful unrelated runs do not transfer.

## Radial-valuation normal-convergence bridge (19 October 2026)

This continuation adds `AnalyticReconstruction.lean`,
`AnalyticReconstruction_Insert.tex`, and
`analytic_reconstruction_exact.py`. The cumulative LaTeX manuscript
now includes the reconstruction theorem as its final mathematical section.
For `F_n in I_n`, the induced analytic norm `||F_n|| <= A_n`, and
`|X|<=R/8`, the finite coefficient-space estimate proves for each
`b>=0`:

`|∂_eta^b F_n(X,eta)| <= 2^(1-n) A_n * b!/(b+1)^2 * (2/rho)^b`.

The argument uses the all-index envelope
`choose(2a+b,b) <= 4^a 2^b` and exact geometric tail
`sum_{a=n}^infty 2^-a = 2^(1-n)`. If the *actual* coefficient
sequence has `A_n <= M T^n/(n+1)^2`, this gives uniform
convergence of each fixed axial derivative for `|s| T < 2`,
with the terminal parameter `s=q^(2h)`.

The local exact replay independently passed 25,921 integer binomial
comparisons, 2,500 rational tail identities, and 665 weighted tail
checks. GitHub Actions has been configured to compile the new Lean module,
but only the eventual *completed successful* CI run can certify it.
No statement in these new files certifies the source leading-profile
holomorphic extension, lower-order Navier--Stokes coefficient
recurrence, full physical derivatives, pressure reconstruction,
or the unforced PDE theorem.

The reader PDF is the original 16-page preprint unchanged with a
nine-page cumulative amendment attached. The editable amendment is
in the GitHub source; do not treat it as a replacement for the
original deposited manuscript's unavailable LaTeX project.


## Source-native delayed-pressure forcing attack (20 October 2026)

The cumulative manuscript now includes `Delayed_Pressure_Source_Ledger_Insert.tex`
as its **ninth mathematical section**. The original deposited
16-page PDF remains unchanged; the replacement cumulative amendment
adds the exact lower-order source decomposition (25)--(27) and the
full `Omega_(n-1)` term from (28), including
`-Z^[2]_(0,n-2) V_(n-2)`.

The especially difficult two-step linear path is
`U_(n-2) -> V_(n-2) -> Omega_(n-1) -> Pi_n -> U_n`.
It differentiates four times in eta and lifts radial degree by
two, with scalar coefficient denominator
`(a+1)^2 (a+2)^2`. For the exact (37) weight, the
all-index principal ratio satisfies

`w_(a,b+4) / [((a+1)^2 (a+2)^2) w_(a+2,b)] <= 54 R^2/rho^4`.

The constant 54 is sharp as `a=0,b->infinity`. The exact
polynomial numerator certificate is

`54(a+1)^4(a+2)^2 - (2a+1)(2a+2)(2a+3)(2a+4)(a+3)^2
 = 2a(a+1)(a+2)(19a^3+71a^2+69a+9) >=0`.

This is formalized in `DelayedPressureFourJet.lean` (source submitted;
kernel validation awaits a completed successful GitHub Actions run).
`delayed_pressure_fourjet_exact.py` independently passed 9,333
exact-rational factor checks for three radius choices.
`source_native_principal_path.py` symbolically composed the **full**
variable-coefficient operators from (22),(24),(26)--(28) and
confirmed 48 exact instances of the highest-jet coefficient

`-(d/L)^4/[4(a+1)^2(a+2)^2]`.

These are new coefficient-level bounds and exact source-level checks.
They **do not establish** the complete lower-order forcing recurrence
(53). Remaining: norm bounds for all lower-jet variable-coefficient
commutators; the complete `Omega_(n-1)` source; every other delayed
and interior quadratic term; fixed leading-profile holomorphic radii;
and the differentiated physical PDE reconstruction. In particular
the highest-jet channel is O(1), not automatically O(1/n), so it
belongs in the two-step `A_(n-2)` forcing bound, not in the current
feedback block.

The full normal convergence statement (Theorem 1.1) is **not**
independently end-to-end Lean-certified. Keep PR #1 in draft.


### Extended five-channel symbolic bound (20 October 2026)

The delayed-pressure source manuscript has been upgraded beyond the sharp
four-jet coefficient lemma. Let (w_{a,b}) be the exact weight (37).
For (n>=2), (a>=n-2), (b>=0), and integer (0<=k<=4),

```
(n+1)^(4-k) * w_(a,b+k)
    / [(a+1)^2 (a+2)^2 * w_(a+2,b)]
 <= 54 * R^2 * rho^(-k) * (25/(k+1)^2) * 3^(4-k).
```

The proof is all-index and follows by factoring the (k=4) ratio;
the remaining ((4-k)) reciprocal factors are each at most
`1/(a+1)`, while (n+1<=a+3<=3(a+1)).
The `b` ratio is bounded by `(5/(k+1))^2`.
The independent script `fourjet_symbol_bounds_exact.py` passed
15,345 exact-rational formula and inequality checks.

Total new local exact replay in this tranche:
9,333 four-jet ratios + 48 full source-native symbolic differential
compositions + 15,345 mixed slots = **24,726** reproducible cases.
The actual complete variable-coefficient forcing recurrence (53)
still lacks a uniform all-channel Banach-norm certificate and
remains **open**. Exact-rational replay is not Lean kernel validation;
watch the new workflow run for its conclusion.


## Full variable-coefficient delayed-viscosity pressure bound (20 October 2026)

The cumulative manuscript now contains the *complete* linear delayed-viscosity
pressure path from U_(n-2) to U_n, including all derivatives falling on the
rational eta-dependent multipliers. Source proof:
`DelayedPressureBanach_Insert.tex` (subsection of the ninth section);
the 29-page revised reading copy is the unchanged 16-page source preprint
with a single 13-page cumulative mathematical amendment.

For 0<h<1/100, on E=[-1,1], R>0, 0<rho<=1/4, and all n>=2,
the operator induced by the **specific** source path
`U_(n-2) -> V_(n-2) -> -Z^[2]_(0,n-2)V_(n-2) -> Pi_n -> U_n`
maps `I_(n-2) -> I_n` with uniform bound

`||P_n|| <= (14487066/4)*(80/27)*54*R^2 * sum_(j=0)^4 [25*3^(4-j)/((j+1)^2*rho^j)]`.

The proof writes the exact composition of three shifted Z factors
applied to the full first-order radial-velocity operator; the
coefficients of the normal form `sum_j c_(a,n,j)(eta)*partial_eta^j`
are bounded by
`|partial_eta^ell c_(a,n,j)| <= 14487066*(a+n+1)^(4-j)*ell!`.
This follows from uniform rational-multiplier bounds on complex
|eta|<=3, three nested Cauchy radius losses of 1/4, and the
explicit normal-form induction factor 87. The strengthened
all-slot weight inequality controls `(a+n+1)^(4-j)`, rather than
only `(n+1)^(4-j)`. The analytic multiplication commutator
factor is <= sum_(ell>=0)(ell+1)^2 rho^ell <= 80/27.

Independent exact replay: 48 full-variable-coefficient SymPy symbol
compositions and **64,800** exact-rational all-slot checks passed;
the exact composition majorant `22*87^3=14487066` also passed.
File: `full_delayed_pressure_banach_exact.py`.
Finite Lean lemmas for the index, Leibniz and composition budget are
in `DelayedPressureBanachLemmas.lean` and included in the GitHub Actions
workflow. Confirm an actual successful latest run before reporting them
as Lean kernel-certified.

**Critical boundary:** This is NOT the full Omega_(n-1) source in (28);
other linear forcing terms, all quadratic products, and the imported
leading-profile analytic radii must still be controlled to derive
recurrence (53). The four-block theorem remains conditional on the
leading-profile hypotheses. No end-to-end Lean proof of the local
Navier--Stokes Theorem 1.1 or whole-space unforced blow-up is claimed.


## Remaining two direct linear pressure terms — cumulative paper revision (20 October 2026)

The cumulative manuscript source now inputs
`Remaining_Linear_Pressure_and_Nonlinear_Ledger_Insert.tex`.
The printed reading copy is the deposited 16-page source followed by
one updated 15-page mathematical amendment (31 pages combined).
The source paper is retained unchanged and this PR remains in draft.

Equations (17),(18),(24),(26)–(28) produce **different radial
valuations** for the two direct sources in `Omega_(n-1)`:
* `-2 X V_(n-1),XX` gives `I_(n-1) -> I_n`, with
  `||L_n|| <= (1157/2)*(80/27)*R*(4+8/rho+8/rho^2)`.
* `T_(0,n-1)V_(n-1)` gives `I_(n-1) -> I_(n+1)`, with
  `||T_n|| <= (9256/4)*(80/27)*54*R^2/n *
    sum_(j=0)^3 25*3^(4-j)/[(j+1)^2*rho^j]`.

These are derived in the induced weighted coefficient norm for
`0<h<1/100`, `0<rho<=1/4`, and `E=[-1,1]`. The proof controls
the *complete* variable-coefficient `Z T H` and `Z H`
compositions, including commutators, using explicit Cauchy discs,
a Leibniz-series factor `80/27`, and the existing radial weights.

`RemainingLinearPressure.lean` encodes only finite scalar
pressure integration identities and order-index lemmas.
`remaining_linear_pressure_exact.py` independently checks
36 source-native full symbolic compositions and 79,380 exact-rational
weight/shift bounds. The new Lean kernel check is pending successful
execution of its specific GitHub Actions job; earlier successful jobs
do not certify it.

**Remaining pressure source:** after these two contributions and the
previously studied delayed-viscosity operator, the exact `Omega_k`
has five leading-profile interaction terms and a positive-order
quadratic interior sum. The entire lower-order forcing recurrence
(53), actual profile radii, quadratic pressure bounds, and physical
PDE reconstruction remain OPEN. No end-to-end Lean proof of
Theorem 1.1 or global unforced blow-up has been obtained.

## Leading-profile pressure: five-term cancellation and valuation (20 October 2026)

The cumulative paper now includes `Leading_Profile_Pressure_Cancellation_Insert.tex`
in its ninth section. It establishes the complete exact identity for the five
ordered leading-profile interactions in source equation (28). Writing
`v=V0/X`, `F=Uk`, `Vk=XWk`, `B=2eta/L`, `G=d/L`,
`Wk=B F-B(D+lambda_k) A_XF-G partial_eta A_XF`, and
`K0=G partial_eta v-B(v+D_Xv)`, the source satisfies

```
S_k/X = (D_X+1)(v Wk)
       + U0 [G partial_eta+B(lambda_k-1-D_X)] Wk
       + F K0.
```

The radial derivative and the pressure primitive cancel **exactly**:
`int_0^X (D_X+1)(vWk) dx = X vWk`.
Thus the full induced pressure contribution is

```
P_lead_(k+1) F =
 -1/4 J1 Z_(-2A,k+1) [
   X v Wk + int_0^X {
     U0 [G partial_eta + B(lambda_k-1-D_X)] Wk
     + F K0
   } dx ].
```

Coefficientwise, this maps `I_k` into `I_(k+2)`. In the three
grouped channels the unknown F sees respectively <=2, <=3, and <=1
axial derivatives after final pressure reconstruction.

An exact all-index *scalar* coefficient inequality, for
`j=0,1,2,3` and `r=a+1`, is

```
r^(3-j)*w_(a,b+j) / (r^2*(r+1)^2*w_(a+2,b))
 <= [54 R^2/(r rho^j)] * [25*3^(4-j)/(j+1)^2].
```

It follows from the previously proved 4-jet/2-lift inequality.
`leading_profile_pressure_exact.py` passed 72 source-native symbolic
replays and 41,472 exact rational coefficient inequalities.
The finite algebra/valuation parts are encoded in
`LeadingProfilePressure.lean`, with an explicit CI compilation step.
A new Lean theorem is NOT kernel-verified until the current CI succeeds.

**Open gate:** This is NOT a uniform analytic Banach norm estimate of
the full leading-profile pressure operator. A proof must still bound
the convolution with every radial coefficient of the actual v and U0
profiles, their parameter derivatives and radial commutators, using
one specified analytic radius. The separate map
`partial_eta A_X` is not bounded in the underlying induced norm
and must not be estimated in isolation.

After that, quadratic interior pressure terms and the remaining
momentum sources must be controlled to derive the actual recurrence
(53). Theorem 1.1 is still not end-to-end Lean-certified, and this
work does not establish whole-space unforced Navier--Stokes blow-up.
The cumulative reader PDF is the original 16-page source unchanged
plus a 17-page cumulative amendment; do not treat it as a revision
of the original 16 pages in place.

## Leading- and quadratic-pressure exact cancellations (20 October 2026)

The current cumulative paper has a new part of Section 9:
`Leading_Profile_Pressure_Cancellation_Insert.tex` and
`Quadratic_Pressure_Symmetrization_Insert.tex`.
The 34-page reading PDF consists of the original 16-page source, unchanged,
followed by a single 18-page cumulative mathematical amendment.

**All five leading-profile terms**, with `v=V0/X`, `F=Uk`,
`Vk=XWk`, `B=2eta/L`, `G=d/L`, `K0=G d_eta v-B(v+D_X v)`,
obey the EXACT identity

```
S_k/X = (D_X+1)(v Wk)
      +U0[G d_eta+B(lambda_k-1-D_X)]Wk
      +F K0.
```

The first three original contributions form the radial total derivative
`X(D_X+1)(vWk)`; its pressure primitive is exactly `XvWk`.
After the physical pressure equation and `J1 Z` reconstruction the
full five-term contribution has radial valuation at least `I_(k+2)`.
The three grouped contributions have at most 2, 3, and 1 derivatives
of the unknown `F`, respectively.

The all-index **scalar** two-radial-lift inequality is, for
`0<=j<=3`, `a,b>=0` and `r=a+1`,

```
r^(3-j) w_(a,b+j) / [r^2(r+1)^2 w_(a+2,b)]
  <= [54 R^2 / (r rho^j)] * [25*3^(4-j)/(j+1)^2].
```

The non-leading positive-order quadratic velocity source ALSO
symmetrizes exactly over ordered pairs. Writing
`Q_k=sum_(i+j=k, i,j>=1) Wi Wj` and
`H_k=sum_(i+j=k) Ui[G d_eta+B(lambda_j-1-D_X)]Wj`,

```
Omega_k^(quad) = (X/2)(D_X+1) Q_k + X H_k,
Pi_(k+1)^(quad) = -(X/4) Q_k - (1/2) int_0^X H_k dx.
```

Its full contribution after pressure reconstruction also lies in
`I_(k+2)` coefficientwise. No general analytic operator norm
is inferred solely from these identities.

**Independent replay:** `leading_profile_pressure_exact.py` passed
72 exact symbolic source/pressure cases and 41,472 rational scalar
weight checks. `quadratic_pressure_exact.py` passed 120 symbolic
ordered-source/pressure cases and 29,106 rational ordered-pair
coefficient checks. Total: **70,770 independent exact test cases**.

**Lean proof scope:** `LeadingProfilePressure.lean` and
`QuadraticPressureCancellation.lean` contain finite algebraic
cancellation, primitive-factor, and valuation lemmas; the GitHub
workflow has been updated to compile both. They must not be
described as kernel-certified until the current run actually passes.

**Open gate, explicitly:** Prove the uniform induced Banach norm for
the complete `P_(k+1)^lead`, including all radial coefficients and
derivatives of the actual leading multipliers, and for the remaining
bilinear `H_k` operator. Then certify the other positive-order
momentum terms and full source-to-norm hypotheses before applying
recurrence (53) to the actual hierarchy. Theorem 1.1 remains open
as an end-to-end Lean/PDE assertion. Do not present these
finite source identities as a full Navier--Stokes singularity proof.


## Uniform radial convolution after two lifts — 20 October 2026

The cumulative article now includes `Weighted_Radial_Convolution_Smoothing_Insert.tex`,
a complete mathematical proof covering **unrestricted radial Taylor
series**, not only coefficient-monomial tests.

For the exact doubled weight (37), the convolution/Leibniz/Vandermonde
argument yields the explicit Banach multiplication constant
`||g F|| <= 64 ||g|| ||F||`, improving the paper's previous sufficient
`16*pi^4/9`.

For `n>=1, j=0,1,2,3, F in I_n`, define
`(R_(n,j)F)_(a+2)=(a+n+2)^(3-j)/(a+1)^2(a+2)^2 * d_eta^j F_a`.
The all-index two-lift estimate yields
`||R_(n,j)F|| <= D_j/(n+1) ||F||`, with
`D_j=675*2^(4-j)*R^2/((j+1)^2*rho^j)`.

The radial-convolution-inverse operator
`(C_(n,j)(g,F))_N =
 sum_(a+c+2=N) (N+n)^(3-j)/[(N-1)^2*N^2] * g_c * d_eta^j F_a`
maps to `I_(n+2)`, with norm
`<= [64 D_j/(n+1)] * (sum_(s=0)^(3-j) choose(3-j,s)
 ||D_X^s g||) * ||F||`, as long as those indicated norms are
finite on the **same** analytic domain.

The crucial proof detail is the exact binomial expansion
`(a+c+n+2)^(3-j) =
 sum choose(3-j,s) (a+n+2)^(3-j-s) c^s`.
It accounts for arbitrarily high radial multiplier frequencies
`c` through `D_X^s g`; the output inverse denominators are
monotone in `c`. It uses the derivative Leibniz rule and the
uniform product algebra bound, not a truncated coefficient grid.

The independently replayed exact tests passed **99,494 cases**:
500 one-dimensional telescoping-convolution inequalities;
48,510 Vandermonde/Leibniz coefficient inequalities;
48,048 two-lift `O(1/n)` weight ratios; and 2,436 index
polynomial/denominator comparisons (including multiplier indices
up to 1000). Script: `radial_convolution_smoothing_exact.py`.
The standalone Lean file `WeightedRadialConvolution.lean`
contains the finite index and polynomial proof gates and has been
added to pinned CI; its kernel status depends on the latest completed
run, not prior runs.

**Remaining genuine PDE bridge:** The complete source-native
leading-pressure formula and nonlinear `H_k` pressure term must be
normal-ordered into this *specific* controlled multiplier class,
including intermediate radial averages and the two unknown inputs
in bilinear terms, with actual imported leading-profile norm bounds.
This normal-ordering is NOT claimed by the new abstract theorem.
The physical full recurrence (53), normal convergence and
Theorem 1.1 remain open; no full Lean or global singularity
claim follows.


### Exact leading-pressure highest derivative — added source-native corollary

The updated cumulative paper now proves a sharper **source-specific**
piece of the pressure estimate. Writing the full five-interaction
leading-pressure operator with input F=U_k, at radial input a>=k and
leading-profile index c>=0, r=a+1, m=a+c+1, N=m+1, its exact third-
eta-derivative coefficient is

`[u_c G^3/(4 r m N^2)] * d_eta^3 F_a`,

where `u_c` is the c-th radial coefficient of U0 and
`G=(1-eta^2)/(1-2h eta^2)`.
The complete infinite radial sum of this **one** high-jet channel
obeys, conditionally on finite `||g||`, the induced-norm estimate

`||P_lead^(3)F|| <= [64 D_3/(k+1)] ||g|| ||F||`,
with `g=G^3 (U0+D_X U0)/4`.

The proof uses `m/r<=1+c` and the full convolution theorem;
there is no truncation of leading-profile Taylor coefficients.
It does NOT bound the remaining j=0,1,2 channels, which need their
own normal-form coefficient estimates. Nor is actual imported
profile regularity independently established.

`leading_pressure_normal_form_exact.py` verifies 24 exact rational
source-native jet expansions and 2,450 radial-index majorizations.
The Lean finite algebra/index claims are submitted in
`WeightedRadialConvolution.lean`; a green latest CI result, not
the PR's historic status, is needed for a kernel certification.

The additional research packet replays **101,968** exact cases
(99,494 algebra/convolution/smoothing and 2,474 source-specific).
The 36-page reader consists of 16 original pages and a 20-page
replacement cumulative scholarly amendment.

## All-four-jets leading-pressure theorem and first quadratic high-jet estimate (20 October 2026)

The cumulative manuscript now includes
`Full_Leading_Pressure_Normal_Form_Insert.tex` and
`Quadratic_Highest_Jet_Insert.tex`. The updated reading copy is
39 pages: the original 16 pages unchanged and one replacement
23-page mathematical amendment.

**Complete source-specific linear leading-profile pressure bound.**
For input `F=U_k in I_k`, `a>=k`, and a leading-profile
Taylor index `c>=0`, define `r=a+1`, `m=a+c+1`,
`N=m+1`, `alpha=r-D-lambda_k`, `epsilon=lambda_k-r`,
`theta=lambda_(k+1)-2A-m`. Expanding the complete five-source
pressure operator yields exactly 27 pair terms, distributed as
8, 12, 6 and 1 at axial-jet orders 0, 1, 2 and 3:
`P_(k+1)^lead(F)_(a+c+2) = -1/[4 r m N²] *
 sum_(j=0)^3 sum_((p,g) in E_j) p*g_c*d_eta^j F_a`.
The source-defined finite pair sets `E_j` are written explicitly
in the new manuscript subsection.

The polynomial factors satisfy `|p| <= (N+k)^(3-j)` and
`m/r <= 1+c`. With finite fixed-multiplier budgets
`M_j=sum_(E_j)sum_(s=0)^(3-j) binom(3-j,s)
 ||D_X^s(1+D_X)g||` on one common weighted analytic space,
the theorem proves
`||P_(k+1)^lead F|| <= C_lead/(k+1) ||F||`,
`C_lead=16*sum_(j=0)^3 D_j*M_j`,
`D_j=675*2^(4-j)*R²/[(j+1)²*rho^j]`.
This proves the complete **conditional** five-term leading-profile
operator estimate, including lower jets and multiplier commutators,
without a finite radial Taylor cutoff. It does NOT verify that
the particular imported leading profiles satisfy the common
holomorphic-radius hypotheses.

The exact verification script `full_leading_normal_form_exact.py`
passes all 27 symbolic normal-form terms, 27 concrete source cases,
and 45,360 exact-rational polynomial index bounds.

**Quadratic pressure highest-jet component.** For ordered
positive orders `i+j=k`, input radial degrees `a>=i`,
`b>=j`, `N=a+b`, its coefficient of
`partial_eta^3(U_j)_b` is exactly
`G³ (U_i)_a / [4(b+1)(N+1)(N+2)²]`.
The inequality
`(b+1)(N+1)(N+2)² >= (b+1)²(b+2)²`
and the two-lift theorem prove
`||Q_ij^(0,3)|| <= 1024*D_3/(j+1) *
 ||G³|| ||U_i|| ||U_j||`.
The source symbolic coefficient and 7,569 integer denominator
comparisons pass in `quadratic_highest_jet_exact.py`.

`FullLeadingPressureNormalForm.lean` includes finite all-index
parameter bounds, radial multiplier comparisons and the bilinear
denominator inequality. It is added to pinned CI, but the
**full Banach operator theorem is not in Lean**. Check the latest
CI outcome before claiming even these finite Lean lemmas have
kernel certificates.

**Open mathematical gates:** the remaining ordered quadratic
pressure terms (mixed derivatives and lower jets); other
positive-order momentum forcing channels; concrete radii of
the imported leading profiles; the complete source recurrence (53);
and the termwise physical PDE reconstruction. Theorem 1.1 and
a global unforced singularity are NOT proved by this release.


## Complete positive-order quadratic pressure estimate (20 October 2026)

The cumulative mathematical manuscript now inputs
`Complete_Bilinear_Pressure_Insert.tex` in its ninth
section. The merged reader is the unchanged original 16-page
preprint followed by one updated 26-page analytic supplement.

**Exact H_k normal form.** For an ordered pair i,j>=1, i+j=k,
input radial degrees a>=i,b>=j, N=a+b, r=b+1, and
B=2eta/L, G=d/L, the actual H_ij pressure contribution
after the pressure primitive, shifted Z, and J1 inverse is
a seven-channel sum of mixed derivatives
`d_eta^p U_i * d_eta^q U_j`. The exact seven pairs are
(0,0),(1,0),(0,1),(1,1),(0,2),(1,2),(0,3).
The normal form is given in the paper, including all derivatives
falling on B and G.

**Weighted bilinear majorant.** For d=p+q<=3 and
t=N+k+2 the two-lift scalar weight ratio obeys

`t^(3-d)*w(N,beta+d)/[(N+1)(N+2)^2*w(N+2,beta)]
 <= E_d=2304*2^(3-d)*R^2/rho^d`.

Instead of bounding bare derivatives of either U_i or U_j,
the proof uses the nonnegative unsigned Leibniz majorant
`M_(N,s)=sum_(a+b=N)sum_(u+v=s) binom(s,u)
 abs(d_eta^u U_i,a) abs(d_eta^v U_j,b)`,
bounded by `64||U_i||||U_j|| w_(N,s)`.
The complete multiplier derivatives are estimated by the
same 64-factor algebra bound, uniformly in both indices.

For E=[-1,1], 0<h<1/100, and 0<rho<=1/4, explicit Cauchy
estimates give simultaneous norm bounds
`||B||,||G||,||B'||,||G'||,||B''||,||G''|| <=25`.
This yields a uniform analytic bilinear bound
`||H_ij|| <= C_H ||U_i||||U_j||`,
`C_H=(64^2/4) A_H (E_0+2E_1+2E_2+2E_3)`,
`A_H=11*64^2*25^3=704000000`.

**Complete symmetrized W_i W_j contribution.**
The second quadratic pressure branch contains eight
mixed derivative splits. The two radial averages satisfy
`(a+1)(b+1)>=a+b+1` and absorb the high-jet
denominator, giving uniform bounds also for this branch.
Let `F_d=2304*2^max(2-d,0)*R^2/rho^d`
and `A_Q=32*64^2*25^3=2048000000`.
Then `||Q_ij|| <= C_Q ||U_i||||U_j||`, where
`C_Q=(64^2/8) A_Q*(F_0+2F_1+3F_2+2F_3)`.
The full ordered-pair **quadratic pressure**
contribution is bounded with `C_quad,p=C_H+C_Q`,
uniformly in i,j, with no radial Taylor truncation and no
new imported leading-profile hypothesis.

**Independent tests:** Local exact replay of the full H
source returned 216 cases, H smoothing 21,576 cases, mixed
Leibniz comparisons 28,665 cases and index constraints
10,404 cases. The Q source replay passed 96 cases,
Q smoothing 21,600 cases and the double-average inequalities
8,427 cases. Total 90,984 exact reproducible cases.
GitHub CI independently reruns seven/eight normal forms
and the scalar exact tests using
`complete_quadratic_pressure_exact.py`.

**Lean boundary:** `CompleteQuadraticPressureScalar.lean`
formalizes finite scalar index, denominator and coefficient
identities. Only a successful completed GitHub Actions job
can certify those finite declarations. The full Banach-space
majorant proof is provided in the mathematical manuscript,
NOT formalized end-to-end in Lean.

**Remaining:** other interior axial/swirl momentum products,
direct delayed forcing, concrete complex analytic radii of
imported leading profiles, and physical PDE reconstruction.
The complete lower-order recurrence (53) and Theorem 1.1
are NOT proved by the quadratic-pressure result alone.
No whole-space finite-energy unforced singularity follows.


## Direct momentum closure and a pressure-norm counterexample (20 October 2026)

**Mathematical advance:** Both positive-order momentum products in source
equations (25) and (26) admit a common uniform estimate after the
regular-singular inverse. With `B=2eta/L`, `G=d/L`,
`V_i=X W_i` and `alpha_(i,a)=1-(D+lambda_i)/(a+1)`,
the complete source is
`S_ij=(W_i(D_X+delta)F_j)+U_i[G d_eta+B(beta+lambda_j-D_X)]F_j`.
The paper proves, in the exact induced analytic norm,
`||(1/2)J_nu S_ij|| <= C_mom ||U_i|| ||F_j||`,
`C_mom=51200R(20+16/rho)`, valid for both swirl and axial
momentum, independent of i,j. It uses unsigned Leibniz
convolution and applies J_nu BEFORE bounding derivatives.

Both *complete* direct delayed momentum sources are also
uniformly bounded:
`||(1/2)J_nu Z^[2]_(beta,n-1)F||
  <= C_delay_mom ||F||`,
`C_delay_mom=1280000R(48+56/rho+8/rho^2)`.
The full normal form has coefficients
`c0=theta G B'+theta(theta-D)B^2`,
`c1=GG'+(2theta-D)GB`, `c2=G^2`.
The Cauchy radius and multiplier estimates include all derivatives
of B and G.

**Crucial counterexample/correction:** The pressure primitive
alone is NOT bounded in the unchanged pressure norm used by
amplitude (52). At h=1/200, rho=1/4,
`U_1=X/(1+4i eta)` belongs to I_1 with norm <=8R;
the isolated pressure component of the source-native
`U_1->V_1->-Z^[2] V_1->Pi_3` path is
`Pi_3^del=X^2 P(eta)`, with a fourth-order pole at
eta=i/4 whose exact Laurent coefficient is
`-921187500*i/4103684801` (nonzero).
Its derivative norm at radial degree two diverges in B:
`w_(1,b+3)/[4w_(2,b)] =
 (27R/(4rho^3)) (b+5)((b+1)/(b+4))^2 -> infinity`.
This refutes a general pressure-primitive boundedness claim in
the specified norm. It DOES NOT refute a particular local solution.

**Research status correction:** Although the momentum products
and direct delayed sources are now bounded, the existing full
amplitude A_n contains `||Pi_n||/(n+1)` in that same space.
Therefore the proposed recurrence (53) and the claimed
normal-convergence proof DO NOT FOLLOW without a repair.
An appropriate next target is a pressure-free coefficient
majorant using only the fully regularised pressure-to-velocity
composite, together with a separate weaker pressure space
(weight `w_(a,b+1)` is one possible candidate), followed by
independent physical-coordinate derivative control.

Reproducibility: `Direct_Momentum_and_Pressure_Norm_Insert.tex`
is included in the cumulative manuscript. The exact script
`momentum_pressure_obstruction_exact.py` verifies 432 ordered
momentum coefficient cases, 104 full Z-squared cases,
72,450 rational inverse multipliers, 12,880 unsigned Leibniz
comparisons, 100 exact pressure-ratio polynomial identities
and the nonzero analytic Laurent coefficient.
`MomentumAndPressureNorm.lean` submits finite scalar gates to
pinned GitHub Actions. They are NOT kernel-certified unless the
current workflow reports completion and success. No end-to-end
Lean formalization of the Banach estimates or Theorem 1.1 is claimed.


## Shifted pressure norm repair — 20 October 2026

**Research correction.** The original normalized amplitude (52) uses the
ordinary doubled analytic coefficient norm of pressure. This norm is
not preserved by an isolated delayed pressure primitive; the exact
counterexample and its nonzero fourth-order pole were already recorded
in the preceding tranche. We now define a weaker but source-compatible
pressure space using one derivative-index shift:

`||Pi||_P = sup_(a,b,eta in [-1,1]) |d_eta^b Pi_a|/w_(a,b+1)`.

**New exact all-index theorem.** For all a,b>=0,
`w_(a,b+3)/[(a+1)^2 w_(a+1,b+1)] <= 8 R/rho^2`
with sharp constant 8, since
`8(a+1)^4-(2a+1)(2a+2)(a+2)^2 =
2a^2(a+1)(2a+3)>=0`.
For the lower three jets, if n>=2,a>=n-2,0<=j<=3,
`(a+n+1)^(3-j) w_(a,b+j)/[(a+1)^2 w_(a+1,b+1)]
 <=32*3^(3-j) R*rho^(1-j)`.

**Uniform delayed pressure primitive.** For 0<h<1/100,
0<rho<=1/4 and n>=3, the *complete isolated* pressure source
generated by `-Z^[2]_(0,n-2)V_(n-2)` maps
`I_(n-2)` in velocity space to `I_(n-1)` in the
shifted pressure space, with uniform bound

`||Pi_n^del||_P <= (320000000 R/27) *
 sum_(j=0)^3 3^(3-j)*rho^(1-j) * ||U_(n-2)||_B`.

This includes variable-coefficient derivatives and all four
parameter jet orders, not just the principal symbol.

**Pressure-to-velocity boundedness.** The complete
`(1/2)J1 Z_(-2A,n)` from shifted P to original velocity B
has uniform bound

`||(1/2)J1 Z_(-2A,n)Pi||_B <=
(40/27)*(104R/rho^2+168R/rho) * ||Pi||_P`.

The fourth-order pressure pole in the original counterexample
becomes a fifth-order pole at the next radial degree after
regularisation and is compatible with the original velocity norm.
Exact output pole coefficient:
`1044012500000*i/19709998099203`.

**Source code and tests.**
`Shifted_Pressure_Repair_Insert.tex` is integrated into
`Direct_Momentum_and_Pressure_Norm_Insert.tex`, with the
cumulative manuscript abstract revised accordingly.
`ShiftedPressureRepair.lean` contains scalar polynomial/valuation
proof gates, NOT the full pressure Banach-space theorem.
`shifted_pressure_exact.py` replays 92,160 four-jet weight
identities and bounds, 90,720 pressure-to-velocity scalar ratios,
62,220 shifted pressure multiplier/Leibniz cases and exact
symbolic pole/restoration identities.
All 245,100 finite core coefficient checks passed locally.

**What remains open.** The proper pressure-space shift repairs the
isolated delayed channel, but the *complete pressure sequence*
has not yet been controlled in shifted P norm, nor has every
lower-order velocity source been collectively shown to satisfy
the corrected velocity-only majorant recurrence. The inherited
leading-profile complex analytic radii and differentiated
physical PDE reconstruction remain to be independently certified.
Consequently no full end-to-end Lean proof or theorem 1.1 proof
is claimed. Latest new Lean source was submitted to GitHub Actions,
but kernel status is PENDING until the run completes successfully.


## Three additional pressure-source bounds in the shifted space — 20 October 2026

The next mathematical release, source `Shifted_Pressure_Source_Closure_Insert.tex`,
proves in the one-derivative-loss shifted pressure norm:

1. **Sharp axis primitive:** `||int_0^X F dx||_P <= (16/3) R rho ||F||_B`.
   The constant is attained by the degree-zero input and follows from
   `4(a+1)^3(2a+3)-3(a+2)^2 =
   a(8a^3+36a^2+57a+32)>=0`.
   The complete swirl-square source in (27) is thereby bounded by
   `(1024/3) R rho |C|^(-2) sum_(i+j=n) ||phi_i||||phi_j||`,
   including the leading/current index pairs.

2. **Exact radial-Laplacian pressure cancellation:** the term
   `-2X V_(k,XX)` in Omega_k gives
   `Pi_(k+1)^lap = partial_X V_k` (k>=1, zero axis constant).
   In source variables its degree-a coefficient is
   `(a+1-D-lambda_k) B F_a-G partial_eta F_a`.
   The one-shift weight absorbs both contributions uniformly:
   `||Pi_(k+1)^lap||_P <= (80/27)(32 rho+13)||U_k||_B`.

3. **Complete direct time-pressure composite:** the term
   `T_(0,k)V_k` yields a two-eta-derivative, six-term
   variable-coefficient normal form after one axis primitive.
   Its source-native proof gives
   `||Pi_(k+1)^time||_P <=
    (1280 R/27)((32/3)rho+12+8/rho)||U_k||_B`.
   The proof covers all derivative orders, the similarity shift,
   and all derivatives of the fixed rational coefficients.

In combination with the prior *isolated* delayed-pressure theorem,
these bound the three direct linear Omega_(n-1) contributions
(n>=3) and the entire swirl-square pressure source in shifted P.
This is an explicit substantial reduction of the two-space
recurrence problem, NOT the complete recurrence.

**Exact regression:** `shifted_pressure_sources_exact.py`
replays 21,675 axis-primitive weight identities,
21,675 Laplacian pressure weight ratios, 65,025 time-pressure
jet inequalities, and 24 exact symbolic source cases:
**108,375 coefficient checks and 24 symbolic cases** pass.
`ShiftedPressureSourceGates.lean` encodes the finite all-index
scalar polynomial inequalities and exact source algebra,
with a new CI compilation gate. The full analytic Banach
source theorems are written in the paper, not end-to-end
formalized in Lean; check a completed successful Actions
run before treating these new declarations as kernel-certified.

The combined reader is **50 pages**: the original 16-page
preprint unchanged plus one updated 34-page cumulative
mathematical amendment. Editable LaTeX and the independently
tested full regression are included in the 20-file ZIP release.

**Remaining critical gates:** prove shifted-P pressure primitive
bounds for the five leading-profile Omega interactions and the
ordered positive-order quadratic Omega terms (previous post-J1
velocity estimates do not suffice); certify the actual imported
leading-profile complex radii; derive the full two-space
recurrence including finite startup data; and prove differentiated
physical-coordinate PDE reconstruction. Neither Theorem 1.1
nor a global unforced finite-energy singularity has been
proved in this release.


## Direct source closure in the shifted pressure space — 20 October 2026

This checkpoint extends the pressure-norm repair to the **other direct
sources**, retaining the original velocity space `B` and the weaker
one-derivative-shifted pressure space `P` with
`||Pi||_P = sup |partial_eta^b Pi_a|/w_(a,b+1)`.

The updated cumulative paper inputs
`Shifted_Pressure_Source_Closure_Insert.tex` as a continuation of
`Shifted_Pressure_Repair_Insert.tex`. It is distributed as one
**50-page reader**: the deposited original 16 pages unchanged, plus
one replacement 34-page cumulative mathematical amendment.

- **Sharp axis primitive:** `||int_0^X F dx||_P <=
  (16/3) R*rho ||F||_B`. Equality of the coefficient constant
  occurs at radial and axial indices `(a,b)=(0,0)`.
  The swirl-square pressure source consequently has bound
  `(1024/3)R*rho*|C|^-2*sum_(i+j=n)||phi_i||||phi_j||`.
- **Exact radial-Laplacian cancellation:** the isolated source
  `-2X V_(k,XX)` contributes `Pi_(k+1)^lap=d_X V_k`
  with axis integration constant zero, and
  `||Pi_(k+1)^lap||_P <=
  (80/27)(32*rho+13)||U_k||_B`.
- **Full direct time pressure:** the source `T_(0,k)V_k`
  has a six-term, 0/1/2-derivative normal form including
  all `B,G,L` multiplier derivatives, and
  `||Pi_(k+1)^time||_P <=
  (1280R/27)*[(32/3)rho+12+8/rho]||U_k||_B`,
  independently of k and the radial Taylor cutoff.
- **Previously proved isolated delayed pressure:** the direct
  `-Z^[2]_(0,k-1)V_(k-1)` primitive is bounded into the
  same shifted pressure space.

Reproducibility: the new
`ShiftedPressureSourceGates.lean` contains scalar arithmetic
and source identities; `shifted_pressure_sources_exact.py`
replays the source and analytic-weight comparisons. Independently
executed local tests passed **108,375 exact coefficient comparisons**
(21,675 axis primitive, 21,675 Laplacian, 65,025 time pressure)
and **24 symbolic source-normal-form cases**.
New Lean declarations are only submitted to the pinned GitHub
workflow; do not report a kernel PASS until the relevant CI run
finishes successfully. The written Banach-space theorems are not
end-to-end Lean formalized.

**Remaining critical gates:** Establish shifted-`P` norm
bounds for the bare leading-profile pressure interactions and the
positive-order quadratic pressure primitives; then jointly prove
the full simultaneous two-space recurrence, certify the imported
leading-profile analytic radii, and reconstruct the physical PDE
with termwise derivative justification. Estimates for pressure
*after* final `J1 Z` reconstruction do not by themselves bound
the bare pressure primitive. The full Theorem 1.1 remains unproved
and no whole-space unforced finite-energy blow-up follows.


## Completion of the shifted-pressure source ledger (20 October 2026)

The newly added cumulative theorem
`Remaining_Shifted_Pressure_Insert.tex` proves the two previously open
bare-pressure estimates. The reading PDF is the unchanged 16-page
deposited paper plus one replacement 37-page cumulative mathematical
amendment (53 pages total). The original Zenodo record is not modified.

1. The exact mixed product estimate is
   `||fP||_P <=64||f||_B||P||_P`, for arbitrary nontruncated
   analytic radial Taylor series. The proof uses the positive
   differentiated coefficient ratio, Vandermonde's inequality,
   and two telescoping index convolutions. This is a **mixed**
   algebra statement; it does NOT claim that P is an algebra.
2. The elementary shifted-pressure operations obey
   `||XP||_P <=4R||P||_P`,
   `||int_0^X P||_P <=4R/(m+1)||P||_P` for `P in I_m`,
   and `||int_0^X partial_eta P||_P <=8R/rho||P||_P`.
   The radial-velocity coefficient satisfies
   `||W_k||_P <= C_W||U_k||_B`,
   `C_W=64(4rho||B||_B+||G||_B)<=1600(4rho+1)`.
3. **All five leading-profile pressure interactions** have an exact
   radial integration-by-parts identity
   `-2 Pi_(k+1)^lead = X(v-BU0)W_k
     +int_0^X[ U0 G d_eta W_k
       +B(lambda_k U0 +D_X U0)W_k +U_k K0]dx`.
   This yields `||Pi_(k+1)^lead||_P <=
   C_lead,P||U_k||_B`, with the explicit constant in the
   new manuscript; it is uniform in k **conditional on**
   `U0,D_X U0,v,D_Xv,K0` having finite norms on a common
   analytic domain. That domain has not been checked for the
   *actual imported* leading profiles.
4. **All positive-order quadratic bare-pressure terms** have the
   exact symmetrized ordered-pair radial integration-by-parts
   identity shown in the manuscript. The apparent `D_XU_i`
   factor is divided by the total radial degree:
   `0<=(a+lambda_j)/(a+b+1)<=1` for `a>=i,b>=j`.
   The two radial averages also satisfy
   `(a+1)(b+1)>=a+b+1`. Combining the mixed product
   and unsigned jet majorants proves
   `||Pi_(i+j+1)^quad,ij||_P
      <= C_quad,P||U_i||_B||U_j||_B`.
   The constant in the manuscript is explicit, independent of
   both orders and does not require the shifted pressure space
   to multiply with itself.
5. This gives a **complete pressure-source inequality**:
   `P_n <= C_sw sum_(i+j=n)B_iB_j
       +(C_P,time+C_P,lap+C_lead,P)B_(n-1)
       +C_P,del B_(n-2)
       +C_quad,P sum_(i+j=n-1,i,j>=1) B_i B_j`,
   for the full source ledger and the fixed leading multipliers
   assumed finite. The `phi_0 phi_n` term is current-order and
   must remain in the coupled velocity feedback system.

Independent local script `remaining_shifted_pressure_exact.py`
passed **38,539** finite exact checks: 840 mixed two-index
convolution sums, 31,850 shifted-weight transfer comparisons,
5,832 ordered-pair radial inequalities, and 17 symbolic
leading/quadratic integration-by-parts identities.
`RemainingShiftedPressure.lean` encodes finite scalar transport,
double-average and valuation gates. The **full** mixed Banach
algebra and source theorems are manuscript proofs, NOT completely
formalized Lean statements. Await a completed successful CI run
before describing the finite Lean lemmas as kernel-certified.

**Still open:** Verified imported leading-profile complex analytic
radii, the full current-order feedback and actual closed velocity
recurrence, the physical-coordinate chain-rule/pressure
reconstruction, and an end-to-end Lean certification of Theorem 1.1.
No whole-space finite-energy Navier--Stokes singularity is claimed.


## Source-derived leading radius and current pressure feedback — 20 October 2026

The new `Leading_Profile_Radius_and_Current_Feedback_Insert.tex` in the
cumulative manuscript studies three distinct issues.

**Imported leading-profile regularity.** Appendix B, Proposition B.2
of OpenAI, *Finite Time Blowup for Navier–Stokes* (2026), supplies
analyticity of the chosen source leading profile with Y=Lambda X on
a common complex neighborhood; its proof selects a radial coefficient
radius S in (4.1,20). If one freezes an admissible Lambda,C and
exhibits a δ-neighborhood and uniform complex bound M for the
actual profile, then R<=S/(8 Lambda), rho<=δ/8 yield
||F(ΛX,eta)||_B<=M. The same Cauchy transfer proves finite
norms of every fixed D_X^p ∂eta^q leading multiplier on smaller
radii. This is **qualitative/existential** from the source, not
a numerical fixed-parameter interval certificate. The source
does not provide a chosen numeric Lambda,C,δ,M quadruple.

**Current-order pressure gain.** For every F in I_n(B),
`||int_0^X F||_P <=8R*rho/(n+1)^2 ||F||_B`.
Proof: the exact weight ratio is maximal at b=0; its
polynomial radial bound is
`2(a+1)(2a+3)-(a+2)^2=3a^2+6a+2>=0`.
The two ordered source pairs (0,n),(n,0) in (27) contribute
`Pi_n^cur=(2/C²)int_0^X phi0 phi_n dx` and therefore
`||Pi_n^cur||_P <=
1024 R*rho*||phi0||_B/(|C|²(n+1)^2)*||phi_n||_B`.
Applying the pressure-to-velocity operator adds its fixed
norm C_E. This remains a **current-order K_Uphi block**,
never part of lower-order source forcing.

**Conditional pressure reconstruction.** Given
`B_n=||phi_n||+||U_n||<=M*T^n/(n+1)^2`, the complete shifted-P
ledger yields `||Pi_n||_P<=Gamma*T^n/(n+1)^2`, with an explicit
Gamma in the paper. If all velocity and pressure bounds hold,
the physical-coordinate transformation has nonzero Jacobian
`L=1-2h eta²` on the inner real core, and differentiated
series can be reconstructed termwise on compact q>0 regions.
The geometric velocity bound is still a hypothesis, not proved
by this implication.

**Noncircular startup-radius issue.** The earlier suggestion
'choose rho below the radii of finitely many startup orders
below N*(rho)' is not generally valid without a uniformity
theorem, because N* grows when rho shrinks. The model
radii rho_n=exp(-n), cutoff N*(rho)=ceil(1/rho)+1,
all rho_n>0, admit no self-consistent 0<rho<=1.
This is a counterexample to that radius-selection logic,
not to the actual Navier–Stokes hierarchy.

**Reproducibility.** Script `current_order_feedback_exact.py`
passes 43,200 rational source-weight identities, 45 symbolic
current-swirl pressure checks, and six finite Euler/Cauchy envelope
checks. `CurrentPressureFeedback.lean` contains only finite scalar
polynomial and coordinate identities; a completed successful Actions
job, not merely submission, is required before calling them
kernel-certified. The full Banach/PDE theorem is not encoded there.

**Remaining gates:** certify one fixed admissible leading-profile
complex enclosure; establish a *noncircular common analytic width*
including every startup coefficient; audit the entire velocity
forcing and current feedback in the induced norm; then derive
the closed recurrence and justify all physical derivatives.
Theorem 1.1 remains unproved; this is not a global unforced
Navier–Stokes blow-up proof.


## Fixed-radius factorial feedback resolvent and two-shift majorant (20 October 2026)

The cumulative manuscript now inputs
\`Fixed_Radius_Volterra_and_Two_Space_Majorant_Insert.tex\`. The updated
research reader has **58 pages**: original deposited 16-page source
unchanged plus one replacement 42-page cumulative mathematical amendment.
The work stays on draft PR #1; do not merge the original source or claim
its Theorem 1.1 proved.

**Mathematical theorem.** With all fixed leading-profile multiplier
norms finite on the same selected analytic coefficient space, the actual
four current-order block maps \(K_n\) raise radial valuation and satisfy
\`K_n(I_m^2) subset I_(m+1)^2\`,
\`||K_n F|| <= C_*||F||/(m+1)\`
for all \`m>=n>=1\`. The source similarity shift \`lambda_n=2hn\`
does not spoil this because \`n<=m\`. The factorial iteration yields
\`||K_n^ell|| <= C_*^ell*n!/(n+ell)! <= C_*^ell/ell!\`.
Hence the Neumann series converges for EVERY n, independently of whether
\`||K_n||\` is less than one, with
\`||(I-K_n)^(-1)|| <= exp(C_*)\`.
This eliminates the earlier *radius-dependent finite-startup cutoff*
for the current-order inversion, on a fixed common analytic domain.

**Two-shift quadratic majorant.** The full source ledger contains
\`sum_(i+j=n)B_i B_j\` and \`sum_(i+j=n-1)B_i B_j\`.
A constructive majorant with both present is proved: if
\`B_n <= H[B_(n-1)+B_(n-2)+Q_n+Q_(n-1)]\`,
then taking \`M=1/[32(1+H)]\` and sufficiently large T as stated
in the manuscript gives \`B_n<= M T^n/(n+1)^2\`.
The Q_(n-1) term is not silently merged into Q_n.

**Source-to-majorant reduction, strictly conditional.** Combining
previously proved source-specific momentum and shifted-pressure operator
norms yields conservative budgets
\`L1=2*C_del,mom+C_E*C_L\`,
\`L2=C_E*C_D\`,
\`Q0=2*C_mom+C_E*C_sw\`,
\`Q1=C_E*C_quad,P\`.
If the proposed *unforced* coefficient equations and startup
normalization match the exact ledger on ONE independently selected
common analytic domain, the source estimate together with the factorial
inverse yields the above majorant with
\`H=exp(C_*)*max(1,L1,L2,Q0,Q1)\`.
This is a **conditional local reconstruction criterion**,
not a proof that those source and profile hypotheses hold.

**Independent exact replay:** \`fixed_radius_volterra_exact.py\`
passed 20,520 rational shift/index comparisons, 4,410 factorial
comparisons, 1,588 two-shift convolution bounds, six majorant budget
settings, and nine finite triangular inverses even at strong startup
feedback C=80. Scalar comparison total: **26,524 passed**, plus
nine finite inverse checks. This does not replace the analytic proof
or verify physical Navier--Stokes.

**Lean status:** \`FixedRadiusVolterra.lean\` contains only elementary
scalar radial/index and delayed-ratio gates. The GitHub workflow was
updated to invoke it. It is NOT kernel-certified until the corresponding
run finishes successfully; the Banach operator resolvent and the PDE
source hierarchy are not formalized end-to-end.

**Open gates:** (i) freeze and independently verify a specific
admissible tuple of source parameters and common complex profile radius,
(ii) check the correspondence of every actual n=1,2 startup and
n>=3 unforced coefficient equation and pressure datum with the
source-specific norm lemmas, (iii) prove physical-coordinate termwise
reconstruction and residual zero, (iv) formalize these in Lean.

**Source provenance:** OpenAI, *Finite Time Blowup for Navier--Stokes*,
Appendix B, Proposition B.2, constructs leading profiles for a broader
construction whose full-space theorem involves **smooth compactly
supported forcing**. The local analytic profile does NOT itself
establish the user's proposed unforced global singularity.


## Source-level startup and physical-reconstruction audit — 20 October 2026

The cumulative mathematical amendment now includes
`Source_Level_Startup_and_Reconstruction_Insert.tex` (source-derived
from equations (5.2)--(5.6) and Appendix B of OpenAI's
*Finite Time Blowup for Navier--Stokes*, 2026). The **60-page**
reader preserves the original deposited 16-page paper unchanged
and appends a 44-page cumulative amendment. The original
Zenodo upload is not modified.

**Source leading-profile provenance.** The actual leading
pressure trace `Pi0(0,eta)` comes from the outer matching
Lemma A.5; the axis data use `U_*=4eta+j0` with
`0<j0<=0.05`. Appendix B then chooses regularization
parameters `delta_*,sigma_*`, a zero-free complex
neighborhood `Omega`, and `zeta_*=-L H_*/(H_*²+sigma_*²)`,
`phi_*=exp(Lambda*integral zeta_*)`. Only afterward
does it choose `Lambda` sufficiently large and `C`
large enough for the complex supremum of `phi_*`.
The paper gives existential analytic regularity but no
independently frozen numerical parameter/norm certificate for
all those objects. The example `h=1/200,C=3` in symbolic
test scripts is merely a generic algebraic test, NOT the
source's certified leading profile.

**Exact order 1 and 2 forcing:** The new note lists
`Omega_0` and `Omega_1`, the `Pi_1` and `Pi_2`
pressure primitives, and all swirl/axial lower-order sources.
The order-1 pressure known source is
`-1/2 int_0^X Omega_0/x dx`;
at order 2 it is
`int_0^X [C^-2 phi_1² - Omega_1/(2x)]dx`.
`Omega_1` contains `-Z^[2]_(0,0)V_0`.
The current pressure term `2C^-2 phi_0 phi_n`
is not double-counted in lower-order forcing.
Positive-order pressure gauge `Pi_n(0,eta)=0`
is distinct from prescribed `Pi_0(0,eta)`.

**Exact algebraic verification:**
`startup_source_symbolic_exact.py` independently checks
39 source coefficient identities across n=1 and n=2 on
generic polynomial probes; tests include incompressibility,
axis-regular Omega, complete pressure derivative,
current/known split, and both momentum equations.
`startup_index_exact.py` checks **2,003,000** ordered
convolution-index pairs over n=1..2000 and the
triangularity of Omega_(n-1), plus 20 exact rational
similarity Jacobian/shift examples.
A nonzero n=1 delayed swirl source is reproduced on
one generic polynomial probe to demonstrate that the
startup system is nontrivial; the probe does NOT solve
the actual leading equations.

**Conditional physical reconstruction.** From
`tau=q(1-eta²), z=q^D eta, X=r²/(2q)` the exact chain
rules `T_a,Z_a` and Jacobian `L=1-2h eta²>0` follow.
If a fixed analytic leading solution, ALL actual positive
order equations, pressure gauges, and locally normally
convergent physical derivatives are independently verified,
then termwise reconstruction has exactly zero unforced PDE
residual. Those hypotheses are NOT certified in this update.

**Lean scope:** `StartupSourceAudit.lean` proves only
finite ordered-pair and Jacobian scalar gates if/when the
pinned GitHub Actions job succeeds. The actual source
functions, Banach-space inverse and full physical PDE
are not formalized in Lean. The earlier source whole-space
result uses smooth compactly supported forcing and its
own formal higher-order background is made smooth by
order-dependent cutoffs; this is not an unforced proof.
Maintain the PR as draft and do not claim Theorem 1.1.


## Explicit source axis-data complex fence and first two radial jets (20 October 2026)

A new cumulative scholarly subsection is included as
`Axis_Profile_Geometric_Fence_and_Jets_Insert.tex`.
The canonical attached reading PDF is 62 pages: the unchanged original
16-page preprint and a replacement 46-page mathematical amendment.
The attached research ZIP (29 entries) contains the complete editable
TeX, source checker scripts, finite Lean gates and a verification status
report. These attachments do NOT update the existing Zenodo deposit.

**Proved denominator geometry (universal ranges).** For all
`0<h<=1/100`, `0<j0<=1/20`, `0<sigma<=1/10`, and
`Hstar(z)=(1/2-h)z+(1-z²)(4z+j0)`, let
`Omega_sigma={|Re z|<=11/10, |Im z|<=sigma/100}`.
The exact proof shows
`|L(z)|>=607/625`,
`|Hstar(z)^2+sigma^2|>=9 sigma²/16`,
and `|zeta_star(z)|<=25/sigma²` for
`zeta_star=-L Hstar/(Hstar²+sigma²)`.
For `varphi_star=exp(Lambda integral_0^z zeta_star)`,
`sup|varphi_star|<=exp(30 Lambda/sigma²)`.
Thus `C>=exp(30 Lambda/sigma²)` suffices for **only**
the normalization (B.16), and the degree-zero analytic
weighted norm of `g=varphi_star/C` is at most one if
`rho<=sigma/1600`.

**Diagnostic, NOT source-admissible tuple.**
`h=1/200,j0=1/50,sigma=1/100` produces the exact polynomial
`Hstar=-4z³-z²/50+(899/200)z+1/50`;
`Hstar(-1/200)=-99/40000`,
`Hstar(-1/250)=63123/31250000`, and
`-Wstar>=14701/5000>2.8` on the real physical strip.
The rational multiplier is regular on
`|Re z|<=1.1,|Im z|<=1e-4`, with
`|zeta_star|<=250000`. This does NOT verify that this
specific sigma satisfies (B.2) because Zstar depends on
the un-frozen actual pressure trace.

**Leading-profile radial jet formulas.** Coefficient extraction from
source (B.12)–(B.15) now gives exact expressions for
`Phi=1+p1 Y+p2 Y²+...`,
`u=q1 Y+q2 Y²+...`, with
`p1=[-chi+(Wstar+h(1-2eta Ustar))/(Lambda L)]/4`,
`q1=-Zstar/(2L)`, and source-defined explicit
`p2=(-chi*p1+R11/Lambda)/12`,
`q2=R21/(8Lambda)`. Also
`Pi=Pi0+(g²/Lambda)Y+(g²p1/Lambda)Y²+...`.
All eight generic formal coefficient identities and the
rational safety constants pass independent SymPy exact replay.
These are **radial Y coefficients of the leading profile**,
not solutions of the distinct similarity-order n=1,2 startup
correction systems.

**Blocking source dependencies.** The actual prescribed pressure
trace is the Lemma A.5 full exterior-schedule integral
`Pi0(eta)=-(1/2) int E_id,sched(y,eta)² dy`.
Until its concrete analytic integral bounds are frozen,
(B.2) cannot be checked numerically. Further unknown
thresholds are `Lambda0`, `C0(Lambda)` and the quantitative
B.2 contraction ball. No actual fully admissible numerical
leading profile or n=1/n=2 unforced correction solution has
yet been certified. Theorem 1.1 and whole-space unforced
singularity remain OPEN.

**Lean and exact replay:** `AxisProfileFence.lean` contains
finite rational polynomial certificates, while the complex
zero-free proof is mathematical prose, not Lean-formalized.
`axis_profile_fence_exact.py` and
`axis_profile_radial_jets_exact.py` are in the pinned CI
workflow. Do not call them kernel-certified until a successful
run is returned. Existing Mathematica/SymPy probes are not
a numerical enclosure of the originating Appendix-A pressure
integral and do not turn a forced published construction into
an unforced proof.


## Outer pressure measure and quantitative Appendix-B (B.2) (20 October 2026)

This round proves a source-preserving reduction of the actual axis
pressure trace, rather than replacing it with an invented numerical
pressure function. In Lemma A.5 of OpenAI's *Finite Time Blowup for
Navier--Stokes*, the pressure-neutral angular correction bumps are
omitted and each remaining schedule stage is exactly
`E_id,sched(y,eta)=c(y)(1+eta²)^(-theta(y))`, with `0<=theta<=1`.
The measure `mu = (theta)_#(c(y)^2 dy)` on [0,1] is positive and finite,
and the reference inner tail contributes an atom of mass `5Pstar²` at
`theta=1`. Thus
`Pi0(eta)=-1/2 int_[0,1](1+eta²)^(-2s)dmu(s)`
is an **exact** representation of the prescribed source pressure.
Writing `m=-Pi0(0)=mu([0,1])/2`, one gets
`|Pi0'|<=2m`, `|Pi0''|<=8m` on [-1,1] and the
source lower bound `Pi0<=-(5/2)Pstar²/(1+eta²)^2`.
On the complex rectangle
`|Re eta|<=1.1,|Im eta|<=0.1`,
`|Pi0(eta)| <= (100/99)^2 m`, with Cauchy derivative
bounds `|Pi0^(b)| <= (100/99)^2 m b! 20^b`.
These statements are mathematical analytic consequences of the source
schedule's positive-measure form; **m is not numerically frozen**.

A **constructive condition (B.2) theorem**, requiring the source's
`Pstar>=1,0<h<=1/100,0<j0<=1/20`, sets

`K=200(1+m), delta_star=j0/12, epsilon=j0/(12K),
 sigma_star=epsilon/30=j0/[72000(1+m)]`.

It proves the unique real Hstar zero eta0 lies in
`(-j0/4,-j0/5)`, `Zstar(eta0)>j0/3`,
`|Zstar'|<K`, and
`|Hstar(eta)|>(2/5)|eta-eta0|` on [-1,1].
Therefore `|Zstar|<=delta_star` implies
`chi=Hstar²/(Hstar²+sigma_star²)>=144/145>0.99`.
The strict margins persist on a slightly larger real compact interval.

The proof is in
`TerminalCore2026/Outer_Pressure_Measure_and_Admissibility_Insert.tex`;
its exact rational replay is
`TerminalCore2026/outer_pressure_measure_B2_exact.py`;
finite scalar Lean gates are in
`TerminalCore2026/OuterPressureB2Scalar.lean`.
CI has been updated to check both. The complex and measure arguments are
**not** formalized in Lean. Numerical synthetic masses in the checker
are NOT the original outer schedule.

The associated reading PDF is the original 16-page deposited paper
unchanged plus a revised 48-page mathematical amendment: **64 pages**.
The 26-entry reproducibility packet contains the manuscript TeX,
exact replay and source proof limitations, with a SHA256 manifest.

**Still missing:** a frozen actual exterior schedule and numerical
`m`, explicitly chosen large parameters `Lambda,C` with a
verified Appendix-B contraction map, actual n=1/n=2 unforced
coefficient solutions on one common domain, and an end-to-end
physical Navier--Stokes residual proof. Appendix-B (B.2) is only
one admissibility condition; this round does NOT certify a complete
leading profile or establish Theorem 1.1. The source's whole-space
blowup theorem uses smooth compactly supported forcing.


## Exact exterior pressure mass and stagewise certification (20 October 2026)

This revision extends the verified source pressure-measure theorem
by returning to the actual Appendix-A moment-matched schedule.
It identifies an **exact finite-stage-plus-tail decomposition**

`M0 = (5/2)Pstar^2 + (1/2)int_0^YT c(y)^2 dy
       + cT^2/[2(1+2h)]`.

The last term is an exact tail integral because the source
sets `l=-h` and removes all eta dependence beyond YT.
The first source transition has `0<=l<=3/5`
for one unit; the following axial transition has `l=0`
for length `Td=e^Md+10`. Both retain exponent theta=1.
Thus the sharper **source-specific** inequality holds:

`M0 >= (3 - exp(-1-Td)/2) Pstar^2
     > (3 - exp(-1-Td)/2) exp(2Td)`.

The pressure positive measure has at least
`(6-exp(-1-Td))Pstar^2` concentrated at exponent one.
These bounds are exact and do NOT require arbitrarily selecting
moment-correction amplitudes.

For a frozen source schedule whose successive lengths and
logarithmic slopes are independently enclosed, the manuscript
gives explicit interval formulas for every finite stage and
the final tail. `outer_schedule_enclosure.py` implements these
using outward-rounded interval exp arithmetic; the included
default benchmark is clearly labelled **NOT source-admissible**.
Its pressure mass numerical interval is NOT a numerical value
for the actual Appendix-A family.

The previously certified complex denominator gives a
bound for the source norm (B.4)
`||chi|| <= 301/sigma_star^2` and its multiplication operator
`M_chi <=19264/sigma_star^2`. The actual angular
factorial inverse obeys
`||(1 + J2*chi/2)^(-1)|| <= exp(770560/sigma_star^2)`.
This is an explicit linear inverse bound only.

Given independently validated remainder bounds `A1,A2`,
Lipschitz bounds `L1,L2`, an axis Banach ball radius `r`
and inverse bound `B`, the source Appendix-B fixed-point map
is a strict contraction under the sufficient **conditional**
threshold
`Lambda >= 2*max(40*B*A1/r,80*A2/r,40*B*L1,80*L2)`.
The actual numerical `A_i,L_i` and matching schedule do NOT
appear as a frozen validated dataset in the source, so no
concrete numerical Lambda, C, or complete leading profile is certified.

The new theorem is in
`Outer_Pressure_Schedule_Enclosure_Insert.tex`.
`stagewise_source_checks.py` tests the exact early-stage/tail
identities, 10,000 Cauchy derivative ratios and conditional
threshold arithmetic. `SourceScheduleMass.lean` submits only
finite scalar polynomial/rational gates to CI. The complex,
interval-stage and PDE conclusions are **not** Lean formalized.

The new reader PDF contains the original 16 pages unchanged
and a replacement 50-page cumulative amendment (66 pages total).
The reproducibility ZIP includes 27 source/test/verification entries
and a SHA-256 manifest. Its sources must be read with the
explicit release note: NO actual validated M0, no nonlinear
fixed point, no actual n=1,2 startup corrections, and no
unforced Navier--Stokes physical residual theorem.
The original OpenAI result has smooth compactly supported forcing.


## Narrow fixed Appendix-A pulse and moment correction certificate (20 Oct 2026)

A source-specific result has been added in
`Pulse_Moment_Matrix_and_Amplitude_Insert.tex`, using exactly
Appendix A equations (A.5), (A.9), (A.19)-(A.20), and the
translated two-bump moment matrix (A.1) of OpenAI's
*Finite Time Blowup for Navier–Stokes*.

Because the source smooth step satisfies
`sigma(t)+sigma(1-t)=1`, its integrated pulse shape obeys
`phi_b(x)=x-1/100` for `x>=1/50`.
Elementary exponential integration with two controlled
transition errors gives the **rigorous rational interval**

`0.2450478 < K_b < 0.245052`.

Its principal quadratic source amplitude
`A0^2 K_b=(1-exp(-26))/4` is therefore
`1.010045 < A0 < 1.010055`, **independent of the unchosen
exterior moment-correction amplitudes**.

For the *actual* moment amplitude satisfying
`F(A,eta)=K_b A^2-(1-exp(-26))/4+E(A,eta)=0`,
the sufficient validated threshold
`|E|<=0.0004` and `|d_A E|<=0.01`
on `[1.009,1.011]x[-1,1]` implies one and only one
`A(eta) in (1.009,1.011)`, with
`|d_eta A|<=sup|d_eta E|/0.48`. The actual
source's `E(A,eta)` has NOT yet been enclosed to this
threshold for one frozen source-admissible schedule.

The normalized two-bump correction matrix in (A.1), using
nonnegative unit-mass width-0.3 translates separated by
`Delta=2`, has for `0<lambda<=1/20`:
`|det B| >= (1369/400)*lambda>3lambda` and
`||B^(-1)||_infty<2/lambda`.
Thus the corrected coefficients can be enclosed once the
*actual normalized* moment discrepancies are enclosed.

The independent Python Fraction script
`pulse_moment_exact.py` passes the exact exponential-series,
fixed-pulse, root-sign and matrix-condition arithmetic.
`PulseMomentSharp.lean` submits finite rational gates, NOT
a kernel certificate of the smooth-step integrals. The latest
GitHub Actions status must be checked separately.

The downloadable research reader has **68 pages** (original
16 pages unchanged plus one revised 52-page amendment).
The **30-file** source/verification ZIP includes a
SHA-256 manifest and a precise proof-status note.

**Still open:** independently freeze the true exterior schedule,
bound its `E(A,eta)` and normalized moment discrepancies,
certify the actual pressure mass `M0`, give concrete source
parameters and Appendix-B nonlinear contraction constants,
and solve/verify the distinct unforced `n=1,2` systems.
The originating whole-space theorem includes smooth forcing;
no unforced theorem or global singularity is established here.


## Exact Appendix A (A.19) quadratic remainder (20 October 2026)

**New source-level identity.** The fixed main pulse is zero by
`xi=11`, whereas the two correction bumps start after
`xi>=13-(63/20)*lambda>11` for `0<lambda<=1/20`.
Therefore pulse-bump and bump-bump cross terms in the actual
S-moment vanish EXACTLY. With the source normalizations,

`E(A,eta) = P_pre(eta)-D_post(eta)
             + J1*c1(A,eta)^2 + J2*c2(A,eta)^2`,

where `J_i=lambda*int exp(-2lambda y)*beta_i(y)^2 dy >0`,
`P_pre=lambda*S(Xp)/(Xp*eb^2*f^2)` and
`D_post=lambda/(2*Xp*eb^2*f^2)*int_(Xend)^infty E^2 dX`.
The source constructs post-pulse E independently of Amp.

The M and J moment constraints are linear in U; with the
normalized (A.1) matrix, `c_i=a_i(eta)+Amp*b_i` exactly.
The `b_i` depend on the fixed pulse and matrix but not eta.
Thus the FULL amplitude equation is a quadratic polynomial
in Amp, with positive leading coefficient
`K_b + J1*b1^2+J2*b2^2`; in particular
`partial_A^2 E=2*(J1*b1^2+J2*b2^2)>=0`.
If the constant polynomial coefficient is negative, there is
exactly one positive root, expressed by the quadratic formula.

**Explicit quantitative bump control.** For a permissible
normalized smooth plateau bump supported in [-0.15,0.15],
`int beta^2<=5`. Let `D0` bound the two transported
pre-pulse normalized M/J discrepancies and `D1` bound the
main-pulse weighted moment discrepancies. Then
`D1<=(55/2)*exp[-(2/5)*(2/lambda-3)]` and
`J1+J2<=10lambda*exp[-26+6.3lambda]`.
The new theorem gives independent all-lambda bounds on
the value and A derivative of the bump-energy remainder.

If the ACTUAL source pre-pulse normalized moment budget is
independently verified to be <=1, the bounds imply for
`0<lambda<=1/20` and `|Amp|<=1.011`:
`0 <= E-(P_pre-D_post)<2e-18` and
`|partial_A E|<4e-18`.
This condition has NOT been verified for any frozen exterior schedule.
In particular the source's true exterior bias `P_pre-D_post`
has NOT yet been enclosed at 0.0004. The numerical
Appendix-A amplitude, M0 and Appendix-B fixed point are OPEN.

**Reproducibility:** `Exact_A19_Remainder_and_Quadratic_Amplitude_Insert.tex`
is incorporated into the cumulative manuscript. Finite
scalar checks in `ExactA19RemainderScalar.lean` are submitted
to pinned GitHub CI (no kernel PASS claimed before completion).
`remainder_quadratic_exact.py` replays the exact symbolic
polynomial, disjoint-support gap, finite-series exponential
bounds and conditional error certificate.
`amplitude_remainder_certificate.py --demo` runs outward
interval arithmetic on explicitly ASSUMED example bounds;
it is NOT a source numerical certificate.

The downloadable 70-page reading PDF preserves the original
16-page source preprint unchanged and appends a revised 54-page
mathematical amendment. The 35-entry ZIP contains the editable
LaTeX, full theorem, scalar Lean source, exact scripts,
interval demo and hash manifest.

**Next source gate:** independently freeze the actual
pre-pulse moments `M(Xp),J(Xp)`, the source parameters and the
amplitude-independent normalized balance `P_pre-D_post`.
Only then is it legitimate to turn the quadratic formula into
a verified TRUE source moment-matched amplitude. The originating
OpenAI global Navier--Stokes construction has smooth forcing;
the proposed unforced theorem remains unproved.


## ERRATUM and exact four-moment source transport — 20 October 2026

**Material correction to previous A.19 numeric claim.** The originating
Appendix A FIXES its two axial moment-correction bumps to be rescaled
copies of the derivative of its specific smooth step (A.5). An earlier
manuscript revision replaced that by an unrelated smooth plateau bump
and asserted `int beta^2<=5`. This bound is FALSE for the fixed
source correction. The source-specific revised analytic proof gives
`27/5 < int beta_source^2 <= 640/3`; exploratory quadrature yields
approximately 18.30243186625. The exact quadratic remainder formula
survives support separation, but the **correct conditional** estimates
for `0<lambda<=1/20, |A|<=1.011` with true pre-pulse moments <=1
are instead `0<=E-(P_pre-D_post)<5e-17` and
`|d_A E|<1e-16`. Previous 2e-18 and 4e-18 claims MUST NOT
be used for the actual Appendix-A bump.

**New exact source anchor at X_R, from (A.7), (4.15):**
`M_R=4 eta X_R`;
`J_R=(5/2) eta X_R sqrt(2X_R) Pstar f(eta)`;
`S_R=X_R[16eta^2-(5/12)Pstar^2 f(eta)^2]`.
These values derive by elementary exact power-law integration,
not surrogate initial conditions.

**Four scale-normalized transport equations:** Put
`y=log(X/X_R)`, `a=U/E`,
`ell=partial_y log(sqrt(X)E)`,
`m=M/(X E)`, `j=J/(X H E)`,
`s=S/(X E^2)`, and
`d=(2 X E^2)^(-1) integral_X^infty E^2 dx`.
Then EXACTLY
`m'=a-(ell+1/2)m`, `j'=a-(2ell+1/2)j`,
`s'=a^2-1/2-2ell*s`, `d'=-1/2-2ell*d`.
At the source's pure power-law terminal stage
`d_T=1/(4h)` (note this differs from the pressure-mass
tail integral, which has denominator `1+2h`).
The exact amplitude-independent remainder is
`P_pre-D_post=lambda[s(Xp)-exp(-26)d(Xend)]`.

**Exact endpoint numerical gate:**
`max(|m(Xp)|,|j(Xp)|)<=1`, plus
`lambda sup_eta |s(Xp)-exp(-26)*d(Xend)| <=0.0004-5e-17`.
These are the ONLY data still needed for the corrected earlier
conditional amplitude certificate, but they have NOT been
checked for any frozen source-admissible Appendix-A schedule.

**Independent local checks:** Exact SymPy integrals at X_R;
all four normalized transport differential identities; exact
terminal-tail boundary and pulse-end e^-26; exact rational
source-bump norm bounds and corrected 5e-17/1e-16 error thresholds.
The optional high-precision sigma' integral is exploratory,
not a validated quadrature value. The new Lean scalar module
contains only finite arithmetic identities and is not an
end-to-end proof of the integral or Navier--Stokes results.

**Files:** `Source_Moment_Transport_and_Bump_Correction_Insert.tex`,
`source_bump_exact_audit.py`,
`source_moment_transport_exact.py`,
`SourceMomentBumpScalar.lean`. Previous source remainder
insert and interval demo have been corrected to use B2<=640/3.
The downloadable reading PDF is 72 pages (16-page original
unchanged plus corrected 56-page cumulative mathematical
amendment); the 32-file ZIP passes integrity checks.

**Open:** exact source-admissible parameter schedule; stagewise
interval enclosures of a and ell; actual numerical M0, A19
amplitude, nonlinear Appendix-B contraction, n=1,2 UNFORCED
corrections and zero physical residual. Theorem 1.1 is open.


## Exact source pulse-entrance moment and energy envelopes (20 Oct 2026)

The new cumulative mathematical source
`Pulse_Entrance_Uniform_Source_Envelope_Insert.tex` proves directly
from Appendix A.2's prescribed FIRST TWO stages and the exact
four-moment transport system:

`sup_eta max(|m(Xp,eta)|,|j(Xp,eta)|) < 9/100`,

for `T_d=e^{M_d}+10>10`, `Pstar>e^{T_d}` and
`0<lambda<=1/20`. This is uniform in the cutoff shape and
does NOT require freezing its later pulse-end corrections. It
supersedes the previous *unverified size-one pre-pulse bound*:
the source's reference pre-pulse stage satisfies a much stronger
0.09 bound.

A constructive conditional choice
`0<lambda<=10^-6/(T_d+T_f+1)` yields

`lambda*sup_eta|s(Xp,eta)|<1/10000`.

If the ACTUAL post-pulse azimuthal corrections retain the
source's claimed slope inequalities (including nonpositive
slopes through interpolation and the plateau, a 4log(1/h)
hold at slope -1, and slope <=-3h/4 thereafter), the exact
exterior-energy representation gives

`d(Xend)<=T_f/2+15log(1/lambda)+3/4+h^7/3`
and `lambda exp(-26)d(Xend)<1/40000`.

Thus the full amplitude-independent A.19 bias is below
`1/8000=0.000125`. Combining with the corrected prescribed
`sigma'` bump result (B2<=640/3, not the invalid plateau
B2<=5) gives the rigorous *conditional* amplitude gates
`|E(A,eta)|<0.0004`, `|d_A E|<0.01`. On these
source-staged hypotheses the genuine A.19 equation has one
root in (1.009,1.011).

The source's later choice of `T_f`, `lambda` and the
azimuthal moment-correction coefficients must still be
shown simultaneously admissible for one explicit parameter
tuple; the theorem is NOT a fully frozen numerical source
certificate. We have not computed a numeric pressure mass M0,
certified the Appendix-B nonlinear fixed point or solved the
distinct unforced startup correction systems.

`pulse_entrance_exact_certificate.py` passes exact rational
and exponential-series checks. `PulseEntranceScalar.lean`
contains only finite scalar gates submitted to GitHub Actions,
not an end-to-end analytic proof or Lean kernel claim.
The new 74-page reader retains the deposited 16-page original
unchanged, followed by a replacement 58-page cumulative
mathematical amendment; the 33-file ZIP has SHA-256 manifest
and verified integrity. Theorem 1.1 remains OPEN.


## Source-native (A.11) two-bump azimuthal moment certification — 20 October 2026

This release advances the post-pulse angular-moment corrections in
OpenAI's *Finite Time Blowup for Navier–Stokes*, Appendix A.2–A.3,
equations (A.10)–(A.11). It uses only the **prescribed** normalized
width-3/10 bumps, scaled translates of the actual smooth-step
derivative sigma', not the invalid alternative plateau bump.

**Exact corrected source system.** In log-radius centered on the first
bump, `E_new=E_base(1+c1*beta(y)+c2*beta(y-2))`. The two exact
conditions are
`u(c1+x*c2)=DeltaI`,
`2v(c1+z*c2)+w(c1^2+z*c2^2)=0`, with
`u=int exp((1-lambda)t)beta(t)dt`,
`v=int exp(-(1+2lambda)t)beta(t)dt`,
`w=int exp(-(1+2lambda)t)beta(t)^2dt`,
`x=exp(2(1-lambda))`, `z=exp(-2(1+2lambda))`,
`DeltaI=1/(1-lambda)-I(X1)/(X1H(X1))`.
An exact scalar quadratic formula follows by eliminating c1.

**Proved all-index estimates for 0<lambda<=1/20:**
- The exact Jacobian inverse in infinity norm is <3/2; the
  quadratic correction norm is <320. This **angular** inverse is
  uniform as lambda→0, unlike the earlier inverse bound
  for a distinct AXIAL correction matrix.
- Source rI=I/(XH) obeys rI'+(1+ell)rI=1. From its exact
  reference value 5/8, the prescribed interpolation and the
  30log(1/lambda) constant-slope interval give
  `|DeltaI|<64lambda^28`.
- Applying source Lemma A.2 yields the unique small pair
  `max(|c1|,|c2|)<=192lambda^28`.
- Exact smooth-step derivative envelopes
  `||sigma'||<=64`, `||sigma''||<=17152`
  imply `||beta||<=640/3` and `||beta'||<200000`.
  The edited E is positive and
  `-3lambda/2<=ell_corrected<=-lambda/2`
  on the correction supports; elsewhere ell=-lambda.
  Thus the earlier qualitative post-pulse nonpositive-slope
  condition is quantitatively verified for these corrections.

**Partial parameter selection:** `Tf=512` certifies the
(A.10) interpolation slope
`-lambda-7/80<=ell<=-lambda`.
The terminal (A.12) cutoff can use `co=1/256` with
`0<=fo'/fo<h/4` for h<=1/100.
For every source `Td>10`, one explicit local-smallness
family is `lambda=10^-6/(Td+513)`,
`h=lambda*exp(-Td)/10^6`.
This is NOT a frozen *globally source-admissible* tuple:
the stress-cone inequalities, outer stopping length,
large Md and Pstar thresholds, Appendix-B fixed point and
unforced startup PDE remain to be checked.

**Reproducibility and formalization:** The mathematical theorem
is in `Source_A11_Azimuthal_Moment_Correction_Insert.tex`,
the independent exact rational/symbolic replay is
`A11_exact_certificate.py`, and the finite scalar Lean gates
are `A11FiniteGates.lean`.
Latest 76-page reading PDF is 16-page unchanged original plus
a replacement 60-page cumulative amendment. The 41-entry
editable source ZIP passed the integrity test. GitHub CI has
been updated, but the full theorem is NOT kernel-certified:
the Lean file concerns rational scalar gates only.
The proposed unforced Theorem 1.1 remains unproved.


## Actual A.11 parameter derivatives and explicit terminal stopping length — 20 October 2026

Further to the source-native two-bump correction theorem in
`Source_A11_Azimuthal_Moment_Correction_Insert.tex`, a new section
`A11_Derivatives_and_Explicit_Terminal_Stop_Insert.tex` establishes
two additional all-index results.

**Parameter-derivative certificate:** For the source's actual
post-pulse interpolation (A.10) and fixed Tf=512,
the normalized angular moment r=I/(XH) has eta-independent
initial value 5/8 and follows r'+(1+ell)r=1.
On the interpolation |ell_eta|<=1/8,
r<=20/17 and 1+ell>=17/20, whence
|r_eta|<=50/289. Its decay over the later
30log(1/lambda)-3 constant-slope units implies
|Delta_eta|<4lambda^28. Differentiating the exact
(A.11) 2x2 linear-quadratic correction system gives

`max |partial_eta c_i| < 12 lambda^28`,
`|partial_eta ell_corrected| < 5,000,000 lambda^28`,

uniformly for eta in [-1,1], 0<lambda<=1/20.
The pressure-neutrality and angular moment identities
hold identically in eta and hence preserve their
fixed eta derivatives where smooth.

**Explicit terminal stopping:** On the source's subsequent
unit transition to ell=-1, hold for 4log(1/h), and unit
transition to ell=-h, for 0<h<=1/100 and h<lambda,
the source Q_s transport obeys

`Q_start >= (4/e)(1-h)log(1/h) > 5`.

For terminal cutoff c_o=1/256, the actual Qp from (A.13)
has the exact representation

`Qp = (1/f_o(0)) int_0^3 exp((1-h)v) f_o'(v) dv`

and source-explicit interval

`c_o h/(1-c_o h) <= Qp <=
  exp(3(1-h))c_o h/(1-c_o h) < h/10`.

Thus the UNIQUE positive constant-slope stopping length is

`L_stop = log(Q_start/Qp)/(1-h)`.

All terms are independent of eta; this discharges the
source's qualitative positivity-of-stopping-length step
under its stated stage conditions. It does NOT certify
the full global cone test or a numerical terminal profile.

**Verification:** `A11_stopping_and_eta_exact.py` passes
exact-rational exponential-series, Jacobian perturbation,
parameter-slope and terminal Q bounds;
`A11ParameterAndStopping.lean` submits finite scalar
gates to CI, not complete analytic/PDE formalization.
No kernel certification is claimed until the run passes.
The 78-page reader retains the original 16-page deposited
preprint and appends a revised 62-page amendment.
The source package includes a separate scope note and
SHA-256 manifest.

**Still open:** jointly admissible actual numerical
(M_d,P_*,lambda,h,X_R, all stress-cone parameters) source tuple,
verified moment-matched pressure mass M0, Appendix-B
nonlinear fixed point, unforced n=1,2 corrections and
complete unforced Navier-Stokes PDE residual. The
originating OpenAI whole-space construction includes forcing.


## Appendix-A stress cone: strict A.11 support criterion (20 October 2026)

The original OpenAI *Finite Time Blowup for Navier--Stokes* source
requires the relaxed stress-cone condition (4.21) on some
inner/joining stages and the FULL condition (4.22) on designated
outer stages. Negative corrected azimuthal slope does NOT by
itself imply cone admissibility. The earlier A.11 theorem supplied
bounds on the correction amplitudes, eta derivatives and terminal
matching length, but did not verify the cone.

New mathematics in `A11_Cone_Certificate_Insert.tex`:

- On both A.11 azimuthal-bump supports, the source has U=M=J=0,
  hence the axial shear b_s=0. Existing source slope bounds give
  2+lambda <= a=2-2ell <= 2+3lambda <= 43/20.
- The direct full-cone sufficient certificate is
  Q_s>=lambda/4, |N_s|/E<=lambda/4, X>=18/lambda.
  It yields p_s1>=9/2>=2a and the exact STRICT normalized
  margin 2(1-a/p_s1)^2-(a-2)w^2>=7/20, w=N_s/(E Q_s).
- Using the previously proved first parameter-derivative and
  corrector bounds, the exact r=I/(XH) ODE implies
  |r-(1-lambda)^(-1)|<3e8 lambda^28,
  |r_eta|<2e7 lambda^28, and
  |I_eta/(XH)|<2.1e7 lambda^28.
  Under h<=lambda/100,
  Q_s >= (lambda-h)/(1-lambda)-3.2e8 lambda^28
      >= lambda/2, UNIFORMLY on the two bumps.
- Accordingly the remaining sufficient SUPPORT tests reduce to
  |N_s|/E <= lambda/2 and X >= 9/lambda.
  The radial condition can be reached by scaling X_R only AFTER
  the other choices; |N_s|/E is not yet source-certified.
- A quantitative perturbation bound for the two A.24 scalar
  margins gives an interval-transfer route on every other stage.
  The source's pulse O(1) and o(1) bounds are not replaced with
  fabricated explicit constants; the actual pulse stress cone
  still requires its uniform remainder certificate.

The exact Python checker `a11_cone_exact.py` includes a
general rational interval cone evaluator and a negative control.
Its demonstrations are SYNTHETIC and are **not** numerical
enclosures of the actual corrected exterior. The new Lean file
`A11ConeMargin.lean` contains only finite real-algebra and
rational-constant lemmas. A successful GitHub Actions run is
required before those lemmas can be called kernel-certified;
the analytic moment ODE comparison and physical equations have
NOT been fully translated into Lean.

The new 80-page research reader preserves the original deposited
16-page manuscript unchanged and appends the revised 64-page
cumulative mathematical amendment. A separate end-to-end Lean
dependency ledger is `LEAN_A11_TO_THEOREM11_DEPENDENCIES.md`.
Even a complete certificate of the FORCED source stress cone
would not prove the proposed UNFORCED local Theorem 1.1.

**Remaining main gaps:** source-verified N_s/E intervals, complete
stagewise strict stress-cone margins and parameter tuple, the
numerical moment-matched exterior pressure datum, Appendix-B
analytic contraction, true unforced n=1 and n=2 corrections,
all-order convergence and exact unforced Navier--Stokes residual.


## A.11 exterior-tail certificate (20 October 2026)

The exact source equations (4.15), (4.16), (A.11), (A.19)
yield a new analytic control of the axial cone component on
both azimuthal correction supports. AFTER solving the true A.19
moment equation S(infinity,eta)=0, with pressure normalized at
infinity and U=0 at all later radii, one has exactly

  S(X)=1/2 integral_X^infty E(x)^2 dx,
  Pi(X)=-1/2 integral_X^infty E(x)^2 dx/x.

Define D_s=S/(X E²), P_s=-Pi/E² and g=d_eta log E.
Then equation (4.16) gives
  N_s/E = E {4eta(h D_s-A P_s)
             -(1-eta²)[2g(D_s-P_s)+D_s,eta-P_s,eta]}.
Under future slopes ell<=0 and |g|<=eps, this implies
  |N_s|/E <= E[4h D_s+2A+2eps(D_s+1/2)].

Using the actual sigma-prime correction's first-eta bounds,
eps<=5120 lambda^28. The source transition/terminal bounds
give P_s<=1/2 and
D_s<=T_f/2+15log(1/lambda)+3+h^7/3.

With T_f=512, T_d>10, Pstar>exp(T_d), choose
  lambda<=min(10^-6/(T_d+513),
              1/[10(1+log Pstar)],1/20),
  h<=lambda/100.
The fixed source-stage inequalities give
  E_support<=Pstar exp(4-13/(2lambda))<lambda/4,
while the remaining bracket is less than two. Consequently
  sup_{two A.11 supports,eta in [-1,1]} |N_s|/E<lambda/2.

Combined with the earlier analytical Q_s>=lambda/2,
corrected slope and X>=9/lambda, the source's strict stress
cone inequality is satisfied on the two A.11 supports,
CONDITIONALLY on exact global S(infinity)=0, pressure gauge,
and the source's post-pulse slope hypotheses.

New sources: A11_Actual_Ns_Exterior_Tail_Certificate_Insert.tex,
A11NsExteriorTail.lean, a11_ns_tail_exact.py.
The exact rational checker has passing positive/negative controls;
it does NOT create source-derived interval inputs. Scalar Lean
statements are submitted, NOT certified by a local Lean kernel.
The mathematical note has a complete conventional proof of this
conditional support lemma, NOT of the proposed unforced PDE theorem.

The 82-page cumulative PDF includes the unchanged 16-page
original and a revised 66-page mathematical amendment.
The full source packet is accompanied by a fresh hash manifest.
Remaining: jointly frozen Appendix A realization and all other
stagewise cone checks, the pulse o(1) margins, Appendix B nonlinear
profile, true n=1,2 unforced corrections and the physical zero
forcing residual. Theorem 1.1 is still OPEN.


## Source A.5 pulse: explicit curvature and cone acceptance — 20 October 2026

The new scholarly insert `A5_Pulse_Quantified_Cone_Insert.tex`
addresses the main axial pulse's formerly unspecified O(lambda^2)
remainder (source equation A.28). From the **actual source sigmoid**
(A.5), its derivatives and cutoff, one proves
`||sigma'||<=64`, `||sigma''||<=17152`,
`||R0'||<=705`, and `||R0''||<=192000`.
The causal exponential convolution therefore has a quantitative
error bounded by `192000 |Amp| lambda^2 / (1/2-lambda)^3`
plus the decaying entry moment and separately bounded **A.9 axial**
end bumps. No A.11 azimuthal bump estimate is substituted.

The source's two Appendix A.24 quadratic leading expressions have
exact maxima `58081/80000 = 0.7260125` and
`58081/35000 = 1.659457142857...`. Hence a verified upper
error <=0.01 in both expressions preserves the source's
0.74 and 1.68 bounds respectively, with the second remaining
strictly under the cone threshold 2.

A separate conditional scalar pulse theorem gives a stronger
pointwise acceptance test. Under the **jointly unverified**
requirements `1.009<Amp<1.011`,
`lambda<=1/(2*10^9)`, `h<=lambda/10^4`,
`|c_i^axial|<=lambda/400000`, one has the exact source
shear relation
`b_s=-(1+2lambda)R_b+2lambda partial_xi R_b`
and `|b_s+A R0|<10^-6`.
If an independently generated source interval additionally
certifies `|w-(2A R0-C_d A R0')|<=10^-6`
with `w=N_s/(E Q_s)`, plus Q_s positivity and sufficiently
large XQ_s/L, the full axial pulse has both strict source
cone margins. This is a conditional implication: the
relevant w interval still needs to be calculated from source
(A.29)--(A.30), and the A.9 axial coefficients must be
certified separately.

`A5PulseFiniteGates.lean` contains finite scalar candidates.
`a5_pulse_cone_exact.py` checks rational coefficient comparisons;
`a5_pulse_source_gate.py --demo` includes passing and failing
SYNTHETIC controls, not actual source-data certification.
These new files are wired into pinned CI; no kernel pass is
claimed before its completed successful workflow run.

The local **84-page** reading PDF retains the original 16-page
preprint unchanged and appends a newly compiled 68-page cumulative
mathematical amendment. The associated ZIP has a SHA-256 manifest
and the full  start-to-finish Lean dependency ledger. The full
source-generated exterior stress cone, parameter tuple, pulse
w bound, terminal matching, Appendix B contraction, unforced
startup profiles and Theorem 1.1 remain **OPEN**. The originating
OpenAI whole-space construction has compact smooth forcing.


## Exact pulse ratio A.29--A.30 and Lean dependency gate (20 October 2026)

The source-native identity from (4.16) is now implemented:
`w-w0=[q0*(lambda/beta)*R+(D+c_eta)*em-D*eta*m_eta+eN-w0*eQ]/(q0+eQ)`.
It includes the exact pressure source term, axial and angular cumulative
moment derivatives and the intrinsic lambda/beta shift; there is no
assumed numerical Cpre coefficient.

A sufficient **CONDITIONAL** pulse ratio gate is
`0<lambda<=1e-14`, `0<h<=lambda/10000`,
`|R|<=12,|w0|<=1500`, with relative source residual bounds
`|eQ|/q0<=1e-10, |em|/q0<=1e-7,
 |eta*m_eta|/q0<=2e-7, |eN|/q0<=1e-7`.
Exact arithmetic gives `|w-w0|<4.51e-7<1e-6`
IF all four input certificates hold. They have **NOT**
been checked on any frozen actual exterior.

The old shear-only axial bound `|ci|<=lambda/400000`
does not suffice: its permitted averaged velocity error after
division by q0 is O(0.00237), much larger than 1e-6.
The actual affine two-moment formula and the previously derived
pre-pulse/amplitude hypotheses imply the stronger
`|ci|<lambda*1e-40, |em|/q0<3e-8` at
`lambda<=1e-14`, but this is still conditional on the
true source moment/amplitude data.

New materials:
- `A29_A30_Exact_Residual_and_Certification_Insert.tex`
- `A29A30PulseScalar.lean` (finite scalar proof candidate, NOT PDE Lean)
- `a29a30_source_exact.py` (source algebra and exact ratio budget)
- `a29a30_source_interval_gate.py` (requires independently sourced
  outward-enclosed original moment and pressure fields; no source
  data supplied)
- `LEAN_START_TO_FINISH_DEPENDENCY_LEDGER.md` (all open gates).

The original 16-page preprint is unchanged. A cumulative 70-page
mathematical research amendment accompanies it (86-page reader).
A full source-certified w ratio, all-stage stress cone, terminal
matching, Appendix B contraction and the proposed UNFORCED
Theorem 1.1 remain OPEN.


## 21 Oct 2026: Exact ten-state interval tubes and closed pulse transfer

The manuscript now separates the normalized source hierarchy into
**eight forward states** (m,i,j,s and their eta jets) and **two
backward pressure states** (p,p_eta). It establishes a conditional,
all-index exact-rational affine interval ODE comparison theorem, with
a strict cell criterion Delta*L<1 and a rigorous Picard-enclosure
refinement. The new test passes exact source-native positive controls
in the reference power-law region and the pure exterior pressure tail,
and rejects unsafe stage lengths/invalid dimensions.

The actual Appendix-A axial pulse (A.9) retains
ell=-lambda, ell_eta=0, g=-2eta/(1+eta^2) exactly. Consequently
i,i_eta,p,p_eta have elementary closed transfer formulas, while
m,j and their jets and s,s_eta have exact integrating-factor
convolutions on the fixed shape interval xi=lambda*y in [0,13].
The source's A.9 axial bumps are not the later A.11 azimuthal
moment corrections.

GitHub sources: Ten_State_Affine_Interval_Tubes_Insert.tex,
Pulse_Exact_Integrating_Factors_Insert.tex,
ten_state_interval_tubes.py, pulse_transfer_exact.py,
TenStateAffineTubes.lean, PulseTransferScalar.lean,
LEAN_TEN_STATE_TO_UNFORCED_THEOREM_LEDGER.md.
The accompanying complete local research packet also contains
the full 8+2 rational tube checker and source-native controls.
The new cumulative reader has 91 pages (original 16 unchanged;
75-page mathematical amendment).

**Critical scope:** The exact checker accepts bounds supplied by
a source verifier; it does not certify the actual Appendix-A profile
or source inputs. Naive Delta*L stepping over 13/lambda would be
prohibitively expensive at tiny lambda; the exact pulse transfers
give a better route but the A.28 convolution and the full
source-specific interval covering remain open. No source ratio
10^-6, complete stress cone, Appendix-B contraction, unforced
startup systems, physical zero-force PDE residual or full Lean
Theorem 1.1 proof has been established. Do not mark the Lean
candidate declarations as kernel certified without completed CI.


## 21 October 2026: centerline precision and proof provenance audit

The source A.29--A.30 residual ratio now has an independently replayed
denominator-cleared polynomial identity. At eta=0:
`q0=(lambda-h)/(1-lambda)`; when 0<h<=lambda/10000,
0<lambda<=1e-14, the requested |eQ/q0|<=1e-10 and
|eN/q0|<=1e-7 budgets require absolute enclosures of
approximately 1e-24 and 1e-21 at lambda=1e-14.
For smaller lambda, the requirement tightens further.
A plain 1e-16 cancellation-error estimate cannot suffice.

New files:
- `Pulse_Precision_and_Proof_Provenance_Insert.tex` — scholarly
  statement and proof of the precision bound, exact identity, and
  remaining source certification conditions.
- `pulse_precision_and_identity_exact.py` — passed exact SymPy
  and Fraction rational identities, plus a negative precision control.
- `PulseResidualPrecision.lean` — a **candidate** Lean proof of the
  cleared polynomial identity and finite rational gates. The
  analytic-source, enclosure, and unforced PDE theorems are NOT
  formalized; kernel status requires a successful completed CI run.
- `pulse_provenance_replay_gate.py` — binds source, derivation, and
  interval-proof file paths to their true byte digests; its selftest
  rejects empty covers, forged hashes, changed bytes and path traversal.
  A matching hash still does NOT prove mathematical interval enclosure
  validity.
- `PULSE_SOURCE_EVIDENCE_REQUIRED_V2.json` — empty input template;
  deliberately contains NO fabricated source interval cells.

The full source-derived covering of
`[0,13] x [-1,1]`, all A.11 and exterior stress cones,
Appendix-B nonlinear fixed point, unforced n=1/n=2 correction
solutions, and physical zero-force PDE residual are OPEN.
The starting OpenAI manuscript/theorem and its Lean repository
concern forced Navier--Stokes; they do not prove this new
unforced terminal-core theorem.

The local checkpoint includes a 95-page cumulative reading PDF
(original deposited 16 pages unchanged + corrected 79-page amendment)
and a 90-entry research/proof audit ZIP. File integrity and paper
rendering pass, but the raw source PDF was not byte-downloadable into
this execution environment; no fresh source-PDF hash was asserted.


## Actual source-to-interval proof layer — 21 October 2026

The A.5 fixed-pulse interval source issue now has a concrete partial
certificate, not merely input-syntax validation. The new
`Fixed_Pulse_Source_Interval_Certification_Insert.tex` proves an
analytic enclosure theorem for the actual source
`sigma(t)=exp(-1/t^2)/(exp(-1/t^2)+exp(-1/(1-t)^2))`,
`phi_b(xi)=int_0^xi sigma(50v)dv`,
`R0(xi)=phi_b(xi)(1-sigma(xi-10))`, and its first xi and eta
derivatives. The implementation
`source_pulse_exact_boxes.py` uses only Python Fraction:
positive Taylor polynomial and geometric remainder for exp,
monotone sigma endpoints, 16-panel initial phi integration,
exact phi=xi-1/100 after xi=1/50, and sigma'<=64.

**Replayed exact source coverage:** 20 xi cells x 2 eta cells =
40 closed rectangles cover [0,13]x[-1,1]. Every submitted
R0, R0_xi, R0_eta and R0_xi_eta range has a rigorously
derived interval plus a strict rational guard 2^-120.
The central plateau [1,10] has exact R0=xi-1/100>=99/100
and R0_xi=1. `verify_fixed_pulse_boxes.py` recomputes the
source arithmetic, tests rational cover completeness and rejects
negative controls. This is an **actual fixed-pulse source**
certificate, not a synthetic physical Qs/Ns cell claim.

**Crucial distinction:** the containment guard is NOT a stress
cone margin, and broad cells can be far too wide for the
10^-24-scale centerline normalized residual. NO source-authenticated
full cell intervals exist yet for the transported fields
E,U,M,J,S,Pi,Qs,Ns or their eta derivatives, the true A.9 and
A.11 corrections on one simultaneous frozen parameter tuple, or
the complete physical source stress cone.

`FixedPulseSourceScalar.lean` holds only finite plateau/rational
gates; the exp-Taylor, integral soundness and full 40-cell
certificate remain analytic manuscript proofs with Python exact
rational replay, NOT Lean kernel proofs. A 97-page reading PDF
retains the 16-page original unchanged and appends an updated
81-page cumulative scholarly amendment. The supplied full
reproducibility ZIP includes the generator, 40-cell data,
verifier, proof source, sample negative controls, and SHA-256 manifest.

NEXT: Certify source a, a_eta, ell, ell_eta for actual A.9/A.11
supports, propagate ten-state interval enclosures using exact
moment-cancellation and integrating-factor estimates, verify strict
A.29/A.30 and |Ns|/E<=lambda/2 margins across EVERY closed
physical cell, then close all later cone stages, Appendix-B
contraction, actual unforced startup PDE and end-to-end Lean
kernel proof. Theorem 1.1 remains UNPROVED.


## 21 October 2026: exact A.11 N_s/E slack and Lean dependency checkpoint

The new source-derived Appendix A.11 tail theorem is in
`A11_Ns_Quantitative_Slack_Insert.tex`. Subject to the
simultaneous source budgets `E<=lambda/4`,
`4hD_s<=61/100`, `P_s<=1/2`,
`2A<=1001/1000`, and
`2epsilon(D_s+1/2)<=1/100` on both COMPLETE A.11 supports,
the exact source tail formula gives

  `|N_s|/E <= 1621*lambda/4000 < lambda/2`,

with explicit strict slack `379*lambda/4000`. Combining
the separately assumed `Q_s>=lambda/2`, source slope
bounds, `lambda<=1/20` and `X>=9/lambda` gives
normalized strict cone margin

  `>=32117077/80000000 > 2/5`

(stronger than the previous conditional 7/20 margin).

`A11NsQuantitativeSlack.lean` submits elementary real
inequalities to GitHub Actions and is NOT a complete Lean
proof of the tail integrals, the actual source fields, the
full stress cone or the unforced theorem. Its kernel status
is PENDING until a completed successful run. The exact
`a11_ns_quantitative_slack_exact.py` replay tests rational
bounds and fails deliberately incomplete and bad-budget cells.
Inputs are NOT source-authenticated.

The 98-page cumulative reading PDF retains the original
16-page source unchanged; the updated analytic amendment is
82 pages. The attached 97-file packet includes a full
start-to-finish Lean dependency ledger, all known source
checks and the exact-rational conditional validation gate.
**Open:** the actual A.11 source interval premise,
joint Appendix-A parameter certification, full pulse A.29/A.30,
all exterior stages, Appendix-B contraction, n=1,2 unforced
corrections, physical zero-force residual and complete Lean proof.
The original OpenAI Theorem 1.1 constructs a smooth-FORCED flow;
no unforced Millennium-problem solution is claimed here.


## 21 October 2026: A.11 endpoint-tail source proof gate

A new theorem reduces the whole two-support azimuthal stress
certificate to actual correction coefficient bounds and only
the uncorrected base profile's endpoint amplitude and tail
moments. With `delta=40960 lambda^28`, the multiplicative
future-tail distortion factor is at most `1+8delta`, and
`delta<10^-31` for `0<lambda<=1/20`.

Because the uncorrected slope is exactly `-lambda` between
the two extreme bump endpoints, its normalized tail ODEs are
`Db'=2lambda Db-1/2` and
`Pb'=(1+2lambda)Pb-1/2`, making the endpoint reduction
exact rather than sampled. Under independently certified
terminal, future-slope, leading-amplitude and endpoint
budgets, the earlier `|Ns|/E<=1621 lambda/4000` and
strict cone-margin arithmetic are recovered.

See `A11_Endpoint_Tail_Comparison_Insert.tex`,
`A11EndpointScalar.lean`, `a11_endpoint_exact.py`,
`a11_endpoint_gate.py`, and
`A11_Endpoint_Proof_Obligations.md`.
The arithmetic checker ALWAYS outputs a conditional,
non-source-authenticated status. A genuine frozen Appendix-A
source and outward enclosure of the endpoint values are still
missing. The original OpenAI theorem is FORCED; the proposed
UNFORCED theorem remains unproved, as does any complete Lean
proof. The downloadable 100-page research reader preserves
the original 16-page paper and appends a cumulative 84-page
amendment; the complete accompanying ZIP is supplied by email.


## A.11 corrected angular moment derivative and stronger cone gate — 21 Oct 2026

**Source correction:** On the two A.11 azimuthal correction supports,
the exact source (4.16) has
`Qs=-1+(1-h)*I/(XH)-D*eta*I_eta/(XH)` when U=M=J=0.
The I_eta term is generally nonzero INSIDE the corrections; the
equilibrium expression without it is valid only where I_eta=0.

Assuming the true first-bump-center C¹ entrance errors
`|rb-1/(1-lambda)|,|rb_eta|<=64lambda^28` and genuine
source-prescribed bump corrections
`|ci|<=192lambda^28, |ci_eta|<=12lambda^28`,
the positive angular moment comparison yields on BOTH full
supports
`|rc-rb|<=327680lambda^28` and
`|Ic_eta/(XHc)|<=10400lambda^28`.
Therefore for 0<lambda<=1/20 and h<=lambda/100,
`Qs>49lambda/50`.
This explicitly retains the moment derivative and removes
the earlier independent Qs>lambda/2 interval obligation
**conditional on the real entrance and bump jet bounds**.

With the separately required genuine infinity gauges,
`Ec<=lambda/4`, `Ds<233/100`,
`Ps<=(1+8delta)/2`, baseline future slope <=0 and the
local derivative cancellation <1/1000, the previous source
Ns identity then gives `|Ns|/Ec<63lambda/250<lambda/2`.
If the corrected radial slope and X>=9/lambda are proved,
the companion cone exceeds `55743/50000>9/20`.

Files:
`A11_Qs_Eta_Derivative_Improved_Cone_Insert.tex`,
`A11QsEtaDerivativeImproved.lean`, and
`a11_qs_eta_source_gate.py --selftest`.
The exact script rejects missing I_eta, terminal-gauge, future
slope, positivity and radius inputs (eight negative controls).
Its positive case is MATHEMATICAL-FIXTURE INPUT, not a
source-authenticated interval calculation. The Lean module
proves conditional scalar consequences only, not source
integral/interval-soundness or the unforced Navier--Stokes PDE.

The standalone addendum and verification packet are attached
in the current conversation. The locally concatenated
78-page convenience reader uses an archived 74-page base and
therefore omits some INTERVENING A.11 GitHub manuscript
chapters. The living cumulative LaTeX on this branch now
includes the new A.11 source theorem; its CI manuscript
build is the appropriate full up-to-date manuscript route.

Open: independent complete source boxes for one frozen
Appendix-A schedule, terminal gauges, full exterior cone,
Appendix B, distinct unforced startup coefficients,
physical zero-force residual and a kernel-checked end-to-end
Lean proof. The original OpenAI theorem has smooth forcing.


## 21 October 2026 — source-native entrance angular-moment derivative and A.11 jet closure

A new manuscript insertion `A11_Exact_Entrance_Angular_Jet_Insert.tex`
derives the angular-moment **eta derivative through the ACTUAL A.10
interpolation** from the source's separable pre-interpolation
azimuthal field `E(X,eta)=e(X)/(1+eta²)`. Thus
`(I/(XH))_eta=0` before interpolation. For
`a=1-lambda, J0=log(1+eta²), theta(t)=1-sigma(t/Tf),
 G=exp[(1-theta)(J0-log2)]`, the full exact derivative at
the end of interpolation is

`r_f_eta = -J0_eta*exp(-a*Tf)/G(Tf)*
   [r_p+int_0^Tf theta(t)*exp(a*t)*G(t)dt]`.

For source `0<lambda<=1/20` and pre-interpolation
`1+ell>=17/20`, `r_f` and `|r_f_eta|` are both
at most `40/17`. Propagating through the genuine
`30log(1/lambda)` plateau gives on BOTH complete
width-3/10 A.11 supports:

`|r_b-1/(1-lambda)|<18 lambda^28`,
`|r_b_eta|<12 lambda^28`.

The true nonlinear two-bump moment matrix (NOT a substitute bump)
has a particularly small first inverse column. Differentiating
its exact equations proves `|c_i|<=54lambda^28` and
`|c_i_eta|<6lambda^28` on the small source correction branch.
These are sufficient to discharge the earlier four IMPORTED
entrance/eta-jet upper assumptions in the conditional A.11
Qs, Ns/E, and cone source theorem. The actual terminal S and
pressure gauges, future energy/pressure tail certificates,
whole exterior stress cone, Appendix B contraction, and
unforced n=1,2 startup/PDE remain OPEN.

`a11_entrance_jet_exact.py` replays the exponential upper
bound `exp(1197/400)<20`, symbolic derivative cancellation,
and all scalar inequalities with exact Fraction arithmetic.
`A11EntranceJetScalar.lean` is a scalar-only formalization
candidate; GitHub Actions is triggered on commit, not proof
of a Lean kernel PASS until its jobs complete.

A verified standalone 4-page mathematical note and a 78-page
reading copy (the latest available 74-page baseline plus the
4-page new note) were created on 21 October 2026.
The FULL living integrated cumulative TeX with all
intervening A.11 amendments is on this draft branch.
A 40-file reproducibility ZIP contains the previous working
sources and the new theorem, Python, Lean and dependency ledger.
No full unforced theorem has been proved.


## Appendix A.11 exact entrance derivative and two-support stress bound (21 October 2026)

The mathematical insert `A11_Entrance_Derivative_and_Ns_Certificate_Insert.tex` is now included in the master cumulative paper. This is a sharpening of the source's A.10/A.11 interpolation and the previously recorded A11 endpoint/tail gates.

**Entrance derivative.** The source pre-interpolation profile has the common factor `(1+eta²)^(-1)`, so `r_p=I_p/(Xp Hp)` has `partial_eta r_p=0`. Differentiating the exact A.10 moment solution and using smooth-step symmetry yields
`r_f,eta=-J0'(eta)[2r_p e^(-aTf)/(1+eta²)+ integral_0^Tf e^(-a u)(2/(1+eta²))^sigma(u/Tf) sigma(u/Tf) du]`,
with `a=1-lambda`. It has sign opposite to eta, and the split at Tf/4 gives `sup|r_f,eta|<1.41e-6` for `Tf>=512`, `0<lambda<=1/20`, and `r_p<=1/a`.

**ACTUAL two-bump moments.** The two source `sigma'` bumps centered 3 and 1 logarithmic units before the end of the 30log(1/lambda) plateau satisfy an EXACT two-equation moment system: one linear I-row and one pressure-neutral row with positive quadratic bump energy. The explicit linear part has `|det|>5`, `||inverse||_infty<7`, and the nonlinear pressure coefficient `kappa<150`. A Banach contraction on the small coefficient ball yields
`||c||_infty<=42 lambda^(30(1-lambda))`,
`||c_eta||_infty<=70 lambda^(30(1-lambda))`.
These imply `|q|<1/4`, `|q_eta|<1`, `|q_y|<3lambda/8` and preserve the corrected slope `ell<=-lambda/2`.

**Necessary distinction: entrance r_eta does not itself bound N_s.**
Using the source integrated five-moment identity (4.16) together with the completed source constraints `S(infinity)=0` and `Pi(infinity)=0` gives the exact future energy/pressure representation of `N_s`. Under the stated post-pulse nonpositive slopes, the 4log(1/h) steep hold and final slope <=-3h/4, it gives `|N_s|/E<=4 E_base` simultaneously on both true A11 supports, and then the source pulse decay yields
`|N_s|/E<=40 Pstar lambda^15 exp(-13/(2lambda))`.
Therefore the requested target `sup |N_s|/E<=lambda/2` follows from the single explicit sufficient inequality
`80 Pstar lambda^14 exp(-13/(2lambda))<=1`.

**Status.** This is a rigorous, conditional SOURCE-FAMILY sufficient criterion, not an independent interval certification of one full moment-matched exterior. A diagnostic parameter check in `a11_source_gates.py` is NOT an admissible whole-profile certificate. The source amplitude constraint `S(infinity)=0`, all later corrected exterior slopes, global stress-cone endpoint margins, Appendix-B contraction, unforced n=1,2 startup equations and the unforced physical PDE residual remain separately open. No complete start-to-finish Lean theorem has been claimed. `A11ScalarGates.lean` formalizes only algebraic/rational pieces; GitHub CI must complete before even those can be called kernel-certified.


## A.11 refined supportwise axial-stress theorem — 21 October 2026

A new standalone, source-derived subsection is integrated into the cumulative
LaTeX as `A11_Support_Stress_Improved_20261021_Insert.tex`.
It builds on the previously established A.10 entrance-moment derivative identity
and **does not** assume that this entrance derivative alone controls stress.

With source `Tf=512`, `a=1-lambda`, the two prescribed `sigma'`
bumps centred at `30log(1/lambda)-3` and `30log(1/lambda)-1`,
the exact A.11 angular-moment/pressure-neutral system is
`u(c1+x*c2)=delta`,
`2p(c1+z*c2)+w(c1^2+z*c2^2)=0`.
The proof gives
`|delta|<=50lambda^28`,
`|delta_eta|<=3e-5lambda^28`,
`max|c_i|<=|delta|`,
`max|c_i,eta|<=|delta_eta|`,
and preserves `ell<=-lambda/2` on the full supports.
The **actual** prescribed smooth-step derivative bump is used;
there is no substitution of an inadmissible smooth plateau.

Under the source-final moment/pressure gauges
`S(infinity)=Pi(infinity)=0`, source post-correction nonpositive
slopes, the `4log(1/h)` slope-`-1` hold and tail
`ell<=-3h/4`, equation (4.16) gives an exact future-energy formula
for `Ns`. The future-energy factor is <3 and
`|Ns|/E<2E`. The explicit *additional sufficient* parameter
restrictions
`lambda<=min(1/20,1/(1+log(Pstar)))` and
`h<=min(1/10000,lambda/100,exp(-Td)/100)`
make `E<lambda/25` on both complete supports. Consequently,

`sup_(two A.11 supports, |eta|<=1) |Ns|/E<2lambda/25<lambda/2.`

This is a conditional improvement on the earlier bound
`63lambda/250`. The extra `Pstar`-dependent condition can be
imposed after fixing `Pstar`, but has **not** been reconciled with
every other selected source parameter. The proof still assumes the
final pressure and S gauges and the specified following exterior
stages. It does not certify the full stress cone on the whole
exterior, full Appendix-B contraction, unforced startup/PDE residual,
or unforced Theorem 1.1.

`a11_support_strong_exact.py` runs exact rational/finite exponential
comparison tests and outward-interval diagnostic examples.
`A11SupportStrongScalar.lean` is finite scalar arithmetic ONLY.
These files are hooked into GitHub Actions; wait for successful
CI before calling even the scalar lemmas kernel-checked. Neither
the analytic source integrals nor the full Navier-Stokes theorem
have a Lean formalization in this release.

The local reproducible release packet and 78-page cumulative reader
are also available as conversation attachments; the 78-page file
contains the previous 74-page reader followed by one self-contained
four-page research addition, not a re-upload to Zenodo.


## Appendix A.11 stress-support certificate — 21 October 2026

This update appends `A11_Stress_Support_Certificate_Insert.tex`
to the cumulative paper and adds `A11StressScalar.lean`,
`a11_stress_exact.py`, `a11_quadratic_exact.py`,
`a11_interval_gate.py`, and `A11_Lean_Dependency_Ledger.md`.
The available combined reading copy is **77 pages** (original
16-page deposited paper unchanged, plus a revised 61-page amendment);
the reproducibility ZIP contains **40 files**.

**Analytic conditional theorem, actual source equations.**
On the two A.11 azimuthal correction supports, the exact
cumulative formula (4.16) and terminal S/Pi gauges give

  Ns(y,eta) = integral_y^infty [
    2eta(h exp(v-y)-A) E(v,eta)^2 +
    (1-eta²)(1-exp(v-y)) E(v,eta) E_eta(v,eta)
  ] dv.

The piecewise slope argument, crucially including the long
ell=-1 hold and the eventual ell~=-h tail, yields
`E(y)^(-2) integral_y^infty exp(v-y) E(v)^2 dv
  <= 83/20 + 1/2 + (2/3)h^7 < 47/10`.

For the prescribed bump, validated analytic envelope
`B0<=640/3`, `B1<=2000000/9`.
If the TRUE A.11 relative coefficients satisfy
`gamma<=min(3/1280,9 lambda/8000000)`,
`gamma_eta<=3lambda/10240`,
the unedited source amplitude on the supports is <=lambda/30,
and all source gauges and future slopes hold, then
`|Ns|/E<lambda/2` on both supports.
Additional explicit assumptions on the interpolation-exit Qs,
an unedited plateau and `X>=35/lambda` imply
`Qs>=lambda/4`, `p1>=4a` and
`2(p1-a)^2-(a-2)p2^2 >=21 p1^2/40>0`.
This verifies the **support cone conditionally**, not the
complete pulse/exterior cone certificate.

**Exact nonlinear coefficient elimination.** For source-normalized
positive bump integrals u,v0,w and translation factors x,z,
the true A.11 equations are
`u(c1+x c2)=DeltaI`,
`2v0(c1+z c2)+w(c1²+z c2²)=0`.
Eliminating c1 gives an exact scalar quadratic in c2,
with an explicit derivative formula for interval propagation
of the actual `DeltaI_eta`.

**Decisive outstanding gates:** Independently enclose the
source-specific `DeltaI,DeltaI_eta,u,v0,w,c_i,c_i_eta`,
verify source Ebase and Qs data and S/Pi endpoint gauges
for ONE common choice of Td,Tf,Pstar,lambda,h and all moment
corrections, then certify the pulse region, terminal
transitions, all cone endpoints, Appendix-B nonlinear
contraction and UNFORCED startup/physical residual.
The interval gate deliberately returns NOT_CERTIFIED for
its synthetic default example. Neither the complete Lean
proof nor the proposed unforced Theorem 1.1 exists yet.


## 21 October 2026 — joint scalar feasibility and sharper A.11 cone implication

The new A11 joint-parameter theorem takes any fixed Td>10 and Pstar>exp(Td),
with source-permitted Tf=512, and sets
  Q=1+Td+Tf+log(Pstar), lambda=10^(-20)/Q,
  h=lambda*exp(-Td)/10^6.
It proves that the specific published *scalar smallness budgets*
(lambda<1e-14; lambda<1e-6/(Td+Tf+1);
lambda<1/[10(1+log Pstar)]; h<lambda/1e4;
h<exp(-Td)/100; lambda*Tf<1e-6) coexist.
It additionally proves lambda*log(1/lambda)<61e-20.
This is a **nonempty smallness wedge**, not a source-admissible Appendix A
moment-corrected exterior profile.

Given independently authenticated source support bounds
|Ns|/E<2lambda/25, Qs>=49lambda/50,
-3lambda/2<=ell<=-lambda/2, X>=9/lambda and
0<L<=1, the normalized full cone is strictly
  2(1-a/p1)^2-(a-2)w^2 > 107949/96040 > 1 > 9/20.
The numeric consequence uses rational inequalities only.
It does NOT authenticate any of the source premises.

- PAPER: A11_Joint_Parameter_Wedge_and_Strict_Cone_20261021_Insert.tex
- LEAN: A11JointParameterScalar.lean (finite diagnostic rational gates;
  GitHub kernel outcome must be verified, no end theorem)
- EXACT: a11_joint_parameter_exact.py (48 grid instances and cone rational)
- STATUS: scalar theorem proof in manuscript; source A.11 joint
  certification OPEN; all downstream analytic/PDE Lean steps OPEN.

### Remaining release-critical source checks
Actual Md/Td/Pstar choice; source-permitted Tf=512; true A.9
moment/amplitude; A.11 delta and eta-jet; true sigma-prime u,p,w;
isolated quadratic root and its derivative; S/Pi infinity gauges;
two complete A.11 support covers for Ns/E, Qs and X; full axial pulse
(A.29)-(A.30), all exterior transition/terminal cone cells; Appendix B
analytic nonlinear contraction; unforced n=1,2 coefficient solutions;
higher-order recurrence; Cartesian zero-force residual; and eventual
Lean kernel proof of those complete mathematical statements.

The originating published global theorem uses forcing; this programme
has NOT produced an unforced finite-time blowup theorem.


## 21 October 2026 — A.11 whole-patch stress, including the gap

The cumulative manuscript now inputs
`A11_Full_Patch_Gap_20261021_Insert.tex`.
The proof is based on the authentic source (4.16), not a surrogate
stress. Under the genuine terminal gauges `S(infinity)=Pi(infinity)=0`,
and with the corrected azimuthal profile
`E=Eb(1+sum_i c_i(eta) beta_i(y))`,
the perturbation is an integral over the **remaining bump support**.
It is valid everywhere from the first support's start to the second
support's end, including the non-overlapping gap.

The gap matters: it is not enough to check only the two supports when
releasing a complete exterior cone certificate.

For the prescribed source two bumps, the source-conditional jet estimates
`|c_i|<=54 lambda^28`, `|d_eta c_i|<=6 lambda^28`
give `delta<=11520 lambda^28`,
`epsilon<=1280 lambda^28`, both below 0.0001 for
`lambda<=1/20`. If the true source also satisfies
`h<=lambda/100`, `Eb<=lambda/4`, unedited slope
`ell_b=-lambda` on the hull and `ell_b<=0` afterward,
plus the **actual future energy** bound
`Eb(y)^(-2) int_y^infty exp(v-y)*Eb(v)^2 dv<=47/10`,
the exact full-patch result is

`sup_(y on 2 supports AND gap, |eta|<=1) |Ns|/E
     <=101*lambda/400 < lambda/2`,

with strict slack at least `99*lambda/400`.

The term `Ns_b^tail` is an **auxiliary future-tail functional**,
not necessarily the stress of a globally moment-matched unedited
solution. The A.11 conditions alone do not prove the terminal
`S(infinity)=0` gauge, which must be source-authenticated.

`A11FullPatchGapScalar.lean` and
`a11_full_patch_gap_exact.py` are now CI inputs, but they prove/test
finite scalar inequalities only. The complete future-tail integral,
interval-cover soundness, true moment-correction roots, other cone
intervals, Appendix B construction, unforced startups and zero-force
physical PDE theorem are still OPEN. The separate full dependency ledger is
`A11_FULL_HULL_TO_UNFORCED_LEAN_ROADMAP_20261021.md`.

The original OpenAI whole-space result is for Navier--Stokes **with
forcing**; no unforced blowup theorem follows from this A.11 lemma.


## 21 Oct 2026 — terminal-gauge source audit (NEW)

Source (4.15)--(4.16), A.11, A.19 and A.21--A.23 show that
`S(infinity,eta)=0` and `Pi(infinity,eta)=0` are INDEPENDENT
terminal requirements. A.11 preserves a pressure increment; the
unmodified source axis datum and pressure-neutrality enforce the
absolute pressure terminal condition. Only the COMPLETE true A.19
amplitude root for the same profile enforces `S(infinity)=0`.

On A.11 supports, where U=M=J=0, setting
`sigma=S(infinity)`, `pi=Pi(infinity)` gives the exact identity

`Ns=Ns_tail+[4h eta sigma-(1-eta^2)sigma_eta]/X
           +4(1/2+h)eta pi-(1-eta^2)pi_eta.`

After both terminal conditions are established, the actual
`Ns/E` has a SINGLE future-tail integral kernel
`E(x)^2*[2h eta/X -2(1/2+h)eta/x
 +(1-eta^2)*partial_eta(log E(x))*(1/x-1/X)]/E(X)`.
This strengthens the logical provenance of the future-tail test:
without both terminal roots this integral is only `Ns_tail/E`.

An independent exact SymPy replay and Fraction audit prove the
following **conditional implication**, requiring true future
slope <=0, source E<=lambda/4, D_s<=233/100,
future |partial_eta log E|<=1/1000, h<=lambda/100 and
lambda<=1/20, as well as exact terminal gauges:

`|Ns|/E < 253 lambda/1000 < lambda/2.`

For nonzero terminal defects, the same strict conclusion holds
if their two explicit error ratios sum to less than
`247 lambda/1000`.
The source-scale calculation reveals opposing conditioning:
the S-defect normalized contribution decays as
`exp(-(1/2-lambda)*y)`, while the pressure-defect one
grows as `exp((1/2+lambda)*y)` for increasing y.
An approximate pressure integral cannot silently be treated
as a zero terminal gauge.

Files:
`A11_Terminal_Gauge_and_Tail_20261021_Insert.tex`,
`A11TerminalGaugeScalar.lean`,
`a11_terminal_gauge_exact.py`,
`a11_terminal_fail_closed.py`.
The standalone 4-page mathematical proof note and combined
78-page baseline reader are supplied in the conversation packet.
The 78-page reader is the last locally assembled 74-page baseline
plus this note; the living GitHub cumulative master contains
additional intervening A11 inputs, so it is NOT a fresh verified
complete build of every current GitHub input.

**Status:** Full source matching, actual pressure and S terminal roots,
both corrected-support interval hulls, full exterior cone,
Appendix B, unforced n=1/2 startup, physical force-free residual
and a complete trusted Lean proof remain OPEN. The finite Lean module
has been submitted but is NOT claimed kernel-certified.


## 21 October 2026 — pressure rigidity and exact total A.19 derivative

A new cumulative subsection
`A11_Terminal_Rigidity_and_A19_Residual_20261021_Insert.tex`
extends the source-exact A.11 terminal-gauge analysis.

**Global necessity:** On the pure source exterior with
`E=c_inf X^(-A)`, `A=1/2+h<1`, the future-tail
terms in `N_s` cancel exactly. For terminal defects
`sigma=S(infty,eta)`, `pi=Pi(infty,eta)`,
`N_s/E = X^(A-1)/c_inf *[4h eta sigma -d sigma_eta]
       + X^A/c_inf *[4A eta pi-d pi_eta]`.
A bounded normalized stress on the *whole pure tail* forces
`d pi_eta=4A eta pi`, hence
`pi=C(1-eta²)^(-2A)`; smoothness at the similarity endpoints
forces `C=0`. Thus an approximate pressure gauge is insufficient
for global bounded normalized exterior stress. This is a source
algebra / ODE theorem, NOT an unforced PDE theorem.

**Exact A19 residual gate:** The *total* normalized residual
`F(eta)=lambda*S(infty,eta)/(Xp*eb²*f(eta)²)` satisfies
`(N_s-N_tail)/E = K[(4h eta +4eta d/(1+eta²))*F-d F_eta]`
when the true source pressure gauge is fixed exactly, with
`K=Xp eb² f²/(lambda X E)`.
On [-1,1], `|4eta d/(1+eta²)|<=2`.
Thus existing source-conditional tail bound `<0.253 lambda`
and the newly specified strict gate
`Ksup*[(2+4h)*||F||+||F_eta(total)||]<0.247lambda`
imply the desired support `|N_s|/E<lambda/2`.
The chosen amplitude derivative must be included in F_eta.

**Source support factor:** On the two A.11 bumps, writing
`t` for the post-interpolation uniform-stage coordinate,
`B=1+sum c_i(eta) beta_i(t)>0`, one obtains
`K=2eb*f²/(lambda*B)*exp[-(1/2-lambda)
    *(13/lambda+Tf+t)]`,
with `t>=30log(1/lambda)-63/20`.
This is an explicit route to an interval value of Ksup once
true source enclosures of eb and B positivity are available.

**Normalized energy derivative correction:** If
`Ds=S_tail/(X E²)`, `Ps=-Pi_tail/E²`,
they generally depend on eta. The complete local stress formula
includes `-(1-eta²)*E*(Ds_eta-Ps_eta)`. The earlier
symbolic check treating Ds,Ps as constants was a special-case
identity; the full source-exact future-integral formula remains valid.
The new SymPy replay audits the general derivative terms.

**Release scope:** A separately compiled three-page theorem note,
finite Lean scalar candidate and exact symbolic/fail-closed scripts
are in this checkpoint. The true corrected-profile interval covers,
source A19 root, pressure normalization correspondence, the full
exterior cone, Appendix B, the unforced coefficient hierarchy and
Theorem 1.1 remain OPEN. No complete trusted Lean theorem is
claimed, and the originating OpenAI global result uses forcing.


## 21 October 2026: authentic A11 root and angular-jet certificate

The source Appendix A.10 interpolation with Tf=512, eta-independent
moment ratio before interpolation, and 0<lambda<=1/100 gives the
actual first-bump mismatch bounds
`|DeltaI|<0.63*lambda^28` and
`|partial_eta DeltaI|<0.25*lambda^28`.
The exact A.11 two-bump nonlinear moment system and its uniform
matrix inverse then give **one uniquely determined small branch**
`max|c_i|<2lambda^28` and
`max|partial_eta c_i|<lambda^28`.
The fixed-point contraction bound is <0.01 on the source parameter
range. The corresponding corrected E and its angular derivative
have hull budgets (1280/3)lambda^28 and (640/3)lambda^28,
improving earlier conditional 54/6 coefficient hypotheses.

New sources:
- `A11_Authentic_Root_Jet_20261021_Insert.tex`
- `A11RootJetBounds.lean` (finite scalar/polynomial gates only)
- `a11_rootjet_improved_exact.py` (independent exact replay)
- `A11_ROOT_JET_TO_UNFORCED_LEAN_LEDGER_20261021.md`
- `A11_ONE_DATASET_REQUIRED_20261021.json` (intentionally incomplete).

The GitHub cumulative master TeX now inputs this theorem, and the pinned
Lean/algebra workflows include the new source file and checks.
A submitted Lean source is NOT a completed kernel certificate unless
Actions actually reports success.

The previously proved **conditional** two-support+gap consequence
`|Ns|/E<503lambda/2000<lambda/2` can use these improved authentic
bump-value/jet bounds. Still OPEN and not silently assumed:
source-verified terminal S(infinity)=Pi(infinity)=0 on the SAME profile,
full future-tail interval bounds, Qs and E endpoint constraints,
entire exterior/terminal stress cone, exact Appendix B contraction,
genuine unforced n=1,2 profiles, all-order convergence and physical
zero-force Navier--Stokes residual.

Release reader: a verified 78-page historical PDF consisting of the
earlier 74-page combined preprint/amendment and the new 4-page annex.
It is NOT a typeset snapshot of ALL 21-Oct intervening GitHub inserts:
the latest cumulative source on this branch is authoritative.
The separate ZIP includes the Lean source, exact code, source manifest,
dependency ledger and a nested previous research packet.
The proposed unforced Theorem 1.1 remains unproved.


## Backward angular-moment A.11 full-hull reduction — 21 October 2026

The cumulative manuscript now includes
`A11_Backward_Angular_Endpoint_20261021_Insert.tex`. This
derives a stronger conditional A.11 whole-hull bound directly
from the true right-end angular moment in (A.11), without an
independent grid of `Q_s` or slope values on the two bumps
and intervening gap.

**Source identity (do not omit the angular derivative):**
`Q_s=-1+(1-h)*I/(XH)-(1/2-h)*eta*I_eta/(XH)`.
With `r=I/(XH)`, `g=partial_eta log E`, the full derivative is
`I_eta/(XH)=r_eta+r*g`. The A.11 endpoint target, together
with the subsequent unedited `ell=-lambda` plateau, yields
`r(yR)=1/(1-lambda)` and `r_eta(yR)=0` at the right edge
of the second bump. Both are propagated BACKWARD.

Assuming the prior authentic root jets
`|c_i|<=54 lambda^28, |d_eta c_i|<=6 lambda^28`,
the source sigma-prime envelopes and
`0<lambda<=1/100,0<h<=lambda/100`, one obtains across
the full **23/10** closed hull (including the **17/10 gap**):

`|r-1/(1-lambda)| < 6e8 lambda^28`,
`|r_eta| < 1.3e8 lambda^28`,
`|I_eta/(XH)| < 1.31e8 lambda^28`,
`-3lambda/2<ell<-lambda/2`, and
`Q_s >= (lambda-h)/(1-lambda)-7e8 lambda^28
    >49lambda/50`.

If the SAME corrected source profile has exact infinity
S/pressure gauges and independently certified future-tail
bound `|Ns|/E<=503lambda/2000`, and `X>=9/lambda`,
then the strict cone is at least
`85676973/76832000>11/10>9/20` across the full hull.
The source-correct angular derivative term is retained.

The exact-rational checker
`a11_backward_angular_exact.py` and finite scalar Lean module
`A11BackwardAngularScalar.lean` are included in GitHub Actions.
The **local** checker passed. The new GitHub Lean run remains
queued, not kernel-certified. The manuscript integral/ODE theorem
is NOT formalized end-to-end in Lean.

A three-page standalone PDF and a seven-file source packet were
created locally and attached to the research correspondence.
The `exterior_cell_gate.py` program rejects missing gauges,
uncovered cells and incomplete exterior stages; its demonstration
is synthetically assumed and prints a CONDITIONAL status only.

**Not finished:** authenticate all source root/terminal inputs,
the same-profile A.19 S and pressure gauges, actual future-tail
enclosures and the pulse/release/hold/terminal/far-tail stress
cells for one admissible tuple. Appendix B contraction,
the distinct unforced startup coefficient systems, the
unforced physical Navier--Stokes residual and the proposed
Theorem 1.1 remain OPEN. The OpenAI published whole-space
construction is forced.


## 22 October 2026: Source-local A.11 future-tail theorem

The cumulative manuscript now imports
`A11_Source_Local_Future_Tail_20261022_Insert.tex`. Its
source-local proof retains the parameter-derivative term in
the exact 4.16 future-integral formula and applies to both
actual A.11 correction supports **and the intervening gap**.

If the same corrected source has authentic A.11 root jets
`|c_i|<=2lambda^28`, `|d_eta c_i|<=lambda^28`,
the exact S/Pi infinity gauges, and the original prescribed
negative-slope future stages, the whole-hull estimate is

`|Ns|/E <= E_star/(1-a) * [2(1+a)^2*(A+5h)
                                  + (23/10)*(1+a)*b]`,
`a=(640/3)max|c_i|`, `b=(640/3)max|d_eta c_i|`.

An explicit sequential small choice
`0<lambda<=min(1/100, 1/[100(1+log Pstar)])`,
`0<h<=lambda/100`
makes the actual *unedited* stage amplitude
`E_star<8Pstar exp(-Td/2)lambda^45 exp(-13/(2lambda))
       <lambda/1000`.
The authenticated root jets then give
`a,b<1/1000`, so the exact rational corner
coefficient is `2513764253/2497500000<11/10`,
and `sup_hull |Ns|/E < 11lambda/10000 <lambda/500`.
This removes the need for an independent numerical
future-tail N_s bound **once those same-profile inputs are met**.

Finite exact Fraction checks passed; the candidate scalar
Lean file is `A11SourceLocalTailScalar.lean`.
The proof dependencies are listed in
`A11_Lean_Dependency_Ledger_20261022.md`.
The entire future-integral/ODE statement is NOT yet
formalized end-to-end in Lean, and CI success must be
independently confirmed.

**Unresolved:** genuinely joint A.11 and A.19 roots,
same-profile exact terminal S and pressure gauges, full
pulse/release/hold/terminal cone stages, Appendix B fixed point,
the distinct UNFORCED n=1,2 hierarchy, and the Cartesian
PDE residual. Theorem 1.1 remains open; the originating
OpenAI whole-space theorem has smooth forcing.
