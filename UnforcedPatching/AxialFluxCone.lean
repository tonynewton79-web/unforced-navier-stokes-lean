import UnforcedPatching.ConeBudget
import Mathlib.Tactic

/-!
# Sharp meridional stress bound under the genuine seven-ray floor

The four-field coordinate `A = H_rz` controls the integrated axial
meridional flux in the cylindrical H8 balance. This is a pointwise
necessary cone condition, *not* an analytic divergence inverse.
-/

namespace UnforcedPatching

/-- An exact sharp necessary pointwise cap for the meridional stress.
The constant `51113/245800` is attained by a positive ray allocation;
only the upper bound is proved in this declaration. -/
theorem one_sided_positive_cone_axial_cap
    (ρ A B C D : ℝ) (hρ : 0 ≤ ρ)
    (hFloor : ∀ i : Fin 7,
      ρ * sevenRayCenter i + sevenRayCorrection A B C D i ≥ ρ/100) :
    |A| ≤ (51113 / 245800 : ℝ) * ρ := by
  have hC1 := hFloor (1 : Fin 7)
  have hC2 := hFloor (2 : Fin 7)
  have hA1 := hFloor (3 : Fin 7)
  have hA2 := hFloor (4 : Fin 7)
  have hB1 := hFloor (5 : Fin 7)
  have hB2 := hFloor (6 : Fin 7)
  simp [sevenRayCenter, sevenRayCorrection] at
    hC1 hC2 hA1 hA2 hB1 hB2
  apply abs_le.mpr
  constructor <;> nlinarith

/-- Explicit positive ray allocation saturating the sharp local `A` cap.
This witness is finite algebra, not a compactly supported stress. -/
theorem one_sided_positive_cone_axial_cap_sharp :
    ∀ i : Fin 7,
      sevenRayCenter i +
        sevenRayCorrection
          (51113 / 245800 : ℝ)
          (15971 / 983200 : ℝ)
          (16 / 1229 : ℝ)
          (19171 / 491600 : ℝ) i ≥ (1 / 100 : ℝ) := by
  intro i
  fin_cases i <;> norm_num [sevenRayCenter, sevenRayCorrection]

/-- The cylindrical azimuthal stress coordinate `C=H_rtheta` lies in
a sharp asymmetric interval under the one-sided seven-ray floor. -/
theorem one_sided_positive_cone_azimuthal_interval
    (ρ A B C D : ℝ) (hρ : 0 ≤ ρ)
    (hFloor : ∀ i : Fin 7,
      ρ * sevenRayCenter i + sevenRayCorrection A B C D i ≥ ρ/100) :
    -(15971 / 122900 : ℝ) * ρ ≤ C ∧
      C ≤ (19171 / 122900 : ℝ) * ρ := by
  have hC1 := hFloor (1 : Fin 7)
  have hC2 := hFloor (2 : Fin 7)
  have hA1 := hFloor (3 : Fin 7)
  have hA2 := hFloor (4 : Fin 7)
  simp [sevenRayCenter, sevenRayCorrection] at hC1 hC2 hA1 hA2
  constructor <;> linarith

/-- Exact pointwise ray allocation saturating the upper C bound. -/
theorem one_sided_positive_cone_azimuthal_upper_sharp :
    ∀ i : Fin 7,
      sevenRayCenter i + sevenRayCorrection
        (0 : ℝ) (0 : ℝ)
        (19171 / 122900 : ℝ)
        (-(15971 / 491600) : ℝ) i ≥ (1 / 100 : ℝ) := by
  intro i
  fin_cases i <;> norm_num [sevenRayCenter, sevenRayCorrection]

/-- Exact pointwise ray allocation saturating the lower C bound. -/
theorem one_sided_positive_cone_azimuthal_lower_sharp :
    ∀ i : Fin 7,
      sevenRayCenter i + sevenRayCorrection
        (0 : ℝ) (0 : ℝ)
        (-(15971 / 122900) : ℝ)
        (-(15971 / 491600) : ℝ) i ≥ (1 / 100 : ℝ) := by
  intro i
  fin_cases i <;> norm_num [sevenRayCenter, sevenRayCorrection]

end UnforcedPatching
