import Mathlib

/-! Finite scalar consequences of the source Appendix B axis third jet.
No full PDE or analytic-profile formalization is claimed. -/
namespace TerminalCore2026
theorem axis_source_W0 : (1 : ℝ)-4 = -3 := by norm_num
theorem axis_jet_algebra (Λ χ h C : ℝ) (hΛ : Λ ≠ 0) (hC : C ≠ 0) :
    3*Λ*((-χ+(-3+h)/Λ)/4)/C =
      -(3/(4*C))*(Λ*χ+3-h) := by
  field_simp [hΛ,hC]
  ring
theorem axis_jet_strict (Λ χ h C : ℝ)
    (hΛ : 0 < Λ) (hχ : 0 ≤ χ) (hh : h ≤ 1/100) (hC : 0 < C) :
    -(3/(4*C))*(Λ*χ+3-h) < 0 := by
  have hp : 0 ≤ Λ*χ := mul_nonneg (le_of_lt hΛ) hχ
  have hs : 0 < Λ*χ+3-h := by linarith
  have hc : 0 < 3/(4*C) := by positivity
  nlinarith [mul_pos hc hs]
theorem axis_jet_coefficient_lower (Λ χ h : ℝ)
    (hΛ : 0 < Λ) (hχ : 0 ≤ χ) (hh : h ≤ 1/100) :
    (897/400 : ℝ) ≤ (3/4)*(Λ*χ+3-h) := by
  have hp : 0 ≤ Λ*χ := mul_nonneg (le_of_lt hΛ) hχ
  nlinarith
#print axioms axis_source_W0
#print axioms axis_jet_algebra
#print axioms axis_jet_strict
#print axioms axis_jet_coefficient_lower
end TerminalCore2026