import UnforcedPatching.ConeBudget
import Mathlib.Tactic

/-!
# The original seven-ray H8 coefficient budget as three exact inequalities

This pointwise equivalence is stronger information than the sufficient
`14 * max(|A|,|B|,|C|,|D|)` estimate. It supplies no spatial inverse.
-/

noncomputable section

namespace UnforcedPatching

private theorem two_abs_bounds_iff (x y τ : ℝ) :
    (|x + y| ≤ τ ∧ |x - y| ≤ τ) ↔ |x| + |y| ≤ τ := by
  constructor
  · rintro ⟨hplus, hminus⟩
    have hp := abs_le.mp hplus
    have hm := abs_le.mp hminus
    rcases le_total 0 x with hx | hx <;> rcases le_total 0 y with hy | hy
    · rw [abs_of_nonneg hx, abs_of_nonneg hy]; linarith
    · rw [abs_of_nonneg hx, abs_of_nonpos hy]; linarith
    · rw [abs_of_nonpos hx, abs_of_nonneg hy]; linarith
    · rw [abs_of_nonpos hx, abs_of_nonpos hy]; linarith
  · intro h
    constructor
    · exact le_trans (abs_add_le x y) h
    · have hs : |x - y| ≤ |x| + |y| := by
        simpa [sub_eq_add_neg] using (abs_add_le x (-y))
      exact le_trans hs h

/-- The original seven individual H8 coefficient constraints are exactly
three coupled weighted diamonds. No `14`-factor relaxation is used. -/
theorem original_seven_coefficient_cone_exact (A B C D τ : ℝ) :
    (∀ i : Fin 7, |sevenRayCorrection A B C D i| ≤ τ) ↔
      (4 * |D| + 2 * |C| ≤ τ ∧
       4 * |D| + 2 * |A - 4 * B| ≤ τ ∧
       8 * |B| ≤ τ) := by
  have hc : (|2*C+4*D| ≤ τ ∧ |2*C-4*D| ≤ τ) ↔
      4*|D|+2*|C| ≤ τ := by
    have h := two_abs_bounds_iff (2*C) (4*D) τ
    simpa [abs_mul, add_comm, mul_comm] using h
  have ha : (|(2*A-8*B)+4*D| ≤ τ ∧ |(2*A-8*B)-4*D| ≤ τ) ↔
      4*|D|+2*|A-4*B| ≤ τ := by
    have h := two_abs_bounds_iff (2*(A-4*B)) (4*D) τ
    have hx : 2*(A-4*B) = 2*A-8*B := by ring
    rw [hx] at h
    have habs : |2*A-8*B| = 2*|A-4*B| := by
      rw [← hx, abs_mul]
      norm_num
    rw [habs] at h
    simpa [abs_mul, add_comm, mul_comm] using h
  constructor
  · intro h
    have hcdPlus : |2*C+4*D| ≤ τ := by
      have h2 := h (2 : Fin 7)
      have eq : -(2*C)-4*D = -(2*C+4*D) := by ring
      norm_num [sevenRayCorrection] at h2
      rw [eq, abs_neg] at h2
      exact h2
    have hcdMinus : |2*C-4*D| ≤ τ := by
      simpa [sevenRayCorrection] using h (1 : Fin 7)
    have habPlus : |(2*A-8*B)+4*D| ≤ τ := by
      simpa [sevenRayCorrection, sub_eq_add_neg, add_assoc] using h (3 : Fin 7)
    have habMinus : |(2*A-8*B)-4*D| ≤ τ := by
      have h4 := h (4 : Fin 7)
      have eq : -(2*A)+8*B+4*D = -((2*A-8*B)-4*D) := by ring
      norm_num [sevenRayCorrection] at h4
      rw [eq, abs_neg] at h4
      exact h4
    have hb : 8*|B| ≤ τ := by
      simpa [sevenRayCorrection, abs_mul] using h (5 : Fin 7)
    exact ⟨hc.mp ⟨hcdPlus,hcdMinus⟩,ha.mp ⟨habPlus,habMinus⟩,hb⟩
  · rintro ⟨hCD,hAB,hB⟩ i
    have hpCD := (hc.mpr hCD).1
    have hmCD := (hc.mpr hCD).2
    have hpAB := (ha.mpr hAB).1
    have hmAB := (ha.mpr hAB).2
    have hzero : |-(3/2)*D| ≤ τ := by
      have hh : (3/2:ℝ)*|D| ≤ τ := by
        nlinarith [abs_nonneg C, abs_nonneg D]
      have hcoef : |(3/2:ℝ)| = 3/2 := by norm_num
      simpa [abs_mul, abs_neg, hcoef] using hh
    fin_cases i
    · simpa [sevenRayCorrection] using hzero
    · simpa [sevenRayCorrection] using hmCD
    · change |(-2:ℝ)*C-4*D| ≤ τ
      have eq : (-2:ℝ)*C-4*D = -(2*C+4*D) := by ring
      rw [eq, abs_neg]
      exact hpCD
    · simpa [sevenRayCorrection, sub_eq_add_neg, add_assoc] using hpAB
    · change |(-2:ℝ)*A+8*B+4*D| ≤ τ
      have eq : (-2:ℝ)*A+8*B+4*D = -((2*A-8*B)-4*D) := by ring
      rw [eq, abs_neg]
      exact hmAB
    · simpa [sevenRayCorrection, abs_mul] using hB
    · simpa [sevenRayCorrection, abs_mul, abs_neg] using hB

end UnforcedPatching
