import UnforcedPatching.Residual

/-!
# Preservation of physical torus constraints under addition

These elementary steps are required when a background field is combined with
a patch or correction. They do not prove a compactly supported patch exists.
-/

namespace UnforcedPatching

open NavierStokes.ProblemStatement

/-- The sum of two fields with the same unit periods retains those periods. -/
theorem unitSpatialPeriodsOn_add {V : Type*} [Add V] {times : Set ℝ}
    {f g : SpaceTime → V}
    (hf : UnitSpatialPeriodsOn times f)
    (hg : UnitSpatialPeriodsOn times g) :
    UnitSpatialPeriodsOn times (f + g) := by
  intro t ht x i
  change f (t, x + coordinateVector i) + g (t, x + coordinateVector i) =
    f (t, x) + g (t, x)
  rw [hf t ht x i, hg t ht x i]

/-- At a point of spatial differentiability, divergence is additive. -/
theorem spatialDivergence_add (u v : VelocityField) (t : ℝ) (x : Space)
    (hu : DifferentiableAt ℝ (fun y : Space => u (t, y)) x)
    (hv : DifferentiableAt ℝ (fun y : Space => v (t, y)) x) :
    spatialDivergence (u + v) t x =
      spatialDivergence u t x + spatialDivergence v t x := by
  unfold spatialDivergence
  rw [← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro i _
  rw [spatialDerivative_add u v t x hu hv, add_apply]
  rfl

/-- Two differentiable divergence-free fields have a divergence-free sum. -/
theorem divergence_free_add (u v : VelocityField) (t : ℝ) (x : Space)
    (hu : DifferentiableAt ℝ (fun y : Space => u (t, y)) x)
    (hv : DifferentiableAt ℝ (fun y : Space => v (t, y)) x)
    (hdu : spatialDivergence u t x = 0)
    (hdv : spatialDivergence v t x = 0) :
    spatialDivergence (u + v) t x = 0 := by
  rw [spatialDivergence_add u v t x hu hv, hdu, hdv, add_zero]

end UnforcedPatching
