import Mathlib

/-!
# Exact scalar geometry used by the constructive majorant

The statements here verify the polynomial and parameter inequalities used
in the scalar majorant. They do not import the analytic coefficient
recurrence, prove the all-index convolution summation, or assert a PDE
solution. See the companion mathematical paper for those arguments.
-/
namespace TerminalCore2026

theorem pair_square_convolution (x y : ℝ) :
    (x+y)^2 ≤ 2*(x^2+y^2) := by
  nlinarith [sq_nonneg (x-y)]

theorem majorant_delay_ratios (n : ℝ) (hn : 3 ≤ n) :
    (n+1)^2 ≤ 2*n^2 ∧ (n+1)^2 ≤ 4*(n-1)^2 := by
  constructor
  · nlinarith [sq_nonneg (n-3)]
  · nlinarith [sq_nonneg (n-3)]

/-- The three sufficient scalar smallness budgets are each at most 1/4. -/
theorem majorant_budget
    (C0 C1 M R : ℝ)
    (hR : 0 < R)
    (hC0 : 0 ≤ C0)
    (hRfirst : 8*C0 ≤ R)
    (hRsecond : 16*C0 ≤ R^2)
    (hM : 16*C1*M ≤ 1) :
    2*C0/R + 4*C0/(R^2) + 4*C1*M ≤ (3:ℝ)/4 := by
  have hr2 : 0 < R^2 := sq_pos_of_pos hR
  have ha : 2*C0/R ≤ (1:ℝ)/4 :=
    (div_le_iff₀ hR).2 (by nlinarith [hRfirst])
  have hb : 4*C0/(R^2) ≤ (1:ℝ)/4 :=
    (div_le_iff₀ hr2).2 (by nlinarith [hRsecond])
  linarith

#print axioms pair_square_convolution
#print axioms majorant_delay_ratios
#print axioms majorant_budget

end TerminalCore2026
