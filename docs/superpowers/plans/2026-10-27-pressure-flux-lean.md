# Pressure-compensated annular flux Lean implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Kernel-check the complete radial fundamental-theorem-of-calculus bridge between the axial source marginal, shear slice, and axial pressure/tensor boundary trace.

**Architecture:** Reuse Mathlib interval integration and the repo's `MeridionalInverse` calculus conventions. Separate the conservative derivative and the integrated identity, retaining the boundary trace as a distinct source term. Supply explicit hypotheses rather than inventing an H8 source.

**Tech Stack:** Lean 4.34.0-rc2, pinned Mathlib, Lake, existing UnforcedPatching definitions.

**Spec:** The `pressure-compensated annular H8 gate` proposition in `paper.tex`, and Tony's approved next decisive analytic Lean bridge.

## Global constraints

- No `sorry`, `admit`, custom `axiom`, or fake physical profile.
- The pressure boundary term must survive the formula unchanged.
- No claim of the full cylindrical source derivation, compact support, rotating-frame derivative control, or unforced PDE closure.

## Review focus

1. Nonzero pressure boundary term survives and changes the source primitive.
2. Zero pressure reduces to the correct simpler identity.
3. The inner boundary term `a*S(a)/r` is retained.
4. Division is allowed only for nonzero radius.
5. Interval integration has actual differentiability and integrability hypotheses.

### Task 1: Prove radial flux identity

**Files:** Create `UnforcedPatching/PressureCompensatedFlux.lean`, create `UnforcedPatching/PressureCompensatedFluxSmoke.lean`.

**Interface:** `pressureCompensatedFluxIdentity` consumes derivative and interval-integrability hypotheses for shear `S`, source `F`, and boundary trace `q`, and returns the displayed exact source primitive equality.

- [x] Write the smoke import and `#check`/`#print axioms` for the named theorem.
- [x] Run `lake env lean` and observe failure because the module does not exist.
- [x] Prove the conservative weighted derivative and the interval FTC identity.
- [x] Compile the theorem and smoke modules with `lake build`.

### Task 2: Integrate and verify

**Files:** Modify `.github/workflows/unforced-torus-patching.yml`; create `docs/unforced-integration/PRESSURE_FLUX_LEAN_20261027.md`.

**Interfaces:** CI builds `UnforcedPatching.PressureCompensatedFluxSmoke`; the note reproduces the certificate and states open PDE gates.

- [x] Add CI smoke target and source-to-Lean scope note.
- [x] Run the full existing Python test suite and `git diff --check`.
- [x] Save on the existing draft research branch and independently verify uploaded byte hashes.
