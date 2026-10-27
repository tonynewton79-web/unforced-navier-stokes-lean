import UnforcedPatching.PressureGauge

/-!
# Exact physical correction obligation

A background velocity-pressure pair and a correction pair solve the *unforced*
PDE together if the correction cancels the full physical residual. This is
a conditional closure theorem, not a construction of the correction or a
global existence/singularity result.
-/

namespace UnforcedPatching

open NavierStokes.ProblemStatement

/-- The actual nonlinear physical equation a correction must solve at a
point. `navierStokesResidual w π` includes the correction's *self-advection*
and viscous Laplacian; the remaining terms are both background cross terms. -/
def PhysicalCorrectionEquation (u : VelocityField) (p : PressureField)
    (w : VelocityField) (π : PressureField) (t : ℝ) (x : Space) : Prop :=
  navierStokesResidual w π t x + spatialDerivative u t x (w (t, x)) +
    spatialDerivative w t x (u (t, x)) = -navierStokesResidual u p t x

/-- Pointwise cancellation of the **complete** correction equation implies
the full unforced PDE for the sum, under the physical regularity hypotheses. -/
theorem physicalCorrection_closes (u w : VelocityField) (p π : PressureField)
    (t : ℝ) (x : Space)
    (hu : ResidualRegularAt u p t x)
    (hw : ResidualRegularAt w π t x)
    (hc : PhysicalCorrectionEquation u p w π t x) :
    navierStokesResidual (u + w) (p + π) t x = 0 := by
  rw [navierStokesResidual_add u w p π t x hu hw]
  unfold PhysicalCorrectionEquation at hc
  calc
    navierStokesResidual u p t x + navierStokesResidual w π t x +
        spatialDerivative u t x (w (t, x)) +
        spatialDerivative w t x (u (t, x)) =
      navierStokesResidual u p t x +
        (navierStokesResidual w π t x +
          spatialDerivative u t x (w (t, x)) +
          spatialDerivative w t x (u (t, x))) := by abel
    _ = navierStokesResidual u p t x + -navierStokesResidual u p t x := by rw [hc]
    _ = 0 := add_neg_cancel _

end UnforcedPatching
