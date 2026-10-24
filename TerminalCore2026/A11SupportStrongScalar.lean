import Mathlib

/-!
# The two A.11 supports: finite scalar cone margin gates

The analytic source integrals, moment-correction contraction,
global exterior stress inequalities and unforced Navier-Stokes
Theorem 1.1 are NOT Lean formalized here.
-/
namespace TerminalCore2026

theorem a11_new_matrix_separation (x z : ℝ)
    (hx : 6 ≤ x) (hz : z ≤ 1 / 4) :
    (23 / 4 : ℝ) ≤ x - z := by
  linarith

theorem a11_new_fixed_point_small :
    (8 / 23 : ℚ) + 743 / 1000000 < 1 ∧
    1485 / 1000000 < 1 / 100 := by
  constructor <;> norm_num

theorem a11_new_true_bump_derivative_budget :
    (640 / 3 : ℚ) * 50 / 20^28 < 1 / 1000 ∧
    (250000 : ℚ) * 50 / 20^27 < 1 / 4 ∧
    (640 / 3 : ℚ) * 3 / 100000 < 1 / 100 := by
  constructor
  · norm_num
  constructor <;> norm_num

theorem a11_new_stress_coefficient_margin :
    4 * (1 / 100 : ℚ) * 3 +
      (1 + 2 * (1 / 100 : ℚ)) + 3 * (1 / 100 : ℚ) < 2 := by
  norm_num

theorem a11_new_energy_to_cone
    (lam e : ℝ) (hl : 0 < lam) (he : e ≤ lam / 25) :
    2 * e < lam / 2 := by
  linarith

theorem a11_new_support_gap :
    (2 : ℚ) + 2 * (3 / 20 : ℚ) < 3 := by
  norm_num

theorem a11_new_sigma_second_derivative_budget :
    (256^2 + 3072 : ℚ) / 4 < 20000 ∧
    (100 / 9 : ℚ) * 20000 < 250000 := by
  constructor <;> norm_num

#print axioms a11_new_matrix_separation
#print axioms a11_new_fixed_point_small
#print axioms a11_new_true_bump_derivative_budget
#print axioms a11_new_stress_coefficient_margin
#print axioms a11_new_energy_to_cone
end TerminalCore2026
