import Mathlib
/-! Scalar gates for the exact-rational 8+2 source moment enclosure theorem.
    Actual source ODE comparisons and the unforced PDE are not formalized. -/
namespace TerminalCore2026
theorem ten_state_reference_i_stationary :
    (1:ℝ)-((3/5:ℝ)+1)*(5/8)=0 := by norm_num
theorem ten_state_reference_s_stationary :
    (0:ℝ)^2-1/2-2*(3/5:ℝ)*(-(5/12))=0 := by norm_num
theorem ten_state_pressure_tail_equilibrium (h:ℝ) (hh:1+2*h≠0) :
    -(1/2:ℝ)+(2*(-h)-1)*(-1/(2*(1+2*h)))=0 := by
  field_simp
  ring
theorem ten_state_scalar_tube (M B L d S V:ℝ)
    (hd:0≤d) (hL:0≤L) (hsmall:d*L<1)
    (hS:M+d*B≤(1-d*L)*S)
    (hV:V≤M+d*(L*V+B)) : V≤S := by
  by_contra hbad
  have hp:0<1-d*L := by linarith
  have hv:0<V-S := by linarith
  have prod:=mul_pos hp hv
  nlinarith
#print axioms ten_state_reference_i_stationary
#print axioms ten_state_reference_s_stationary
#print axioms ten_state_pressure_tail_equilibrium
#print axioms ten_state_scalar_tube
end TerminalCore2026