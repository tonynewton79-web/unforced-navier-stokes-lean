import Mathlib

/-!
# Finite scalar gates for the fixed-radius Volterra inverse

The analytic operator-norm and full Navier–Stokes coefficient theorem
are in the accompanying paper, not formalized end-to-end here.
-/
namespace TerminalCore2026

theorem similarity_order_under_valuation (n m : ℝ)
    (hn : 0 ≤ n) (hm : n ≤ m) : n ≤ m + 1 := by
  linarith

theorem iterated_radial_valuation (n ell : ℕ) : n ≤ n + ell := by
  omega

theorem first_delay_ratio (n : ℝ) (hn : 3 ≤ n) :
    (n+1)^2 ≤ 2*n^2 := by
  have h : 0 ≤ (n-3)*(n+3) :=
    mul_nonneg (by linarith) (by linarith)
  nlinarith [sq_nonneg (n-3)]

theorem second_delay_ratio (n : ℝ) (hn : 3 ≤ n) :
    (n+1)^2 ≤ 4*(n-1)^2 := by
  have h : 0 ≤ (n-3)*(3*n-1) :=
    mul_nonneg (by linarith) (by linarith)
  nlinarith

theorem fixed_order_parameter_compensation (n m h : ℝ)
    (hn : 0 ≤ n) (h_nm : n ≤ m) (hh : 0 ≤ h) :
    2*h*n ≤ 2*h*(m+1) := by
  have hd : 0 ≤ m+1-n := by linarith
  have hp : 0 ≤ 2*h*(m+1-n) := mul_nonneg (by positivity) hd
  nlinarith

#print axioms similarity_order_under_valuation
#print axioms iterated_radial_valuation
#print axioms first_delay_ratio
#print axioms second_delay_ratio
#print axioms fixed_order_parameter_compensation

end TerminalCore2026
