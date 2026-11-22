import Mathlib

/-!
Attack 94 finite algebra only.  The complex-analytic multiplier bound
and B.26 continuum shear transfer are in the companion mathematical
note; Lean does not formalize those analytic assertions here.
-/
namespace UnforcedPatching.Attack94

theorem chi_complex_majorant :
    (1:ℚ) + 1 / ((9:ℚ)/10)^2 = 181/81 := by
  norm_num

theorem weighted_coefficient_constant :
    (181:ℚ)/81 * (9:ℚ)/4 = 181/36 := by
  norm_num

theorem source_multiplier_rational :
    ((40:ℚ)/3)^2 * ((181:ℚ)/36) = 72400/81 := by
  norm_num

theorem source_multiplier_lt_900 :
    (72400:ℚ)/81 < 900 := by
  norm_num

theorem zeta_coefficient_constant :
    (103:ℚ)/100 / ((9:ℚ)/10) * ((9:ℚ)/4) = 103/40 := by
  norm_num

theorem companion_shell_radius :
    ((61:ℚ)/10)/((16:ℚ)/25) = 305/32 := by
  norm_num

theorem source_shear_vs_case006 :
    (4:ℚ)/5 < 2 ∧ (4:ℚ)/5 < 10 := by
  norm_num

theorem rayleigh_discriminant_positive
    (a F : ℝ) (ha : a < 4/5) (hF : F ≠ 0) :
    2*F^2*(2-a) > (12/5)*F^2 := by
  have hF2 : 0 < F^2 := sq_pos_of_ne_zero hF
  have hA : 0 < (4/5-a) := by linarith
  have hProd : 0 < (4/5-a)*F^2 := mul_pos hA hF2
  nlinarith

#print axioms chi_complex_majorant
#print axioms weighted_coefficient_constant
#print axioms source_multiplier_rational
#print axioms source_multiplier_lt_900
#print axioms zeta_coefficient_constant
#print axioms companion_shell_radius
#print axioms source_shear_vs_case006
#print axioms rayleigh_discriminant_positive

end UnforcedPatching.Attack94
