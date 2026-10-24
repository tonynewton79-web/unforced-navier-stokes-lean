import Mathlib

/-!
# One-derivative channel of the terminal-core radial inverse

The estimates are dimensionless weight-ratio bounds for the ambient
analytic coefficient norm in eq. (37) of Zenodo 23474915. They are
not the four-block PDE current-order bound (51).
-/
namespace TerminalCore2026

noncomputable section

def firstDerivativeRatio (a b nu : ℝ) : ℝ :=
  2 * (a+2)^2 * (2*a+1) * (b+1)^2 /
    ((a+1)^2 * (a+nu) * (2*a+b+2) * (b+2)^2)

/-- For the one-eta-derivative channel, the regular-singular inverse
has an explicit O(1/(a+1)) coefficient multiplier. -/
theorem first_derivative_ratio_le
    (a b nu : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) (hnu : 1 ≤ nu) :
    firstDerivativeRatio a b nu ≤ 8 / (a+1) := by
  have ha1 : 0 < a+1 := by linarith
  have han : 0 < a+nu := by linarith
  have hb2 : 0 < b+2 := by linarith
  have htw : 0 < 2*a+b+2 := by linarith
  have hcore : (a+2)^2 ≤ 4*(a+1)^2 := by nlinarith [sq_nonneg a]
  have hf : 2*a+1 ≤ 2*a+b+2 := by linarith
  have hbnd : (b+1)^2 ≤ (b+2)^2 := by nlinarith
  have hnu' : a+1 ≤ a+nu := by linarith
  have hbase :
      (a+2)^2 * (2*a+1) * (b+1)^2 ≤
      4*(a+1)^2 * (2*a+b+2) * (b+2)^2 := by
    calc
      _ ≤ 4*(a+1)^2 * (2*a+1) * (b+1)^2 := by gcongr
      _ ≤ 4*(a+1)^2 * (2*a+b+2) * (b+2)^2 := by gcongr
  have hscale :
      (a+1)*((a+2)^2*(2*a+1)*(b+1)^2) ≤
      4*(a+1)^2*(a+nu)*(2*a+b+2)*(b+2)^2 := by
    calc
      _ ≤ (a+1)*(4*(a+1)^2*(2*a+b+2)*(b+2)^2) :=
        mul_le_mul_of_nonneg_left hbase (le_of_lt ha1)
      _ ≤ (a+nu)*(4*(a+1)^2*(2*a+b+2)*(b+2)^2) := by
        gcongr
      _ = _ := by ring
  have hden : 0 <
      (a+1)^2*(a+nu)*(2*a+b+2)*(b+2)^2 := by positivity
  unfold firstDerivativeRatio
  apply (div_le_div_iff₀ hden ha1).2
  nlinarith [hscale]

#print axioms first_derivative_ratio_le

end
end TerminalCore2026
