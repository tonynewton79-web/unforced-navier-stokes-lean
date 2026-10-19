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
theorem two_derivative_ratio_le_sixteen
    (a b nu : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) (hnu : 1 ≤ nu) :
    twoDerivativeRatio a b nu ≤ 16 := by
  have ha1 : 0 < a+1 := by linarith
  have ha2 : 0 ≤ 2*a+1 := by linarith
  have han : 0 < a+nu := by linarith
  have hb3 : 0 < b+3 := by linarith
  have h1 : (a+2)^2 ≤ 4*(a+1)^2 := by nlinarith [sq_nonneg a]
  have h2 : 2*a+1 ≤ 2*(a+nu) := by linarith
  have h3 : (b+1)^2 ≤ (b+3)^2 := by nlinarith
  have h12 : (a+2)^2*(2*a+1) ≤
      (4*(a+1)^2)*(2*(a+nu)) := by
    exact mul_le_mul h1 h2 (le_of_lt (by linarith : 0 < 2*a+1))
      (by positivity)
  have h123 : ((a+2)^2*(2*a+1))*(b+1)^2 ≤
      ((4*(a+1)^2)*(2*(a+nu)))*(b+3)^2 := by
    exact mul_le_mul h12 h3 (sq_nonneg _) (by positivity)
  have hden : 0 < ((a+1)^2 * (a+nu)) * (b+3)^2 := by positivity
  unfold twoDerivativeRatio
  rw [div_le_iff₀ hden]
  nlinarith [h123]

#print axioms two_derivative_ratio_le_sixteen

end
end TerminalCore2026
