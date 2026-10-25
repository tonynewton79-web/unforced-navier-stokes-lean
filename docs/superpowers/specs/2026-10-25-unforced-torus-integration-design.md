# Unforced periodic Navier–Stokes: proof-integration design

Date: 25 October 2026. Repository: `tonynewton79-web/unforced-navier-stokes-lean`. Integration branch: `integration/unforced-torus-20261025`, frozen at inherited research commit `1376c33866a103b2019cfee871e1924aa8ae2b7d` when created.

## 1. Intent, output, and honest theorem status

Consolidate Tony Newton's exact-local-core, carrier-independent structured-stress, periodic closure, and October XXXIX–XLII results into one dependency-controlled programme. The primary mathematical target is an **unforced** incompressible Navier–Stokes finite-time blow-up construction on the unit three-torus `ℝ³/ℤ³`. Use a separate whole-space diagnostic lane for the recent Gaussian, cylinder, and near-axis results; never infer torus assertions from `ℝ³` assertions without an explicit localization/periodization theorem.

This work does not currently prove the target. A successful finite scalar Lean file is not a full PDE formalization. Release states are exactly `PROVED_PAPER`, `LEAN_KERNEL_CHECKED`, `CONDITIONAL`, `TESTED_NUMERICALLY`, `OPEN`, `REFUTED_FOR_ROUTE`; each theorem can carry multiple classifications with precise scope.

## 2. Target proposition and physical conventions

Use the pinned `NavierStokes.ProblemStatement` types `Space`, `SpaceTime`, `VelocityField`, `PressureField`, `UnitSpatialPeriodsOn`, `navierStokesResidual`, and `SpeedUnboundedAtOne`, at viscosity **exactly one**. To claim all positive viscosities, separately prove a scaling theorem; do not silently mix source parameters with this normalization.

Define `UnforcedPeriodicCandidate (u : VelocityField) (p : PressureField) : Prop` with:
1. `ContDiffOn ℝ ∞ u preSingularDomain` and the same for `p`;
2. unit periodicity of `u` and `p` on `Ico 0 1`;
3. divergence-free velocity on `Ico 0 1`;
4. `navierStokesResidual u p t x = 0` for every `t ∈ Ioo 0 1` and `x`;
5. smooth, periodic, divergence-free **nonzero** initial velocity `u₀=u(0,·)` and appropriate finite torus kinetic energy;
6. `SpeedUnboundedAtOne u`.

The imported upstream `CandidateProperties` assumes *zero* initial velocity and includes a smooth external force. Do not reuse it as an unforced candidate: the smooth unforced energy identity makes zero-data finite-energy blow-up impossible. The main target is `∃ u p, UnforcedPeriodicCandidate u p` only when every analytic gate below has been discharged. Do not introduce this existential as an axiom.

For a smooth periodic background `U,P` and correction `w,π`, the physical residual identity is
```
R(U+w,P+π)
 = R(U,P) + (∂ₜ-Δ)w + (U·∇)w
   + (w·∇)U + (w·∇)w + ∇π.
```
This algebra is the first *semantic* Lean integration target. It must be stated for the actual Frechet derivative definitions with sufficient smoothness, not just variables standing for generic elements of an abstract module. Divergence-free, period preservation, pressure gauge, energy and endpoint retention are additional, independent obligations.

## 3. Selected approach and alternatives

- **Selected primary lane:** periodic `𝕋³`, carrier-independent compact stress attachment, seven-ray positive cone, H8 weighted compact anti-divergence. It matches the existing abstract closure repository and the mathematical work's explicit `C₄` lattice geometry.
- **Kept as independent diagnostics:** `ℝ³` source-native direct forced-carrier correction, Annex/Edition XXXIX–XLII angular-momentum flux restrictions and Gaussian examples. These are not automatic periodic blow-up lemmas.
- **Rejected as an unqualified shortcut:** reuse the OpenAI *forced* Navier–Stokes theorem with the force set to zero; splice local terminal core and distant shell without proving exact residual cancellation; or infer the final conclusion from the abstract fixed-point lemma alone.

## 4. Mathematical proof dependency gates

