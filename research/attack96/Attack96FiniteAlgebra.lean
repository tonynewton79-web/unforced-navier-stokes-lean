import Mathlib

/-!
Attack 96 finite algebra only. These declarations do not formalize the
analytic source, compact AA inverse, weighted cone PDE or NS blow-up.
-/
namespace UnforcedPatching.Attack96

theorem exact_cone_slack :
    (172:ℚ)/1229 - 1/100 = 15971/122900 := by
  norm_num

theorem half_reserve_floor :
    (172:ℚ)/1229 - (15971:ℚ)/245800 =
      1/100 + (15971:ℚ)/245800 := by
  norm_num

theorem manufactured_cost :
    (3:ℚ)/8 < 1/2 := by
  norm_num

theorem exact_positive_curl_pairing :
    (0:ℚ) < 2096/59657815174123018125 := by
  norm_num

theorem exact_dual_pairing_factor :
    2*((524:ℚ)/13233463425)*((2:ℚ)/4508102925) =
      2096/59657815174123018125 := by
  norm_num

theorem first_moment_numerator
    (m0 m1 m2 n0 n1 n2 : ℝ) :
    m0*(m1*n2-m2*n1)
    +m1*(m2*n0-n2*m0)
    +m2*(n1*m0-m1*n0) = 0 := by
  ring

theorem second_moment_numerator
    (m0 m1 m2 n0 n1 n2 : ℝ) :
    n0*(m1*n2-m2*n1)
    +n1*(m2*n0-n2*m0)
    +n2*(n1*m0-m1*n0) = 0 := by
  ring

theorem manufactured_components :
    8*((1:ℚ)/64) = 1/8 ∧
    2*((1:ℚ)/16)+4*((1:ℚ)/32)=1/4 ∧
    2*((1:ℚ)/8)+4*((1:ℚ)/32)=3/8 := by
  norm_num

#print axioms exact_cone_slack
#print axioms half_reserve_floor
#print axioms manufactured_cost
#print axioms exact_positive_curl_pairing
#print axioms exact_dual_pairing_factor
#print axioms first_moment_numerator
#print axioms second_moment_numerator
#print axioms manufactured_components

end UnforcedPatching.Attack96
