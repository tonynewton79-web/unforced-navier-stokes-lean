import Mathlib

/-!
# A quantitative Cauchy-to-weighted-coefficient bridge

If Cauchy estimates on a larger complex polydisc yield
|∂η^b F_a| ≤ M S^(-a) δ^(-b) b!, then the coefficient weight
in the terminal-core manuscript dominates that estimate whenever
R/S ≤ 1/4 and ρ/δ ≤ 1/4.

This Lean file proves the exact elementary all-index polynomial-
geometric bounds underlying that implication. It does not assume
that the specific imported Navier--Stokes leading profiles have
already been shown to extend holomorphically to the required domain.
-/

namespace TerminalCore2026

noncomputable section

/-- The square-polynomial factor is absorbed by a quarter-power
at *every* natural index, without finite-grid truncation. -/
theorem polynomial_geometric_bound
    (q : ℝ) (hq0 : 0 ≤ q) (hq : q ≤ (1 : ℝ)/4) :
    ∀ n : ℕ, ((n : ℝ)+1)^2 * q^n ≤ 1 := by
  intro n
  induction n with
  | zero =>
      norm_num
  | succ n ih =>
      have hn : 0 ≤ (n : ℝ) := Nat.cast_nonneg _
      have hgrow : ((n : ℝ)+2)^2 ≤
          4*((n : ℝ)+1)^2 := by
        nlinarith [sq_nonneg (n : ℝ)]
      have hqpow : 0 ≤ q^n := pow_nonneg hq0 n
      have hfac : 0 ≤ 4*q := by positivity
      calc
        (((↑(n+1) : ℝ)+1)^2) * q^(n+1)
            = ((n : ℝ)+2)^2*(q^n*q) := by
                push_cast
                rw [pow_succ]
                ring
        _ ≤ (4*((n : ℝ)+1)^2)*(q^n*q) :=
            mul_le_mul_of_nonneg_right hgrow (mul_nonneg hqpow hq0)
        _ = (((n : ℝ)+1)^2*q^n)*(4*q) := by ring
        _ ≤ 1*(4*q) := mul_le_mul_of_nonneg_right ih hfac
        _ ≤ 1 := by nlinarith

/-- Both radial and axial-index powers are simultaneously controlled,
which is the coefficientwise core of the analytic-polydisc embedding. -/
theorem two_index_cauchy_factor
    (q s : ℝ) (hq0 : 0 ≤ q) (hs0 : 0 ≤ s)
    (hq : q ≤ (1 : ℝ)/4) (hs : s ≤ (1 : ℝ)/4)
    (a b : ℕ) :
    (((a : ℝ)+1)^2 * q^a) *
      (((b : ℝ)+1)^2 * s^b) ≤ 1 := by
  have ha := polynomial_geometric_bound q hq0 hq a
  have hb := polynomial_geometric_bound s hs0 hs b
  have hnonnegA : 0 ≤ ((a : ℝ)+1)^2*q^a :=
    mul_nonneg (sq_nonneg _) (pow_nonneg hq0 a)
  have hnonnegB : 0 ≤ ((b : ℝ)+1)^2*s^b :=
    mul_nonneg (sq_nonneg _) (pow_nonneg hs0 b)
  calc
    _ ≤ 1 * (((b : ℝ)+1)^2*s^b) :=
        mul_le_mul_of_nonneg_right ha hnonnegB
    _ ≤ 1 := by simpa using hb

/-- An explicit uniform jet majorant for arrays satisfying
a product Cauchy bound. Physical jets are related to this array
after dividing out the Cauchy factorial and outer radii. -/
theorem normalized_cauchy_array_bounded
    (M q s : ℝ) (hM : 0 ≤ M)
    (hq0 : 0 ≤ q) (hs0 : 0 ≤ s)
    (hq : q ≤ (1 : ℝ)/4) (hs : s ≤ (1 : ℝ)/4)
    (jets : ℕ → ℕ → ℝ)
    (hjets : ∀ a b, |jets a b| ≤ M * q^a * s^b) :
    ∀ a b, |jets a b| *
      (((a : ℝ)+1)^2*((b : ℝ)+1)^2) ≤ M := by
  intro a b
  have hp : 0 ≤ (((a : ℝ)+1)^2*((b : ℝ)+1)^2) :=
    mul_nonneg (sq_nonneg _) (sq_nonneg _)
  have hbnd := two_index_cauchy_factor q s hq0 hs0 hq hs a b
  have hMproduct : 0 ≤ M := hM
  calc
    |jets a b| * (((a : ℝ)+1)^2*((b : ℝ)+1)^2)
      ≤ (M*q^a*s^b)*(((a : ℝ)+1)^2*((b : ℝ)+1)^2) :=
        mul_le_mul_of_nonneg_right (hjets a b) hp
    _ = M * ((((a : ℝ)+1)^2*q^a)*
      (((b : ℝ)+1)^2*s^b)) := by ring
    _ ≤ M*1 := mul_le_mul_of_nonneg_left hbnd hMproduct
    _ = M := by ring

#print axioms polynomial_geometric_bound
#print axioms two_index_cauchy_factor
#print axioms normalized_cauchy_array_bounded

end
end TerminalCore2026
