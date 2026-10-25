import Mathlib

/-!
# Exact scalar gates for the Appendix-B outer pressure mixture

These finite rational facts do not formalize the positive-measure
representation, the holomorphic pressure tube, the contraction theorem,
or an unforced Navier--Stokes solution.
-/
namespace TerminalCore2026

theorem axis_pressure_root_left (D j : ℚ) :
    D*(-j/4)+(1-(-j/4)^2)*(4*(-j/4)+j) = -D*j/4 := by ring

theorem axis_pressure_root_right (D j : ℚ) :
    D*(-j/5)+(1-(-j/5)^2)*(4*(-j/5)+j) =
      j*(1-D-j^2/25)/5 := by ring

theorem pressure_axis_secant (D j x y : ℚ) :
    (D*x+(1-x^2)*(4*x+j))-(D*y+(1-y^2)*(4*y+j)) =
    (x-y)*(D+4-4*(x^2+x*y+y^2)-j*(x+y)) := by ring

theorem pressure_B2_gap : (144:ℚ)/145 > 99/100 := by norm_num

theorem pressure_root_positive_gap :
    (1:ℚ)/2*(1-2/7) > 1/3 := by norm_num

theorem pressure_secant_endpoint_right :
    (49:ℚ)/100-4*(1/80)^2-1/20 > 2/5 := by norm_num

theorem pressure_secant_endpoint_left :
    (49:ℚ)/100-4*(1/80)^2 > 2/5 := by norm_num

theorem pressure_Z_derivative_polynomial :
    (51:ℚ)/100*((2*(81/20)+8)*(81/20)+(1+2*(81/20))*4)
     +4*(83/5)<120 := by norm_num

theorem pressure_Z_derivative_trace :
    (2:ℚ)*2+8+4*(51/100)+4*(51/100)*2<20 := by norm_num

#print axioms axis_pressure_root_left
#print axioms axis_pressure_root_right
#print axioms pressure_axis_secant
#print axioms pressure_B2_gap
#print axioms pressure_Z_derivative_polynomial

end TerminalCore2026
