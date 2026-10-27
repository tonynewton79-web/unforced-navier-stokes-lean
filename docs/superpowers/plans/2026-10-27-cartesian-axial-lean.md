# Cartesian axisymmetric axial divergence implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Kernel-check the Cartesian-to-cylindrical axial divergence formula for radially varying axisymmetric stress, preserving swirl and pressure.

**Architecture:** Define the radius and Cartesian physical axial-column components. Derive the two radial partials from Mathlib's square-root chain rule, prove swirl cancellation, then add an independent axial pressure derivative. Separate this from global H8 source authentication.

**Tech Stack:** Pinned Lean 4.34.0-rc2 and Mathlib, Lake, existing UnforcedPatching modules.

**Spec:** `docs/superpowers/specs/2026-10-27-cartesian-axisymmetric-axial-design.md`.

## Global constraints

- No `sorry`, `admit`, custom `axiom`, or fake physical profile.
- Require strictly positive radius and actual scalar `HasDerivAt` witnesses.
- Preserve nonzero azimuthal stress and axial pressure derivative.
- Distinguish the axisymmetric result from general rotating-frame H8 closure.

## Review focus

1. The origin `x=y=0` must be excluded.
2. The tangential component `N` must be allowed to be nonzero.
3. Differentiation must act on Cartesian `x` and `y`, not assumed cylindrical formulas.
4. The axial derivative of `K_zz+p` must remain in the source.
5. The result must not claim global angular dependence or compact support.

### Task 1: Geometric Lean theorem

**Files:** Create `UnforcedPatching/CartesianAxialBridge.lean` and `UnforcedPatching/CartesianAxialBridgeSmoke.lean`.

**Interfaces:** `cartesianAxisymmetricAxialDivergence` accepts radius positivity and `HasDerivAt` of `M,N`; `cartesianAxialPressureBalance` appends a `HasDerivAt` axial trace. A smoke example uses nonzero `N`.

- [x] Create missing-module smoke test and observe the expected red failure.
- [x] Prove radial square-root chain derivatives and axisymmetric Cartesian divergence.
- [x] Prove the pressure-source corollary and nonzero-swirl example.
- [x] Compile the smoke module; review reported axioms.

### Task 2: Integration and audit

**Files:** Update `.github/workflows/unforced-torus-patching.yml`; create a focused proof-scope note.

- [x] Add CI smoke target and document exact scope and remaining H8 steps.
- [x] Re-run repository tests, `git diff --check`, and Lean build.
- [ ] Upload verified files to existing draft PR #5 and confirm blob hashes.
