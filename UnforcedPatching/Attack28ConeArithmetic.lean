import Mathlib

/-!
# Attack 28: finite rational arithmetic for the joint toroidal cone gate

Only the scalar algebraic consequences are formalized here. The cylindrical
Navier--Stokes angular-momentum identity, source-matched compact stress
existence, integrating-factor integral, authentic implicit-q carrier and
the global unforced PDE do not follow from this module.
-/

namespace UnforcedPatching

/-- The exact one-sided B-coefficient slack in the specified seven-ray cone. -/
def attack28Gamma : ℚ := 15971 / 122900

theorem attack28_gamma_pos : (0 : ℚ) < attack28Gamma := by
  norm_num [attack28Gamma]

/-- This fraction is the exact radial polynomial control threshold. -/
theorem attack28_threshold_normalization :
    (9 : ℚ) / (10 * attack28Gamma) = 110610 / 15971 := by
  norm_num [attack28Gamma]

/-- The sign of the generated fourfold flux cannot be reversed by a real
amplitude ε because its relative ε² correction is nonnegative. -/
theorem attack28_fourfold_increases_flux_magnitude (ε : ℝ) :
    1 ≤ 1 + (5 / 264 : ℝ) * ε ^ 2 := by
  nlinarith [sq_nonneg ε]

theorem attack28_fourfold_multiplier_pos (ε : ℝ) :
    0 < 1 + (5 / 264 : ℝ) * ε ^ 2 := by
  have h := attack28_fourfold_increases_flux_magnitude ε
  linarith

/-- Scalar consequence of the integrated positive-factor inequality.
The actual analytic integral identity is an explicit external proof
obligation and is not encoded in this theorem. -/
theorem attack28_weighted_budget_threshold
    (gamma lambda M j : ℝ)
    (hgamma : 0 < gamma) (hM : 0 < M)
    (hbudget : |j| * M ≤ (gamma / 8) * lambda * M) :
    8 * |j| / gamma ≤ lambda := by
  have hcap : |j| ≤ (gamma / 8) * lambda := by
    apply (mul_le_mul_right hM).mp
    nlinarith [hbudget]
  have hn : 8 * |j| ≤ gamma * lambda := by
    nlinarith [hcap]
  exact (div_le_iff₀ hgamma).2 hn

#print axioms attack28_gamma_pos
#print axioms attack28_threshold_normalization
#print axioms attack28_fourfold_increases_flux_magnitude
#print axioms attack28_fourfold_multiplier_pos
#print axioms attack28_weighted_budget_threshold

end UnforcedPatching
