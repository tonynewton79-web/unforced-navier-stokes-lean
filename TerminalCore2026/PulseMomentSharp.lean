import Mathlib

/-! Arithmetic gates for Appendix A's fixed pulse shape and moment matrix.
    Does NOT formalize its smooth-step integrals or the full source profile. -/
namespace TerminalCore2026
theorem pulse_baseline :
    (1/4 : ℚ) - (1/100)/2 + (1/100)^2/2 = 4901/20000 := by norm_num
theorem pulse_tail_factor :
    ((10 - (1/100:ℚ))^2)/2 + (10 - 1/100)/2 + 1/4 =
    1102901/20000 := by norm_num
theorem pulse_safe_integral_lower :
    (1225239:ℚ)/5000000 <
    4901/20000 - 1/500000 - (1102901/20000)/470000000 := by norm_num
theorem amplitude_left_margin :
    (1009/1000:ℚ)^2 * (61263/250000) -
      (1 - 1/100000000000)/4 < -(1/2500) := by norm_num
theorem amplitude_right_margin :
    (1011/1000:ℚ)^2 * (1225239/5000000) - 1/4 >
      (1/2500) := by norm_num
theorem amplitude_derivative_margin :
    2*(1009/1000:ℚ)*(1225239/5000000) - 1/100 > 48/100 := by norm_num
theorem principal_amplitude_lower_margin :
    (1010045/1000000:ℚ)^2 * (61263/250000) -
      (1 - 1/100000000000)/4 < 0 := by norm_num
theorem principal_amplitude_upper_margin :
    (1010055/1000000:ℚ)^2 * (1225239/5000000) - 1/4 > 0 := by norm_num
theorem moment_matrix_determinant_factor :
    4*(37/40:ℚ)^2 = 1369/400 := by norm_num
theorem moment_matrix_inverse_factor :
    (13/2:ℚ)/(1369/400) < 2 := by norm_num
#print axioms pulse_baseline
#print axioms pulse_safe_integral_lower
#print axioms amplitude_left_margin
#print axioms amplitude_right_margin
#print axioms amplitude_derivative_margin
#print axioms moment_matrix_inverse_factor
end TerminalCore2026