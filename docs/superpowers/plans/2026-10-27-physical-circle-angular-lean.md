# Physical-circle angular chain rule implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make physical Cartesian stress's angular pullback supply the derivative and endpoint hypotheses of the already-proved angular FTC.

**Architecture:** Differentiate the genuine circle with `HasDerivAt.prodMk`, compose a Frechet derivative for stress, evaluate its angular directional coefficients, then invoke `angularDerivativeIntegral_zero`.

**Tech Stack:** Lean 4.34.0-rc2, pinned Mathlib, Lake.

**Spec:** `docs/superpowers/specs/2026-10-27-physical-circle-angular-design.md`.

## Global constraints

- No `sorry`, `admit` or custom `axiom`.
- `r>0` for physical cylindrical use; all differentiability hypotheses stated.
- Do not confuse integrated cancellation with pointwise disappearance.
- No source-specific H8 or differentiation-under-integral claim.

## Review focus

1. Correct tangent vector `(-r sin θ,r cos θ)`.
2. Correct sign of `-y n_x+x n_y`.
3. Endpoint equality supplied by the actual circle, not an assumption on `n`.
4. Derivative integrability must remain explicit.
5. Nonzero angular derivatives allowed before averaging.

### Task 1 — local chain rule and period

**Files:** `UnforcedPatching/PhysicalCircleAngular.lean`, matching smoke module.

- [x] Introduce smoke tests and observe expected missing-module error.
- [x] Prove circle derivative and Frechet composition.
- [x] Prove coordinate-direction identity and endpoint equality.
- [x] Apply angular FTC with an explicit derivative-integrability hypothesis.
- [x] Check Lean and printed foundational axioms.

### Task 2 — release

**Files:** CI smoke target, one documentation note, cumulative manuscript status.

- [x] Update and typeset the cumulative manuscript with accurate boundaries.
- [x] Run exact and Lean regression tests and diff checks.
- [ ] Upload to draft PR and verify remote blob hashes.
