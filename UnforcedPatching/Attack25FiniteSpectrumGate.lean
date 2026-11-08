import Mathlib

/-!
# Attack 25: finite-band obstruction and carrier-coupling norm gate

Both theorems are independent of any alleged 3D blow-up solution.

* No finite Fourier Galerkin support with a uniform squared-coefficient
  energy bound can produce unbounded Fourier coefficients.
* If a projected carrier-coupling term is smaller than the prescribed
  first-generation source in norm, it cannot cancel it exactly.

The first is a finite-sum estimate. It is not, by itself, a PDE theorem
about uniform physical speed; that further step needs the Fourier
reconstruction/Parseval bridge and uniform support cardinality.
-/

namespace UnforcedPatching

/-- A positive initial source survives any smaller coupling perturbation.
This is the exact abstract form of the carrier-inclusive source gate. -/
theorem carrier_coupling_norm_lower
    {X : Type*} [NormedAddCommGroup X]
    (source coupling : X) :
    ‖source‖ - ‖coupling‖ ≤ ‖source + coupling‖ := by
  have h : ‖source‖ ≤ ‖source + coupling‖ + ‖coupling‖ := by
    calc
      ‖source‖ = ‖(source + coupling) - coupling‖ := by
        congr 1
        abel
      _ ≤ ‖source + coupling‖ + ‖coupling‖ := norm_sub_le _ _
  linarith

/-- The actual projected forcing cannot vanish whenever the carrier
coupling is strictly smaller than the isolated source. -/
theorem carrier_coupling_strictly_nonzero
    {X : Type*} [NormedAddCommGroup X]
    (source coupling : X)
    (hsmall : ‖coupling‖ < ‖source‖) :
    source + coupling ≠ 0 := by
  intro hz
  have h := carrier_coupling_norm_lower source coupling
  rw [hz, norm_zero] at h
  linarith

/-- Each Fourier coordinate is controlled by the finite total energy.
No assumption about the Navier--Stokes PDE is inserted. -/
theorem finite_modal_energy_controls_coordinate
    {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (a : ι → ℝ) (E : ℝ)
    (henergy : (∑ i ∈ s, (a i)^2) ≤ E)
    (k : ι) (hk : k ∈ s) :
    (a k)^2 ≤ E := by
  have hterm : (a k)^2 ≤ ∑ i ∈ s, (a i)^2 :=
    Finset.single_le_sum (fun i hi => sq_nonneg (a i)) hk
  exact le_trans hterm henergy

/-- This modest L-infinity consequence is enough to rule out blowup of
a coefficient on a *fixed finite support* and a uniform finite
energy budget. The constant E+1 is nonoptimal but elementary. -/
theorem finite_modal_energy_controls_absolute_coefficient
    {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (a : ι → ℝ) (E : ℝ)
    (hE : 0 ≤ E)
    (henergy : (∑ i ∈ s, (a i)^2) ≤ E)
    (k : ι) (hk : k ∈ s) :
    |a k| ≤ E + 1 := by
  have hsq := finite_modal_energy_controls_coordinate s a E henergy k hk
  have hupper : a k ≤ E + 1 := by
    nlinarith [sq_nonneg (a k - 1)]
  have hlower : -(E + 1) ≤ a k := by
    nlinarith [sq_nonneg (a k + 1)]
  exact abs_le.mpr ⟨hlower, hupper⟩

/-- Fixed-support modal blowup would demand arbitrarily large Fourier
coordinates before the terminal time. -/
def FixedSupportModalBlowup
    {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (a : ℝ → ι → ℝ) : Prop :=
  ∀ M : ℝ, ∃ t ∈ Set.Ioo (0 : ℝ) 1,
    ∃ k ∈ s, M < |a t k|

/-- A uniform modal-energy budget precludes fixed-support modal blowup.
Any claimed singular Fourier cascade needs unbounded support or a
violation of the assumed energy bound. -/
theorem energy_bounded_fixed_support_no_modal_blowup
    {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (a : ℝ → ι → ℝ) (E : ℝ)
    (hE : 0 ≤ E)
    (henergy : ∀ t ∈ Set.Ioo (0 : ℝ) 1,
      (∑ k ∈ s, (a t k)^2) ≤ E) :
    ¬ FixedSupportModalBlowup s a := by
  intro hblow
  obtain ⟨t, ht, k, hk, hlarge⟩ := hblow (E + 1)
  have hbound :=
    finite_modal_energy_controls_absolute_coefficient
      s (a t) E hE (henergy t ht) k hk
  linarith

/-- Correct 2π-dependent receiver threshold:
40π J A B C > 240νπ² J² C²
forces AB > 6πν J C when J,C,ν are positive. -/
theorem exact_viscous_receiver_gain_implies_threshold
    (J A B C nu : ℝ)
    (hJ : 0 < J) (hC : 0 < C) (hnu : 0 < nu)
    (hgain : 0 <
      40 * Real.pi * J * A * B * C -
        240 * nu * Real.pi^2 * J^2 * C^2) :
    6 * Real.pi * nu * J * C < A * B := by
  have hfactor : 0 < 40 * Real.pi * J * C := by
    positivity
  have hfactorization :
      40 * Real.pi * J * A * B * C -
        240 * nu * Real.pi^2 * J^2 * C^2 =
        (40 * Real.pi * J * C) *
          (A * B - 6 * Real.pi * nu * J * C) := by
    ring
  rw [hfactorization] at hgain
  have hdiff : 0 < A * B - 6 * Real.pi * nu * J * C := by
    by_contra hn
    have hle : A * B - 6 * Real.pi * nu * J * C ≤ 0 :=
      le_of_not_gt hn
    have hbad := mul_nonpos_of_nonneg_of_nonpos
      (le_of_lt hfactor) hle
    exact (not_lt.mpr hbad) hgain
  nlinarith

#print axioms carrier_coupling_norm_lower
#print axioms carrier_coupling_strictly_nonzero
#print axioms finite_modal_energy_controls_coordinate
#print axioms finite_modal_energy_controls_absolute_coefficient
#print axioms energy_bounded_fixed_support_no_modal_blowup
#print axioms exact_viscous_receiver_gain_implies_threshold

end UnforcedPatching
