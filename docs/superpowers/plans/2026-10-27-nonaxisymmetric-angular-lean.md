# Nonaxisymmetric axial geometry and angular mean implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Kernel-check the full local nonaxisymmetric Cartesian axial mixed-stress divergence and the exact cancellation of a periodic angular derivative after averaging.

**Architecture:** Decompose the Cartesian physical axial column with `r=sqrt(x²+y²)` and prove its actual Cartesian derivatives. Independently use interval FTC for the angular derivative and integrate the sum; do not silently discard the term pointwise.

**Tech Stack:** Pinned Lean 4.34.0-rc2, Mathlib, Lake.

**Spec:** `docs/superpowers/specs/2026-10-27-nonaxisymmetric-angular-design.md`.

## Global constraints

- No `sorry`, `admit`, custom `axiom` or fabricated H8 function.
- Work away from the cylindrical axis (`r>0`).
- Distinguish pointwise divergence from averaged cancellation.
- Keep axial pressure/tensor boundary traces in the source-to-flux chain.

## Review focus

1. Nonconstant angular stress must contribute pointwise.
2. Angular derivative cancels only with genuine endpoint periodicity.
3. `2π` normalization must be correct, with integrability assumptions.
4. Cartesian `x` and `y` derivatives must really be taken.
5. The theorem must not assume an H8 frame/cutoff is authenticated.

### Task 1 — periodic angular FTC

**Files:** Create `UnforcedPatching/AngularMean.lean`, `UnforcedPatching/AngularMeanSmoke.lean`.

**Interfaces:** `angularDerivativeIntegral_zero` and `angularMean_derivative_vanishes`; a nonconstant periodic profile regression.

- [x] Add smoke test, observe missing-module red failure.
- [x] Implement angular FTC and mean cancellation.
- [x] Compile smoke and inspect axioms.

### Task 2 — general Cartesian mixed-stress divergence

**Files:** Create `UnforcedPatching/NonaxisymmetricAxialBridge.lean`, `UnforcedPatching/NonaxisymmetricAxialBridgeSmoke.lean`.

**Interfaces:** `cartesianGeneralAxialDivergence` consumes four Cartesian derivative witnesses, preserves both polar-directional terms; `cartesianGeneralAxialPressureBalance` adds the axial derivative.

- [x] Add smoke test, observe missing-module red failure.
- [x] Prove Cartesian derivative identity and angular stress contribution.
- [x] Compile smoke and inspect axioms.

### Task 3 — audit and upload

**Files:** CI workflow and one focused scope note.

- [x] Add both smoke targets; describe exact remaining authentic H8 gates.
- [x] Re-run complete Python suite, Lean targets, and `git diff --check`.
- [x] Upload to draft PR #5 and independently compare Git blob hashes.
