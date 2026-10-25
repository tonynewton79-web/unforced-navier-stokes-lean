import Mathlib

/-!
# Rational scalar gates for the Appendix-B axis-data complex fence

These are finite rational-polynomial certificates. The complete complex
nonvanishing theorem is proved in the accompanying mathematical note;
the source pressure datum, nonlinear fixed point, and unforced NS theorem
are NOT kernel-certified here.
-/
namespace TerminalCore2026

theorem axis_fence_rational_constants :
    (0:ℚ) < 607/625 ∧
    (219/10:ℚ) < 22 ∧
    (6217/500:ℚ) < 13 ∧
    (103/100:ℚ)*13*(16/9) < 25 ∧
    (11/10:ℚ)+(1/10)/100 < 6/5 := by
  norm_num

theorem source_axis_H_diagnostic (z : ℚ) :
    (99/200:ℚ)*z + (1-z^2)*(4*z+1/50) =
      -4*z^3-z^2/50+(899/200)*z+1/50 := by
  ring

theorem source_axis_H_bracket_left :
    (-4*(-1/200:ℚ)^3-(-1/200:ℚ)^2/50
     +(899/200)*(-1/200)+1/50) = -99/40000 := by
  norm_num

theorem source_axis_H_bracket_right :
    (-4*(-1/250:ℚ)^3-(-1/250:ℚ)^2/50
     +(899/200)*(-1/250)+1/50) = 63123/31250000 := by
  norm_num

theorem source_axis_W_lower (eta : ℚ)
    (hl : -1 ≤ eta) (hr : eta ≤ 1) :
    14701/5000 ≤ 3-eta^2/25+(99/5000)*eta := by
  have h1 : 0 ≤ 1-eta := by linarith
  have h2 : 0 ≤ 1+eta := by linarith
  have hh : 0 ≤ (1-eta)*(1+eta) := mul_nonneg h1 h2
  nlinarith

#print axioms axis_fence_rational_constants
#print axioms source_axis_H_diagnostic
#print axioms source_axis_H_bracket_left
#print axioms source_axis_H_bracket_right
#print axioms source_axis_W_lower

end TerminalCore2026
