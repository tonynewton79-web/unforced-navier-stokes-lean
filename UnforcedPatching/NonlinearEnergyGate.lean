import Mathlib

/-!
# Nonlinear correction algebra and the dyadic energy gate

This file intentionally proves *only* algebraic implications.  A proof of the
physical energy identity, radial Poincare inequality, and the carrier's
actual terminal norm bounds remains an independent PDE analysis obligation.
No unforced singular solution is asserted or postulated here.
-/

namespace UnforcedPatching

noncomputable section

variable {X Y : Type*}
variable [AddCommGroup X] [Module ℝ X]
variable [AddCommGroup Y] [Module ℝ Y]

/-- The frozen projected linear-plus-quadratic residual.  `B` is bilinear. -/
def abstractResidual (L : X →ₗ[ℝ] Y)
    (B : X →ₗ[ℝ] X →ₗ[ℝ] Y) (U : X) : Y :=
  L U + B U U

/-- The left-hand side of the full correction equation moved to zero. -/
def abstractCorrectionDefect (L : X →ₗ[ℝ] Y)
    (B : X →ₗ[ℝ] X →ₗ[ℝ] Y) (U w : X) : Y :=
  L w + B U w + B w U + B w w + abstractResidual L B U

/-- The correction defect is exactly the full residual of `U + w`. -/
theorem abstractCorrectionDefect_eq_totalResidual
    (L : X →ₗ[ℝ] Y) (B : X →ₗ[ℝ] X →ₗ[ℝ] Y)
    (U w : X) :
    abstractCorrectionDefect L B U w = abstractResidual L B (U + w) := by
  simp only [abstractCorrectionDefect, abstractResidual, map_add, LinearMap.add_apply]
  abel

/-- The exact correction `w = -U` always satisfies the correction equation.
It produces the zero total velocity and therefore proves no singularity. -/
theorem trivial_cancellation_solves_abstract_correction
    (L : X →ₗ[ℝ] Y) (B : X →ₗ[ℝ] X →ₗ[ℝ] Y)
    (U : X) :
    abstractCorrectionDefect L B U (-U) = 0 := by
  rw [abstractCorrectionDefect_eq_totalResidual]
  simp [abstractResidual]

/-- The equality of frozen source stress and frozen residual is *not* a
non-cancellation condition: complete cancellation still solves the algebra. -/
theorem exact_source_match_does_not_forbid_cancellation
    (L : X →ₗ[ℝ] Y) (B : X →ₗ[ℝ] X →ₗ[ℝ] Y)
    (U : X) (F : Y)
    (hsource : F = abstractResidual L B U) :
    abstractCorrectionDefect L B U (-U) = 0 ∧
      F = abstractResidual L B U := by
  exact ⟨trivial_cancellation_solves_abstract_correction L B U, hsource⟩

/-- Algebraic last step of a terminal energy contradiction: if the exact
kinetic energy drops by at least a factor of two across a dyadic slab,
its asymptotic fifth-root profile cannot have the much slower drop. -/
theorem dyadic_energy_ratio_obstruction
    (M r : ℝ) (hM : 0 < M) (hr : r < 2)
    (henergy : M ≤ M * r / 2) : False := by
  have hgap : 0 < M * (2 - r) := mul_pos hM (sub_pos.mpr hr)
  nlinarith

/-- A strict relative norm bound rules out the trivial cancellation.
This alone never constructs an admissible correction. -/
theorem relative_norm_excludes_trivial_cancellation
    {Z : Type*} [NormedAddCommGroup Z] (U : Z) (δ : ℝ)
    (hU : U ≠ 0) (hδ : δ < 1) :
    ¬ ‖-U‖ ≤ δ * ‖U‖ := by
  intro h
  rw [norm_neg] at h
  have hpos : 0 < ‖U‖ := norm_pos_iff.mpr hU
  have hgap : 0 < (1 - δ) * ‖U‖ := mul_pos (sub_pos.mpr hδ) hpos
  nlinarith

#print axioms abstractCorrectionDefect_eq_totalResidual
#print axioms trivial_cancellation_solves_abstract_correction
#print axioms exact_source_match_does_not_forbid_cancellation
#print axioms dyadic_energy_ratio_obstruction
#print axioms relative_norm_excludes_trivial_cancellation

end
end UnforcedPatching
