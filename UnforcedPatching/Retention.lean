import UnforcedPatching.Correction
import Mathlib.Tactic

/-!
# Terminal speed retention under a subleading physical correction

This is a conditional step toward gate G7. It certifies that a correction
cannot erase unbounded terminal speed when its magnitude is strictly below
the leading magnitude, up to a fixed additive allowance. It supplies
neither the leading field nor a correction solving the Navier--Stokes PDE.
-/

noncomputable section

namespace UnforcedPatching

open NavierStokes.ProblemStatement
open Set

/-- Quantitative terminal subleadingness on the physical time interval.
The strict `α < 1` prevents a correction `w = -u` from cancelling the
leading singular trace. No such estimate is asserted to hold for H8. -/
def SubleadingCorrectionBound (u w : VelocityField) : Prop :=
  ∃ α C : ℝ, 0 ≤ α ∧ α < 1 ∧ 0 ≤ C ∧
    ∀ t ∈ Ioo (0 : ℝ) 1, ∀ x : Space,
      ‖w (t, x)‖ ≤ α * ‖u (t, x)‖ + C

/-- A uniform physical correction bound is a special case of a subleading
bound with coefficient `α = 0`. -/
def UniformCorrectionBound (w : VelocityField) : Prop :=
  ∃ B : ℝ, 0 ≤ B ∧
    ∀ t ∈ Ioo (0 : ℝ) 1, ∀ x : Space, ‖w (t, x)‖ ≤ B

/-- If an underlying velocity has arbitrarily large speed near time one,
then an `α < 1` relative correction cannot cancel that growth. The proof
uses the actual physical `SpeedUnboundedAtOne` endpoint quantifiers. -/
theorem speedUnbounded_add_subleading (u w : VelocityField)
    (hu : SpeedUnboundedAtOne u)
    (hw : SubleadingCorrectionBound u w) :
    SpeedUnboundedAtOne (u + w) := by
  obtain ⟨α, C, hα, hαone, hC, hrel⟩ := hw
  intro M hM δ hδ
  have hden : 0 < 1 - α := sub_pos.mpr hαone
  have hnum : 0 < M + C := add_pos_of_pos_of_nonneg hM hC
  obtain ⟨t, x, ht, hnear, hlarge⟩ :=
    hu ((M + C) / (1 - α)) (div_pos hnum hden) δ hδ
  refine ⟨t, x, ht, hnear, ?_⟩
  have hleading : M + C < (1 - α) * ‖u (t, x)‖ := by
    simpa only [mul_comm] using (div_lt_iff₀ hden).mp hlarge
  have htriangle : ‖u (t, x)‖ ≤ ‖(u + w) (t, x)‖ + ‖w (t, x)‖ := by
    have hrewrite : u (t, x) = (u + w) (t, x) - w (t, x) := by
      simp only [Pi.add_apply]
      abel
    rw [hrewrite]
    exact norm_sub_le _ _
  have hcorrection := hrel t ht x
  nlinarith

/-- A globally bounded correction is in particular incapable of removing
unbounded terminal speed. This remains a *conditional* implication. -/
theorem speedUnbounded_add_bounded (u w : VelocityField)
    (hu : SpeedUnboundedAtOne u)
    (hw : UniformCorrectionBound w) :
    SpeedUnboundedAtOne (u + w) := by
  obtain ⟨B, hB, hb⟩ := hw
  apply speedUnbounded_add_subleading u w hu
  refine ⟨0, B, le_refl _, by norm_num, hB, ?_⟩
  intro t ht x
  simpa using hb t ht x

end UnforcedPatching
