import UnforcedPatching.PressureCompensatedFlux

/-!
Regression for the *continuum radial FTC* identity, with the pressure
boundary trace included. This is not an authentic H8 source construction.
-/

namespace UnforcedPatching

#check pressureCompensatedFluxIdentity
#check pressureCompensatedFluxConservativeDerivative
#check pressureCompensatedFluxZeroTrace
#check pressureCompensatedFluxSupportGate
#check pressureCompensatedFluxNonzeroTraceExample

#print axioms pressureCompensatedFluxIdentity
#print axioms pressureCompensatedFluxConservativeDerivative
#print axioms pressureCompensatedFluxZeroTrace
#print axioms pressureCompensatedFluxSupportGate
#print axioms pressureCompensatedFluxNonzeroTraceExample

end UnforcedPatching
