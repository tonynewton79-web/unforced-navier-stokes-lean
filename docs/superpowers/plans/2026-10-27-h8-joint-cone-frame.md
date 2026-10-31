# H8 Joint Cone and Frame Correction Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans or superpowers:subagent-driven-development to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax.

**Goal:** Correct the variable-angle dual estimate and add exact coupled axial/azimuthal cone data without overstating full PDE closure.

**Architecture:** Keep the finite rational cone, spatial-frame enclosure,
physical manuscript and Lean statements separate. Use a source-freeze ledger
to prevent test functions or conditional PDE hypotheses being promoted to
authenticated inputs.

**Tech Stack:** Python 3 rational `fractions.Fraction`, `unittest`, Lean 4/Mathlib, LaTeX.

**Spec:** `docs/superpowers/specs/2026-10-27-h8-joint-cone-frame-design.md`

## Global Constraints

- Preserve the exact asymmetric seven-ray floor; do not replace it by the stricter absolute budget.
- Keep pressure endcaps, angular dependence, temporal source and independent cutoffs.
- Do not claim a green Lean proof without a fresh compilation receipt.
- Leave G0 and G4--G8 OPEN; G1--G3 remain PAPER_CONDITIONAL.

## Review Focus

1. A constant frame with a varying physical test must incur nonzero test error.
2. Density zero must force all four stress coordinates to vanish.
3. Independent axial/torque cap maxima are not jointly realizable.
4. The pressure trace and temporal marginal are retained in physical flux claims.
5. Current GitHub CI may be queued; the final declaration remains uninhabited.

### Task 1: Rational joint cone

**Files:** `h8_positive_cone.py`, `tests/test_h8_joint_cone.py`.

- [ ] Write tests for all six vertices, mixed facets and explicit lifting.
- [ ] Confirm tests fail due to absent joint-cone interfaces.
- [ ] Add `joint_ac_feasible`, `joint_ac_witness`, `joint_ac_support`.
- [ ] Run tests and the existing cone suite.

### Task 2: Correct variable test enclosure

**Files:** `h8_split_cutoff_gate.py`, `tests/test_h8_split_cutoff_gate.py`.

- [ ] Write test rejecting unspecified angular-test data and one checking nonzero test variation with zero frame error.
- [ ] Confirm the regression fails on the old API.
- [ ] Require a certified reference test tensor and its variation; add the corresponding mass-weighted error.
- [ ] Run the affected and full tests.

### Task 3: Mathematical manuscript and formal statements

**Files:** `manuscript/Unforced_Navier_Stokes.tex`, `UnforcedPatching/JointFluxCone.lean`, `UnforcedPatching/JointFluxConeSmoke.lean`.

- [ ] Insert the exact constructive hexagon theorem and joint dual.
- [ ] Repair the physical-frame proposition with a genuine cellwise weighted integral.
- [ ] Add conservative Lean necessary inequalities and explicit rational checks.
- [ ] Compile with pinned Lean where possible; record any unavailable CI receipt.

### Task 4: Source and theorem boundaries

**Files:** `docs/unforced-integration/H8_SOURCE_FREEZE_CHECKLIST.md`, `docs/unforced-integration/proof_gates.json`, release audit note.

- [ ] Record immutable tuple requirements, full source and unforced correction equation.
- [ ] Preserve OPEN/PAPER_CONDITIONAL proof statuses.
- [ ] Verify machine-readable ledger and bibliography of existing certificates.

### Task 5: Publish and verify

**Files:** revised PDF alongside TeX, feature branch commit and existing draft PR #5.

- [ ] Run full Python suite and exact arithmetic source checks.
- [ ] Compile, render and visually verify every PDF page.
- [ ] Commit and push only verified changes to the requested existing feature branch.
- [ ] Report CI results, remaining mathematical blockers, and direct source links.
