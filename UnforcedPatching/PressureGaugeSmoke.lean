import UnforcedPatching.PressureGauge

/-! Spacetime pressure-gauge regression: c(t) cannot affect ∇p or R(u,p). -/

open NavierStokes.ProblemStatement
open UnforcedPatching

example (u : VelocityField) (p : PressureField)
    (c : ℝ → ℝ) (t : ℝ) (x : Space) :
    navierStokesResidual u (fun z => p z + c z.1) t x =
      navierStokesResidual u p t x := by
  exact navierStokesResidual_timeGauge u p c t x

#print axioms UnforcedPatching.navierStokesResidual_timeGauge
