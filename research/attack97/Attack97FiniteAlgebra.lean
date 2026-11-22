import Mathlib

/-!
Attack 97: exact finite rational checks only. The original continuum Case006
source has NOT been frozen, and no full H8 inverse or NS theorem is proved.
-/
namespace UnforcedPatching.Attack97

theorem source_alpha_as_coefficient :
    -(4443:ℚ)/9832 = -((4443:ℚ)/4916)/2 := by
  norm_num

theorem scalar_lower_endpoint :
    -(1:ℚ)/2 - ((15971:ℚ)/122900)/((4443:ℚ)/4916)
     = -(143017:ℚ)/222150 := by
  norm_num

theorem scalar_upper_endpoint :
    -(1:ℚ)/2 + ((15971:ℚ)/122900)/((4443:ℚ)/4916)
     = -(79133:ℚ)/222150 := by
  norm_num

theorem angular_fixed_zero_lower :
    -(1:ℚ)/2 - ((15971:ℚ)/122900)/(2*((4443:ℚ)/4916))
      = -(63523:ℚ)/111075 := by
  norm_num

theorem required_positive_asymmetry_remainder :
    (4443:ℚ)/4916 - (15971:ℚ)/122900
      = (23776:ℚ)/30725 := by
  norm_num

theorem opposite_profile_fails_scalar :
    (15971:ℚ)/122900 < (4443:ℚ)/4916 := by
  norm_num

theorem source_axial_positive_forbidden :
    -(4443:ℚ)/9832 + (15971:ℚ)/122900 < 0 := by
  norm_num

theorem scalar_normalized_violation_factor :
    ((4443:ℚ)/4916)/((15971:ℚ)/122900)
      = (111075:ℚ)/15971 := by
  norm_num

#print axioms source_alpha_as_coefficient
#print axioms scalar_lower_endpoint
#print axioms scalar_upper_endpoint
#print axioms angular_fixed_zero_lower
#print axioms required_positive_asymmetry_remainder
#print axioms opposite_profile_fails_scalar
#print axioms source_axial_positive_forbidden
#print axioms scalar_normalized_violation_factor

end UnforcedPatching.Attack97
