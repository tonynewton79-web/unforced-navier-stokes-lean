import Mathlib
/-!
Finite scalar gates for Appendix A.5 of the originating Navier--Stokes
source. No new axioms or sorry. The analytic sigmoid, moment integrals,
full stress cone and unforced PDE are NOT Lean-formalized.
-/
namespace TerminalCore2026
theorem pulse_main_second_derivative_constant :
    (50:ℚ)*64+2*64+11*17152=192000 := by norm_num
theorem pulse_sigmoid_central_second_budget :
    ((256:ℚ)^2+3072)/4=17152 := by norm_num
theorem pulse_sigmoid_tail_polynomial_budget :
    (4:ℚ)*4^6+6*4^4+20*4^3+44=19244 := by norm_num
theorem pulse_taylor_rational_budget :
    (192000:ℚ)*(1011/1000)*(20/9)^3<2131000 := by norm_num
theorem pulse_first_quadratic_max (R : ℝ) :
    -2*R^2+(241/100)*R ≤ 58081/80000 := by
  nlinarith [sq_nonneg (R-241/400)]
theorem pulse_second_quadratic_max (R : ℝ) :
    -(7/2)*R^2+(241/50)*R ≤ 58081/35000 := by
  nlinarith [sq_nonneg (R-241/350)]
theorem pulse_exact_shear_identity (lam R Rp : ℝ) :
    -(1+2*lam)*R+2*lam*Rp+R=2*lam*(Rp-R) := by ring
theorem pulse_Cd_rational_budget :
    ((1/2:ℚ)*(10000/9999))/((1/2-1/2000000000)^2)
     < 2001/1000 := by norm_num
theorem pulse_first_margin_budget :
    (58081:ℚ)/80000+1512/1000000+1/1000000000000
     < 74/100 := by norm_num
theorem pulse_second_margin_budget :
    (58081:ℚ)/35000+2*(1/2000000000)*1500^2+
    3336/1000000+4/1000000000000 < 168/100 := by norm_num
theorem pulse_axial_shear_gate :
    (1453:ℚ)/2000000000 < 1/1000000 := by norm_num
#print axioms pulse_main_second_derivative_constant
#print axioms pulse_first_quadratic_max
#print axioms pulse_second_quadratic_max
#print axioms pulse_exact_shear_identity
#print axioms pulse_first_margin_budget
#print axioms pulse_second_margin_budget
end TerminalCore2026