# Formal Verification Status

## Current release state

| Gate | Status | Meaning |
|---|---|---|
| Exact rational arithmetic replay | **PASS** | The finite scalar identities and sampled admissible-margin checks in `verify_unforced_closure.py` pass using Python exact rational arithmetic. |
| Contraction arithmetic replay | **PASS** | The explicit test cases satisfying `4 C η < 1` obey the stated ball-invariance inequality. |
| Lean source hygiene | **PASS** | The packaged Lean file contains none of the forbidden release tokens checked by the replay script: `sorry`, `admit`, new `axiom`, `unsafe`, or `native_decide`. |
| Lean kernel compile in the original packaging environment | **NOT RUN** | Lean was unavailable in that local build environment. GitHub CI is supplied to perform this step after repository upload. |
| PDE-specific upstream integration | **HOLD** | The manuscript's Appendix A hypotheses have not yet been replaced by concrete imports and theorem applications from the frozen upstream repository. |
| Final unforced PDE theorem in Lean | **HOLD** | No compiled Lean theorem currently discharges the full unforced periodic finite-time blow-up statement. |

## What may be claimed after green CI

If `.github/workflows/verify.yml` completes successfully, it is accurate to say:

> The abstract unforced-closure Lean file compiles in the pinned Lean/Mathlib environment, and its contained formal declarations are kernel-checked.

It is still **not** accurate to say:

> The full unforced three-dimensional Navier–Stokes finite-time blow-up theorem has been formally verified in Lean.

That wording becomes appropriate only after the PDE integration gate in `PDE_INTEGRATION_GATE.md` is closed and the final theorem compiles without unproved assumptions or forbidden placeholders.

## Manuscript relationship

The paper's release theorem is conditional on its explicitly enumerated analytic hypotheses. This repository's present Lean file formalizes a finite abstract closure layer downstream of those hypotheses; it does not independently establish the hypotheses themselves.
