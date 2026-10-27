import UnforcedPatching.ConeOperator

/-!
Downstream use of a four-field quantitative H8 sufficient bound.
The numerical coefficient is sharp for the chosen componentwise norm;
no compact PDE inverse is asserted by these finite algebraic claims.
-/

namespace UnforcedPatching

example (A B C D ε : ℝ) (hA : |A| ≤ ε) (hB : |B| ≤ ε)
    (hC : |C| ≤ ε) (hD : |D| ≤ ε) (i : Fin 7) :
    |sevenRayCorrection A B C D i| ≤ 14 * ε := by
  exact sevenRayCorrection_bound_fourField A B C D ε hA hB hC hD i

example (ρ A B C D ε : ℝ) (hρ : 0 ≤ ρ)
    (hA : |A| ≤ ε) (hB : |B| ≤ ε)
    (hC : |C| ≤ ε) (hD : |D| ≤ ε)
    (hbudget : 14 * ε ≤ h8CoefficientBudget * ρ) (i : Fin 7) :
    ρ * sevenRayCenter i + sevenRayCorrection A B C D i ≥ ρ / 100 := by
  exact sevenRay_positive_floor_of_fourField ρ A B C D ε
    hρ hA hB hC hD hbudget i

example : sevenRayCorrection 1 (-1) 0 1 ⟨3, by decide⟩ = 14 :=
  sevenRay_fourField_factor14_sharp

end UnforcedPatching

#print axioms UnforcedPatching.sevenRayCorrection_bound_fourField
#print axioms UnforcedPatching.sevenRay_positive_floor_of_fourField
#print axioms UnforcedPatching.sevenRay_fourField_factor14_sharp
