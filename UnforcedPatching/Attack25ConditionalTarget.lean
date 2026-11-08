import UnforcedPatching.Correction
import UnforcedPatching.Retention
import UnforcedPatching.Definitions
import Mathlib

/-!
# Attack 25: semantic endpoint for the *unforced* periodic problem

This file makes the remaining obligations explicit in the exact upstream PDE
types. In particular, the correction equation is still a HYPOTHESIS:
the file does not construct w, assume the final target, or claim blow-up.

Only after another development proves all the assumptions from a genuine
profile and global correction can this conditional theorem be used to close
the complete target. The hypotheses must never be relabelled as "verified".
-/

noncomputable section
namespace UnforcedPatching

open NavierStokes.ProblemStatement
open Set
open scoped ContDiff

/-- Physical, conditional assembly. This is not an existence theorem.

The two residual regularity conditions are needed for fderiv_add, including
the Laplacian. The complete correction PDE is a separate analytic
obligation. The pressure and periodicity are physical rather than abstract.
-/
theorem target_of_constructed_correction
    (U w : VelocityField) (p π : PressureField)
    (hUreg : ∀ t ∈ Ioo (0 : ℝ) 1, ∀ x : Space,
      ResidualRegularAt U p t x)
    (hwreg : ∀ t ∈ Ioo (0 : ℝ) 1, ∀ x : Space,
      ResidualRegularAt w π t x)
    (hcorrection : ∀ t ∈ Ioo (0 : ℝ) 1, ∀ x : Space,
      PhysicalCorrectionEquation U p w π t x)
    (huSmooth : ContDiffOn ℝ ∞ (U + w) preSingularDomain)
    (hpSmooth : ContDiffOn ℝ ∞ (p + π) preSingularDomain)
    (hvelPeriods : UnitSpatialPeriodsOn (Ico (0 : ℝ) 1) (U + w))
    (hpressPeriods : UnitSpatialPeriodsOn (Ico (0 : ℝ) 1) (p + π))
    (hinit : InitialNonzero (U + w))
    (henergy : FiniteCellEnergy (U + w))
    (hsol : ∀ t ∈ Ico (0 : ℝ) 1, ∀ x : Space,
      spatialDivergence (U + w) t x = 0)
    (hcarrierBlowup : SpeedUnboundedAtOne U)
    (hsubleading : SubleadingCorrectionBound U w) :
    unforcedTargetStatement := by
  unfold unforcedTargetStatement
  refine ⟨U + w, p + π, ?_⟩
  refine {
    velocity_smooth := huSmooth
    pressure_smooth := hpSmooth
    velocity_periodic := hvelPeriods
    pressure_periodic := hpressPeriods
    initial_nonzero := hinit
    finite_cell_energy := henergy
    divergence_free := hsol
    navier_stokes_zero := ?_
    speed_unbounded := speedUnbounded_add_subleading U w hcarrierBlowup hsubleading
  }
  intro t ht x
  exact physicalCorrection_closes U w p π t x
    (hUreg t ht x) (hwreg t ht x) (hcorrection t ht x)

#print axioms target_of_constructed_correction

end UnforcedPatching
