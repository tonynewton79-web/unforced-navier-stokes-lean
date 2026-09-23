# Formal Verification Status

## Current release state

| Gate | Status | Meaning |
|---|---|---|
| Exact rational arithmetic replay | **PASS** | The finite scalar identities and admissible exponent-margin checks in `verify_unforced_closure.py` pass using exact rational arithmetic. |
| Contraction arithmetic replay | **PASS** | The explicit scalar cases satisfying `4 C η < 1` obey the stated ball-invariance inequality. |
| Lean source hygiene | **PASS** | The packaged Lean file contains none of the forbidden release tokens checked by the replay script: `sorry`, `admit`, new `axiom`, `unsafe`, or `native_decide`. |
| Abstract Lean kernel compile | **PASS** | `UnforcedClosure.lean` compiled successfully in the pinned Lean/Mathlib environment in GitHub Actions Run #12. |
| Frozen upstream dependency resolution | **PASS** | The pinned `openai/NavierStokesAndEuler` dependency resolves at the frozen commit used by the manuscript. |
| Frozen upstream `NavierStokes` library build | **IN PROGRESS / NOT YET CERTIFIED** | A dedicated CI run is building the upstream library before compiling the PDE integration layer. This status must not be interpreted as a mathematical failure. |
| PDE-specific upstream integration | **HOLD** | The manuscript's Appendix A hypotheses have not yet been replaced one-by-one by concrete imported Lean theorems and newly proved bridge lemmas. |
| Final unforced PDE theorem in Lean | **HOLD** | No compiled Lean theorem currently discharges the full unforced periodic finite-time blow-up statement. |

## Certified abstract Lean result

The following statement is accurate:

> The abstract unforced-closure Lean file compiles in the pinned Lean/Mathlib environment, and the formal declarations contained in that file are kernel-checked.

The successful CI certificate covers the abstract closure layer, including:

- the exact cumulative-mean identity `9/10 - 1/2 = 2/5`;
- the released defect identity `2/5 - 1/10 = 3/10`;
- positivity of the scalar coupling and nonlinear spare margins;
- the implication from an exact right inverse plus a fixed-point equation to exact zero residual;
- the scalar radius-`2η` ball-invariance inequality;
- finite Neumann support preservation.

The successful compile reports no `sorryAx` dependency for `fixedPoint_implies_zero_residual`.

## What is not yet certified

It is still **not** accurate to say:

> The full unforced three-dimensional Navier–Stokes finite-time blow-up theorem has been formally verified in Lean.

That stronger statement requires closure of the PDE-specific integration gate.

In particular, the current manuscript revision makes explicit several PDE-side requirements that must be connected to concrete operators and spaces in Lean:

1. the core/regular coupling term must land in the core source space on which the core right inverse is valid, schematically
   `K_full G_reg S_r(Y) ⊆ Y_c`;
2. the periodic pressure reconstruction must include the divergence of the imported force unless the force has first been explicitly replaced by its Leray projection;
3. the actual contraction gate is the full quantity `4 M_G C_B η < 1`, not merely `η → 0`;
4. the functional-analytic fixed-point space must be complete, and the smoothness/regularity bootstrap for the correction must be proved.

These are now part of the release-level PDE audit and are not claimed to be discharged by the abstract Lean file.

## Manuscript relationship

The paper's release theorem is conditional on its explicitly enumerated analytic hypotheses. The present Lean file formalizes a finite abstract closure layer downstream of those hypotheses; it does not independently establish the PDE-specific hypotheses themselves.

## Required wording for external summaries

Until the PDE integration gate is closed, the preferred description is:

> The abstract nonlinear closure layer has been kernel-checked in Lean in a pinned reproducible environment. The full PDE-specific unforced Navier–Stokes theorem remains subject to explicit analytic hypotheses and a separate Lean integration gate.

## Final release gate

The repository may describe the full unforced theorem as Lean-verified only after all of the following are complete:

- the frozen upstream repository builds in the pinned environment;
- the PDE integration layer imports both the upstream development and `UnforcedClosure`;
- every Appendix A hypothesis is mapped to a concrete upstream or newly proved Lean declaration;
- the corrected global right-inverse range condition is typed and proved;
- the corrected pressure reconstruction is typed and proved;
- the full contraction estimate is instantiated in the actual graph-norm spaces;
- the correction is constructed by the fixed-point theorem in the PDE spaces;
- smoothness, periodicity, solenoidality, and pressure reconstruction are connected to the constructed solution;
- the asymptotic subleading estimate is connected to the imported carrier coefficient;
- the final theorem compiles with no `sorry`, `admit`, project-local axioms, or equivalent escape hatches;
- `#print axioms` and a clean-checkout CI replay are recorded.
