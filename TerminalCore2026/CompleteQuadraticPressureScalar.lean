import Mathlib

/-!
# Scalar gates for complete mixed quadratic pressure smoothing

These statements certify polynomial/index comparisons in the seven H and
eight Q channels. They do not formalize the full Banach-space norm or
the Navier--Stokes equation. DOI 10.5281/zenodo.23474915.
-/
namespace TerminalCore2026

theorem quadratic_mixed_shift_bound (N k : ℝ)
    (hN : 0 ≤ N) (hk : 0 ≤ k) (hkn : k ≤ N) :
    N+1 ≤ N+k+2 ∧ N+k+2 ≤ 2*(N+1) := by
  constructor <;> linarith

theorem quadratic_double_radial_average (a b : ℝ)
    (ha : 0 ≤ a) (hb : 0 ≤ b) :
    a+b+1 ≤ (a+1)*(b+1) := by
  nlinarith [mul_nonneg ha hb]

theorem quadratic_mixed_theta_domination (a b k : ℝ)
    (ha : 0 ≤ a) (hb : 0 ≤ b) (hk : 0 ≤ k)
    (hkn : k ≤ a+b) :
    a+b+k+2 ≤ 2*(a+1)*(b+1) := by
  nlinarith [mul_nonneg ha hb]

theorem quadratic_H_third_jet (r m N u G : ℝ)
    (hr : r ≠ 0) (hm : m ≠ 0) (hN : N ≠ 0) :
    -(G*(u*(-G^2/r)))/(4*m*N^2) = u*G^3/(4*r*m*N^2) := by
  field_simp
  ring

theorem complete_bilinear_multiplier_budgets :
    11*(64:ℕ)^2*25^3 = 704000000 ∧
    32*(64:ℕ)^2*25^3 = 2048000000 := by
  constructor <;> norm_num

#print axioms quadratic_mixed_shift_bound
#print axioms quadratic_double_radial_average
#print axioms quadratic_mixed_theta_domination
#print axioms quadratic_H_third_jet
#print axioms complete_bilinear_multiplier_budgets

end TerminalCore2026
