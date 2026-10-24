import Mathlib
/-!
# Exact rational full-pulse covering and residual-budget scalar gates
Only arithmetic and order logic. No Appendix-A source interval
enclosures or Navier--Stokes physical PDE is formalized here.
-/
namespace TerminalCore2026

theorem sample_three_rectangle_cover (x eta : ℝ)
    (hx0 : 0 ≤ x) (hx13 : x ≤ 13)
    (he0 : -1 ≤ eta) (he1 : eta ≤ 1) :
    (x ≤ 5 ∧ eta ≤ 0) ∨
    (5 ≤ x ∧ eta ≤ 0) ∨
    (0 ≤ eta ∧ 0 ≤ x ∧ x ≤ 13) := by
  rcases le_total eta 0 with h | h
  · rcases le_total x 5 with hx | hx
    · exact Or.inl ⟨hx,h⟩
    · exact Or.inr (Or.inl ⟨hx,h⟩)
  · exact Or.inr (Or.inr ⟨h,hx0,hx13⟩)

theorem pulse_normalized_budget_rational :
    (1:ℚ)/10000000000000*(20/9)*12
      +1/10000000+(1/2)*(2/10000000)
      +1/10000000+1500/10000000000
        < (1-1/10000000000)/1000000 := by
  norm_num

theorem positive_pulse_Q_from_relative_budget
    (q0 eQ : ℝ) (hq : 0 < q0)
    (herr : -(q0/10000000000) ≤ eQ) :
    0 < q0 + eQ := by
  have h : 0 < (1-1/10000000000:ℝ) := by norm_num
  nlinarith

#print axioms sample_three_rectangle_cover
#print axioms pulse_normalized_budget_rational
#print axioms positive_pulse_Q_from_relative_budget
end TerminalCore2026