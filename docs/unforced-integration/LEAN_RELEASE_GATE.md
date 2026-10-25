# Unforced periodic integration: Lean release receipt

Date: 25 October 2026. Branch: `integration/unforced-torus-20261025`.

## Checked locally against pinned dependencies

- Lean: `4.34.0-rc2` (commit `6a10ac8c22beadecabdbb0919c2b50214762f91d`)
- Upstream: `openai/NavierStokesAndEuler@f9e8bc5b38b6e212696e8a30e3e91517af887bbd`
- Mathlib: `85e3a25e006c35636f0e53b0e9296caca2685bc0`
- Command: `lake build UnforcedPatching.DefinitionsSmoke UnforcedPatching.ResidualSmoke UnforcedPatching.PeriodicitySmoke UnforcedPatching.ConeBudgetSmoke UnforcedPatching.SevenRayCenterSmoke UnforcedPatching.PressureGaugeSmoke UnforcedPatching.CorrectionSmoke UnforcedPatching.RetentionSmoke`
- Result: **LOCAL COMPILE PASS** (the new terminal-retention smoke and seven preceding smoke targets completed in a 3,319-job Lake build, zero errors). This does not imply GitHub CI has passed.
- Printed axiom sets for the new theorems: `[propext, Classical.choice, Quot.sound]`, without project-local axioms or `sorryAx`.

## What these kernel checks actually establish

1. A correctly typed unforced **candidate definition**, with nonzero initial velocity and finite fundamental-cell squared-speed integral. There is **no witness** and no theorem asserting its existence.
2. Additivity of the full physical viscosity-one residual with both nonlinear cross-advection terms, under explicit first/second derivative regularity.
3. Additivity of spatial divergence and preservation of coordinate periods under sums, with needed differentiability hypotheses.
4. The exact rational H8 margin identity and the seven coefficient **positivity consequence conditional on the weighted coefficient bound**. The existence of a compact spatial correction satisfying that bound remains unknown.
5. Exact invariance of the full residual under an arbitrary time-dependent *spatially constant* pressure gauge, without a differentiability hypothesis on that gauge.
6. An exact sufficient pointwise physical correction equation whose satisfaction implies a zero residual for the patched field. This theorem **does not supply a correction witness**.
7. Full rational source-matched seven-ray covariance, its trace and rank-one projector, the coefficient scaling, and the transformed physical axial-product efficiency `4443/9832`. Independent Python `fractions.Fraction` tests reproduce the finite calculation.
8. Conditional terminal speed retention: if the physical correction obeys `‖w‖ ≤ α‖u‖ + C` at all positive presingular times, with `0 ≤ α < 1` and `C ≥ 0`, unbounded speed of `u` transfers to `u+w`. This does **not** certify the H8 spatial correction, the relative estimate, or a singular leading field.

## CI promotion boundary

The workflow `.github/workflows/unforced-torus-patching.yml` is introduced in this branch. Its PR #3 run [40181414568](https://github.com/tonynewton79-web/unforced-navier-stokes-lean/actions/runs/40181414568) on the preceding head `69d71bb` was observed **QUEUED** on 25 October; the new terminal-retention module will require another run after publication. No successful commit SHA or run can yet be claimed. After a successful action, record its actual run and commit hash here. Do not promote G0, G2, G4, G6, G7, or the full target to `LEAN_KERNEL_CHECKED` solely on passing these helper-module tests: their PDE-construction obligations remain open.

The release validator now restricts the final target status to `OPEN` or `LEAN_KERNEL_CHECKED`. A purported final proof also requires a separately identified `UnforcedPatching.unforcedExistenceTheorem` proving `unforcedTargetStatement`, a statement digest, and CI receipt. These are syntactic checks, **not** cryptographic or online authentication of the run; a human/source audit remains mandatory. The receipt and final theorem do not currently exist.

The unforced finite-time blow-up theorem is still **OPEN**, including H8 compact attachment (`15971/122900` coefficient budget), full pressure and nonlocal right-inverse estimates, and terminal trace retention.
