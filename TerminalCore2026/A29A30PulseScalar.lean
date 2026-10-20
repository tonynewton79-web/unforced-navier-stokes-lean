import Mathlib

/-!
Finite scalar polynomial/rational gates for the exact source pulse
(A.29)--(A.30). No source integral, PDE or 1e-6 source-realization
claim is formalized here.
-/
namespace TerminalCore2026

theorem pulse_leading_ratio_polynomial (lam h c R : ℝ) :
    (lam-h+c)*((1-lam)-2*(1/2-lam))*R =
      (lam-h+c)*lam*R := by ring

theorem pulse_main_coefficient_polynomial (lam h c : ℝ) :
    (1/2-h+c)-(1/2-lam)=lam-h+c := by ring

theorem pulse_parameter_c_nonnegative (D eta : ℝ) (hD : 0 ≤ D) :
    0 ≤ 2*D*eta^2 := by positivity

theorem pulse_normalized_budget :
    ((12:ℚ)*(1/10^14)/(1/2-1/10^14)+
       3/10^7+1500/10^10)/(1-1/10^10) < 1/10^6 := by
  norm_num

theorem pulse_previous_bump_bound_insufficient :
    ((1280:ℚ)/3)*(20/9)*(1/400000)=8/3375 ∧
    (8:ℚ)/3375 > 1/10^7 := by
  constructor <;> norm_num

theorem pulse_curvature_small_parameter :
    (2131000:ℚ)*(1/10^14)/(9999/10000)<1/10^7 := by
  norm_num

#print axioms pulse_leading_ratio_polynomial
#print axioms pulse_normalized_budget
#print axioms pulse_previous_bump_bound_insufficient
#print axioms pulse_curvature_small_parameter

end TerminalCore2026
