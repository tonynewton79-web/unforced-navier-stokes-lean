# H8 frame-connection Lean implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Derive the exact connection commutator of a differentiable rotating-frame stress in Lean.

**Architecture:** Use scalar component `HasDerivAt` proofs for the three-term tensor derivative; then use orthogonal matrix identities to obtain the connection formula, skewness and a nonconstant-frame check.

**Tech Stack:** Lean 4.34.0-rc2, pinned Mathlib, existing `FrameMatrix`.

**Spec:** `docs/superpowers/specs/2026-10-27-h8-frame-connection-design.md`.

## Global constraints

- No sorry/admit/custom axiom.
- All differentiability and orthogonality/tangent assumptions explicit.
- No physical H8 source or PDE closure claim.

## Review focus

1. Distinguish E H Eᵀ from Eᵀ H E.
2. Check the sign and order of Ω H − H Ω.
3. Check Ω skewness depends on tangent orthogonality.
4. Confirm each component derivative is proved, not assumed.
5. Nonconstant frame with noncommuting H must have nonzero derivative.

### Task 1 — differential core

**Files:** `UnforcedPatching/FrameConnectionDerivative.lean`, matching smoke module.

- [x] Write missing-module smoke and see expected red result.
- [x] Derive entrywise tensor derivative from scalar product rules.
- [x] Prove matrix equivalence with the existing `rotateStress` representation.
- [x] Prove connection/skew algebra and assemble the derivative theorem.
- [x] Add exact nontrivial connection and trigonometric tests, and print axiom dependencies.

### Task 2 — release

**Files:** CI, integration note, cumulative manuscript.

- [x] Rebuild the integrated manuscript and inspect the rendered PDF.
- [x] Run all regression tests, nine-gate checker and diff checks.
- [x] Upload source and text to the existing draft PR; all seven Git blob hashes match.
