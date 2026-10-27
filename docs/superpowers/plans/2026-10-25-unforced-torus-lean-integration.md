# Unforced Torus Lean Integration — First Milestones Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans for native task-by-task execution. Every new proof module requires a failing import/theorem-use test before implementation. Never infer the final PDE theorem from green scalar CI.

**Goal:** Establish an auditable, exact-semantics Lean entry point and proof-obligation atlas for the carrier-independent periodic unforced Navier–Stokes programme, without claiming an as-yet-unproved singularity.

**Architecture:** Base the isolated branch on the current October research branch, retain the upstream viscosity-one `NavierStokes.ProblemStatement` definitions, and add an explicitly different unforced candidate with nonzero initial data. The first semantic theorem will be the exact physical residual-of-sum identity, followed by periodicity/divergence compatibility; later analytic gates remain named obligations, not axioms.

**Tech Stack:** Lean 4.34.0-rc2, pinned Mathlib `85e3a25e006c35636f0e53b0e9296caca2685bc0`, frozen `openai/NavierStokesAndEuler` at `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`, Lake, GitHub Actions, LaTeX and exact Python independent checks.

**Spec:** `docs/superpowers/specs/2026-10-25-unforced-torus-integration-design.md`.

## Global Constraints

- Geometry: periodic `ℝ³/ℤ³` only in the target, with `ℝ³` Edition XXXIX–XLII results kept as separate diagnostics.
- Viscosity: exactly `ν=1` in the first Lean target; general viscosity needs a separate scaling proof.
- Initial data: **nonzero**, explicitly `∃ x : Space, u (0,x) ≠ 0`; never inherit upstream zero-data forced `CandidateProperties`.
- Use physical `navierStokesResidual`, not an unconstrained `R : X→Y` surrogate, when asserting the PDE patching equation.
- Do not introduce project axioms, `sorry`, `admit`, `native_decide`, or unproved existence in a theorem; standard `propext`, `Quot.sound`, `Classical.choice` are permissible and must be listed.
- Do not change the inherited source branches, open draft PRs, or historic files; create narrow integration paths on this branch.
- Final theorem, H8, exact source/local-to-global matching and blow-up retention remain `OPEN` until independently proved and kernel-checked.

## Review Focus

1. **Forced zero-data mismatch:** a test must make the unforced target's nonzero initial datum visible and reject any structural alias for `CandidateProperties` (Task 2).
2. **Wrong pressure sign:** a residual-addition theorem-use test uses the actual upstream `pressureGradient (P+π)` with positive sign and fails if the new definition changes it (Task 3).
3. **Dropped cross advection:** a theorem-use test contains both `(U·∇)w` and `(w·∇)U`, rather than just `(w·∇)w` (Task 3).
4. **Misapplied geometry/regularity:** periodicity and divergence additivity tests use fields on the upstream torus lift and explicit derivative hypotheses, not generic scalar placeholders (Task 4).
5. **False green status:** the targeted workflow executes the real PDE import and Lean tests; manuscript/H8/terminal gates remain `OPEN` even if all current tests pass (Task 5).

---

### Task 1: Audit ledger and source provenance

**Files:**
- Create: `docs/unforced-integration/PROOF_OBLIGATIONS_2026-10-25.md`
- Create: `docs/unforced-integration/SOURCE_ASSETS.md`

**Interfaces:**
- Consumes: spec G0–G8 and the exact named source manuscripts, PR #1 Edition XXXIX–XLII, carrier-independent H8 theorem, current Lean source.
- Produces: stable gate IDs and status labels used by every later declaration and draft PR; source/asset checklist.

- [ ] **Step 1:** Establish an audit check: each gate G0–G8 has a status, geometry, source, Lean declaration (or `NONE`), and independent evidence (or `NONE`). A missing `G4` or `G7` record must fail the check.
- [ ] **Step 2:** Run the check against the currently absent ledger; record the expected missing-file/record failure.
- [ ] **Step 3:** Write the ledger (including H8 exact budget `15971/122900`, latest CI queued, the nonzero-data issue and the `ℝ³`/torus separation) and asset manifest (188-page master `\\includepdf`/asset dependencies, separate 65/16-page papers).
- [ ] **Step 4:** Re-run the audit; ensure G0–G8 complete and all unproved gates say `OPEN`/conditional rather than `PASS`.
- [ ] **Step 5:** Commit only these two files.

### Task 2: Unforced physical candidate definitions

**Files:**
- Create: `UnforcedPatching/Definitions.lean`
- Create: `UnforcedPatching/DefinitionsSmoke.lean`

