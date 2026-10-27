import UnforcedPatching.CompactGauge

/-!
Actual one-dimensional differentiation smoke test for the radial-axial
pressure-gauge compatibility identity. Whole-space cylindrical divergence,
compact support, and the weighted H8 inverse are separate obligations.
-/

namespace UnforcedPatching

example (F Fr : ℝ → ℝ) (r a : ℝ) (hr : r ≠ 0)
    (hF : HasDerivAt F (Fr r) r)
    (hFr : HasDerivAt Fr a r) :
    deriv (axialCarrier F Fr) r =
      deriv (radialCarrier F Fr) r + radialCarrier F Fr r / r := by
  exact radial_axial_carrier_derivative F Fr r a hr hF hFr

end UnforcedPatching

#print axioms UnforcedPatching.radial_axial_carrier_derivative
