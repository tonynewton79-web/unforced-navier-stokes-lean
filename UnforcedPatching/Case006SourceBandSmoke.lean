import UnforcedPatching.Case006SourceBand

/-!
Regression of the Case 006 source-native *necessary* interval.
The claims are finite dimensional and are not a construction of a PDE stress.
-/

namespace UnforcedPatching

#check original_absolute_cone_shear
#check case006_conditional_axial_band
#check case006_weighted_finite_slice_band
#check case006_positive_witness
#check case006_positive_not_original_budget
#check case006_absolute_upper_sharp
#check case006_absolute_lower_sharp

example :
    ∀ i : Fin 7,
      sevenRayCenter i +
        sevenRayCorrection case006WitnessA case006WitnessB
          case006WitnessC case006WitnessD i ≥ (1 / 100 : ℝ) :=
  case006_positive_witness

example : ¬ ∀ i : Fin 7,
    |sevenRayCorrection case006WitnessA case006WitnessB
      case006WitnessC case006WitnessD i| ≤ h8CoefficientBudget :=
  case006_positive_not_original_budget

#print axioms original_absolute_cone_shear
#print axioms case006_conditional_axial_band
#print axioms case006_weighted_finite_slice_band
#print axioms case006_positive_witness
#print axioms case006_positive_not_original_budget
#print axioms case006_absolute_upper_sharp
#print axioms case006_absolute_lower_sharp

end UnforcedPatching
