import UnforcedPatching.ConeBudget

/-!
# Sharp four-field coefficient bound for the H8 seven-ray cone

The source's seven coefficient perturbations depend linearly on four
pointwise symmetric-stress coordinates `A,B,C,D`. Their sharp operator
norm from the maximum absolute coordinate to the maximum absolute
coefficient is `14`. This is an algebraic, source-independent estimate,
not a construction or weighted bound for any compact stress solution.
-/

namespace UnforcedPatching

/-- A directly checkable sufficient bound for *all seven* coefficients.
The constant `14` is sharp in the componentwise maximum norm. -/
theorem sevenRayCorrection_bound_fourField (A B C D ε : ℝ)
    (hA : |A| ≤ ε) (hB : |B| ≤ ε)
    (hC : |C| ≤ ε) (hD : |D| ≤ ε)
    (i : Fin 7) :
    |sevenRayCorrection A B C D i| ≤ 14 * ε := by
  rcases abs_le.mp hA with ⟨hAl, hAu⟩
  rcases abs_le.mp hB with ⟨hBl, hBu⟩
  rcases abs_le.mp hC with ⟨hCl, hCu⟩
  rcases abs_le.mp hD with ⟨hDl, hDu⟩
  apply abs_le.mpr
  constructor
  · fin_cases i <;> norm_num [sevenRayCorrection] <;> linarith
  · fin_cases i <;> norm_num [sevenRayCorrection] <;> linarith

/-- The fourth ray realizes the absolute row sum `2+8+4=14` at
`(A,B,C,D)=(1,-1,0,1)`. Hence no coefficient smaller than fourteen
can control all seven perturbations by the coordinate maximum. -/
theorem sevenRay_fourField_factor14_sharp :
    sevenRayCorrection 1 (-1) 0 1 ⟨3, by decide⟩ = 14 := by
  norm_num [sevenRayCorrection]

/-- The unresolved weighted H8 inequality can be reduced to the stronger
componentwise sufficient bound `14 ε ≤ (15971/122900) ρ`.

The exact compact inverse and its profile-dependent `ε` estimate are
still absent; this theorem only propagates an explicit assumption. -/
theorem sevenRay_positive_floor_of_fourField (ρ A B C D ε : ℝ)
    (hρ : 0 ≤ ρ) (hA : |A| ≤ ε) (hB : |B| ≤ ε)
    (hC : |C| ≤ ε) (hD : |D| ≤ ε)
    (hbudget : 14 * ε ≤ h8CoefficientBudget * ρ)
    (i : Fin 7) :
    ρ * sevenRayCenter i + sevenRayCorrection A B C D i ≥ ρ / 100 := by
  apply sevenRay_positive_floor ρ A B C D hρ
  · intro j
    exact (sevenRayCorrection_bound_fourField A B C D ε hA hB hC hD j).trans hbudget

end UnforcedPatching
