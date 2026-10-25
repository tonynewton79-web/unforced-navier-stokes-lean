import Mathlib

/-!
# Direct pressure-source gates in the shifted analytic norm

Exact scalar inequalities for the axis primitive, radial-Laplacian
cancellation, and time-transport pressure normal form. Not an
end-to-end Lean Banach-space theorem or Navier--Stokes solution.
-/
namespace TerminalCore2026

theorem shifted_pressure_primitive_polynomial (a : ℝ) :
    4*(a+1)^3*(2*a+3)-3*(a+2)^2 =
      a*(8*a^3+36*a^2+57*a+32) := by
  ring

theorem shifted_time_zero_jet_polynomial (a : ℝ) :
    4*(a+1)^2*(2*a+3)-3*(a+2)^2 =
      a*(8*a^2+25*a+20) := by
  ring

theorem shifted_pressure_primitive_gate (a : ℝ) (ha : 0 ≤ a) :
    3*(a+2)^2 ≤ 4*(a+1)^3*(2*a+3) := by
  have hp : 0 ≤ a*(8*a^3+36*a^2+57*a+32) := by positivity
  nlinarith [shifted_pressure_primitive_polynomial a]

theorem shifted_time_zero_gate (a : ℝ) (ha : 0 ≤ a) :
    3*(a+2)^2 ≤ 4*(a+1)^2*(2*a+3) := by
  have hp : 0 ≤ a*(8*a^2+25*a+20) := by positivity
  nlinarith [shifted_time_zero_jet_polynomial a]

theorem shifted_pressure_laplacian_gate (a b : ℝ)
    (ha : 0 ≤ a) (hb : 0 ≤ b) :
    (a+1)*(b+2)^2 ≤ 4*(b+1)^2*(2*a+b+1) := by
  have h1 : a+1 ≤ 2*a+b+1 := by linarith
  have h2 : (b+2)^2 ≤ 4*(b+1)^2 := by
    nlinarith [sq_nonneg b]
  calc
    (a+1)*(b+2)^2 ≤ (2*a+b+1)*(b+2)^2 :=
      mul_le_mul_of_nonneg_right h1 (sq_nonneg _)
    _ ≤ (2*a+b+1)*(4*(b+1)^2) :=
      mul_le_mul_of_nonneg_left h2 (by linarith)
    _ = 4*(b+1)^2*(2*a+b+1) := by ring

theorem shifted_pressure_laplacian_source_identity
    (r alpha B G f df : ℝ) (hr : r ≠ 0) :
    r*(alpha*B*f-G*df/r) = r*alpha*B*f-G*df := by
  field_simp

theorem shifted_pressure_time_source_identity
    (r q Linv H alpha B dB G dG f df ddf : ℝ) (hr : r ≠ 0) :
    -(1/(2*r))*
      ((r-q)*Linv*(alpha*B*f-G*df/r) +
       H*(alpha*dB*f+alpha*B*df-dG*df/r-G*ddf/r)) =
    -(1/(2*r))*
      (((r-q)*Linv*alpha*B+H*alpha*dB)*f +
       (-(r-q)*Linv*G/r+H*(alpha*B-dG/r))*df +
       (-H*G/r)*ddf) := by
  field_simp
  ring

#print axioms shifted_pressure_primitive_gate
#print axioms shifted_time_zero_gate
#print axioms shifted_pressure_laplacian_gate
#print axioms shifted_pressure_laplacian_source_identity
#print axioms shifted_pressure_time_source_identity

end TerminalCore2026
