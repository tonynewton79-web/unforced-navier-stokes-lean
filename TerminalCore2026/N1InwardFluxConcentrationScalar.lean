import Mathlib

/-!
Edition XL: finite algebraic consequences only. The genuine
Navier--Stokes PDE, the smooth mild solution, Gaussian integrals,
radial energy inequalities and source singularity are NOT formalized.
-/
namespace TerminalCore2026

theorem xl_positive_core_torque (r : ℝ)
    (h0 : 0 < r) (h1 : r < 1) :
    0 < 4*r^2*(1-r^2) := by
  have hr2 : 0 < r^2 := sq_pos_of_pos h0
  have hrsmall : r^2 < 1 := by nlinarith
  have hdiff : 0 < 1-r^2 := by linarith
  positivity

theorem xl_inward_flux_sign (c r : ℝ)
    (hc : 0 < c) (hr : 0 < r) :
    -(c*r^4) < 0 := by
  have h4 : 0 < r^4 := pow_pos hr 4
  have hmul : 0 < c*r^4 := mul_pos hc h4
  linarith

theorem xl_energy_log_width (A width B : ℝ)
    (hA : 0 < A) (hbound : A*width ≤ B) :
    width ≤ B/A := by
  apply (le_div_iff₀ hA).2
  nlinarith

theorem xl_spike_radial_steepness (A B L : ℝ)
    (hA : 0 < A) (hB : 0 < B)
    (hL : L = 4*B/A) :
    ((3*A/4)/L) = 3*A^2/(16*B) := by
  rw [hL]
  field_simp [ne_of_gt hA, ne_of_gt hB]
  ring

theorem xl_flux_h2_exponent (h : ℝ)
    (hh : 0 < h) :
    (1:ℝ) < (4/3)*(1+h) := by
  linarith

#print axioms xl_positive_core_torque
#print axioms xl_inward_flux_sign
#print axioms xl_energy_log_width
#print axioms xl_spike_radial_steepness
#print axioms xl_flux_h2_exponent
end TerminalCore2026
