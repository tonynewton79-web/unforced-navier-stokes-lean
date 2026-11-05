import Mathlib

/-!
# Attack 20: finite Fourier mode energy and frequency-power gates

These are *finite algebraic implications*, corresponding to the summation
step after establishing a PDE-specific terminal Fourier coefficient bound.
This module does not prove terminal Duhamel, Fourier Parseval, actual
Navier–Stokes mode equations, or existence of a blowup solution.
-/

namespace UnforcedPatching

/-- If each mode is bounded by C times a nonnegative weight, then the
squared Fourier energy is bounded by C^2 times the squared weights.
The analytic PDE remains a separate assumption. -/
theorem finite_mode_squared_sum
    {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (a w : ι → ℝ) (C : ℝ)
    (hC : 0 ≤ C)
    (hw : ∀ i ∈ s, 0 ≤ w i)
    (hmodal : ∀ i ∈ s, |a i| ≤ C * w i) :
    (∑ i ∈ s, a i ^ 2) ≤ C ^ 2 * (∑ i ∈ s, w i ^ 2) := by
  have hterm : ∀ i ∈ s, a i ^ 2 ≤ (C * w i) ^ 2 := by
    intro i hi
    have hb := abs_le.mp (hmodal i hi)
    have hz : 0 ≤ C * w i := mul_nonneg hC (hw i hi)
    have h1 : 0 ≤ C * w i - a i := by linarith [hb.2]
    have h2 : 0 ≤ C * w i + a i := by linarith [hb.1]
    have hp := mul_nonneg h1 h2
    nlinarith
  calc
    (∑ i ∈ s, a i ^ 2) ≤ (∑ i ∈ s, (C * w i) ^ 2) := by
      apply Finset.sum_le_sum
      intro i hi
      exact hterm i hi
    _ = C ^ 2 * (∑ i ∈ s, w i ^ 2) := by
      simp only [mul_pow, ← Finset.mul_sum]

/-- A finite energy of weight functions converts the per-mode bound
into a total spectral energy bound, without assuming a PDE solution. -/
theorem finite_mode_squared_sum_budget
    {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (a w : ι → ℝ) (C B : ℝ)
    (hC : 0 ≤ C)
    (hw : ∀ i ∈ s, 0 ≤ w i)
    (hmodal : ∀ i ∈ s, |a i| ≤ C * w i)
    (hbudget : (∑ i ∈ s, w i ^ 2) ≤ B) :
    (∑ i ∈ s, a i ^ 2) ≤ C ^ 2 * B := by
  calc
    (∑ i ∈ s, a i ^ 2) ≤ C ^ 2 * (∑ i ∈ s, w i ^ 2) :=
      finite_mode_squared_sum s a w C hC hw hmodal
    _ ≤ C ^ 2 * B := mul_le_mul_of_nonneg_left hbudget (sq_nonneg C)

/-- In three dimensions the power exponent 11/25 marks the threshold
from K^5 when p=1/5. -/
theorem fixed_mode_evacuation_power
    (α : ℚ) (hα : α < 11 / 25) :
    0 < 11 / 5 - 5 * α := by
  linarith

/-- The energy-matched exterior field satisfies the previous 90% low
frequency necessary fraction, but this is insufficient to solve the PDE. -/
theorem exterior_fraction_exceeds_nine_tenths :
    (9 / 10 : ℚ) < 11 / 12 := by
  norm_num

/-- Terminal Fourier coefficients of order tau^(1/10) cannot be
asymptotically O(tau^(6/5)) with a fixed coefficient; this declaration
records the exact exponent order, not its analytic derivation. -/
theorem fixed_mode_scaling_gap :
    (1 / 10 : ℚ) < 6 / 5 := by
  norm_num

#print axioms finite_mode_squared_sum
#print axioms finite_mode_squared_sum_budget
#print axioms fixed_mode_evacuation_power
#print axioms exterior_fraction_exceeds_nine_tenths
#print axioms fixed_mode_scaling_gap

end UnforcedPatching
