import Mathlib

/-!
# Attack 19: finite Fourier spectral mass gate

For a finite frequency set, all positive modal energy at frequencies
tau * |xi|^2 >= 1 is controlled by tau times the dissipation.
This is an exact finite-sum inequality.  Passage to infinite Fourier sums,
periodic Parseval, and the physical Navier--Stokes energy identity remain
separate theorem obligations.  No singular solution is asserted.
-/

namespace UnforcedPatching

/-- Positive energy in the selected high-frequency modes cannot exceed
tau times the same modes' total dissipative cost. -/
theorem finite_high_frequency_energy_bound
    {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (a frequency : ι → ℝ)
    (tau D : ℝ)
    (htau : 0 ≤ tau)
    (ha : ∀ i ∈ s, 0 ≤ a i)
    (hfrequency : ∀ i ∈ s, 1 ≤ tau * frequency i)
    (hD : (∑ i ∈ s, frequency i * a i) ≤ D) :
    (∑ i ∈ s, a i) ≤ tau * D := by
  have hterm : ∀ i ∈ s, a i ≤ tau * (frequency i * a i) := by
    intro i hi
    have hmul := mul_le_mul_of_nonneg_right (hfrequency i hi) (ha i hi)
    nlinarith [hmul]
  calc
    (∑ i ∈ s, a i) ≤ (∑ i ∈ s, tau * (frequency i * a i)) := by
      apply Finset.sum_le_sum
      intro i hi
      exact hterm i hi
    _ = tau * (∑ i ∈ s, frequency i * a i) := by
      simp only [Finset.mul_sum]
    _ ≤ tau * D := mul_le_mul_of_nonneg_left hD htau

/-- Final spectral fraction comparison: the physical carrier exponent p
enters only through the separate energy-law hypothesis. -/
theorem high_frequency_fraction_of_dyadic_rate
    (E D H tau p epsilon : ℝ)
    (hE : 0 < E)
    (hH : 0 ≤ H)
    (hHigh : H ≤ tau * D)
    (hDyad : tau * D ≤ (p / 2 + epsilon) * E) :
    H / E ≤ p / 2 + epsilon := by
  have h : H ≤ (p / 2 + epsilon) * E := le_trans hHigh hDyad
  exact (div_le_iff₀ hE).2 (by simpa only [mul_comm] using h)

#print axioms finite_high_frequency_energy_bound
#print axioms high_frequency_fraction_of_dyadic_rate

end UnforcedPatching
