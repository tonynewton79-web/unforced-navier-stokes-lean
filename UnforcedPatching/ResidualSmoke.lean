import UnforcedPatching.Residual

/-!
Compile-only regression: addition of two smooth physical fields includes
**both** transport cross terms and no external forcing.
-/

open NavierStokes.ProblemStatement
open UnforcedPatching

#check ResidualRegularAt
#check navierStokesResidual_add

example (u v : VelocityField) (p q : PressureField) (t : ℝ) (x : Space)
    (hu : ResidualRegularAt u p t x)
    (hv : ResidualRegularAt v q t x) :
    navierStokesResidual (u + v) (p + q) t x =
      navierStokesResidual u p t x + navierStokesResidual v q t x +
        spatialDerivative u t x (v (t, x)) +
        spatialDerivative v t x (u (t, x)) := by
  exact navierStokesResidual_add u v p q t x hu hv

#print axioms UnforcedPatching.navierStokesResidual_add
#print axioms UnforcedPatching.spatialLaplacian_add
