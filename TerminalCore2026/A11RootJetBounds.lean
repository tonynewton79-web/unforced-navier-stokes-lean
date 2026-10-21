import Mathlib

/-!
Scalar A.11 root/derivative proof gates, NOT an end-to-end unforced PDE proof.
No sorry or user-defined axioms. Full source A.10 ODE and pressure gauges
are not formalized here.
-/
namespace TerminalCore2026

def rootPoly (v w x z k t : ℝ) : ℝ :=
  2*v*(k-x*t+z*t)+w*((k-x*t)^2+z*t^2)

theorem rootPoly_explicit (v w x z k t : ℝ) :
    rootPoly v w x z k t =
      w*(x^2+z)*t^2+(2*v*(z-x)-2*w*x*k)*t+
      (2*v*k+w*k^2) := by
  unfold rootPoly
  ring

theorem jet_second_row (v w z c1 c2 d1 d2 : ℝ) :
    (2*v+2*w*c1)*d1+(2*v*z+2*w*z*c2)*d2 =
      2*v*(d1+z*d2)+2*w*(c1*d1+z*c2*d2) := by
  ring

theorem rootjet_contraction_rational :
    (1920:ℚ)/(100:ℚ)^28 < 1/100 := by norm_num

theorem rootjet_selfmap_rational :
    (3/2:ℚ)*(63/100)+(1920:ℚ)/(100:ℚ)^28 < 2 := by
  norm_num

theorem rootjet_delta_derivative_rational :
    (20/17:ℚ)*21/100 < 1/4 := by norm_num

theorem rootjet_eta_inverse_rational :
    (3/2:ℚ)/(1-1/100)*(1/4) = 25/66 ∧
      (25/66:ℚ) < 1 := by
  constructor <;> norm_num

theorem rootjet_hull_delta_rational :
    (640/3:ℚ)*2 = 1280/3 := by norm_num

#print axioms rootPoly_explicit
#print axioms jet_second_row
#print axioms rootjet_contraction_rational
#print axioms rootjet_selfmap_rational
#print axioms rootjet_delta_derivative_rational
#print axioms rootjet_eta_inverse_rational

end TerminalCore2026
