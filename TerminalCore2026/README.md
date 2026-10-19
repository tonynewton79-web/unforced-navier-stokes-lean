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
