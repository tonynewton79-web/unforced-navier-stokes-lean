import Mathlib

/-! Scalar current-order pressure feedback gates; not an end-to-end PDE proof. -/
namespace TerminalCore2026
theorem current_pressure_radial_identity (a : ℝ) :
    2*(a+1)*(2*a+3)-(a+2)^2=3*a^2+6*a+2 := by
  ring
theorem current_pressure_radial_gain (a : ℝ) (ha : 0 ≤ a) :
    (a+2)^2 ≤ 2*(a+1)*(2*a+3) := by
  have hp : 0 ≤ 3*a^2+6*a+2 := by positivity
  nlinarith [current_pressure_radial_identity a]
theorem current_pressure_degree_monotonic (n a : ℝ)
    (hn : 0 ≤ n) (h : n ≤ a) :
    (n+1)^2 ≤ (a+1)^2 := by
  nlinarith [sq_nonneg (a-n)]
theorem current_swirl_two_ordered_pairs (φ₀ φₙ : ℝ) :
    φ₀*φₙ+φₙ*φ₀=2*φ₀*φₙ := by ring
theorem terminal_similarity_jacobian (h η : ℝ) :
    1-(1-2*(1/2-h))*η^2=1-2*h*η^2 := by ring
#print axioms current_pressure_radial_identity
#print axioms current_pressure_radial_gain
#print axioms current_pressure_degree_monotonic
#print axioms current_swirl_two_ordered_pairs
#print axioms terminal_similarity_jacobian
end TerminalCore2026
