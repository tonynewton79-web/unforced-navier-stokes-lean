import Mathlib

/-! Conditional rational A.10 to A.11 scalar gates only.
The source smooth-step integrals and unforced PDE are not formalized. -/
namespace TerminalCore2026

theorem a11_source_A10_entrance_budget :
  (40 / 17 : ℚ) / 10000000000 +
    (200 / 99) * (1 / 1000000 + 1 / 10000000000)
    < 3 / 1000000 := by
  norm_num

theorem a11_source_fixed_mismatch :
  (420 / 19 : ℚ) / 100 = 21 / 95 := by
  norm_num

theorem a11_source_fixed_root_budget :
  (3 : ℚ) * (21 / 95) = 63 / 95 ∧ (63 / 95 : ℚ) < 1 := by
  constructor <;> norm_num

theorem a11_source_fixed_jet_budget :
  (2 : ℚ) * 21 * (3 / 1000000) / 100 < 1 / 100000 := by
  norm_num

theorem a11_source_fixed_neumann_budget :
  (184320 : ℚ) / 100 ^ 28 < 1 / 4 := by
  norm_num

#print axioms a11_source_A10_entrance_budget
#print axioms a11_source_fixed_mismatch
#print axioms a11_source_fixed_root_budget
#print axioms a11_source_fixed_jet_budget
#print axioms a11_source_fixed_neumann_budget
end TerminalCore2026
