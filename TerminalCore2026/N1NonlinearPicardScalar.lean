import Mathlib

/-! Edition XIV, finite scalar inequalities ONLY; PDE not formalized. -/
namespace TerminalCore2026

theorem picard_ball_scalar
    (source M A gamma : ℝ)
    (hM : 0 ≤ M) (hgamma : 0 ≤ gamma)
    (hsource : source = M / 2)
    (hgate : gamma * (2 * A + 2 * M) ≤ (1 / 2 : ℝ)) :
    source + gamma * (2 * A * M + M ^ 2) ≤ M := by
  have hmul := mul_le_mul_of_nonneg_right hgate hM
  have hnonneg : 0 ≤ gamma * M ^ 2 := by positivity
  rw [hsource]
  nlinarith

theorem picard_lipschitz_scalar
    (A M gamma delta : ℝ)
    (hdelta : 0 ≤ delta)
    (hgate : gamma * (2 * A + 2 * M) ≤ (1 / 2 : ℝ)) :
    gamma * (2 * A + 2 * M) * delta ≤ delta / 2 := by
  have h := mul_le_mul_of_nonneg_right hgate hdelta
  nlinarith

theorem picard_source_ball_radius (T F : ℝ) :
    T * F = (2 * T * F) / 2 := by ring

theorem terminal_background_exponent :
    (1 / 2 : ℚ) - (3 / 4 : ℚ) = -(1 / 4 : ℚ) := by norm_num

theorem terminal_residual_exponent :
    (3 / 2 : ℚ) - (2 : ℚ) = -(1 / 2 : ℚ) := by norm_num

theorem gate_failure_is_not_nonexistence :
    (1 : ℚ) * (2 * 1 + 4 * 1 * 1) > 1 / 2 := by norm_num

#print axioms picard_ball_scalar
#print axioms picard_lipschitz_scalar
#print axioms picard_source_ball_radius
#print axioms terminal_background_exponent
#print axioms terminal_residual_exponent
#print axioms gate_failure_is_not_nonexistence
end TerminalCore2026
