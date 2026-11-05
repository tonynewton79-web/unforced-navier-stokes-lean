import Mathlib

/-!
# Attack 21: moving packet scalar exponents and variance floor

Only exact rational powers, a finite two-weight variance implication, and
scalar calibration identities are formalized. The full Gaussian series,
carrier energy estimates, and projected Navier--Stokes PDE are separate open
Lean obligations.
-/

namespace UnforcedPatching

theorem packet_power_ledger :
    (1 / 10 : ℚ) - 1 - 9 / 20 = -(27 / 20 : ℚ) ∧
    (1 / 10 : ℚ) - 2 * (9 / 20 : ℚ) = -(4 / 5 : ℚ) ∧
    (1 / 5 : ℚ) - 9 / 20 = -(1 / 4 : ℚ) ∧
    -(27 / 20 : ℚ) < -(4 / 5 : ℚ) ∧
    -(4 / 5 : ℚ) < -(1 / 4 : ℚ) := by
  norm_num

theorem packet_frequency_window :
    (11 / 25 : ℚ) < 9 / 20 ∧ (9 / 20 : ℚ) < 1 / 2 := by
  norm_num

/-- A lower bound on the probability at two neighbouring integer modes
forces a variance floor once their pair contribution is included. -/
theorem positive_pair_variance_floor
    (p q variance : ℝ)
    (hp : (1 / 15 : ℝ) ≤ p) (hq : (1 / 15 : ℝ) ≤ q)
    (hvar : p * q ≤ variance) :
    (1 / 225 : ℝ) ≤ variance := by
  have hprod : 0 ≤ (p - 1 / 15) * (q - 1 / 15) := by
    apply mul_nonneg <;> linarith
  nlinarith

/-- The scalar calibration gives the exact target Rayleigh ratio.
The physical identification of D0 and M0 is NOT certified here. -/
theorem calibrated_rayleigh_scalar
    (D0 M0 y0 : ℝ) (hD : 0 < D0)
    (hy : y0 = 10 * D0 - M0) :
    D0 / (M0 + y0) = (1 / 10 : ℝ) := by
  rw [hy]
  have h : (10 : ℝ) * D0 ≠ 0 := ne_of_gt (by positivity)
  field_simp
  ring

theorem halo_energy_leading_positive
    (D0 M0 : ℝ) (hM : 0 < M0)
    (hRadial : (6 / 5 : ℝ) * M0 ≤ D0) :
    11 * M0 ≤ 10 * D0 - M0 := by
  linarith

#print axioms packet_power_ledger
#print axioms packet_frequency_window
#print axioms positive_pair_variance_floor
#print axioms calibrated_rayleigh_scalar
#print axioms halo_energy_leading_positive

end UnforcedPatching
