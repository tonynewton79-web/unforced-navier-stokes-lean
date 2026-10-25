import UnforcedPatching.ConeBudget

/-! The exact H8 coefficient budget is only a *conditional* margin lemma. -/

open UnforcedPatching

#check sevenRayCorrection
#check h8CoefficientBudget
#check h8_budget_identity

example (ρ A B C D : ℝ) (hρ : 0 ≤ ρ)
    (hH : ∀ i : Fin 7, |sevenRayCorrection A B C D i| ≤ h8CoefficientBudget * ρ)
    (i : Fin 7) :
    ρ * sevenRayCenter i + sevenRayCorrection A B C D i ≥ ρ / 100 := by
  exact sevenRay_positive_floor ρ A B C D hρ hH i

#print axioms UnforcedPatching.h8_budget_identity
#print axioms UnforcedPatching.sevenRay_positive_floor
