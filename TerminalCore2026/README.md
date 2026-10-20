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
