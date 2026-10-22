import Mathlib

/-! Scalar rational gates for the A.11 two-support improvement.
This does NOT formalize future integrals, terminal gauges, or NS. -/
namespace TerminalCore2026

theorem a11_two_supports_total_length :
    (2:ℚ)*(3/10) = 3/5 ∧ (23:ℚ)/10-3/5=17/10 := by
  constructor <;> norm_num

theorem a11_support_measure_exact_factor :
    ((2:ℚ)*(1001/1000)^2*(2503/5000)
      +(3/5)*(1001/1000)*(1/1000))/(999/1000)
      = 2509510003/2497500000 := by
  norm_num

theorem a11_support_measure_margin :
    (2509510003:ℚ)/2497500000 < 201/200 := by
  norm_num

theorem a11_support_measure_vs_hull :
    ((23:ℚ)/10 - 3/5)*(1001/1000)*(1/1000) > 0 := by
  norm_num

theorem a11_full_hull_scalar_gate (lam s : ℝ)
    (hlam : 0 < lam)
    (hs : s ≤ lam * ((2509510003:ℝ)/2497500000)/1000) :
    s < lam/2 := by
  have hc : ((2509510003:ℝ)/2497500000)/1000 < 1/2 := by
    norm_num
  have hd : lam * ((2509510003:ℝ)/2497500000)/1000
      < lam/2 := by
    have hp : 0 < lam * (1/2-((2509510003:ℝ)/2497500000)/1000) :=
      mul_pos hlam (by linarith)
    nlinarith
  exact lt_of_le_of_lt hs hd

#print axioms a11_two_supports_total_length
#print axioms a11_support_measure_exact_factor
#print axioms a11_support_measure_margin
#print axioms a11_full_hull_scalar_gate
end TerminalCore2026
