import Mathlib

/-!
# Exact two-parameter derivative ratio for the doubled analytic weight

This file formalizes the dimensionless coefficient-ratio bound underlying
equations (45) and (118) of *Exact Local Unforced Terminal-Core Dynamics*
(doi:10.5281/zenodo.23474915). Here a, b represent nonnegative indices;
nu ≥ 1 covers both ν=1 and ν=2 radial inverses.

The theorem is an all-index real inequality (not a finite numerical grid).
To turn it into the analytic operator statement (42), a concrete function
space, its norm, and the associated coefficientwise operator must be defined
and connected by a separate Lean theorem.
-/

namespace TerminalCore2026

noncomputable section

/-- The dimensionless factor in the two-eta-derivative coefficient ratio,
with the overall factor R/rho^2 removed. -/
def twoDerivativeRatio (a b nu : ℝ) : ℝ :=
  (2 * (a+2)^2 * (2*a+1) * (b+1)^2) /
    ((a+1)^2 * (a+nu) * (b+3)^2)

/-- All-index (not finite-grid) bound corresponding to Eq. (45)/(118). -/
theorem two_derivative_ratio_le_eight
    (a b nu : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) (hnu : 1 ≤ nu) :
    twoDerivativeRatio a b nu ≤ 8 := by
  have ha1 : 0 < a+1 := by linarith
  have ha2 : 0 ≤ 2*a+1 := by linarith
  have han : 0 < a+nu := by linarith
  have hb3 : 0 < b+3 := by linarith
  have hzero : 0 ≤ a^2 * (2*a+3) :=
    mul_nonneg (sq_nonneg a) (by linarith)
  have hcore : (a+2)^2*(2*a+1) ≤ 4*(a+1)^3 := by
    nlinarith [hzero]
  have hshift : (a+1)^3 ≤ (a+1)^2*(a+nu) := by
    have hmono : a+1 ≤ a+nu := by linarith
    have hprod := mul_le_mul_of_nonneg_left hmono (sq_nonneg (a+1))
    nlinarith [hprod]
  have h2 : (a+2)^2*(2*a+1) ≤
      4*((a+1)^2*(a+nu)) := by
    linarith
  have h3 : (b+1)^2 ≤ (b+3)^2 := by nlinarith
  have h123 : ((a+2)^2*(2*a+1))*(b+1)^2 ≤
      (4*((a+1)^2*(a+nu)))*(b+3)^2 := by
    exact mul_le_mul h2 h3 (sq_nonneg _) (by positivity)
  have hden : 0 < ((a+1)^2 * (a+nu)) * (b+3)^2 := by positivity
  unfold twoDerivativeRatio
  rw [div_le_iff₀ hden]
  nlinarith [h123]

/-- The dimensionless ratio has nonnegative coefficients on its physical domain. -/
theorem two_derivative_ratio_nonneg
    (a b nu : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) (hnu : 1 ≤ nu) :
    0 ≤ twoDerivativeRatio a b nu := by
  have ha1 : 0 ≤ a+1 := by linarith
  have ha2 : 0 ≤ a+2 := by linarith
  have ha3 : 0 ≤ 2*a+1 := by linarith
  have han : 0 ≤ a+nu := by linarith
  have hb1 : 0 ≤ b+1 := by linarith
  have hb3 : 0 ≤ b+3 := by linarith
  unfold twoDerivativeRatio
  positivity

/-- A concrete bounded-array operator induced by the normalized two-eta
coefficient transport. For actual profile jets, the correspondence to
the weighted analytic coefficient space is a further obligation. -/
theorem normalized_jet_transport_bounded
    (nu M : ℝ) (hnu : 1 ≤ nu) (hM : 0 ≤ M)
    (jets : ℕ → ℕ → ℝ)
    (hjets : ∀ a b, |jets a b| ≤ M) :
    ∀ (a b : ℕ),
      |twoDerivativeRatio (a : ℝ) (b : ℝ) nu *
        jets a (b+2)| ≤ 8*M := by
  intro a b
  have ha : 0 ≤ (a : ℝ) := Nat.cast_nonneg _
  have hb : 0 ≤ (b : ℝ) := Nat.cast_nonneg _
  have hr0 : 0 ≤ twoDerivativeRatio (a : ℝ) (b : ℝ) nu :=
    two_derivative_ratio_nonneg _ _ _ ha hb hnu
  have hr8 : twoDerivativeRatio (a : ℝ) (b : ℝ) nu ≤ 8 :=
    two_derivative_ratio_le_eight _ _ _ ha hb hnu
  rw [abs_mul, abs_of_nonneg hr0]
  calc
    twoDerivativeRatio (a : ℝ) (b : ℝ) nu *
        |jets a (b+2)| ≤
      twoDerivativeRatio (a : ℝ) (b : ℝ) nu * M :=
        mul_le_mul_of_nonneg_left (hjets _ _) hr0
    _ ≤ 8*M := mul_le_mul_of_nonneg_right hr8 hM

#print axioms normalized_jet_transport_bounded

#print axioms two_derivative_ratio_le_eight

end
end TerminalCore2026
