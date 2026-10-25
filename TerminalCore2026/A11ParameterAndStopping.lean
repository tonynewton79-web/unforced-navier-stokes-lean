import Mathlib

/-! Finite rational gates for true Appendix A.11 parameter derivatives
and the terminal Q matching interval. The analytic ODE, integrals
and full Navier--Stokes PDE are NOT formalized here. -/
namespace TerminalCore2026

theorem A11_eta_discrepancy_margin :
    (1050:ℚ)/289 < 4 := by norm_num

theorem A11_eta_jacobian_small :
    (3/2:ℚ)*640*192*(1/20)^28 < 1/2 := by norm_num

theorem A11_eta_slope_derivative_margin :
    (2:ℚ)*200000*12 +
    4*200000*192*(640/3)*12*(1/20)^28 < 5000000 := by norm_num

theorem A11_terminal_Qp_upper_margin :
    (21:ℚ)*(1/256)/(1-(1/256)*(1/100)) < 1/10 := by norm_num

theorem A11_terminal_Qstart_lower_margin :
    (16:ℚ)/3*(1-1/100) > 5 := by norm_num

theorem A11_terminal_cutoff_ratio_positive (h:ℝ)
    (hh:0<h) (hmax:h≤1/100) :
    0 < 1-(1/256)*h := by
  linarith

#print axioms A11_eta_discrepancy_margin
#print axioms A11_eta_jacobian_small
#print axioms A11_eta_slope_derivative_margin
#print axioms A11_terminal_Qp_upper_margin
#print axioms A11_terminal_Qstart_lower_margin

end TerminalCore2026