**Interfaces:**
- Consumes: `NavierStokes.ProblemStatement.{VelocityField, PressureField, Space, preSingularDomain, UnitSpatialPeriodsOn, spatialDivergence, navierStokesResidual, SpeedUnboundedAtOne}`.
- Produces: `UnforcedPatching.InitialNonzero`, `UnforcedPatching.UnforcedPeriodicCandidate`, `UnforcedPatching.unforcedTargetStatement`; exact field names fixed in the new structure: `velocity_smooth`, `pressure_smooth`, `velocity_periodic`, `pressure_periodic`, `divergence_free`, `initial_nonzero`, `navier_stokes_zero`, `speed_unbounded`. A separate `finite_initial_energy` predicate is included only after its torus-cell `IntegrableOn` definition has type-checked.

- [ ] **Step 1:** Write `DefinitionsSmoke.lean` importing `UnforcedPatching.Definitions`, with `#check` for all three named interfaces and an example extracting `initial_nonzero` from a candidate.
- [ ] **Step 2:** Run `lake env lean UnforcedPatching/DefinitionsSmoke.lean`; verify expected failure because the implementation file/declarations do not yet exist (not a network failure).
- [ ] **Step 3:** Implement the minimal definitions using imported viscosity-one physical residual and `∃ x, u (0,x) ≠ 0`. Do not assert the existential target.
- [ ] **Step 4:** Run smoke and `#print axioms`; record whether initial torus kinetic-energy integrability is now a proved consequence or an explicit independent formalization gate.
- [ ] **Step 5:** Commit definitions/smoke only, retaining status `G0 PARTIAL`.

### Implementation name reconciliation (25 October 2026)

The working tree's compiled Task 3 modules are `UnforcedPatching/Residual.lean`
and `ResidualSmoke.lean`; Task 4 modules are `UnforcedPatching/Periodicity.lean`
and `PeriodicitySmoke.lean`. In these files the physical theorem names are
`navierStokesResidual_add`, `unitSpatialPeriodsOn_add`, and
`spatialDivergence_add`. The finite-energy candidate field is
`finite_cell_energy`, defined using the explicitly normalized Euclidean
fundamental-cell Haar measure. These as-built names supersede the earlier
placeholder `ResidualIdentity*`, `Geometry*`, and `finite_initial_energy`
names below. An additional finite algebraic gate is implemented in
`ConeBudget.lean` and `ConeBudgetSmoke.lean`; it proves the conditional
seven-ray floor, **not** existence of the H8 compact inverse.
The subsequently compiled `PressureGauge.lean` and `Correction.lean` and their
smoke tests provide pressure-gauge invariance and conditional physical
zero-residual closure; they do not assert a correction witness.
`SevenRayCenter.lean` and its smoke test later certified the complete
source-matched rational H8 covariance, rank-one trace-free projector,
physical axial efficiency and coefficient scaling. A separate exact
`fractions.Fraction` regression reproduces the finite results.

### Task 3: Exact physical residual identity

**Files:**
- Create: `UnforcedPatching/ResidualIdentity.lean`
- Create: `UnforcedPatching/ResidualIdentitySmoke.lean`

**Interfaces:**
- Consumes: `navierStokesResidual`, `temporalDerivative`, `spatialDerivative`, `advection`, `spatialLaplacian`, `pressureGradient` and Task 2 field definitions.
- Produces: `UnforcedPatching.residual_add` at a physical point. The theorem states exactly
  `R(U+w,P+π)=R(U,P)+R(w,π)+D_x w(U)+D_x U(w)`
  under sufficient local differentiability of both velocities to second order and both pressures to first order. This is algebraically equivalent to the complete `(∂t-Δ)w + (U·∇)w+(w·∇)U+(w·∇)w+∇π` formula.

- [ ] **Step 1:** Write `ResidualIdentitySmoke.lean` first: import the as-yet-absent module and demand `residual_add` with two cross-advection terms; include a usage with the positive pressure gradient. A sign-reversed statement is not an accepted substitute.
- [ ] **Step 2:** Run the test and observe missing declaration, not a typo/configuration error.
- [ ] **Step 3:** Inspect Mathlib derivative-addition and second-derivative theorems in the pinned version; implement the identity using only actual Frechet derivative regularity and bilinear expansion, no new `axiom` or opaque `hResidual` hypothesis.
- [ ] **Step 4:** Run both `lake env lean` commands and `#print axioms residual_add`. Independently expand the residual in a small symbolic polynomial fixture and compare signs/terms.
- [ ] **Step 5:** Commit source and smoke once both compile.

### Task 4: Periodicity and divergence compatibility

**Files:**
- Create: `UnforcedPatching/Geometry.lean`
- Create: `UnforcedPatching/GeometrySmoke.lean`

**Interfaces:**
- Consumes: `UnitSpatialPeriodsOn`, `spatialDivergence`, Task 2 definitions and Mathlib derivative linearity.
- Produces: `unit_periods_add` for field sums and `divergence_add` with appropriate differentiability at `(t,x)`. These do **not** construct a localized correction or prove H8.

