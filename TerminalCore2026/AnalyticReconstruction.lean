import Mathlib

/-!
# Uniform radial-binomial and geometric-tail bounds

This file targets the coefficient-space reconstruction step of
Newton, *Exact Local Unforced Terminal-Core Dynamics*,
DOI 10.5281/zenodo.23474915.

Its statements are elementary all-index bounds. They do NOT prove
the Navier--Stokes lower-order forcing recurrence, the existence of
the leading profiles, or the physical PDE reconstruction.
-/
namespace TerminalCore2026

/-- Binomial growth in the doubled analytic weight is at most
four per radial degree and two per axial-derivative degree. -/
theorem choose_radial_geometric_envelope (a b : ℕ) :
    Nat.choose (2*a+b) b ≤ 4^a * 2^b := by
  calc
    Nat.choose (2*a+b) b ≤ 2^(2*a+b) :=
      Nat.choose_le_two_pow _ _
    _ = (2^2)^a * 2^b := by rw [pow_add, pow_mul]
    _ = 4^a * 2^b := by norm_num

/-- The exact finite geometric tail identity. -/
theorem half_tail_identity (n N : ℕ) :
    (∑ j ∈ Finset.range N, (1/2 : ℝ)^(n+j)) =
      2 * (1/2 : ℝ)^n * (1-(1/2 : ℝ)^N) := by
  induction N with
  | zero => simp
  | succ N ih =>
      rw [Finset.sum_range_succ, ih]
      rw [pow_add, pow_succ]
      ring

/-- Every finite radial tail is uniformly bounded, independently of
the truncation order. -/
theorem half_tail_le (n N : ℕ) :
    (∑ j ∈ Finset.range N, (1/2 : ℝ)^(n+j)) ≤
      2 * (1/2 : ℝ)^n := by
  rw [half_tail_identity]
  have hp : 0 ≤ (1/2 : ℝ)^N := pow_nonneg (by norm_num) _
  have hn : 0 ≤ (1/2 : ℝ)^n := pow_nonneg (by norm_num) _
  nlinarith

#print axioms choose_radial_geometric_envelope
#print axioms half_tail_identity
#print axioms half_tail_le

end TerminalCore2026
