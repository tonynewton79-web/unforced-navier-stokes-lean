# Unforced Navier–Stokes — Lean Audit and Reproducibility Package

> **Current mathematical status (30 October 2026):** The original unforced finite-time singularity construction is **NOT proved**. The latest journal-style research edition proves a **conditional pressure-driven retention obstruction**, an exact finite seven-ray cone, and a new **logarithmic dyadic summability exclusion**; it does not construct a source-matched nonlinear correction. See [the journal-style edition and precise theorem scope](docs/unforced-integration/H8_JAMS_RESEARCH_EDITION_20261030.md) and [the proof-gate ledger](docs/unforced-integration/proof_gates.json). The earlier archival manuscript title below is historical and **must not be understood as a currently verified proof of unforced blow-up**.

This repository accompanies the manuscript

> **Unforced Finite-Time Blow-Up for Navier–Stokes: Exact Nonlinear Closure on the Three-Dimensional Periodic Torus**  
> Tony Newton — Newton Astro Labs, London, UK

It contains the manuscript source and PDF, an **abstract Lean 4 formalization of the closure layer**, exact-arithmetic replay scripts, a pinned Lean/Mathlib environment, a frozen upstream Navier–Stokes dependency, and a GitHub Actions workflow for reproducible checks.

## Paper and archival release

The manuscript and associated formal-verification materials are archived on Zenodo:

**Tony Newton, _Unforced Finite-Time Blow-Up for Navier–Stokes: Exact Nonlinear Closure on the Three-Dimensional Periodic Torus_**

Zenodo record: `22903432`  
DOI: `10.5281/zenodo.22903432`

### 29 October 2026: full-equation and energy-compatibility audit

The cumulative **editable** manuscript at
\`manuscript/Unforced_Navier_Stokes.tex\` now includes the exact
two-mode equations (Appendix M), terminal-dyad injection necessities
(Appendix Q), and the global energy-compatibility theorem (Appendix R).
The existing Appendices N--P remain on this research branch.

For a compact similarity carrier with
\(\|U\|_2^2\sim M_0\tau^p\) and
\(\|\nabla U\|_2^2\sim R_0M_0\tau^{p-1}\),
an exact unforced energy-law argument shows that, assuming a bounded
dimensionless Laplacian-shape ratio, **global relative \(L^2\) retention**
\(\|u-U\|_2=o(\|U\|_2)\) requires \(R_0\le p/2\).
The confined Appendix O prepared-field prototype violates this bound
by a rigorous disk spectral estimate. Thus the specific globally
\(L^2\)-subleading correction route is excluded for that prototype.
This does **not** exclude non-negligible exterior-energy corrections
or an alternative carrier. It is not a proof of finite-time blow-up.

Twelve independent mathematical regressions now pass locally: six exact 3D PDE/pressure/energy/chart checks, five terminal energy-dyad/spectral checks, and one direct full-residual projection of both amplitude and translation equations.
The new physical CI workflow explicitly executes all three pytest modules, while the full final theorem remains open. They are supportive symbolic/spectral checks, not an independent
Lean kernel theorem or a physical PDE solution. CI status is tracked
separately. The G0--G8 proof gates and the global unforced
Navier--Stokes existential theorem remain **OPEN**.
See \`docs/unforced-integration/proof_gates.json\`.

## Current formal status

The present Lean development **does not constitute a machine-checked proof of the full unforced three-dimensional Navier–Stokes theorem**.

### Case 006 H8 joint-cone and angular-frame audit (27 October 2026)

The cumulative mathematical paper is
`manuscript/Unforced_Navier_Stokes.tex`; it is distinct from the older
conditional archival manuscript `paper.tex`. The current H8 revision
proves a **jointly sharp axial--azimuthal hexagon** for the original
one-sided seven-ray coefficient floors, with a constructive rational
lift. `h8_positive_cone.py` and `tests/test_h8_joint_cone.py` replay
the calculation. The new `UnforcedPatching/JointFluxCone.lean` contains
the corresponding necessary inequalities; a hosted compilation receipt
for its exact GitHub commit is required before calling that declaration
kernel-checked.

An adversarial review also found that the earlier cell-mass-only
physical variable-frame support formula incorrectly treated
`e_r(theta) tensor e_z` as constant over angular cells. The cumulative
manuscript now keeps the frozen-frame support *inside the angular
integral*. The rational Python enclosure separately requires certified
test-tensor variation and frame-variation errors. See
`docs/unforced-integration/H8_SOURCE_FREEZE_CHECKLIST.md`.

The next exact source-side screen is a **zero-density collar / flat-edge
curl obstruction**. All four admissible H8 stress coefficients vanish
where `rho=0`; consequently a genuine source
`f=div(E H E^T)+grad(p)` must have zero curl there. At any smooth flat
boundary point of `rho`, every jet of `curl(f)` must vanish. The proof
is in the cumulative manuscript, with exact finite Python regression
and a new (hosted compilation pending) Lean zero-density lemma.

The original complete H8 cutoff, frame, shaper, pressure and source
tuple remains unauthenticated. Moreover, stress-divergence matching
is not equivalent to solving the nonlinear unforced PDE. The final
existential theorem, source-matched inverse and smooth nonlinear
correction remain **OPEN**. See the machine-readable
`docs/unforced-integration/proof_gates.json` ledger.

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
