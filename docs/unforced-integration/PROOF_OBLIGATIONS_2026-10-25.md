# Unforced periodic Navier–Stokes: proof and certification ledger

25 October 2026. Primary target: viscosity-one incompressible flow on the unit three-torus with **nonzero** smooth initial velocity, finite torus kinetic energy, no external force and speed unbounded as time approaches one. This is an auditable *research target*, not a proved existential theorem.

The authoritative machine-readable gate data are in [`proof_gates.json`](proof_gates.json), checked by `python tools/check_proof_gates.py docs/unforced-integration/proof_gates.json`. A successful ledger validation checks status completeness and evidence syntax only; it is **not** a PDE proof and cannot independently attest a GitHub Actions run.

## Main dependency graph

| Gate | Domain | Present analytic/machine status | Mathematical bridge still needed |
|---|---|---|---|
| G0 — physical theorem | Torus | OPEN | Define actual Lean proposition for nonzero initial data, viscosity one, divergence, periodicity, finite energy and speed growth. |
| G1 — exact local core | Local whole space | PAPER_CONDITIONAL | Independently certify common source profiles, full hierarchy/pressure, differentiated convergence and analytic first-shell supply. Local-to-torus chart transport remains separate. |
| G2 — periodic localization | Torus | PAPER_CONDITIONAL | Physical mean/pressure identities, nonlocal transverse inverse and compatible first-shell bounds. |
| G3 — temporal carriers | Torus | PAPER_CONDITIONAL | Two-color, phase-lock, compact tube and graph-space PDE inequalities, not only scalar algebra. |
| G4 — shrinking spatial attachment | Torus | **OPEN**; exact pointwise margin algebra compiled in Lean | One explicit compact H8 profile and weighted inverse with exact coefficient budget `15971/122900`. |
| G5 — coupled contraction | Torus | **OPEN** | Physical right-inverse range `K_full G_reg S_r(Y) ⊆ Y_c`, constants `4 M_G C_B η < 1`, Banach completeness and smoothness bootstrap. |
| G6 — physical unforced completion | Torus | **OPEN** | Full zero vector-valued residual, one pressure gauge, smooth periodic finite-energy solution on every `t<1`. |
| G7 — singular trace retention | Torus | **OPEN**; conditional subleading-correction theorem locally compiled in Lean | Produce a genuine singular leading field and verify the needed strict relative correction bound along its terminal approach. |
| G8 — final Lean theorem | Torus | **OPEN** | Full end-to-end theorem free of project-local axioms/admissions, audited `#print axioms` and a successful pinned CI run. |

Source-of-claim distinctions:

- `UnforcedClosure.fixedPoint_implies_zero_residual` is an **abstract** module theorem with a previously recorded successful kernel check; it does not discharge G5. `PDEIntegration.lean` currently checks imported declaration names, not an unforced physical solution.
- The imported OpenAI `NavierStokes.ProblemStatement.CandidateProperties` includes a force and **zero initial velocity**. It cannot serve as the new unforced nonzero-data theorem. At viscosity one, `navierStokesResidual` carries the physical acceleration, advection, Laplacian and **positive** pressure-gradient sign.
- Original source stages A.11/A.19 are not blanket G1 assumptions for the carrier-independent periodic route. They become obligations only if an exact dependency of the selected local core on those stages is exhibited; otherwise keep them in the independent forced-source audit.
- `Carrier_Independent_Structured_Stress_Route_FINAL_COLOUR.tex`, Proposition on the rational seven-ray centre, supplies pointwise algebra `4443/9832 > 9/20` and coefficient floor `172/1229`. It explicitly leaves the compact H8 weighted bound open. Finite algebra does not solve it.
- `UnforcedPatching.ConeBudget` now kernel-checks the exact rational difference `172/1229 - 1/100 = 15971/122900` and derives a seven-ray positive coefficient floor **assuming** the bound on all seven corrections. It does not construct the weighted compact inverse or certify that the bound holds for any specific profile.
- `UnforcedPatching.SevenRayCenter` computes the full `3×3` raw rational covariance directly from the seven rays, proves its trace, the source-matched trace-free rank-one projector, all seven normalized raw coefficients, and the exact physical radial–axial product `-4443/9832`. The independent `tests/test_seven_ray_exact.py` replay agrees. This verifies algebraic H8 input, not the existence or bounds of a spatial stress solution.
- `UnforcedPatching.PressureGauge` proves spatially constant time-dependent shifts do not change the pressure gradient or full residual. `UnforcedPatching.Correction` proves that an actual solution of the complete pointwise nonlinear correction equation cancels the residual of the summed field. Neither module constructs the correction, solves H8 or proves terminal speed blow-up.
- `UnforcedPatching.Retention` proves the exact `SpeedUnboundedAtOne` quantifiers persist under `‖w(t,x)‖ ≤ α ‖u(t,x)‖ + C` on physical times when `0 ≤ α < 1` and `C ≥ 0`; uniformly bounded corrections are a corollary. This is a conditional G7 implication, not evidence that the terminal leading field or its physical correction exists. The strict inequality matters: `w = -u` would cancel the trace if `α = 1` were allowed.
- The 188-page `Unforced_Finite-Time_Blow-Up_for_Navier-Stokes.pdf` repeatedly calls its global periodic route conditional, not end-to-end Lean-compiled. Its earlier continuous-global-axisymmetry torus route was withdrawn in favor of local lifts, `C4`, and one global periodic pressure.

