import Mathlib

/-!
Edition XIII scalar consequences only. The actual Leray projector,
Bochner heat-semigroup integral, Gaussian PDE and Navier--Stokes
singularity are NOT formalized here.
-/
namespace TerminalCore2026

theorem projected_first_step_residual
    (R projected gradient linearCorrection pressureCorrection nonlinear : ℝ)
    (hSplit : R = projected + gradient)
    (hLinear : linearCorrection = -projected)
    (hPressure : pressureCorrection = -gradient) :
    R + linearCorrection + pressureCorrection + nonlinear = nonlinear := by
  rw [hSplit, hLinear, hPressure]
  ring

theorem projected_startup_dual
    (backgroundPair projectedPair gradientPair initialJet : ℝ)
    (hsplit : backgroundPair = projectedPair + gradientPair)
    (hpressure : gradientPair = 0)
    (hjet : initialJet = -projectedPair) :
    initialJet = -backgroundPair := by
  rw [hsplit, hpressure] at *
  linarith

theorem first_step_abstract_remainder_budget
    (a M U C : ℝ) (ha : 0 ≤ a) (hM : 0 ≤ M)
    (hU : 0 ≤ U) (hC : 0 ≤ C) :
    0 ≤ U * a * M + C * a^2 * M^2 := by
  positivity

theorem gaussian_radial_curl_coefficient
    (r z E : ℝ) : 4 * r * z * E = 2 * (2 * r * z * E) := by
  ring

#print axioms projected_first_step_residual
#print axioms projected_startup_dual
#print axioms first_step_abstract_remainder_budget
#print axioms gaussian_radial_curl_coefficient
end TerminalCore2026
