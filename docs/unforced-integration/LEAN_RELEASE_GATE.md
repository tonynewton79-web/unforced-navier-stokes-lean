# Unforced periodic integration: Lean release receipt

Date: 25 October 2026. Branch: `integration/unforced-torus-20261025`.

## Checked locally against pinned dependencies

- Lean: `4.34.0-rc2` (commit `6a10ac8c22beadecabdbb0919c2b50214762f91d`)
- Upstream: `openai/NavierStokesAndEuler@f9e8bc5b38b6e212696e8a30e3e91517af887bbd`
- Mathlib: `85e3a25e006c35636f0e53b0e9296caca2685bc0`
- Command: `lake build UnforcedPatching.DefinitionsSmoke UnforcedPatching.ResidualSmoke UnforcedPatching.PeriodicitySmoke UnforcedPatching.ConeBudgetSmoke UnforcedPatching.ConeOperatorSmoke UnforcedPatching.SevenRayCenterSmoke UnforcedPatching.PressureGaugeSmoke UnforcedPatching.CorrectionSmoke UnforcedPatching.RetentionSmoke UnforcedPatching.CompactGaugeSmoke UnforcedPatching.MeridionalInverseSmoke`
- Result: **LOCAL COMPILE PASS** for all 11 smoke targets in one 3,372-job Lake build, zero errors. The new source-matched theorem was independently recompiled after being added. GitHub-hosted CI for the new head must still be checked separately.
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
9. The sharp four-field-to-seven-ray coefficient operator norm is exactly `14` in the componentwise maximum norm. It yields an explicitly stronger **sufficient** stress-coordinate smallness condition `max(|A|,|B|,|C|,|D|) ≤ (15971/1720600)ρ`, not a constructed compact weighted inverse.
10. A genuine radial derivative compatibility theorem for the explicit two-diagonal pressure-neutral gauge `K=r F_r`, `C=K+F`. The full cylindrical divergence identity and zero radial moment are paper calculations, not formal theorems. The pressure-neutral gauge does not solve the **prescribed** H8 residual and does not guarantee positivity. An independent exact rational polynomial negative control finds uncompensated pure-radial divergence curl `-5103/32768` at `(5/4,1/2)`.
11. New `MeridionalInverse`: Lean checks the **two defined cylindrical meridional divergence expressions** of the source-matched hoop correction and actual axial interval primitive, with Mathlib FTC hypotheses; it also checks `(rH)'=rJ` via the radial moment integral and its mixed carrier, plus the direct source match `S_zz=ρ`, `f_z=∂zρ` used in the dual test. These are pointwise coordinate identities only, **not** the Cartesian divergence bridge, global smooth compact support, force compatibility, or weighted H8 estimate. Its smoke module reports only standard logical axioms.
12. An independent exact rational certificate supplies a pressure-neutral dual obstruction for the **stronger physical entrywise** stress cap at the same numeric `β=15971/1720600`. It does **not** imply a counterexample to the original H8 four-coordinate cone. The exact positive margin is `443015653/2967690880000`.

## CI promotion boundary

The workflow `.github/workflows/unforced-torus-patching.yml` is in this branch. Its PR #3 run [40191730077](https://github.com/tonynewton79-web/unforced-navier-stokes-lean/actions/runs/40191730077) on the preceding head `fbe23c3` was observed **QUEUED** on 25 October; the compact-gauge theorem requires a new run after publication. No successful commit SHA or run can yet be claimed. After a successful action, record its actual run and commit hash here. Do not promote G0, G2, G4, G6, G7, or the full target to `LEAN_KERNEL_CHECKED` solely on passing these helper-module tests: their PDE-construction obligations remain open.

The release validator now restricts the final target status to `OPEN` or `LEAN_KERNEL_CHECKED`. A purported final proof also requires a separately identified `UnforcedPatching.unforcedExistenceTheorem` proving `unforcedTargetStatement`, a statement digest, and CI receipt. These are syntactic checks, **not** cryptographic or online authentication of the run; a human/source audit remains mandatory. The receipt and final theorem do not currently exist.

The unforced finite-time blow-up theorem is still **OPEN**, including H8 compact attachment (`15971/122900` coefficient budget), full pressure and nonlocal right-inverse estimates, and terminal trace retention.
