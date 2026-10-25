import UnforcedPatching.Correction

/-!
The future patch must solve a *physical* correction equation before the
zero-residual theorem can be used. No correction witness is assumed to exist.
-/

open NavierStokes.ProblemStatement
open UnforcedPatching

example (u w : VelocityField) (p π : PressureField) (t : ℝ) (x : Space)
    (hu : ResidualRegularAt u p t x)
    (hw : ResidualRegularAt w π t x)
    (hc : PhysicalCorrectionEquation u p w π t x) :
    navierStokesResidual (u + w) (p + π) t x = 0 := by
  exact physicalCorrection_closes u w p π t x hu hw hc

#print axioms UnforcedPatching.physicalCorrection_closes
