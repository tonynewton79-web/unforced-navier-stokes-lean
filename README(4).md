# Unforced Navier–Stokes — Lean Audit and Reproducibility Package

This repository accompanies the manuscript

> **Unforced Finite-Time Blow-Up for Navier–Stokes: Exact Nonlinear Closure on the Three-Dimensional Periodic Torus**  
> Tony Newton — Newton Astro Labs, London, UK

It contains the manuscript source and PDF, an **abstract Lean 4 formalization of the closure layer**, exact-arithmetic replay scripts, a pinned Lean/Mathlib environment, a frozen upstream Navier–Stokes dependency, and a GitHub Actions workflow for reproducible checks.

## Paper and archival release

The manuscript and associated formal-verification materials are archived on Zenodo:

**Tony Newton, _Unforced Finite-Time Blow-Up for Navier–Stokes: Exact Nonlinear Closure on the Three-Dimensional Periodic Torus_**

Zenodo record: `22903432`  
DOI: `10.5281/zenodo.22903432`

## Current formal status

The present Lean development **does not constitute a machine-checked proof of the full unforced three-dimensional Navier–Stokes theorem**.

What is already kernel-checked in `UnforcedClosure.lean`:

- the exact cumulative-mean bottleneck identity `9/10 - 1/2 = 2/5`;
- the released defect identity `2/5 - 1/10 = 3/10`;
- positivity of the coupling and nonlinear spare exponents for `0 < h < 1/2`;
- the abstract implication from a fixed-point equation plus an exact right inverse to exact zero residual;
- the scalar radius-`2η` ball-invariance inequality;
- finite Neumann support preservation under an abstract support predicate.

The abstract closure file compiled successfully in the pinned Lean/Mathlib environment in GitHub Actions Run `#12` (Run ID `35779131542`).

The successful abstract compile is recorded in `CI_CERTIFICATE.md`.

## What remains outside the abstract Lean certificate

The following items remain part of the PDE-specific integration gate:

- importing and instantiating the relevant PDE-specific hypotheses from the frozen `openai/NavierStokesAndEuler` repository;
- replacing the manuscript's Appendix A hypotheses one-by-one with concrete upstream theorem applications or newly proved bridge lemmas;
- proving the actual core/regular range compatibility needed by the global right inverse;
- proving the pressure reconstruction for the actual imported force and correction;
- instantiating the full contraction estimate in the actual graph-norm spaces;
- proving completeness and the smoothness/regularity bootstrap for the correction;
- connecting the asymptotically subleading correction to the imported singular carrier;
- compiling a final theorem asserting unforced periodic finite-time blow-up.

Accordingly, the correct external description is:

> **The abstract nonlinear closure layer has been kernel-checked in Lean in a pinned reproducible environment. The full PDE-specific unforced Navier–Stokes theorem remains subject to explicit analytic hypotheses and a separate Lean integration gate.**

## Corrected PDE audit conditions

The current manuscript makes the following PDE-side requirements explicit.

### 1. Core-range condition for the global inverse

For the global inverse formula

\[
G = G_c S_c + G_{\rm reg} S_r - G_c K_{\rm full} G_{\rm reg} S_r,
\]

the mismatch term must lie in the core source space on which `G_c` is a right inverse:

\[
K_{\rm full} G_{\rm reg} S_r(Y) \subseteq Y_c.
\]

This is a range/support condition, not merely a small-norm estimate.

### 2. Correct pressure reconstruction

Unless the imported force has first been explicitly replaced by its Leray projection, the periodic pressure equation must include the force divergence:

\[
-\Delta \pi
=
\nabla\!\cdot F_*
+
\partial_i\partial_j
\left(
U_{*,i}v_j+v_iU_{*,j}+v_iv_j
\right).
\]

### 3. Full contraction gate

The decisive smallness condition is

\[
4 M_G C_B \eta < 1,
\]

not merely `η → 0` by itself.

### 4. Functional-analytic closure

The fixed-point space must be complete, and the resulting correction must be upgraded to the claimed smoothness class through an explicit regularity/bootstrap argument.

These conditions are now part of the manuscript-level PDE audit. They are **not** claimed to have been discharged by the abstract Lean file.

## Repository contents

| File | Purpose |
|---|---|
| `paper.pdf` | Corrected manuscript |
| `paper.tex` | Matching LaTeX source |
| `references.bib` | Bibliography |
| `UnforcedClosure.lean` | Abstract Lean 4 closure formalization |
| `PDEIntegration.lean` | Staging bridge to the frozen upstream Navier–Stokes development |
| `lean-toolchain` | Pinned Lean toolchain |
| `lakefile.toml` | Pinned Mathlib and frozen upstream dependencies |
| `verify_unforced_closure.py` | Exact-rational arithmetic and Lean-source hygiene checks |
| `test_unforced_closure.py` | Pytest wrapper |
| `verification_receipt.json` | Machine-readable verification status |
| `pytest_receipt.txt` | Recorded Python test result |
| `FORMAL_STATUS.md` | Precise PASS/HOLD interpretation |
| `CI_CERTIFICATE.md` | Successful abstract Lean CI certificate |
| `REPRODUCIBILITY.md` | Local and CI replay instructions |
| `PDE_INTEGRATION_GATE.md` | Requirements for a full PDE-specific Lean theorem |
| `CITATION.cff` | Citation metadata |
| `SHA256SUMS.txt` | Release-file hashes |

## Pinned environment

Lean:

`leanprover/lean4:v4.34.0-rc2`

Mathlib commit:

`85e3a25e006c35636f0e53b0e9296caca2685bc0`

Frozen upstream Navier–Stokes repository commit:

`f9e8bc5b38b6e212696e8a30e3e91517af887bbd`

Upstream repository:

`https://github.com/openai/NavierStokesAndEuler`

## Quick verification

With `elan`, Lean/Lake, and Python available:

```bash
lake update
lake exe cache get
lake env lean UnforcedClosure.lean
lake build
python verify_unforced_closure.py
python -m pytest -q test_unforced_closure.py
```

For the staged PDE integration layer, the workflow additionally builds the frozen upstream `NavierStokes` library before compiling:

```bash
lake env lean PDEIntegration.lean
```

## Interpreting CI correctly

A successful abstract Lean job means:

> `UnforcedClosure.lean` type-checks in the pinned Lean/Mathlib environment and the declarations in that file are kernel-checked.

It does **not** mean:

> the manuscript's entire PDE construction, all Appendix A analytic hypotheses, or the final unforced finite-time blow-up theorem have been formally verified in Lean.

That stronger release gate is documented in `PDE_INTEGRATION_GATE.md`.

## Claim discipline

Until the PDE integration gate is closed, please preserve the distinction between:

1. **kernel-checked abstract closure logic**, and
2. **the full PDE-specific unforced blow-up theorem**, whose explicit analytic hypotheses and Lean bridge remain to be discharged.

The repository is intended to make that distinction auditable rather than obscure it.