| Gate | Mathematical obligation | Current boundary |
| --- | --- | --- |
| G0 | Exact theorem statement, viscosity, torus, nonzero data, pressure gauge, energy, singularity notion | Definition to be built and checked |
| G1 | Source-compatible local unforced coefficient hierarchy, pressure, normal convergence, real physical residual zero and first-shell jets | Paper-level claim; source A.11/A.19 and full PDE Lean reconstruction incomplete |
| G2 | Divergence-free `C₄` localization, mean control, transverse anti-divergence and full-gradient helical interface | Conditional analytic results, not full Lean |
| G3 | Temporal two-color stress routing, moving-frame phase locking, dyadic carrier coherence and actual graph-norm constants | Paper-level reductions, not full Lean |
| G4 | **H8**: explicit compact weighted symmetric anti-divergence and shrinking-support anisotropic covariance with a provable coefficient margin | OPEN: exact profile and weighted inverse bound missing |
| G5 | Coupled structured-to-regular contraction: actual right inverse range `K_full G_reg S_r(Y) ⊆ Y_c`, contraction constant, Banach completeness | Abstract algebra checked only |
| G6 | One global periodic pressure and zero *physical* force, smoothness and finite energy for all `t<1` | OPEN |
| G7 | Exact persistence of a nonzero terminal trace against the global correction, yielding `SpeedUnboundedAtOne` | OPEN |
| G8 | Completely trusted Lean theorem depending only on Mathlib and cited proved upstream facts; no `sorry`, `admit`, `native_decide` shortcuts or project axioms | OPEN |

For the seven-ray centre the paper gives exact rational axial efficiency `4443/9832>9/20`, coefficient floor `172/1229`, and H8 sufficient budget `𝒞(H) ≤ (15971/122900)ρ`. This **inequality for the actual frozen profile is not proved**. The predecessor periodic Green inverse has the right scaling but not compact weighted support; generic compact symmetric inverses lack the quantitative coefficient bound. Any failure or dual obstruction must be recorded, not hidden.

## 5. Source incorporation, cross-checks, and publication layout

Maintain a theorem ledger with stable IDs, exact source (paper/equation/PR SHA), geometry (`𝕋³` or `ℝ³`), analytic conditions, proof status, Lean declaration, test/CI evidence and downstream gate. Preserve previous work without assuming it is compatible. Resolve superseded and contradictory claims explicitly.

The scholarly cumulative TeX/PDF will use at most nine main sections and seven subsections per section, with central theorem early, notation before use, complete proofs, restrained visuals, accurate provenance and a claim-status paragraph. Its October XXXIX–XLII inserts belong to the *limitations/independent diagnostics* discussion unless a genuine analytic bridge demonstrates positive terminal retention. Do not treat their necessary energy/BV bounds or short-time viscous torque growth as a singularity mechanism.

Do not silently replace original attached manuscript sources or merge either existing draft PR. Preserve existing user work and edit only newly agreed integration files. No automated public-claim upgrade from CI green.

## 6. Lean architecture

Start with a single narrow `UnforcedPatching` module importing `NavierStokes.ProblemStatement`; keep the existing `UnforcedClosure` and `PDEIntegration` unchanged. Formalize the exact unforced candidate *definition* and elementary refusals. Prove the physical residual addition identity only after checking upstream derivative rules and field smoothness. Separate purely algebraic scalar certificates from analytic PDE declarations. Use only source-justified hypotheses and display them in theorem signatures.

Proof files are grouped by semantics rather than paper edition: `UnforcedPatching/Definitions.lean`, `UnforcedPatching/ResidualIdentity.lean` (later), `UnforcedPatching/Geometry.lean` (later), `UnforcedPatching/AnalyticGates.lean` (later), `UnforcedPatching/Final.lean` (last). The first two are only a proposed interface until type-checked against the pinned compiler. Avoid large imports or wholesale reorganization without a separate review.

## 7. Verification, falsification, and release policy

All new Lean declarations: source hygiene check, `lake env lean` in pinned Lean/Mathlib/upstream environment, `#print axioms` inspection, clean-branch CI receipt. Tests must fail for an absent intended definition or changed physical residual; simply passing a scalar theorem under an unproved premise is not a physical check. Independent exact-rational/SymPy tests can support finite identities but cannot certify analytic source intervals or pressure.

Negative controls: (a) unforced zero-data candidate is ruled out by energy, (b) forced `CandidateProperties` is never accepted as target, (c) `ℝ³` Gaussian smooth example is not tagged singular, (d) persistent shrinking-radius flux is ruled out by Edition XL dissipation, (e) H8 absent or wrong weighted constant prevents release, (f) missing range or pressure term prevents claiming zero physical residual.

No claim of a full unforced blow-up proof until all G0–G8 are proved and a fresh pinned Lean build passes without project axioms. Any queued, cancelled or failing CI stays `UNVERIFIED`.

## 8. First incremental deliverable and review boundary

Deliver (i) this design, (ii) an executable implementation plan, (iii) a status-indexed theorem/obligation ledger, and (iv) after plan review, the smallest physical-semantics Lean module on the integration branch. Create a **draft** PR targeting the original research branch, not `main`, so the new checks can be reviewed without merging the 898-commit research PR. The first milestone may verify only definitions/elementary refusals; it must never be represented as the desired full theorem.

After the bridge is honestly defined, attack H8 with one explicitly frozen compact profile and either a rigorous rational/interval weighted bound or a dual counterexample. The remaining mathematical work is research, not a bounded implementation task with a guaranteed positive outcome.
