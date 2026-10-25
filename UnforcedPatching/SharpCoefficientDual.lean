import UnforcedPatching.ExactCoefficientCone
import Mathlib.Tactic

/-!
# A sharp candidate upper support bound for the original H8 coefficient cone

All statements are finite-dimensional, pointwise facts about the **original**
seven absolute coefficient budgets. They do not assume a PDE inverse exists.
-/

noncomputable section

namespace UnforcedPatching

/-- A source-independent bound for the dual pairing with the genuine
four-coordinate seven-ray coefficient set. Independent exact rational
extremizers (in the companion Python test) show the constant is sharp. -/
theorem original_cone_dual_upper (A B C D τ a b c d : ℝ)
    (hcone : ∀ i : Fin 7, |sevenRayCorrection A B C D i| ≤ τ) :
    A*a + B*b + C*c + D*d ≤
      τ * (max ((|a|+|c|)/2) (|d|/4) + |4*a+b|/8) := by
  obtain ⟨hCD, hAB, hB⟩ := (original_seven_coefficient_cone_exact A B C D τ).mp hcone
  have hτ : 0 ≤ τ := by nlinarith [abs_nonneg B]
  have hD : |D| ≤ τ / 4 := by nlinarith [abs_nonneg C]
  have hX : |A-4*B| ≤ τ / 2 - 2 * |D| := by nlinarith
  have hC : |C| ≤ τ / 2 - 2 * |D| := by nlinarith
  have hB' : |B| ≤ τ / 8 := by nlinarith
  have hxprod : |A-4*B| * |a| ≤ (τ/2-2*|D|) * |a| :=
    mul_le_mul_of_nonneg_right hX (abs_nonneg a)
  have hcprod : |C| * |c| ≤ (τ/2-2*|D|) * |c| :=
    mul_le_mul_of_nonneg_right hC (abs_nonneg c)
  have hbprod : |B| * |4*a+b| ≤ τ/8 * |4*a+b| :=
    mul_le_mul_of_nonneg_right hB' (abs_nonneg (4*a+b))
  have hl1 : (A-4*B)*a ≤ |A-4*B| * |a| := by
    calc (A-4*B)*a ≤ |(A-4*B)*a| := le_abs_self _
      _ = |A-4*B| * |a| := abs_mul _ _
  have hl2 : B*(4*a+b) ≤ |B| * |4*a+b| := by
    calc B*(4*a+b) ≤ |B*(4*a+b)| := le_abs_self _
      _ = |B| * |4*a+b| := abs_mul _ _
  have hl3 : C*c ≤ |C| * |c| := by
    calc C*c ≤ |C*c| := le_abs_self _
      _ = |C| * |c| := abs_mul _ _
  have hl4 : D*d ≤ |D| * |d| := by
    calc D*d ≤ |D*d| := le_abs_self _
      _ = |D| * |d| := abs_mul _ _
  have hbase :
      A*a + B*b + C*c + D*d ≤
        τ/2*(|a|+|c|) + |D| * (|d|-2*(|a|+|c|)) + τ/8*|4*a+b| := by
    nlinarith [hl1,hl2,hl3,hl4,hxprod,hcprod,hbprod]
  by_cases hcase : |d| ≤ 2*(|a|+|c|)
  · have hnonpos : |D| * (|d|-2*(|a|+|c|)) ≤ 0 :=
      mul_nonpos_of_nonneg_of_nonpos (abs_nonneg D) (sub_nonpos.mpr hcase)
    have hmax : (|a|+|c|)/2 ≤ max ((|a|+|c|)/2) (|d|/4) := le_max_left _ _
    have hmul := mul_le_mul_of_nonneg_left hmax hτ
    nlinarith
  · have hcase' : 0 ≤ |d|-2*(|a|+|c|) := by
      have hh := lt_of_not_ge hcase
      linarith
    have hprod : |D| * (|d|-2*(|a|+|c|)) ≤
        (τ/4)*(|d|-2*(|a|+|c|)) :=
      mul_le_mul_of_nonneg_right hD hcase'
    have hmax : |d|/4 ≤ max ((|a|+|c|)/2) (|d|/4) := le_max_right _ _
    have hmul := mul_le_mul_of_nonneg_left hmax hτ
    nlinarith

end UnforcedPatching
