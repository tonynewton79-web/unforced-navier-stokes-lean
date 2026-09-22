# Unforced Navier–Stokes — Lean Audit and Reproducibility Package

This repository accompanies the manuscript

> **Unforced Finite-Time Blow-Up for Navier–Stokes: Exact Nonlinear Closure on the Three-Dimensional Periodic Torus**  
> Tony Newton — Newton Astro Labs, London, UK

It contains the manuscript source and PDF, an **abstract Lean 4 formalization of the closure layer**, exact-arithmetic replay scripts, and a GitHub Actions workflow intended to compile the Lean file and rerun the Python checks on every push and pull request.

## Paper and archival release

The manuscript and associated formal-verification materials are archived on Zenodo:

**Tony Newton, _Unforced Finite-Time Blow-Up for Navier–Stokes:
Exact Nonlinear Closure on the Three-Dimensional Periodic Torus_**

Zenodo record: 22903432  
DOI: 10.5281/zenodo.22903432

## Formal status

The present Lean file **does not constitute a machine-checked proof of the full unforced three-dimensional Navier–Stokes theorem**.

What is formalized in `UnforcedClosure.lean`:

- the exact cumulative-mean bottleneck identity `9/10 - 1/2 = 2/5`;
- the released defect identity `2/5 - 1/10 = 3/10`;
- positivity of the coupling and nonlinear spare exponents for `0 < h < 1/2`;
- the abstract implication from a fixed-point equation plus an exact right inverse to zero residual;
- the scalar radius-`2η` ball-invariance inequality;
- finite Neumann support preservation under an abstract support predicate.

What remains outside this formalization:

- importing and instantiating the PDE-specific hypotheses from the upstream `openai/NavierStokesAndEuler` repository;
- replacing the manuscript's Appendix A hypotheses by concrete Lean theorem applications;
- compiling a final PDE theorem asserting unforced periodic finite-time blow-up;
- independent external verification and refereeing of the complete analytic argument.

Accordingly, a green CI run establishes that the **abstract closure file compiles and its local formal claims are kernel-checked**. It must not be described as verification of the complete PDE theorem.

## Repository contents

| File | Purpose |
|---|---|
| `paper.pdf` | Revised manuscript with Lean/formal-status audit language |
| `paper.tex` | LaTeX source for the manuscript |
| `references.bib` | Bibliography used by the manuscript |
| `UnforcedClosure.lean` | Abstract Lean 4 closure formalization |
| `lean-toolchain` | Pinned Lean toolchain |
| `lakefile.toml` | Pinned Mathlib dependency and Lake package definition |
| `verify_unforced_closure.py` | Exact-rational arithmetic and Lean-source hygiene checks |
| `test_unforced_closure.py` | Pytest wrapper for the replay checks |
| `verification_receipt.json` | Status receipt produced for the packaged audit |
| `pytest_receipt.txt` | Recorded Python test result from the packaged audit |
| `FORMAL_STATUS.md` | Precise interpretation of PASS/HOLD states |
| `REPRODUCIBILITY.md` | Local and CI replay instructions |
| `PDE_INTEGRATION_GATE.md` | Requirements for upgrading to a full PDE-specific Lean theorem |
| `CITATION.cff` | GitHub citation metadata |
| `SHA256SUMS.txt` | Cryptographic hashes for the release files |

## Pinned Lean environment

- Lean: `leanprover/lean4:v4.34.0-rc2`
- Mathlib: `85e3a25e006c35636f0e53b0e9296caca2685bc0`

The manuscript audits the upstream OpenAI Lean repository at commit:

`f9e8bc5b38b6e212696e8a30e3e91517af887bbd`

Upstream repository: `https://github.com/openai/NavierStokesAndEuler`

## Quick verification

With `elan`, Lean/Lake, and Python available:

```bash
lake update
lake env lean UnforcedClosure.lean
lake build
python verify_unforced_closure.py
python -m pytest -q test_unforced_closure.py
```

The GitHub Actions workflow in `.github/workflows/verify.yml` performs the same checks automatically.

## Interpreting CI

A successful Lean job means:

> `UnforcedClosure.lean` type-checks in the pinned Lean/Mathlib environment with the declarations contained in that file.

It does **not** mean:

> the manuscript's entire PDE construction, all Appendix A analytic hypotheses, or the final unforced finite-time blow-up theorem have been imported and discharged in Lean.

That stronger release gate is documented in `PDE_INTEGRATION_GATE.md`.

## Paper claim discipline

Until the PDE integration gate is closed, the appropriate description is:

> *The abstract closure layer is supplied as Lean source together with exact-arithmetic replay tests. Full PDE-specific machine verification remains a separate integration gate.*

Please preserve that distinction in citations, summaries, and derivative releases.
