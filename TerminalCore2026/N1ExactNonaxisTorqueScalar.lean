import Mathlib

/-!
Edition XXXVII: only scalar algebraic identities derived from
the exact nonaxisymmetric Gaussian initial torque are formalized.
The Fourier existence theorem, physical Navier-Stokes evolution,
angular averaging and Reynolds-torque PDE are analytic inputs,
NOT Lean-kernel-certified by this file.
-/
namespace TerminalCore2026

theorem xxxvii_torque_polynomial (r : ℝ) :
    4*r^2*(r^2-1) = 4*r^4-4*r^2 := by
  ring

theorem xxxvii_half_radius_torque :
    (4:ℚ)*(1/2)^2*((1/2)^2-1) = -(3/4) := by
  norm_num

theorem xxxvii_small_data_picard (q : ℝ)
    (hq : q < 1/16) : 16*q < 1 := by
  linarith

theorem xxxvii_mean_momentum_generation
    (a g t : ℝ)
    (ht : 0 < t) (hg : 0 < g)
    (hder : a ≤ -(g/2)*t) : a < 0 := by
  have hn : -(g/2)*t < 0 := by positivity
  exact lt_of_le_of_lt hder hn

theorem xxxvii_nosource_retention
    (source actual bound : ℝ)
    (hu : actual ≤ bound)
    (hb : bound < source) :
    actual < source := by
  linarith

#print axioms xxxvii_torque_polynomial
#print axioms xxxvii_half_radius_torque
#print axioms xxxvii_small_data_picard
#print axioms xxxvii_mean_momentum_generation
#print axioms xxxvii_nosource_retention

end TerminalCore2026
