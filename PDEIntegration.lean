import UnforcedClosure

/-!
# PDEIntegration

Staging file for the next formal verification phase.

The abstract unforced-closure layer is already kernel-checked.
This file will become the bridge to the frozen upstream Navier–Stokes
formalization once that repository is added as a pinned Lake dependency.

No full PDE-specific blow-up theorem is claimed here yet.
-/

namespace PDEIntegration

#check UnforcedClosure.fixedPoint_implies_zero_residual
#check UnforcedClosure.ball_invariance_scalar
#check UnforcedClosure.neumannPartial_preserves

end PDEIntegration
