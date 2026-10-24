import Mathlib

/-!
Edition XXIV. Finite real-algebraic portion of the nonaxisymmetric
Reynolds-flux feasibility gate. The cylindrical angular equation,
radial integrations, Reynolds PSD, source profile, and PDE are NOT
formalized by this file.
-/
namespace TerminalCore2026

/-- For a positive 2x2 covariance minor, its mixed entry is bounded
by half of the sum of its diagonal entries. -/
theorem flux_covariance_budget (a b t : ℝ)
    (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hgram : t ^ 2 ≤ a * b) :
    2 * t ≤ a + b ∧ -2 * t ≤ a + b := by
  have hsum : 0 ≤ a + b := add_nonneg ha hb
  have hdiff : 0 ≤ (a - b) ^ 2 := sq_nonneg _
  constructor
  · by_contra hnot
    have h1 : 0 < 2 * t - (a + b) := by linarith
    have h2 : 0 < 2 * t + (a + b) := by linarith
    have hp := mul_pos h1 h2
    nlinarith [hdiff, hgram, hp]
  · by_contra hnot
    have h1 : 0 < -2 * t - (a + b) := by linarith
    have h2 : 0 < -2 * t + (a + b) := by linarith
    have hp := mul_pos h1 h2
    nlinarith [hdiff, hgram, hp]

/-- Two slices with bounded directional weighted moments cannot
support an integrated torque exceeding the moment cap. -/
theorem source_two_slice_oscillation_gate
    (fluxHi fluxLo momentHi momentLo cap : ℝ)
    (hHi : 2 * fluxHi ≤ momentHi)
    (hLo : -2 * fluxLo ≤ momentLo)
    (hCapHi : momentHi ≤ cap)
    (hCapLo : momentLo ≤ cap) :
    fluxHi - fluxLo ≤ cap := by
  linarith

/-- This fixture tests the Gaussian source antiderivative, not PDE. -/
theorem gaussian_torque_antiderivative_gap :
    (1 / 8 : ℚ) - (-1 / 8) = 1 / 4 := by
  norm_num

/-- With zero initial energy, the smooth unforced energy inequality
forces all later nonnegative kinetic energy to vanish. Scalar only. -/
theorem zero_initial_kinetic_energy_gate
    (energy dissipation : ℝ)
    (henergy : 0 ≤ energy) (hdiss : 0 ≤ dissipation)
    (hbound : energy + dissipation ≤ 0) :
    energy = 0 ∧ dissipation = 0 := by
  constructor <;> linarith

#print axioms flux_covariance_budget
#print axioms source_two_slice_oscillation_gate
#print axioms gaussian_torque_antiderivative_gap
#print axioms zero_initial_kinetic_energy_gate
end TerminalCore2026
