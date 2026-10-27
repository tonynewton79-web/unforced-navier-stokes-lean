import UnforcedPatching.Retention

/-!
An independent downstream theorem-use test for the terminal trace bridge.
Both nonlinear cancellation and exact PDE construction remain separate gates.
-/

namespace UnforcedPatching

open NavierStokes.ProblemStatement
open Set

example (u w : VelocityField) (hu : SpeedUnboundedAtOne u)
    (α C : ℝ) (hα : 0 ≤ α) (hsmall : α < 1) (hC : 0 ≤ C)
    (hw : ∀ t ∈ Ioo (0 : ℝ) 1, ∀ x : Space,
      ‖w (t, x)‖ ≤ α * ‖u (t, x)‖ + C) :
    SpeedUnboundedAtOne (u + w) := by
  exact speedUnbounded_add_subleading u w hu
    ⟨α, C, hα, hsmall, hC, hw⟩

example (u w : VelocityField) (hu : SpeedUnboundedAtOne u)
    (B : ℝ) (hB : 0 ≤ B)
    (hw : ∀ t ∈ Ioo (0 : ℝ) 1, ∀ x : Space, ‖w (t, x)‖ ≤ B) :
    SpeedUnboundedAtOne (u + w) := by
  exact speedUnbounded_add_bounded u w hu ⟨B, hB, hw⟩

end UnforcedPatching

#print axioms UnforcedPatching.speedUnbounded_add_subleading
#print axioms UnforcedPatching.speedUnbounded_add_bounded
