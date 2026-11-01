import UnforcedPatching.ExactCoefficientCone
import Mathlib.Tactic

/-!
# Case 006: a source-native axial band and its precise logical scope

This proves the *finite-dimensional* implication in the Case 006
source-native interval of the 27 October manuscript. The hypothesis is the
original symmetric **absolute** seven-coefficient budget. The same bound
does not follow from positivity of the seven final coefficients: an exact
rational counterexample below satisfies all seven positive floors.

The slice-integral source identity, zero boundary traces, rotating frames,
existence of a compact correction and the unforced Navier--Stokes PDE are
NOT proved here. The physical equality `T = alpha * rho + A` is explicit.
-/

noncomputable section

namespace UnforcedPatching

/-- Exact sharp shear bound for the original absolute coefficient budget.
It uses the coupled cone, not the insufficient 14-factor estimate. -/
theorem original_absolute_cone_shear (A B C D τ : ℝ)
    (hBudget : ∀ i : Fin 7, |sevenRayCorrection A B C D i| ≤ τ) :
    |A| ≤ τ := by
  obtain ⟨_, hAB, hB⟩ :=
    (original_seven_coefficient_cone_exact A B C D τ).mp hBudget
  have htriangle : |A| ≤ |A - 4 * B| + 4 * |B| := by
    calc
      |A| = |(A - 4 * B) + 4 * B| := by congr 1; ring
      _ ≤ |A - 4 * B| + |4 * B| := abs_add_le _ _
      _ = |A - 4 * B| + 4 * |B| := by rw [abs_mul]; norm_num
  linarith [abs_nonneg D]

/-- The manuscript's Case 006 interval, conditional on the *actual*
source-to-correction shear equality and the original absolute budget.
`rho` and `T` can be pointwise or previously integrated quantities only
when that budget and equality have been independently established. -/
theorem case006_conditional_axial_band
    (ρ T A B C D : ℝ) (_hρ : 0 ≤ ρ)
    (hShear : T = -(4443 / 9832 : ℝ) * ρ + A)
    (hBudget : ∀ i : Fin 7,
      |sevenRayCorrection A B C D i| ≤ h8CoefficientBudget * ρ) :
    -(143017 / 245800 : ℝ) * ρ ≤ T ∧
      T ≤ -(79133 / 245800 : ℝ) * ρ := by
  have hA := original_absolute_cone_shear A B C D
    (h8CoefficientBudget * ρ) hBudget
  have hAlo := (abs_le.mp hA).1
  have hAhi := (abs_le.mp hA).2
  unfold h8CoefficientBudget at hAlo hAhi
  constructor <;> linarith

