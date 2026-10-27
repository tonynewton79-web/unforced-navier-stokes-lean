import UnforcedPatching.MeridionalInverse

/-! Kernel smoke test for the actual axial antiderivative and pointwise
radial/axial meridional divergence equations. A missing theorem or a
type-mismatched identity must break this module's compilation. -/

#check UnforcedPatching.axialPrimitive_partialAxial
#check UnforcedPatching.meridional_correction_divergence
#check UnforcedPatching.radialMoment_relation
#check UnforcedPatching.mixedCarrier_radial_balance
#check UnforcedPatching.sourceMatched_axialStress

#print axioms UnforcedPatching.axialPrimitive_partialAxial
#print axioms UnforcedPatching.meridional_correction_divergence
#print axioms UnforcedPatching.radialMoment_relation
#print axioms UnforcedPatching.mixedCarrier_radial_balance
#print axioms UnforcedPatching.sourceMatched_axialStress
