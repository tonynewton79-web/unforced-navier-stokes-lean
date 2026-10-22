import Mathlib

/-!
Scalar logical gates for the A.11 full-hull stress criterion.
The actual Appendix A source intervals, their soundness, Banach
operators and the UNFORCED PDE theorem are NOT proved here.
-/
namespace TerminalCore2026

theorem a11_terminal_residual_margin
    (lam b0 correction : ℝ)
    (h0 : b0 ≤ lam / 500)
    (h1 : correction < 249 * lam / 500) :
    b0 + correction < lam / 2 := by
  linarith

theorem a11_two_support_measure :
    (2 : ℚ) * (3/10) = 3/5 ∧
    (23/10 : ℚ) - 3/5 = 17/10 := by
  constructor <;> norm_num

theorem a11_source_local_fraction_margin :
    (2509510003 : ℚ) / 2497500000 < 201 / 200 := by
  norm_num

theorem a11_full_hull_cone_scalar_margin :
    2 * (3/4 : ℚ)^2 - (151/5000 : ℚ) * (111/9700 : ℚ)^2
      > 1124/1000 := by
  norm_num

#print axioms a11_terminal_residual_margin
#print axioms a11_two_support_measure
#print axioms a11_source_local_fraction_margin
#print axioms a11_full_hull_cone_scalar_margin

end TerminalCore2026