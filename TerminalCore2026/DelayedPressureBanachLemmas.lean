import Mathlib

/-!
# Scalar gates for the complete variable-coefficient delayed-pressure operator

These finite lemmas formalize the order/valuation and Leibniz inequalities
used in the analytic norm proof for the linear
U_(n-2) -> V_(n-2) -> Omega_(n-1) -> Pi_n -> U_n channel.

The full analytic Banach-space theorem, the source-leading profiles and
the Navier--Stokes recurrence are NOT kernel-formalized here.
-/
namespace TerminalCore2026

/-- The radial valuation dominates the expansion and radial indices. -/
theorem delayed_pressure_index_control (a n : ℝ)
    (ha : 0 ≤ a) (hn : 2 ≤ n) (hvaluation : n ≤ a+2) :
    a+n+1 ≤ 3*(a+1) := by
  linarith

/-- Exact Leibniz-weight polynomial correction bound. -/
theorem delayed_pressure_leibniz_window (b ell : ℝ)
    (hb : 0 ≤ b) (hell : 0 ≤ ell) (hle : ell ≤ b) :
    b+1 ≤ (ell+1)*(b-ell+1) := by
  have h1 : 0 ≤ b-ell := by linarith
  have hp : 0 ≤ ell*(b-ell) := mul_nonneg hell h1
  nlinarith [hp]

/-- Cauchy-radius loss and analytic coefficient bounds yield
a factor at most 87 per shifted Z composition. -/
theorem delayed_pressure_composition_step
    (C X Y : ℝ) (hC : 0 ≤ C)
    (hX : 0 ≤ X) (hXupper : X ≤ 13)
    (hY : 0 ≤ Y) (hYupper : Y ≤ 22) :
    (X+4*X+Y)*C ≤ 87*C := by
  have hstep : X+4*X+Y ≤ 87 := by linarith
  exact mul_le_mul_of_nonneg_right hstep hC

/-- Explicit bound on all normal-form coefficient functions. -/
theorem delayed_pressure_symbol_constant :
    22 * (87 : ℕ)^3 = 14487066 := by norm_num

#print axioms delayed_pressure_index_control
#print axioms delayed_pressure_leibniz_window
#print axioms delayed_pressure_composition_step
#print axioms delayed_pressure_symbol_constant

end TerminalCore2026
