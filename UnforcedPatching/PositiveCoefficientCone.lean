import UnforcedPatching.ConeBudget
import Mathlib.Tactic

/-!
# The one-sided seven-ray positivity cone and its sharp dual upper bound

The coefficient floor is one-sided and the third centre weight differs
from the remaining six. This is not the symmetric absolute-correction
polytope. Only finite-dimensional, pointwise facts are established.
-/

noncomputable section

namespace UnforcedPatching

/-- The true one-sided coefficient polytope's candidate support function.
The radius `ρ` is a nonnegative density envelope. -/
def oneSidedPositiveConeSupport (ρ a b c d : ℝ) : ℝ :=
  let g : ℝ := 15971 / 122900
  let h : ℝ := 22371 / 122900
  ρ * ((h - g) * c / 4 + g * |4*a+b| / 8 +
    max (((3*g+h)/4)*|c| - g*d/4)
        (((3*g+h)/4)*|a| + (g+h)*d/8))

private theorem dual_upper_from_coordinate_intervals
    (ρ g h A B C D a b c d : ℝ)
    (hρ : 0 ≤ ρ)
    (hX : |A-4*B| ≤ g*ρ/2+2*D)
    (hC : |C-(h-g)*ρ/4| ≤ (g+h)*ρ/4-2*D)
    (hB : |B| ≤ g*ρ/8)
    (hDlo : -g*ρ/4 ≤ D)
    (hDhi : D ≤ (g+h)*ρ/8) :
    A*a+B*b+C*c+D*d ≤
      ρ*((h-g)*c/4 + g*|4*a+b|/8 +
        max (((3*g+h)/4)*|c|-g*d/4)
            (((3*g+h)/4)*|a|+(g+h)*d/8)) := by
  have hxprod : |A-4*B| * |a| ≤ (g*ρ/2+2*D)*|a| :=
    mul_le_mul_of_nonneg_right hX (abs_nonneg a)
  have hcprod : |C-(h-g)*ρ/4| * |c| ≤
        ((g+h)*ρ/4-2*D)*|c| :=
    mul_le_mul_of_nonneg_right hC (abs_nonneg c)
  have hbprod : |B| * |4*a+b| ≤ (g*ρ/8)*|4*a+b| :=
    mul_le_mul_of_nonneg_right hB (abs_nonneg (4*a+b))
  have hlx : (A-4*B)*a ≤ |A-4*B| * |a| := by
    calc (A-4*B)*a ≤ |(A-4*B)*a| := le_abs_self _
      _ = |A-4*B| * |a| := abs_mul _ _
  have hlc : (C-(h-g)*ρ/4)*c ≤ |C-(h-g)*ρ/4| * |c| := by
    calc (C-(h-g)*ρ/4)*c ≤ |(C-(h-g)*ρ/4)*c| := le_abs_self _
      _ = |C-(h-g)*ρ/4| * |c| := abs_mul _ _
  have hlb : B*(4*a+b) ≤ |B| * |4*a+b| := by
    calc B*(4*a+b) ≤ |B*(4*a+b)| := le_abs_self _
      _ = |B| * |4*a+b| := abs_mul _ _
  have hbase : A*a+B*b+C*c+D*d ≤
      ρ*(g*|a|/2+(g+h)*|c|/4+g*|4*a+b|/8+(h-g)*c/4)
      +D*(2*|a|-2*|c|+d) := by
    nlinarith [hxprod, hcprod, hbprod, hlx, hlc, hlb]
  by_cases hs : 0 ≤ 2*|a|-2*|c|+d
  · have hdprod : D*(2*|a|-2*|c|+d) ≤
        ((g+h)*ρ/8)*(2*|a|-2*|c|+d) :=
      mul_le_mul_of_nonneg_right hDhi hs
    have hmax : ((3*g+h)/4)*|a|+(g+h)*d/8 ≤
      max (((3*g+h)/4)*|c|-g*d/4)
          (((3*g+h)/4)*|a|+(g+h)*d/8) := le_max_right _ _
    nlinarith [mul_le_mul_of_nonneg_left hmax hρ]
  · have hs' : 2*|a|-2*|c|+d ≤ 0 := le_of_not_ge hs
    have hdprod : D*(2*|a|-2*|c|+d) ≤
        (-g*ρ/4)*(2*|a|-2*|c|+d) :=
      mul_le_mul_of_nonpos_right hDlo hs'
    have hmax : ((3*g+h)/4)*|c|-g*d/4 ≤
      max (((3*g+h)/4)*|c|-g*d/4)
          (((3*g+h)/4)*|a|+(g+h)*d/8) := le_max_left _ _
    nlinarith [mul_le_mul_of_nonneg_left hmax hρ]

/-- The one-sided positivity floor implies the exact sharp support
upper bound for each finite-dimensional four-field correction. -/
theorem one_sided_positive_cone_dual_upper
    (ρ A B C D a b c d : ℝ) (hρ : 0 ≤ ρ)
    (hFloor : ∀ i : Fin 7,
      ρ * sevenRayCenter i + sevenRayCorrection A B C D i ≥ ρ/100) :
    A*a+B*b+C*c+D*d ≤ oneSidedPositiveConeSupport ρ a b c d := by
  let g : ℝ := 15971 / 122900
  let h : ℝ := 22371 / 122900
  have h1 : ρ * (172/1229:ℝ) + 2*C-4*D ≥ ρ/100 := by
    have hh := hFloor (1 : Fin 7)
    simp [sevenRayCenter, sevenRayCorrection] at hh
    linarith
  have h2 : ρ * (236/1229:ℝ) - 2*C-4*D ≥ ρ/100 := by
    have hh := hFloor (2 : Fin 7)
    simp [sevenRayCenter, sevenRayCorrection] at hh
    linarith
  have h3 : ρ * (172/1229:ℝ) + 2*A-8*B+4*D ≥ ρ/100 := by
    have hh := hFloor (3 : Fin 7)
    simp [sevenRayCenter, sevenRayCorrection] at hh
    linarith
  have h4 : ρ * (172/1229:ℝ) - 2*A+8*B+4*D ≥ ρ/100 := by
    have hh := hFloor (4 : Fin 7)
    simp [sevenRayCenter, sevenRayCorrection] at hh
    linarith
  have h5 : ρ * (172/1229:ℝ) + 8*B ≥ ρ/100 := by
    have hh := hFloor (5 : Fin 7)
    simp [sevenRayCenter, sevenRayCorrection] at hh
    linarith
  have h6 : ρ * (172/1229:ℝ) - 8*B ≥ ρ/100 := by
    have hh := hFloor (6 : Fin 7)
    simp [sevenRayCenter, sevenRayCorrection] at hh
    linarith
  have hX : |A-4*B| ≤ g*ρ/2+2*D := by
    apply abs_le.mpr
    constructor <;> dsimp [g] <;> linarith
  have hC : |C-(h-g)*ρ/4| ≤ (g+h)*ρ/4-2*D := by
    apply abs_le.mpr
    constructor <;> dsimp [g,h] <;> linarith
  have hB : |B| ≤ g*ρ/8 := by
    apply abs_le.mpr
    constructor <;> dsimp [g] <;> linarith
  have hDlo : -g*ρ/4 ≤ D := by
    dsimp [g]
    linarith
  have hDhi : D ≤ (g+h)*ρ/8 := by
    dsimp [g,h]
    linarith
  have hu := dual_upper_from_coordinate_intervals ρ g h A B C D a b c d
    hρ hX hC hB hDlo hDhi
  simpa only [oneSidedPositiveConeSupport, g, h] using hu

end UnforcedPatching
