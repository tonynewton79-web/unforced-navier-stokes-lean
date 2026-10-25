import Mathlib

/-!
Edition XLI. Limited finite scalar algebra only. The actual PDE
radial-variation and Fourier covariance theorems are NOT Lean-formalized.
-/
namespace TerminalCore2026

theorem xli_product_energy_bound (a b c : ℝ) :
    2 * |a*b| ≤ a^2+b^2+c^2 := by
  have h1 : 2*a*b ≤ a^2+b^2 := by nlinarith [sq_nonneg (a-b)]
  have h2 : -(2*a*b) ≤ a^2+b^2 := by nlinarith [sq_nonneg (a+b)]
  rcases le_total 0 (a*b) with h | h
  · rw [abs_of_nonneg h]
    nlinarith [sq_nonneg c]
  · rw [abs_of_nonpos h]
    nlinarith [sq_nonneg c]

theorem xli_axis_quadratic_torque (j3 k2z lam : ℝ)
    (h : lam = -4*j3-k2z) : lam+4*j3+k2z=0 := by
  linarith

theorem xli_axis_scaling (X tau lam : ℝ) :
    (2*X*tau)*lam = 2*X*tau*lam := by ring

theorem xli_spike_budget (amp duration width budget : ℝ)
    (h : amp*duration*width ≤ budget) :
    amp*duration*width ≤ budget := h

theorem xli_exponent_threshold :
    (3/2:ℚ)-(5/6) = 2/3 := by norm_num

#print axioms xli_product_energy_bound
#print axioms xli_axis_quadratic_torque
#print axioms xli_axis_scaling
#print axioms xli_spike_budget
#print axioms xli_exponent_threshold
end TerminalCore2026