## Whole-space diagnostics kept outside the torus proof chain

| 25 October work | Exact mathematical scope | What it does **not** establish |
|---|---|---|
| Edition XXXIX: moving cylinders | Angular-momentum conservation, four moving-boundary fluxes, dyadic transfer and Fourier leakage | Positive terminal transport or pointwise blow-up |
| Edition XL extension | Energy–dissipation rules out a persistent `τ^{-h}` advective flux on the parabolic moving radius | No-go for narrow intermittent flux/derivative spikes or viscous/axial transport |
| Edition XLI | Radial space–time variation and an exact leading Cartesian axis torque coefficient | The required source-compatible positive terminal torque lower bound |
| Edition XLII | Exact pressure-complete jet equation and short-time positive coefficient derivative for one **globally smooth** unforced Gaussian example | A closed positive jet ODE, nonlinear-strain growth mechanism, terminal blow-up or a Lean PDE proof |

These statements are about `ℝ³` and remain hypotheses/benchmarks for `𝕋³` until a separate geometry-transfer theorem is established. The XLII positive derivative is initially produced by viscosity, not the nonlinear pressure-complete acceleration.

## Lean verification boundary and acceptance

The currently imported proof development is pinned at Lean `v4.34.0-rc2`, Mathlib commit `85e3a25e006c35636f0e53b0e9296caca2685bc0`, upstream OpenAI `NavierStokesAndEuler` commit `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`.

A new mathematical gate is promoted only after (1) source-matched full hypotheses and an independently valid analytic derivation, (2) actual Lean proposition semantic comparison, (3) successful targeted compile at a recorded commit, (4) `#print axioms` review, and (5) a clear result/discrepancy ledger. Standard `propext`, `Quot.sound`, `Classical.choice` are acceptable; new project axioms and `sorryAx` are not.

`LEAN_KERNEL_CHECKED` in the JSON requires a nonempty declaration list and a successful CI receipt; the script validates fields but does not query GitHub to authenticate the run. Any malformed or queued receipt must remain unpublished as PASS. Source-numerical and exact-rational checks apply only to the quantified finite claim being tested.

## Task execution rulings

- **Ruling:** machine-readable `proof_gates.json` and a standard-library validation test accompany the human ledger — human prose alone cannot enforce fail-closed release; cost: a small schema to maintain in every proof update.
- **Ruling:** run a focused standard-library unit-test suite before treating all historical tests as available; the workspace does not yet contain `pytest` or Lean, while the pre-existing `python verify_unforced_closure.py` passed its three finite abstract checks in this session. Cost: Lean/GitHub kernel outcome must be checked separately and cannot be implied by local Python.

No claim of an unforced finite-time Navier–Stokes singularity or full Lean certification is made here.
