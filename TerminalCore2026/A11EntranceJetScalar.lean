import Mathlib

/-! A.10--A.11 source entrance moment and true two-bump arithmetic gates.
    Analytic source integrals, interval soundness, and unforced PDE are
    NOT formalized or assumed solved here. -/
namespace TerminalCore2026

theorem A11_entrance_moment_error_margin :
    (40/17:ℚ) * 5 + (20/19:ℚ) * 5 < 18 := by norm_num
theorem A11_entrance_eta_jet_margin :
    (40/17:ℚ) * 5 < 12 := by norm_num
theorem A11_first_column_inverse_bound :
    (1:ℚ) / ((4/5:ℚ) * (6-(1/7:ℚ))) = 35/164 := by norm_num
theorem A11_correction_small_branch_budget :
    2 * (3/2:ℚ) * 18 = 54 := by norm_num
theorem A11_jacobian_smallness_gate :
    (3/2:ℚ) * 640 * 54 / (20:ℚ)^28 < 1/2 := by norm_num
theorem A11_contraction_smallness_gate :
    8*(3/2:ℚ)^2*320*18/(20:ℚ)^28 < 1 := by norm_num
theorem A11_correction_eta_margin :
    2*(35/164:ℚ)*12 < 6 := by norm_num
theorem A11_stronger_implies_prior_gates :
    (18:ℚ) ≤ 80 ∧ (12:ℚ) ≤ 80 ∧
    (54:ℚ) ≤ 192 ∧ (6:ℚ) ≤ 12 := by norm_num

#print axioms A11_entrance_moment_error_margin
#print axioms A11_entrance_eta_jet_margin
#print axioms A11_first_column_inverse_bound
#print axioms A11_correction_small_branch_budget
#print axioms A11_jacobian_smallness_gate
#print axioms A11_correction_eta_margin
end TerminalCore2026