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
