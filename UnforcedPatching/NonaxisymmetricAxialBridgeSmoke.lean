import UnforcedPatching.NonaxisymmetricAxialBridge

/-! Smoke check: the pointwise angular stress contribution is retained. -/

namespace UnforcedPatching

#check cartesianGeneralAxialDivergence
#check cartesianGeneralAxialPressureBalance
#check cartesianNonzeroAngularGradientExample

#print axioms cartesianGeneralAxialDivergence
#print axioms cartesianGeneralAxialPressureBalance
#print axioms cartesianNonzeroAngularGradientExample

end UnforcedPatching
