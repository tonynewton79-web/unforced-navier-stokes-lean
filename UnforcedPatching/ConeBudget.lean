import UnforcedPatching.Periodicity
import Mathlib.Tactic

/-!
# Exact seven-ray coefficient margin at the H8 boundary

This is the finite, pointwise *algebraic* part of H8 from the October 2026
carrier-independent manuscript. It does not construct a compact stress,
solve a symmetric-divergence equation, establish the weighted estimate,
or provide a proof of any Navier--Stokes singularity.

Index conventions: `0,...,6` correspond to the paper's rays `1,...,7`.
-/

noncomputable section

namespace UnforcedPatching

/-- The seven normalized coefficients of the rational centre. -/
def sevenRayCenter (i : Fin 7) : ℝ :=
  if i.val = 2 then 236 / 1229 else 172 / 1229

/-- The pressure-gauge-adjusted coefficient perturbations of the four-field
trace-free symmetric matrix H(A,B,C,D), in the paper's ray order. -/
def sevenRayCorrection (A B C D : ℝ) (i : Fin 7) : ℝ :=
  match i.val with
  | 0 => -(3 / 2) * D
  | 1 => 2 * C - 4 * D
  | 2 => -2 * C - 4 * D
  | 3 => 2 * A - 8 * B + 4 * D
  | 4 => -2 * A + 8 * B + 4 * D
  | 5 => 8 * B
  | _ => -8 * B

/-- Exact final maximum-perturbation budget; this is not a bound verified
for any spatial stress H. -/
def h8CoefficientBudget : ℝ := 15971 / 122900

/-- The paper's rational margin identity, checked in exact arithmetic. -/
theorem h8_budget_identity :
    (172 : ℚ) / 1229 - 1 / 100 = 15971 / 122900 := by
  norm_num

/-- Conditional positivity: *if* all seven coefficient perturbations are
below the explicit budget times a nonnegative envelope, each updated
coefficient retains the promised one-hundredth envelope floor.

The pointwise hypothesis is precisely the unsolved quantitative part of H8,
not an assertion that a compact inverse meeting it exists. -/
theorem sevenRay_positive_floor (ρ A B C D : ℝ) (hρ : 0 ≤ ρ)
    (hH : ∀ i : Fin 7,
      |sevenRayCorrection A B C D i| ≤ h8CoefficientBudget * ρ)
    (i : Fin 7) :
    ρ * sevenRayCenter i + sevenRayCorrection A B C D i ≥ ρ / 100 := by
  have hcenter : (172 / 1229 : ℝ) ≤ sevenRayCenter i := by
    by_cases h : i.val = 2
    · simp [sevenRayCenter, h]
      norm_num
    · simp [sevenRayCenter, h]
  have hbaseline : ρ * (172 / 1229 : ℝ) ≤ ρ * sevenRayCenter i :=
    mul_le_mul_of_nonneg_left hcenter hρ
  have hperturb : -(h8CoefficientBudget * ρ) ≤ sevenRayCorrection A B C D i :=
    (abs_le.mp (hH i)).1
  have hfloor : ρ * (172 / 1229 : ℝ) - h8CoefficientBudget * ρ = ρ / 100 := by
    unfold h8CoefficientBudget
    ring
  linarith

end UnforcedPatching
