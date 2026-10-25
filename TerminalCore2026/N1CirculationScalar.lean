import Mathlib

/-!
Edition XXII. Real-algebraic implications of a circulation maximum-principle
budget. The actual cylindrical PDE, scalar maximum principle, physical source,
Leray projection, and terminal blow-up are NOT formalized in this file.
-/

namespace TerminalCore2026

/-- The source swirl exponent exceeds the parabolic radial exponent by h. -/
theorem circulation_source_exponent (h : ℝ) :
    ((1 / 2 : ℝ) + h) - 1 / 2 = h := by
  ring

/-- Under a bounded circulation budget, the source coefficient requires
a correction as large as its leading term when the scaling factor grows. -/
theorem leading_swirl_coefficient_must_cancel
    (g f correction M : ℝ)
    (hg : 0 < g)
    (hbound : g * (f + correction) ≤ M) :
    correction ≤ M / g - f := by
  have hprod : (f + correction) * g ≤ M := by
    nlinarith [hbound]
  have hquot : f + correction ≤ M / g :=
    (le_div_iff₀ hg).mpr hprod
  linarith

/-- Any coefficient correction no more negative than -f/2 requires
at least half the corresponding circulation in the total budget. -/
theorem half_source_budget_necessary
    (g f correction M J : ℝ)
    (hg : 0 ≤ g) (hcor : -f / 2 ≤ correction)
    (hbudget : g * (f + correction) ≤ M + J) :
    g * f ≤ 2 * (M + J) := by
  have hpos : 0 ≤ g * (f + 2 * correction) :=
    mul_nonneg hg (by linarith)
  nlinarith [hpos, hbudget]

/-- Direct contradiction when a fixed circulation cap falls below half the
growing source circulation. -/
theorem half_source_obstruction
    (g f correction M : ℝ)
    (hg : 0 ≤ g) (hcor : -f / 2 ≤ correction)
    (hbudget : g * (f + correction) ≤ M)
    (hstrict : 2 * M < g * f) : False := by
  have h := half_source_budget_necessary g f correction M 0 hg hcor
    (by simpa using hbudget)
  linarith

#print axioms circulation_source_exponent
#print axioms leading_swirl_coefficient_must_cancel
#print axioms half_source_budget_necessary
#print axioms half_source_obstruction
end TerminalCore2026
