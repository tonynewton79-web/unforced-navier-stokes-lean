import Mathlib

/-!
# Four-jet radial compensation in the delayed pressure channel

Newton, *Exact Local Unforced Terminal-Core Dynamics*, Zenodo 23474915:
The principal coefficient path from U_(n-2) through V_(n-2),
the delayed Z^[2] term in Omega_(n-1), pressure integration,
and Z_(-2A,n) followed by J_1 raises radial valuation by two
while differentiating in eta four times. The theorem below controls
its normalized scalar highest-jet weight ratio.

The full variable-coefficient pressure operator and complete forcing
recurrence are not encoded in this file.
-/

namespace TerminalCore2026

noncomputable section

/-- The exact factorization behind the sharp coefficient constant 54. -/
theorem fourth_jet_gap_identity (a : ℝ) :
    54 * (a+1)^4 * (a+2)^2 -
      (2*a+1)*(2*a+2)*(2*a+3)*(2*a+4)*(a+3)^2 =
      2*a*(a+1)*(a+2)*(19*a^3+71*a^2+69*a+9) := by
  ring

/-- Uniform all-real-index polynomial domination. The coefficient-level
full ratio has a further factor (b+1)^2/(b+5)^2 ≤ 1. -/
theorem fourth_jet_gap_le_fifty_four (a : ℝ) (ha : 0 ≤ a) :
    (2*a+1)*(2*a+2)*(2*a+3)*(2*a+4)*(a+3)^2 ≤
      54 * (a+1)^4 * (a+2)^2 := by
  have hp : 0 ≤
      2*a*(a+1)*(a+2)*(19*a^3+71*a^2+69*a+9) := by
    positivity
  have hi := fourth_jet_gap_identity a
  linarith

/-- The additional axial-jet weight factor is ≤ 1. -/
theorem fourth_jet_axial_factor_le_one (b : ℝ) (hb : 0 ≤ b) :
    (b+1)^2 ≤ (b+5)^2 := by
  nlinarith

#print axioms fourth_jet_gap_identity
#print axioms fourth_jet_gap_le_fifty_four
#print axioms fourth_jet_axial_factor_le_one

end
end TerminalCore2026
