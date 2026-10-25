import Mathlib
/-!
Scalar algebra for the A.11 local-normalization derivative cancellation.
This module does not formalize tail integration, true c_i coefficients,
interval inclusion, Navier--Stokes, or an unforced singularity.
-/
namespace TerminalCore2026

theorem a11_local_normalizer_derivative_cancel
    (v dv ad ap dad dap : ℝ) (hv : v ≠ 0) :
    2 * (dv / v) * (ad / (2*v^2) - ap / (2*v^2)) +
    (dad / (2*v^2) - ad*dv / v^3) -
    (dap / (2*v^2) - ap*dv / v^3) =
    (dad-dap) / (2*v^2) := by
  field_simp
  ring

theorem a11_local_new_slack :
    (1/2:ℚ) - 63/250 = 31/125 := by norm_num

theorem a11_local_new_cone :
    (1/2:ℚ) - (3/20)*(63/125)^2 = 144343/312500 := by
  norm_num

theorem a11_local_cone_margin :
    (9/20:ℚ) < 144343/312500 := by norm_num

theorem a11_local_tail_budget :
    (1/200:ℚ) + 1002/1000 + 1/1000 = 1008/1000 := by
  norm_num

#print axioms a11_local_normalizer_derivative_cancel
#print axioms a11_local_new_slack
#print axioms a11_local_new_cone
#print axioms a11_local_cone_margin
end TerminalCore2026