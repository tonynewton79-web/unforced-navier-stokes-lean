import Mathlib
/-! Finite algebraic scalar gates for Appendix-A axial pulse transfers.
    Full integral and PDE statements remain unformalized. -/
namespace TerminalCore2026
theorem pulse_decay_coefficients (lam:ℝ) (hl0:0<lam)
    (hls:lam≤1/20) :
    0<(1/2:ℝ)-lam ∧ 0<(1/2:ℝ)-2*lam ∧
    0<(1:ℝ)-lam ∧ 0<(1:ℝ)+2*lam := by
  constructor <;> try constructor <;> linarith
theorem pulse_i_equilibrium (lam:ℝ) (h:1-lam≠0) :
    (1-lam)*(1/(1-lam))=(1:ℝ) := by
  field_simp
theorem pulse_p_equilibrium (lam:ℝ) (h:1+2*lam≠0) :
    (1+2*lam)*(-1/(2*(1+2*lam)))=-(1/2:ℝ) := by
  field_simp
  ring
theorem pulse_end_rescaled_length (lam:ℝ) (h:lam≠0) :
    lam*(13/lam)=(13:ℝ) := by field_simp
#print axioms pulse_decay_coefficients
#print axioms pulse_i_equilibrium
#print axioms pulse_p_equilibrium
#print axioms pulse_end_rescaled_length
end TerminalCore2026