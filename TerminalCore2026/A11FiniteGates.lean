import Mathlib

/-! Finite scalar gates for the exact Appendix A.11 angular two-bump
correction. Full smooth-step integrals, source parameter selection and
unforced Navier--Stokes PDE are not Lean-formalized here. -/
namespace TerminalCore2026
theorem A11_inverse_first_row : (3625 : ℚ)/2624 < 3/2 := by norm_num
theorem A11_inverse_second_row : (2625 : ℚ)/5248 < 3/2 := by norm_num
theorem A11_quadratic_norm : (6400 : ℚ)/21 < 320 := by norm_num
theorem A11_contraction_max_lambda :
    (8 : ℚ)*(3/2)^2*320*64*(1/20)^28 < 1 := by norm_num
theorem A11_perturbation_positive :
    (640 : ℚ)/3*192*(1/20)^28 < 1/2 := by norm_num
theorem A11_derivative_gain :
    (76800000 : ℚ)*(1/20)^27 < 1/2 := by norm_num
theorem A11_Tf_interpolation :
    (7 : ℚ)/10 * 64 / 512 = 7/80 := by norm_num
theorem A11_terminal_cutoff :
    ((1 : ℚ)/256)*32/(1-((1 : ℚ)/256)*(1/100)) < 1/4 := by norm_num
#print axioms A11_inverse_first_row
#print axioms A11_quadratic_norm
#print axioms A11_contraction_max_lambda
#print axioms A11_derivative_gain
end TerminalCore2026
