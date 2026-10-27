import UnforcedPatching.SevenRayCenter

/-! Source-matched exact seven-ray covariance and rank-one projector test. -/

open UnforcedPatching

#check quarterRay
#check quarterRawWeight
#check rawQuarterCovariance
#check quarter_source_covariance_exact
#check quarter_raw_trace
#check quarter_raw_coefficients_scale_to_margin
#check quarter_physical_axial_efficiency
#check quarter_axial_efficiency_exceeds_companion

example (a b : Fin 3) :
    normalizedQuarterTraceFree a b = rationalQuarterProjector a b := by
  exact quarter_tracefree_rankOne a b

#print axioms UnforcedPatching.quarter_tracefree_rankOne
#print axioms UnforcedPatching.quarter_physical_axial_efficiency
