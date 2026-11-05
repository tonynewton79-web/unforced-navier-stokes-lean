import UnforcedPatching.NonlinearTriad22
import Mathlib.Tactic

/-!
# Attack 22: exact finite-triad viscous receiver threshold

This is the scalar implication after the 20-mode Fourier coefficient has
been computed. The antecedent is not an assertion about a full PDE solution.
-/
namespace UnforcedPatching

theorem positive_receiver_requires_small_amplitude
    (x A B C nu : ℝ)
    (hx : 0 < x) (hC : 0 < C) (hnu : 0 < nu)
    (hgain : 0 < (x * C) * (A * B - 6 * nu * x * C)) :
    C < A * B / (6 * nu * x) := by
  have hxc : 0 < x * C := mul_pos hx hC
  have hdiff : 0 < A * B - 6 * nu * x * C := by
    by_contra hn
    have hle : A * B - 6 * nu * x * C ≤ 0 := le_of_not_gt hn
    have hb := mul_nonpos_of_nonneg_of_nonpos (le_of_lt hxc) hle
    exact (not_lt.mpr hb) hgain
  have hden : 0 < 6 * nu * x := by positivity
  apply (lt_div_iff₀ hden).2
  nlinarith

theorem scaled_triad_exponent_gap :
    (1 / 5 : ℚ) + 9 / 20 = 13 / 20 ∧
    (1 / 5 : ℚ) < 13 / 10 ∧
    (1 / 10 : ℚ) < 13 / 20 := by
  norm_num

#print axioms positive_receiver_requires_small_amplitude
#print axioms scaled_triad_exponent_gap

end UnforcedPatching
