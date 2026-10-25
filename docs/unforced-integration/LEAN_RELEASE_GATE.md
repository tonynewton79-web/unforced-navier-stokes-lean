# Unforced periodic integration: Lean release receipt

Date: 25 October 2026. Branch: `integration/unforced-torus-20261025`.

## Checked locally against pinned dependencies

- Lean: `4.34.0-rc2` (commit `6a10ac8c22beadecabdbb0919c2b50214762f91d`)
- Upstream: `openai/NavierStokesAndEuler@f9e8bc5b38b6e212696e8a30e3e91517af887bbd`
- Mathlib: `85e3a25e006c35636f0e53b0e9296caca2685bc0`
- Command: `lake build UnforcedPatching.DefinitionsSmoke UnforcedPatching.ResidualSmoke UnforcedPatching.PeriodicitySmoke` and `lake build UnforcedPatching.ConeBudgetSmoke`
- Result: **LOCAL COMPILE PASS** (the final H8 smoke dependency graph rebuilt 3,308 jobs, zero errors). This does not imply GitHub CI has passed.
- Printed axiom sets for the new theorems: `[propext, Classical.choice, Quot.sound]`, without project-local axioms or `sorryAx`.

## What these kernel checks actually establish

1. A correctly typed unforced **candidate definition**, with nonzero initial velocity and finite fundamental-cell squared-speed integral. There is **no witness** and no theorem asserting its existence.
2. Additivity of the full physical viscosity-one residual with both nonlinear cross-advection terms, under explicit first/second derivative regularity.
3. Additivity of spatial divergence and preservation of coordinate periods under sums, with needed differentiability hypotheses.
4. The exact rational H8 margin identity and the seven coefficient **positivity consequence conditional on the weighted coefficient bound**. The existence of a compact spatial correction satisfying that bound remains unknown.

## CI promotion boundary

The workflow `.github/workflows/unforced-torus-patching.yml` is introduced in this branch. The GitHub workflow run [40178823488](https://github.com/tonynewton79-web/unforced-navier-stokes-lean/actions/runs/40178823488) on the preceding branch commit was observed **QUEUED**; the newly added cone-budget module and stronger ledger tests will require another run. No successful commit SHA or run can yet be claimed. After a successful action, record its actual run and commit hash here. Do not promote G0, G2, G4, G6, or the full target to `LEAN_KERNEL_CHECKED` solely on passing these helper-module tests: their PDE-construction obligations remain open.

The release validator now restricts the final target status to `OPEN` or `LEAN_KERNEL_CHECKED`. A purported final proof also requires a separately identified `UnforcedPatching.unforcedExistenceTheorem` proving `unforcedTargetStatement`, a statement digest, and CI receipt. These are syntactic checks, **not** cryptographic or online authentication of the run; a human/source audit remains mandatory. The receipt and final theorem do not currently exist.

The unforced finite-time blow-up theorem is still **OPEN**, including H8 compact attachment (`15971/122900` coefficient budget), full pressure and nonlocal right-inverse estimates, and terminal trace retention.
