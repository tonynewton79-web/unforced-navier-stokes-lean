import UnforcedPatching.FrameConnectionDerivative

/-! Smoke test: missing or sign-reversed frame-connection theorems
must fail Lean elaboration/kernel verification. -/

open UnforcedPatching

#check rotateStress_eq_matrixProduct
#check frameRotationEntry_hasDerivAt
#check frameOmega_skew
#check frameVelocity_eq_frameOmega
#check frameDifferential_commutator
#check rotatingFrameStress_hasDerivAt
#check rotatingFrame_constantFrame
#check frameConnection_nontrivial_example
#check planarRotation_example_hasDerivAt

#print axioms rotateStress_eq_matrixProduct
#print axioms frameRotationEntry_hasDerivAt
#print axioms frameOmega_skew
#print axioms frameVelocity_eq_frameOmega
#print axioms frameDifferential_commutator
#print axioms rotatingFrameStress_hasDerivAt
#print axioms rotatingFrame_constantFrame
#print axioms frameConnection_nontrivial_example
#print axioms planarRotation_example_hasDerivAt
