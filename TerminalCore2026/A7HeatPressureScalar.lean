import Mathlib

/-! Conditional algebra for Appendix A.7's signed heat replacement.
Source gamma-integral, moment-map inversion and PDE are NOT formalized. -/
namespace TerminalCore2026

theorem heat_square_defect (E q : ℝ) :
    (E * (1 - q)) ^ 2 - E ^ 2 = -(E ^ 2 * (q * (2 - q))) := by
  ring

theorem heat_pressure_nonpositive (E q : ℝ)
    (hq0 : 0 ≤ q) (hq1 : q ≤ 1) :
    (E * (1 - q)) ^ 2 - E ^ 2 ≤ 0 := by
  have htwo : 0 ≤ 2 - q := by linarith
  have hfac : 0 ≤ q * (2 - q) := mul_nonneg hq0 htwo
  have hmul : 0 ≤ E ^ 2 * (q * (2 - q)) :=
    mul_nonneg (sq_nonneg E) hfac
  nlinarith [hmul]

theorem heat_pressure_strict (E q : ℝ)
    (hE : 0 < E) (hq0 : 0 < q) (hq1 : q < 1) :
    (E * (1 - q)) ^ 2 - E ^ 2 < 0 := by
  have htwo : 0 < 2 - q := by linarith
  have hfac : 0 < q * (2 - q) := mul_pos hq0 htwo
  have hsquare : 0 < E ^ 2 := pow_pos hE 2
  have hmul : 0 < E ^ 2 * (q * (2 - q)) := mul_pos hsquare hfac
  nlinarith [hmul]

theorem exact_three_moment_restoration
    (base heat bump : ℝ) (hcancel : heat + bump = 0) :
    base + heat + bump = base := by
  linarith

theorem discrete_three_weight_witness :
    ((1 : ℚ) * ((-1/2) * 4 - (-1/4) * 2)
      - (1/8) * ((-1) * 4 - (-1/4) * 1)
      + (1/64) * ((-1) * 2 - (-1/2) * 1)) = -135/128 := by
  norm_num

theorem zero_initial_energy_obstruction
    (energy dissipation : ℝ)
    (he : 0 ≤ energy) (hd : 0 ≤ dissipation)
    (hidentity : energy + dissipation = 0) :
    energy = 0 ∧ dissipation = 0 := by
  constructor <;> linarith

#print axioms heat_square_defect
#print axioms heat_pressure_nonpositive
#print axioms heat_pressure_strict
#print axioms exact_three_moment_restoration
#print axioms discrete_three_weight_witness
#print axioms zero_initial_energy_obstruction
end TerminalCore2026
