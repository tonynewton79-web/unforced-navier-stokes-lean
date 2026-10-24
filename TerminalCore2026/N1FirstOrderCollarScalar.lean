import Mathlib

/-! Edition VIII finite algebra of the first-order collar obstruction.
This does NOT formalize the full similarity-coordinate PDE or prove
Navier--Stokes blowup. -/
namespace TerminalCore2026

theorem a_z_at_symmetry_plane :
    (-2*(0:ℝ))/(1-2*(1/200:ℝ)*0^2)=0 := by norm_num

theorem b_z_at_symmetry_plane :
    (((-2*(1/2-(1/200:ℝ))*0*0)+(1-0^2)*(-2))/(1-2*(1/200:ℝ)*0^2))=-2 := by
  norm_num

theorem sigma_midpoint_prime_value : (1/4:ℚ)*32=8 := by
  norm_num

theorem outer_cutoff_midpoint_derivative (rho : ℝ) :
    rho / 2 * 8 = 4 * rho := by ring

theorem first_order_collar_exact (K scale rho : ℝ) :
    -(K*scale*(0^2 * (0:ℝ) + (-2)*(rho/2*8))) =
    8*K*scale*rho := by ring

theorem first_order_collar_strict
    (K scale rho : ℝ) (hK : 0 < K)
    (hs : 0 < scale) (hrho : 0 < rho) :
    0 < 8*K*scale*rho := by positivity

theorem no_zero_stress_if_nonzero_residual
    (residual stressDiv : ℝ)
    (hbalanced : stressDiv = -residual)
    (hres : 0 < residual) :
    stressDiv ≠ 0 := by
  intro hz
  rw [hz] at hbalanced
  linarith

#print axioms a_z_at_symmetry_plane
#print axioms b_z_at_symmetry_plane
#print axioms sigma_midpoint_prime_value
#print axioms outer_cutoff_midpoint_derivative
#print axioms first_order_collar_exact
#print axioms first_order_collar_strict
#print axioms no_zero_stress_if_nonzero_residual
end TerminalCore2026
