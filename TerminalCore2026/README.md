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
