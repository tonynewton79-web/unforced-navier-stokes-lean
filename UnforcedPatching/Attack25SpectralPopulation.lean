import Mathlib

/-!
# Attack 25: conditional spectral-population necessity

This is a finite-family Cauchy--Schwarz certificate.  To apply it to a
smooth periodic Navier--Stokes solution, a separate theorem must establish
Fourier reconstruction, absolutely summable modal amplitudes and Parseval.
The exponent is a necessary condition, never a construction of a cascade.
-/

namespace UnforcedPatching

/-- Finite Cauchy--Schwarz: squared modal L1 mass costs at most N times
the squared modal L2 mass. -/
theorem finite_spectral_participation_bound
    {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (a : ι → ℝ) (E : ℝ)
    (henergy : (∑ i ∈ s, (a i)^2) ≤ E) :
    (∑ i ∈ s, |a i|)^2 ≤ (s.card : ℝ) * E := by
  calc
    (∑ i ∈ s, |a i|)^2 ≤
        (s.card : ℝ) * (∑ i ∈ s, (a i)^2) := by
      simpa only [sq_abs] using
        (sq_sum_le_card_mul_sum_sq (s := s) (f := fun i => |a i|))
    _ ≤ (s.card : ℝ) * E :=
      mul_le_mul_of_nonneg_left henergy (by positivity)

/-- Any physical peak bounded above by the sum of absolute Fourier
amplitudes requires a sufficiently large effective population. -/
theorem finite_peak_requires_modal_population
    {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (a : ι → ℝ) (E peak : ℝ)
    (hpeak : 0 ≤ peak)
    (hpeakL1 : peak ≤ ∑ i ∈ s, |a i|)
    (henergy : (∑ i ∈ s, (a i)^2) ≤ E) :
    peak^2 ≤ (s.card : ℝ) * E := by
  have hmass : 0 ≤ ∑ i ∈ s, |a i| := by
    apply Finset.sum_nonneg
    intro i hi
    exact abs_nonneg (a i)
  have hdiff : 0 ≤ (∑ i ∈ s, |a i|) - peak :=
    sub_nonneg.mpr hpeakL1
  have hsum : 0 ≤ (∑ i ∈ s, |a i|) + peak :=
    add_nonneg hmass hpeak
  have hprod := mul_nonneg hdiff hsum
  have hsq : peak^2 ≤ (∑ i ∈ s, |a i|)^2 := by
    nlinarith
  exact le_trans hsq
    (finite_spectral_participation_bound s a E henergy)

/-- If E>0, the quantitative lower bound on modal cardinality. -/
theorem finite_population_card_lower
    {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (a : ι → ℝ) (E peak : ℝ)
    (hE : 0 < E)
    (hpeak : 0 ≤ peak)
    (hpeakL1 : peak ≤ ∑ i ∈ s, |a i|)
    (henergy : (∑ i ∈ s, (a i)^2) ≤ E) :
    peak^2 / E ≤ (s.card : ℝ) := by
  apply (div_le_iff₀ hE).2
  simpa only [mul_comm] using
    finite_peak_requires_modal_population s a E peak hpeak hpeakL1 henergy

/-- If squared energy scales as tau^(1/5) and the speed lower bound
has exponent 3/5, the necessary Fourier participation exponent is 7/5.
The scale assumptions themselves are NOT established by this theorem. -/
theorem terminal_population_power :
    (2 * (3 / 5 : ℚ) + 1 / 5 = 7 / 5) ∧
    (2 * ((1 / 2 : ℚ) + 1 / 10) + 1 / 5 = 7 / 5) := by
  norm_num

#print axioms finite_spectral_participation_bound
#print axioms finite_peak_requires_modal_population
#print axioms finite_population_card_lower
#print axioms terminal_population_power

end UnforcedPatching
