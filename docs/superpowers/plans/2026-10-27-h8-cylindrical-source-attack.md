# Full H8 cylindrical source attack plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Certify all Cartesian-to-cylindrical connection contributions for the actual cylindrical source-frame tensor, retaining pressure and missing-source gates.

**Architecture:** An independent exact SymPy tensor calculation checks three frame-direction derivatives and all divergence components. A source-input ledger separates the standard cylindrical frame from the unfrozen H8 cutoff and tilt.

**Tech Stack:** Python/SymPy, unittest, existing Lean 4.34.0-rc2/Mathlib and LaTeX.

**Spec:** `docs/superpowers/specs/2026-10-27-h8-cylindrical-source-authentication-design.md`.

## Global constraints

- Never substitute manufactured polynomial profiles for authentic H8.
- The frame derivative calculations are valid only for r>0.
- Retain angular and axial pressure derivatives and the axial boundary jump.
- Never label H8 cone or global PDE theorem as proved.

## Review focus

1. Connection coefficients `-D/r`, `2C/r`, `A/r` and their signs.
2. Exact `cos(theta),sin(theta)` differentiation with all r factors.
3. `theta` derivatives vanish only after full-circle integration.
4. Pressure stays in all three components and axial jump.
5. Original unprovided H8 cutoff and cone density remain OPEN.

### Task 1 — exact full source

**Files:** `h8_cylindrical_full_source.py`, `tests/test_h8_cylindrical_full_source.py`.

- [ ] Write tests with hand-derived full source and sign regressions.
- [ ] Run red tests against the missing module.
- [ ] Implement E, H, K and Cartesian-chain differentiation.
- [ ] Recompute complete source and prove residual identities.
- [ ] Test genuine nonzero C4/angular and pressure instances.
- [ ] Run the full regression suite and fail-closed proof gates.

### Task 2 — integration

**Files:** H8 authentication note, cumulative LaTeX and draft PR.

- [ ] Record exact source and unprovided authentic profile data.
- [ ] Integrate the three-component formula into the manuscript.
- [ ] Rebuild and inspect PDF with zero layout warnings.
- [ ] Update draft PR, verify remote hashes and CI status.
