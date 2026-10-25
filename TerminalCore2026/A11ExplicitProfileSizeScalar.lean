import Mathlib

/-! Finite scalar implications for the A.11 source-stage size bound.
The actual source ODEs, full moment gauges, Banach/integral estimates,
stress cone and proposed unforced Navier--Stokes theorem are NOT Lean
formalized here. -/
namespace TerminalCore2026

theorem A11_cutoff_from_stage_budget (P lam : ℝ)
    (hlam : 0 ≤ lam) (hbudget : 64 * P * lam ^ 44 ≤ 1) :
    16 * P * lam ^ 45 ≤ lam / 4 := by
  have hmul := mul_le_mul_of_nonneg_right hbudget hlam
  calc
    16 * P * lam ^ 45 = (64 * P * lam ^ 44) * lam / 4 := by ring
    _ ≤ lam / 4 := by nlinarith

theorem A11_source_stage_exponent :
    (1/2:ℚ)+(1/20)<2/3 ∧
    ((1/2:ℚ)+(1/20))*(63/20)<2 := by
  constructor <;> norm_num

theorem A11_disjoint_bump_majorant :
    (640/3:ℚ)*54=11520 := by norm_num

#print axioms A11_cutoff_from_stage_budget
#print axioms A11_source_stage_exponent
#print axioms A11_disjoint_bump_majorant
end TerminalCore2026