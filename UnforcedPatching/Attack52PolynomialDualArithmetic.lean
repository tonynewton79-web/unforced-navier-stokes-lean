import Mathlib

/-!
Attack 52 finite algebra: self-contained exact rational moment constants for
polynomial toroidal tests in the frozen diagnostic plateau.
NOT covered: physical weak-form integration, periodic chart, compact support,
smooth carrier existence, actual G1/B.12 source, or an unforced blow-up.
-/
namespace UnforcedPatching
noncomputable section

/-- Polynomial moment of (1-x²)^4 over [-1,1], as an exact binomial sum. -/
theorem attack52_I0 :
    (2 : ℚ) * (1 - 4/3 + 6/5 - 4/7 + 1/9) = 256/315 := by
  norm_num

/-- Polynomial moment of x²(1-x²)^4 over [-1,1]. -/
theorem attack52_I2 :
    (2 : ℚ) * (1/3 - 4/5 + 6/7 - 4/9 + 1/11) = 256/3465 := by
  norm_num

/-- The coefficient in J = pi * (529/993484800). -/
theorem attack52_J_over_pi :
    (2 : ℚ) / (128^4 * 16) *
      (1728 * (256/315) + 36 * (256/3465)) * (256/315) =
    529/993484800 := by
  norm_num

/-- Rational source lower bound after using pi>3 and time-cutoff mass 8/15. -/
theorem attack52_source_constant :
    (201 : ℝ)/4000 * (3 * (529/993484800)) * (8/15) =
    35443/827904000000 := by
  norm_num

/-- Bounded derivative and nonlinear contributions. -/
theorem attack52_linear_and_total_constant :
    ((119552 : ℝ) + 21/2 + 17/10)/16 = 597821/80 ∧
    (((119552 : ℝ) + 21/2 + 17/10)/16 + 72) = 603581/80 := by
  constructor <;> norm_num

/-- Sum-of-squares identity for the quadratic contraction bound. -/
theorem attack52_quadratic_identity (a b c : ℝ) :
    72*(a^2+b^2+c^2) - (128*a*b+16*b*c) =
    64*(a-b)^2+8*(b-c)^2+8*a^2+64*c^2 := by
  ring

theorem attack52_quadratic_upper (a b c : ℝ) :
    128*a*b+16*b*c ≤ 72*(a^2+b^2+c^2) := by
  have hp : 0 ≤ 64*(a-b)^2+8*(b-c)^2+8*a^2+64*c^2 := by positivity
  nlinarith [attack52_quadratic_identity a b c]

/-- Exact final rational lower bound. -/
theorem attack52_final_ratio :
    ((35443 : ℝ) / 827904000000) / (603581/80) =
    35443 / 6246339052800000 := by
  norm_num

/-- Finite conditional inference: weak PDE inequality remains a hypothesis. -/
theorem attack52_lower_of_assumed_weak_inequality
    {q : ℝ} (hq : 0 ≤ q)
    (hweak : (35443 : ℝ) / 827904000000 <
      (597821/80) * q + 72*q^2) :
    (35443 : ℝ) / 6246339052800000 < q := by
  by_cases hq1 : q ≤ 1
  · have hq2 : q^2 ≤ q := by
      nlinarith [mul_nonneg hq (sub_nonneg.mpr hq1)]
    have hupper : (597821 : ℝ) / 80 * q + 72*q^2 ≤
        (603581 : ℝ) / 80 * q := by
      nlinarith
    have htot : (35443 : ℝ) / 827904000000 <
        (603581 : ℝ) / 80 * q := lt_of_lt_of_le hweak hupper
    norm_num at htot ⊢
    nlinarith
  · have hsmall : (35443 : ℝ) / 6246339052800000 < 1 := by norm_num
    linarith

#print axioms attack52_I0
#print axioms attack52_I2
#print axioms attack52_J_over_pi
#print axioms attack52_quadratic_upper
#print axioms attack52_lower_of_assumed_weak_inequality

end
end UnforcedPatching
