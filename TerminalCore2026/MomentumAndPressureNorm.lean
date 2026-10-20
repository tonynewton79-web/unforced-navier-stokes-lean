import Mathlib

/-!
# Direct momentum channels and pressure primitive norm obstruction

Finite Lean proof gates for the momentum product/delayed viscosity
estimates and the exact polynomial divergence in the isolated
pressure primitive. These DO NOT formalize the full analytic Banach
space or prove the Navier--Stokes coefficient recurrence.
Source: Tony Newton, doi:10.5281/zenodo.23474915.
-/
namespace TerminalCore2026

theorem direct_momentum_shift_bound
    (a n : ℝ) (ha : 0 ≤ a) (hn : 0 ≤ n) (h : n ≤ a) :
    n+1 ≤ a+1 ∧ a+n+2 ≤ 2*(a+1) := by
  constructor <;> linarith

theorem positive_momentum_radial_split
    (a c : ℝ) (ha : 0 ≤ a) (hc : 0 ≤ c) :
    a ≤ a+c ∧ c ≤ a+c := by
  constructor <;> linarith

theorem pressure_pole_weight_gap_identity (b : ℝ) :
    16*(b+1)^2-(b+4)^2 = 3*b*(5*b+8) := by
  ring

theorem pressure_pole_weight_gap_nonnegative
    (b : ℝ) (hb : 0 ≤ b) :
    (b+4)^2 ≤ 16*(b+1)^2 := by
  have hp : 0 ≤ 3*b*(5*b+8) := by positivity
  nlinarith [pressure_pole_weight_gap_identity b]

/-- The lower comparison multiplier grows linearly in b,
which is incompatible with a b-independent pressure norm. -/
theorem pressure_pole_linear_lower
    (b : ℝ) (hb : 0 ≤ b) :
    (b+5)*(b+1)^2*16 ≥ (b+5)*(b+4)^2 := by
  have h := pressure_pole_weight_gap_nonnegative b hb
  exact mul_le_mul_of_nonneg_left h (by linarith)

theorem uniform_source_polynomial_budget :
    (64:ℕ)^2*25 = 102400 ∧
    (64:ℕ)^2*25^2 = 2560000 := by
  constructor <;> norm_num

#print axioms direct_momentum_shift_bound
#print axioms positive_momentum_radial_split
#print axioms pressure_pole_weight_gap_identity
#print axioms pressure_pole_weight_gap_nonnegative
#print axioms pressure_pole_linear_lower
#print axioms uniform_source_polynomial_budget

end TerminalCore2026
