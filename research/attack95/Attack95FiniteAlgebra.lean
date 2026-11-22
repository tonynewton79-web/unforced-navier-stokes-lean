import Mathlib

/-!
Attack95 finite algebraic statements only. The continuum source-curl
compatibility, smooth compact multiplier, and ninth-jet functional
analysis are proved in the accompanying paper, NOT formalized here.
-/
namespace UnforcedPatching.Attack95

theorem swirl_square_change (u w : ℝ) :
    (u+w)^2-u^2=2*u*w+w^2 := by
  ring

theorem multiplier_amplitude_exact :
    (60:ℚ)^5/(61:ℚ)^5 = 777600000/844596301 := by
  norm_num

theorem multiplier_amplitude_drop :
    (1:ℚ) - (60:ℚ)^5/(61:ℚ)^5 > 79/1000 := by
  norm_num

theorem compact_shear_shift (a : ℝ) (ha : 0 < a) (hb : a < 4/5) :
    10 < a+10 ∧ a+10 < 54/5 := by
  constructor <;> linarith

theorem two_moment_determinant_factor
    (m1 m2 g1 g2 : ℝ) :
    m1*(m2*g2)-m2*(m1*g1) = m1*m2*(g2-g1) := by
  ring

theorem fixed_shape_velocity_ninth_exponent (h : ℝ) :
   -(1/2+h)-9/2+(1+(1/2-h))/2 = -17/4-3*h/2 := by
  ring

theorem fixed_shape_heat_ninth_exponent (h : ℝ) :
   -(1/2+h)-1-9/2+(1+(1/2-h))/2 = -21/4-3*h/2 := by
  ring

theorem meridional_curl_scale_exponent (h : ℝ) :
   -2*(1/2+h)-1/2-(1/2-h) = -2-h := by
  ring

#print axioms swirl_square_change
#print axioms multiplier_amplitude_exact
#print axioms multiplier_amplitude_drop
#print axioms compact_shear_shift
#print axioms two_moment_determinant_factor
#print axioms fixed_shape_velocity_ninth_exponent
#print axioms fixed_shape_heat_ninth_exponent
#print axioms meridional_curl_scale_exponent

end UnforcedPatching.Attack95
