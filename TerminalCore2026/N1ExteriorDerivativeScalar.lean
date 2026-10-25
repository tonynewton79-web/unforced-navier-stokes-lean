import Mathlib

/-! Edition XVI: scalar positivity of the exact SOURCE heat exterior polynomial,
not the full gamma integral, Sobolev geometry or unforced NSE. -/
namespace TerminalCore2026

theorem exterior_heat_polynomial_strict
    (h a R : ℝ) (hh : 0 ≤ h) (ha : 0 ≤ a) (hr : 0 < R) :
    0 < 6 * a ^ 3 + (6 * h + 18) * a ^ 2 * R ^ 2 +
      (12 * h + 18) * a * R ^ 4 +
      ((1 + 2 * h) * (2 + 2 * h) * (3 + 2 * h)) * R ^ 6 := by
  have h1 : 0 < 1 + 2 * h := by linarith
  have h2 : 0 < 2 + 2 * h := by linarith
  have h3 : 0 < 3 + 2 * h := by linarith
  have hc2 : 0 ≤ 6 * h + 18 := by linarith
  have hc3 : 0 ≤ 12 * h + 18 := by linarith
  have ht1 : 0 ≤ 6 * a ^ 3 := by positivity
  have ht2 : 0 ≤ (6 * h + 18) * a ^ 2 * R ^ 2 := by positivity
  have ht3 : 0 ≤ (12 * h + 18) * a * R ^ 4 := by positivity
  have ht4 : 0 < ((1 + 2 * h) * (2 + 2 * h) * (3 + 2 * h)) * R ^ 6 := by
    positivity
  linarith

theorem exterior_source_exponent (h : ℝ) :
    ((1 / 2 : ℝ) + h) + 3 / 2 - (1 + (1 / 2 - h)) / 2 =
      5 / 4 + 3 * h / 2 := by
  ring

theorem exterior_picard_exponent (h : ℝ) :
    (1 / 2 : ℝ) - (5 / 4 + 3 * h / 2) =
      -(3 / 4 + 3 * h / 2) := by
  ring

theorem source_cubic_coefficient (h : ℝ) :
    (1 + 2 * h) * (2 + 2 * h) * (3 + 2 * h) =
      8 * h ^ 3 + 24 * h ^ 2 + 22 * h + 6 := by
  ring

theorem positive_source_H3_constant
    (m a b : ℝ) (hm : 0 < m) (ha : 0 ≤ a) (hab : a < b) :
    0 < m ^ 2 * (b ^ 2 - a ^ 2) := by
  have hleft : 0 < b - a := sub_pos.mpr hab
  have hright : 0 < b + a := by linarith
  have hprod := mul_pos hleft hright
  have hab2 : 0 < b ^ 2 - a ^ 2 := by nlinarith [hprod]
  positivity

#print axioms exterior_heat_polynomial_strict
#print axioms exterior_source_exponent
#print axioms exterior_picard_exponent
#print axioms source_cubic_coefficient
#print axioms positive_source_H3_constant
end TerminalCore2026
