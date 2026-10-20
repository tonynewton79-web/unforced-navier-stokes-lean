import Mathlib

/-!
# Scalar proof gates for weighted radial convolution and two-lift smoothing

These statements formalize index and denominator comparisons from the
analytic convolution theorem in the cumulative manuscript. They do not
instantiate the entire Banach-space norm or the Navier--Stokes pressure source.
-/
namespace TerminalCore2026

theorem radial_convolution_quadratic_gate
    (a i : ℝ) (ha : 0 ≤ a) (hi : 0 ≤ i) (hii : i ≤ a) :
    (a+1)^2 ≤ 2*((i+1)^2+(a-i+1)^2) := by
  have hp : 0 ≤ (2*i-a)^2 := sq_nonneg _
  nlinarith

theorem two_lift_tame_index_gate
    (n a : ℝ) (hn : 1 ≤ n) (ha : n ≤ a) :
    2*(n+1) ≤ a+n+2 ∧ a+n+2 ≤ 2*(a+1) := by
  constructor <;> linarith

theorem radial_convolution_denominator_gate
    (a c : ℝ) (ha : 0 ≤ a) (hc : 0 ≤ c) :
    (a+1)^2*(a+2)^2 ≤ (a+c+1)^2*(a+c+2)^2 := by
  have hp1 : 0 ≤ c*(2*a+c+2) := mul_nonneg hc (by linarith)
  have hp2 : 0 ≤ c*(2*a+c+4) := mul_nonneg hc (by linarith)
  have h1 : (a+1)^2 ≤ (a+c+1)^2 := by nlinarith [hp1]
  have h2 : (a+2)^2 ≤ (a+c+2)^2 := by nlinarith [hp2]
  calc
    (a+1)^2*(a+2)^2 ≤ (a+c+1)^2*(a+2)^2 :=
      mul_le_mul_of_nonneg_right h1 (sq_nonneg _)
    _ ≤ (a+c+1)^2*(a+c+2)^2 :=
      mul_le_mul_of_nonneg_left h2 (sq_nonneg _)

theorem cubic_radial_multiplier_split (t c : ℝ) :
    (t+c)^3 = t^3+3*t^2*c+3*t*c^2+c^3 := by
  ring

#print axioms radial_convolution_quadratic_gate
#print axioms two_lift_tame_index_gate
#print axioms radial_convolution_denominator_gate
#print axioms cubic_radial_multiplier_split

end TerminalCore2026