- [ ] **Step 1:** Write theorem-use tests for `UnitSpatialPeriodsOn` inheritance and physical `spatialDivergence (U+w)`, requiring explicit hypotheses.
- [ ] **Step 2:** Run smoke; verify failure from missing declarations.
- [ ] **Step 3:** Prove actual periodicity/additive divergence identity with field-point evaluation and `fderiv_add`.
- [ ] **Step 4:** Run smoke, `#print axioms`, and the full available integration tests; do not infer compact support or terminal control.
- [ ] **Step 5:** Commit.

### Task 5: Narrow CI and release receipt

**Files:**
- Create: `.github/workflows/unforced-torus-patching.yml`
- Create: `docs/unforced-integration/LEAN_RELEASE_GATE.md`

**Interfaces:**
- Consumes: Tasks 2–4 Lean source and smoke files.
- Produces: a branch-filtered workflow that installs pinned toolchain, reuses the frozen dependency/cache, rejects proof escapes, compiles all six source/smoke modules, and prints axioms; a human-readable checked-SHA/status ledger.

- [ ] **Step 1:** Write a release-gate expectation requiring source and smoke compilation, not just a scalar `norm_num` test. Confirm current branch lacks this gate.
- [ ] **Step 2:** Add branch-specific workflow and status document with `UNVERIFIED` placeholders; do not label queued runs green.
- [ ] **Step 3:** Trigger or observe GitHub Actions; inspect all check steps, exit statuses, and `#print axioms` outputs.
- [ ] **Step 4:** Update receipt to `PASS` **only** for the exact SHA that truly passed. If queued/failing, preserve `PENDING`/`FAIL` and report actual diagnostics.
- [ ] **Step 5:** Commit the audited status and open a **draft** PR targeting `feature/zenodo-23474915-lean` (not `main`).

### Task 6: Cumulative manuscript assembly and source/asset audit

**Files:**
- Create: `docs/unforced-integration/MANUSCRIPT_ASSEMBLY.md`
- Create: `paper/unforced_torus_cumulative.tex` only when all necessary input assets are present and verified; otherwise keep a complete missing-asset ledger.

**Interfaces:**
- Consumes: attached 188-page master LaTeX, 65-page carrier-independent LaTeX, 16-page exact local-core LaTeX, Editions XXXIX–XLII PDFs, and the checked proof-obligation ledger.
- Produces: one ordered manuscript source tree and a page/asset/source provenance report, explicitly distinguishing proved restrictions from conditional constructions.

- [ ] **Step 1:** List exact `\\input`, `\\includepdf`, `\\includegraphics`, bibliography, and package dependencies of each supplied source; demonstrate failure of a full build with a missing dependency when applicable.
- [ ] **Step 2:** Sort and deduplicate overlapping inserts by original date, theorem scope and dependency; flag superseded, withdrawn and contradictory claims.
- [ ] **Step 3:** Assemble a cumulative chapter map with at most nine main sections; separate the periodic core/patching development from whole-space transport obstructions and benchmarks.
- [ ] **Step 4:** If every required byte is available, compile twice, check labels/citations, render all pages, and inspect overlaps. If any is absent, preserve a manifest rather than claim a built full manuscript.
- [ ] **Step 5:** Commit assembly/asset status. Do not announce a publication-ready full PDF unless verified.

### Task 7: Next research-only mathematical milestones (not promised as implementation success)

**Files (future, after analytic proof):**
- `docs/unforced-integration/H8_PROFILE_CERTIFICATE.md`
- `UnforcedPatching/AnalyticGates.lean`
- `UnforcedPatching/Final.lean`
- Compiled cumulative PDF only after the necessary sources/assets have been provided and visually verified.

**Interfaces:**
- Consumes: genuine solution of the H8 fixed-profile weighted compact inverse bound, a fully matched local unforced core, and exact global handoff estimates.
- Produces: formally checked compact support, pressure, energy, smoothness and terminal retention. The existential `unforcedTargetStatement` may become a theorem *only then*.

- [ ] Freeze one explicit smooth compact profile and the seven-ray coefficient inverse; verify exact `15971/122900` margin by rigorous interval/rational arithmetic or find a dual obstruction.
- [ ] Prove the geometry-specific core/regular right-inverse range and `4 M_G C_B η<1` gate.
- [ ] Formalize the physical pressure/zero force, global periodic smoothness, nonzero initial energy and terminal trace retention.
- [ ] Audit complete analytic LaTeX/Lean correspondence; render and inspect the cumulative PDF from a full source/asset manifest.
- [ ] Only after all G0–G8 close, state and prove the final no-extra-assumption Lean existential theorem.

## Self-review / handoff

The first six tasks are testable and worthwhile independently of future research success. Task 7 is **open mathematics**, not an engineering deliverable with a guaranteed end date. All source-specific A.11/A.19 material is a dependency only if the actual selected carrier-independent core requires it; otherwise keep it in the parallel forced-source diagnostic ledger. The plan does not authorize merging PR #1 or claiming an unforced Millennium-problem proof.

Review the spec and this plan before executing Task 1. Recommended execution mode: native incremental implementation, followed by independent whole-branch mathematical and Lean review.
