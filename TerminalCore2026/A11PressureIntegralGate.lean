import Mathlib

/-! A.11 pressure normalization: conditional exact Lean implications.
The actual prescribed support integrals, corrected roots and full PDE
are not formalized here. -/
open MeasureTheory
noncomputable section
namespace TerminalCore2026

theorem terminal_pressure_of_equal_integrals
    (Eref Ec : ℝ → ℝ)
    (hneutral : (∫ y : ℝ, Ec y ^ 2) = (∫ y : ℝ, Eref y ^ 2)) :
    -(∫ y : ℝ, Eref y ^ 2) / 2 +
      (∫ y : ℝ, Ec y ^ 2) / 2 = 0 := by
  rw [hneutral]
  ring

theorem source_A11_terminal_pressure
    (Iref Icorrected P0 E1sq R2 : ℝ)
    (href : P0 = -(Iref / 2))
    (hfactor : Icorrected - Iref = E1sq * R2)
    (hneut : R2 = 0) :
    P0 + Icorrected / 2 = 0 := by
  have heq : Icorrected = Iref := by
    rw [hneut] at hfactor
    nlinarith [hfactor]
  rw [href, heq]
  ring

theorem source_A11_terminal_pressure_derivative
    (P : ℝ → ℝ) (hzero : ∀ η : ℝ, P η = 0) (η : ℝ) :
    deriv P η = 0 := by
  have heq : P = fun _ : ℝ => (0 : ℝ) := by
    funext x
    exact hzero x
  rw [heq]
  simp

theorem amplitude_only_is_insufficient :
    (2 : ℚ) * ((1 / 10 : ℚ) + (1 / 8 : ℚ) * 0) +
      20 * ((1 / 10 : ℚ)^2 + (1 / 8 : ℚ) * 0^2) = 2 / 5 := by
  norm_num

#print axioms terminal_pressure_of_equal_integrals
#print axioms source_A11_terminal_pressure
#print axioms source_A11_terminal_pressure_derivative
#print axioms amplitude_only_is_insufficient
end TerminalCore2026
