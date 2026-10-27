import UnforcedPatching.AxialFluxCone
import Mathlib.Tactic

/-!
# Coupled axial--azimuthal necessary bounds in the H8 source frame

The original one-sided seven-ray floors constrain `A = H_rz` and
`C = H_rtheta` jointly. These finite algebraic inequalities do not
establish a compact symmetric-divergence inverse or an unforced PDE
solution. The converse lift is recorded in the analytic manuscript and
exact-rational Python certificates; this module proves necessity.
-/

namespace UnforcedPatching

/-- Sharp necessary joint bounds for the azimuthal-axial coefficient
projection `(A,B)`. This is the parallelogram which also governs the
source curl at an axial rank-one quadratic vacuum point once the
analytic stress-jet reduction has been established. -/
theorem one_sided_positive_cone_ab_parallelogram
    (ρ A B C D : ℝ) (_hρ : 0 ≤ ρ)
    (hFloor : ∀ i : Fin 7,
      ρ * sevenRayCenter i + sevenRayCorrection A B C D i ≥ ρ/100) :
    |B| ≤ (15971 / 983200 : ℝ) * ρ ∧
      |A - 4 * B| ≤ (17571 / 122900 : ℝ) * ρ := by
  have hC1 := hFloor (1 : Fin 7)
  have hC2 := hFloor (2 : Fin 7)
  have hA1 := hFloor (3 : Fin 7)
  have hA2 := hFloor (4 : Fin 7)
  have hB1 := hFloor (5 : Fin 7)
  have hB2 := hFloor (6 : Fin 7)
  simp [sevenRayCenter, sevenRayCorrection] at
    hC1 hC2 hA1 hA2 hB1 hB2
  have hDhi : D ≤ (19171 / 491600 : ℝ) * ρ := by
    linarith
  have hBhi : B ≤ (15971 / 983200 : ℝ) * ρ := by
    linarith
  have hBlo : -B ≤ (15971 / 983200 : ℝ) * ρ := by
    linarith
  have hXhi : A - 4 * B ≤ (17571 / 122900 : ℝ) * ρ := by
    linarith
  have hXlo : -(A - 4 * B) ≤ (17571 / 122900 : ℝ) * ρ := by
    linarith
  exact ⟨abs_le.mpr ⟨hBlo, hBhi⟩,
    abs_le.mpr ⟨hXlo, hXhi⟩⟩

/-- Exact jointly sharp hexagonal necessary bounds for the `A,C`
projection of the one-sided seven-ray coefficient floor. -/
theorem one_sided_positive_cone_joint_ac_bounds
    (ρ A B C D : ℝ) (hρ : 0 ≤ ρ)
    (hFloor : ∀ i : Fin 7,
      ρ * sevenRayCenter i + sevenRayCorrection A B C D i ≥ ρ/100) :
    (-(15971 / 122900 : ℝ) * ρ ≤ C ∧
      C ≤ ((15971 + 22371) / 245800 : ℝ) * ρ) ∧
    |A| - C ≤ (47913 / 245800 : ℝ) * ρ ∧
    |A| + C ≤ (54313 / 245800 : ℝ) * ρ := by
  have hC := one_sided_positive_cone_azimuthal_interval ρ A B C D hρ hFloor
  have h1 := hFloor (1 : Fin 7)
  have h2 := hFloor (2 : Fin 7)
  have h3 := hFloor (3 : Fin 7)
  have h4 := hFloor (4 : Fin 7)
  have h5 := hFloor (5 : Fin 7)
  have h6 := hFloor (6 : Fin 7)
  simp [sevenRayCenter, sevenRayCorrection] at h1 h2 h3 h4 h5 h6
  have hAhi : A ≤ (15971 / 122900 : ℝ) * ρ + 2 * D := by
    linarith
  have hAlo : -A ≤ (15971 / 122900 : ℝ) * ρ + 2 * D := by
    linarith
  have hAbs : |A| ≤ (15971 / 122900 : ℝ) * ρ + 2 * D :=
    abs_le.mpr ⟨by linarith, hAhi⟩
  refine ⟨?_, ?_, ?_⟩
  · constructor
    · exact hC.1
    · linarith [hC.2]
  · linarith
  · linarith

/-- Where the coefficient envelope vanishes, all four source-frame
coordinates vanish. This is a pointwise algebraic lemma. The analytic
consequence that a source is irrotational on an open zero-density collar
requires the actual differential source identity and is not asserted
by this Lean theorem. -/
theorem one_sided_positive_cone_zero_density
    (A B C D : ℝ)
    (hFloor : ∀ i : Fin 7,
      (0 : ℝ) * sevenRayCenter i +
        sevenRayCorrection A B C D i ≥ (0 : ℝ) / 100) :
    A = 0 ∧ B = 0 ∧ C = 0 ∧ D = 0 := by
  have h1 := hFloor (1 : Fin 7)
  have h2 := hFloor (2 : Fin 7)
  have h3 := hFloor (3 : Fin 7)
  have h4 := hFloor (4 : Fin 7)
  have h5 := hFloor (5 : Fin 7)
  have h6 := hFloor (6 : Fin 7)
  simp [sevenRayCorrection] at h1 h2 h3 h4 h5 h6
  refine ⟨?_, ?_, ?_, ?_⟩ <;> linarith

end UnforcedPatching
