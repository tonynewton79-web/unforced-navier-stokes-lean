import UnforcedClosure
import NavierStokes

/-!
# PDEIntegration

First concrete bridge between the kernel-checked abstract unforced-closure layer
and the frozen upstream NavierStokesAndEuler development.

This file intentionally performs only an import/type-compatibility gate and
names concrete upstream PDE declarations that later bridge lemmas will use.
It does not yet assert the final unforced blow-up theorem.
-/

namespace PDEIntegration

-- Certified abstract closure layer.
#check UnforcedClosure.fixedPoint_implies_zero_residual
#check UnforcedClosure.ball_invariance_scalar
#check UnforcedClosure.neumannPartial_preserves

-- Concrete upstream Navier--Stokes PDE objects.
#check NavierStokes.ProblemStatement.VelocityField
#check NavierStokes.ProblemStatement.PressureField
#check NavierStokes.ProblemStatement.navierStokesResidual
#check NavierStokes.ProblemStatement.CandidateProperties
#check NavierStokes.ProblemStatement.SpeedUnboundedAtOne

-- Concrete upstream residual bridge from graph coordinates to the physical PDE.
#check NavierStokes.PhysicalResidualBridge.graphResidual
#check NavierStokes.PhysicalResidualBridge.graphResidual_eq_cylindrical

end PDEIntegration
