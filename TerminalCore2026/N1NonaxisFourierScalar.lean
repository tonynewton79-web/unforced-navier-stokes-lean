import Mathlib

/-!
Edition XXIII: finite scalar mathematics behind m=+1/-1 selection,
quadratic Reynolds covariance, and radial torque constants. This does
NOT formalize cylindrical PDE, pressure, source matching or unforced blowup.
-/
namespace TerminalCore2026

theorem angular_plus_minus_zero : (1 : ℤ) + (-1) = 0 := by norm_num
theorem angular_plus_plus_two : (1 : ℤ) + 1 = 2 := by norm_num
theorem angular_minus_minus_minus_two : (-1 : ℤ) + (-1) = -2 := by norm_num

/-- A two-dimensional Gram minor is an exact square. -/
theorem nonaxis_mode_gram_minor (a b c d : ℝ) :
    (2 * (a ^ 2 + b ^ 2)) * (2 * (c ^ 2 + d ^ 2)) -
    (2 * (a * c + b * d)) ^ 2 =
      4 * (a * d - b * c) ^ 2 := by
  ring

theorem nonaxis_mode_gram_minor_nonneg (a b c d : ℝ) :
    0 ≤ (2 * (a ^ 2 + b ^ 2)) * (2 * (c ^ 2 + d ^ 2)) -
      (2 * (a * c + b * d)) ^ 2 := by
  rw [nonaxis_mode_gram_minor]
  positivity

theorem gaussian_slice_torque_algebra (lam c : ℝ) :
    (2 * lam * c) * ((2 : ℝ) * (1 / 8) - (1 / 8)) =
      lam * c / 4 := by
  ring

theorem m_two_curl_witness_components :
    ((-2 : ℤ) ^ 2 + (5 : ℤ) ^ 2) = 29 := by norm_num

#print axioms angular_plus_minus_zero
#print axioms angular_plus_plus_two
#print axioms angular_minus_minus_minus_two
#print axioms nonaxis_mode_gram_minor
#print axioms nonaxis_mode_gram_minor_nonneg
#print axioms gaussian_slice_torque_algebra
#print axioms m_two_curl_witness_components
end TerminalCore2026
