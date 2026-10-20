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
