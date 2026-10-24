import Mathlib

/-! Finite algebra for the second projected Duhamel correction.
This does not construct the Leray projector, semigroup, pressure, or unforced PDE. -/
namespace TerminalCore2026

theorem second_increment_bilinear
    {V : Type*} [AddCommGroup V]
    (B : V → V → V)
    (hleft : ∀ a b c, B (a + b) c = B a c + B b c)
    (hright : ∀ a b c, B a (b + c) = B a b + B a c)
    (u w1 w2 : V) :
    B (u + w1 + w2) (u + w1 + w2) - B (u + w1) (u + w1) =
      B u w2 + B w2 u + B w1 w2 + B w2 w1 + B w2 w2 := by
  simp only [hleft, hright]
  abel

theorem second_step_abstract_cancellation
    {V : Type*} [AddCommGroup V]
    (f l1 q1 l2 q2 : V) (hfirst : l1 = -f) (hsecond : l2 = -q1) :
    f + l1 + q1 + l2 + q2 = q2 := by
  rw [hfirst, hsecond]
  abel

theorem second_defect_budget_nonneg
    (A U V C : ℝ) (hA : 0 ≤ A) (hU : 0 ≤ U)
    (hV : 0 ≤ V) (hC : 0 ≤ C) :
    0 ≤ C * (2 * (A + U) * V + V ^ 2) := by
  positivity

#print axioms second_increment_bilinear
#print axioms second_step_abstract_cancellation
#print axioms second_defect_budget_nonneg
end TerminalCore2026
