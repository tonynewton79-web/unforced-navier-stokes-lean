import UnforcedPatching.Periodicity

/-!
# Spatially constant pressure gauge

The incompressible Navier--Stokes equation is unchanged when pressure is
shifted by a function of time alone. This is an equality for the actual
upstream physical pressure gradient and residual, without a differentiability
assumption on the time-gauge function.
-/

namespace UnforcedPatching

open NavierStokes.ProblemStatement

/-- Every time-dependent spatially constant pressure shift has zero
effect on the physical spatial gradient. -/
theorem pressureGradient_timeGauge (p : PressureField) (c : ℝ → ℝ)
    (t : ℝ) (x : Space) :
    pressureGradient (fun z => p z + c z.1) t x = pressureGradient p t x := by
  unfold pressureGradient
  apply Finset.sum_congr rfl
  intro i _
  change (fderiv ℝ (fun y : Space => p (t, y) + c t) x)
      (coordinateVector i) • coordinateVector i = _
  rw [fderiv_add_const]

/-- Pressure-gauge freedom holds for the *complete* physical residual. -/
theorem navierStokesResidual_timeGauge (u : VelocityField) (p : PressureField)
    (c : ℝ → ℝ) (t : ℝ) (x : Space) :
    navierStokesResidual u (fun z => p z + c z.1) t x =
      navierStokesResidual u p t x := by
  unfold navierStokesResidual
  rw [pressureGradient_timeGauge p c t x]

end UnforcedPatching