/-- A finite, nonnegative weighted slice inherits exactly the same
source-native interval. This supplies a rigorous quadrature-level
consequence. It is NOT yet the continuum cylindrical integral: a separate
FTC, measurability and source-matching bridge is needed for that step. -/
theorem case006_weighted_finite_slice_band
    {ι : Type*} [Fintype ι]
    (w ρ T A B C D : ι → ℝ)
    (hw : ∀ i, 0 ≤ w i) (hρ : ∀ i, 0 ≤ ρ i)
    (hShear : ∀ i, T i = -(4443 / 9832 : ℝ) * ρ i + A i)
    (hBudget : ∀ i, ∀ j : Fin 7,
      |sevenRayCorrection (A i) (B i) (C i) (D i) j| ≤
        h8CoefficientBudget * ρ i) :
    -(143017 / 245800 : ℝ) * (∑ i, w i * ρ i) ≤
        (∑ i, w i * T i) ∧
      (∑ i, w i * T i) ≤
        -(79133 / 245800 : ℝ) * (∑ i, w i * ρ i) := by
  have hlocal (i : ι) := case006_conditional_axial_band
    (ρ i) (T i) (A i) (B i) (C i) (D i)
      (hρ i) (hShear i) (hBudget i)
  constructor
  · calc
      -(143017 / 245800 : ℝ) * (∑ i, w i * ρ i) =
          ∑ i, w i * (-(143017 / 245800 : ℝ) * ρ i) := by
        rw [Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro i _
        ring
      _ ≤ ∑ i, w i * T i := Finset.sum_le_sum (by
        intro i _
        exact mul_le_mul_of_nonneg_left (hlocal i).1 (hw i))
  · calc
      (∑ i, w i * T i) ≤
          ∑ i, w i * (-(79133 / 245800 : ℝ) * ρ i) :=
        Finset.sum_le_sum (by
          intro i _
          exact mul_le_mul_of_nonneg_left (hlocal i).2 (hw i))
      _ = -(79133 / 245800 : ℝ) * (∑ i, w i * ρ i) := by
        rw [Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro i _
        ring

/-- The candidate attaining the *upper* endpoint of the symmetric band. -/
def case006SharpA : ℝ := h8CoefficientBudget
def case006SharpB : ℝ := h8CoefficientBudget / 8

theorem case006_absolute_upper_sharp :
    (∀ i : Fin 7,
      |sevenRayCorrection case006SharpA case006SharpB 0 0 i| ≤
        h8CoefficientBudget) ∧
      -(4443 / 9832 : ℝ) + case006SharpA =
        -(79133 / 245800 : ℝ) := by
  constructor
  · intro i
    fin_cases i <;>
      norm_num [sevenRayCorrection, case006SharpA,
        case006SharpB, h8CoefficientBudget]
  · norm_num [case006SharpA, h8CoefficientBudget]

/-- Reversing both the shear and compensating azimuthal coefficient
attains the *lower* endpoint. -/
theorem case006_absolute_lower_sharp :
    (∀ i : Fin 7,
      |sevenRayCorrection (-case006SharpA) (-case006SharpB) 0 0 i| ≤
        h8CoefficientBudget) ∧
      -(4443 / 9832 : ℝ) - case006SharpA =
        -(143017 / 245800 : ℝ) := by
  constructor
  · intro i
    fin_cases i <;>
      norm_num [sevenRayCorrection, case006SharpA,
        case006SharpB, h8CoefficientBudget]
  · norm_num [case006SharpA, h8CoefficientBudget]

/-- Two rational widths in the one-sided positive cone. -/
def case006MarginG : ℝ := 15971 / 122900
def case006MarginH : ℝ := 22371 / 122900

def case006WitnessA : ℝ := (5 * case006MarginG + case006MarginH) / 4
def case006WitnessB : ℝ := case006MarginG / 8
def case006WitnessC : ℝ := (case006MarginH - case006MarginG) / 4
def case006WitnessD : ℝ := (case006MarginG + case006MarginH) / 8

/-- This explicit unit-envelope tensor satisfies all original **positive**
ray floors, including the asymmetric third ray. -/
theorem case006_positive_witness :
    ∀ i : Fin 7,
      sevenRayCenter i +
        sevenRayCorrection case006WitnessA case006WitnessB
          case006WitnessC case006WitnessD i ≥ (1 / 100 : ℝ) := by
  intro i
  fin_cases i <;>
    norm_num [sevenRayCenter, sevenRayCorrection, case006WitnessA,
      case006WitnessB, case006WitnessC, case006WitnessD,
      case006MarginG, case006MarginH]

/-- In spite of its seven positive ray floors, this tensor violates the
original *absolute* budget. This is a counterexample to conflating the
two cones, not a counterexample to the original conditional theorem. -/
theorem case006_positive_not_original_budget :
    ¬ ∀ i : Fin 7,
      |sevenRayCorrection case006WitnessA case006WitnessB
        case006WitnessC case006WitnessD i| ≤ h8CoefficientBudget := by
  intro hBudget
  have hA := original_absolute_cone_shear case006WitnessA
    case006WitnessB case006WitnessC case006WitnessD
    h8CoefficientBudget hBudget
  have hStrict : h8CoefficientBudget < |case006WitnessA| := by
    norm_num [h8CoefficientBudget, case006WitnessA,
      case006MarginG, case006MarginH]
  exact (not_lt_of_ge hA) hStrict

end UnforcedPatching
