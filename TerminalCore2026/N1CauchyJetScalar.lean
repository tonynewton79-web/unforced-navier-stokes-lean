import Mathlib
namespace TerminalCore2026
theorem cauchy_cube_gate (a B rho delta : ℝ)
    (ha : 0 < a) (hB : 0 < B) (hrho : 0 < rho)
    (hd : 0 ≤ delta)
    (hsmall : delta ≤ rho / 2)
    (hbudget : 12 * B * delta ≤ a * rho) :
    3 * B * delta / (rho - delta) ≤ a / 2 := by
  have hden : 0 < rho - delta := by linarith
  have hmul : 6 * B * delta ≤ a * rho / 2 := by
    nlinarith [hbudget]
  apply (div_le_iff₀ hden).2
  have hb0 : 0 ≤ a * delta := mul_nonneg (le_of_lt ha) hd
  nlinarith [hmul, hb0]
end TerminalCore2026
