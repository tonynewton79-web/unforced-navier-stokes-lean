import UnforcedPatching.Periodicity

/-! Independent compile-time tests for torus gluing semantics. -/

open NavierStokes.ProblemStatement
open UnforcedPatching

example {V : Type*} [Add V] {times : Set ℝ} {f g : SpaceTime → V}
    (hf : UnitSpatialPeriodsOn times f)
    (hg : UnitSpatialPeriodsOn times g) :
    UnitSpatialPeriodsOn times (f + g) :=
  unitSpatialPeriodsOn_add hf hg

example (u v : VelocityField) (t : ℝ) (x : Space)
    (hu : DifferentiableAt ℝ (fun y : Space => u (t, y)) x)
    (hv : DifferentiableAt ℝ (fun y : Space => v (t, y)) x)
    (hdu : spatialDivergence u t x = 0)
    (hdv : spatialDivergence v t x = 0) :
    spatialDivergence (u + v) t x = 0 :=
  divergence_free_add u v t x hu hv hdu hdv

#print axioms UnforcedPatching.unitSpatialPeriodsOn_add
#print axioms UnforcedPatching.divergence_free_add
