import Mathlib

/-! Conditional A11/A19 finite dimensional algebra.
No source root existence or PDE proof is claimed. -/
namespace TerminalCore2026

theorem a11_a19_block_det
    (u v w x z q1 q2 k2 k1 A : ℝ) :
    (u*(2*z*(v+w*q2))-(u*x)*(2*(v+w*q1)))*(2*k2*A+k1) =
    2*u*(z*(v+w*q2)-x*(v+w*q1))*(2*k2*A+k1) := by
  ring

theorem a11_pressure_square_expansion
    (E2 v w z q1 q2 : ℝ) :
    E2*(2*v*(q1+z*q2)+w*(q1^2+z*q2^2)) =
    E2*(2*v*q1+2*v*z*q2+w*q1^2+w*z*q2^2) := by
  ring

theorem a19_discriminant_root_identity
    (k2 k1 k0 A : ℝ)
    (hroot : k2*A^2+k1*A+k0=0) :
    (2*k2*A+k1)^2=k1^2-4*k2*k0 := by
  have h : k2*A^2+k1*A=-k0 := by linarith
  calc
    (2*k2*A+k1)^2 = k1^2+4*k2*(k2*A^2+k1*A) := by ring
    _ = k1^2-4*k2*k0 := by rw [h]; ring

theorem a11_pressure_negative_control :
    (2*(1 : ℚ)*((1/10)+(1/8)*0)+
      20*((1/10)^2+(1/8)*0^2)) = 2/5 := by
  norm_num

#print axioms a11_a19_block_det
#print axioms a11_pressure_square_expansion
#print axioms a19_discriminant_root_identity
#print axioms a11_pressure_negative_control
end TerminalCore2026
